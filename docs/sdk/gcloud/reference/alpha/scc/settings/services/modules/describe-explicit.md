---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/settings/services/modules/describe-explicit/
title: gcloud alpha scc settings services modules describe-explicit \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:49:11.757020+00:00
---

# gcloud alpha scc settings services modules describe-explicit  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/settings/services/modules/describe-explicit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha scc settings services modules describe-explicit Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha scc settings services modules describe-explicit - display module settings of Security Command Center(SCC)
SYNOPSIS
    

`gcloud alpha scc settings services modules describe-explicit` `--module`=`MODULE_NAME` `--service`=`SERVICE_NAME` [`--folder`=`FOLDER_ID` | `--organization`=`ORGANIZATION_ID` | `--project`=`PROJECT_ID`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Describe explicit module settings of Security Command Center(SCC). 
EXAMPLES
     To describe the explict 'OPEN_FIREWALL' module setting in service 'SECURITY_HEALTH_ANALYTICS' of project "12345", run: 
    
    
    gcloud alpha scc settings services modules describe-explicit --project=12345 --service=SECURITY_HEALTH_ANALYTICS --module=OPEN_FIREWALL

REQUIRED FLAGS
    

`--module`=`MODULE_NAME`
     Module name in Security Command Center 
`--service`=`SERVICE_NAME`
     Service name in Security Command Center. `SERVICE_NAME` must be one of: `container-threat-detection`, `event-threat-detection`, `security-health-analytics`, `virtual-machine-threat-detection`, `web-security-scanner`. 
OPTIONAL FLAGS
    

At most one of these can be specified: 

`--folder`=`FOLDER_ID`
     Folder ID 
`--organization`=`ORGANIZATION_ID`
     Organization ID 
`--project`=`PROJECT_ID`
     Project ID 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
