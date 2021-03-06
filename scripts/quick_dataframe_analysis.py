# A one-off script that is run (manually) to look at individual results
from django.contrib.auth import get_user_model

from importers.serializers.excel.serializers import ExcelSupplementFileSerializer

# Setup Constants
User = get_user_model()
user = User.objects.get(username='jeffshek')
personal_fixtures_file = '/betterself/personal_fixtures/supplement_event_log.xlsx'

# Import Process
sanitizer = ExcelSupplementFileSerializer(personal_fixtures_file, user=user, sheet='Log')
dataframe = sanitizer.get_sanitized_dataframe()
sanitizer.save_results(dataframe)

# TODO - split this and separate out to some object versus scripting
# ignore_columns = [
#     'Day',
#     'Notes',
# ]
#
# correlation_driver = 'Productivity Time (Minutes)'
# # use this to ignore rest days that destroy correlations
# rest_day_column_name = 'Rest Day'
#
# analyzer = DataFrameEventsAnalyzer(dataframe, ignore_columns=ignore_columns, rest_day_column=rest_day_column_name)
# dataframe = analyzer.dataframe
# dataframe_with_yesterday = analyzer.add_yesterday_shifted_to_dataframe(dataframe)
#
# # get a list of any values that isn't a zero that should be counted
# # use this to filter out any supplements / events that don't have a # greater than a threshold.
# # ie. if you've only tried supplement Y three times, it's probably full of placebo
# # and you shouldn't care about it.
# event_count = analyzer.get_dataframe_event_count(dataframe)
#
# results = analyzer.get_correlation_across_summed_days_for_measurement(measurement=correlation_driver,
#     add_yesterday_lag=False)
# results.to_csv('output.csv')
#
# results_with_counts = pd.DataFrame(data={
#     'correlation': results,
#     'count': event_count
# })
#
# results_with_counts = results_with_counts.sort_values(['correlation'])
#
# results_above_threshold = results_with_counts['count'] > 20
#
# results_with_counts = results_with_counts[results_above_threshold]
# results_with_counts.to_csv('output.csv')
