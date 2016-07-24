from rest_framework.generics import GenericAPIView
from django.db.models import Q

from apis.betterself.v1.serializers import IngredientCompositionSerializer, SupplementProductSerializer, \
    MeasurementSerializer, IngredientSerializer
from supplements.models import Ingredient, IngredientComposition, MeasurementUnit, SupplementProduct


class BaseGenericAPIViewV1(GenericAPIView):
    model = None

    def get_queryset(self):
        # for all objects returned, a user should only see either
        # objects that don't belong to a user or objects owned by a
        # specific user
        queryset = self.model.filter(Q(user=self.request.user) | Q(user=None))
        return queryset


class IngredientView(BaseGenericAPIViewV1):
    serializer_class = IngredientSerializer
    model = Ingredient


class MeasurementUnitView(BaseGenericAPIViewV1):
    serializer_class = MeasurementSerializer
    model = MeasurementUnit


class IngredientCompositionView(BaseGenericAPIViewV1):
    serializer_class = IngredientCompositionSerializer
    model = IngredientComposition


class SupplementProductView(BaseGenericAPIViewV1):
    serializer_class = SupplementProductSerializer
    model = SupplementProduct
