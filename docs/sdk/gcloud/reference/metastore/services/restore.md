---
url: https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/restore/
title: gcloud metastore services restore \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:38:27.080140+00:00
---

# gcloud metastore services restore  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud metastore services restore Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud metastore services restore - restore a Dataproc Metastore service 
SYNOPSIS
    

`gcloud metastore services restore` (`SERVICE` : `--location`=`LOCATION`) (`--backup`=`BACKUP` | `--backup-location`=`BACKUP_LOCATION`) [`--async`] [`--restore-type`=`RESTORE_TYPE`; default="metadata-only"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Restore a Dataproc Metastore service from the given backup or backup-location 

If run asynchronously with `--async`, exits after printing an operation name that can be used to poll the status of the creation via: 
    
    
    gcloud metastore operations describe

EXAMPLES
     To restore a Dataproc Metastore service with the name `my-service` from the backup `my-backup` with a `FULL` restore type, run: 
    
    
    gcloud metastore services restore my-service --backup=my-backup --restore-type=full

To restore a Dataproc Metastore service with the name `my-service` from the backup-location `gs://gcs_bucket` with a `FULL` restore type, run: 
    
    
    gcloud metastore services restore my-service --backup-location=gs://gcs_bucket --restore-type=full

POSITIONAL ARGUMENTS
    

Service resource - Arguments and flags that specify the Dataproc Metastore service you want to restore. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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
    

The backup resource or the location of the backup artifacts to store from. Exactly one of these must be specified: 

`--backup`=`BACKUP`
     The backup resource to restore from. This can be the backup's ID, fully-qualified URL, or relative name in the form `projects/{project_id}/locations/{location_id}/services/{service_id}/backups/{backup_id}`. 
`--backup-location`=`BACKUP_LOCATION`
     The location of the backup artifacts to restore from. This should be a Cloud Storage URI, contains backup avro files under "avro/", backup_metastore.json and service.json, in the form `gs://<path_to_backup>`. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--restore-type`=`RESTORE_TYPE`; default="metadata-only"
     The type of restore to perform. `RESTORE_TYPE` must be one of: 

`full`
     The service's metadata and configuration are restored. 
`metadata-only`
     Only the service's metadata is restored. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `metastore/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/dataproc-metastore/docs>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha metastore services restore](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/metastore/services/restore)
    
    
    [gcloud beta metastore services restore](https://docs.cloud.google.com/sdk/gcloud/reference/beta/metastore/services/restore)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
