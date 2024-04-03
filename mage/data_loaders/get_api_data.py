import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    url = 'https://data.cincinnati-oh.gov/api/views/k59e-2pvf/rows.csv?accessType=DOWNLOAD&api_foundry=true'

    cincy_schema = {
    'INSTANCEID': 'object',
    'INCIDENT_NO': 'object',
    'CLSD': 'object',
    'UCR': 'float64',
    'DST': 'object',
    'BEAT': 'object',
    'OFFENSE': 'object',
    'LOCATION': 'object',
    'THEFT_CODE': 'object',
    'FLOOR': 'object',
    'SIDE': 'object',
    'OPENING': 'object',
    'HATE_BIAS': 'object',
    'DAYOFWEEK': 'object',
    'RPT_AREA': 'object',
    'CPD_NEIGHBORHOOD': 'object',
    'WEAPONS': 'object',
    'HOUR_FROM': 'float64',
    'HOUR_TO': 'float64',
    'ADDRESS_X': 'object',
    'LONGITUDE_X': 'float64',
    'LATITUDE_X': 'float64',
    'VICTIM_AGE': 'object',
    'VICTIM_RACE': 'object',
    'VICTIM_ETHNICITY': 'object',
    'VICTIM_GENDER': 'object',
    'SUSPECT_AGE': 'object',
    'SUSPECT_RACE': 'object',
    'SUSPECT_ETHNICITY': 'object',
    'SUSPECT_GENDER': 'object',
    'TOTALNUMBERVICTIMS': 'float64',
    'TOTALSUSPECTS': 'float64',
    'UCR_GROUP': 'object',
    'ZIP': 'float64',
    'COMMUNITY_COUNCIL_NEIGHBORHOOD': 'object',
    'SNA_NEIGHBORHOOD': 'object'
    }

    parse_dates = ['DATE_REPORTED', 'DATE_FROM', 'DATE_TO', 'DATE_OF_CLEARANCE']


    cincy_df = pd.read_csv(url, dtype=cincy_schema, parse_dates=parse_dates)

    return cincy_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
