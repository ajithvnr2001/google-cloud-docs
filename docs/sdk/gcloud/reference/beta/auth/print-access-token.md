---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/auth/print-access-token/
title: gcloud beta auth print-access-token \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:28:13.973350+00:00
---

# gcloud beta auth print-access-token  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/auth/print-access-token/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta auth print-access-token Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta auth print-access-token - print an access token for the specified account 
SYNOPSIS
    

`gcloud beta auth print-access-token` [`ACCOUNT`] [`--lifetime`=`LIFETIME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Print an access token for the specified account. See [RFC6749](https://tools.ietf.org/html/rfc6749) for more information about access tokens. 

Note that token itself may not be enough to access some services. If you use the token with curl or similar tools, you may see permission errors similar to "API has not been used in project 32555940559 before or it is disabled.". If it happens, you may need to provide a quota project in the "X-Goog-User-Project" header. For example, 
    
    
    curl -H "X-Goog-User-Project: your-project" -H "Authorization: Bearer $(gcloud auth print-access-token)" foo.googleapis.com

The identity that granted the token must have the serviceusage.services.use permission on the provided project. See <https://cloud.google.com/apis/docs/system-parameters> for more information. 

EXAMPLES
     To print access tokens: 
    
    
    gcloud beta auth print-access-token

POSITIONAL ARGUMENTS
    

[`ACCOUNT`]
     Account to get the access token for. If not specified, the current active account will be used. 
FLAGS
    

`--lifetime`=`LIFETIME`
     Access token lifetime. The default access token lifetime is 3600 seconds, but you can use this flag to reduce the lifetime or extend it up to 43200 seconds (12 hours). The org policy constraint `constraints/iam.allowServiceAccountCredentialLifetimeExtension` must be set if you want to extend the lifetime beyond 3600 seconds. Note that this flag is for service account impersonation only, so it must be used together with the `--impersonate-service-account` flag. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud auth print-access-token](https://docs.cloud.google.com/sdk/gcloud/reference/auth/print-access-token)
    
    
    [gcloud alpha auth print-access-token](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/auth/print-access-token)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
