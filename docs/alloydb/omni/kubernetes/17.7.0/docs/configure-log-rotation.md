---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/configure-log-rotation/
title: Configure AlloyDB Omni log rotation \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 17.7.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:28:37.418854+00:00
---

# Configure AlloyDB Omni log rotation  |  AlloyDB Omni using the container orchestrator: 17.7.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/configure-log-rotation/

This page documents AlloyDB Omni version **17.7.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/overview)



Send feedback 

#  Configure AlloyDB Omni log rotation Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 17.7.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/configure-log-rotation)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/configure-log-rotation)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/configure-log-rotation)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/configure-log-rotation)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/configure-log-rotation)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/configure-log-rotation)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/configure-log-rotation)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/configure-log-rotation)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/configure-log-rotation)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/configure-log-rotation)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/configure-log-rotation)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/configure-log-rotation)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/configure-log-rotation)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/configure-log-rotation)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/configure-log-rotation)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/configure-log-rotation)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/configure-log-rotation)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/configure-log-rotation)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/configure-log-rotation)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/configure-log-rotation)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/configure-log-rotation)



This document describes how to configure rotation of AlloyDB Omni diagnostic logs when you use the AlloyDB Omni Kubernetes operator.

The following log files are located in the `/obs/diagnostic/` directory:

  * `postgresql.log`: This log file collects PostgreSQL server logs, such as client connections, queries, and administrative notices. These logs are always collected and don't need to be enabled.

  * `postgresql.audit`: This log file collects session and object access audit logs. To collect audit logs, see Manage audit logs with pgAudit.

  * `postgresql.internal`: AlloyDB Omni provides more messages in addition to regular PostgreSQL logs. These messages provide additional technical information that can assist in the debugging of database issues.




## Understand and configure log rotation

Learn how AlloyDB Omni handles log rotation and how to configure rotation thresholds based on file size or duration.

### Log rotation behavior

When a log file rotates, the following occurs:

  1. The existing log file is archived into the `/obs/diagnostic/archive/` directory.

  2. The active log file in `/obs/diagnostic/` is reset so that subsequent log entries begin writing to a clean file.

  3. Log information continues writing to the active log file until the file reaches a size or age threshold, at which point it rotates again. Logs rotate so that active log files don't become too large.




By default, the rotation setting is for each log file to rotate when its size reaches 200 MB. The default rotation doesn't include an age setting.

Archived files are retained for 7 days. Archived files that are older than 7 days are automatically removed, except for the file that was archived during the last rotation. For example, if `log_rotation_age` is older than 7 days, then the archived file reaches the 7-day threshold before the rotation of the current file. In this case, this archived file isn't removed until the next rotation generates a new archived file.

Each rotated log filename follows the format `postgresql-%Y-%m-%d_%H%M%S.EXTENSION.gz`, where `EXTENSION` is `log`, `audit`, or `internal`. The rotation time determines the timestamp in Coordinated Universal Time (UTC). For example, if a log file rotates at 13:01:02 on December 20, 2024 UTC, the archived filename is `postgresql-2024-12-20_130102.log.gz`.

The system compresses each archived file individually by using the `gzip` file format.

### Configure rotation thresholds

In AlloyDB Omni, the database Pod's dedicated `logrotate-agent` container manages log rotation rather than the database engine. Don't enable the PostgreSQL `logging_collector` parameter. The operator sets this parameter to `off` and overrides any value that you configure. To manage your logs, use the log rotation features described in this document. 

To control when logs rotate, configure a maximum file size, a duration between log rotations, or both. The duration between log rotations is also called the age of the log. If you use both settings, then each log rotates when it reaches one of the thresholds.

To configure log rotation, you set one or both of the following parameters in the `parameters` section of the `DBCluster` manifest:

  * `log_rotation_size`: "SIZE_IN_KB"
  * `log_rotation_age`: "AGE_IN_MINUTES"



Replace the following:

  * `SIZE_IN_KB`: the maximum file size, in kilobytes, before logs rotate.
  * `AGE_IN_MINUTES`: the duration between log rotations, in minutes.



  * Specify both the `log_rotation_size` and `log_rotation_age` parameters as integer strings, such as `"400000"` or `"1440"`. Don't include units such as `"400MB"` or `"1d"`.
  * The database Pod's `logrotate-agent` container consumes the `log_rotation_size` and `log_rotation_age` parameters directly and doesn't pass them to the database engine. You can't query or view these parameters from within the database by using `psql` (for example, by running `SHOW log_rotation_size` or querying `pg_settings`).



To disable one of the log rotation settings, set it to zero, `"0"`. To retain the default setting that rotates logs when their file size reaches 200 MB, don't set either parameter.

#### Rotate by log size and duration

