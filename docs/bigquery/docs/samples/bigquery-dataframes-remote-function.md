---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-dataframes-remote-function/
title: Deploy and apply a remote function using BigQuery DataFrames \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:39.848784+00:00
---

# Deploy and apply a remote function using BigQuery DataFrames  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-dataframes-remote-function/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Deploy and apply a remote function using BigQuery DataFrames Stay organized with collections  Save and categorize content based on your preferences. 

Use the BigQuery DataFrames API to deploy a Python function as a Cloud Function and use it as a remote function.

## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import bigframes.pandas as bpd
    
    # Set BigQuery DataFrames options
    bpd.options.bigquery.project = your_gcp_project_id
    bpd.options.bigquery.location = "US"
    
    # BigQuery DataFrames gives you the ability to turn your custom scalar
    # functions into a BigQuery remote function. It requires the GCP project to
    # be set up appropriately and the user having sufficient privileges to use
    # them. One can find more details about the usage and the requirements via
    # `help` command.
    help(bpd.remote_function)
    
    # Read a table and inspect the column of interest.
    df = bpd.read_gbq("bigquery-public-data.ml_datasets.penguins")
    df["body_mass_g"].head(10)
    
    # Define a custom function, and specify the intent to turn it into a remote
    # function. It requires a BigQuery connection. If the connection is not
    # already created, BigQuery DataFrames will attempt to create one assuming
    # the necessary APIs and IAM permissions are setup in the project. In our
    # examples we will be letting the default connection `bigframes-default-connection`
    # be used. We will also set `reuse=False` to make sure we don't
    # step over someone else creating remote function in the same project from
    # the exact same source code at the same time. Let's try a `pandas`-like use
    # case in which we want to apply a user defined scalar function to every
    # value in a `Series`, more specifically bucketize the `body_mass_g` value
    # of the penguins, which is a real number, into a category, which is a
    # string.
    @bpd.remote_function(
        reuse=False,
        cloud_function_service_account="default",
    )
    def get_bucket(num: float) -> str:
        if not num:
            return "NA"
        boundary = 4000
        return "at_or_above_4000" if num >= boundary else "below_4000"
    
    # Then we can apply the remote function on the `Series` of interest via
    # `apply` API and store the result in a new column in the DataFrame.
    df = df.assign(body_mass_bucket=df["body_mass_g"].apply(get_bucket))
    
    # This will add a new column `body_mass_bucket` in the DataFrame. You can
    # preview the original value and the bucketized value side by side.
    df[["body_mass_g", "body_mass_bucket"]].head(10)
    
    # The above operation was possible by doing all the computation on the
    # cloud. For that, there is a google cloud function deployed by serializing
    # the user code, and a BigQuery remote function created to call the cloud
    # function via the latter's http endpoint on the data in the DataFrame.
    
    # The BigQuery remote function created to support the BigQuery DataFrames
    # remote function can be located via a property `bigframes_remote_function`
    # set in the remote function object.
    print(f"Created BQ remote function: {get_bucket.bigframes_remote_function}")
    
    # The cloud function can be located via another property
    # `bigframes_cloud_function` set in the remote function object.
    print(f"Created cloud function: {get_bucket.bigframes_cloud_function}")
    
    # Warning: The deployed cloud function may be visible to other users with
    # sufficient privilege in the project, so the user should be careful about
    # having any sensitive data in the code that will be deployed as a remote
    # function.
    
    # Let's continue trying other potential use cases of remote functions. Let's
    # say we consider the `species`, `island` and `sex` of the penguins
    # sensitive information and want to redact that by replacing with their hash
    # code instead. Let's define another scalar custom function and decorate it
    # as a remote function. The custom function in this example has external
    # package dependency, which can be specified via `packages` parameter.
    @bpd.remote_function(
        reuse=False,
        packages=["cryptography"],
        cloud_function_service_account="default",
    )
    def get_hash(input: str) -> str:
        from cryptography.fernet import Fernet
    
        # handle missing value
        if input is None:
            input = ""
    
        key = Fernet.generate_key()
        f = Fernet(key)
        return f.encrypt(input.encode()).decode()
    
    # We can use this remote function in another `pandas`-like API `map` that
    # can be applied on a DataFrame
    df_redacted = df[["species", "island", "sex"]].map(get_hash)
    df_redacted.head(10)
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
