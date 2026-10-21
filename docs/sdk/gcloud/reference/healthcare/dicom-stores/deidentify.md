---
url: https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/deidentify/
title: gcloud healthcare dicom-stores deidentify \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:22.234623+00:00
---

# gcloud healthcare dicom-stores deidentify  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/deidentify/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud healthcare dicom-stores deidentify Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud healthcare dicom-stores deidentify - de-identify data from the source store and write it to the destination store 
SYNOPSIS
    

`gcloud healthcare dicom-stores deidentify` (`DICOM_STORE` : `--dataset`=`DATASET` `--location`=`LOCATION`) `--destination-store`=`DESTINATION_STORE` [`--async`] [`--dicom-filter-tags`=[`DICOM_FILTER_TAGS`,…]] [`--text-redaction-mode`=`TEXT_REDACTION_MODE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     De-identify data from the source store and write it to the destination store. 
EXAMPLES
     To generate a de-identified version of the DICOM store 'test-dicom-store', run the command below. 
    
    
    gcloud healthcare dicom-stores deidentify test-dicom-store --destination-store=projects/{projectId}/locations/us-central1/datasets/{datasetId}/dicomStores/test-deid-dicom-store --dicom-filter-tags=MediaStorageSOPClassUID,SeriesInstanceUID,StudyInstanceUID

POSITIONAL ARGUMENTS
    

DicomStore resource - Source Cloud Healthcare API DICOM store to deidentify. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `dicom_store` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`DICOM_STORE`
     ID of the dicomStore or fully qualified identifier for the dicomStore. 

To set the `dicom_store` attribute: 

  * provide the argument `dicom_store` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--dataset`=`DATASET`
     Cloud Healthcare dataset. 

To set the `dataset` attribute: 

  * provide the argument `dicom_store` on the command line with a fully specified name; 
  * provide the argument `--dataset` on the command line. 


`--location`=`LOCATION`
     Google Cloud location. 

To set the `location` attribute: 

  * provide the argument `dicom_store` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `healthcare/location`. 


REQUIRED FLAGS
    

`--destination-store`=`DESTINATION_STORE`
     The name of the DICOM store to which the redacted data should be written (e.g., projects/{projectId}/locations/{locationId}/datasets/{datasetId}/dicomStores/{dicomStoreId}). The destination DICOM store must already exist, or the request will fail. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--dicom-filter-tags`=[`DICOM_FILTER_TAGS`,…]
     Tags to be filtered. Tags must be DICOM Data Elements, File Meta Elements, or Directory Structuring Elements, as defined at: http://dicom.nema.org/medical/dicom/current/output/html/part06.html#table_6-1,. They may be provided by "Keyword" or "Tag". For example "PatientID", "0010,0010". 
`--text-redaction-mode`=`TEXT_REDACTION_MODE`
     Determines how to redact text from image. `TEXT_REDACTION_MODE` must be (only one value is supported): 

`all`
     Redact all text. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `healthcare/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/healthcare>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha healthcare dicom-stores deidentify](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/healthcare/dicom-stores/deidentify)
    
    
    [gcloud beta healthcare dicom-stores deidentify](https://docs.cloud.google.com/sdk/gcloud/reference/beta/healthcare/dicom-stores/deidentify)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
