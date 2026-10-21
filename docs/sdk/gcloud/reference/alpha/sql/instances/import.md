---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/import/
title: gcloud alpha sql instances import \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:02:16.291678+00:00
---

# gcloud alpha sql instances import  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha sql instances import Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha sql instances import - imports data into a Cloud SQL instance from Google Cloud Storage 
SYNOPSIS
    

`gcloud alpha sql instances import` `INSTANCE` `URI` [`--async`] [`--database`=`DATABASE`, `-d` `DATABASE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `(DEPRECATED)` Imports data into a Cloud SQL instance from Google Cloud Storage. 

This command is deprecated and will be removed in version 205.0.0. Use `[gcloud sql import sql](https://docs.cloud.google.com/sdk/gcloud/reference/sql/import/sql)` instead. 

Note: authorization is required. For more information on importing data into Google Cloud SQL see <https://cloud.google.com/sql/docs/import-export/importing>. 

Cloud SQL supports importing CSV files and SQL dump files from both MySQL and PostgreSQL. For more information on how to create these export formats, see <https://cloud.google.com/sql/docs/mysql/import-export/creating-sqldump-csv>

POSITIONAL ARGUMENTS
    

`INSTANCE`
     Cloud SQL instance ID. 
`URI`
     Path to the MySQL dump file in Google Cloud Storage from which the import is made. The URI is in the form gs://bucketName/fileName. Compressed gzip files (.gz) are also supported. 
FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--database`=`DATABASE`, `-d` `DATABASE`
     Database to which the import is made. The database needs to be created before importing. If not set, it is assumed that the database is specified in the file to be imported. If your SQL dump file includes a database statement, it will override the database set in this flag. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud sql instances import](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/import)
    
    
    [gcloud beta sql instances import](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/instances/import)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
