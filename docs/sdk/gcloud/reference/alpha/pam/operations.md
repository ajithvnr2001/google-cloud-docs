---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/operations/
title: gcloud alpha pam operations \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:34.686540+00:00
---

# gcloud alpha pam operations  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha pam operations Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha pam operations - manage Privileged Access Manager Long Running Operations 
SYNOPSIS
    

`gcloud alpha pam operations` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` The `[gcloud pam operations](https://docs.cloud.google.com/sdk/gcloud/reference/pam/operations)` command group lets you manage Privileged Access Manager (PAM) operations. 
EXAMPLES
     To describe an operation with the full name ``OPERATION_NAME``, run: 
    
    
    [gcloud alpha pam operations describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/operations/describe) OPERATION_NAME

To list all operations in a project named `sample-project` and in location `global`, run: 
    
    
    [gcloud alpha pam operations list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/operations/list) --project=sample-project --location=global

To list all operations in a folder with ID ``FOLDER_ID`` and in location `global`, run: 
    
    
    [gcloud alpha pam operations list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/operations/list) --folder=FOLDER_ID --location=global

To list all operations in an organization with ID ``ORGANIZATION_ID`` and in location `global`, run: 
    
    
    [gcloud alpha pam operations list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/operations/list) --organization=ORGANIZATION_ID --location=global

To delete an operation with the full name ``OPERATION_NAME``, run: 
    
    
    [gcloud alpha pam operations delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/operations/delete) OPERATION_NAME

To poll an operation with the full name ``OPERATION_NAME``, run: 
    
    
    [gcloud alpha pam operations wait](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/operations/wait) OPERATION_NAME

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/operations/delete)`
     `(ALPHA)` Delete a Privileged Access Manager (PAM) long running operation. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/operations/describe)`
     `(ALPHA)` Show details of a Privileged Access Manager (PAM) long running operation. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/operations/list)`
     `(ALPHA)` List all Privileged Access Manager (PAM) long running operations under a location. 
`[wait](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/operations/wait)`
     `(ALPHA)` Poll a Privileged Access Manager (PAM) long running operation. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud pam operations](https://docs.cloud.google.com/sdk/gcloud/reference/pam/operations)
    
    
    [gcloud beta pam operations](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pam/operations)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
