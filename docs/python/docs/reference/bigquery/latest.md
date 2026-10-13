---
url: https://docs.cloud.google.com/python/docs/reference/bigquery/latest/
title: Python Client for Google BigQuery \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:59:11.181820+00:00
---

# Python Client for Google BigQuery  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/bigquery/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Python Client for Google BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

3.46.1 (latest)  3.46.0  3.45.2  3.44.0  3.43.0  3.42.3  3.41.0  3.40.1  3.39.0  3.38.0  3.37.0  3.36.0  3.35.1  3.34.0  3.33.0  3.31.0  3.30.0  3.29.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.1  3.22.0  3.21.0  3.20.1  3.19.0  3.18.0  3.17.2  3.16.0  3.15.0  3.14.1  3.13.0  3.12.0  3.11.4  3.4.0  3.3.6  3.2.0  3.1.0  3.0.1  2.34.4  2.33.0  2.32.0  2.31.0  2.30.1  2.29.0  2.28.1  2.27.1  2.26.0  2.25.2  2.24.1  2.23.3  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.1  2.15.0  2.14.0  2.13.1  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.2  2.5.0  2.4.0  2.3.1  2.2.0  2.1.0  2.0.0  1.28.2  1.27.2  1.26.1  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0 

[![image](https://img.shields.io/badge/support-GA-gold.svg)](https://github.com/googleapis/google-cloud-python/blob/main/README.rst#general-availability) [![image](https://img.shields.io/pypi/v/google-cloud-bigquery.svg)](https://pypi.org/project/google-cloud-bigquery/) [![image](https://img.shields.io/pypi/pyversions/google-cloud-bigquery.svg)](https://pypi.org/project/google-cloud-bigquery/)

Querying massive datasets can be time consuming and expensive without the right hardware and infrastructure. Google [BigQuery](https://cloud.google.com/bigquery/what-is-bigquery) solves this problem by enabling super-fast, SQL queries against append-mostly tables, using the processing power of Google’s infrastructure.

  * [Client Library Documentation](https://cloud.google.com/python/docs/reference/bigquery/latest/summary_overview)

  * [Product Documentation](https://cloud.google.com/bigquery/docs/reference/v2/)




## Related Libraries

For higher-level data analysis and DataFrame operations, consider using one of the following connector libraries:

Library | Description | Documentation  
---|---|---  
[BigQuery DataFrames (bigframes)](https://dataframes.bigquery.dev/) | Flexible pandas-like and scikit-learn-like API powered by BigQuery engine for large-scale data analysis and ML. | [BigFrames Docs](https://dataframes.bigquery.dev/)  
[pandas-gbq](https://pandas-gbq.readthedocs.io/) | Convenient integration allowing pandas DataFrames to load from and write to BigQuery. | [pandas-gbq Docs](https://pandas-gbq.readthedocs.io/)  
  
## Quick Start

In order to use this library, you first need to go through the following steps:

  1. [Select or create a Cloud Platform project.](https://console.cloud.google.com/project)

  2. [Enable billing for your project.](https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project)

  3. [Enable the Google Cloud BigQuery API.](https://cloud.google.com/bigquery)

  4. [Setup Authentication.](https://googleapis.dev/python/google-api-core/latest/auth.html)




### Installation

Install this library in a [virtualenv](https://virtualenv.pypa.io/en/latest/) using pip. [virtualenv](https://virtualenv.pypa.io/en/latest/) is a tool to create isolated Python environments. The basic problem it addresses is one of dependencies and versions, and indirectly permissions.

With [virtualenv](https://virtualenv.pypa.io/en/latest/), it’s possible to install this library without needing system install permissions, and without clashing with the installed system dependencies.

#### Supported Python Versions

Python >= 3.10

#### Unsupported Python Versions

Python <= 3.9.

The last version of this library compatible with Python 2.7 and 3.5 is google-cloud-bigquery==1.28.0.

#### Mac/Linux
    
    
    pip install virtualenv
    virtualenv <your-env>
    source <your-env>/bin/activate
    <your-env>/bin/pip install google-cloud-bigquery
    

#### Windows
    
    
    pip install virtualenv
    virtualenv <your-env>
    <your-env>\Scripts\activate
    <your-env>\Scripts\pip.exe install google-cloud-bigquery
    

## Example Usage

### Perform a query
    
    
    from google.cloud import [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest)
    
    client = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)()
    
    # Perform a query.
    QUERY = (
        'SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` '
        'WHERE state = "TX" '
        'LIMIT 100')
    query_job = client.[query](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)(QUERY)  # API request
    rows = [query_job](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dbapi.Cursor.html#google_cloud_bigquery_dbapi_Cursor_query_job).result()  # Waits for query to finish
    
    for row in rows:
        print(row.name)
    

## Instrumenting With OpenTelemetry

This application uses [OpenTelemetry](https://opentelemetry.io) to output tracing data from API calls to BigQuery. To enable OpenTelemetry tracing in the BigQuery client the following PyPI packages need to be installed:
    
    
    pip install google-cloud-bigquery[opentelemetry] opentelemetry-exporter-gcp-trace
    

After installation, OpenTelemetry can be used in the BigQuery client and in BigQuery jobs. First, however, an exporter must be specified for where the trace data will be outputted to. An example of this can be found here:
    
    
    from opentelemetry import trace
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import BatchSpanProcessor
    from opentelemetry.exporter.cloud_trace import CloudTraceSpanExporter
    tracer_provider = TracerProvider()
    tracer_provider = BatchSpanProcessor(CloudTraceSpanExporter())
    trace.set_tracer_provider(TracerProvider())
    

In this example all tracing data will be published to the Google [Cloud Trace](https://cloud.google.com/trace) console. For more information on OpenTelemetry, please consult the [OpenTelemetry documentation](https://opentelemetry-python.readthedocs.io).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
