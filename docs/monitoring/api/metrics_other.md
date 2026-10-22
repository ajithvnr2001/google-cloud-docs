---
url: https://docs.cloud.google.com/monitoring/api/metrics_other/
title: External metrics list \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:22.417071+00:00
---

# External metrics list  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/metrics_other/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  External metrics list Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Monitoring collects the metric types from open-source projects and other external sources listed in this document.

## About the tables of metrics

The tables of metrics provide formatted versions of the publicly available [metric descriptors](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor). This section provides additional information to help you interpret and use these descriptors.

  * For a general explanation of the entries in the tables, including information about values like `DELTA` and `GAUGE`, see [Metric types](https://docs.cloud.google.com/monitoring/api/v3/kinds-and-types).

To chart or monitor metric types with values of type `STRING`, you must use Monitoring Query Language (MQL), and you must convert the value into a numeric value. For information about MQL string-conversion methods, see [`String`](https://docs.cloud.google.com/monitoring/mql/reference#string-group).

  * For information about the units used in the metric lists, see the [`unit` field](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor.FIELDS.unit) in the `MetricDescriptor` reference.

  * For information about statements of the form “Sampled every _x_ seconds” and “After sampling, data is not visible for up to _y_ seconds”, see [Additional information: metadata](https://docs.cloud.google.com/monitoring/api/metrics#metadata).

  * The resource-hierarchy level tells you if the metric is written at the project, organization, or folder level(s). When the level is not specified in the metric descriptor, the metric writes at the project level by default.



  * For pricing information, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing).


  * For information about the meaning of launch stages such as `GA` (General Availability) and `BETA` (Preview), see [Product launch stages](https://cloud.google.com/products#product-launch-stages).



## external.googleapis.com

Metrics sent to Google Cloud projects with a metric type beginning `external.googleapis.com` are known as **external metrics**. The metrics are typically exported by open-source projects and third-party providers. There is presently a limit of 25,000 external metric descriptors per Google Cloud project.

Cloud Monitoring treats external metrics the same as [custom metrics](https://docs.cloud.google.com/monitoring/custom-metrics), with one exception. For external metrics, a **resource_type** of `global` is invalid and results in the metric data being discarded.

External metric descriptors that are created but then not used for at least 24 months are subject to deletion.

**Note:** Until an external metric is used in a project, there is no metric descriptor for it. This is also true of [custom metrics](https://docs.cloud.google.com/monitoring/custom-metrics). Therefore, this document cannot list information about all the possible external metric types. If you use external metrics in your project, you can look at their metric descriptors using the [`metricDescriptors.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/list) or [`metricDescriptors.get`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/get) Monitoring API methods.

### user

`external.googleapis.com/user/` is a valid domain for user-defined metrics. It is functionally identical to `custom.googleapis.com`, although it has some backend optimizations that make queries perform better at scale. If you have many projects with identical metrics in every project, then you should use the `external.googleapis.com/user/` prefix instead of `custom.googleapis.com` for performance reasons.

### vmware/vcenter

Metrics whose names begin `external.googleapis.com/vmware/vcenter/` come from [Google Cloud VMware Engine](https://docs.cloud.google.com/vmware-engine/docs/overview) environments that are running the [standalone GCVE agent](https://docs.cloud.google.com/vmware-engine/docs/environment/howto-cloud-monitoring-standalone) to collect and send metrics to Cloud Monitoring. For a list of metrics that the agent can collect, see [List of collected metrics](https://docs.cloud.google.com/vmware-engine/docs/environment/howto-cloud-monitoring-standalone#list_of_collected_metrics).

### prometheus

Metrics whose names begin `external.googleapis.com/prometheus/` come from [Prometheus](https://prometheus.io/), an open-source monitoring tool often used with Kubernetes. When you configure Prometheus with [Stackdriver Prometheus sidecar (deprecated)](https://github.com/Stackdriver/stackdriver-prometheus-sidecar), metrics exported by Prometheus are converted to Cloud Monitoring metric types with simple [metric descriptors](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor), such as the following:
    
    
    {
      "name": "projects/my-gcp-project/metricDescriptors/external.googleapis.com/prometheus/apiserver_client_certificate_expiration_seconds",
      "metricKind": "CUMULATIVE",
      "valueType": "DISTRIBUTION",
      "description": "Auto-created custom metric.",
      "type": "external.googleapis.com/prometheus/apiserver_client_certificate_expiration_seconds"
    }
    

If you are using the sidecar to ingest Prometheus metrics, then we recommend migrating to [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus).

## Other metrics

Metrics from other domains.

The following list was last generated at 2026-10-14 20:24:33 UTC. For more information about this process, see [ About the lists](https://docs.cloud.google.com/monitoring/api/metrics#generated).

### cloudonefs

Metrics from [Dell PowerScale for Google Cloud](https://docs.cloud.google.com/dell). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `cloudonefs.isiloncloud.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`cluster/operation_count` GA ** _(project)_**   
I/O operations   
`DELTA`, `INT64`, `count`   
**[dell_emc_cloud_onefs_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_dell_emc_cloud_onefs_cluster)** |  _Count of the read/write operations performed on the cluster. Sampled every 60 seconds._   
`type`: Type of operation.   
`cluster/received_bytes_count` GA ** _(project)_**   
Ingress network traffic   
`DELTA`, `INT64`, `By`   
**[dell_emc_cloud_onefs_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_dell_emc_cloud_onefs_cluster)** |  _Total ingress traffic associated to the cluster in bytes. Sampled every 60 seconds._  
`cluster/sent_bytes_count` GA ** _(project)_**   
Egress network traffic   
`DELTA`, `INT64`, `By`   
**[dell_emc_cloud_onefs_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_dell_emc_cloud_onefs_cluster)** |  _Total egress traffic associated to the cluster in bytes. Sampled every 60 seconds._  
`cluster/total_bytes` GA ** _(project)_**   
Storage capacity allocated   
`GAUGE`, `INT64`, `By`   
**[dell_emc_cloud_onefs_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_dell_emc_cloud_onefs_cluster)** |  _Total capacity allocated to the cluster, in bytes. Sampled every 60 seconds._  
`cluster/used_bytes` GA ** _(project)_**   
Storage usage   
`GAUGE`, `INT64`, `By`   
**[dell_emc_cloud_onefs_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_dell_emc_cloud_onefs_cluster)** |  _Total storage space used by the cluster in bytes. Sampled every 60 seconds._  
  
### cloudvolumesgcp-api.netapp.com

Metrics from [NetApp Cloud Volumes](https://cloud.netapp.com/cloud-volumes-service-for-gcp). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `cloudvolumesgcp-api.netapp.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`cloudvolume/inode_allocation` BETA ** _(project)_**   
Volume inode allocation   
`GAUGE`, `INT64`, `1`   
**[cloudvolumesgcp-api.netapp.com/CloudVolume](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudvolumesgcp-api.netapp.com/CloudVolume)** |  _Inodes allocated for the volume (hard cap). Tied to allocated capacity (size) of volume._  
`cloudvolume/inode_usage` BETA ** _(project)_**   
Volume inode usage   
`GAUGE`, `INT64`, `1`   
**[cloudvolumesgcp-api.netapp.com/CloudVolume](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudvolumesgcp-api.netapp.com/CloudVolume)** |  _Number of inodes in use on the volume._  
`cloudvolume/logical_bytes_backed_up` BETA ** _(project)_**   
Logical bytes backed up   
`GAUGE`, `INT64`, `By`   
**[cloudvolumesgcp-api.netapp.com/CloudVolume](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudvolumesgcp-api.netapp.com/CloudVolume)** |  _Logical bytes backed up (baseline and incremental changes)._  
`cloudvolume/operation_count` BETA ** _(project)_**   
Operations count   
`DELTA`, `INT64`, `1`   
**[cloudvolumesgcp-api.netapp.com/CloudVolume](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudvolumesgcp-api.netapp.com/CloudVolume)** |  _Number of operations being performed on the cloud volume by the end users._   
`type`: Type of operation, read, write, or metadata.   
`cloudvolume/read_bytes_count` BETA ** _(project)_**   
Bytes read   
`DELTA`, `INT64`, `By`   
**[cloudvolumesgcp-api.netapp.com/CloudVolume](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudvolumesgcp-api.netapp.com/CloudVolume)** |  _I/O bytes from read operations by the end user._  
`cloudvolume/replication_healthy` BETA ** _(project)_**   
Volume Replication Healthy   
`GAUGE`, `INT64`, `1`   
**[cloudvolumesgcp-api.netapp.com/CloudVolume](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudvolumesgcp-api.netapp.com/CloudVolume)** |  _Values of TRUE for healthy and FALSE for unhealthy replication relationship._  
`cloudvolume/replication_lag_time` BETA ** _(project)_**   
Volume Replication Transfer Lag Time   
`GAUGE`, `INT64`, `sec`   
**[cloudvolumesgcp-api.netapp.com/CloudVolume](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudvolumesgcp-api.netapp.com/CloudVolume)** |  _Elapsed time since the exported snapshot copy (last complete transfer) was created on the destination._  
`cloudvolume/replication_last_transfer_duration` BETA ** _(project)_**   
Volume Replication Last Transfer Duration   
`GAUGE`, `INT64`, `sec`   
**[cloudvolumesgcp-api.netapp.com/CloudVolume](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudvolumesgcp-api.netapp.com/CloudVolume)** |  _Duration of the last transfer job._  
`cloudvolume/replication_last_transfer_size` BETA ** _(project)_**   
Volume Replication Last Transfer Size   
`GAUGE`, `INT64`, `By`   
**[cloudvolumesgcp-api.netapp.com/CloudVolume](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudvolumesgcp-api.netapp.com/CloudVolume)** |  _Size of the last transfer job._  
`cloudvolume/replication_relationship_progress` BETA ** _(project)_**   
Volume Replication Transfer Progress   
`CUMULATIVE`, `INT64`, `By`   
**[cloudvolumesgcp-api.netapp.com/CloudVolume](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudvolumesgcp-api.netapp.com/CloudVolume)** |  _Amount of data transferred thus far for the current job._  
`cloudvolume/replication_relationship_status` BETA ** _(project)_**   
Volume Replication Status   
`GAUGE`, `INT64`, `1`   
**[cloudvolumesgcp-api.netapp.com/CloudVolume](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudvolumesgcp-api.netapp.com/CloudVolume)** |  _Status of replication: TRUE = transferring, FALSE = idle._  
`cloudvolume/replication_total_transfer_bytes` BETA ** _(project)_**   
Volume Replication Total Transfer Bytes   
`CUMULATIVE`, `INT64`, `By`   
**[cloudvolumesgcp-api.netapp.com/CloudVolume](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudvolumesgcp-api.netapp.com/CloudVolume)** |  _Cumulative data transferred for the relationship since it was created._  
`cloudvolume/request_latencies` BETA ** _(project)_**   
Volume IO operation latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[cloudvolumesgcp-api.netapp.com/CloudVolume](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudvolumesgcp-api.netapp.com/CloudVolume)** |  _Distribution of IO operation request latencies, in milliseconds._   
`method`: Type of latency, read or write.   
`cloudvolume/volume_percent_used` BETA ** _(project)_**   
Volume percentage used   
`GAUGE`, `INT64`, `%`   
**[cloudvolumesgcp-api.netapp.com/CloudVolume](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudvolumesgcp-api.netapp.com/CloudVolume)** |  _Percent of volume allocated space used._  
`cloudvolume/volume_size` BETA ** _(project)_**   
Volume space allocation   
`GAUGE`, `INT64`, `By`   
**[cloudvolumesgcp-api.netapp.com/CloudVolume](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudvolumesgcp-api.netapp.com/CloudVolume)** |  _Space allocated to the volume, in bytes. A measure of the actual provisioned size of the volume._  
`cloudvolume/volume_usage` BETA ** _(project)_**   
Volume space usage   
`GAUGE`, `INT64`, `By`   
**[cloudvolumesgcp-api.netapp.com/CloudVolume](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudvolumesgcp-api.netapp.com/CloudVolume)** |  _Space utilized by the volume, in bytes. A measure of the actual size of the volume._   
`type`: Type of usage, logical or snapshot.   
`cloudvolume/write_bytes_count` BETA ** _(project)_**   
Bytes written   
`DELTA`, `INT64`, `By`   
**[cloudvolumesgcp-api.netapp.com/CloudVolume](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudvolumesgcp-api.netapp.com/CloudVolume)** |  _I/O bytes from write operations by the end user._  
`cloudvolumepool/size` BETA ** _(project)_**   
Storage pool space allocation   
`GAUGE`, `INT64`, `By`   
**[cloudvolumesgcp-api.netapp.com/CloudVolumePool](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudvolumesgcp-api.netapp.com/CloudVolumePool)** |  _Space allocated to the pool, in bytes._  
`cloudvolumepool/usage` BETA ** _(project)_**   
Storage pool space usage   
`GAUGE`, `INT64`, `By`   
**[cloudvolumesgcp-api.netapp.com/CloudVolumePool](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudvolumesgcp-api.netapp.com/CloudVolumePool)** |  _Space used by all the volumes in the storage pool, in bytes._  
  
### netapp.com

Metrics from [NetApp](https://netapp.com/).

The "metric type" strings in this table must be prefixed with `netapp.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`cloudvolume/inode_allocation` DEPRECATED ** _(project)_**   
Volume inode allocation   
`GAUGE`, `INT64`, `{inode}`   
**[netapp_cloud_volume](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp_cloud_volume)** |  _Inode allocated for the volume (hard cap). Tied to allocated capacity (size) of volume. Sampled every 300 seconds._  
`cloudvolume/inode_usage` DEPRECATED ** _(project)_**   
Volume inode usage   
`GAUGE`, `INT64`, `{inode}`   
**[netapp_cloud_volume](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp_cloud_volume)** |  _Number of inode in use on the volume. Sampled every 300 seconds._   
`type`: Type of usage, either logical or snapshot.   
`cloudvolume/operation_count` DEPRECATED ** _(project)_**   
Operations count   
`DELTA`, `INT64`, `count`   
**[netapp_cloud_volume](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp_cloud_volume)** |  _Number of operations being performed on the cloud volume by the end users. Sampled every 60 seconds._   
`type`: Type of utilization, either logical or snapshot.   
`cloudvolume/read_bytes_count` DEPRECATED ** _(project)_**   
Bytes read   
`DELTA`, `INT64`, `By`   
**[netapp_cloud_volume](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp_cloud_volume)** |  _I/O bytes from read operations by the end user. Sampled every 60 seconds._  
`cloudvolume/request_latencies` DEPRECATED ** _(project)_**   
Volume IO operation latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[netapp_cloud_volume](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp_cloud_volume)** |  _Distribution of IO operation request latencies, in milliseconds. A measure of responsiveness of the volume. Sampled every 60 seconds._   
`method`: NetApp Cloud Volume IO operation.   
`cloudvolume/volume_size` DEPRECATED ** _(project)_**   
Volume space allocation   
`GAUGE`, `INT64`, `By`   
**[netapp_cloud_volume](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp_cloud_volume)** |  _Space allocated to the volume, in bytes. A measure of the actual provisioned size of the volume. Sampled every 60 seconds._  
`cloudvolume/volume_usage` DEPRECATED ** _(project)_**   
Volume space usage   
`GAUGE`, `INT64`, `By`   
**[netapp_cloud_volume](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp_cloud_volume)** |  _Space utilized by the volume, in bytes. A measure of the actual size of the volume. Sampled every 60 seconds._   
`type`: Type of usage, either logical or snapshot.   
`cloudvolume/write_bytes_count` DEPRECATED ** _(project)_**   
Bytes written   
`DELTA`, `INT64`, `By`   
**[netapp_cloud_volume](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp_cloud_volume)** |  _I/O bytes from write operations by the end user. Sampled every 60 seconds._  
  
Generated at 2026-10-14 20:24:33 UTC.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
