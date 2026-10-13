---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/
title: gcloud alpha pam \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:44:00.118601+00:00
---

# gcloud alpha pam  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha pam Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha pam - manage Privileged Access Manager entitlements and grants 
SYNOPSIS
    

`gcloud alpha pam` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` The `[gcloud pam](https://docs.cloud.google.com/sdk/gcloud/reference/pam)` command group lets you manage Privileged Access Manager (PAM) entitlements and grants. 
EXAMPLES
     To check the PAM onboarding status for a project named `sample-project` and in location `global`, run: 
    
    
    [gcloud alpha pam check-onboarding-status](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/check-onboarding-status) --project=sample-project --location=global

To check the PAM onboarding status for a folder with ID ``FOLDER_ID`` and in location `global`, run: 
    
    
    [gcloud alpha pam check-onboarding-status](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/check-onboarding-status) --folder=FOLDER_ID --location=global

To check the PAM onboarding status for an organization with ID ``ORGANIZATION_ID`` and in location `global`, run: 
    
    
    [gcloud alpha pam check-onboarding-status](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/check-onboarding-status) --organization=ORGANIZATION_ID --location=global

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[entitlements](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements)`
     `(ALPHA)` Manage Privileged Access Manager (PAM) entitlements. 
`[grants](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/grants)`
     `(ALPHA)` Manage Privileged Access Manager (PAM) grants. 
`[operations](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/operations)`
     `(ALPHA)` Manage Privileged Access Manager (PAM) Long Running Operations. 
`[settings](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/settings)`
     `(ALPHA)` Manage Privileged Access Manager (PAM) Settings. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[check-onboarding-status](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/check-onboarding-status)`
     `(ALPHA)` Check Privileged Access Manager (PAM) onboarding status for a resource. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud pam](https://docs.cloud.google.com/sdk/gcloud/reference/pam)
    
    
    [gcloud beta pam](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pam)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
