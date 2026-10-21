---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/
title: gcloud alpha pam entitlements \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:33.361292+00:00
---

# gcloud alpha pam entitlements  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha pam entitlements Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha pam entitlements - manage Privileged Access Manager entitlements 
SYNOPSIS
    

`gcloud alpha pam entitlements` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` The `[gcloud pam entitlements](https://docs.cloud.google.com/sdk/gcloud/reference/pam/entitlements)` command group lets you manage Privileged Access Manager (PAM) entitlements. 
EXAMPLES
     To create a new entitlement with a name of `sample-entitlement`, in a project named `sample-project`, in location `global`, and the entitlement configuration stored in a file named `sample-entitlement.yaml`, run: 
    
    
    [gcloud alpha pam entitlements create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/create) sample-entitlement --project=sample-project --location=global --entitlement-file=sample-entitlement.yaml

To create a new entitlement with a name of `sample-entitlement`, in a folder with ID ``FOLDER_ID``, in location `global`, and the entitlement configuration stored in a file named `sample-entitlement.yaml`, run: 
    
    
    [gcloud alpha pam entitlements create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/create) sample-entitlement --folder=FOLDER_ID --location=global --entitlement-file=sample-entitlement.yaml

To create a new entitlement with a name of `sample-entitlement`, in an organization with ID ``ORGANIZATION_ID``, in location `global`, and the entitlement configuration stored in a file named `sample-entitlement.yaml`, run: 
    
    
    [gcloud alpha pam entitlements create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/create) sample-entitlement --organization=ORGANIZATION_ID --location=global --entitlement-file=sample-entitlement.yaml

To update an entitlement with a name of `sample-entitlement`, in a project named `sample-project`, in location `global`, and the new entitlement configuration stored in a file named `sample-entitlement.yaml`, run: 
    
    
    [gcloud alpha pam entitlements update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/update) sample-entitlement --project=sample-project --location=global --entitlement-file=sample-entitlement.yaml

To update an entitlement with a name of `sample-entitlement`, in a folder with ID ``FOLDER_ID``, in location `global`, and the new entitlement configuration stored in a file named `sample-entitlement.yaml`, run: 
    
    
    [gcloud alpha pam entitlements update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/update) sample-entitlement --folder=FOLDER_ID --location=global --entitlement-file=sample-entitlement.yaml

To update an entitlement with a name of `sample-entitlement`, in an organization with ID ``ORGANIZATION_ID``, in location `global`, and the new entitlement configuration stored in a file named `sample-entitlement.yaml`, run: 
    
    
    [gcloud alpha pam entitlements update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/update) sample-entitlement --organization=ORGANIZATION_ID --location=global --entitlement-file=sample-entitlement.yaml

To describe an entitlement with a name of `sample-entitlement`, in a project named `sample-project`, and in location `global`, run: 
    
    
    [gcloud alpha pam entitlements describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/describe) sample-entitlement --project=sample-project --location=global

To describe an entitlement with a name of `sample-entitlement`, in a folder with ID ``FOLDER_ID``, and in location `global`, run: 
    
    
    [gcloud alpha pam entitlements describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/describe) sample-entitlement --folder=FOLDER_ID --location=global

To describe an entitlement with a name of `sample-entitlement`, in an organization with ID ``ORGANIZATION_ID``, and in location `global`, run: 
    
    
    [gcloud alpha pam entitlements describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/describe) sample-entitlement --organization=ORGANIZATION_ID --location=global

To search for and list all entitlements for which you are a requester, in a project named `sample-project`, and in location `global`, run: 
    
    
    [gcloud alpha pam entitlements search](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/search) --project=sample-project --location=global --caller-access-type=grant-requester

To search for and list all entitlements for which you are an approver, in a project named `sample-project`, and in location `global`, run: 
    
    
    [gcloud alpha pam entitlements search](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/search) --project=sample-project --location=global --caller-access-type=grant-approver

To search for and list all entitlements for which you are a requester, in a folder with ID ``FOLDER_ID``, and in location `global`, run: 
    
    
    [gcloud alpha pam entitlements search](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/search) --folder=FOLDER_ID --location=global --caller-access-type=grant-requester

To search for and list all entitlements for which you are an approver, in a folder with ID ``FOLDER_ID``, and in location `global`, run: 
    
    
    [gcloud alpha pam entitlements search](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/search) --folder=FOLDER_ID --location=global --caller-access-type=grant-approver

To search for and list all entitlements for which you are a requester, in an organization with ID ``ORGANIZATION_ID``, and in location `global`, run: 
    
    
    [gcloud alpha pam entitlements search](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/search) --organization=ORGANIZATION_ID --location=global --caller-access-type=grant-requester

To search for and list all entitlements for which you are an approver, in an organization with ID ``ORGANIZATION_ID``, and in location `global`, run: 
    
    
    [gcloud alpha pam entitlements search](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/search) --organization=ORGANIZATION_ID --location=global --caller-access-type=grant-approver

To list all entitlements in a project named `sample-project` and in location `global`, run: 
    
    
    [gcloud alpha pam entitlements list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/list) --project=sample-project --location=global

To list all entitlements in a folder with ID ``FOLDER_ID`` and in location `global`, run: 
    
    
    [gcloud alpha pam entitlements list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/list) --folder=FOLDER_ID --location=global

To list all entitlements in an organization with ID ``ORGANIZATION_ID`` and in location `global`, run: 
    
    
    [gcloud alpha pam entitlements list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/list) --organization=ORGANIZATION_ID --location=global

To delete an entitlement with a name of `sample-entitlement`, in a project named `sample-project`, and in location `global`, run: 
    
    
    [gcloud alpha pam entitlements delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/delete) sample-entitlement --project=sample-project --location=global

To delete an entitlement with a name of `sample-entitlement`, in a folder with ID ``FOLDER_ID``, and in location `global`, run: 
    
    
    [gcloud alpha pam entitlements delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/delete) sample-entitlement --folder=FOLDER_ID --location=global

To delete an entitlement with a name of `sample-entitlement`, in an organization with ID ``ORGANIZATION_ID``, and in location `global`, run: 
    
    
    [gcloud alpha pam entitlements delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/delete) sample-entitlement --organization=ORGANIZATION_ID --location=global

To export an entitlement with a name of `sample-entitlement`, in a project named `sample-project`, and in location `global` to a local YAML file named `sample-entitlement.yaml`, run: 
    
    
    [gcloud alpha pam entitlements export](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/export) sample-entitlement --project=sample-project --location=global --destination=sample-entitlement.yaml

To export an entitlement with a name of `sample-entitlement`, in a folder with ID ``FOLDER_ID``, and in location `global` to a local YAML file named `sample-entitlement.yaml`, run: 
    
    
    [gcloud alpha pam entitlements export](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/export) sample-entitlement --folder=FOLDER_ID --location=global --destination=sample-entitlement.yaml

To export an entitlement with a name of `sample-entitlement`, in an organization with ID ``ORGANIZATION_ID``, and in location `global` to a local YAML file named `sample-entitlement.yaml`, run: 
    
    
    [gcloud alpha pam entitlements export](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/export) sample-entitlement --organization=ORGANIZATION_ID --location=global --destination=sample-entitlement.yaml

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/create)`
     `(ALPHA)` Create a new Privileged Access Manager (PAM) entitlement. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/delete)`
     `(ALPHA)` Delete a Privileged Access Manager (PAM) entitlement. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/describe)`
     `(ALPHA)` Show details of a Privileged Access Manager (PAM) entitlement. 
`[export](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/export)`
     `(ALPHA)` Export a Privileged Access Manager (PAM) entitlement into a local YAML file. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/list)`
     `(ALPHA)` List all Privileged Access Manager (PAM) entitlements under a parent. 
`[search](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/search)`
     `(ALPHA)` Search and list all Privileged Access Manager (PAM) entitlements in a parent for which you are a requester/approver. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/update)`
     `(ALPHA)` Update an existing Privileged Access Manager (PAM) entitlement. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud pam entitlements](https://docs.cloud.google.com/sdk/gcloud/reference/pam/entitlements)
    
    
    [gcloud beta pam entitlements](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pam/entitlements)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
