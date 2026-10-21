---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/supported-permissions/
title: gcloud beta access-context-manager supported-permissions \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:43:03.156379+00:00
---

# gcloud beta access-context-manager supported-permissions  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/supported-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta access-context-manager supported-permissions Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta access-context-manager supported-permissions - retrieve VPC Service Controls Supported Permissions 
SYNOPSIS
    

`gcloud beta access-context-manager supported-permissions` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` The gcloud beta access-context-manager supported-permissions command group lets you list VPC Service Controls supported permissions. It also lets you describe which permissions in a provided role are supported by VPC Service Controls. 
EXAMPLES
     To see all VPC Service Controls supported permissions: 
    
    
    [gcloud beta access-context-manager supported-permissions list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/supported-permissions/list)

To see which permissions in a provided role are supported by VPC Service
    
    
    Controls:
    
    
    gcloud beta access-context-manager supported-permissions describe roles/example.role.name

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/supported-permissions/describe)`
     `(BETA)` Describes which permissions in a provided role are supported by VPC Service Controls. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/supported-permissions/list)`
     `(BETA)` Lists all VPC Service Controls supported permissions. 
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud access-context-manager supported-permissions](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/supported-permissions)
    
    
    [gcloud alpha access-context-manager supported-permissions](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/supported-permissions)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
