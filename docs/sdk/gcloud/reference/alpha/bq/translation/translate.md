---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bq/translation/translate/
title: gcloud alpha bq translation translate \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:43:50.639103+00:00
---

# gcloud alpha bq translation translate  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bq/translation/translate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha bq translation translate Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha bq translation translate - translate a SQL query from a source dialect to BigQuery 
SYNOPSIS
    

`gcloud alpha bq translation translate` `--location`=`LOCATION` `--source-dialect`=`SOURCE_DIALECT` `--target-dialect`=`TARGET_DIALECT` [`--explanation-output-file`=`EXPLANATION_OUTPUT_FILE`] [`--input-file`=`INPUT_FILE`] [`--metadata-gcs-uri`=`METADATA_GCS_URI`] [`--output-file`=`OUTPUT_FILE`] [`--source-ddl-output-file`=`SOURCE_DDL_OUTPUT_FILE`] [`--translation-config-files`=[`CONFIG_FILE`,…]] [`--translation-log-file`=`TRANSLATION_LOG_FILE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Translate a SQL query from a source dialect to BigQuery. 

The command reads a SQL query from standard input (or an input file) and prints the translated query to standard output (or an output file). 

EXAMPLES
     To translate a Snowflake query from stdin, run: 
    
    
    echo 'SELECT * FROM test.my_table;' | gcloud alpha bq translation translate --source-dialect=SNOWFLAKE --target-dialect=BIGQUERY --location=us

To translate a Snowflake query from a file and save the output and logs to files, run: 
    
    
    gcloud alpha bq translation translate --source-dialect=SNOWFLAKE --target-dialect=BIGQUERY --location=us --project=my-project --input-file=input.sql --output-file=output.sql --translation-log-file=translation_logs.yaml

REQUIRED FLAGS
    

`--location`=`LOCATION`
     Google Cloud Storage location to use for the translation. 
`--source-dialect`=`SOURCE_DIALECT`
     Source dialect of the query. See supported dialects in <https://docs.cloud.google.com/bigquery/docs/enable-sql-translations#supported_sql_dialects>
`--target-dialect`=`TARGET_DIALECT`
     Target dialect of the query. See supported dialects in <https://docs.cloud.google.com/bigquery/docs/enable-sql-translations#supported_sql_dialects>
OPTIONAL FLAGS
    

`--explanation-output-file`=`EXPLANATION_OUTPUT_FILE`
     File to which to write the translation explanation. 
`--input-file`=`INPUT_FILE`
     File from which to read the SQL query to translate. Can be piped through stdin as well. 
`--metadata-gcs-uri`=`METADATA_GCS_URI`
     Cloud Storage URI for the metadata zip file. 
`--output-file`=`OUTPUT_FILE`
     File to which to write the translated SQL. Writes to stdout if not provided or if set to ``-´´. 
`--source-ddl-output-file`=`SOURCE_DDL_OUTPUT_FILE`
     File to which to write the generated source DDL. 
`--translation-config-files`=[`CONFIG_FILE`,…]
     A comma-separated list of paths to YAML configuration files. File names must end with .config.yaml. See <https://docs.cloud.google.com/bigquery/docs/config-yaml-translation> for more details. 
`--translation-log-file`=`TRANSLATION_LOG_FILE`
     File to which to write the translation logs. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
