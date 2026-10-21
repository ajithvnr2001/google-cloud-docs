---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/databases/ddl/update/
title: gcloud alpha spanner databases ddl update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:51:32.199486+00:00
---

# gcloud alpha spanner databases ddl update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/databases/ddl/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha spanner databases ddl update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha spanner databases ddl update - update the DDL for a Cloud Spanner database 
SYNOPSIS
    

`gcloud alpha spanner databases ddl update` (`DATABASE` : `--instance`=`INSTANCE`) [`--async`] [`--ddl`=`DDL`] [`--ddl-file`=`DDL_FILE`] [`--proto-descriptors-file`=`PROTO_DESCRIPTORS_FILE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update the DDL for a Cloud Spanner database. 
EXAMPLES
     To add a column to a table in the given Cloud Spanner database, run: 
    
    
    gcloud alpha spanner databases ddl update my-database-id --instance=my-instance-id --ddl='ALTER TABLE test_table ADD COLUMN a INT64'

POSITIONAL ARGUMENTS
    

Database resource - The Cloud Spanner database of which the ddl to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `database` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`DATABASE`
     ID of the database or fully qualified identifier for the database. 

To set the `database` attribute: 

  * provide the argument `database` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--instance`=`INSTANCE`
     The Cloud Spanner instance for the database. 

To set the `instance` attribute: 

  * provide the argument `database` on the command line with a fully specified name; 
  * provide the argument `--instance` on the command line; 
  * set the property `spanner/instance`. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--ddl`=`DDL`
     Semi-colon separated DDL (data definition language) statements to run inside the database. If a statement fails, all subsequent statements in the batch are automatically cancelled. 
`--ddl-file`=`DDL_FILE`
     Path of a file containing semi-colon separated DDL (data definition language) statements to run inside the database. If a statement fails, all subsequent statements in the batch are automatically cancelled. If --ddl_file is set, --ddl is ignored. One line comments starting with -- are ignored. 
`--proto-descriptors-file`=`PROTO_DESCRIPTORS_FILE`
     Path of a file that contains a protobuf-serialized google.protobuf.FileDescriptorSet message. To generate it, install and run `protoc` with --include_imports and --descriptor_set_out. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud spanner databases ddl update](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/databases/ddl/update)
    
    
    [gcloud beta spanner databases ddl update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/databases/ddl/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
