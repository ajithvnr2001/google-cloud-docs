---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/lakes/authorize/
title: gcloud alpha dataplex lakes authorize \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:17:48.408177+00:00
---

# gcloud alpha dataplex lakes authorize  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/lakes/authorize/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dataplex lakes authorize Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dataplex lakes authorize - authorize a service agent to manage resources 
SYNOPSIS
    

`gcloud alpha dataplex lakes authorize` (`--project-resource`=`PROJECT_RESOURCE` | `--storage-bucket-resource`=`STORAGE_BUCKET_RESOURCE` | `--bigquery-dataset-resource`=`BIGQUERY_DATASET_RESOURCE` `--secondary-project`=`SECONDARY_PROJECT`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` The service agent for the primary project will be granted an IAM role on a secondary project, a Cloud Storage bucket, or a BigQuery dataset. 
EXAMPLES
     To authorize the service agent in project `test-project` to manage resources in the project `test-project2`, run: 
    
    
    gcloud alpha dataplex lakes authorize --project=test-project --project-resource=test-project2

To authorize the service agent in project `test-project` to manage the Cloud Storage bucket `dataplex-storage-bucket`, run: 
    
    
    gcloud alpha dataplex lakes authorize --project=test-project --storage-bucket-resource=dataplex-storage-bucket

To authorize the service agent in project `test-project` to manage the BigQuery dataset `test-dataset` in project `test-project2`, run: 
    
    
    gcloud alpha dataplex lakes authorize --project=test-project --bigquery-dataset-resource=test-dataset --secondary-project=test-project2

REQUIRED FLAGS
    

The resource on which to grant a role to the service agent. 

Exactly one of these must be specified: 

`--project-resource`=`PROJECT_RESOURCE`
     The identifier of the project whose resources the service agent will manage. 
`--storage-bucket-resource`=`STORAGE_BUCKET_RESOURCE`
     The identifier of the Cloud Storage bucket that the service agent will manage. 
Or at least one of these can be specified: 

Fields to identify the BigQuery dataset. 
`--bigquery-dataset-resource`=`BIGQUERY_DATASET_RESOURCE`
     The identifier of the BigQuery dataset that the service agent will manage. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--secondary-project`=`SECONDARY_PROJECT`
     The identifier of the project where the BigQuery dataset is located. 

This flag argument must be specified if any of the other arguments in this group are specified. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud dataplex lakes authorize](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/lakes/authorize)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
