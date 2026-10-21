---
url: https://docs.cloud.google.com/sdk/gcloud/reference/spanner/operations/describe/
title: gcloud spanner operations describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:30:21.733635+00:00
---

# gcloud spanner operations describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/spanner/operations/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud spanner operations describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud spanner operations describe - describe a Cloud Spanner operation 
SYNOPSIS
    

`gcloud spanner operations describe` `OPERATION-ID` (`--instance`=`INSTANCE` | `--instance-config`=`INSTANCE_CONFIG`) [`--backup`=`BACKUP`] [`--database`=`DATABASE`] [`--instance-partition`=`INSTANCE_PARTITION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Describe a Cloud Spanner operation. 
EXAMPLES
     To describe a Cloud Spanner instance operation, run: 
    
    
    gcloud spanner operations describe _auto_12345 --instance=my-instance-id

To describe a Cloud Spanner database operation, run: 
    
    
    gcloud spanner operations describe _auto_12345 --instance=my-instance-id --database=my-database-id

To describe a Cloud Spanner backup operation, run: 
    
    
    gcloud spanner operations describe _auto_12345 --instance=my-instance-id --backup=my-backup-id

To describe an instance partition operation, run: 
    
    
    gcloud spanner operations describe _auto_12345 --instance=my-instance-id --instance-partition=my-partition-id

POSITIONAL ARGUMENTS
    

`OPERATION-ID`
     ID of the operation 
REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--instance`=`INSTANCE`
     The ID of the instance the operation is executing on. 
`--instance-config`=`INSTANCE_CONFIG`
     The ID of the instance configuration the operation is executing on. 
OPTIONAL FLAGS
    

`--backup`=`BACKUP`
     For a backup operation, the name of the backup the operation is executing on. 
`--database`=`DATABASE`
     For a database operation, the name of the database the operation is executing on. 
`--instance-partition`=`INSTANCE_PARTITION`
     For an instance partition operation, the name of the instance partition the operation is executing on. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha spanner operations describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/operations/describe)
    
    
    [gcloud beta spanner operations describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/operations/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
