---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/bigtable/schema-bundles/create/
title: gcloud beta bigtable schema-bundles create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:10:14.185388+00:00
---

# gcloud beta bigtable schema-bundles create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/bigtable/schema-bundles/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta bigtable schema-bundles create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta bigtable schema-bundles create - create a new Bigtable schema bundle 
SYNOPSIS
    

`gcloud beta bigtable schema-bundles create` (`SCHEMA_BUNDLE` : `--instance`=`INSTANCE` `--table`=`TABLE`) `--proto-descriptors-file`=`PROTO_DESCRIPTORS_FILE` [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a new Bigtable schema bundle. 
EXAMPLES
     To create a schema bundle `my-schema-bundle` in instance `my-instance` and table `my-table`, using the descriptor file `my-descriptor-file.pb`: 
    
    
    gcloud beta bigtable schema-bundles create my-schema-bundle --instance=test-instance --table=test-table --proto-descriptors-file=my-descriptor-file.pb

POSITIONAL ARGUMENTS
    

Schema bundle resource - Bigtable schema bundle to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `schema_bundle` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`SCHEMA_BUNDLE`
     ID of the schema-bundle or fully qualified identifier for the schema-bundle. 

To set the `schema_bundle` attribute: 

  * provide the argument `schema_bundle` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--instance`=`INSTANCE`
     Name of the Bigtable instance. 

To set the `instance` attribute: 

  * provide the argument `schema_bundle` on the command line with a fully specified name; 
  * provide the argument `--instance` on the command line. 


`--table`=`TABLE`
     Name of the Bigtable table. 

To set the `table` attribute: 

  * provide the argument `schema_bundle` on the command line with a fully specified name; 
  * provide the argument `--table` on the command line. 


REQUIRED FLAGS
    

The schema to include in the bundle. Exactly one of these must be specified: 

`--proto-descriptors-file`=`PROTO_DESCRIPTORS_FILE`
     Path of a file that contains a protobuf-serialized `google.protobuf.FileDescriptorSet` message. If specified, the schema bundle contains the protobuf schema. To generate the file, install and run `protoc` with the following command: 
    
    
    protoc --proto_path=IMPORT_PATH --include_imports --descriptor_set_out=DESCRIPTOR_OUTPUT_LOCATION path/to/file.proto

where the --proto_path option specifies where to look for .proto files when resolving import directives (the current directory is used if you do not provide a value), and the --descriptor_set_out option specifies where you want the generated FileDescriptorSet to be written. 

OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `bigtableadmin/v2` API. The full documentation for this API can be found at: <https://cloud.google.com/bigtable/>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud bigtable schema-bundles create](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/schema-bundles/create)
    
    
    [gcloud alpha bigtable schema-bundles create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bigtable/schema-bundles/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
