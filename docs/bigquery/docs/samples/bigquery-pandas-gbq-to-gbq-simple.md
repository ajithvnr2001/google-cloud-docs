---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-pandas-gbq-to-gbq-simple/
title: Load a DataFrame to BigQuery with pandas-gbq \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:42:01.103258+00:00
---

# Load a DataFrame to BigQuery with pandas-gbq  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-pandas-gbq-to-gbq-simple/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Load a DataFrame to BigQuery with pandas-gbq Stay organized with collections  Save and categorize content based on your preferences. 

Use the pandas-gbq package to load a DataFrame to BigQuery.

## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import bigframes.pandas as bpd
    import pandas as pd
    import pandas_gbq
    
    # Set partial ordering mode for BigQuery DataFrames.
    bpd.options.bigquery.ordering_mode = "partial"
    
    
    def pandas_to_gbq_simple_pandas_gbq(
        destination_table: str = "your-project.your_dataset.your_table_name",
    ) -> None:
        """Uploads a pandas DataFrame to BigQuery using pandas-gbq directly."""
        df = pd.DataFrame(
            {
                "my_string": ["a", "b", "c"],
                "my_int64": [1, 2, 3],
                "my_float64": [4.0, 5.0, 6.0],
                "my_bool1": [True, False, True],
                "my_bool2": [False, True, False],
                "my_dates": pd.date_range("now", periods=3),
            }
        )
        pandas_gbq.to_gbq(df, destination_table, if_exists="replace")
        print(f"Uploaded DataFrame to {destination_table} using pandas-gbq.")
    
    
    def pandas_to_gbq_simple_bigframes(
        destination_table: str = "your-project.your_dataset.your_table_name",
    ) -> None:
        """Uploads a pandas DataFrame to BigQuery using BigQuery DataFrames."""
        df = pd.DataFrame(
            {
                "my_string": ["a", "b", "c"],
                "my_int64": [1, 2, 3],
                "my_float64": [4.0, 5.0, 6.0],
                "my_bool1": [True, False, True],
                "my_bool2": [False, True, False],
                "my_dates": pd.date_range("now", periods=3),
            }
        )
        bq_df = bpd.read_pandas(df)
        bq_df.to_gbq(destination_table, if_exists="replace")
        print(f"Uploaded DataFrame to {destination_table} using BigQuery DataFrames.")
    
    
    # [Preferred] Run using pandas-gbq:
    # pandas_to_gbq_simple_pandas_gbq("your-project.your_dataset.your_table_name")
    
    # Alternatively, run using BigQuery DataFrames:
    # pandas_to_gbq_simple_bigframes("your-project.your_dataset.your_table_name")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
