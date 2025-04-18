import streamlit as st # added
from google.oauth2 import service_account #added
import pandas_gbq # added

@st.cache_resource
def connect_to_bigquery_manhattan(table):

    # create API client
    creds = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(creds)

    sql = f"""
    SELECT filing_date,
            job_type,
            building_type,
            proposed_dwelling_units,
            latitude,
            longitude,
            filing_status,
    FROM `{table}`
    WHERE (UPPER(borough)='MANHATTAN' or borough='1') AND job_type='New Building'
    """

    return pandas_gbq.read_gbq(sql, credentials=credentials)

@st.cache_resource
def connect_to_bigquery_bronx(table):

    # create API client
    creds = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(creds)

    # filter_datetime = f"""
    # SAFE.PARSE_DATETIME('%Y-%m-%dT%H:%M:%S.%f', sale_date) IS NOT NULL AND
    # SAFE.PARSE_DATETIME('%Y-%m-%dT%H:%M:%S.%f', sale_date) > DATETIME '{filter}'
    # """

    sql = f"""
    SELECT filing_date,
            job_type,
            building_type,
            proposed_dwelling_units,
            latitude,
            longitude,
            filing_status
    FROM `{table}`
    WHERE UPPER(borough)='BRONX' or borough='2' AND job_type='New Building'
    """

    return pandas_gbq.read_gbq(sql, credentials=credentials)

@st.cache_resource
def connect_to_bigquery_brooklyn(table):

    # create API client
    creds = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(creds)

    # filter_datetime = f"""
    # SAFE.PARSE_DATETIME('%Y-%m-%dT%H:%M:%S.%f', sale_date) IS NOT NULL AND
    # SAFE.PARSE_DATETIME('%Y-%m-%dT%H:%M:%S.%f', sale_date) > DATETIME '{filter}'
    # """

    sql = f"""
    SELECT filing_date,
            job_type,
            building_type,
            proposed_dwelling_units,
            latitude,
            longitude,
            filing_status
    FROM `{table}`
    WHERE UPPER(borough)='BROOKLYN' or borough='3' AND job_type='New Building'
    """

    return pandas_gbq.read_gbq(sql, credentials=credentials)

@st.cache_resource
def connect_to_bigquery_queens(table):

    # create API client
    creds = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(creds)

    # filter_datetime = f"""
    # SAFE.PARSE_DATETIME('%Y-%m-%dT%H:%M:%S.%f', sale_date) IS NOT NULL AND
    # SAFE.PARSE_DATETIME('%Y-%m-%dT%H:%M:%S.%f', sale_date) > DATETIME '{filter}'
    # """

    sql = f"""
    SELECT filing_date,
            job_type,
            building_type,
            proposed_dwelling_units,
            latitude,
            longitude,
            filing_status
    FROM `{table}`
    WHERE UPPER(borough)='QUEENS' or borough='4' AND job_type='New Building'
    """

    return pandas_gbq.read_gbq(sql, credentials=credentials)

@st.cache_resource
def connect_to_bigquery_staten(table):

    # create API client
    creds = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(creds)

    # filter_datetime = f"""
    # SAFE.PARSE_DATETIME('%Y-%m-%dT%H:%M:%S.%f', sale_date) IS NOT NULL AND
    # SAFE.PARSE_DATETIME('%Y-%m-%dT%H:%M:%S.%f', sale_date) > DATETIME '{filter}'
    # """

    sql = f"""
    SELECT filing_date,
            job_type,
            building_type,
            proposed_dwelling_units,
            latitude,
            longitude,
            filing_status
    FROM `{table}`
    WHERE UPPER(borough)='STATEN ISLAND' or borough='5' AND job_type='New Building'
    """

    return pandas_gbq.read_gbq(sql, credentials=credentials)

# sql = f"""
#     SELECT job_filing_number, 
#             filing_status, 
#             building_type, # used
#             proposed_no_of_stories,
#             proposed_height,
#             proposed_dwelling_units, # used
#             filing_date, # used
#             latitude, # used
#             longitude, # used
#             job_type # used
#     FROM `{table}`
#     WHERE UPPER(borough)='STATEN ISLAND' or borough='5' AND job_type='New Building'
#     """