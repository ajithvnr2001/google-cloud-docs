---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/metastore/services/import/gcs/
title: gcloud beta metastore services import gcs \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:18:59.320924+00:00
---

# gcloud beta metastore services import gcs  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/metastore/services/import/gcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta metastore services import gcs Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta metastore services import gcs - import metadata into a Dataproc Metastore service from Google Cloud Storage 
SYNOPSIS
    

`gcloud beta metastore services import gcs` (`SERVICE` : `--location`=`LOCATION`) `--database-dump`=`DATABASE_DUMP` `--import-id`=`IMPORT_ID` [`--async`] [`--description`=`DESCRIPTION`] [`--dump-type`=`DUMP_TYPE`; default="mysql"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Import metadata into a Dataproc Metastore service from Google Cloud Storage. 

If run asynchronously with `--async`, exits after printing the operation name that can be used to poll the status of the export via: 
    
    
    gcloud metastore operations describe

EXAMPLES
     To import metadata with the name `my-import` and description `testing description` into service `my-service` from a database dump with uri `gs://database-dump` and database type `mysql`, run: 
    
    
    gcloud beta metastore services import gcs my-service --import-id=my-import --description='testing description' --dump-type=mysql --database-dump=gs://database-dump

POSITIONAL ARGUMENTS
    

Service resource - Arguments and flags that specify the Dataproc Metastore service you want to import. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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
    

`--database-dump`=`DATABASE_DUMP`
     A Cloud Storage object URI that specifies a database dump from which to import metadata. It must begin with `gs://`. 
`--import-id`=`IMPORT_ID`
     The ID of this metadata import. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     The description of this metadata import. 
`--dump-type`=`DUMP_TYPE`; default="mysql"
     The type of the database dump;. If unspecified, defaults to `mysql`. `DUMP_TYPE` must be one of: 

`avro`
     Database dump contains AVRO files. 
`mysql`
     Database dump is a MYSQL dump file. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `metastore/v1beta` API. The full documentation for this API can be found at: <https://cloud.google.com/dataproc-metastore/docs>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud metastore services import gcs](https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/import/gcs)
    
    
    [gcloud alpha metastore services import gcs](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/metastore/services/import/gcs)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
