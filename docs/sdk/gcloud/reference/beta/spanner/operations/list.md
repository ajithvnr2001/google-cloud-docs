---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/operations/list/
title: gcloud beta spanner operations list \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:39:44.970133+00:00
---

# gcloud beta spanner operations list  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/operations/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta spanner operations list Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta spanner operations list - list the Cloud Spanner operations 
SYNOPSIS
    

`gcloud beta spanner operations list` (`--instance`=`INSTANCE` | `--instance-config`=`INSTANCE_CONFIG`) [`--backup`=`BACKUP`] [`--database`=`DATABASE`] [`--instance-partition`=`INSTANCE_PARTITION`] [`--type`=`TYPE`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]] [`--uri`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` List the Cloud Spanner operations. 
EXAMPLES
     To list Cloud Spanner instance operations for an instance, run: 
    
    
    gcloud beta spanner operations list --instance=my-instance-id --type=INSTANCE

To list Cloud Spanner backup operations for an instance, run: 
    
    
    gcloud beta spanner operations list --instance=my-instance-id --type=BACKUP

To list Cloud Spanner database operations for an instance, run: 
    
    
    gcloud beta spanner operations list --instance=my-instance-id --type=DATABASE

To list Cloud Spanner database operations for a database, run: 
    
    
    gcloud beta spanner operations list --instance=my-instance-id --database=my-database-id --type=DATABASE

To list Cloud Spanner backup operations for a database, run: 
    
    
    gcloud beta spanner operations list --instance=my-instance-id --database=my-database-id --type=BACKUP

To list Cloud Spanner backup operations for a backup, run: 
    
    
    gcloud beta spanner operations list --instance=my-instance-id --backup=my-backup-id --type=BACKUP

To list instance partition operations for an instance partition, run: 
    
    
    gcloud beta spanner operations list --instance=my-instance-id --instance-partition=my-partition-id --type=INSTANCE_PARTITION

To list instance partition operations for all instance partitions belonging to this instance, run: 
    
    
    gcloud beta spanner operations list --instance=my-instance-id --type=INSTANCE_PARTITION

REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--instance`=`INSTANCE`
     The ID of the instance the operation is executing on. 
`--instance-config`=`INSTANCE_CONFIG`
     The ID of the instance configuration the operation is executing on. 
FLAGS
    

`--backup`=`BACKUP`
     For backup operations, the name of the backup the operations are executing on. 
`--database`=`DATABASE`
     For database operations, the name of the database the operations are executing on. 
`--instance-partition`=`INSTANCE_PARTITION`
     For instance partition operations, the name of the instance partition the operation is executing on. 
`--type`=`TYPE`
     (optional) List only the operations of the given type. `TYPE` must be one of: 

`BACKUP`
     If only the instance is specified (--instance), returns all backup operations associated with backups in the instance. When a backup is specified (--backup), only the backup operations for the given backup are returned. 
`DATABASE`
     If only the instance is specified (--instance), returns all database operations associated with the databases in the instance. When a database is specified (--database), the command would return database operations for the given database. 
`DATABASE_CHANGE_QUORUM`
     Database change quorum operations are returned for all databases in the given instance (--instance only) or only those associated with the given database (--database). 
`DATABASE_CREATE`
     Database create operations are returned for all databases in the given instance (--instance only) or only those associated with the given database (--database) 
`DATABASE_RESTORE`
     Database restore operations are returned for all databases in the given instance (--instance only) or only those associated with the given database (--database) 
`DATABASE_UPDATE_DDL`
     Database update DDL operations are returned for all databases in the given instance (--instance only) or only those associated with the given database (--database) 
`INSTANCE`
     Returns instance operations for the given instance. Note, type=INSTANCE does not work with --database or --backup. 
`INSTANCE_CONFIG_CREATE`
     Instance configuration create operations are returned for the given instance configuration (--instance-config). 
`INSTANCE_CONFIG_UPDATE`
     Instance configuration update operations are returned for the given instance configuration (--instance-config). 
`INSTANCE_PARTITION`
     If only the instance is specified (--instance), returns all instance partition operations associated with instance partitions in the instance. When an instance partition is specified (--instance-partition), only the instance partition operations for the given instance partition are returned. 
LIST COMMAND FLAGS
    

`--filter`=`EXPRESSION`
     Apply a Boolean filter `EXPRESSION` to each resource item to be listed. If the expression evaluates `True`, then that item is listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters). This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--limit`=`LIMIT`
     Maximum number of resources to list. The default is `unlimited`. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--page-size`=`PAGE_SIZE`
     Some services group resource list output into pages. This flag specifies the maximum number of resources per page. The default is determined by the service if it supports paging, otherwise it is `unlimited` (no paging). Paging may be applied before or after `--filter` and `--limit` depending on the service. 
`--sort-by`=[`FIELD`,…]
     Comma-separated list of resource field key names to sort by. The default order is ascending. Prefix a field with ``~´´ for descending order on that field. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--uri`
     Print a list of resource URIs instead of the default output, and change the command output to a list of URIs. If this flag is used with `--format`, the formatting is applied on this URI list. To display URIs alongside other keys instead, use the `uri()` transform. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud spanner operations list](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/operations/list)
    
    
    [gcloud alpha spanner operations list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/operations/list)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
