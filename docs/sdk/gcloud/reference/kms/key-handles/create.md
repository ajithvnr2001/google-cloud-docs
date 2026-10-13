---
url: https://docs.cloud.google.com/sdk/gcloud/reference/kms/key-handles/create/
title: gcloud kms key-handles create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:45.907587+00:00
---

# gcloud kms key-handles create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/kms/key-handles/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud kms key-handles create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud kms key-handles create - create a new KeyHandle 
SYNOPSIS
    

`gcloud kms key-handles create` `--location`=`LOCATION` `--resource-type`=`RESOURCE_TYPE` (`--generate-key-handle-id` | `--key-handle-id`=`KEY_HANDLE_ID`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Creates a new KeyHandle, triggering the provisioning of a new CryptoKey for CMEK use with the given resource type in the configured key project and the same location 
EXAMPLES
     The following command creates a KeyHandle named `my-key-handle` within the location `global` for the resource type `compute.googleapis.com/Disk`: 
    
    
    gcloud kms key-handles create --key-handle-id=my-key-handle --location=global --resource-type=compute.googleapis.com/Disk

To generate a random KeyHandle id, the `--generate-key-handle-id` flag can be used instead of `--key-handle-id`. 

REQUIRED FLAGS
    

Location resource - The KMS location resource. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--location` on the command line with a fully specified name; 
  * set the property `core/project`. 



This must be specified. 

`--location`=`LOCATION`
     ID of the location or fully qualified identifier for the location. 

To set the `location` attribute: 

  * provide the argument `--location` on the command line. 


`--resource-type`=`RESOURCE_TYPE`
     The resource type selector for KeyHandle resources of the form {SERVICE}.{UNIVERSE_DOMAIN}/{TYPE}. 
Exactly one of these must be specified: 

`--generate-key-handle-id`
     Generate a KeyHandle id for the new KeyHandle resource. 
`--key-handle-id`=`KEY_HANDLE_ID`
     The KeyHandle id for the new KeyHandle resource. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha kms key-handles create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/key-handles/create)
    
    
    [gcloud beta kms key-handles create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms/key-handles/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
