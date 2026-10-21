---
url: https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/export/gcs/
title: gcloud metastore services export gcs \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:41:52.869697+00:00
---

# gcloud metastore services export gcs  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/export/gcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud metastore services export gcs Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud metastore services export gcs - export metadata from a Dataproc Metastore service to Google Cloud Storage 
SYNOPSIS
    

`gcloud metastore services export gcs` (`SERVICE` : `--location`=`LOCATION`) `--destination-folder`=`DESTINATION_FOLDER` [`--async`] [`--dump-type`=`DUMP_TYPE`; default="mysql"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Export metadata from a Dataproc Metastore service to Google Cloud Storage. 

If run asynchronously with `--async`, exits after printing the operation name that can be used to poll the status of the export via: 
    
    
    gcloud metastore operations describe

EXAMPLES
     To export metadata from a Dataproc Metastore service with the name `my-metastore-service` in location `us-central1` to the destination folder `gs://my-bucket/destination-folder`, run: 
    
    
    gcloud metastore services export gcs my-metastore-service --location=us-central1 --destination-folder=gs://my-bucket/destination-folder

POSITIONAL ARGUMENTS
    

Service resource - Arguments and flags that specify the Dataproc Metastore service you want to export. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `service` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`SERVICE`
     ID of the service or fully qualified identifier for the service. 

To set the `service` attribute: 

  * provide the argument `service` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the Dataproc Metastore service. 

If not specified, will use `default` metastore/location. To set the `location` attribute: 

  * provide the argument `service` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `metastore/location`. 


REQUIRED FLAGS
    

`--destination-folder`=`DESTINATION_FOLDER`
     A Cloud Storage URI of a folder that metadata is exported to, in the format `gs://<bucket_name>/<path_inside_bukcet>`. A sub-folder containing exported files will be created below it. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--dump-type`=`DUMP_TYPE`; default="mysql"
     The type of the database dump. If unspecified, defaults to `mysql`. `DUMP_TYPE` must be one of: 

`avro`
     Database dump contains AVRO files. 
`mysql`
     Database dump is a MYSQL dump file. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `metastore/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/dataproc-metastore/docs>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha metastore services export gcs](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/metastore/services/export/gcs)
    
    
    [gcloud beta metastore services export gcs](https://docs.cloud.google.com/sdk/gcloud/reference/beta/metastore/services/export/gcs)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
