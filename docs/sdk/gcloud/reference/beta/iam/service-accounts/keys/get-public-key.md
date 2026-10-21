---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/service-accounts/keys/get-public-key/
title: gcloud beta iam service-accounts keys get-public-key \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:59:49.045407+00:00
---

# gcloud beta iam service-accounts keys get-public-key  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/service-accounts/keys/get-public-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta iam service-accounts keys get-public-key Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta iam service-accounts keys get-public-key - get the public key for a service account key pair 
SYNOPSIS
    

`gcloud beta iam service-accounts keys get-public-key` `KEY-ID` `--iam-account`=`IAM_ACCOUNT` `--output-file`=`OUTPUT_FILE` [`--type`=`TYPE`; default="pem"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Get the public key for a service account key pair in pem or raw format. 
EXAMPLES
     To get the public key for some key ID for some service account (to validate a blob or JWT signature, for example), run: 
    
    
    gcloud beta iam service-accounts keys get-public-key keyid --output-file=key-file --iam-account=my-iam-account@my-project.iam.gserviceaccount.com

POSITIONAL ARGUMENTS
    

`KEY-ID`
     The key to get. 
REQUIRED FLAGS
    

`--iam-account`=`IAM_ACCOUNT`
     A textual name to display for the account. 
`--output-file`=`OUTPUT_FILE`
     The output file to write the public key. 
OPTIONAL FLAGS
    

`--type`=`TYPE`; default="pem"
     The type of the public key to get. `TYPE` must be one of: `pem`, `raw`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha iam service-accounts keys get-public-key](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/service-accounts/keys/get-public-key)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
