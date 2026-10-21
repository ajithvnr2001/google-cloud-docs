---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/generate-login-token/
title: gcloud alpha sql generate-login-token \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:26:02.910070+00:00
---

# gcloud alpha sql generate-login-token  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/generate-login-token/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha sql generate-login-token Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha sql generate-login-token - generate an IAM login token for Cloud SQL 
SYNOPSIS
    

`gcloud alpha sql generate-login-token` [`--application-default-credential`] [`--instance`=`INSTANCE`, `-i` `INSTANCE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` gcloud alpha sql generate-login-token generates an IAM token to use for logging in to Cloud SQL instances. 
EXAMPLES
     To generate an IAM login token using gcloud credentials, run: 
    
    
    gcloud alpha sql generate-login-token

To generate an IAM login token using application default credentials, run: 
    
    
    gcloud alpha sql generate-login-token --application-default-credential

To generate an IAM login token using gcloud credentials for instance `my-instance`, run: 
    
    
    gcloud alpha sql generate-login-token --instance=my-instance

To generate an IAM login token using application default credentials for instance `my-instance`, run: 
    
    
    gcloud alpha sql generate-login-token --instance=my-instance --application-default-credential

FLAGS
    

`--application-default-credential`
     Use application default credentials to generate the login token. 
`--instance`=`INSTANCE`, `-i` `INSTANCE`
     Cloud SQL instance ID. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud sql generate-login-token](https://docs.cloud.google.com/sdk/gcloud/reference/sql/generate-login-token)
    
    
    [gcloud beta sql generate-login-token](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/generate-login-token)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
