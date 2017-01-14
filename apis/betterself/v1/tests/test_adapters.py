from django.test import LiveServerTestCase
from django.test import TestCase

from apis.betterself.v1.adapters import BetterSelfAPIAdapter
from apis.betterself.v1.constants import VALID_REST_RESOURCES
from betterself.users.models import User
from supplements.fixtures.factories import IngredientFactory, IngredientCompositionFactory
from supplements.models import Ingredient, IngredientComposition
from vendors.fixtures.factories import VendorFactory
from vendors.models import Vendor

"""
This inherits LiveServerTestCase since we're spin up a port to listen and test
adapters responds correctly. Most of the tests here are functional and not pure unit
tests ,,, there's also some overlap with some of the more basic unit tests
"""

MOCK_VENDOR_NAME = 'MadScienceLabs'
MOCK_INGREDIENT_NAME = 'BCAA'

# python manage.py test apis.betterself.v1.tests.test_adapters


class AdapterTests(LiveServerTestCase, TestCase):
    @classmethod
    def setUpTestData(cls):
        default_user, _ = User.objects.get_or_create(username='default')
        VendorFactory(user=default_user, name=MOCK_VENDOR_NAME)
        ingredient = IngredientFactory(user=default_user, name=MOCK_INGREDIENT_NAME)
        IngredientCompositionFactory(user=default_user, ingredient=ingredient)

    def setUp(self):
        self.default_user, _ = User.objects.get_or_create(username='default')
        self.adapter = BetterSelfAPIAdapter(self.default_user)
        super().setUp()


class GenericAdapterTests(AdapterTests):
    def test_resources_get_on_adapter(self):
        for resource in VALID_REST_RESOURCES:
            response = self.adapter.get_resource_response(resource)
            self.assertEqual(response.status_code, 200)


class VendorAdapterTests(AdapterTests):
    def test_get_vendor_view_handles_empty_filter(self):
        parameters = {
            'name': 'FakeFakeVendor',
        }
        data = self.adapter.get_resource_data(Vendor, parameters=parameters)
        self.assertEqual(len(data), 0)

    def test_get_vendor_view_filters(self):
        parameters = {
            'name': MOCK_VENDOR_NAME,
        }
        data = self.adapter.get_resource_data(Vendor, parameters=parameters)
        self.assertEqual(len(data), 1)

    def test_post_on_vendor_resource(self):
        name = 'non_existent'
        email = 'somefakeemail@gmail.com'

        parameters = {
            'name': name,
            'email': email,
        }

        data = self.adapter.post_resource_data(Vendor, parameters)

        self.assertEqual(data['name'], name)
        self.assertEqual(data['email'], email)


class IngredientAdapterTests(AdapterTests):
    def test_get_ingredient_name_filter(self):
        parameters = {
            'name': MOCK_INGREDIENT_NAME,
        }
        data = self.adapter.get_resource_data(Ingredient, parameters=parameters)
        self.assertEqual(len(data), 1)

    def test_get_ingredient_empty_filter(self):
        parameters = {
            'name': 'non_existent',
        }
        data = self.adapter.get_resource_data(Ingredient, parameters=parameters)
        self.assertEqual(len(data), 0)

    def test_post_ingredient(self):
        parameters = {
            'name': 'non_existent',
        }
        data = self.adapter.post_resource_data(Ingredient, parameters)
        print (data)

    def test_get_ingredient_composition(self):
        data = self.adapter.get_resource_data(Ingredient)
        self.assertEqual(len(data), 1)

    def test_get_filters_on_ingredient_composition(self):
        data = self.adapter.get_resource_data(IngredientComposition)
        for ingredient_composition in data:
            ingredient_uuid = ingredient_composition['ingredient']['uuid']

            # do a lookup based on an ingredient .. make sure we can navigate
            # back and forth based on uuid lookups
            filter_parameters = {
                'ingredient_uuid': ingredient_uuid
            }
            filtered_data = self.adapter.get_resource_data(IngredientComposition, parameters=filter_parameters)
            filtered_data_ingredient_uuids = [result['ingredient']['uuid'] for result in filtered_data]

            self.assertTrue(ingredient_uuid in filtered_data_ingredient_uuids)
