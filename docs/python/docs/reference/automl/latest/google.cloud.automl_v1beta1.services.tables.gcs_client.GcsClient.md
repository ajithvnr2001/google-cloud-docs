---
url: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.gcs_client.GcsClient
title: Class GcsClient (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:57:41.494423+00:00
---

# Class GcsClient (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.gcs_client.GcsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class GcsClient (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.1  2.19.0  2.18.1  2.17.0  2.16.4  2.15.0  2.14.1  2.13.5  2.12.0  2.11.4  2.10.1  2.9.0  2.8.3  2.7.3  2.6.0  2.5.2  2.4.2  2.3.0  2.2.0  2.1.0  2.0.0  1.0.3  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0 
    
    
    GcsClient(bucket_name=None, client=None, credentials=None, project=None)

Uploads Pandas DataFrame to a bucket in Google Cloud Storage.

## Methods 

### GcsClient
    
    
    GcsClient(bucket_name=None, client=None, credentials=None, project=None)

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`bucket_name` |  `Optional[str]`   
The name of Google Cloud Storage bucket for this client to send requests to.  
`client` |  `Optional[storage.Client]`   
A Google Cloud Storage Client instance.  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify this application to the service. If none are specified, the client will attempt to ascertain the credentials from the environment.  
`project` |  `Optional[str]`   
The project ID of the GCP project to attach to the underlying storage client. If none is specified, the client will attempt to ascertain the credentials from the environment.  
  
### ensure_bucket_exists
    
    
    ensure_bucket_exists(project, region)

Checks if a bucket named '{project}-automl-tables-staging' exists.

If this bucket doesn't exist, creates one. If this bucket already exists in `project`, do nothing. If this bucket exists in a different project that we don't have access to, creates a bucket named '{project}-automl-tables-staging-{create_timestamp}' because bucket's name must be globally unique. Save the created bucket's name and reuse this for future requests.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `str`   
The ID of the project that stores the bucket.  
`region` |  `str`   
The region of the bucket.  
  
### upload_pandas_dataframe
    
    
    upload_pandas_dataframe(dataframe, uploaded_csv_name=None)

Uploads a Pandas DataFrame as CSV to the bucket.

**Parameters**  
---  
**Name** | **Description**  
`dataframe` |  `pandas.DataFrame`   
The Pandas Dataframe to be uploaded.  
`uploaded_csv_name` |  `Optional[str]`   
The name for the uploaded CSV.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