The following sample sets logs to rotate when their file size reaches 400 MB or when the time between log rotations reaches one day, whichever happens first:
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: DBCluster
    metadata:
      name: DB_CLUSTER_NAME
    spec:
    ...
      primarySpec:
      ...
        parameters:
          log_rotation_size: "400000" # 400 MB
          log_rotation_age: "1440" # 24 hours * 60 minutes = 1 day
    

Replace `DB_CLUSTER_NAME` with the name of your database cluster.

#### Rotate by log size only

The following sample sets logs to rotate when their file size reaches 400 MB:
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: DBCluster
    metadata:
      name: DB_CLUSTER_NAME
    spec:
    ...
      primarySpec:
      ...
        parameters:
          log_rotation_size: "400000" # 400 MB
          log_rotation_age: "0" # Set to 0 to disable
    

Replace `DB_CLUSTER_NAME` with the name of your database cluster.

#### Rotate by duration only

The following sample sets logs to rotate once every 24 hours:
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: DBCluster
    metadata:
      name: DB_CLUSTER_NAME
    spec:
    ...
      primarySpec:
      ...
        parameters:
          log_rotation_size: "0" # Set to 0 to disable
          log_rotation_age: "1440" # 24 hours * 60 minutes = 1 day
    

Replace `DB_CLUSTER_NAME` with the name of your database cluster.

## Supported PostgreSQL logging parameters

You can configure what information is emitted to `postgresql.log` by setting standard PostgreSQL logging Grand Unified Configuration (GUC) parameters in the `parameters` section of your `DBCluster` manifest:
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: DBCluster
    metadata:
      name: DB_CLUSTER_NAME
    spec:
    ...
      primarySpec:
      ...
        parameters:
          log_min_messages: "warning"
          log_min_duration_statement: "250" # Log queries taking >= 250ms
          log_statement: "ddl" # Log all DDL statements
          log_lock_waits: "on"
          log_checkpoints: "on"
          log_temp_files: "0" # Log all temporary files created
          log_autovacuum_min_duration: "1000" # Log autovacuum runs taking >= 1s
    

Replace `DB_CLUSTER_NAME` with the name of your database cluster.

