---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/import/sql/
title: gcloud beta sql import sql \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:07:03.981269+00:00
---

# gcloud beta sql import sql  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/import/sql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta sql import sql Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta sql import sql - imports data into a Cloud SQL instance from a SQL dump file 
SYNOPSIS
    

`gcloud beta sql import sql` `INSTANCE` `URI` [`--async`] [`--clean`] [`--database`=`DATABASE`, `-d` `DATABASE`] [`--if-exists`] [`--parallel`] [`--threads`=`THREADS`] [`--user`=`USER`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` gcloud beta sql import sql imports data into a Cloud SQL instance from a SQL dump file in Google Cloud Storage. 

NOTE: Certain roles and permissions are required to import data into Google Cloud SQL. For more information on importing data into Google Cloud SQL see [Import a SQL dump file](https://cloud.google.com/sql/docs/mysql/import-export/import-export-sql#gcloud_1). 

For detailed help on importing data into Cloud SQL, refer to this guide: <https://cloud.google.com/sql/docs/mysql/import-export/importing>

EXAMPLES
     To import data from a SQL dump file into a database, `testdb`, on the specified Cloud SQL instance `test-instance-1`, run: 
    
    
    [gcloud sql import sql](https://docs.cloud.google.com/sdk/gcloud/reference/sql/import/sql) test-instance-1 gs://test-bucket/test-file.sql.gz --database=testdb

POSITIONAL ARGUMENTS
    

`INSTANCE`
     Cloud SQL instance ID. 
`URI`
     Path to the MySQL dump file in Google Cloud Storage from which the import is made. The URI is in the form `gs://bucketName/fileName`. Compressed gzip files (.gz) are also supported. 
FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--clean`
     Option to clean (DROP) database objects before recreating them. corresponds to the clean flag for pg_restore. Only applies if --parallel is set. PostgreSQL only. 
`--database`=`DATABASE`, `-d` `DATABASE`
     Database to which the import is made. The database needs to be created before importing. If not set, it is assumed that the database is specified in the file to be imported. If your SQL dump file includes a database statement, it will override the database set in this flag. 
`--if-exists`
     Include an SQL statement (IF EXISTS) with each DROP statement produced by \--clean; corresponds to the if-exists flag for pg_restore. Only applies if \--parallel is set. PostgreSQL only. 
`--parallel`
     Perform a parallel import. This flag is only applicable to MySQL and Postgres. When this flag is used, the URI specifies a folder in the Cloud Storage bucket where the multiple files to be imported are located. 
`--threads`=`THREADS`
     Specifies the number of threads to use for the parallel import. If `--parallel` is specified and this flag is not provided, Cloud SQL uses a default thread count to optimize performance. 
`--user`=`USER`
     PostgreSQL user for this import operation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud sql import sql](https://docs.cloud.google.com/sdk/gcloud/reference/sql/import/sql)
    
    
    [gcloud alpha sql import sql](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/import/sql)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
