---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/auth/application-default/
title: gcloud beta auth application-default \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:28:12.809633+00:00
---

# gcloud beta auth application-default  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/auth/application-default/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta auth application-default Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta auth application-default - manage your active Application Default Credentials 
SYNOPSIS
    

`gcloud beta auth application-default` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Application Default Credentials (ADC) provide a method to get credentials used in calling Google APIs. The gcloud beta auth application-default command group allows you to manage active credentials on your machine that are used for local application development. 

These credentials are only used by Google client libraries in your own application. 

For more information about ADC and how it works, see [Authenticating as a service account](https://cloud.google.com/docs/authentication/production). 

EXAMPLES
     To use your own user credentials for your application to access an API, run: 
    
    
    [gcloud beta auth application-default login](https://docs.cloud.google.com/sdk/gcloud/reference/beta/auth/application-default/login)

This will take you through a web flow to acquire new user credentials. 

To create a service account and have your application use it for API access, run: 
    
    
    [gcloud iam service-accounts create](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/create) my-account
    [gcloud iam service-accounts keys create](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/create) key.json --iam-account=my-account@my-project.iam.gserviceaccount.com
    export GOOGLE_APPLICATION_CREDENTIALS=key.json
    ./my_application.sh

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[login](https://docs.cloud.google.com/sdk/gcloud/reference/beta/auth/application-default/login)`
     `(BETA)` Acquire new user credentials to use for Application Default Credentials. 
`[print-access-token](https://docs.cloud.google.com/sdk/gcloud/reference/beta/auth/application-default/print-access-token)`
     `(BETA)` Print an access token for your current Application Default Credentials. 
`[revoke](https://docs.cloud.google.com/sdk/gcloud/reference/beta/auth/application-default/revoke)`
     `(BETA)` Revoke previously generated Application Default Credentials. 
`[set-quota-project](https://docs.cloud.google.com/sdk/gcloud/reference/beta/auth/application-default/set-quota-project)`
     `(BETA)` Update or add a quota project in application default credentials (ADC). 
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud auth application-default](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default)
    
    
    [gcloud alpha auth application-default](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/auth/application-default)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
