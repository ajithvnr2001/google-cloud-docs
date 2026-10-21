---
url: https://docs.cloud.google.com/sdk/gcloud/reference/iap/oauth-clients/create/
title: gcloud iap oauth-clients create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:13:30.111868+00:00
---

# gcloud iap oauth-clients create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/iap/oauth-clients/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud iap oauth-clients create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud iap oauth-clients create - create a Cloud IAP OAuth client in the project 
SYNOPSIS
    

`gcloud iap oauth-clients create` `BRAND` `--display_name`=`DISPLAY_NAME` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(DEPRECATED)` This command is deprecated and will be non-functional after the IAP OAuth Admin APIs are turned down. Jan 19, 2026: Google will discontinue support for the IAP OAuth Admin APIs. New projects will not be able to use these APIs. March 19, 2026: The IAP OAuth Admin APIs will be permanently shut down. Access to this feature will no longer be available. 

`gcloud iap oauth-clients create` is used to create an OAuth client in the project to be used by Cloud IAP. To call this command, the Cloud OAuth brand for the project must exist and be set for 'internal only'. The new client is owned by Cloud IAP. 

EXAMPLES
     To create a Cloud IAP OAuth client for the current project, run: 
    
    
    gcloud iap oauth-clients create BRAND --display_name=DISPLAY_NAME

To create a Cloud IAP OAuth client for the project PROJECT_ID, run: 
    
    
    gcloud iap oauth-clients create BRAND --display_name=DISPLAY_NAME --project=PROJECT_ID

POSITIONAL ARGUMENTS
    

Brand resource - Name of the Cloud OAuth brand to create a Cloud IAP OAuth client under. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `brand` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`BRAND`
     ID of the brand or fully qualified identifier for the brand. 

To set the `brand` attribute: 

  * provide the argument `brand` on the command line. 


REQUIRED FLAGS
    

`--display_name`=`DISPLAY_NAME`
     User friendly name for the Cloud IAP OAuth client. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `iap/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/iap>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha iap oauth-clients create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iap/oauth-clients/create)
    
    
    [gcloud beta iap oauth-clients create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iap/oauth-clients/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
