---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/import/tde/
title: gcloud beta sql import tde \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:07:04.055156+00:00
---

# gcloud beta sql import tde  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/import/tde/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta sql import tde Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta sql import tde - import TDE certificate into a Cloud SQL for SQL Server instance 
SYNOPSIS
    

`gcloud beta sql import tde` `INSTANCE` (`--cert-path`=`CERT_PATH` `--certificate`=`CERTIFICATE` `--pvk-path`=`PVK_PATH` (`--prompt-for-pvk-password` | `--pvk-password`=`PVK_PASSWORD`)) [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` gcloud beta sql import tde imports a TDE certificate into a Cloud SQL instance from a certificate file in Google Cloud Storage. 

For detailed help on importing data into Cloud SQL, refer to this guide: <https://cloud.google.com/sql/docs/sqlserver/import-export/importing>

EXAMPLES
     To import a TDE certificate with the name `foo` and certificate path `my-bucket/my-cert.cert` and private key path `my-bucket/my-key.pvk` and pvk password `my-pvk-password` into the Cloud SQL instance `my-instance`, run: 
    
    
    gcloud beta sql import tde my-instance --certificate=foo --cert-path=gs://my-bucket/my-cert.cert --pvk-path=gs://my-bucket/my-key.pvk --pvk-password=my-pvk-password

To import a TDE certificate with the name `foo` and certificate path `my-bucket/my-cert.cert` and private key path `my-bucket/my-key.pvk` into the Cloud SQL instance `my-instance` and prompting for the private key password, run: 
    
    
    gcloud beta sql import tde my-instance --certificate=foo --cert-path=gs://my-bucket/my-cert.cert --pvk-path=gs://my-bucket/my-key.pvk --prompt-for-pvk-password

POSITIONAL ARGUMENTS
    

`INSTANCE`
     Cloud SQL instance ID. 
REQUIRED FLAGS
    

Encryption info to support importing a TDE certificate file 

This must be specified. 

`--cert-path`=`CERT_PATH`
     Path to the encryption certificate file in Google Cloud Storage. The URI is in the form `gs://bucketName/fileName`. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--certificate`=`CERTIFICATE`
     Name of the encryption certificate. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--pvk-path`=`PVK_PATH`
     Path to the encryption private key file in Google Cloud Storage. The URI is in the form `gs://bucketName/fileName`. 

This flag argument must be specified if any of the other arguments in this group are specified. 

Exactly one of these must be specified: 

`--prompt-for-pvk-password`
     Prompt for the private key password associated with the certificate file with character echo disabled. The password is all typed characters up to but not including the RETURN or ENTER key. 
`--pvk-password`=`PVK_PASSWORD`
     The private key password associated with the certificate file. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud sql import tde](https://docs.cloud.google.com/sdk/gcloud/reference/sql/import/tde)
    
    
    [gcloud alpha sql import tde](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/import/tde)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
