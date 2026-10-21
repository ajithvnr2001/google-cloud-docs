---
url: https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/create/
title: gcloud ai endpoints create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:44.487820+00:00
---

# gcloud ai endpoints create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud ai endpoints create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud ai endpoints create - create a new Vertex AI endpoint 
SYNOPSIS
    

`gcloud ai endpoints create` `--display-name`=`DISPLAY_NAME` [`--description`=`DESCRIPTION`] [`--encryption-kms-key-name`=`ENCRYPTION_KMS_KEY_NAME`] [`--endpoint-id`=`ENDPOINT_ID`] [`--labels`=[`KEY`=`VALUE`,…]] [`--network`=`NETWORK`] [`--region`=`REGION`] [`--request-response-logging-rate`=`REQUEST_RESPONSE_LOGGING_RATE` `--request-response-logging-table`=`REQUEST_RESPONSE_LOGGING_TABLE`] [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To create an endpoint under project ``example`` in region ``us-central1``, run: 
    
    
    gcloud ai endpoints create --project=example --region=us-central1 --display-name=my_endpoint

REQUIRED FLAGS
    

`--display-name`=`DISPLAY_NAME`
     Display name of the endpoint. 
OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     Description of the endpoint. 
`--encryption-kms-key-name`=`ENCRYPTION_KMS_KEY_NAME`
     The Cloud KMS resource identifier of the customer managed encryption key used to protect a resource. Has the form: projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key. 

The key needs to be in the same region as where the compute resource is created. 

`--endpoint-id`=`ENDPOINT_ID`
     User-specified ID of the endpoint. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--network`=`NETWORK`
     The full name of the Google Compute Engine network to which the endpoint should be peered. 
Region resource - Cloud region to create endpoint. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--region` on the command line with a fully specified name; 
  * set the property `ai/region` with a fully specified name; 
  * choose one from the prompted list of available regions with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--region`=`REGION`
     ID of the region or fully qualified identifier for the region. 

To set the `region` attribute: 

  * provide the argument `--region` on the command line; 
  * set the property `ai/region`; 
  * choose one from the prompted list of available regions. 


`--request-response-logging-rate`=`REQUEST_RESPONSE_LOGGING_RATE`
     Prediction request & response sampling rate for logging to BigQuery table. 
`--request-response-logging-table`=`REQUEST_RESPONSE_LOGGING_TABLE`
     BigQuery table uri for prediction request & response logging. 

You can provide table uri that does not exist, it will be created for you. 

Value should be provided in format: bq://``PROJECT_ID``/``DATASET``/``TABLE``

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha ai endpoints create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/create)
    
    
    [gcloud beta ai endpoints create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
