---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/databases/update/
title: gcloud beta spanner databases update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:39:41.982308+00:00
---

# gcloud beta spanner databases update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/databases/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta spanner databases update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta spanner databases update - update a Cloud Spanner database 
SYNOPSIS
    

`gcloud beta spanner databases update` (`DATABASE` : `--instance`=`INSTANCE`) [`--async`] [`--clear-kms-keys` | `--[no-]enable-drop-protection` | `--kms-keys`=`KMS_KEY`,[`KMS_KEY`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update a Cloud Spanner database. 
EXAMPLES
     To enable database deletion protection on a Cloud Spanner database 'my-database', run: 
    
    
    gcloud beta spanner databases update my-database --enable-drop-protection

To disable database deletion protection on a Cloud Spanner database 'my-database', run: 
    
    
    gcloud beta spanner databases update my-database --no-enable-drop-protection

To update KMS key references for a Cloud Spanner database 'my-database', run: 
    
    
    gcloud beta spanner databases update my-database --kms-keys="KEY1,KEY2"

To remove all KMS key references and revert a Cloud Spanner database 'my-database' to Google-managed encryption, run: 
    
    
    gcloud beta spanner databases update my-database --clear-kms-keys

POSITIONAL ARGUMENTS
    

Database resource - The Cloud Spanner database to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `database` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`DATABASE`
     ID of the database or fully qualified identifier for the database. 

To set the `database` attribute: 

  * provide the argument `database` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--instance`=`INSTANCE`
     The Cloud Spanner instance for the database. 

To set the `instance` attribute: 

  * provide the argument `database` on the command line with a fully specified name; 
  * provide the argument `--instance` on the command line; 
  * set the property `spanner/instance`. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
At most one of these can be specified: 

`--clear-kms-keys`
     Removes all KMS key references and reverts the database to Google-managed encryption. 
`--[no-]enable-drop-protection`
     Enable database deletion protection on this database. Use `--enable-drop-protection` to enable and `--no-enable-drop-protection` to disable. 
`--kms-keys`=`KMS_KEY`,[`KMS_KEY`,…]
     Update KMS key references for this database. Users should always provide the full set of required KMS key references. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud spanner databases update](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/databases/update)
    
    
    [gcloud alpha spanner databases update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/databases/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
