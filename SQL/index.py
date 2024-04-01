import pandas as pd

# Load datasets
dataset_1 = pd.read_csv('2016_-_Citywide_GHG_Emissions_20240207.csv')
dataset_2 = pd.read_csv('2017_-_Cities_Community_Wide_Emissions.csv')
dataset_3 = pd.read_csv('2017_-_Cities_Emissions_Reduction_Targets_20240207.csv')
dataset_4 = pd.read_csv('2023_Cities_Climate_Risk_and_Vulnerability_Assessments_20240207.csv')
dataset_5 = pd.read_csv('2016_-_Cities_Emissions_Reduction_Targets_20240207.csv')

# Function to prepare and rename columns
def prepare_dataset(dataset, col_mappings, cols_to_add):
    # Rename columns
    dataset = dataset.rename(columns=col_mappings)
    # Add missing columns as NaN
    for col in cols_to_add:
        if col not in dataset.columns:
            dataset[col] = pd.NA
    return dataset

# Column mappings for each dataset
col_mappings_1 = {
    'City Name': 'city',
    'City GDP': 'city_gdp',
    'Current Population': 'city_population',
    'Country': 'country',
        'Total CO2 emissions (metric tonnes CO2e)': 'emission'
}

col_mappings_2 = {
    'City': 'city',
    'GDP': 'city_gdp',
    'Population': 'city_population',
    'Country': 'country',
    'Total City-wide emissions (metric tonnes CO2e)': 'emission'
}

col_mappings_3 = {
    'City': 'city',
    'Country': 'country',
    'Sector': 'sector',
    'Baseline emissions (metric tonnes CO2e)': 'emission',
    'Percentage reduction target': 'emission_target'
}

col_mappings_4 = {
    'Organization Name': 'city',
    'Country/Area': 'country',
    'Population': 'city_population'
}

col_mappings_5 = {
    'Organisation': 'city',
    'Country': 'country',
    'Sector': 'sector',
    'Baseline emissions (metric tonnes CO2e)': 'emission',
    'Percentage reduction target': 'emission_target'
}

# Prepare each dataset
dataset_1_prepared = prepare_dataset(dataset_1, col_mappings_1, ['sector', 'emission_target', 'emission_status'])
dataset_2_prepared = prepare_dataset(dataset_2, col_mappings_2, ['sector', 'emission_target', 'emission_status'])
dataset_3_prepared = prepare_dataset(dataset_3, col_mappings_3, ['city_gdp', 'city_population', 'emission_status'])
dataset_4_prepared = prepare_dataset(dataset_4, col_mappings_4, ['city_gdp', 'emission', 'sector', 'emission_target', 'emission_status'])
dataset_5_prepared = prepare_dataset(dataset_5, col_mappings_5, ['city_gdp', 'city_population', 'emission_status'])

# Merge all datasets
final_merged_dataset = pd.concat([dataset_1_prepared, dataset_2_prepared, dataset_3_prepared, dataset_4_prepared, dataset_5_prepared])

# Select only the specified columns
final_selected_columns_dataset = final_merged_dataset[[
    'city', 'city_gdp', 'city_population', 'country', 'emission', 'emission_status', 'emission_target', 'sector'
]]

# Save the selected columns dataset
final_selected_columns_dataset.to_csv('selected_columns_merged_dataset.csv', index=False)