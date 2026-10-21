---
url: https://docs.cloud.google.com/sdk/gcloud/reference/data-catalog/entries/update/
title: gcloud data-catalog entries update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:12:58.704426+00:00
---

# gcloud data-catalog entries update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/data-catalog/entries/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud data-catalog entries update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud data-catalog entries update - update a Data Catalog entry 
SYNOPSIS
    

`gcloud data-catalog entries update` [`ENTRY` : `--entry-group`=`ENTRY_GROUP` `--location`=`LOCATION`] [`--description`=`DESCRIPTION`] [`--display-name`=`DISPLAY_NAME`] [`--lookup-entry`=`RESOURCE`] [`--add-file-patterns`=[`PATTERN`,…] `--clear-file-patterns` | `--remove-file-patterns`=[`PATTERN`,…] | `--linked-resource`=`LINKED_RESOURCE` `--user-specified-system`=`USER_SPECIFIED_SYSTEM` `--user-specified-type`=`USER_SPECIFIED_TYPE`] [`--schema`=[`COLUMN_NAME`=`COLUMN_TYPE`,…] | `--schema-from-file`=`PATH_TO_FILE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(DEPRECATED)` This command is deprecated. Please use `[gcloud dataplex entries](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/entries)` instead. 

Update a Data Catalog entry. The entry to update can either be specified directly, or the `--lookup-entry` flag may be used to update the entry corresponding to the lookup of the given resource. 

EXAMPLES
     To update the schema of a Cloud Pub/Sub entry inline, run: 
    
    
    gcloud data-catalog entries update entry1 --location=global --entry-group=@pubsub --schema="column1=type1,column2=type2"

To update the schema of a Cloud Pub/Sub entry from a file, run: 
    
    
    gcloud data-catalog entries update entry1 --location=global --entry-group=@pubsub --schema-from-file="/tmp/schema.json"

To lookup the entry of a Cloud Pub/Sub topic by its SQL name and update its schema in one command, run: 
    
    
    gcloud data-catalog entries update --lookup-entry='pubsub.topic.`my-project1`.topic1' --schema="column1=type1,column2=type2"

POSITIONAL ARGUMENTS
    

Entry resource - Entry to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `entry` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


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


FLAGS
    

`--description`=`DESCRIPTION`
     Textual description of the entry. 
`--display-name`=`DISPLAY_NAME`
     Human-readable name for the entry. 
`--lookup-entry`=`RESOURCE`
     The name of the target resource whose entry to update. This can be either the Google Cloud Platform resource name or the SQL name of a Google Cloud Platform resource. This flag allows one to update the entry corresponding to the lookup of the given resource, without needing to specify the entry directly. 
At most one of these can be specified: 

`--add-file-patterns`=[`PATTERN`,…]
     A list of file patterns to add to the current list. 
At most one of these can be specified: 

`--clear-file-patterns`
     If specified, clear the current list of file patterns. 
`--remove-file-patterns`=[`PATTERN`,…]
     A list of file patterns to remove from the current list. 
`--linked-resource`=`LINKED_RESOURCE`
     Link to the resource in external system. If `--type` is not used, then `--linked-resource` may be provided. 
`--user-specified-system`=`USER_SPECIFIED_SYSTEM`
     External system from which the entry is fed. This can be updated for on prem entries. 
`--user-specified-type`=`USER_SPECIFIED_TYPE`
     Type of the entry coming from external system. This can be updated for on prem entries. 
New column schema for the entry. A schema consists of a list of column names along with their types, descriptions, modes, and nested subcolumns. For example: 
    
    
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
     This command uses the `datacatalog/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/data-catalog/docs/>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha data-catalog entries update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/data-catalog/entries/update)
    
    
    [gcloud beta data-catalog entries update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-catalog/entries/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
