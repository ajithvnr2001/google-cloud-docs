---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/service-accounts/
title: gcloud beta iam service-accounts \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:59:47.752688+00:00
---

# gcloud beta iam service-accounts  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/service-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta iam service-accounts Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta iam service-accounts - create and manipulate service accounts 
SYNOPSIS
    

`gcloud beta iam service-accounts` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create and manipulate IAM service accounts. A service account is a special Google account that belongs to your application or a VM, instead of to an individual end user. Your application uses the service account to call the Google API of a service, so that the users aren't directly involved. 

Note: Service accounts use client quotas for tracking usage. 

More information on service accounts can be found at: <https://cloud.google.com/iam/docs/service-accounts>

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[keys](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/service-accounts/keys)`
     `(BETA)` Manage service account keys. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/service-accounts/add-iam-policy-binding)`
     `(BETA)` Add an IAM policy binding to an IAM service account. 
`[create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/service-accounts/create)`
     `(BETA)` Create a service account for a project. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/service-accounts/delete)`
     `(BETA)` Delete a service account from a project. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/service-accounts/describe)`
     `(BETA)` Show metadata for a service account from a project. 
`[disable](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/service-accounts/disable)`
     `(BETA)` Disable an IAM service account. 
`[enable](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/service-accounts/enable)`
     `(BETA)` Enable an IAM service account. 
`[get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/service-accounts/get-iam-policy)`
     `(BETA)` Get the IAM policy for a service account. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/service-accounts/list)`
     `(BETA)` List all of a project's service accounts. 
`[remove-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/service-accounts/remove-iam-policy-binding)`
     `(BETA)` Remove IAM policy binding from a service account. 
`[set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/service-accounts/set-iam-policy)`
     `(BETA)` Set IAM policy for a service account. 
`[sign-blob](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/service-accounts/sign-blob)`
     `(BETA)` Sign a blob with a managed service account key. 
`[sign-jwt](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/service-accounts/sign-jwt)`
     `(BETA)` Sign a JWT with a managed service account key. 
`[undelete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/service-accounts/undelete)`
     `(BETA)` Undelete a service account for a project. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/service-accounts/update)`
     `(BETA)` Update an IAM service account. 
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud iam service-accounts](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts)
    
    
    [gcloud alpha iam service-accounts](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/service-accounts)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
