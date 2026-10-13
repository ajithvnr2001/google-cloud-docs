---
url: https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/update/
title: gcloud healthcare fhir-stores update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:26.201516+00:00
---

# gcloud healthcare fhir-stores update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud healthcare fhir-stores update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud healthcare fhir-stores update - update a Cloud Healthcare API FHIR store 
SYNOPSIS
    

`gcloud healthcare fhir-stores update` (`FHIR_STORE` : `--dataset`=`DATASET` `--location`=`LOCATION`) [`--enable-update-create`] [`--pubsub-topic`=`PUBSUB_TOPIC`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update a Cloud Healthcare API FHIR store. 
EXAMPLES
     To update the Cloud Pub/Sub topic on a FHIR store 'test-fhir-store', run: 
    
    
    gcloud healthcare fhir-stores update test-fhir-store --pubsub-topic=projects/my-project/topics/test-pubsub-topic

POSITIONAL ARGUMENTS
    

FhirStore resource - The Cloud Healthcare API FHIR store you want to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `fhir_store` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`FHIR_STORE`
     ID of the fhirStore or fully qualified identifier for the fhirStore. 

To set the `fhir_store` attribute: 

  * provide the argument `fhir_store` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--dataset`=`DATASET`
     Cloud Healthcare dataset. 

To set the `dataset` attribute: 

  * provide the argument `fhir_store` on the command line with a fully specified name; 
  * provide the argument `--dataset` on the command line. 


`--location`=`LOCATION`
     Google Cloud location. 

To set the `location` attribute: 

  * provide the argument `fhir_store` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `healthcare/location`. 


FLAGS
    

`--enable-update-create`
     Whether this FHIR store has the [updateCreate] (https://www.hl7.org/fhir/capabilitystatement-definitions.html#CapabilityStatement.rest.resource.updateCreate) capability. Determines if the client can use an Update operation to create a new resource with a client-specified ID. If false, all IDs are server-assigned through the Create operation and attempts to Update a non-existent resource will return errors. 
`--pubsub-topic`=`PUBSUB_TOPIC`
     Google Cloud Pub/Sub topic to send updates to. 

Note, a topic needs to be created before publishing or subscribing to it. For instructions on creating topics, refer to: <https://cloud.google.com/pubsub/docs/admin#create_a_topic>

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `healthcare/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/healthcare>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha healthcare fhir-stores update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/healthcare/fhir-stores/update)
    
    
    [gcloud beta healthcare fhir-stores update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/healthcare/fhir-stores/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
