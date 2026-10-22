---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-load-table-dataframe/
title: Load data from DataFrame \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:20.419021+00:00
---

# Load data from DataFrame  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-load-table-dataframe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Load data from DataFrame Stay organized with collections  Save and categorize content based on your preferences. 

Load contents of a pandas DataFrame to a table.

## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import datetime
    from zoneinfo import ZoneInfo
    
    import bigframes.pandas as bpd
    import pandas as pd
    import pandas_gbq
    
    # Set partial ordering mode for BigQuery DataFrames.
    bpd.options.bigquery.ordering_mode = "partial"
    
    
    def load_table_dataframe_bigframes(
        table_id: str = "your-project.your_dataset.your_table_name",
    ) -> None:
        """Loads a pandas DataFrame into a BigQuery table using BigQuery DataFrames."""
        records = [
            {
                "title": "The Meaning of Life",
                "release_year": 1983,
                "length_minutes": 112.5,
                "release_date": datetime.datetime(
                    1983, 5, 9, 13, 0, 0, tzinfo=ZoneInfo("Europe/Paris")
                ).astimezone(datetime.timezone.utc),
                # Assume UTC timezone when a datetime object contains no timezone.
                "dvd_release": datetime.datetime(2002, 1, 22, 7, 0, 0),
            },
            {
                "title": "Monty Python and the Holy Grail",
                "release_year": 1975,
                "length_minutes": 91.5,
                "release_date": datetime.datetime(
                    1975, 4, 9, 23, 59, 2, tzinfo=ZoneInfo("Europe/London")
                ).astimezone(datetime.timezone.utc),
                "dvd_release": datetime.datetime(2002, 7, 16, 9, 0, 0),
            },
            {
                "title": "Life of Brian",
                "release_year": 1979,
                "length_minutes": 94.25,
                "release_date": datetime.datetime(
                    1979, 8, 17, 23, 59, 5, tzinfo=ZoneInfo("America/New_York")
                ).astimezone(datetime.timezone.utc),
                "dvd_release": datetime.datetime(2008, 1, 14, 8, 0, 0),
            },
            {
                "title": "And Now for Something Completely Different",
                "release_year": 1971,
                "length_minutes": 88.0,
                "release_date": datetime.datetime(
                    1971, 9, 28, 23, 59, 7, tzinfo=ZoneInfo("Europe/London")
                ).astimezone(datetime.timezone.utc),
                "dvd_release": datetime.datetime(2003, 10, 22, 10, 0, 0),
            },
        ]
        dataframe = pd.DataFrame(
            records,
            # In the loaded table, the column order reflects the order of the
            # columns in the DataFrame.
            columns=[
                "title",
                "release_year",
                "length_minutes",
                "release_date",
                "dvd_release",
            ],
            # Optionally, set a named index, which can also be written to the
            # BigQuery table.
            index=pd.Index(["Q24980", "Q25043", "Q24953", "Q16403"], name="wikidata_id"),
        )
    
        bq_df = bpd.read_pandas(dataframe)
        bq_df.to_gbq(table_id, if_exists="replace", index=True)
        print(f"Loaded DataFrame to {table_id} using BigQuery DataFrames.")
    
    
    def load_table_dataframe_pandas_gbq(
        table_id: str = "your-project.your_dataset.your_table_name",
    ) -> None:
        """Loads a pandas DataFrame into a BigQuery table using pandas-gbq."""
        records = [
            {
                "title": "The Meaning of Life",
                "release_year": 1983,
                "length_minutes": 112.5,
                "release_date": datetime.datetime(
                    1983, 5, 9, 13, 0, 0, tzinfo=ZoneInfo("Europe/Paris")
                ).astimezone(datetime.timezone.utc),
                # Assume UTC timezone when a datetime object contains no timezone.
                "dvd_release": datetime.datetime(2002, 1, 22, 7, 0, 0),
            },
            {
                "title": "Monty Python and the Holy Grail",
                "release_year": 1975,
                "length_minutes": 91.5,
                "release_date": datetime.datetime(
                    1975, 4, 9, 23, 59, 2, tzinfo=ZoneInfo("Europe/London")
                ).astimezone(datetime.timezone.utc),
                "dvd_release": datetime.datetime(2002, 7, 16, 9, 0, 0),
            },
            {
                "title": "Life of Brian",
                "release_year": 1979,
                "length_minutes": 94.25,
                "release_date": datetime.datetime(
                    1979, 8, 17, 23, 59, 5, tzinfo=ZoneInfo("America/New_York")
                ).astimezone(datetime.timezone.utc),
                "dvd_release": datetime.datetime(2008, 1, 14, 8, 0, 0),
            },
            {
                "title": "And Now for Something Completely Different",
                "release_year": 1971,
                "length_minutes": 88.0,
                "release_date": datetime.datetime(
                    1971, 9, 28, 23, 59, 7, tzinfo=ZoneInfo("Europe/London")
                ).astimezone(datetime.timezone.utc),
                "dvd_release": datetime.datetime(2003, 10, 22, 10, 0, 0),
            },
        ]
        dataframe = pd.DataFrame(
            records,
            # In the loaded table, the column order reflects the order of the
            # columns in the DataFrame.
            columns=[
                "title",
                "release_year",
                "length_minutes",
                "release_date",
                "dvd_release",
            ],
            # Optionally, set a named index, which can also be written to the
            # BigQuery table.
            index=pd.Index(["Q24980", "Q25043", "Q24953", "Q16403"], name="wikidata_id"),
        )
    
        pandas_gbq.to_gbq(dataframe, table_id, if_exists="replace")
        print(f"Loaded DataFrame to {table_id} using pandas-gbq.")
    
    
    # [Preferred] Run using BigQuery DataFrames:
    # load_table_dataframe_bigframes("your-project.your_dataset.your_table_name")
    
    # Alternatively, run using pandas-gbq:
    # load_table_dataframe_pandas_gbq("your-project.your_dataset.your_table_name")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
