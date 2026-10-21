---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/redis/clusters/update/
title: gcloud alpha redis clusters update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:35:19.125491+00:00
---

# gcloud alpha redis clusters update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/redis/clusters/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha redis clusters update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha redis clusters update - update Memorystore Cluster for Redis instance 
SYNOPSIS
    

`gcloud alpha redis clusters update` (`CLUSTER` : `--region`=`REGION`) [`--acl-policy`=`ACL_POLICY`] [`--aof-append-fsync`=`AOF_APPEND_FSYNC`] [`--async`] [`--auth-mode`=`AUTH_MODE`] [`--automated-backup-mode`=`AUTOMATED_BACKUP_MODE`] [`--automated-backup-start-time`=`AUTOMATED_BACKUP_START_TIME`] [`--automated-backup-ttl`=`AUTOMATED_BACKUP_TTL`] [`--deletion-protection`] [`--maintenance-version`=`MAINTENANCE_VERSION`] [`--node-type`=`NODE_TYPE`] [`--persistence-mode`=`PERSISTENCE_MODE`] [`--rdb-snapshot-period`=`RDB_SNAPSHOT_PERIOD`] [`--rdb-snapshot-start-time`=`RDB_SNAPSHOT_START_TIME`] [`--remove-redis-config`=[`KEY`,…]] [`--replica-count`=`REPLICA_COUNT`] [`--rotate-server-certificate`] [`--shard-count`=`SHARD_COUNT`] [`--simulate-maintenance-event`] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--update-redis-config`=`KEY`=`VALUE`] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`--maintenance-window-any` | `--maintenance-window-day`=`MAINTENANCE_WINDOW_DAY` `--maintenance-window-hour`=`MAINTENANCE_WINDOW_HOUR`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update the metadata and/or configuration parameters of a Redis cluster. 

This command can fail for the following reasons: 

  * The cluster specified does not exist. 
  * The active account does not have permission to update the given cluster. 


EXAMPLES
     To update a Redis cluster with 5 shard and 2 replica, run: 
    
    
    gcloud alpha redis clusters update my-redis-cluster --shard-count=5 --replica-count=2

POSITIONAL ARGUMENTS
    

Cluster resource - Arguments and flags that specify the Memorystore Redis cluster you want to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `cluster` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CLUSTER`
     ID of the cluster or fully qualified identifier for the cluster. 

To set the `cluster` attribute: 

  * provide the argument `cluster` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     The name of the Redis region of the cluster. Overrides the default redis/region property value for this command invocation. To set the `region` attribute: 

  * provide the argument `cluster` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `redis/region`. 


FLAGS
    

`--acl-policy`=`ACL_POLICY`
     The ACL policy to use for the cluster. 
`--aof-append-fsync`=`AOF_APPEND_FSYNC`
     Fsync configuration. `AOF_APPEND_FSYNC` must be one of: 

`always`
     Redis explicitly calls fsync for every write command. 
`everysec`
     (default) Redis explicitly calls fsync every second. 
`no`
     Redis will not explicitly call fsync. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--auth-mode`=`AUTH_MODE`
     Available authorization mode of a Redis cluster. `AUTH_MODE` must be one of: 

`disabled`
     Authorization is disabled for the cluster. 
`token-auth`
     Token based authorization is enabled for the cluster. 
`--automated-backup-mode`=`AUTOMATED_BACKUP_MODE`
     Automated backup mode. `AUTOMATED_BACKUP_MODE` must be one of: 

`disabled`
     (default) Automated backup is disabled. 
`enabled`
     Automated backup is enabled. 
`--automated-backup-start-time`=`AUTOMATED_BACKUP_START_TIME`
     One-hour window when you want automated-backup operations to start. Specify the time in the format HH:00 on a 24-hour cycle in UTC time. 
`--automated-backup-ttl`=`AUTOMATED_BACKUP_TTL`
     Time to live for automated backups. A backup will be deleted automatically after the TTL is reached. It ranges from 1 day to 365 days. For example, "10d" for 10 days. If not specified, the default value is 35 days. 
`--deletion-protection`
     Enable deletion protection for the Redis Cluster. Use `--deletion-protection`/`--no-deletion-protection` to enable/disable it. 
`--maintenance-version`=`MAINTENANCE_VERSION`
     The maintenance version of the cluster. 
`--node-type`=`NODE_TYPE`
     Node Type of the redis cluster Node. `NODE_TYPE` must be one of: `redis-highcpu-medium`, `redis-highmem-2xlarge`, `redis-highmem-medium`, `redis-highmem-xlarge`, `redis-shared-core-nano`, `redis-standard-large`, `redis-standard-small`. 
`--persistence-mode`=`PERSISTENCE_MODE`
     Operation mode for persistence. `PERSISTENCE_MODE` must be one of: 

`aof`
     AOF-based persistence 
`disabled`
     Persistence mode is disabled 
`rdb`
     RDB-based persistence 
`--rdb-snapshot-period`=`RDB_SNAPSHOT_PERIOD`
     Attempted period between RDB snapshots. `RDB_SNAPSHOT_PERIOD` must be one of: 

`12h`
     12 hours 
`1h`
     1 hour 
`24h`
     (default) 24 hours 
`6h`
     6 hours 
`--rdb-snapshot-start-time`=`RDB_SNAPSHOT_START_TIME`
     Date and time of the first snapshot in the ISO 1801 format, and alignment time for future snapshots. For example, 2024-01-01T01:00:00Z. If not specified, the current time will be used. 
`--remove-redis-config`=[`KEY`,…]
     A list of Redis Cluster config parameters to remove. Removing a non-existent config parameter is silently ignored. 
`--replica-count`=`REPLICA_COUNT`
     The replica count of each shard. 
`--rotate-server-certificate`
     Rotate the server certificates for the cluster. This is allowed only for clusters using a customer-managed CA. 
`--shard-count`=`SHARD_COUNT`
     The shard count of the cluster. 
`--simulate-maintenance-event`
     Trigger a simulation for maintenance event. 
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--update-redis-config`=`KEY`=`VALUE`
     A list of Redis Cluster config KEY=VALUE pairs to update. If a config parameter is already set, its value is modified; otherwise a new Redis config parameter is added. 
At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud alpha redis clusters update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud alpha redis clusters update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
At most one of these can be specified: 

`--maintenance-window-any`
     Removes the user-specified maintenance window. 
Or at least one of these can be specified: 

`--maintenance-window-day`=`MAINTENANCE_WINDOW_DAY`
     The day of week when the window starts, e.g. `sunday`. `MAINTENANCE_WINDOW_DAY` must be one of: `friday`, `monday`, `saturday`, `sunday`, `thursday`, `tuesday`, `wednesday`. 
`--maintenance-window-hour`=`MAINTENANCE_WINDOW_HOUR`
     Hour of day (`0` to `23`) for the start of maintenance window, in UTC time zone. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `redis/v1alpha1` API. The full documentation for this API can be found at: <https://cloud.google.com/memorystore/docs/redis/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud redis clusters update](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/update)
    
    
    [gcloud beta redis clusters update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/redis/clusters/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
