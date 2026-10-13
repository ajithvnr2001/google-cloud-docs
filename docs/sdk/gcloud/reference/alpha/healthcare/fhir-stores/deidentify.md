---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/healthcare/fhir-stores/deidentify/
title: gcloud alpha healthcare fhir-stores deidentify \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:29:55.583382+00:00
---

# gcloud alpha healthcare fhir-stores deidentify  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/healthcare/fhir-stores/deidentify/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha healthcare fhir-stores deidentify Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha healthcare fhir-stores deidentify - de-identify data from the source store and write it to the destination store 
SYNOPSIS
    

`gcloud alpha healthcare fhir-stores deidentify` (`FHIR_STORE` : `--dataset`=`DATASET` `--location`=`LOCATION`) `--destination-store`=`DESTINATION_STORE` [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` De-identify data from the source store and write it to the destination store. 
EXAMPLES
     To generate a de-identified version of the FHIR store 'test-fhir-store', run the command below. 
    
    
    gcloud alpha healthcare fhir-stores deidentify test-fhir-store --destination-store=projects/{projectId}/locations/us-central1/datasets/{datasetId}/fhirStores/test-deid-fhir-store

POSITIONAL ARGUMENTS
    

FhirStore resource - Source Cloud Healthcare API FHIR store to deidentify. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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


REQUIRED FLAGS
    

`--destination-store`=`DESTINATION_STORE`
     The name of the FHIR store to which the redacted data should be written (e.g., projects/{projectId}/locations/{locationId}/datasets/{datasetId}/fhirStores/{fhirStoreId}). The destination FHIR store must already exist, or the request will fail. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `healthcare/v1alpha2` API. The full documentation for this API can be found at: <https://cloud.google.com/healthcare>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud healthcare fhir-stores deidentify](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/deidentify)
    
    
    [gcloud beta healthcare fhir-stores deidentify](https://docs.cloud.google.com/sdk/gcloud/reference/beta/healthcare/fhir-stores/deidentify)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
