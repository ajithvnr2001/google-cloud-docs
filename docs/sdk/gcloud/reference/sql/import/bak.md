---
url: https://docs.cloud.google.com/sdk/gcloud/reference/sql/import/bak/
title: gcloud sql import bak \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:37.833819+00:00
---

# gcloud sql import bak  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/sql/import/bak/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud sql import bak Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud sql import bak - import data into a Cloud SQL instance from a BAK file 
SYNOPSIS
    

`gcloud sql import bak` `INSTANCE` [`URI`] `--database`=`DATABASE`, `-d` `DATABASE` [`--async`] [`--bak-type`=`BAK_TYPE`; default="FULL"] [`--keep-encrypted`] [`--no-recovery`] [`--recovery-only`] [`--stop-at`=`STOP_AT`] [`--stop-at-mark`=`STOP_AT_MARK`] [`--[no-]striped`] [`--cert-path`=`CERT_PATH` `--pvk-path`=`PVK_PATH` (`--prompt-for-pvk-password` | `--pvk-password`=`PVK_PASSWORD`)] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     gcloud sql import bak imports data into a Cloud SQL instance from a BAK backup file in Google Cloud Storage. You should use a full backup file with a single backup set. 

For detailed help on importing data into Cloud SQL, refer to this guide: <https://cloud.google.com/sql/docs/sqlserver/import-export/importing>

EXAMPLES
     To import data from the BAK file `my-bucket/my-export.bak` into the database `my-database` in the Cloud SQL instance `my-instance`, run: 
    
    
    gcloud sql import bak my-instance gs://my-bucket/my-export.bak --database=my-database

To import data from the encrypted BAK file `my-bucket/my-export.bak` into the database `my-database` in the Cloud SQL instance `my-instance`, with the certificate `gs://my-bucket/my-cert.crt`, private key `gs://my-bucket/my-key.key` and prompting for the private key password, run: 
    
    
    gcloud sql import bak my-instance gs://my-bucket/my-export.bak --database=my-database --cert-path=gs://my-bucket/my-cert.crt --pvk-path=gs://my-bucket/my-key.key --prompt-for-pvk-password

POSITIONAL ARGUMENTS
    

`INSTANCE`
     Cloud SQL instance ID. 
[`URI`]
     Path to the BAK file file in Google Cloud Storage from which the import is made. The URI is in the form `gs://bucketName/fileName`. 
REQUIRED FLAGS
    

`--database`=`DATABASE`, `-d` `DATABASE`
     A new database into which the import is made. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--bak-type`=`BAK_TYPE`; default="FULL"
     Type of bak file that will be imported. Applicable to SQL Server only. `BAK_TYPE` must be one of: `FULL`, `DIFF`, `TLOG`. 
`--keep-encrypted`
     Whether or not to decrypt the imported encrypted BAK file. 
`--no-recovery`
     Whether or not the SQL Server import is executed with NORECOVERY keyword. 
`--recovery-only`
     Whether or not the SQL Server import skip download and bring database online. 
`--stop-at`=`STOP_AT`
     Equivalent to SQL Server STOPAT keyword. Used in transaction log import only. Transaction log import stop at this timestamp. Format: YYYY-MM-DDTHH:MM:SS. 
`--stop-at-mark`=`STOP_AT_MARK`
     Equivalent to SQL Server STOPATMARK keyword. Used in transaction log import only. Transaction log import stop at the given mark. To stop at given LSN, use \--stop-at-mark=lsn:xxx. 
`--[no-]striped`
     Whether SQL Server import should be striped. Use `--striped` to enable and `--no-striped` to disable. 
Encryption info to support importing an encrypted .bak file 
`--cert-path`=`CERT_PATH`
     Path to the encryption certificate file in Google Cloud Storage associated with the BAK file. The URI is in the form `gs://bucketName/fileName`. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--pvk-path`=`PVK_PATH`
     Path to the encryption private key file in Google Cloud Storage associated with the BAK file. The URI is in the form `gs://bucketName/fileName`. 

This flag argument must be specified if any of the other arguments in this group are specified. 

Exactly one of these must be specified: 

`--prompt-for-pvk-password`
     Prompt for the private key password associated with the BAK file with character echo disabled. The password is all typed characters up to but not including the RETURN or ENTER key. 
`--pvk-password`=`PVK_PASSWORD`
     The private key password associated with the BAK file. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha sql import bak](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/import/bak)
    
    
    [gcloud beta sql import bak](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/import/bak)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
