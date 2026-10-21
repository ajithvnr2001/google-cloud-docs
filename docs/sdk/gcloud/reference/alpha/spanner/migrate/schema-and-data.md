---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/migrate/schema-and-data/
title: gcloud alpha spanner migrate schema-and-data \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:51:38.904893+00:00
---

# gcloud alpha spanner migrate schema-and-data  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/migrate/schema-and-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha spanner migrate schema-and-data Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha spanner migrate schema-and-data - migrate data from a source database to Cloud Spanner given a schema 
SYNOPSIS
    

`gcloud alpha spanner migrate schema-and-data` `--source`=`SOURCE` `--target-profile`=`TARGET_PROFILE` [`--dataflow-template`=`DATAFLOW_TEMPLATE`] [`--dry-run`] [`--log-level`=`LOG_LEVEL`] [`--prefix`=`PREFIX`] [`--project`=`PROJECT`] [`--skip-foreign-keys`] [`--source-profile`=`SOURCE_PROFILE`] [`--target`=`TARGET`] [`--write-limit`=`WRITE_LIMIT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Migrate data from a source database to Cloud Spanner given a schema. 
EXAMPLES
     To generate schema and copy data to Cloud Spanner from a source database: 
    
    
    gcloud alpha spanner migrate schema-and-data --source=postgresql < ~/cart.pg_dump --target-profile='instance=spanner-instance'

REQUIRED FLAGS
    

`--source`=`SOURCE`
     Flag for specifying source database (e.g., PostgreSQL, MySQL, DynamoDB). 
`--target-profile`=`TARGET_PROFILE`
     Flag for specifying connection profile for target database (e.g., "dialect=postgresql)". 
OPTIONAL FLAGS
    

`--dataflow-template`=`DATAFLOW_TEMPLATE`
     The google cloud storage path of the minimal downtime migration template to use to run the migration job. 
`--dry-run`
     Flag for generating DDL and schema conversion report without creating a Cloud Spanner database. 
`--log-level`=`LOG_LEVEL`
     To configure the log level for the execution (INFO, VERBOSE). 
`--prefix`=`PREFIX`
     File prefix for generated files. 
`--project`=`PROJECT`
     The project in which the migration job and its resources will be created. 
`--skip-foreign-keys`
     Skip creating foreign keys after data migration is complete. 
`--source-profile`=`SOURCE_PROFILE`
     Flag for specifying connection profile for source database (e.g., "file=<path>,format=dump"). 
`--target`=`TARGET`
     Specifies the target database, defaults to Spanner (accepted values: Spanner) (default "Spanner"). 
`--write-limit`=`WRITE_LIMIT`
     Number of parallel writers to Cloud Spanner during bulk data migrations (default 40). 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
