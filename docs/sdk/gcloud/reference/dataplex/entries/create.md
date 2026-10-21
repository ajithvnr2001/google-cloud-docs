---
url: https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/entries/create/
title: gcloud dataplex entries create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:56:19.090778+00:00
---

# gcloud dataplex entries create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/entries/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud dataplex entries create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud dataplex entries create - create a Dataplex Entry resource 
SYNOPSIS
    

`gcloud dataplex entries create` (`ENTRY` : `--entry-group`=`ENTRY_GROUP` `--location`=`LOCATION`) (`--entry-type`=`ENTRY_TYPE` : `--entry-type-location`=`ENTRY_TYPE_LOCATION` `--entry-type-project`=`ENTRY_TYPE_PROJECT`) [`--aspects`=`YAML_OR_JSON_FILE`] [`--fully-qualified-name`=`FULLY_QUALIFIED_NAME`] [`--parent-entry`=`PARENT_ENTRY`] [`--entry-source-ancestors`=[`ANCESTORS`,…] `--entry-source-create-time`=`DATE_TIME` `--entry-source-description`=`DESCRIPTION` `--entry-source-display-name`=`DISPLAY_NAME` `--entry-source-labels`=[`KEY`=`VALUE`,…] `--entry-source-platform`=`PLATFORM_NAME` `--entry-source-resource`=`RESOURCE` `--entry-source-system`=`SYSTEM_NAME` `--entry-source-update-time`=`DATE_TIME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a Dataplex Entry resource. 
EXAMPLES
     To create a Dataplex entry with name `my-dataplex-entry` in location `us-central1` in entry group `my-entry-group` and with entry type projects/my-project/locations/us-central1/entryTypes/my-type, run: 
    
    
    gcloud dataplex entries create my-dataplex-entry --location=us-central1 --entry_group=my-entry-group --entry-type projects/my-project/locations/us-central1/entryTypes/my-type

To create a Dataplex Entry with name `my-child-entry` and set its parent to an existing entry `my-parent-entry`, run: 
    
    
    gcloud dataplex entries create my-child-entry --location=us-central1 --entry_group=my-entry-group --entry-type projects/my-project/locations/us-central1/entryTypes/my-type --parent-entry projects/my-project/locations/us-central1/entryGroups/my-entry-group/entries/my-parent-entry

To create a Dataplex Entry with its description, display name, ancestors, labels and timestamps populated in its EntrySource, run: 
    
    
    gcloud dataplex entries create my-entry --location=us-central1 --entry_group=my-entry-group --entry-type projects/my-project/locations/us-central1/entryTypes/my-type --entry-source-description 'This is a description of the Entry.' --entry-source-display-name 'display name' --entry-source-ancestors '{"type":"projects/my-project/locations/us-central1/entryTypes/some-type",
     "name":"projects/my-project/locations/us-central1/entryGroups/my-en\
    try-group/entries/ancestor-entry"},
     {"type":"projects/my-project/locations/us-central1/entryTypes/anoth\
    er-type",
     "name":"projects/my-project/locations/us-central1/entryGroups/my-en\
    try-group/entries/another-ancestor-entry"}' \
        --entry-source-labels key1=value1,key2=value2 \
        --entry-source-create-time 2024-01-01T09:39:25.160173Z \
        --entry-source-update-time 2024-01-01T09:39:25.160173Z

To create a Dataplex Entry reading its aspects from a YAML file, run: 
    
    
    gcloud dataplex entries create my-entry --location=us-central1 --entry_group=my-entry-group --entry-type projects/my-project/locations/us-central1/entryTypes/my-type --aspects aspects.yaml

The file containing the aspects has the following format: 
    
    
    my-project.us-central1.my-aspect-type:
      aspectType: my-project.us-central1.my-aspect-type
      createTime: "2024-01-01T09:39:25.160173Z"
      updateTime: "2024-01-01T09:39:25.160173Z"
      data:
        {}

POSITIONAL ARGUMENTS
    

Entry resource - Arguments and flags that define the Dataplex Entry you want to reference. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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
     Entry group containing Dataplex Entries. To set the `entry-group` attribute: 

  * provide the argument `entry` on the command line with a fully specified name; 
  * provide the argument `--entry-group` on the command line. 


`--location`=`LOCATION`
     Location of the Dataplex resource. To set the `location` attribute: 

  * provide the argument `entry` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `dataplex/location`. 


REQUIRED FLAGS
    

Entry type resource - Arguments and flags that define the Dataplex EntryType you want to reference. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`--entry-type`=`ENTRY_TYPE`
     ID of the entry type or fully qualified identifier for the entry type. 

To set the `entry_type` attribute: 

  * provide the argument `--entry-type` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--entry-type-location`=`ENTRY_TYPE_LOCATION`
     The location of the EntryType resource. 

To set the `entry-type-location` attribute: 

  * provide the argument `--entry-type` on the command line with a fully specified name; 
  * provide the argument `--entry-type-location` on the command line. 


`--entry-type-project`=`ENTRY_TYPE_PROJECT`
     The project of the EntryType resource. 

To set the `entry-type-project` attribute: 

  * provide the argument `--entry-type` on the command line with a fully specified name; 
  * provide the argument `--entry-type-project` on the command line. 


OPTIONAL FLAGS
    

`--aspects`=`YAML_OR_JSON_FILE`
     Path to a YAML or JSON file containing Aspects to add or update. 

When this flag is specified, only Aspects referenced in the file are going to be added or updated. Specifying this flag does not remove any Aspects from the entry. In other words, specifying this flag will not lead to a full replacement of Aspects with a contents of the provided file. 

Content of the file contains a map, where keys are in the format ``ASPECT_TYPE@PATH``, or just ``ASPECT_TYPE``, if the Aspect is attached to an entry itself rather than to a specific column defined in the schema. 

Values in the map represent Aspect's content, which must conform to a template defined for a given ``ASPECT_TYPE``. Each Aspect will be replaced fully by the provided content. That means data in the Aspect will be replaced and not merged with existing contents of that Aspect in the Entry. 

``ASPECT_TYPE`` is expected to be in a format ``PROJECT_ID.LOCATION.ASPECT_TYPE_ID``. 

``PATH`` can be either empty (which means a 'root' path, such that Aspect is attached to the entry itself) or point to a specific column defined in the schema. For example: `Schema.some_column`. 

Example YAML format: 
    
    
      project-id1.us-central1.my-aspect-type1:
        data:
          aspectField1: someValue
          aspectField2: someOtherValue
      project-id2.us-central1.my-aspect-type2@Schema.column1:
        data:
          aspectField3: someValue3

Example JSON format: 
    
    
      {
        "project-id1.us-central1.my-aspect-type1": {
          "data": {
            "aspectField1": "someValue",
            "aspectField2": "someOtherValue"
          }
        },
        "project-id2.us-central1.my-aspect-type2@Schema.column1": {
          "data": {
            "aspectField3": "someValue3"
          }
        }
      }

`--fully-qualified-name`=`FULLY_QUALIFIED_NAME`
     A name for the entry that can reference it in an external system. The maximum size of the field is 4000 characters. 
Entry resource - Arguments and flags that define the parent Entry you want to reference. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--parent-entry` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--parent-entry` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `dataplex/location`. 



To set the `entry_group` attribute: 

  * provide the argument `--parent-entry` on the command line with a fully specified name; 
  * provide the argument `--entry_group` on the command line. 


`--parent-entry`=`PARENT_ENTRY`
     ID of the entry or fully qualified identifier for the entry. 

To set the `entry` attribute: 

  * provide the argument `--parent-entry` on the command line. 


Source system related information for an entry. If any of the entry source fields are specified, then ``--entry-source-update-time` must be specified as well. `
`--entry-source-ancestors`=[`ANCESTORS`,…]
     Information about individual items in the hierarchy of an Entry. 
`--entry-source-create-time`=`DATE_TIME`
     The creation date and time of the resource in the source system. 
`--entry-source-description`=`DESCRIPTION`
     Description of the Entry. 
`--entry-source-display-name`=`DISPLAY_NAME`
     User friendly display name. 
`--entry-source-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. `

`--entry-source-platform`=`PLATFORM_NAME`
     The platform containing the source system. 
`--entry-source-resource`=`RESOURCE`
     The name of the resource in the source system. 
`--entry-source-system`=`SYSTEM_NAME`
     The name of the source system. 
`--entry-source-update-time`=`DATE_TIME`
     The update date and time of the resource in the source system. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud alpha dataplex entries create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/entries/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
