---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/healthcare/dicom-stores/export/gcs/
title: gcloud beta healthcare dicom-stores export gcs \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:35:36.996465+00:00
---

# gcloud beta healthcare dicom-stores export gcs  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/healthcare/dicom-stores/export/gcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta healthcare dicom-stores export gcs Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta healthcare dicom-stores export gcs - export a Cloud Healthcare API DICOM store to Google Cloud Storage 
SYNOPSIS
    

`gcloud beta healthcare dicom-stores export gcs` (`DICOM_STORE` : `--dataset`=`DATASET` `--location`=`LOCATION`) `--gcs-uri-prefix`=`GCS_URI_PREFIX` [`--async`] [`--filter-config-gcs-uri`=`FILTER_CONFIG_GCS_URI`] [`--mime-type`=`MIME_TYPE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Export a Cloud Healthcare API DICOM store to Google Cloud Storage. 
EXAMPLES
     To export the dicom-store 'test-dicom-store' to the existing bucket 'testGcsBucket' in the folder 'someFolder', with the mime-type 'application/dicom', run: 
    
    
    gcloud beta healthcare dicom-stores export gcs test-dicom-store --gcs-uri-prefix=gs://testGcsBucket/someFolder --mime-type=application/dicom --dataset=test-dataset

POSITIONAL ARGUMENTS
    

DicomStore resource - Cloud Healthcare API DICOM store to export. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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
    

`--gcs-uri-prefix`=`GCS_URI_PREFIX`
     URI for a Google Cloud Storage directory to which result files should be written (for example, `gs://bucket-id/path/to/destination/dir`). If there is no trailing slash, the service will append one when composing the object path. The user is responsible for creating the Google Cloud Storage bucket referenced in `uri_prefix`. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--filter-config-gcs-uri`=`FILTER_CONFIG_GCS_URI`
     Cloud Storage location of the filter configuration file. The FILTER_CONFIG_GCS_URI must be in the format gs://bucket/path/to/object. The filter configuration file must contain a list of resource paths separated by newline characters (\n or \r\n). Each resource path must be in the format "/studies/{studyUID}[/series/{seriesUID}[/instances/{instanceUID}]]" 

Cloud Healthcare API service account must have the roles/storage.objectViewer Cloud IAM role for this Cloud Storage location. 

`--mime-type`=`MIME_TYPE`
     'MIME types supported by DICOM spec. Each file will be written in the following format: `…/{study_id}/{series_id}/{instance_id}[/{frame_number}].{extension}` The frame_number component will exist only for multi-frame instances. Refer to the DICOM conformance statement for permissible MIME types: <https://cloud.google.com/healthcare/docs/dicom#wado-rs> The following extensions will be used for output files: 

  * application/dicom -> .dcm 
  * image/jpeg -> .jpg 
  * image/png -> .png 



If unspecified, the instances will be exported in their original DICOM format.' 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `healthcare/v1beta1` API. The full documentation for this API can be found at: <https://cloud.google.com/healthcare>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud healthcare dicom-stores export gcs](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/export/gcs)
    
    
    [gcloud alpha healthcare dicom-stores export gcs](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/healthcare/dicom-stores/export/gcs)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
