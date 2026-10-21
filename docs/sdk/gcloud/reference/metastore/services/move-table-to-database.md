---
url: https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/move-table-to-database/
title: gcloud metastore services move-table-to-database \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:38:26.891276+00:00
---

# gcloud metastore services move-table-to-database  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/move-table-to-database/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud metastore services move-table-to-database Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud metastore services move-table-to-database - move table to another database 
SYNOPSIS
    

`gcloud metastore services move-table-to-database` (`SERVICE` : `--location`=`LOCATION`) `--destination_db_name`=`DESTINATION_DB_NAME` `--source_db_name`=`SOURCE_DB_NAME` `--table_name`=`TABLE_NAME` [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Move table to another database from a Dataproc Metastore service's underlying metadata store. 

If run asynchronously with `--async`, exits after printing one operation name that can be used to poll the status of the creation via: 
    
    
    gcloud metastore operations describe

EXAMPLES
     To move table to database with the table_name, source_db_name, and destination_db_name in location `us-central`, run: 
    
    
    gcloud metastore services move-table-to-database my-metastore-service --location=us-central1 --table_name=table_name_to_move --source_db_name=database_name_to_move --destination_db_name=destination_database_name

POSITIONAL ARGUMENTS
    

Service resource - Arguments and flags that specify the table and the destination database you want to move to. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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
    

`--destination_db_name`=`DESTINATION_DB_NAME`
     The name of the database where the table should be moved. 
`--source_db_name`=`SOURCE_DB_NAME`
     The name of the database where the table resides. 
`--table_name`=`TABLE_NAME`
     The name of the table to be moved. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `metastore/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/dataproc-metastore/docs>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha metastore services move-table-to-database](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/metastore/services/move-table-to-database)
    
    
    [gcloud beta metastore services move-table-to-database](https://docs.cloud.google.com/sdk/gcloud/reference/beta/metastore/services/move-table-to-database)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
