---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/service-accounts/
title: gcloud alpha iam service-accounts \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:27:59.134279+00:00
---

# gcloud alpha iam service-accounts  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/service-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha iam service-accounts Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha iam service-accounts - create and manipulate service accounts 
SYNOPSIS
    

`gcloud alpha iam service-accounts` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create and manipulate IAM service accounts. A service account is a special Google account that belongs to your application or a VM, instead of to an individual end user. Your application uses the service account to call the Google API of a service, so that the users aren't directly involved. 

Note: Service accounts use client quotas for tracking usage. 

More information on service accounts can be found at: <https://cloud.google.com/iam/docs/service-accounts>

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[config](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/service-accounts/config)`
     `(ALPHA)` Manage Iam service account configurations. 
`[keys](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/service-accounts/keys)`
     `(ALPHA)` Manage service account keys. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/service-accounts/add-iam-policy-binding)`
     `(ALPHA)` Add an IAM policy binding to an IAM service account. 
`[create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/service-accounts/create)`
     `(ALPHA)` Create a service account for a project. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/service-accounts/delete)`
     `(ALPHA)` Delete a service account from a project. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/service-accounts/describe)`
     `(ALPHA)` Show metadata for a service account from a project. 
`[disable](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/service-accounts/disable)`
     `(ALPHA)` Disable an IAM service account. 
`[enable](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/service-accounts/enable)`
     `(ALPHA)` Enable an IAM service account. 
`[get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/service-accounts/get-iam-policy)`
     `(ALPHA)` Get the IAM policy for a service account. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/service-accounts/list)`
     `(ALPHA)` List all of a project's service accounts. 
`[remove-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/service-accounts/remove-iam-policy-binding)`
     `(ALPHA)` Remove IAM policy binding from a service account. 
`[set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/service-accounts/set-iam-policy)`
     `(ALPHA)` Set IAM policy for a service account. 
`[sign-blob](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/service-accounts/sign-blob)`
     `(ALPHA)` Sign a blob with a managed service account key. 
`[sign-jwt](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/service-accounts/sign-jwt)`
     `(ALPHA)` Sign a JWT with a managed service account key. 
`[undelete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/service-accounts/undelete)`
     `(ALPHA)` Undelete a service account for a project. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/service-accounts/update)`
     `(ALPHA)` Update an IAM service account. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud iam service-accounts](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts)
    
    
    [gcloud beta iam service-accounts](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/service-accounts)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
