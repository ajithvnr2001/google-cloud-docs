---
url: https://docs.cloud.google.com/sdk/gcloud/reference/billing/
title: gcloud billing \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:34:29.627156+00:00
---

# gcloud billing  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/billing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud billing Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud billing - manage billing accounts and associate them with projects 
SYNOPSIS
    

`gcloud billing` `GROUP` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Manage billing accounts and associate them with projects. 
EXAMPLES
     To list billing accounts associated with the current user, run: 
    
    
    [gcloud billing accounts list](https://docs.cloud.google.com/sdk/gcloud/reference/billing/accounts/list)

To link one of the billing accounts `0X0X0X-0X0X0X-0X0X0X` with a project `my-project`, run: 
    
    
    [gcloud billing projects link](https://docs.cloud.google.com/sdk/gcloud/reference/billing/projects/link) my-project --billing-account 0X0X0X-0X0X0X-0X0X0X

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[accounts](https://docs.cloud.google.com/sdk/gcloud/reference/billing/accounts)`
     Manage billing accounts. 
`[budgets](https://docs.cloud.google.com/sdk/gcloud/reference/billing/budgets)`
     Manage the budgets of your billing accounts. 
`[projects](https://docs.cloud.google.com/sdk/gcloud/reference/billing/projects)`
     Manage the billing account configuration of your projects. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha billing](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/billing)
    
    
    [gcloud beta billing](https://docs.cloud.google.com/sdk/gcloud/reference/beta/billing)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
