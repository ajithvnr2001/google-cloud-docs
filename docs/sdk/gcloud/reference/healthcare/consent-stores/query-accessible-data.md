---
url: https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/query-accessible-data/
title: gcloud healthcare consent-stores query-accessible-data \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:19.934952+00:00
---

# gcloud healthcare consent-stores query-accessible-data  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/query-accessible-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud healthcare consent-stores query-accessible-data Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud healthcare consent-stores query-accessible-data - queries all accessible data IDs 
SYNOPSIS
    

`gcloud healthcare consent-stores query-accessible-data` (`CONSENT_STORE` : `--dataset`=`DATASET` `--location`=`LOCATION`) `--gcs-uri`=`GCS_URI` [`--async`] [`--request-attributes`=[`KEY`=`VALUE`,…]] [`--resource-attributes`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Queries all data IDs that are consented for a given use in the given Cloud Healthcare API consent store and writes them to a specified destination. 
EXAMPLES
     To query all data IDs in the consent-store 'test-consent-store' that can be used given request attributes {"organization":"admins", "use_case":"research"} and resource attributes {"anonymity":"identified"}, and write the result file to "gs://test-bucket/folder", run: 
    
    
    gcloud healthcare consent-stores query-accessible-data test-consent-store --gcs-uri=gs://test-bucket/folder --request-attributes=organization=admins,use_case=research --resource-attributes=anonymity=identified --dataset=test-dataset

POSITIONAL ARGUMENTS
    

ConsentStore resource - Cloud Healthcare API consent store to retrieve user data mappings from. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `consent_store` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CONSENT_STORE`
     ID of the consentStore or fully qualified identifier for the consentStore. 

To set the `consent_store` attribute: 

  * provide the argument `consent_store` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--dataset`=`DATASET`
     Cloud Healthcare dataset. 

To set the `dataset` attribute: 

  * provide the argument `consent_store` on the command line with a fully specified name; 
  * provide the argument `--dataset` on the command line. 


`--location`=`LOCATION`
     Google Cloud location. 

To set the `location` attribute: 

  * provide the argument `consent_store` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `healthcare/location`. 


REQUIRED FLAGS
    

`--gcs-uri`=`GCS_URI`
     The Cloud Storage destination for the result file. The Cloud Healthcare API service account must have the `roles/storage.objectAdmin` Cloud IAM role for this Cloud Storage location. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--request-attributes`=[`KEY`=`VALUE`,…]
     Comma-separated list of request attributes associated with this access request. Each attribute has the form "KEY=VALUE". 
`--resource-attributes`=[`KEY`=`VALUE`,…]
     Comma-separated list of resources attributes associated with the type of data being requested. Each attribute has the form "KEY=VALUE". If no values are specified, then all data types are included in the output. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `healthcare/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/healthcare>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha healthcare consent-stores query-accessible-data](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/healthcare/consent-stores/query-accessible-data)
    
    
    [gcloud beta healthcare consent-stores query-accessible-data](https://docs.cloud.google.com/sdk/gcloud/reference/beta/healthcare/consent-stores/query-accessible-data)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
