---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/healthcare/datasets/deidentify/
title: gcloud beta healthcare datasets deidentify \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:35:35.519477+00:00
---

# gcloud beta healthcare datasets deidentify  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/healthcare/datasets/deidentify/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta healthcare datasets deidentify Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta healthcare datasets deidentify - create a new Cloud Healthcare API dataset containing de-identified data from the source dataset 
SYNOPSIS
    

`gcloud beta healthcare datasets deidentify` (`DATASET` : `--location`=`LOCATION`) `--destination-dataset`=`DESTINATION_DATASET` [`--async`] [`--default-fhir-config`] [`--dicom-filter-tags`=[`DICOM_FILTER_TAGS`,…]] [`--text-redaction-mode`=`TEXT_REDACTION_MODE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a new Cloud Healthcare API dataset containing de-identified data from the source dataset. 
EXAMPLES
     To generate a de-identified version of the dataset 'test-dataset', run the command below. To skip the FHIR stores, omit the --default-fhir-config flag, and to skip DICOM stores, omit the --dicom-filter-tags flag. 
    
    
    gcloud beta healthcare datasets deidentify test-dataset --destination-dataset=projects/{projectId}/locations/us-central1/datasets/test-deid-dataset --default-fhir-config --dicom-filter-tags=MediaStorageSOPClassUID,SeriesInstanceUID,StudyInstanceUID

POSITIONAL ARGUMENTS
    

Dataset resource - Source Cloud Healthcare API dataset to deidentify. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `dataset` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`DATASET`
     ID of the dataset or fully qualified identifier for the dataset. 

To set the `dataset` attribute: 

  * provide the argument `dataset` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Google Cloud location. 

To set the `location` attribute: 

  * provide the argument `dataset` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `healthcare/location`. 


REQUIRED FLAGS
    

`--destination-dataset`=`DESTINATION_DATASET`
     The name of the dataset resource to which the redacted data should be written (e.g., projects/{projectId}/locations/{locationId}/datasets/{datasetId}). The new dataset must not exist, or the request will fail. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--default-fhir-config`
     Deidentify FHIR data with default configurations. 
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
     This command uses the `healthcare/v1beta1` API. The full documentation for this API can be found at: <https://cloud.google.com/healthcare>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud healthcare datasets deidentify](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/datasets/deidentify)
    
    
    [gcloud alpha healthcare datasets deidentify](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/healthcare/datasets/deidentify)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
