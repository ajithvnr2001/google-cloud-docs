---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/billing/
title: gcloud alpha billing \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:43:47.362713+00:00
---

# gcloud alpha billing  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/billing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha billing Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha billing - manage billing accounts and associate them with projects 
SYNOPSIS
    

`gcloud alpha billing` `GROUP` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Manage billing accounts and associate them with projects. 
EXAMPLES
     To list billing accounts associated with the current user, run: 
    
    
    [gcloud alpha billing accounts list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/billing/accounts/list)

To link one of the billing accounts `0X0X0X-0X0X0X-0X0X0X` with a project `my-project`, run: 
    
    
    [gcloud alpha billing projects link](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/billing/projects/link) my-project --billing-account 0X0X0X-0X0X0X-0X0X0X

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[accounts](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/billing/accounts)`
     `(ALPHA)` Manage billing accounts. 
`[budgets](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/billing/budgets)`
     `(ALPHA)` Manage the budgets of your billing accounts. 
`[projects](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/billing/projects)`
     `(ALPHA)` Manage the billing account configuration of your projects. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud billing](https://docs.cloud.google.com/sdk/gcloud/reference/billing)
    
    
    [gcloud beta billing](https://docs.cloud.google.com/sdk/gcloud/reference/beta/billing)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
