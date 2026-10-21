---
url: https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/lakes/deauthorize/
title: gcloud dataplex lakes deauthorize \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:56:27.215481+00:00
---

# gcloud dataplex lakes deauthorize  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/lakes/deauthorize/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud dataplex lakes deauthorize Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud dataplex lakes deauthorize - deauthorize a service agent from managing resources 
SYNOPSIS
    

`gcloud dataplex lakes deauthorize` (`--project-resource`=`PROJECT_RESOURCE` | `--storage-bucket-resource`=`STORAGE_BUCKET_RESOURCE` | `--bigquery-dataset-resource`=`BIGQUERY_DATASET_RESOURCE` `--secondary-project`=`SECONDARY_PROJECT`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     The service agent for the primary project will have its IAM role revoked from a secondary project, a Cloud Storage bucket, or a BigQuery dataset. 
EXAMPLES
     To deauthorize the service agent in project `test-project` from managing resources in the project `test-project2`, run: 
    
    
    gcloud dataplex lakes deauthorize --project=test-project --project-resource=test-project2

To deauthorize the service agent in project `test-project` from managing the Cloud Storage bucket `dataplex-storage-bucket`, run: 
    
    
    gcloud dataplex lakes deauthorize --project=test-project --storage-bucket-resource=dataplex-storage-bucket

To deauthorize the service agent in project `test-project` from managing the BigQuery dataset `test-dataset` in project `test-project2`, run: 
    
    
    gcloud dataplex lakes deauthorize --project=test-project --bigquery-dataset-resource=test-dataset --secondary-project=test-project2

REQUIRED FLAGS
    

The resource for which the service agent's role will be revoked. 

Exactly one of these must be specified: 

`--project-resource`=`PROJECT_RESOURCE`
     The identifier of the project whose resources the service agent will no longer manage. 
`--storage-bucket-resource`=`STORAGE_BUCKET_RESOURCE`
     The identifier of the Cloud Storage bucket that the service agent will no longer manage. 
Or at least one of these can be specified: 

Fields to identify the BigQuery dataset. 
`--bigquery-dataset-resource`=`BIGQUERY_DATASET_RESOURCE`
     The identifier of the BigQuery dataset that the service agent will no longer manage. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--secondary-project`=`SECONDARY_PROJECT`
     The identifier of the project where the BigQuery dataset is located. 

This flag argument must be specified if any of the other arguments in this group are specified. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud alpha dataplex lakes deauthorize](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/lakes/deauthorize)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
