---
url: https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/schemas/validate-schema/
title: gcloud pubsub schemas validate-schema \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:26:02.386649+00:00
---

# gcloud pubsub schemas validate-schema  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/schemas/validate-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud pubsub schemas validate-schema Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud pubsub schemas validate-schema - validate a Pub/Sub schema 
SYNOPSIS
    

`gcloud pubsub schemas validate-schema` `--type`=`TYPE` (`--definition`=`DEFINITION` | `--definition-file`=`PATH_TO_FILE`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Validate a new Pub/Sub schema. 
EXAMPLES
     To validate a PROTOCOL_BUFFER schema, run: 
    
    
    gcloud pubsub schemas validate-schema --definition="syntax = 'proto3'; message Message { optional string key = 1; }" --type=PROTOCOL_BUFFER

To validate an equivalent AVRO schema, run: 
    
    
    gcloud pubsub schemas validate-schema --definition='{ "type": "record", "namespace": "my.ns", "name":
     "KeyMsg", "fields": [ { "name": "key", "type": "string" } ] }' \
        --type=AVRO

REQUIRED FLAGS
    

`--type`=`TYPE`
     Type of the schema. `TYPE` must be one of: `avro`, `protocol-buffer`. 
Schema definition. Exactly one of these must be specified: 

`--definition`=`DEFINITION`
     Inline schema definition. 
`--definition-file`=`PATH_TO_FILE`
     File containing schema definition. Use a full or relative path to a local file containing the value of definition_file. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `pubsub/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/pubsub/docs>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha pubsub schemas validate-schema](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pubsub/schemas/validate-schema)
    
    
    [gcloud beta pubsub schemas validate-schema](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pubsub/schemas/validate-schema)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
