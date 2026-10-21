---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/projects/move/
title: gcloud beta projects move \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:20:59.826682+00:00
---

# gcloud beta projects move  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/projects/move/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta projects move Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta projects move - move a project into an organization 
SYNOPSIS
    

`gcloud beta projects move` `PROJECT_ID_OR_NUMBER` [`--folder`=`FOLDER_ID`] [`--organization`=`ORGANIZATION_ID`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Moves the given project into the given organization. 

This command can fail for the following reasons: 

  * There is no project with the given ID. 
  * There is no organization with the given ID, if an organization is given as the destination. 
  * There is no folder with the given ID, if a folder is given as the destination. 
  * More than one of organization or folder is provided. 
  * The active account does not have the resourcemanager.projects.update permission for the given project. 
  * The active account does not have the resourcemanager.projects.create permission for the given organization. 
  * The given project is already in an organization. 


EXAMPLES
     The following command moves a project with the ID `super-awesome-project` into the organization `25872158`: 
    
    
    gcloud beta projects move super-awesome-project --organization=25872158

POSITIONAL ARGUMENTS
    

`PROJECT_ID_OR_NUMBER`
     ID or number for the project you want to move. 
FLAGS
    

`--folder`=`FOLDER_ID`
     ID for the folder to use as a parent 
`--organization`=`ORGANIZATION_ID`
     ID for the organization to use as a parent 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha projects move](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/projects/move)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
