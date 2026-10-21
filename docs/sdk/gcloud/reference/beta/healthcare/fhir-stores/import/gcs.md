---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/healthcare/fhir-stores/import/gcs/
title: gcloud beta healthcare fhir-stores import gcs \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:35:39.480394+00:00
---

# gcloud beta healthcare fhir-stores import gcs  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/healthcare/fhir-stores/import/gcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta healthcare fhir-stores import gcs Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta healthcare fhir-stores import gcs - import FHIR resources from Google Cloud Storage into a Cloud Healthcare API FHIR store 
SYNOPSIS
    

`gcloud beta healthcare fhir-stores import gcs` (`FHIR_STORE` : `--dataset`=`DATASET` `--location`=`LOCATION`) `--gcs-uri`=`GCS_URI` [`--async`] [`--content-structure`=`CONTENT_STRUCTURE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Import FHIR resources from Google Cloud Storage into a Cloud Healthcare API FHIR store. 
EXAMPLES
     To import the FHIR resources from the existing bucket 'testGcsBucket' in the folder 'someFolder' into the FHIR store 'test-fhir-store', run: 
    
    
    gcloud beta healthcare fhir-stores import gcs test-fhir-store --gcs-uri=gs://testGcsBucket/someFolder/* --dataset=test-dataset

To perform the same import, but importing resources with the content structure of 'RESOURCE', run: 
    
    
    gcloud beta healthcare fhir-stores import gcs test-fhir-store --gcs-uri=gs://testGcsBucket/someFolder/* --dataset=test-dataset --content-structure=RESOURCE

POSITIONAL ARGUMENTS
    

FhirStore resource - Cloud Healthcare API FHIR store into which the data is imported. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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
    

`--gcs-uri`=`GCS_URI`
     Cloud Storage source data locations. Each Cloud Storage object should be a text file that contains newline-delimited JSON structures conforming to the FHIR standard. You can use wildcards to import multiple files from one or more directories. 

  * Use * to match 0 or more non-separator characters. For example, gs://BUCKET/DIRECTORY/Example`*`.ndjson matches Example.ndjson and Example22.ndjson in DIRECTORY. 
  * Use ** to match 0 or more characters (including separators). Must be used at the end of a path and with no other wildcards in the path. Can also be used with a filename extension (such as .ndjson), which imports all files with the filename extension in the specified directory and its subdirectories. For example, gs://BUCKET/DIRECTORY/**.ndjson imports all files with the .ndjson filename extension in DIRECTORY and its subdirectories. 
  * Use ? to match 1 character. For example, gs://BUCKET/DIRECTORY/Example?.ndjson matches Example1.ndjson but does not match Example.ndjson or Example01.ndjson. 


OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--content-structure`=`CONTENT_STRUCTURE`
     Content structure in the source location. The default is BUNDLE. `CONTENT_STRUCTURE` must be one of: 

`bundle`
     Each unit is a bundle, which contains one or more resources. 
`bundle-pretty`
     The entire file is one JSON bundle. The JSON can span multiple lines. 
`resource`
     Each unit is a single resource. 
`resource-pretty`
     The entire file is one JSON resource. The JSON can span multiple lines. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `healthcare/v1beta1` API. The full documentation for this API can be found at: <https://cloud.google.com/healthcare>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud healthcare fhir-stores import gcs](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/import/gcs)
    
    
    [gcloud alpha healthcare fhir-stores import gcs](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/healthcare/fhir-stores/import/gcs)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
