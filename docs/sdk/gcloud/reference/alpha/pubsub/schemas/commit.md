---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pubsub/schemas/commit/
title: gcloud alpha pubsub schemas commit \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:00:25.963210+00:00
---

# gcloud alpha pubsub schemas commit  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pubsub/schemas/commit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha pubsub schemas commit Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha pubsub schemas commit - commit a Pub/Sub schema revision 
SYNOPSIS
    

`gcloud alpha pubsub schemas commit` `SCHEMA` `--type`=`TYPE` (`--definition`=`DEFINITION` | `--definition-file`=`PATH_TO_FILE`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Commit a Pub/Sub schema revision. 
EXAMPLES
     To commit a PROTOCOL_BUFFER schema revision called "key-schema" that requires exactly one-string field named "key", run: 
    
    
    gcloud alpha pubsub schemas commit key-schema --definition="syntax = 'proto3'; message Message { optional string key = 1; }" --type=protocol-buffer To commit an equivalent AVRO schema revision, run:
    
    
    gcloud alpha pubsub schemas commit key-schema --definition="{ 'type': 'record', 'namespace': 'my.ns', 'name': 'KeyMsg', 'fields': [ { 'name': 'key', 'type': 'string' } ] }" --type=avro

POSITIONAL ARGUMENTS
    

Schema resource - Name of the schema to revise. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `schema` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`SCHEMA`
     ID of the schema or fully qualified identifier for the schema. 

To set the `schema` attribute: 

  * provide the argument `schema` on the command line. 


REQUIRED FLAGS
    

`--type`=`TYPE`
     The type of the schema. 
Schema definition. 

Exactly one of these must be specified: 

Text-based schema definition, specified as an inline string or a path to the file containing the definition. 

At most one of these can be specified: 

`--definition`=`DEFINITION`
     A string containing the new definition of the schema. 
`--definition-file`=`PATH_TO_FILE`
     Path to a file containing the new definition of the schema. Use a full or relative path to a local file containing the value of definition_file. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud pubsub schemas commit](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/schemas/commit)
    
    
    [gcloud beta pubsub schemas commit](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pubsub/schemas/commit)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
