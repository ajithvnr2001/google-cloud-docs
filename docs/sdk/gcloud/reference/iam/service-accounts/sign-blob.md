---
url: https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/sign-blob/
title: gcloud iam service-accounts sign-blob \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:40:38.893135+00:00
---

# gcloud iam service-accounts sign-blob  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/sign-blob/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud iam service-accounts sign-blob Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud iam service-accounts sign-blob - sign a blob with a managed service account key 
SYNOPSIS
    

`gcloud iam service-accounts sign-blob` `INPUT-FILE` `OUTPUT-FILE` `--iam-account`=`IAM_ACCOUNT` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     This command signs a file containing arbitrary binary data (a blob) using a system-managed service account key. 

If the service account does not exist, this command returns a `PERMISSION_DENIED` error. 

EXAMPLES
     To sign a blob file with a system-managed service account key, run: 
    
    
    gcloud iam service-accounts sign-blob --iam-account=my-iam-account@my-project.iam.gserviceaccount.com input.bin output.bin

POSITIONAL ARGUMENTS
    

`INPUT-FILE`
     A path to the blob file to be signed. 
`OUTPUT-FILE`
     A path the resulting signed blob will be written to. 
REQUIRED FLAGS
    

`--iam-account`=`IAM_ACCOUNT`
     The service account to sign as. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

SEE ALSO
     For more information on how this command ties into the wider cloud infrastructure, please see <https://cloud.google.com/appengine/docs/java/appidentity/>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha iam service-accounts sign-blob](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/service-accounts/sign-blob)
    
    
    [gcloud beta iam service-accounts sign-blob](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/service-accounts/sign-blob)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
