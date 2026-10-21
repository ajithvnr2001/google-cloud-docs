---
url: https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/upload/
title: gcloud iam service-accounts keys upload \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:15:42.553477+00:00
---

# gcloud iam service-accounts keys upload  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/upload/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud iam service-accounts keys upload Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud iam service-accounts keys upload - upload a public key for an IAM service account 
SYNOPSIS
    

`gcloud iam service-accounts keys upload` `PUBLIC_KEY_FILE` `--iam-account`=`IAM_ACCOUNT` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Upload a public key for an IAM service account. 

If the service account does not exist, this command returns a `PERMISSION_DENIED` error. 

EXAMPLES
     The following command uploads a public key certificate to a service account:
    
    
    gcloud iam service-accounts keys upload test_data/public_key.cert --iam-account=my-iam-account@my-project.iam.gserviceaccount.com

POSITIONAL ARGUMENTS
    

`PUBLIC_KEY_FILE`
     Path of the file containing the public key. Note that only public key data in the format of RSA_X509_PEM is supported. See <https://cloud.google.com/iot/docs/concepts/device-security#public_key_format> for more information. 
REQUIRED FLAGS
    

IamAccount resource - The service account for which to upload a key. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--iam-account` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--iam-account`=`IAM_ACCOUNT`
     ID of the iamAccount or fully qualified identifier for the iamAccount. 

To set the `iam-account` attribute: 

  * provide the argument `--iam-account` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `iam/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/iam/>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha iam service-accounts keys upload](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/service-accounts/keys/upload)
    
    
    [gcloud beta iam service-accounts keys upload](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/service-accounts/keys/upload)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
