---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/healthcare/dicom-stores/create/
title: gcloud alpha healthcare dicom-stores create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:29:52.769846+00:00
---

# gcloud alpha healthcare dicom-stores create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/healthcare/dicom-stores/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha healthcare dicom-stores create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha healthcare dicom-stores create - create a Cloud Healthcare API DICOM store 
SYNOPSIS
    

`gcloud alpha healthcare dicom-stores create` (`DICOM_STORE` : `--dataset`=`DATASET` `--location`=`LOCATION`) [`--pubsub-topic`=`PUBSUB_TOPIC`] [`--send-for-bulk-import`] [`--stream-configs`=`STREAM_CONFIGS`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a Cloud Healthcare API DICOM store. 
EXAMPLES
     To create a dicom store called 'test-dicom-store', run: 
    
    
    gcloud alpha healthcare dicom-stores create test-dicom-store --dataset=test-dataset

To create a dicom store with the Cloud Pub/Sub topic 'test-pubsub-topic', run: 
    
    
    gcloud alpha healthcare dicom-stores create test-dicom-store --dataset=test-dataset --pubsub-topic=projects/my-project/topics/test-pubsub-topic

POSITIONAL ARGUMENTS
    

DicomStore resource - Cloud Healthcare API DICOM store to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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


FLAGS
    

`--pubsub-topic`=`PUBSUB_TOPIC`
     Google Cloud Pub/Sub topic to send updates to. 

Note: A topic must be created before publishing or subscribing to it. For instructions on creating topics, refer to: <https://cloud.google.com/pubsub/docs/admin#create_a_topic>

`--send-for-bulk-import`
     Indicates whether or not to send Cloud Pub/Sub notifications on bulk import. Only supported for DICOM imports. 
`--stream-configs`=`STREAM_CONFIGS`
     Configuration that indicates the BigQuery destinations for streaming instances of a DICOM store. To specify StreamConfigs, list all BigQuery destinations into one string separated by comma. (e.g., --stream-configs bq://{bigqueryProjectId1}.{bigqueryDatasetId1}.{bigqueryTableId1},bq://{bigqueryProjectId2}.{bigqueryDatasetId2}.{bigqueryTableId2}). 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `healthcare/v1alpha2` API. The full documentation for this API can be found at: <https://cloud.google.com/healthcare>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud healthcare dicom-stores create](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/create)
    
    
    [gcloud beta healthcare dicom-stores create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/healthcare/dicom-stores/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
