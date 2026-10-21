---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/edge-cloud/auth/print-identity-token/
title: gcloud alpha edge-cloud auth print-identity-token \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:32:11.674088+00:00
---

# gcloud alpha edge-cloud auth print-identity-token  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/edge-cloud/auth/print-identity-token/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha edge-cloud auth print-identity-token Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha edge-cloud auth print-identity-token - print an identity token for a specified audience 
SYNOPSIS
    

`gcloud alpha edge-cloud auth print-identity-token` `--audience`=`AUDIENCE` (`--cred-file`=`CRED_FILE` | [`--login-uri`=`LOGIN_URI` : `--login-cert`=`LOGIN_CERT`]) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` The methods in the class generates an identity token for a specified audience in Google Distributed Cloud zone. The identity token can be generated based on IDP login or Service Account Keys. 
REQUIRED FLAGS
    

`--audience`=`AUDIENCE`
     Intended recipient of the token. Currently, only one audience can be specified. 
Token Generation Arguments. 

Exactly one of these must be specified: 

Credential File Arguments. 
`--cred-file`=`CRED_FILE`
     Credential file. 
IDP Login Arguments. 
`--login-uri`=`LOGIN_URI`
     Google Distributed Cloud zone IDP login URI. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--login-cert`=`LOGIN_CERT`
     Google Distributed Cloud zone CA certificate path 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
