---
url: https://docs.cloud.google.com/sdk/gcloud/reference/iap/oauth-brands/create/
title: gcloud iap oauth-brands create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:13:25.826696+00:00
---

# gcloud iap oauth-brands create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/iap/oauth-brands/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud iap oauth-brands create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud iap oauth-brands create - create a Cloud OAuth brand for the project 
SYNOPSIS
    

`gcloud iap oauth-brands create` `--application_title`=`APPLICATION_TITLE` `--support_email`=`SUPPORT_EMAIL` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(DEPRECATED)` This command is deprecated and will be non-functional after the IAP OAuth Admin APIs are turned down. Jan 19, 2026: Google will discontinue support for the IAP OAuth Admin APIs. New projects will not be able to use these APIs. March 19, 2026: The IAP OAuth Admin APIs will be permanently shut down. Access to this feature will no longer be available. 

`gcloud iap oauth-brands create` is used to create a Cloud OAuth brand for the project. The brand is 'internal only', meaning OAuth clients created under it only accept requests from users who belong to the same G Suite account as the project. The brand is created in unreviewed status. Your domain will not appear on the OAuth consent screen until it is reviewed after you manually start a review process in Google Cloud Platform Console. Note that the 'internal only' setting can be manually changed in Google Cloud Platform Console (https://console.cloud.google.com/apis/credentials/consent). A project can only have one brand. 

EXAMPLES
     To create a Cloud OAuth brand for the current project, run: 
    
    
    gcloud iap oauth-brands create --application_title=APPLICATION_TITLE --support_email=SUPPORT_EMAIL

To create a Cloud OAuth brand for the project PROJECT_ID, run: 
    
    
    gcloud iap oauth-brands create --application_title=APPLICATION_TITLE --support_email=SUPPORT_EMAIL --project=PROJECT_ID

REQUIRED FLAGS
    

`--application_title`=`APPLICATION_TITLE`
     Application name displayed on the OAuth consent screen. 
`--support_email`=`SUPPORT_EMAIL`
     Support email displayed on the OAuth consent screen. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `iap/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/iap>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha iap oauth-brands create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iap/oauth-brands/create)
    
    
    [gcloud beta iap oauth-brands create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iap/oauth-brands/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