The following table describes supported PostgreSQL logging parameters based on [Error Reporting and Logging](https://www.postgresql.org/docs/current/runtime-config-logging.html) in the PostgreSQL documentation.

In AlloyDB Omni, the `log_directory` and `log_filename` parameters are unsupported because the operator manages log file paths in `/obs/diagnostic/`. The `logging_collector` parameter must remain `off` because the Pod's `logrotate-agent` container manages log rotation externally. Any parameter or feature that requires enabling the `logging_collector` parameter isn't supported. 

Parameter | Description  
---|---  
`log_min_messages` | Controls which message levels are written to the server log. Valid values are `debug5`, `debug4`, `debug3`, `debug2`, `debug1`, `info`, `notice`, `warning`, `error`, `log`, `fatal`, and `panic`. Each level includes all following severity levels.  
`log_min_error_statement` | Controls which SQL statements that cause an error condition are recorded in the server log. Valid values are `debug5` through `panic`. To disable statement error logging, set to `panic`.  
`log_min_duration_statement` | Logs the duration of each completed statement if the statement ran for at least the specified number of milliseconds. Setting this parameter to `0` logs all statements and durations. Setting it to `-1` disables duration logging.  
`log_min_duration_sample` | Samples completed statements running for at least the specified milliseconds, at the rate set by `log_statement_sample_rate`. Setting it to `-1` disables sampled duration logging.  
`log_statement_sample_rate` | Specifies the fraction of statements exceeding `log_min_duration_sample` that are logged (`0.0` to `1.0`).  
`log_transaction_sample_rate` | Specifies the fraction of transactions whose statements are all logged (`0.0` to `1.0`), regardless of statement execution duration.  
`log_statement` | Controls which SQL statements are logged: `none` (off), `ddl` (all data definition commands), `mod` (DDL plus data-modifying statements such as `INSERT`, `UPDATE`, and `DELETE`), or `all`.  
`log_duration` | Logs the duration of every completed statement. Query text isn't printed unless the `log_min_duration_statement` threshold is also exceeded.  
`log_line_prefix` | Specifies the `printf`-style prefix output at the beginning of each log line (such as `%m` for timestamp, `%p` for process ID, `%u` for user, and `%d` for database).  
`log_connections` | Controls whether client connections to the database are logged.  
`log_disconnections` | Controls whether session terminations and session durations are logged.  
`log_hostname` | Controls whether the connecting client hostname is logged in addition to its IP address.  
`log_error_verbosity` | Controls the detail level in server log messages: `terse`, `default`, or `verbose` (includes SQLSTATE code and source lines).  
`log_lock_waits` | Controls whether a message is logged when a session waits longer than `deadlock_timeout` to acquire a lock.  
`log_checkpoints` | Records checkpoints and restartpoints in the log, including buffer write statistics and timing.  
`log_autovacuum_min_duration` | Logs each action executed by autovacuum if it ran for at least the specified number of milliseconds. Setting this parameter to `0` logs all actions. Setting it to `-1` disables logging.  
`log_temp_files` | Controls logging of temporary file names and sizes in kilobytes when deleted (for sorts, hashes, or query results). Setting this parameter to `0` logs all temporary files. Setting it to `-1` disables logging.  
`log_parameter_max_length` | Trims bind parameter values logged in non-error statement logs to this number of bytes. Setting this parameter to `-1` logs values in full. Setting it to `0` disables parameter logging.  
`log_parameter_max_length_on_error` | Trims bind parameter values reported in error messages to this number of bytes. Setting this parameter to `0` disables parameters in error messages. Setting it to `-1` logs values in full.  
`log_replication_commands` | Controls whether replication commands and replication slot actions are logged.  
`log_recovery_conflict_waits` | Controls whether a message is logged when the startup process waits longer than `deadlock_timeout` for recovery conflicts.  
`log_startup_progress_interval` | Sets the time in milliseconds between progress messages for long-running startup operations. Setting this parameter to `0` disables it.  
`log_timezone` | Sets the time zone used for timestamps in the server log.  
  
## Manage audit logs with pgAudit

To enable session and object access logging, you must configure pgAudit parameters in your database cluster and install the extension in your databases.

### Step 1: Configure pgAudit parameters in the `DBCluster` manifest

To collect session and object access logs in the `postgresql.audit` file, enable pgAudit and configure which statements to log by using the `pgaudit.log` parameter.

Add the following lines to the `parameters` section of the [`v1_dbcluster_parameters.yaml`](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/samples#full-dbcluster) file:
    
    
    alloydb.enable_pgaudit: "on"
    pgaudit.log: "all"
    

Set the `pgaudit.log` parameter to a non-empty value, such as `"all"` or `"write, ddl"`. If you don't set this parameter or if you set it to `"none"`, pgAudit doesn't generate audit logs even when the `alloydb.enable_pgaudit` parameter is set to `"on"`.

The following example shows this configuration in the `DBCluster` manifest:
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: DBCluster
    metadata:
      name: DB_CLUSTER_NAME
    spec:
      databaseVersion: "17.7.0"
      primarySpec:
        ...
        parameters:
          ...
          alloydb.enable_pgaudit: "on"
          pgaudit.log: "all"
    

Replace `DB_CLUSTER_NAME` with the name of your database cluster.

For more information, see `pgaudit` in [Supported database extensions](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/reference/extensions).

### Step 2: Install the pgAudit extension in each database

After you configure the parameters and the database restarts, connect to your database and install the pgAudit extension:
    
    
    CREATE EXTENSION IF NOT EXISTS pgaudit;
    

Run this command in every database where you want to enable audit logging. This command installs the event triggers required for DDL auditing.

### Supported pgAudit parameters

The following table describes key pgAudit parameters that you can configure in the `parameters` section of your `DBCluster` spec. For more information, see the [pgAudit documentation](https://www.pgaudit.org/).

Parameter | Description | Default value  
---|---|---  
`pgaudit.log` | Specifies which classes of statements are logged by session audit logging. Valid values are `none`, `all`, `read`, `write`, `function`, `role`, `ddl`, `misc`, and `misc_set`. | `none`  
`pgaudit.log_catalog` | Specifies that session logging is enabled if all relations in a statement are in `pg_catalog`. Disabling this reduces log noise from database clients. | `on`  
`pgaudit.log_parameter` | Specifies that audit logging includes the parameters passed with the statement. | `off`  
`pgaudit.log_relation` | Specifies whether session audit creates a separate log entry for each relation (such as tables and views) referenced in a `SELECT` or DML statement. | `off`  
`pgaudit.log_rows` | Specifies that audit logging includes the number of rows retrieved or affected by a statement. | `off`  
`pgaudit.log_statement` | Specifies whether logging includes the statement text and parameters. | `on`  
`pgaudit.role` | Specifies the primary role to use for object audit logging. | None   
  
PostgreSQL server logs are always collected in the `postgresql.log` file and don't require enabling pgAudit.

### Retrieve the active audit log path

Use the SQL function `alloydb_audit_current_logfile` to view the path of the audit log file. If auditing is disabled, then the result is `NULL`.
    
    
    SELECT alloydb_audit_current_logfile();
    
     alloydb_audit_current_logfile
    ----------------------------------
     /obs/diagnostic/postgresql.audit
    

## Forward database logs to a centralized sink

AlloyDB Omni writes database server logs (`postgresql.log`), audit logs (`postgresql.audit`), and internal logs (`postgresql.internal`) to the `/obs/diagnostic/` directory on the `obsdisk` volume inside the database container.

To forward these logs to a centralized logging sink (such as Cloud Logging, Datadog, Splunk, or Elasticsearch), you can deploy a sidecar container by using the `Sidecar` Custom Resource (CR).

The sidecar container runs in the same Pod as the database, mounts the log volume (`obsdisk`), and tails the log files to forward them to your logging destination.

### Example: Forward logs by using a Fluent Bit sidecar

The following example demonstrates how to use a Fluent Bit sidecar to tail all AlloyDB Omni log files and write them to standard output. Standard Kubernetes cluster log collectors, such as the Logging agent on Google Kubernetes Engine (GKE), can then collect these logs.

  1. Create a ConfigMap containing the Fluent Bit configuration to tail server, audit, and internal log files:
         
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: fluentbit-config
           namespace: NAMESPACE
         data:
           fluent-bit.conf: |
             [SERVICE]
                 Flush        1
                 Daemon       Off
                 Log_Level    info
         
             [INPUT]
                 Name         tail
                 Path         /obs/diagnostic/postgresql.log,/obs/diagnostic/postgresql.audit,/obs/diagnostic/postgresql.internal
                 Tag          alloydb.*
                 Path_Key     filename
                 DB           /tmp/fluent-bit.db
         
             [OUTPUT]
                 Name         stdout
                 Match        *
         

Replace `NAMESPACE` with the namespace of your database cluster.

  2. Create a `Sidecar` manifest that defines the Fluent Bit container and mounts both the `obsdisk` volume (containing AlloyDB Omni logs) and the ConfigMap volume:
         
         apiVersion: alloydbomni.dbadmin.goog/v1
         kind: Sidecar
         metadata:
           name: logging-forwarder
           namespace: NAMESPACE
         spec:
           additionalVolumes:
           - name: fluentbit-config-volume
             configMap:
               name: fluentbit-config
           sidecars:
           - name: fluent-bit
             image: fluent/fluent-bit:3.0
             command: ["/fluent-bit/bin/fluent-bit"]
             args: ["-c", "/fluent-bit/etc/fluent-bit.conf"]
             volumeMounts:
             - name: obsdisk
               mountPath: /obs
             - name: fluentbit-config-volume
               mountPath: /fluent-bit/etc/
         

Replace `NAMESPACE` with the namespace of your database cluster.

  3. Update your `DBCluster` manifest to reference the sidecar, or patch the cluster by using the following command:
         
         kubectl patch dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME -n NAMESPACE -p '{"spec":{"primarySpec":{"sidecarRef":{"name":"logging-forwarder"}}}}' --type=merge

Replace the following:

     * `DB_CLUSTER_NAME`: the name of your database cluster.
     * `NAMESPACE`: the namespace of your database cluster.

For more information on managing sidecars, see [Configure a sidecar container](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/kubernetes-sidecar-container).




## Query log rotation history with SQL

When log files rotate, the operator stores the archived files in the `/obs/diagnostic/archive/` directory with their rotation timestamps formatted as `postgresql-%Y-%m-%d_%H%M%S.EXTENSION.gz`.

You can query the latest log rotation time directly from the database by using standard PostgreSQL file system functions.

Running the `pg_ls_dir()` function requires superuser privileges (such as `postgres`) or the `pg_read_server_files` predefined role. 

### Inspect rotation timestamps from archived log filenames

To view the most recent log rotations and their parsed UTC rotation timestamps, run the following query:
    
    
    SELECT
      file,
      to_timestamp(
        substring(file from 'postgresql-([0-9]{4}-[0-9]{2}-[0-9]{2}_[0-9]{6})') || '+00',
        'YYYY-MM-DD_HH24MISS+TZH'
      ) AS rotated_at
    FROM pg_ls_dir('/obs/diagnostic/archive') AS file
    WHERE file ~ '^postgresql-[0-9]{4}-[0-9]{2}-[0-9]{2}_[0-9]{6}'
    ORDER BY rotated_at DESC
    LIMIT 5;
    

The output is similar to the following:
    
    
                       file                   |       rotated_at
    ------------------------------------------+------------------------
     postgresql-2026-09-29_171900.internal.gz | 2026-09-29 17:19:00+00
     postgresql-2026-09-29_072800.log.gz      | 2026-09-29 07:28:00+00
     postgresql-2026-09-28_175300.log.gz      | 2026-09-28 17:53:00+00
     postgresql-2026-09-28_093400.log.gz      | 2026-09-28 09:34:00+00
     postgresql-2026-09-28_092000.audit.gz    | 2026-09-28 09:20:00+00
    (5 rows)
    

## What's next

  * [Manage and monitor AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/run-connect)
  * [Generate and diagnose AlloyDB Omni dump files](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/manage-dump-files)
  * [Learn about automatic memory management](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/automatic-memory-management)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
