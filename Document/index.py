import pandas as pd

# Load datasets
dataset_2016_targets = pd.read_csv('2016_-_Cities_Emissions_Reduction_Targets_20240207.csv')
dataset_2016_ghg = pd.read_csv('2016_-_Citywide_GHG_Emissions_20240207.csv')
dataset_2017_community = pd.read_csv('2017_-_Cities_Community_Wide_Emissions.csv')
dataset_2017_targets = pd.read_csv('2017_-_Cities_Emissions_Reduction_Targets_20240207.csv')
dataset_2023_risk = pd.read_csv('2023_Cities_Climate_Risk_and_Vulnerability_Assessments_20240207.csv')

# Function to prepare and rename columns
def prepare_dataset(dataset, year, col_mappings):
    dataset = dataset.rename(columns=col_mappings)
    dataset['year'] = year
    return dataset

# Define column mappings for each dataset
col_mappings_2016_targets = {
    'City Name': 'city',
    'Country': 'country',
    'Baseline emissions (metric tonnes CO2e)': 'emission',
    'Target date': 'emission_target',
    'Baseline year':'baseline_year',
    'Percentage reduction target': 'target',
    'Sector':'sector'
}
col_mappings_2016_ghg = {
    'City Name': 'city',
    'Country': 'country',
    'Total CO2 emissions (metric tonnes CO2e)': 'emission',
    'City GDP': 'city_gdp',
    'Current Population': 'city_population',
    'Increase/Decrease from last year':'year_status',
    'Reporting Year':'year'
}


col_mappings_2017_community = {
    'City': 'city',
    'Country': 'country',
    'Total emissions (metric tonnes CO2e)': 'emission',
    'GDP': 'city_gdp',
    'Population': 'city_population',
    'Increase/Decrease from last year':'year_status',
    'Reporting Year':'year'
}

col_mappings_2017_targets = {
    'City': 'city',
    'Country': 'country',
    'Baseline emissions (metric tonnes CO2e)': 'emission',
    'Target date': 'emission_target',
    'Baseline year':'baseline_year',
    'Percentage reduction target': 'target',
    'Sector':'sector'
}

col_mappings_2023_risk = {
    'City': 'city',
    'Country/Area': 'country',
    'Year of publication or approval': 'year',
    'Factors considered in assessment': 'factors',
    'Population': 'city_population',
}

# Prepare each dataset
dataset_2016_targets_prepared = prepare_dataset(dataset_2016_targets, 2016, col_mappings_2016_targets)
dataset_2016_ghg_prepared = prepare_dataset(dataset_2016_ghg, 2016, col_mappings_2016_ghg)
dataset_2017_community_prepared = prepare_dataset(dataset_2017_community, 2017, col_mappings_2017_community)
dataset_2017_targets_prepared = prepare_dataset(dataset_2017_targets, 2017, col_mappings_2017_targets)
dataset_2023_risk_prepared = prepare_dataset(dataset_2023_risk, 2023, col_mappings_2023_risk)

# Merge all datasets
merged_dataset = pd.concat([
    dataset_2016_targets_prepared,
    dataset_2016_ghg_prepared,
    dataset_2017_community_prepared,
    dataset_2017_targets_prepared,
    dataset_2023_risk_prepared
])

# Drop duplicates and keep the latest record for each city per year
merged_dataset = merged_dataset.drop_duplicates(subset=['city', 'year'], keep='last')


final_selected_columns_dataset = merged_dataset[[
    'city', 'city_gdp', 'city_population', 'country', 'emission', 'emission_target', 'target', 'baseline_year', 'year', 'year_status', 'factors', 'sector'
]]

# Save the merged dataset
final_selected_columns_dataset.to_json('merged_dataset.json', orient='records', lines=True)