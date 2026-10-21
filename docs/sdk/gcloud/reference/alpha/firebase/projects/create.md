---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firebase/projects/create/
title: gcloud alpha firebase projects create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:13.560140+00:00
---

# gcloud alpha firebase projects create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firebase/projects/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha firebase projects create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha firebase projects create - create and provision a new Firebase project and associated resources 
SYNOPSIS
    

`gcloud alpha firebase projects create` [`PROJECT`] [`--app-namespace`=`APP_NAMESPACE`] [`--async`] [`--display-name`=`DISPLAY_NAME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create and provision a new Firebase project and associated resources. 

Creates (provisions) a Firebase project and initializes a Firebase Web App in region us-west1. 

If a Google Cloud project ID is specified, Firebase is provisioned into that existing project. Otherwise, a new project ID is automatically generated and provisioned. 

EXAMPLES
     To provision a new Firebase project: 
    
    
    gcloud alpha firebase projects create --app-namespace=com.example.my_app --display-name="My Firebase App"

To provision Firebase for an existing Google Cloud project: 
    
    
    gcloud alpha firebase projects create my-project-id --display-name="My Firebase App"

To provision asynchronously: 
    
    
    gcloud alpha firebase projects create --display-name="My Firebase App" --async

POSITIONAL ARGUMENTS
    

[`PROJECT`]
     ID for the Google Cloud project in which to provision Firebase. If omitted, a new project ID will be automatically generated and provisioned. 
FLAGS
    

`--app-namespace`=`APP_NAMESPACE`
     Developer-assigned identifier for the web app to create. Defaults to a generated namespace based on project ID or display name. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--display-name`=`DISPLAY_NAME`
     The display name for the new Project and/or Web App. Defaults to project ID or "My Firebase App". 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-09 UTC."],[],[]] 
