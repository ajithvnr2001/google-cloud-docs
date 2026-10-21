---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iap/web/disable/
title: gcloud alpha iap web disable \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:40:19.985692+00:00
---

# gcloud alpha iap web disable  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iap/web/disable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha iap web disable Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha iap web disable - disable Cloud Identity-Aware Proxy (Cloud IAP) on an IAP resource 
SYNOPSIS
    

`gcloud alpha iap web disable` [`--resource-type`=`RESOURCE_TYPE` : `--region`=`REGION` `--service`=`SERVICE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` This command disables Cloud Identity-Aware Proxy on an IAP resource. Disabling IAP does not clear the OAuth 2.0 credentials. 
EXAMPLES
     To disable IAP on an App Engine application, run: 
    
    
    gcloud alpha iap web disable --resource-type=app-engine

To disable IAP on a global backend service, run: 
    
    
    gcloud alpha iap web disable --resource-type=backend-services --service=SERVICE_ID

To disable IAP on a region backend service, run: 
    
    
    gcloud alpha iap web disable --resource-type=backend-services --service=SERVICE_ID --region=REGION

FLAGS
    

`--resource-type`=`RESOURCE_TYPE`
     Resource type of the IAP resource. `RESOURCE_TYPE` must be one of: `app-engine`, `backend-services`. 
`--region`=`REGION`
     Region name. Not applicable for ``app-engine``. Optional when ``resource-type`` is ``compute``. 
`--service`=`SERVICE`
     Service name. Required with `--resource-type=backend-services`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud iap web disable](https://docs.cloud.google.com/sdk/gcloud/reference/iap/web/disable)
    
    
    [gcloud beta iap web disable](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iap/web/disable)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
