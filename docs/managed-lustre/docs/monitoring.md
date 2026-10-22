---
url: https://docs.cloud.google.com/managed-lustre/docs/monitoring/
title: Monitor instances and operations \u00a0|\u00a0 Managed Lustre \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:09.994821+00:00
---

# Monitor instances and operations  |  Managed Lustre  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  Monitor instances and operations Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Monitoring automatically collects and stores information about your Managed Lustre instance.

This document provides a detailed overview of the metrics available for monitoring Managed Lustre on Google Cloud. These metrics help you understand the performance, capacity, and health of your Managed Lustre file systems, so you can identify bottlenecks, troubleshoot issues, and optimize resource utilization.

You can use these metrics in Cloud Monitoring to create custom dashboards, set up alerts, and gain deeper insights into your Managed Lustre instance's behavior.

Cloud Monitoring is automatically enabled for Managed Lustre. There's no charge for the collection of data or to view metrics in the Google Cloud console. API calls may incur charges; see [Cloud Monitoring pricing](https://docs.cloud.google.com/monitoring#section-7) for pricing details.

**Tip:** When no I/O is happening on the file system, performance graphs show the message "No data is available for the selected time frame". Performance metrics are generated only when there is I/O.

## Required IAM roles

The following roles are required:

  * **Monitoring Viewer** (`roles/monitoring.viewer`), or equivalent permissions, to view metrics in Cloud Monitoring.
  * **Monitoring Editor** (`roles/monitoring.editor`), or equivalent permissions, to configure alerts.



Learn how to [grant an IAM role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).

## View metrics

Cloud Monitoring metrics are available from two locations in the Google Cloud console:

  * The Managed Lustre instance details page displays available metrics. In addition to the metrics listed on this page, it computes the bandwidth of bytes copied and the rate of objects copied.

  * The Cloud Monitoring page provides multiple chart options and customizations.




### View metrics on the instance details page

To view a specific instance's metrics:

  1. Go to the **Instances** page in the Google Cloud console.

