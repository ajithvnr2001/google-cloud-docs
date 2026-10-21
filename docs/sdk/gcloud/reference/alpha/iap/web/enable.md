---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iap/web/enable/
title: gcloud alpha iap web enable \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:40:20.461894+00:00
---

# gcloud alpha iap web enable  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iap/web/enable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha iap web enable Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha iap web enable - enable Cloud Identity-Aware Proxy (Cloud IAP) on an IAP resource 
SYNOPSIS
    

`gcloud alpha iap web enable` [`--oauth2-client-id`=`OAUTH2_CLIENT_ID` `--oauth2-client-secret`=`OAUTH2_CLIENT_SECRET`] [`--resource-type`=`RESOURCE_TYPE` : `--region`=`REGION` `--service`=`SERVICE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` This command enables Cloud Identity-Aware Proxy on an IAP resource. OAuth 2.0 credentials must be set, or must have been previously set, to enable IAP. 
EXAMPLES
     To enable IAP on an App Engine application, run: 
    
    
    gcloud alpha iap web enable --resource-type=app-engine --oauth2-client-id=CLIENT_ID --oauth2-client-secret=SECRET

To enable IAP on a global backend service, run: 
    
    
    gcloud alpha iap web enable --resource-type=backend-services --oauth2-client-id=CLIENT_ID --oauth2-client-secret=SECRET --service=SERVICE_ID

To enable IAP on a region backend service, run: 
    
    
    gcloud alpha iap web enable --resource-type=backend-services --oauth2-client-id=CLIENT_ID --oauth2-client-secret=SECRET --service=SERVICE_ID --region=REGION

FLAGS
    

`--oauth2-client-id`=`OAUTH2_CLIENT_ID`
     OAuth 2.0 client ID to use. 
`--oauth2-client-secret`=`OAUTH2_CLIENT_SECRET`
     OAuth 2.0 client secret to use. 
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
    
    
    [gcloud iap web enable](https://docs.cloud.google.com/sdk/gcloud/reference/iap/web/enable)
    
    
    [gcloud beta iap web enable](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iap/web/enable)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
