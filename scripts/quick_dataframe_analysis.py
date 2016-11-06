# A one-off script that is manually run to look at individual results
from analytics.events.analytics import DataFrameEventsAnalyzer
from importers.excel.importer import ExcelSupplementFileSanitizer

import pandas as pd

personal_fixtures_file = '/betterself/personal_fixtures/supplement_event_log.xlsx'

sanitizer = ExcelSupplementFileSanitizer(personal_fixtures_file, user=None)
dataframe = sanitizer.get_sanitized_dataframe()

ignore_columns = [
    'Day',
    'Notes',
]

correlation_driver = 'Productivity Time (Minutes)'
rest_day_column_name = 'Rest Day'

analyzer = DataFrameEventsAnalyzer(dataframe, ignore_columns=ignore_columns, rest_day_column_name=rest_day_column_name)
print(analyzer.get_correlation_for_measurement(correlation_driver))

dataframe = analyzer.dataframe
test_column = correlation_driver

summed_dataframe = analyzer.get_rolled_dataframe(dataframe, 7)
summed_correlation_ts = summed_dataframe[test_column]
original_correlation_ts = dataframe[test_column]

pretty_view = pd.DataFrame(index=summed_correlation_ts.index,
    data={
        'summed': summed_correlation_ts,
        'original': original_correlation_ts
    }
)

# TD - Create Data fixture that sums up dataframe
# sum function should not accept nulls
# Create datafixture that tests this

analyzer.get_correlation_across_summed_days_for_measurement(correlation_driver)