[Go to Instances](https://console.cloud.google.com/managed-lustre/instances)

  2. Click the instance for which to view metrics. The **Instance details** page appears.

  3. Click the **Monitoring** tab. The default dashboard is displayed.




### View metrics in Cloud Monitoring

To view Managed Lustre metrics in Cloud Monitoring, do the following:

  1. Go to the **Metrics Explorer** page in the Google Cloud console.

[Go to Monitoring: Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer/)

  2. Follow the instructions in [Create charts with Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) to select and display your metrics.




## Set up alerts

You can configure alerting policies in Cloud Monitoring to notify you when your Managed Lustre file system meets specific conditions, such as exceeding storage capacity or throughput limits.

### Prerequisites

To create alerting policies, you must have the **Monitoring Editor** (`roles/monitoring.editor`) IAM role on the project.

### Create an alerting policy

To set up an alert, define a condition using a metric or a PromQL query and configure notification channels.

  1. In the Google Cloud console, go to the **Alerting** page in the Google Cloud console.

[Go to Monitoring: Alerting](https://console.cloud.google.com/monitoring/alerting/)

  2. Click **\+ Create policy**.

  3. Select **Builder** and select your metric, or choose **Code editor** to enter a query with [PromQL](https://docs.cloud.google.com/monitoring/promql). In the metric picker, Managed Lustre metrics fall under the **Lustre instance** and **Lustre location** resources.

  4. Configure your trigger logic and define your [notification channels](https://docs.cloud.google.com/monitoring/support/notification-options) and notification settings.

  5. Click **Create policy**.




For more information about creating triggers and other options, see:

  * [Create metric-threshold alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui)
  * [Create metric-absence alerting policies](https://docs.cloud.google.com/monitoring/alerts/metric-absence)
  * [Create forecasted metric-value alerting policies](https://docs.cloud.google.com/monitoring/alerts/metric-forecast)



### Example: Create a storage capacity alert

The following example demonstrates how to create an alert that triggers when your Managed Lustre instance exceeds 80% of its provisioned capacity.

  1. In the Google Cloud console, go to the **Alerting** page in the Google Cloud console.

[Go to Monitoring: Alerting](https://console.cloud.google.com/monitoring/alerting/)

  2. Click **\+ Create policy**.

  3. Select **Code editor**.

  4. In the **Query Editor** , paste the following PromQL query:
         
         (
           sum by (instance_id, location) (lustre_googleapis_com:instance_capacity_bytes)
           -
           sum by (instance_id, location) (lustre_googleapis_com:instance_available_bytes)
         )
         /
         sum by (instance_id, location) (lustre_googleapis_com:instance_capacity_bytes)
         > 0.8
         

This query calculates the usage ratio across all instances: `(Total - Available) / Total`. The value `0.8` represents the total bytes reaching 80% usage. To alert at 90%, change this value to `0.9`.

  5. Click **Run Query** to verify the syntax and view a chart of the current usage ratio.

  6. Click **Next** and configure the trigger to **Any time series violates**.

  7. Click **Next**. In the **Documentation** section, add recommended actions for resolving the capacity issue. For example:
         
         ## Action Required: Lustre Capacity Warning
         The Managed Lustre instance is exceeding 80% capacity usage.
         
         **Metric:** Usage Ratio > 0.8
         **Severity:** Warning
         
         **Recommended Actions:**
         1. Check the instance details in the Google Cloud console.
         2. Verify if this is expected data growth or a runaway process.
         3. If valid, consider expanding the storage capacity of the instance or deleting old data to free up space.
         4. Failure to address this may result in "No Space Left on Device" errors for client applications.
         




### Create an alerting policy with gcloud

You can create alerting policies using the Google Cloud CLI. Note that you must edit the alert in the Google Cloud console later to enable specific notification channels.

The following example creates an 80% capacity alert using `gcloud`:
    
    
    gcloud monitoring policies create \
      --policy-from-file=/dev/stdin <<EOF
    {
      "displayName": "Lustre High Capacity Usage (>80%)",
      "severity": "WARNING",
      "combiner": "OR",
      "conditions": [
        {
          "displayName": "Capacity Usage Ratio > 0.8",
          "conditionPrometheusQueryLanguage": {
            "query": "(sum by (instance_id, location) (lustre_googleapis_com:instance_capacity_bytes) - sum by (instance_id, location) (lustre_googleapis_com:instance_available_bytes)) / sum by (instance_id, location) (lustre_googleapis_com:instance_capacity_bytes) > 0.8",
            "duration": "300s",
            "evaluationInterval": "60s",
            "alertRule": "AlwaysOn"
          }
        }
      ],
      "documentation": {
        "content": "Action Required: The Managed Lustre instance is exceeding 80% capacity usage. Please verify if storage expansion is required.",
        "mimeType": "text/markdown"
      }
    }
    EOF
    

## Metric details

Managed Lustre metrics are attached to the following monitored resource types:

  * `lustre.googleapis.com/Instance`
  * `lustre.googleapis.com/Job`
  * `lustre.googleapis.com/QuotaEntity`



Data is sampled every 60 seconds. After sampling, data may not be visible for up to 180 seconds.

### Quota metrics

Metrics related to quota.

Quota metrics are attached to the [`lustre.googleapis.com/Location`](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Location) resource. 

Metric | Description | Details  
---|---|---  
`throughput` | The total throughput quota available in a particular zone and VPC network, in GBps. | **Display Name:** Throughput capacity (GBps) per zone and network  
**Metric Kind:** GAUGE  
**Value Type:** INT64  
**Unit:** GBps  
**Labels:**  
`network_name`: The name of the VPC network to which this quota applies.   
`capacity` | The total capacity quota available in a particular zone and VPC network, in GiB. | **Display Name:** Storage capacity (GiB) per zone and network  
**Metric Kind:** GAUGE  
**Value Type:** INT64  
**Unit:** GiB  
**Labels:**  
`network_name`: The name of the VPC network to which this quota applies.   
  
### Storage capacity metrics

Metrics related to the storage space available and provisioned on your Lustre file system.

For metric labels, the value of `target` uses the format `<fsname>-<TYPE><HEXA>` where `<HEXA>` is the zero-based index of the target in hexadecimal. For example, if your file system name is `filesys`, the 43rd OST is `filesys-OST002a`, and the 4th MDT is `filesys-MDT0003`.

Storage capacity metrics are attached to the [`lustre.googleapis.com/Instance`](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Instance) resource. 

Metric | Description | Details  
---|---|---  
`available_bytes` | The number of bytes of storage space for a given Object Storage Target (OST) or Metadata Target (MDT) that is available to non-root users. | **Display Name:** Available bytes  
**Metric Kind:** GAUGE  
**Value Type:** INT64  
**Unit:** bytes  
**Labels:**  
`component`: The target type: `ost`, `mdt`, or `mgt`.  
`target`: The name of the target.  
`capacity_bytes` | The number of bytes provisioned for the given target. The total cluster usable data or metadata space for an instance can be obtained by adding the capacity of all targets for a given type of target. | **Display Name:** Capacity bytes  
**Metric Kind:** GAUGE  
**Value Type:** INT64  
**Unit:** bytes  
**Labels:**  
`component`: The target type: `ost`, `mdt`, or `mgt`.  
`target`: The name of the target.  
`free_bytes` | The number of bytes of storage space for a given OST or MDT that is available to root users. | **Display Name:** Free bytes  
**Metric Kind:** GAUGE  
**Value Type:** INT64  
**Unit:** bytes  
**Labels:**  
`component`: The target type: `ost`, `mdt`, or `mgt`.  
`target`: The name of the target.  
  
### Inode (object) metrics

Metrics related to the number of inodes (objects) available and the maximum capacity.

Inode metrics are attached to the [`lustre.googleapis.com/Instance`](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Instance) resource. 

Metric | Description | Details  
---|---|---  
`inodes_free` | The number of inodes (objects) available on the given target. | **Display Name:** Free inodes  
**Metric Kind:** GAUGE  
**Value Type:** INT64  
**Unit:** inodes  
**Labels:**  
`component`: The target type.  
`target`: The name of the target.  
`inodes_maximum` | The maximum number of inodes (objects) the target can hold. | **Display Name:** Maximum inodes  
**Metric Kind:** GAUGE  
**Value Type:** INT64  
**Unit:** inodes  
**Labels:**  
`component`: The target type.  
`target`: The name of the target.  
  
### I/O performance metrics

Metrics providing insight into data transfer rates and operation latency.

I/O performance metrics are attached to the [`lustre.googleapis.com/Instance`](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Instance) resource. 

Metric | Description | Details  
---|---|---  
`io_time_milliseconds_total` | The number of read or write operations whose latency is within the bucketed latency ranges. | **Display Name:** Operation latency  
**Metric Kind:** CUMULATIVE  
**Value Type:** INT64  
**Unit:** operations  
**Labels:**  
`component`: The target type.  
`operation`: The operation type.  
`size`: The bucketed latency range. For example, 512 includes the count of operations that took between 512 and 1024 milliseconds.  
`target`: The name of the target.   
`read_bytes_total` | The number of data bytes read from the given OST. | **Display Name:** Data read bytes  
**Metric Kind:** CUMULATIVE  
**Value Type:** INT64  
**Unit:** bytes  
**Labels:**  
`component`: The target type: always `ost`.  
`operation`: The operation type: `read`.  
`target`: The name of the target.  
`read_samples_total` | The number of read operations performed on the given OST. | **Display Name:** Data read operations  
**Metric Kind:** CUMULATIVE  
**Value Type:** INT64  
**Unit:** operations  
**Labels:**  
`component`: The target type: always `ost`.  
`operation`: The operation type: `read`.  
`target`: The name of the target.  
`write_bytes_total` | The number of data bytes written to the given OST. | **Display Name:** Data write bytes  
**Metric Kind:** CUMULATIVE  
**Value Type:** INT64  
**Unit:** bytes  
**Labels:**  
`component`: The target type: always `ost`.  
`operation`: The operation type: `write`.  
`target`: The name of the target.  
`write_samples_total` | The number of write operations performed on the given OST. | **Display Name:** Data write operations  
**Metric Kind:** CUMULATIVE  
**Value Type:** INT64  
**Unit:** operations  
**Labels:**  
`component`: The target type: always `ost`.  
`operation`: The operation type: `write`.  
`target`: The name of the target.  
  
### Cache metrics

Metrics providing insight into the performance and utilization of the data caching layer on instances with the [Dynamic tier](https://docs.cloud.google.com/managed-lustre/docs/performance-tiers#dynamic_tier).

Cache metrics are attached to the [`lustre.googleapis.com/Instance`](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Instance) resource. 

Metric | Description | Details  
---|---|---  
`cache/read_hits` | Number of read hits for a specific target. | **Display Name:** Cache read hits  
**Metric Kind:** CUMULATIVE  
**Value Type:** INT64  
**Unit:** 1  
**Labels:**  
`target`: The name of the target.  
`cache/read_misses` | Number of read misses for a specific target. | **Display Name:** Cache read misses  
**Metric Kind:** CUMULATIVE  
**Value Type:** INT64  
**Unit:** 1  
**Labels:**  
`target`: The name of the target.  
  
### Client connection metrics

Metrics specifically for understanding client connectivity.

Client connection metrics are attached to the [`lustre.googleapis.com/Instance`](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Instance) resource. 

Metric | Description | Details  
---|---|---  
`connected_clients` | The number of clients currently connected to the given MDT. | **Display Name:** Connected clients  
**Metric Kind:** GAUGE  
**Value Type:** INT64  
**Unit:** clients  
**Labels:**  
`component`: The target type. This is always `mdt`.  
`target`: The name of the MDT.  
  
### File system quota metrics

File system quota metrics allow you to monitor storage and inode consumption for specific users, groups, and projects. Use these metrics to track current usage against the [soft and hard limits](https://docs.cloud.google.com/managed-lustre/docs/file-system-quotas) configured on your file system.

File system quota metrics are associated with the [`lustre.googleapis.com/QuotaEntity`](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/QuotaEntity) monitored resource.

Metric | Description | Details  
---|---|---  
`used_bytes` | The total number of bytes currently consumed by the user, group, or project. | **Display Name:** Quota used bytes  
**Metric Kind:** GAUGE  
**Value Type:** INT64  
**Unit:** Bytes  
**Labels:**  
`accounting_type`: One of `user`, `group`, or `project`.  
`id`: The numeric ID of the user, group, or project.  
`target`: The name of the Lustre target device.   
`soft_limit_bytes` | The storage consumption threshold that triggers a grace period. If usage remains above this limit after the grace period expires, this becomes an enforced hard limit. | **Display Name:** Quota soft limit bytes  
**Metric Kind:** GAUGE  
**Value Type:** INT64  
**Unit:** Bytes  
**Labels:**  
`accounting_type`: One of `user`, `group`, or `project`.  
`id`: The numeric ID of the user, group, or project.  
`target`: The name of the Lustre target device.  
`hard_limit_bytes` | The maximum storage usage allowed for the user, group, or project. Writes exceeding this limit are denied. | **Display Name:** Quota hard limit bytes  
**Metric Kind:** GAUGE  
**Value Type:** INT64  
**Unit:** Bytes  
**Labels:**  
`accounting_type`: One of `user`, `group`, or `project`.  
`id`: The numeric ID of the user, group, or project.  
`target`: The name of the Lustre target device.  
`used_inodes` | The total number of inodes (file records) currently consumed by the user, group, or project. | **Display Name:** Quota used inodes  
**Metric Kind:** GAUGE  
**Value Type:** INT64  
**Unit:** Count  
**Labels:**  
`accounting_type`: One of `user`, `group`, or `project`.  
`id`: The numeric ID of the user, group, or project.  
`target`: The name of the Lustre target device.  
`soft_limit_inodes` | The inode consumption threshold that triggers a grace period. If usage remains above this limit after the grace period expires, this becomes an enforced hard limit. | **Display Name:** Quota soft limit inodes  
**Metric Kind:** GAUGE  
**Value Type:** INT64  
**Unit:** Count  
**Labels:**  
`accounting_type`: One of `user`, `group`, or `project`.  
`id`: The numeric ID of the user, group, or project.  
`target`: The name of the Lustre target device.  
`hard_limit_inodes` | The maximum number of inodes allowed for the user, group, or project. File creation exceeding this limit is denied. | **Display Name:** Quota hard limit inodes  
**Metric Kind:** GAUGE  
**Value Type:** INT64  
**Unit:** Count  
**Labels:**  
`accounting_type`: One of `user`, `group`, or `project`.  
`id`: The numeric ID of the user, group, or project.  
`target`: The name of the Lustre target device.  
  
### Jobstats metrics

Metrics providing read, write, and metadata statistics per JobID, as configured on the client.

To collect these metrics, use `lctl` to configure the `jobid_var` parameter on your Lustre clients individually. Setting this parameter globally via the Management Server (MGS) is not supported. You can automate this configuration across your clients using [startup scripts](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/linux), or configuration management tools like Chef or Puppet.

To configure the client to report a specific identifier (for example, `procname_uid`), use the [`lctl set_param jobid_var`](https://doc.lustre.org/lustre_manual.xhtml#idm140069637858368) command:
    
    
    lctl set_param jobid_var=procname_uid
    

For more information about how jobstats works or available jobid formats, see [Lustre Jobstats](https://doc.lustre.org/lustre_manual.xhtml#jobstats).

Enabling Jobstats metrics has minimal / no impact on filesystem performance. Statistics are maintained in memory on the server, and the additional network overhead per RPC is negligible.

We recommend using stable identifiers for your JobIDs, such as process names or user IDs. Using unique identifiers for each job, such as random UUIDs, generates high [cardinality](https://docs.cloud.google.com/monitoring/api/v3/metric-model#cardinality), which can slow down queries. In extreme cases, we may pause jobstats collection to ensure stability. To keep query performance within reasonable limits, it is best to have fewer than 1000 unique JobIDs per day.

Avoid including per-client identifiers (like hostname) in the JobID if you intend to track metrics per job across multiple clients. Including hostname will result in per-client metrics rather than aggregated per-job metrics, and can significantly affect metric query performance if you have a large number of clients.

**Caution:** When configuring `jobid_var` on Lustre clients, avoid including information that could be sensitive to your organization, such as process names or the contents of environment variables. Google Support personnel can view information contained in monitoring data.

Jobstats metrics are attached to the [`lustre.googleapis.com/Job`](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Job) resource. 

Metric | Description | Details  
---|---|---  
`read_bytes_total` | The total number of bytes read by the job. |  **Display Name:** Data read bytes by job  
**Metric Kind:** CUMULATIVE  
**Value Type:** INT64  
**Unit:** Bytes  
**Labels:**  
`job_id`: The JobID sent by the client.  
`component`: The target type.  
`target`: The name of the target.  
`instance_id`: The ID of the Managed Lustre instance.   
`write_bytes_total` | The total number of bytes written by the job. |  **Display Name:** Data write bytes by job  
**Metric Kind:** CUMULATIVE  
**Value Type:** INT64  
**Unit:** Bytes  
**Labels:**  
`job_id`: The JobID sent by the client.  
`component`: The target type.  
`target`: The name of the target.  
`instance_id`: The ID of the Managed Lustre instance.   
`metadata_operations_total` | Total metadata operations performed by the job. |  **Display Name:** Metadata operations by job  
**Metric Kind:** CUMULATIVE  
**Value Type:** INT64  
**Unit:** operations  
**Labels:**  
`job_id`: The JobID sent by the client.  
`component`: The target type.  
`target`: The name of the target.  
`instance_id`: The ID of the Managed Lustre instance.   
`read_samples_total` | The total number of read operations performed by the job. |  **Display Name:** Data read operations by job  
**Metric Kind:** CUMULATIVE  
**Value Type:** INT64  
**Unit:** operations  
**Labels:**  
`job_id`: The JobID sent by the client.  
`component`: The target type.  
`target`: The name of the target.  
`instance_id`: The ID of the Managed Lustre instance.   
`write_samples_total` | The total number of write operations performed by the job. |  **Display Name:** Data write operations by job  
**Metric Kind:** CUMULATIVE  
**Value Type:** INT64  
**Unit:** operations  
**Labels:**  
`job_id`: The JobID sent by the client.  
`component`: The target type.  
`target`: The name of the target.  
`instance_id`: The ID of the Managed Lustre instance.   
`read_maximum_size_bytes` | The maximum size in bytes of read operations by the job. |  **Display Name:** Data read maximum size by job  
**Metric Kind:** GAUGE  
**Value Type:** INT64  
**Unit:** Bytes  
**Labels:**  
`job_id`: The JobID sent by the client.  
`component`: The target type.  
`target`: The name of the target.  
`instance_id`: The ID of the Managed Lustre instance.   
`read_minimum_size_bytes` | The minimum size in bytes of read operations by the job. |  **Display Name:** Data read minimum size by job  
**Metric Kind:** GAUGE  
**Value Type:** INT64  
**Unit:** Bytes  
**Labels:**  
`job_id`: The JobID sent by the client.  
`component`: The target type.  
`target`: The name of the target.  
`instance_id`: The ID of the Managed Lustre instance.   
`write_maximum_size_bytes` | The maximum size in bytes of write operations by the job. |  **Display Name:** Data write maximum size by job  
**Metric Kind:** GAUGE  
**Value Type:** INT64  
**Unit:** Bytes  
**Labels:**  
`job_id`: The JobID sent by the client.  
`component`: The target type.  
`target`: The name of the target.  
`instance_id`: The ID of the Managed Lustre instance.   
`write_minimum_size_bytes` | The minimum size in bytes of write operations by the job. |  **Display Name:** Data write minimum size by job  
**Metric Kind:** GAUGE  
**Value Type:** INT64  
**Unit:** Bytes  
**Labels:**  
`job_id`: The JobID sent by the client.  
`component`: The target type.  
`target`: The name of the target.  
`instance_id`: The ID of the Managed Lustre instance.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
