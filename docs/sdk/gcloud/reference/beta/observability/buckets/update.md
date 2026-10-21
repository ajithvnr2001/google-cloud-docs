---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/observability/buckets/update/
title: gcloud beta observability buckets update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:30:30.468967+00:00
---

# gcloud beta observability buckets update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/observability/buckets/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta observability buckets update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta observability buckets update - update a bucket 
SYNOPSIS
    

`gcloud beta observability buckets update` (`BUCKET` : `--location`=`LOCATION`) [`--async`] [`--description`=`DESCRIPTION`] [`--display-name`=`DISPLAY_NAME`] [`--clear-cmek-settings` `--cmek-settings-kms-key`=`CMEK_SETTINGS_KMS_KEY`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update an Observability Bucket. 
EXAMPLES
     To update a bucket, run: 
    
    
    gcloud beta observability buckets update my-bucket --location=us-central1 --display-name="My Bucket"

POSITIONAL ARGUMENTS
    

Bucket resource - Identifier. Name of the bucket. The format is: 
    
    
    projects/[PROJECT_ID]/locations/[LOCATION]/buckets/[BUCKET_ID] The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways.

To set the `project` attribute: 

  * provide the argument `bucket` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`BUCKET`
     ID of the bucket or fully qualified identifier for the bucket. 

To set the `bucket` attribute: 

  * provide the argument `bucket` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the bucket resource. 

To set the `location` attribute: 

  * provide the argument `bucket` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     Description of the bucket. 
`--display-name`=`DISPLAY_NAME`
     User friendly display name. 
Settings for configuring CMEK for a bucket. 
`--clear-cmek-settings`
     Set bucket.cmekSettings back to default value. 
`--cmek-settings-kms-key`=`CMEK_SETTINGS_KMS_KEY`
     The resource name for the configured Cloud KMS key. The format is: 
    
    
    projects/[PROJECT_ID]/locations/[LOCATION]/keyRings/[KEYRING]/cryptoKeys/[KEY]

For example: 
    
    
    projects/my-project/locations/us-central1/keyRings/my-ring/cryptoKeys/my-key

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `observability/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/stackdriver/docs/>
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud observability buckets update](https://docs.cloud.google.com/sdk/gcloud/reference/observability/buckets/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
