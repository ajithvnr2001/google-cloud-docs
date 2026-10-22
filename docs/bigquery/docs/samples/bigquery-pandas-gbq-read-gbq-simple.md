---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-pandas-gbq-read-gbq-simple/
title: Run a query with pandas-gbq \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:22.850370+00:00
---

# Run a query with pandas-gbq  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-pandas-gbq-read-gbq-simple/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Run a query with pandas-gbq Stay organized with collections  Save and categorize content based on your preferences. 

Use the pandas-gbq package to run a simple query.

## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import bigframes.pandas as bpd
    import pandas as pd
    import pandas_gbq
    
    # Set partial ordering mode for BigQuery DataFrames.
    bpd.options.bigquery.ordering_mode = "partial"
    
    
    def read_gbq_simple_pandas_gbq() -> pd.DataFrame:
        """Queries BigQuery using pandas-gbq and returns an in-memory DataFrame."""
        sql = """
        SELECT name, SUM(number) as total_people
        FROM `bigquery-public-data.usa_names.usa_1910_2013`
        WHERE state = 'TX'
        GROUP BY name
        ORDER BY total_people DESC
        LIMIT 20
        """
        df_pandas = pandas_gbq.read_gbq(sql)
        print("Queried using pandas-gbq.")
        return df_pandas
    
    
    def read_gbq_simple_bigframes() -> bpd.DataFrame:
        """Queries BigQuery using BigQuery DataFrames and returns a distributed DataFrame."""
        sql = """
        SELECT name, SUM(number) as total_people
        FROM `bigquery-public-data.usa_names.usa_1910_2013`
        WHERE state = 'TX'
        GROUP BY name
        ORDER BY total_people DESC
        LIMIT 20
        """
        df_bigframes = bpd.read_gbq(sql)
        print("Queried using BigQuery DataFrames.")
        return df_bigframes
    
    
    # [Preferred] Run using pandas-gbq:
    # df_pandas = read_gbq_simple_pandas_gbq()
    # print(df_pandas.head())
    
    # Alternatively, run using BigQuery DataFrames:
    # df_bigframes = read_gbq_simple_bigframes()
    # print(df_bigframes.head())

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
