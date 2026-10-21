---
url: https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/clone/
title: gcloud sql instances clone \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:38.761292+00:00
---

# gcloud sql instances clone  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/clone/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud sql instances clone Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud sql instances clone - clones a Cloud SQL instance 
SYNOPSIS
    

`gcloud sql instances clone` `SOURCE` `DESTINATION` [`--async`] [`--preferred-secondary-zone`=`PREFERRED_SECONDARY_ZONE`] [`--preferred-zone`=`PREFERRED_ZONE`] [`--source-instance-deletion-time`=`SOURCE_INSTANCE_DELETION_TIME`] [`--bin-log-file-name`=`BIN_LOG_FILE_NAME` `--bin-log-position`=`BIN_LOG_POSITION` | [`--point-in-time`=`POINT_IN_TIME` : `--restore-database-name`=`RESTORE_DATABASE_NAME`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud sql instances clone` creates a clone of a Cloud SQL instance. The clone is an independent copy of the source instance with the same data and settings. Source and destination instances must be in the same project. An instance can be cloned from its current state, or from an earlier point in time. 

For MySQL: The binary log coordinates or timestamp (point in time), if specified, act as the point in time the source instance is cloned from. If not specified, the current state of the instance is cloned. 

For PostgreSQL: The point in time, if specified, defines a past state of the instance to clone. If not specified, the current state of the instance is cloned. 

For SQL Server: The point in time, if specified, defines a past state of the instance to clone. If not specified, the current state of the instance is cloned. 

EXAMPLES
     To clone an instance from its current state (most recent binary log coordinates): 
    
    
    gcloud sql instances clone my-source-instance my-cloned-instance

To clone a MySQL instance from an earlier point in time (past binary log coordinates): 
    
    
    gcloud sql instances clone my-source-instance my-cloned-instance --bin-log-file-name mysql-bin.000020 --bin-log-position 170

To clone a MySQL source instance at a specific point in time: 
    
    
    gcloud sql instances clone my-source-instance my-cloned-instance --point-in-time '2012-11-15T16:19:00.094Z'

To clone a PostgreSQL source instance at a specific point in time: 
    
    
    gcloud sql instances clone my-source-instance my-cloned-instance --point-in-time '2012-11-15T16:19:00.094Z'

To clone a SQL Server source instance at a specific point in time: 
    
    
    gcloud sql instances clone my-source-instance my-cloned-instance --point-in-time '2012-11-15T16:19:00.094Z'

To clone a deleted instance, include the name and deletion time of the source instance: 
    
    
    gcloud sql instances clone my-source-instance my-cloned-instance --source-instance-deletion-time '2012-11-15T16:19:00.094Z'

POSITIONAL ARGUMENTS
    

`SOURCE`
     Cloud SQL instance ID of the source. 
`DESTINATION`
     Cloud SQL instance ID of the clone. 
FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--preferred-secondary-zone`=`PREFERRED_SECONDARY_ZONE`
     The preferred secondary zone for the cloned regional instance. If you specify a value for this flag, then the destination instance uses the value as the secondary zone. The secondary zone can't be the same as the primary zone. 
`--preferred-zone`=`PREFERRED_ZONE`
     The preferred zone for the cloned instance. If you specify a value for this flag, then the destination instance uses the value as the primary zone. 
`--source-instance-deletion-time`=`SOURCE_INSTANCE_DELETION_TIME`
     The time the source instance was deleted. This is required if cloning from a deleted instance. 
At most one of these can be specified: 

Binary log coordinates for point-in-time recovery. 
`--bin-log-file-name`=`BIN_LOG_FILE_NAME`
     The name of the binary log file. Enable point-in-time recovery on the source instance to create a binary log file. If specified with <\--bin-log-position> to form a valid binary log coordinate, it defines an earlier point in time to clone a source instance from. For example, mysql-bin.000001. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--bin-log-position`=`BIN_LOG_POSITION`
     Represents the state of an instance at any given point in time inside a binary log file. If specified along with <\--bin-log-file-name> to form a valid binary log coordinate, it defines an earlier point in time to clone a source instance from. For example, 123 (a numeric value). 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--point-in-time`=`POINT_IN_TIME`
     Represents the state of an instance at any given point in time inside a transaction log file. For MySQL, the binary log file is used for transaction logs. For PostgreSQL, the write-ahead log file is used for transaction logs. For SQL Server, the log backup file is used for such purpose. To create a transaction log, enable point-in-time recovery on the source instance. Instance should have transaction logs accumulated up to the point in time they want to restore up to. Uses RFC 3339 format in UTC timezone. If specified, defines a past state of the instance to clone. For example, '2012-11-15T16:19:00.094Z'. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--restore-database-name`=`RESTORE_DATABASE_NAME`
     The name of the database to be restored for a point-in-time restore. If set, the destination instance will only restore the specified database. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha sql instances clone](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/clone)
    
    
    [gcloud beta sql instances clone](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/instances/clone)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
