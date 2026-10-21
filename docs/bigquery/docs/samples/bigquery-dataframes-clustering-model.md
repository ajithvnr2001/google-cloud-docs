---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-dataframes-clustering-model/
title: Create a clustering model with BigQuery DataFrames \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:41:46.583749+00:00
---

# Create a clustering model with BigQuery DataFrames  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-dataframes-clustering-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Create a clustering model with BigQuery DataFrames Stay organized with collections  Save and categorize content based on your preferences. 

Create a k-means clustering model on the lengths and sex of penguins using the BigQuery DataFrames API.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Use ML and AI with BigQuery DataFrames](https://docs.cloud.google.com/bigquery/docs/dataframes-ml-ai)



## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from bigframes.ml.cluster import KMeans
    import bigframes.pandas as bpd
    
    # Load data from BigQuery
    query_or_table = "bigquery-public-data.ml_datasets.penguins"
    bq_df = bpd.read_gbq(query_or_table)
    
    # Create the KMeans model
    cluster_model = KMeans(n_clusters=10)
    cluster_model.fit(bq_df["culmen_length_mm"], bq_df["sex"])
    
    # Predict using the model
    result = cluster_model.predict(bq_df)
    # Score the model
    score = cluster_model.score(bq_df)

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
