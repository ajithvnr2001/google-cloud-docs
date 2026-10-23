---
url: https://docs.cloud.google.com/sql/docs/mysql/configure-performance-capture/
title: Configure performance capture \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:48.426764+00:00
---

# Configure performance capture  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/configure-performance-capture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Configure performance capture Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

[Performance capture](https://docs.cloud.google.com/sql/docs/mysql/performance-capture) lets you diagnose transient issues with your database by capturing detailed metrics for your instance when performance is degraded. To use performance capture, enable performance capture for your instance and configure the thresholds that trigger the detailed metrics-based snapshots of your Cloud SQL instance.

## Guidelines for configuring performance capture triggers

Keep in mind the following guidelines when you configure triggers for performance capture.

  * The following [performance capture triggers](https://docs.cloud.google.com/sql/docs/mysql/performance-capture#performance_capture_triggers) are disabled by default:

    * High CPU utilization
    * High memory usage
    * Transaction lock waits
    * Semaphore waits
    * History list length

If you configure a threshold for one of these triggers but want to disable the trigger afterwards, then set the threshold value to `0`.

  * To help prevent excessive captures, configure your trigger thresholds based on historical performance data.

We recommend setting your thresholds toward the higher end of your historical range (for example, above your normal daily peak workload).

If a threshold is set too low or too close to your typical workload, the agent might repeatedly trigger captures. This can lead to:

    * **Higher costs and logging overhead** : Unnecessary logs can quickly increase your Cloud Logging costs.
    * **Extended cooldown sleep mode** : If an instance repeatedly violates the same threshold, the [adaptive cooldown backoff mechanism](https://docs.cloud.google.com/sql/docs/mysql/performance-capture#cooldown-period) triggers. This puts performance capture in a **24-hour sleep mode** , which suspends all trigger checks and diagnostics. You risk losing crucial diagnostic data during this sleep mode if an actual critical event occurs.



## Before you begin

Complete the following tasks before you configure performance capture.

### Required roles

To get the permissions that you need to modify an instance and enable performance capture, ask your administrator to grant you the following IAM roles on the project: 

  * [Cloud SQL Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)
  * [Compute Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Enable performance capture

You can enable performance capture when you [create your Cloud SQL instance](https://docs.cloud.google.com/sql/docs/mysql/create-instance) or when you update your existing instance.

To enable performance capture, [enable query insights](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights) for your instance. When you enable query insights, your instance uses the basic configuration of performance capture and the default value for any threshold-based triggers. For optional threshold-based triggers, the triggers are disabled.

To enable query insights and performance capture on an existing instance, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. In the **Customize your instance** section, click **Show configuration options**. 
  4. Expand **Query insights**.
  5. Select the **Enable Query insights** checkbox.
  6. In the **Enable additional features** section, make sure the the **Performance capture** checkbox is selected.
  7. Click **Save**.

**Note:** The Google Cloud console provides only the option to enable or disable performance capture. To configure performance capture trigger or probe configuration parameters, you must use the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) or the Cloud SQL Admin API.

## Configure performance capture

You can configure performance capture, such as define specific trigger thresholds, when you create or edit the instance by using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) or the Cloud SQL Admin API. Modifying the configuration of performance capture or a performance capture trigger threshold doesn't restart the instance or cause the instance to go into maintenance.

The following procedure describes how to edit an existing instance to configure performance capture.

### gcloud

To configure performance capture on an existing Cloud SQL instance, run the following command:
    
    
    gcloud sql instances patch INSTANCE_NAME \
      --performance-capture-config="enabled=true,PROBE_CONFIGURATION,PERFORMANCE_CAPTURE_THRESHOLDS"

For the `performance-capture-config` flag, include `enabled=true`. For the same flag, you can specify optional configurations for PROBE_CONFIGURATION and for PERFORMANCE_CAPTURE_THRESHOLDS.

You can also use the [`gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch) command to modify the threshold configuration values for performance capture on an existing instance.

#### Configure the probing interval and consecutive probes of performance metrics

You can replace PROBE_CONFIGURATION with one or both of the following flag settings. If you don't set the flags, then the monitoring agent uses the default value.

  * `probing-interval-seconds=SECONDS`: an integer between `20` and `86400`. The time interval, in seconds, between metric probes. For example, `30`, `60`, `100`. Default is `30`.
  * `probe-threshold=PROBES`: the number of consecutive times a threshold must be exceeded to trigger a performance capture. Valid range is `1` to `20`. Default is `3`.



#### Configure performance capture thresholds

You can replace PERFORMANCE_CAPTURE_THRESHOLDS with one or more of the following flag settings. If you don't set values for the flags, then the monitoring agent uses the default values for the thresholds. For more detailed information about the triggers set by these flags, see [Performance capture triggers](https://docs.cloud.google.com/sql/docs/mysql/performance-capture#performance-capture-triggers).

  * `running-threads-threshold=THREADS`: for either primary or replica instances, the minimum number of active threads considered to be over the threshold. For example, `10`. Must be greater than or equal to `10`. If not set, then the default is based on the size of the instance. Default is `MIN(600, cpuCount * 20)`.
  * `seconds-behind-source-threshold=SECONDS` : for read replicas, the minimum replication lag, in seconds, considered to be over the threshold. Must be greater than `1`. Default is `900`.
  * `transaction-duration-threshold=SECONDS`: the duration, in seconds, of an uncommitted transaction before the transaction is tracked and included in a performance capture log. For example, `300`. Minimum value is `60`. Default is `3600`. You also have the option to end long-running transactions automatically.
  * `cpu-utilization-threshold-percent=CPU_PERCENTAGE`: the overall CPU usage percentage to exceed consistently. For example, `90`. Minimum value is `10` and the maximum is `99`. Default is `0`, which is disabled.
  * `memory-usage-threshold-percent=MEMORY_PERCENTAGE`: the overall memory usage percentage to exceed consistently. For example, `90`. Minimum value is `10` and the maximum is `99`. Default is `0`, which is disabled.
  * `transaction-lock-wait-threshold-count=TRANSACTION_COUNT`: the threshold for transactions that are allowed to be in a `LOCK WAIT` state. For example, `50`. Minimum value is `10` and the maximum is `10000`. Default is `0`, which is disabled.
  * `semaphore-wait-threshold-count=SEMAPHORE_THREAD_COUNT`: the threshold for the number of threads waiting on InnoDB semaphores from the `SHOW ENGINE INNODB STATUS` command. For example, `20`. Minimum value is `10` and the maximum is `10000`. Default is `0`, which is disabled.
  * `history-list-length-threshold-count=HISTORY_LIST_LENGTH_COUNT`: the threshold for the InnoDB History List Length (HLL) count that's allowed for the database. For example, `100000`. Minimum value is `10000` and the maximum is `10000000`. Default is `0`, which is disabled.



### REST v1

Before using any of the request data, make the following replacements: 

For the `performanceCaptureConfig` field, include the following flag settings. If you don't set values for the flags, then performance capture uses the default values for the thresholds. For more detailed information about the triggers set by these flags, see [Performance capture triggers](https://docs.cloud.google.com/sql/docs/mysql/performance-capture#performance-capture-triggers).

  * PERFORMANCE_CAPTURE_ENABLED: set to `true` to enable performance capture for your instance.
  * PROBING_INTERVAL_SECONDS: an integer between `30` and `86400`. The time interval, in seconds, between metric probes. Default is `30`.
  * PROBE_THRESHOLD: the number of consecutive times a threshold must be exceeded to trigger a performance capture. Valid range is `1` to `20`. Default is `3`.
  * RUNNING_THREADS_THRESHOLD: for primary instances, the minimum number of active threads considered to be over the threshold. For example, `10`. Must be greater than or equal to `10`. If not set, then the default is based on the size of the instance. Default is `MIN(600, cpuCount * 20)`.
  * SECONDS_BEHIND_SOURCE_THRESHOLD: for read replicas, the minimum replication lag, in seconds, considered to be over the threshold. Must be greater than `1`. Default is `900`.
  * TRANSACTION_DURATION_THRESHOLD: the duration, in seconds, of an uncommitted transaction before the transaction is tracked and included in a performance capture log. For example, `300`. Minimum value is `60`. Default is `3600`. If you want to configure the automatic ending of long-running transactions, then you can include additional configuration settings in the `performanceCaptureConfig` field. For more information, see [End long-running transactions automatically](https://docs.cloud.google.com/sql/docs/mysql/configure-performance-capture#end-transactions).
  * CPU_UTILIZATION_THRESHOLD_PERCENT: the overall CPU usage percentage to exceed consistently. For example, `90`. Minimum value is `10` and the maximum is `99`. Default is `0`, which is disabled.
  * MEMORY_USAGE_THRESHOLD_PERCENT: the overall memory usage percentage to exceed consistently. For example, `90`. Minimum value is `10` and the maximum is `99`. Default is `0`, which is disabled.
  * TRANSACTION_LOCK_WAIT_THRESHOLD_COUNT: the threshold for transactions that are allowed to be in a `LOCK WAIT` state. For example, `50`. Minimum value is `10` and the maximum is `10000`. Default is `0`, which is disabled.
  * SEMAPHORE_WAIT_THRESHOLD_COUNT: the threshold for the number of threads waiting on InnoDB semaphores from the `SHOW ENGINE INNODB STATUS` command. For example, `20`. Minimum value is `10` and the maximum is `10000`. Default is `0`, which is disabled.
  * HISTORY_LIST_LENGTH_THRESHOLD_COUNT: the threshold for the InnoDB History List Length (HLL) count that's allowed for the database. For example, `100000`. Minimum value is `10000` and the maximum is `10000000`. Default is `0`, which is disabled.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "performanceCaptureConfig": {
         "enabled": PERFORMANCE_CAPTURE_ENABLED,
         "probingIntervalSeconds": PROBING_INTERVAL_SECONDS,
         "probeThreshold": PROBE_THRESHOLD,
         "runningThreadsThreshold": RUNNING_THREADS_THRESHOLD,
         "secondsBehindSourceThreshold": SECONDS_BEHIND_SOURCE_THRESHOLD,
         "transactionDurationThreshold": TRANSACTION_DURATION_THRESHOLD,
         "cpuUtilizationThresholdPercent": CPU_UTILIZATION_THRESHOLD_PERCENT,
         "memoryUsageThresholdPercent": MEMORY_USAGE_THRESHOLD_PERCENT,
         "transactionLockWaitThresholdCount": TRANSACTION_LOCK_WAIT_THRESHOLD_COUNT,
         "semaphoreWaitThresholdCount": SEMAPHORE_WAIT_THRESHOLD_COUNT,
         "historyListLengthThresholdCount": HISTORY_LIST_LENGTH_THRESHOLD_COUNT
      },
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2025-11-10T22:19:33.735Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

Before using any of the request data, make the following replacements: 

For the `performanceCaptureConfig` field, include the following flag settings. If you don't set values for the flags, then the monitoring agent uses the default values for the thresholds. For more detailed information about the triggers set by these flags, see [Performance capture triggers](https://docs.cloud.google.com/sql/docs/mysql/performance-capture#performance-capture-triggers).

  * PERFORMANCE_CAPTURE_ENABLED: set to `true` to enable performance capture for your instance.
  * PROBING_INTERVAL_SECONDS: an integer between `30` and `86400`. The time interval, in seconds, between metric probes. Default is `30`.
  * PROBE_THRESHOLD: the number of consecutive times a threshold must be exceeded to trigger a performance capture. Valid range is `1` to `20`. Default is `3`.
  * RUNNING_THREADS_THRESHOLD: for primary instances, the minimum number of active threads considered to be over the threshold. For example, `10`. Must be greater than or equal to `10`. If not set, then the default is based on the size of the instance. Default is `MIN(600, cpuCount * 20)`.
  * SECONDS_BEHIND_SOURCE_THRESHOLD: for read replicas, the minimum replication lag, in seconds, considered to be over the threshold. Must be greater than `1`. Default is `900`.
  * TRANSACTION_DURATION_THRESHOLD: the duration, in seconds, of an uncommitted transaction before the transaction is tracked and included in a performance capture log. For example, `300`. Minimum value is `60`. Default is `3600`. If you want to configure the automatic ending of long-running transactions, then you can include additional configuration settings in the `performanceCaptureConfig` field. For more information, see [End long-running transactions automatically](https://docs.cloud.google.com/sql/docs/mysql/configure-performance-capture#end-transactions).
  * CPU_UTILIZATION_THRESHOLD_PERCENT: the overall CPU usage percentage to exceed consistently. For example, `90`. Minimum value is `10` and the maximum is `99`. Default is `0`, which is disabled.
  * MEMORY_USAGE_THRESHOLD_PERCENT: the overall memory usage percentage to exceed consistently. For example, `90`. Minimum value is `10` and the maximum is `99`. Default is `0`, which is disabled.
  * TRANSACTION_LOCK_WAIT_THRESHOLD_COUNT: the threshold for transactions that are allowed to be in a `LOCK WAIT` state. For example, `50`. Minimum value is `10` and the maximum is `10000`. Default is `0`, which is disabled.
  * SEMAPHORE_WAIT_THRESHOLD_COUNT: the threshold for the number of threads waiting on InnoDB semaphores from the `SHOW ENGINE INNODB STATUS` command. For example, `20`. Minimum value is `10` and the maximum is `10000`. Default is `0`, which is disabled.
  * HISTORY_LIST_LENGTH_THRESHOLD_COUNT: the threshold for the InnoDB History List Length (HLL) count that's allowed for the database. For example, `100000`. Minimum value is `10000` and the maximum is `10000000`. Default is `0`, which is disabled.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "performanceCaptureConfig": {
         "enabled": PERFORMANCE_CAPTURE_ENABLED,
         "probingIntervalSeconds": PROBING_INTERVAL_SECONDS,
         "probeThreshold": PROBE_THRESHOLD,
         "runningThreadsThreshold": RUNNING_THREADS_THRESHOLD,
         "secondsBehindSourceThreshold": SECONDS_BEHIND_SOURCE_THRESHOLD,
         "transactionDurationThreshold": TRANSACTION_DURATION_THRESHOLD,
         "cpuUtilizationThresholdPercent": CPU_UTILIZATION_THRESHOLD_PERCENT,
         "memoryUsageThresholdPercent": MEMORY_USAGE_THRESHOLD_PERCENT,
         "transactionLockWaitThresholdCount": TRANSACTION_LOCK_WAIT_THRESHOLD_COUNT,
         "semaphoreWaitThresholdCount": SEMAPHORE_WAIT_THRESHOLD_COUNT,
         "historyListLengthThresholdCount": HISTORY_LIST_LENGTH_THRESHOLD_COUNT
      },
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2025-11-10T22:19:33.735Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## End long-running transactions automatically

You can use performance capture to end any transactions that exceed a predefined duration, which can help you prevent runaway queries that can destabilize your instance.

To configure your Cloud SQL for MySQL database to end long-running transactions automatically, use the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) or the Cloud SQL Admin API.

### gcloud

To enable the automatic ending of long-running transactions, you set the threshold limit for transactions. To configure the automatic ending of transactions, run the following command:
    
    
    gcloud sql instances patch INSTANCE_NAME \
      --performance-capture-config="transaction-kill-threshold-seconds=SECONDS"

Replace the following:

  * INSTANCE_NAME: the name of the instance.
  * SECONDS: the duration limit, in seconds, of when to end the long-running transaction automatically. This limit can't be set to a value less than the value you set for the `transaction-duration-threshold` or `transactionDurationThreshold` trigger.



You can also specify the type of transactions to end automatically (defaults to `READ_ONLY_TRANSACTIONS`) and customize a list of specific transaction users or hosts to exempt. To configure these options, run the following command:
    
    
    gcloud sql instances patch INSTANCE_NAME \
      --performance-capture-config="transaction-kill-threshold-seconds=SECONDS,transaction-kill-type=TRANSACTION_TYPE,transaction-kill-excluded-user-hosts=EXCLUSION_LIST"

Replace the following:

  * TRANSACTION_TYPE: determines the categories of transactions to end. Specify one of following values: 
    * `READ_ONLY_TRANSACTIONS`: ends only read-only or `SELECT` queries. This is the default if `transaction-kill-type` is unspecified.
    * `ALL_TRANSACTIONS`: ends any running query that exceeds the threshold, including queries with write operations. This includes `INSERT`, `UPDATE`, `DELETE`, and other `DDL` statements.
  * EXCLUSION_LIST: a list of strings to exempt. You can provide the entries using a specific database username and host combination, such as `user@host` or as a MySQL-style user account name, which defaults to `user@%`. The list supports the wildcards `%` and `_` for matching in the host portion.



For example, you might run the following command to configure the automatic ending of _all transactions_, including all read and write transactions, but exclude specific known users of long-running transactions.
    
    
    gcloud sql instances patch example-instance \
    --performance-capture-config="transaction-kill-threshold-seconds=600,transaction-kill-type=ALL_TRANSACTIONS,transaction-kill-excluded-user-hosts=report_user@%;backup_user@localhost"
    

### REST v1

Before using any of the request data, make the following replacements: 

  * SECONDS: the duration, in seconds, of the long-running transactions to be ended automatically. This limit can't be set to a value less than the value you set for the `transactionDurationThreshold` field.
  * TRANSACTION_TYPE: determines the categories of transactions to end. Use one of the following values: 
    * `READ_ONLY_TRANSACTIONS`: ends only read-only or `SELECT` queries. This is the default if `transactionKillType` is unspecified.
    * `ALL_TRANSACTIONS`: ends any running query that exceeds the threshold, including queries with write operations. This includes `INSERT`, `UPDATE`, `DELETE`, and other `DDL` statements.
  * EXCLUSION_LIST: a list of strings to exempt. You can provide the entries using a specific database username and host combination, such as `user@host` or as a MySQL-style user account name, which defaults to `user@%`. The list supports the wildcards `%` and `_` for matching in the host portion.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "performanceCaptureConfig": {
        "transactionKillThresholdSeconds": SECONDS,
        "transactionKillType": TRANSACTION_TYPE,
        "transactionKillExcludedUserHosts": [ EXCLUSION_LIST
        ]
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2025-11-10T22:19:33.735Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * SECONDS: the duration, in seconds, of the long-running transactions to be ended automatically. This limit can't be set to a value less than the value you set for the `transactionDurationThreshold` field.
  * TRANSACTION_TYPE: determines the categories of transactions to end. Use one of the following values: 
    * `READ_ONLY_TRANSACTIONS`: ends only read-only or `SELECT` queries. This is the default if `transactionKillType` is unspecified.
    * `ALL_TRANSACTIONS`: ends any running query that exceeds the threshold, including queries with write operations. This includes `INSERT`, `UPDATE`, `DELETE`, and other `DDL` statements.
  * EXCLUSION_LIST: a list of strings to exempt. You can provide the entries using a specific database username and host combination, such as `user@host` or as a MySQL-style user account name, which defaults to `user@%`. The list supports the wildcards `%` and `_` for matching in the host portion.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "performanceCaptureConfig": {
        "transactionKillThresholdSeconds": SECONDS,
        "transactionKillType": TRANSACTION_TYPE,
        "transactionKillExcludedUserHosts": [ EXCLUSION_LIST
        ]
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2025-11-10T22:19:33.735Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## Disable performance capture

To disable performance capture, do the following.

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Edit**.
  4. In the **Customize your instance** section, click **Show configuration options**.
  5. Expand **Query insights**.
  6. In the **Enable additional features** section, clear the **Performance capture** checkbox.
  7. Click **Save**.



### gcloud
    
    
    gcloud sql instances patch INSTANCE_NAME \
      --performance-capture-config="enabled=false"

Replace INSTANCE_NAME with the name of the instance where you want to disable performance capture.

### REST v1

HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "performanceCaptureConfig": {
         "enabled": false
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "INSERT_TIME",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "performanceCaptureConfig": {
         "enabled": false
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2025-11-10T22:19:33.735Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## What's next

  * [View performance capture logs](https://docs.cloud.google.com/sql/docs/mysql/view-performance-capture-logs)
  * [Monitor instances](https://docs.cloud.google.com/sql/docs/mysql/monitor-instance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
