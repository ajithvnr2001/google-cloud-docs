---
url: https://docs.cloud.google.com/sdk/gcloud/reference/transfer/authorize/
title: gcloud transfer authorize \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:41:09.752494+00:00
---

# gcloud transfer authorize  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/transfer/authorize/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud transfer authorize Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud transfer authorize - authorize an account for all Storage Transfer Service features 
SYNOPSIS
    

`gcloud transfer authorize` [`--add-missing`] [`--creds-file`=`CREDS_FILE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Authorize a Google account for all Storage Transfer Service features. 

This command provides admin and owner rights for simplicity. If that's too much authority for your use case, see [Agent-based transfer permissions](https://docs.cloud.google.com/storage-transfer/docs/file-system-permissions) or [Agentless transfer permissions](https://docs.cloud.google.com/storage-transfer/docs/iam-cloud) for a fine-grained list of roles. 

EXAMPLES
     To see what Transfer Service IAM roles the account logged into gcloud may be missing, run: 
    
    
    gcloud transfer authorize

To add the missing IAM roles, run: 
    
    
    gcloud transfer authorize --add-missing

To check a custom service account for missing roles, run: 
    
    
    gcloud transfer authorize --creds-file=path/to/service-account-key.json

FLAGS
    

`--add-missing`
     Add IAM roles necessary to use all Transfer Service features to the specified account. By default, this command just prints missing roles. 
`--creds-file`=`CREDS_FILE`
     The path to the creds file for an account to authorize. The file should be in JSON format and contain a "type" and "client_email", which are automatically generated for most creds files downloaded from Google (e.g. service account tokens). If this flag is not present, the command authorizes the user currently logged into gcloud. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud alpha transfer authorize](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/transfer/authorize)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-28 UTC."],[],[]] 
