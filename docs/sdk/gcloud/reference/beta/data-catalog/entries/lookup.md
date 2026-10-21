---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-catalog/entries/lookup/
title: gcloud beta data-catalog entries lookup \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:40.296543+00:00
---

# gcloud beta data-catalog entries lookup  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-catalog/entries/lookup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta data-catalog entries lookup Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta data-catalog entries lookup - lookup a Data Catalog entry by its target name 
SYNOPSIS
    

`gcloud beta data-catalog entries lookup` `RESOURCE` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `(DEPRECATED)` This command is deprecated. Please use `[gcloud dataplex entries](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/entries)` instead. 

Lookup a Data Catalog entry by its target name. 

EXAMPLES
     To lookup the entry for a Cloud Pub/Sub topic by its Google Cloud Platform resource name, run: 
    
    
    gcloud beta data-catalog entries lookup //pubsub.googleapis.com/projects/project1/topics/topic1

To lookup the entry for a Cloud Pub/Sub topic by its SQL name, run: 
    
    
    gcloud beta data-catalog entries lookup 'pubsub.topic.`my-project1`.topic1'

To lookup the entry for a BigQuery table by its SQL name, run: 
    
    
    gcloud beta data-catalog entries lookup 'bigquery.table.`my-project1`.my_dataset.my_table'

POSITIONAL ARGUMENTS
    

`RESOURCE`
     The name of the target resource to lookup. This can be either the Google Cloud Platform resource name or the SQL name of a Google Cloud Platform resource. SQL names follow Standard SQL lexical structure: <https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical>
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `datacatalog/v1beta1` API. The full documentation for this API can be found at: <https://cloud.google.com/data-catalog/docs/>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud data-catalog entries lookup](https://docs.cloud.google.com/sdk/gcloud/reference/data-catalog/entries/lookup)
    
    
    [gcloud alpha data-catalog entries lookup](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/data-catalog/entries/lookup)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
