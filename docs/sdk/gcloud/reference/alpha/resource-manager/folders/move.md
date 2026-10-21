---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-manager/folders/move/
title: gcloud alpha resource-manager folders move \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:51:54.703647+00:00
---

# gcloud alpha resource-manager folders move  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-manager/folders/move/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha resource-manager folders move Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha resource-manager folders move - move a folder to a new position within the same organization 
SYNOPSIS
    

`gcloud alpha resource-manager folders move` `FOLDER_ID` [`--async`] [`--folder`=`FOLDER_ID`] [`--organization`=`ORGANIZATION_ID`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Move the given folder under a new parent folder or under the organization. Exactly one of --folder or --organization must be provided. 

This command can fail for the following reasons: 

  * There is no folder with the given ID. 
  * There is no parent with the given type and ID. 
  * The new parent is not in the same organization of the given folder. 
  * Permission missing for performing this move. 


EXAMPLES
     The following command moves a folder with the ID `123456789` into a folder with the ID `2345`: 
    
    
    gcloud alpha resource-manager folders move 123456789 --folder=2345

The following command moves a folder with the ID `123456789` into an organization with ID `1234`: 
    
    
    gcloud alpha resource-manager folders move 123456789 --organization=1234

POSITIONAL ARGUMENTS
    

`FOLDER_ID`
     ID for the folder you want to move. 
FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--folder`=`FOLDER_ID`
     ID for the folder to use as a parent 
`--organization`=`ORGANIZATION_ID`
     ID for the organization to use as a parent 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud resource-manager folders move](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/folders/move)
    
    
    [gcloud beta resource-manager folders move](https://docs.cloud.google.com/sdk/gcloud/reference/beta/resource-manager/folders/move)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
