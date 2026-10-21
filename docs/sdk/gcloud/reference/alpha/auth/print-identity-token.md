---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/auth/print-identity-token/
title: gcloud alpha auth print-identity-token \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:36.309098+00:00
---

# gcloud alpha auth print-identity-token  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/auth/print-identity-token/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha auth print-identity-token Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha auth print-identity-token - print an identity token for the specified account 
SYNOPSIS
    

`gcloud alpha auth print-identity-token` [`ACCOUNT`] [`--audiences`=`AUDIENCES`] [`--include-email`] [`--include-license` `--token-format`=`TOKEN_FORMAT`; default="standard"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Print an identity token for the specified account. 
EXAMPLES
     To print identity tokens: 
    
    
    gcloud alpha auth print-identity-token

To print identity token for account 'foo@example.com' whose audience is 'https://service-hash-uc.a.run.app', run: 
    
    
    gcloud alpha auth print-identity-token foo@example.com --audiences="https://service-hash-uc.a.run.app"

To print identity token for an impersonated service account 'my-account@example.iam.gserviceaccount.com' whose audience is 'https://service-hash-uc.a.run.app', run: 
    
    
    gcloud alpha auth print-identity-token --impersonate-service-account="my-account@example.iam.gserviceaccount.com" --audiences="https://service-hash-uc.a.run.app"

To print identity token of a Compute Engine instance, which includes project and instance details as well as license codes for images associated with the instance, run: 
    
    
    gcloud alpha auth print-identity-token --token-format=full --include-license

To print identity token for an impersonated service account 'my-account@example.iam.gserviceaccount.com', which includes the email address of the service account, run: 
    
    
    gcloud alpha auth print-identity-token --impersonate-service-account="my-account@example.iam.gserviceaccount.com" --include-email

POSITIONAL ARGUMENTS
    

[`ACCOUNT`]
     Account to print the identity token for. If not specified, the current active account will be used. 
FLAGS
    

`--audiences`=`AUDIENCES`
     Intended recipient of the token. Currently, only one audience can be specified. 
`--include-email`
     Specify whether or not service account email is included in the identity token. If specified, the token will contain 'email' and 'email_verified' claims. This flag should only be used for impersonate service account. 
Parameters for Google Compute Engine instance identity tokens. 
`--include-license`
     Specify whether or not license codes for images associated with this instance are included in the identity token payload. Default is False. This flag does not have effect unless `--token-format=full`. 
`--token-format`=`TOKEN_FORMAT`; default="standard"
     Specify whether or not the project and instance details are included in the identity token payload. This flag only applies to Google Compute Engine instance identity tokens. See <https://cloud.google.com/compute/docs/instances/verifying-instance-identity#token_format> for more details on token format. `TOKEN_FORMAT` must be one of: `standard`, `full`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud auth print-identity-token](https://docs.cloud.google.com/sdk/gcloud/reference/auth/print-identity-token)
    
    
    [gcloud beta auth print-identity-token](https://docs.cloud.google.com/sdk/gcloud/reference/beta/auth/print-identity-token)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
