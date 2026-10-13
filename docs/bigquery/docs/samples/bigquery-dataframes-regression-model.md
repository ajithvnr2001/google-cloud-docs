---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-dataframes-regression-model/
title: Create a regression model with BigQuery DataFrames \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:10:20.826601+00:00
---

# Create a regression model with BigQuery DataFrames  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-dataframes-regression-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Create a regression model with BigQuery DataFrames Stay organized with collections  Save and categorize content based on your preferences. 

Create a linear regression model on the body mass of penguins using the BigQuery DataFrames API.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Use ML and AI with BigQuery DataFrames](https://docs.cloud.google.com/bigquery/docs/dataframes-ml-ai)



## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from bigframes.ml.linear_model import LinearRegression
    import bigframes.pandas as bpd
    
    # Load data from BigQuery
    query_or_table = "bigquery-public-data.ml_datasets.penguins"
    bq_df = bpd.read_gbq(query_or_table)
    
    # Filter down to the data to the Adelie Penguin species
    adelie_data = bq_df[bq_df.species == "Adelie Penguin (Pygoscelis adeliae)"]
    
    # Drop the species column
    adelie_data = adelie_data.drop(columns=["species"])
    
    # Drop rows with nulls to get training data
    training_data = adelie_data.dropna()
    
    # Specify your feature (or input) columns and the label (or output) column:
    feature_columns = training_data[
        ["island", "culmen_length_mm", "culmen_depth_mm", "flipper_length_mm", "sex"]
    ]
    label_columns = training_data[["body_mass_g"]]
    
    test_data = adelie_data[adelie_data.body_mass_g.isnull()]
    
    # Create the linear model
    model = LinearRegression()
    model.fit(feature_columns, label_columns)
    
    # Score the model
    score = model.score(feature_columns, label_columns)
    
    # Predict using the model
    result = model.predict(test_data)

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
