---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/healthcare/hl7v2-stores/export/gcs/
title: gcloud beta healthcare hl7v2-stores export gcs \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:35:40.676591+00:00
---

# gcloud beta healthcare hl7v2-stores export gcs  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/healthcare/hl7v2-stores/export/gcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta healthcare hl7v2-stores export gcs Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta healthcare hl7v2-stores export gcs - export Cloud Healthcare API HL7v2 messages to Google Cloud Storage 
SYNOPSIS
    

`gcloud beta healthcare hl7v2-stores export gcs` (`HL7V2_STORE` : `--dataset`=`DATASET` `--location`=`LOCATION`) `--gcs-uri`=`GCS_URI` [`--async`] [`--end-time`=`END_TIME`] [`--message-view`=`MESSAGE_VIEW`] [`--start-time`=`START_TIME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Export Cloud Healthcare API HL7v2 messages to Google Cloud Storage. 
EXAMPLES
     To export the hl7v2-store 'test-hl7v2-store' to the existing bucket 'testGcsBucket' in the folder 'someFolder', run: 
    
    
    gcloud beta healthcare hl7v2-stores export gcs test-hl7v2-store --gcs-uri=gs://testGcsBucket/someFolder --dataset=test-dataset

To perform the same export, but exporting messages with the message view of 'RAW_ONLY', run: 
    
    
    gcloud beta healthcare hl7v2-stores export gcs test-hl7v2-store --gcs-uri=gs://testGcsBucket/someFolder --dataset=test-dataset --message-view=RAW_ONLY

POSITIONAL ARGUMENTS
    

Hl7v2Store resource - Cloud Healthcare API HL7v2 store to export messages from. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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


REQUIRED FLAGS
    

`--gcs-uri`=`GCS_URI`
     The Cloud Storage destination location. Specify a path to a Cloud Storage bucket or folder rather than a concrete object. The exported messages are ordered by the message send_time (MSH.7) in ascending order. The server will create one or more objects. Each object contains newline delimited JSON, and each line is an HL7v2 message. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--end-time`=`END_TIME`
     The end of the range in message send_time (MSH.7) to process. If not specified, the time when the export is scheduled is used. 
`--message-view`=`MESSAGE_VIEW`
     Specifies the parts of the Message resource to include in the export. The default is FULL. `MESSAGE_VIEW` must be one of: 

`basic`
     Exported resources include only the name field. 
`full`
     Exported resources include all the message fields. 
`parsed-only`
     Exported resources include all the message fields except data and schematizedData fields. 
`raw-only`
     Exported resources include all the message fields except parsedData and schematizedData fields. 
`schematized-only`
     Exported resources include all the message fields except data and parsedData fields. 
`--start-time`=`START_TIME`
     The start of the range in message send_time (MSH.7) to process. If not specified, the UNIX epoch (1970-01-01T00:00:00Z) is used. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `healthcare/v1beta1` API. The full documentation for this API can be found at: <https://cloud.google.com/healthcare>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud healthcare hl7v2-stores export gcs](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/export/gcs)
    
    
    [gcloud alpha healthcare hl7v2-stores export gcs](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/healthcare/hl7v2-stores/export/gcs)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
