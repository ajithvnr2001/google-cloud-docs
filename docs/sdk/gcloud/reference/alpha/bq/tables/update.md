---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bq/tables/update/
title: gcloud alpha bq tables update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:43:50.154221+00:00
---

# gcloud alpha bq tables update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bq/tables/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha bq tables update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha bq tables update - update a new BigQuery table 
SYNOPSIS
    

`gcloud alpha bq tables update` (`TABLE` : `--dataset`=`DATASET`) [`--description`=`DESCRIPTION`] [`--expiration`=`EXPIRATION`] [`--relax-columns`=[`FIELD_NAME`,…]] [`--add-columns`=[`FIELD_NAME`=`FIELD_TYPE`,…] | `--add-columns-file`=`PATH_TO_FILE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a new BigQuery table. Updates one or more attributes of a table or view. 
EXAMPLES
     The following command updates the description on a table with ID `my-table` in `my-dataset`: 
    
    
    gcloud alpha bq tables update /projects/myproject/datasets/my-dataset/tables/my-table --description 'My New Table'

The following command changes the schema mode from `REQUIRED` to `NULLABLE` on the `value` and `tags` columns in a table with ID `my-other-table` in dataset `my-other-dataset`: 
    
    
    gcloud alpha bq tables update my-other-table --dataset my-other-dataset --relax-columns name,tags

POSITIONAL ARGUMENTS
    

Table resource - The BigQuery table you want to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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

`--relax-columns`=[`FIELD_NAME`,…]
     A comma-separated list of field names in the current schema that should have their mode changed from REQUIRED to NULLABLE. 

For more details on updating and managing BigQuery schemas see: <https://cloud.google.com/bigquery/docs/managing-table-schemas>

Specify changes to the table schema. 

At most one of these can be specified: 

`--add-columns`=[`FIELD_NAME`=`FIELD_TYPE`,…]
     A comma-separated list of entries of the form FIELD_NAME[=FIELD_TYPE] specifying field names and types for the columns being added to the table. FIELD_TYPE defaults to string if not present. Possible FIELD_TYPES are `string`, `integer`, `float`, `boolean`, `record`, and `timestamp`. 

For more details on BigQuery schemas see: <https://cloud.google.com/bigquery/docs/schemas>. 

`--add-columns-file`=`PATH_TO_FILE`
     The name of a JSON file containing a single object containing an array each element of which is an object with properties name, type, and, optionally a mode (one of: `NULLABLE` or `REPEATED`), specifying the columns to be added to the table. If mode is omitted the default is 'NULLABLE'. 

For example: { 'schema': [ { 'name': 'field1', 'type': 'string', 'mode': 'REQUIRED' }, { 'name': 'field2', 'type': 'integer', 'mode': 'REPEATED' }, [ { 'name': 'fieldN', 'type': TYPE, ['mode': MODE] } … ] ] } 

For more details on BigQuery schemas see: <https://cloud.google.com/bigquery/docs/schemas>. 

Use a full or relative path to a local file containing the value of add_columns_file. 

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
