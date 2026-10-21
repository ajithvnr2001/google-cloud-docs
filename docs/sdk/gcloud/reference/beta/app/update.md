---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/update/
title: gcloud beta app update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:14:02.118997+00:00
---

# gcloud beta app update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta app update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta app update - updates an App Engine application 
SYNOPSIS
    

`gcloud beta app update` [`--service-account`=`SERVICE_ACCOUNT`] [`--[no-]split-health-checks`] [`--ssl-policy`=`SSL_POLICY`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` This command is used to update settings on an app engine application. 
EXAMPLES
     To enable split health checks on an application: 
    
    
    gcloud beta app update --split-health-checks

To update the app-level service account on an application: 
    
    
    gcloud beta app update --service-account=SERVICE_ACCOUNT

To update the app-level minimum SSL policy of the application: 
    
    
    gcloud beta app update --ssl-policy=TLS_VERSION_1_2

FLAGS
    

`--service-account`=`SERVICE_ACCOUNT`
     The app-level default service account to update the app with. 
`--[no-]split-health-checks`
     Enables/disables split health checks by default on new deployments. Use `--split-health-checks` to enable and `--no-split-health-checks` to disable. 
`--ssl-policy`=`SSL_POLICY`
     The app-level SSL policy to update the app with. `SSL_POLICY` must be one of: `TLS_VERSION_1_0`, `TLS_VERSION_1_2`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud app update](https://docs.cloud.google.com/sdk/gcloud/reference/app/update)
    
    
    [gcloud alpha app update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/app/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
