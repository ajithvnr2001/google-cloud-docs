---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/auth/activate-service-account/
title: gcloud alpha auth activate-service-account \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:34.149374+00:00
---

# gcloud alpha auth activate-service-account  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/auth/activate-service-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha auth activate-service-account Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha auth activate-service-account - authorize access to Google Cloud with a service account 
SYNOPSIS
    

`gcloud alpha auth activate-service-account` [`ACCOUNT`] `--key-file`=`KEY_FILE` [`--password-file`=`PASSWORD_FILE` | `--prompt-for-password`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` To allow `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` (and other tools in Google Cloud CLI) to use service account credentials to make requests, use this command to import these credentials from a file that contains a private authorization key, and activate them for use in `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)`. gcloud alpha auth activate-service-account serves the same function as `[gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login)` but uses a service account rather than Google user credentials. 

For more information on authorization and credential types, see: <https://cloud.google.com/sdk/docs/authorizing>. 

`Key File`

To obtain the key file for this command, use either the [Google Cloud Console](https://console.cloud.google.com) or `gcloud iam service-accounts keys create`. The key file can be .json (preferred) or .p12 (legacy) format. In the case of legacy .p12 files, a separate password might be required and is displayed in the Console when you create the key. 

`Credentials`

Credentials will also be activated (similar to running `gcloud config set account [ACCOUNT_NAME]`). 

If a project is specified using the `--project` flag, the project is set in active configuration, which is the same as running `gcloud config set project [PROJECT_NAME]`. Any previously active credentials, will be retained (though no longer default) and can be displayed by running `[gcloud auth list](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list)`. 

If you want to delete previous credentials, see `[gcloud auth revoke](https://docs.cloud.google.com/sdk/gcloud/reference/auth/revoke)`. 

`Note:` Service accounts use client quotas for tracking usage. 

EXAMPLES
     To authorize `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` to access Google Cloud using an existing service account while also specifying a project, run: 
    
    
    gcloud alpha auth activate-service-account SERVICE_ACCOUNT@DOMAIN.COM --key-file=/path/key.json --project=PROJECT_ID

POSITIONAL ARGUMENTS
    

[`ACCOUNT`]
     E-mail address of the service account. 
REQUIRED FLAGS
    

`--key-file`=`KEY_FILE`
     Path to the private key file. 
OPTIONAL FLAGS
    

At most one of these can be specified: 

`--password-file`=`PASSWORD_FILE`
     Path to a file containing the password for the service account private key (only for a .p12 file). 
`--prompt-for-password`
     Prompt for the password for the service account private key (only for a .p12 file). 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud auth activate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference/auth/activate-service-account)
    
    
    [gcloud beta auth activate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference/beta/auth/activate-service-account)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
