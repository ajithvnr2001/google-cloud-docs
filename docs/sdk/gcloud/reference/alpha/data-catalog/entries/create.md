---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/data-catalog/entries/create/
title: gcloud alpha data-catalog entries create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:01:40.016909+00:00
---

# gcloud alpha data-catalog entries create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/data-catalog/entries/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha data-catalog entries create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha data-catalog entries create - create a Data Catalog entry 
SYNOPSIS
    

`gcloud alpha data-catalog entries create` (`ENTRY` : `--entry-group`=`ENTRY_GROUP` `--location`=`LOCATION`) `--gcs-file-patterns`=[`GCS_FILE_PATTERNS`,…] [`--description`=`DESCRIPTION`] [`--display-name`=`DISPLAY_NAME`] [`--schema`=[`COLUMN_NAME`=`COLUMN_TYPE`,…] | `--schema-from-file`=`PATH_TO_FILE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `(DEPRECATED)` This command is deprecated. Please use `[gcloud dataplex entries](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/entries)` instead. 

Create a Data Catalog entry. 

EXAMPLES
     To create an entry for a Google Cloud Storage fileset, run: 
    
    
    gcloud alpha data-catalog entries create entry1 --location=us-central1 --entry-group=group1 --gcs-file-patterns="gs://bucket1/abc/*,gs://bucket1/file1" --display-name="analytics data"

To create an entry for a Google Cloud Storage fileset with an inline schema, run: 
    
    
    gcloud alpha data-catalog entries create entry1 --location=us-central1 --entry-group=group1 --gcs-file-patterns="gs://bucket1/*" --display-name="sales data" --schema="qtr=STRING,sales=FLOAT,year=STRING"

To create an entry for a Google Cloud Storage fileset with a schema from a file, run: 
    
    
    gcloud alpha data-catalog entries create entry1 --location=us-central1 --entry-group=group1 --gcs-file-patterns="gs://bucket1/*" --display-name="sales data" --schema-from-file=/tmp/schema.json

POSITIONAL ARGUMENTS
    

Entry resource - Entry to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `entry` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ENTRY`
     ID of the entry or fully qualified identifier for the entry. 

To set the `entry` attribute: 

  * provide the argument `entry` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--entry-group`=`ENTRY_GROUP`
     Entry group of the entry. To set the `entry-group` attribute: 

  * provide the argument `entry` on the command line with a fully specified name; 
  * provide the argument `--entry-group` on the command line. 


`--location`=`LOCATION`
     Location of the entry. To set the `location` attribute: 

  * provide the argument `entry` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--gcs-file-patterns`=[`GCS_FILE_PATTERNS`,…]
     Patterns to identify a set of files in Google Cloud Storage. A star (`*`) may be used at the end of a pattern to match arbitrary files beginning with that pattern. 

Examples of valid file patterns: 

  * gs://bucket_name/`*` \- Matches all files in 'bucket_name'. 
  * gs://bucket_name/file`*` \- Matches files prefixed by 'file' in 'bucket_name'. 
  * gs://another_bucket/a.txt - Matches 'gs://another_bucket/a.txt'. 


OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     Textual description of the entry. 
`--display-name`=`DISPLAY_NAME`
     Human-readable name for the entry. 
Column schema for the entry. A schema consists of a list of column names along with their types, descriptions, modes, and nested subcolumns. For example: 
    
    
    - column: first_name
      description: First name
      mode: REQUIRED
      type: STRING
    - column: last_name
      description: Last name
      mode: REQUIRED
      type: STRING
    - column: addresses
      description: Addresses
      mode: REPEATED
      type: RECORD
      subcolumns:
      - column: city
        description: City
        mode: NULLABLE
        type: STRING
      - column: state
        description: State
        mode: NULLABLE
        type: STRING

At most one of these can be specified: 

`--schema`=[`COLUMN_NAME`=`COLUMN_TYPE`,…]
     Inline schema for the entry. When specifying a schema via this argument, only column names and types should be provided. Column modes will default to NULLABLE, and column descriptions and nested subcolumns are not supported. 
`--schema-from-file`=`PATH_TO_FILE`
     Path to a JSON or YAML file containing the schema for the entry. This can be used to specify schemas with column descriptions, column modes other than NULLABLE, and nested subcolumns. Use a full or relative path to a local file containing the value of schema. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `datacatalog/v1beta1` API. The full documentation for this API can be found at: <https://cloud.google.com/data-catalog/docs/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud data-catalog entries create](https://docs.cloud.google.com/sdk/gcloud/reference/data-catalog/entries/create)
    
    
    [gcloud beta data-catalog entries create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-catalog/entries/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
