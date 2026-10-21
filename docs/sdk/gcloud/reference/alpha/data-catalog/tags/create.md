---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/data-catalog/tags/create/
title: gcloud alpha data-catalog tags create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:01:44.352422+00:00
---

# gcloud alpha data-catalog tags create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/data-catalog/tags/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha data-catalog tags create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha data-catalog tags create - create a Data Catalog entry tag 
SYNOPSIS
    

`gcloud alpha data-catalog tags create` `--tag-file`=`TAG_FILE` (`--entry`=`ENTRY` : `--entry-group`=`ENTRY_GROUP` `--location`=`LOCATION`) (`--tag-template`=`TAG_TEMPLATE` : `--tag-template-location`=`TAG_TEMPLATE_LOCATION` `--tag-template-project`=`TAG_TEMPLATE_PROJECT`) [`--scope`=`SCOPE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `(DEPRECATED)` This command is deprecated. Please use `[gcloud dataplex entries](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/entries)` instead. Note that aspects - successors of tags - are part of the entry resource and are managed by `[gcloud dataplex entries](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/entries)` command. 

Create a Data Catalog entry tag. 

EXAMPLES
     Create a Data Catalog entry tag: 
    
    
    gcloud alpha data-catalog tags create --entry=ENTRY --tag-template=TAG_TEMPLATE --tag-file=TAG_FILE

REQUIRED FLAGS
    

`--tag-file`=`TAG_FILE`
     Path to a JSON or YAML file containing the tag. 

The file should contain a JSON/YAML object with a key and value for each field that should be set. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on how to specify timestamp fields. 

For example: 
    
    
    {
      "dbl_field": 123,
      "str_field": "String",
      "bool_field": true,
      "ts_field": "1970-01-01T00:00:00.000Z",
      "enum_field": "ENUM_A",
    }

Entry resource - Entry to attach the tag to. The arguments in this group can be used to specify the attributes of this resource. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--entry` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--entry`=`ENTRY`
     ID of the entry or fully qualified identifier for the entry. 

To set the `entry` attribute: 

  * provide the argument `--entry` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--entry-group`=`ENTRY_GROUP`
     Entry group of the entry. To set the `entry-group` attribute: 

  * provide the argument `--entry` on the command line with a fully specified name; 
  * provide the argument `--entry-group` on the command line. 


`--location`=`LOCATION`
     Location of the entry. To set the `location` attribute: 

  * provide the argument `--entry` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


Tag template resource - Tag template. `--tag-template-location` defaults to the tag's location. `--tag-template-project` defaults to the tag's project. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`--tag-template`=`TAG_TEMPLATE`
     ID of the tag template or fully qualified identifier for the tag template. 

To set the `tag_template` attribute: 

  * provide the argument `--tag-template` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--tag-template-location`=`TAG_TEMPLATE_LOCATION`
     Location of the tag template. To set the `location` attribute: 

  * provide the argument `--tag-template` on the command line with a fully specified name; 
  * provide the argument `--tag-template-location` on the command line; 
  * provide the argument `--location` on the command line. 


`--tag-template-project`=`TAG_TEMPLATE_PROJECT`
     Project of the tag template. To set the `project` attribute: 

  * provide the argument `--tag-template` on the command line with a fully specified name; 
  * provide the argument `--tag-template-project` on the command line; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


OPTIONAL FLAGS
    

`--scope`=`SCOPE`
     Scope within the parent resource that the tag is attached to. Scopes allow users to attach tags to individual columns based on the parent resource's schema. To attach a tag to a nested column, use '.' to separate the column names: 'outer_column.inner_column'. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `datacatalog/v1beta1` API. The full documentation for this API can be found at: <https://cloud.google.com/data-catalog/docs/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud data-catalog tags create](https://docs.cloud.google.com/sdk/gcloud/reference/data-catalog/tags/create)
    
    
    [gcloud beta data-catalog tags create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-catalog/tags/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
