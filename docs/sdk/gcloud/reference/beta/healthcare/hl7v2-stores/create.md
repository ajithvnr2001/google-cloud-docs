---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/healthcare/hl7v2-stores/create/
title: gcloud beta healthcare hl7v2-stores create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:35:40.405968+00:00
---

# gcloud beta healthcare hl7v2-stores create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/healthcare/hl7v2-stores/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta healthcare hl7v2-stores create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta healthcare hl7v2-stores create - create a Cloud Healthcare API HL7v2 store 
SYNOPSIS
    

`gcloud beta healthcare hl7v2-stores create` (`HL7V2_STORE` : `--dataset`=`DATASET` `--location`=`LOCATION`) [`--parser-version`=`PARSER_VERSION`] [`--pubsub-topic`=`PUBSUB_TOPIC`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a Cloud Healthcare API HL7v2 store. 
EXAMPLES
     To create a HL7v2 store called 'test-hl7v2-store', run: 
    
    
    gcloud beta healthcare hl7v2-stores create test-hl7v2-store --dataset=test-dataset

To create a HL7v2 store with the Cloud Pub/Sub topic 'test-pubsub-topic', run: 
    
    
    gcloud beta healthcare hl7v2-stores create test-hl7v2-store --dataset=test-dataset --pubsub-topic=projects/my-project/topics/test-pubsub-topic

POSITIONAL ARGUMENTS
    

Hl7v2Store resource - Cloud Healthcare API HL7v2 store to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `hl7v2_store` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`HL7V2_STORE`
     ID of the hl7v2Store or fully qualified identifier for the hl7v2Store. 

To set the `hl7v2_store` attribute: 

  * provide the argument `hl7v2_store` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--dataset`=`DATASET`
     Cloud Healthcare dataset. 

To set the `dataset` attribute: 

  * provide the argument `hl7v2_store` on the command line with a fully specified name; 
  * provide the argument `--dataset` on the command line. 


`--location`=`LOCATION`
     Google Cloud location. 

To set the `location` attribute: 

  * provide the argument `hl7v2_store` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `healthcare/location`. 


FLAGS
    

`--parser-version`=`PARSER_VERSION`
     Immutable. Determines the version of both the default parser to be used when [schema](https://cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores#ParserConfig.FIELDS.schema) is not given, as well as the schematized parser used when [schema](https://cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores#ParserConfig.FIELDS.schema) is specified. This field is immutable after HL7v2 store creation. `PARSER_VERSION` must be one of: 

`v1`
     The parsedData includes every given non-empty message field except the Field Separator (MSH-1) field. As a result, the parsed MSH segment starts with the MSH-2 field and the field numbers are off-by-one with respect to the HL7 standard. 
`v2`
     The parsedData includes every given non-empty message field. 
`v3`
     This version is the same as V2, with the following change. The parsedData contains unescaped escaped field separators, component separators, sub-component separators, repetition separators, escape characters, and truncation characters. If [schema](https://cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores#ParserConfig.FIELDS.schema) is specified, the schematized parser uses improved parsing heuristics compared to previous versions. 
`--pubsub-topic`=`PUBSUB_TOPIC`
     A Google Cloud Pub/Sub topic name for notifications. 

Note: A topic must be created before publishing or subscribing to it. For instructions on creating topics, refer to: <https://cloud.google.com/pubsub/docs/admin#create_a_topic>

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `healthcare/v1beta1` API. The full documentation for this API can be found at: <https://cloud.google.com/healthcare>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud healthcare hl7v2-stores create](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/create)
    
    
    [gcloud alpha healthcare hl7v2-stores create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/healthcare/hl7v2-stores/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
