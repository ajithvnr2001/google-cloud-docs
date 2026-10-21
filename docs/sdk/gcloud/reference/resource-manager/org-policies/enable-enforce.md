---
url: https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/enable-enforce/
title: gcloud resource-manager org-policies enable-enforce \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:11:47.699978+00:00
---

# gcloud resource-manager org-policies enable-enforce  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/enable-enforce/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud resource-manager org-policies enable-enforce Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud resource-manager org-policies enable-enforce - turns on enforcement of boolean Organization Policy constraint 
SYNOPSIS
    

`gcloud resource-manager org-policies enable-enforce` `ORG_POLICY_ID` (`--folder`=`FOLDER_ID` | `--organization`=`ORGANIZATION_ID` | `--project`=`PROJECT_ID`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Turns on enforcement of a boolean Organization Policy constraint at the specified resource. 
EXAMPLES
     The following command enables enforcement of the Organization Policy boolean constraint `compute.disableSerialPortAccess` on project `foo-project`: 
    
    
    gcloud resource-manager org-policies enable-enforce compute.disableSerialPortAccess --project=foo-project

POSITIONAL ARGUMENTS
    

`ORG_POLICY_ID`
     The Org Policy constraint name. 
REQUIRED FLAGS
    

Resource that is associated with the organization policy. 

Exactly one of these must be specified: 

`--folder`=`FOLDER_ID`
     Folder ID. 
`--organization`=`ORGANIZATION_ID`
     Organization ID. 
`--project`=`PROJECT_ID`
     Project ID. Overrides the default `core/project` property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha resource-manager org-policies enable-enforce](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-manager/org-policies/enable-enforce)
    
    
    [gcloud beta resource-manager org-policies enable-enforce](https://docs.cloud.google.com/sdk/gcloud/reference/beta/resource-manager/org-policies/enable-enforce)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
