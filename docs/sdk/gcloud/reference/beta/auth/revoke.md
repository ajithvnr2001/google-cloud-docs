---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/auth/revoke/
title: gcloud beta auth revoke \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:52:45.340289+00:00
---

# gcloud beta auth revoke  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/auth/revoke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta auth revoke Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta auth revoke - revoke access credentials for an account 
SYNOPSIS
    

`gcloud beta auth revoke` [`ACCOUNTS` …] [`--all`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Revokes credentials for the specified user accounts, service accounts or external accounts (workload identity pools). 

When given a user account, this command revokes the user account token on the server. If the revocation is successful, or if the token has already been revoked, this command removes the credential from the local machine. 

When given a service account, this command does not revoke the service account token on the server because service account tokens are not revocable. Instead, it will print a warning and remove the credential from the local machine. When used with a service account, this command has only a local effect and the key associated with the service account is not deleted. This can be done by executing `[gcloud iam service-accounts keys delete](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/delete)` after `revoke`. 

When given an external account (workload identity pool), whether impersonated or not, the command does not revoke the corresponding token on the server because these tokens are not revocable. The underlying external credentials (OIDC, AWS, etc.) used to generate these access tokens have to be revoked too, but gcloud has no control over that. Instead, it will print a warning and remove the credential from the local machine. 

If no account is specified, this command revokes credentials for the currently active account, effectively logging out of that account. If --all is given, the behaviors described above apply individually to each account in the list. 

You can revoke credentials when you want to prevent gcloud and other Google Cloud CLI tools from using the specified account. You do not need to revoke credentials to switch between accounts. 

POSITIONAL ARGUMENTS
    

[`ACCOUNTS` …]
     Accounts whose credentials are to be revoked. 
FLAGS
    

`--all`
     Revoke credentials for all accounts. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud auth revoke](https://docs.cloud.google.com/sdk/gcloud/reference/auth/revoke)
    
    
    [gcloud alpha auth revoke](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/auth/revoke)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
