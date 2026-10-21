---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/databases/import/
title: gcloud alpha spanner databases import \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:51:32.876843+00:00
---

# gcloud alpha spanner databases import  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/databases/import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha spanner databases import Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha spanner databases import - import data from various source files to Cloud Spanner 
SYNOPSIS
    

`gcloud alpha spanner databases import` `--database`=`DATABASE` `--instance`=`INSTANCE` `--source-format`=`SOURCE_FORMAT` `--source-uri`=`SOURCE_URI` [`--csv-field-delimiter`=`CSV_FIELD_DELIMITER`] [`--csv-line-delimiter`=`CSV_LINE_DELIMITER`] [`--database-dialect`=`DATABASE_DIALECT`] [`--schema-uri`=`SCHEMA_URI`] [`--table-name`=`TABLE_NAME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Import data from various source files to Cloud Spanner. 
EXAMPLES
     To import data from a source file to Cloud Spanner: 
    
    
    gcloud alpha spanner databases import --instance=instanceA --database=databaseA --table-name=tableA --source-uri=gs://bucket/data.csv --source-format=csv --schema-uri=gs://bucket/schema.json
    
    
    gcloud alpha spanner databases import --instance=instanceA --database=databaseA --source-uri=gs://bucket/dump.sql --source-format=mysqldump

REQUIRED FLAGS
    

`--database`=`DATABASE`
     Cloud Spanner database ID. 
`--instance`=`INSTANCE`
     Cloud Spanner instance ID. 
`--source-format`=`SOURCE_FORMAT`
     Format of the file with data to import.Supported formats: csv or mysqldump or pgdump 
`--source-uri`=`SOURCE_URI`
     URI of the file with data to import 
OPTIONAL FLAGS
    

`--csv-field-delimiter`=`CSV_FIELD_DELIMITER`
     Field delimiter for CSV files. 
`--csv-line-delimiter`=`CSV_LINE_DELIMITER`
     Line delimiter for CSV files. 
`--database-dialect`=`DATABASE_DIALECT`
     Dialect for the spanner database. `DATABASE_DIALECT` must be one of: `POSTGRESQL`, `GOOGLE_STANDARD_SQL`. 
`--schema-uri`=`SCHEMA_URI`
     URI of the file with schema of the data to import 
`--table-name`=`TABLE_NAME`
     Cloud Spanner table name 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
