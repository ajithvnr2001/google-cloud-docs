---
url: https://docs.cloud.google.com/sdk/gcloud/reference/edge-cloud/api-keys/create/
title: gcloud edge-cloud api-keys create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:18:43.756562+00:00
---

# gcloud edge-cloud api-keys create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/edge-cloud/api-keys/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud edge-cloud api-keys create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud edge-cloud api-keys create - create a Google Distributed Cloud API key 
SYNOPSIS
    

`gcloud edge-cloud api-keys create` (`API_KEY` : `--location`=`LOCATION`) `--service-account`=`SERVICE_ACCOUNT` `--zone`=`ZONE` [`--api-target`=[`KEY`=`VALUE`,…]] [`--async`] [`--validity`=`VALIDITY`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Creates a Google Distributed Cloud API key. 
EXAMPLES
     To create a service-account-bound API key in a specific Google Distributed Cloud zone that is valid for two hours and restricted to specific API methods, run: 
    
    
    gcloud edge-cloud api-keys create my-api-key --location=us-central1 --project=my-project --zone=us-central1-edge-zone1 --service-account=my-sa --validity=7200s --api-target service="compute.test-api.com",methods="*" --api-target service="storage.test-api.com",methods="GET|LIST"

POSITIONAL ARGUMENTS
    

ApiKey resource - The API key to be created. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `api_key` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`API_KEY`
     ID of the apiKey or fully qualified identifier for the apiKey. 

To set the `api_key` attribute: 

  * provide the argument `api_key` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location name. 

To set the `location` attribute: 

  * provide the argument `api_key` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--service-account`=`SERVICE_ACCOUNT`
     The ID of the service account to bind the API key to. 
`--zone`=`ZONE`
     The Google Distributed Cloud zone ID where the API key will be created. 
OPTIONAL FLAGS
    

`--api-target`=[`KEY`=`VALUE`,…]
     API target restriction. Can be specified multiple times. Each instance is a comma-separated list of key=value pairs. 

  * Required keys: 'service'. 
  * Optional keys: 'methods'. 'methods' should be a pipe-separated string. Omit the 'methods' key to allow all methods. 



Examples: 

  * `--api-target service="compute.test-api.com",methods="*"`
  * `--api-target service="storage.test-api.com",methods="GET|LIST"`
  * `--api-target service="pubsub.test-api.com"`


`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--validity`=`VALIDITY`
     The validity duration for the key (e.g., 3600s, 1h, 1d). Default and maximum allowed is 366d. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `edgecontainer/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/edge-cloud>
NOTES
     This variant is also available: 
    
    
    [gcloud alpha edge-cloud api-keys create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/edge-cloud/api-keys/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
