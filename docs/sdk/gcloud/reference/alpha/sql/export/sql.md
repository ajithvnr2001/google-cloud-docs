---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/export/sql/
title: gcloud alpha sql export sql \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:26:02.051483+00:00
---

# gcloud alpha sql export sql  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/export/sql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha sql export sql Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha sql export sql - exports data from a Cloud SQL instance to a SQL file 
SYNOPSIS
    

`gcloud alpha sql export sql` `INSTANCE` `URI` [`--async`] [`--clean`] [`--database`=`DATABASE`,[`DATABASE`,…], `-d` `DATABASE`,[`DATABASE`,…]] [`--if-exists`] [`--offload`] [`--parallel`] [`--table`=`TABLE`,[`TABLE`,…], `-t` `TABLE`,[`TABLE`,…]] [`--threads`=`THREADS`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Exports data from a Cloud SQL instance to a Google Cloud Storage bucket as a SQL dump file. 

NOTE: Certain roles and permissions are required to export data to Google Cloud Storage. For more information on exporting data from Google Cloud SQL see [Export from Cloud SQL to a SQL dump file](https://cloud.google.com/sql/docs/mysql/import-export/import-export-sql#gcloud). 

POSITIONAL ARGUMENTS
    

`INSTANCE`
     Cloud SQL instance ID. 
`URI`
     The path to the file in Google Cloud Storage where the export will be stored. The URI is in the form gs://bucketName/fileName. If the file already exists, the operation fails. If the filename ends with .gz, the contents are compressed. 
FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--clean`
     Include SQL statements (DROP <object>) required to drop database objects prior to import; corresponds to the clean flag for pg_dump. Only applies to PostgreSQL non-parallel exports. 
`--database`=`DATABASE`,[`DATABASE`,…], `-d` `DATABASE`,[`DATABASE`,…]
     Database(s) from which the export is made. Information on requirements can be found here: <https://cloud.google.com/sql/docs/mysql/admin-api/v1beta4/instances/export#exportContext.databases>
`--if-exists`
     Include an SQL statement (IF EXISTS) with each drop statement produced by the clean flag; corresponds to the if-exists flag for pg_dump. Only applies to PostgreSQL non-parallel exports. 
`--offload`
     Offload an export to a temporary instance. Doing so reduces strain on source instances and allows other operations to be performed while the export is in progress. 
`--parallel`
     Perform a parallel export. This flag is only applicable to MySQL and Postgres. When this flag is used, the URI specifies a folder in the Cloud Storage bucket. After the parallel export completes, you will have multiple files in that folder. 
`--table`=`TABLE`,[`TABLE`,…], `-t` `TABLE`,[`TABLE`,…]
     Tables to export from the specified database. If you specify tables, specify one and only one database. For PostgreSQL instances, only one table can be exported at a time. 
`--threads`=`THREADS`
     Specifies the number of threads to use for the parallel export. If `--parallel` is specified and this flag is not provided, Cloud SQL uses a default thread count to optimize performance. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud sql export sql](https://docs.cloud.google.com/sdk/gcloud/reference/sql/export/sql)
    
    
    [gcloud beta sql export sql](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/export/sql)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
