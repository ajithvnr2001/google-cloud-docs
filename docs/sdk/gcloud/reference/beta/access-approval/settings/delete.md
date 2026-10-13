---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-approval/settings/delete/
title: gcloud beta access-approval settings delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:14:34.320831+00:00
---

# gcloud beta access-approval settings delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-approval/settings/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta access-approval settings delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta access-approval settings delete - delete Access Approval settings 
SYNOPSIS
    

`gcloud beta access-approval settings delete` [`--folder`=`FOLDER` | `--organization`=`ORGANIZATION` | `--project`=`PROJECT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Delete the Access Approval settings associated with a project, a folder, or organization. 
EXAMPLES
     To delete the settings for the current project use 
    
    
    gcloud beta access-approval settings delete

To delete the settings for folder f1 use 
    
    
    gcloud beta access-approval settings delete --folder=f1

FLAGS
    

At most one of these can be specified: 

`--folder`=`FOLDER`
     Folder number. Only one of --project, --folder, or --organization can be provided. If none are provided then it uses config property [core/project]. 
`--organization`=`ORGANIZATION`
     Organization number. Either --project, --folder, or --organization must be provided. If none are provided then it uses config property [core/project]. 
`--project`=`PROJECT`
     Project number or id. Only one of --project, --folder, or --organization can be provided. If none are provided then it uses config property [core/project]. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud access-approval settings delete](https://docs.cloud.google.com/sdk/gcloud/reference/access-approval/settings/delete)
    
    
    [gcloud alpha access-approval settings delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/access-approval/settings/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
