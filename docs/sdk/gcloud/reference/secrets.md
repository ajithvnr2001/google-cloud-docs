---
url: https://docs.cloud.google.com/sdk/gcloud/reference/secrets/
title: gcloud secrets \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:34:45.406709+00:00
---

# gcloud secrets  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/secrets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud secrets Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud secrets - manage secrets on Google Cloud 
SYNOPSIS
    

`gcloud secrets` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Google Secret Manager allows users to store and retrieve secrets such as API keys, certificates, passwords on Google Cloud. Google Secret Manager is integrated with Cloud IAM and Cloud Audit Logging so users can manage permissions on individual secrets and monitor how these are used. 

To learn more about Google Secret Manager, visit: 
    
    
    <https://cloud.google.com/secret-manager/>

To read API and usage documentation, visit: 
    
    
    <https://cloud.google.com/secret-manager/docs/>

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[locations](https://docs.cloud.google.com/sdk/gcloud/reference/secrets/locations)`
     Manage locations of users' secrets. 
`[replication](https://docs.cloud.google.com/sdk/gcloud/reference/secrets/replication)`
     Manage secret replication. 
`[versions](https://docs.cloud.google.com/sdk/gcloud/reference/secrets/versions)`
     Manage secret versions. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/secrets/add-iam-policy-binding)`
     Add IAM policy binding to a secret. 
`[create](https://docs.cloud.google.com/sdk/gcloud/reference/secrets/create)`
     Create a new secret. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/secrets/delete)`
     Delete a secret. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/secrets/describe)`
     Describe a secret's metadata. 
`[enable-managed-rotation](https://docs.cloud.google.com/sdk/gcloud/reference/secrets/enable-managed-rotation)`
     Enable managed rotation for a secret. 
`[get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/secrets/get-iam-policy)`
     Get the IAM policy for the secret. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/secrets/list)`
     List all secret names. 
`[remove-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/secrets/remove-iam-policy-binding)`
     Remove IAM policy binding for a secret. 
`[rotate-secret](https://docs.cloud.google.com/sdk/gcloud/reference/secrets/rotate-secret)`
     Rotate a secret. 
`[set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/secrets/set-iam-policy)`
     Set the IAM policy binding for a secret. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/secrets/update)`
     Update a secret's metadata. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha secrets](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/secrets)
    
    
    [gcloud beta secrets](https://docs.cloud.google.com/sdk/gcloud/reference/beta/secrets)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-28 UTC."],[],[]] 
