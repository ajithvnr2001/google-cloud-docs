---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bq/tables/create/
title: gcloud alpha bq tables create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:43:49.415049+00:00
---

# gcloud alpha bq tables create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bq/tables/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha bq tables create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha bq tables create - create a new BigQuery table 
SYNOPSIS
    

`gcloud alpha bq tables create` (`TABLE` : `--dataset`=`DATASET`) [`--description`=`DESCRIPTION`] [`--expiration`=`EXPIRATION`] [`--overwrite`] [`--schema`=[`FIELD_NAME`=`FIELD_TYPE`,…] | `--schema-file`=`PATH_TO_FILE` | [`--view`=`VIEW` : `--use-legacy-sql`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a new BigQuery table. Create a table or view with a specified name. A view is a collection of rows selected by a query in a flag, and manipulated as a table. The dataset to contain the table or view must already exist, and must not contain a table or view with the specified name. 
EXAMPLES
     The following command creates a table with ID `my-table` in `my-dataset`: 
    
    
    gcloud alpha bq tables create /projects/myproject/datasets/my-dataset/tables/my-table --description 'My New Table'

The following command creates a view with ID `my-view` in dataset `my-other-dataset`: 
    
    
    gcloud alpha bq tables create my-view --dataset my-other-dataset --view 'SELECT field1, field3 FROM
     `my-project.my-other-dataset.my-table`'

POSITIONAL ARGUMENTS
    

Table resource - The BigQuery table you want to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `table` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`TABLE`
     ID of the table or fully qualified identifier for the table. 

To set the `table` attribute: 

  * provide the argument `table` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--dataset`=`DATASET`
     The id of the BigQuery dataset. 

To set the `dataset` attribute: 

  * provide the argument `table` on the command line with a fully specified name; 
  * provide the argument `--dataset` on the command line. 


FLAGS
    

`--description`=`DESCRIPTION`
     Description of the table. 
`--expiration`=`EXPIRATION`
     How long after creation should this table or view expire e.g. 1d, 2w etc. 

See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats 

`--overwrite`
     Overwrite if the resource already exists. 
Specify the table schema. 

At most one of these can be specified: 

`--schema`=[`FIELD_NAME`=`FIELD_TYPE`,…]
     A comma-separated list of entries of the form FIELD_NAME[=FIELD_TYPE] specifying field names and types for the table being created. FIELD_TYPE defaults to string if not present. Possible FIELD_TYPES are `string`, `integer`, `float`, `boolean`, `record`, and `timestamp`. 

For more details on BigQuery schemas see: <https://cloud.google.com/bigquery/docs/schemas>. 

`--schema-file`=`PATH_TO_FILE`
     The name of a JSON file containing a single object containing an array each element of which is an object with properties name, type, and, optionally a mode (one of: `NULLABLE`, `REQUIRED` or `REPEATED`), specifying a schema for the table being created. If mode is omitted the default is 'NULLABLE'. 

For example: { 'schema': [ { 'name': 'field1', 'type': 'string', 'mode': 'REQUIRED' }, { 'name': 'field2', 'type': 'integer', 'mode': 'REPEATED' }, [ { 'name': 'fieldN', 'type': TYPE, ['mode': MODE] } … ] ] } 

For more details on BigQuery schemas see: <https://cloud.google.com/bigquery/docs/schemas>. 

Use a full or relative path to a local file containing the value of schema_file. 

Or at least one of these can be specified: 

Create a view instead of regular table. 
`--view`=`VIEW`
     Create a view with this SQL query. (If this flag is not specified, a table is created.) 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--use-legacy-sql`
     If specified, query will use BigQuery's legacy SQL syntax. If not specified, query will use BigQuery's standard SQL dialect by default (https://cloud.google.com/bigquery/sql-reference/). 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `bigquery/v2` API. The full documentation for this API can be found at: <https://cloud.google.com/bigquery/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
