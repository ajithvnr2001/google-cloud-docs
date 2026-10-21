---
url: https://docs.cloud.google.com/data-fusion/docs/concepts/metrics-overview/
title: Metrics overview \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:35.512757+00:00
---

# Metrics overview  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/concepts/metrics-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Metrics overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the metrics that help you monitor the health and performance of your Cloud Data Fusion instances and pipelines. Use Cloud Monitoring to monitor these metrics. The metrics provide insights into pipeline runs, instance details, API requests, and authorization checks.

The metrics are categorized as either _pipeline metrics_ or _instance metrics_ :

  * **Pipeline metrics** provide data about individual pipeline runs, such as run status, duration, latency, and data throughput.
  * **Instance metrics** provide aggregated information about the pipelines within an instance, including service availability, the number of deployed pipelines, and API request counts.



Filter and aggregate Cloud Data Fusion pipeline and instance metrics in Monitoring using [_metric_ and _monitored-resource_ labels](https://docs.cloud.google.com/monitoring/api/v3/metric-model#generic-label-info). When you [customize your metrics views](https://docs.cloud.google.com/data-fusion/docs/how-to/metrics-views), you can use one or both of these label types.

## Cloud Data Fusion Pipeline monitored-resource labels

Filter and aggregate the metrics with the following _Cloud Data Fusion Pipeline_ monitored-resource labels:

Label name | Description  
---|---  
`resource_container` | The ID of the customer project.  
`org_id` | The ID of the organization that the customer project belongs to.  
`location` | The zone or region where the instance is hosted.  
`edition` | The edition of the Cloud Data Fusion instance.  
`is_private_ip_enabled` | Whether the instance uses an internal IP address.  
`version` | The Cloud Data Fusion data plane version of the instance.  
`instance_id` | The Cloud Data Fusion instance ID.  
`namespace` | The namespace of the pipeline.  
`pipeline_id` | The pipeline ID.  
`run_id` | The run ID for the pipeline.  
  
## Pipeline metric labels

Filter and aggregate the metrics with the following Cloud Data Fusion metric labels in Monitoring:

Name | Metric | Description | Metric labels  
---|---|---|---  
Pipeline run status | `datafusion.googleapis.com/pipeline/v2/runs_completed_count` | The cumulative count of pipelines that have completed a run. | 

  * `complete_state`
  * `previous_state`
  * `program`
  * `provisioner`
  * `cluster_state`
  * `compute_profile_id`
  * `enable_rbac`
  * `private_service_connect_enabled`

  
Pipeline run time | `datafusion.googleapis.com/pipeline/v2/pipeline_duration` | Time taken to complete the pipeline run. | 

  * `complete_state`
  * `program`
  * `provisioner`
  * `cluster_state`
  * `compute_profile_id`
  * `enable_rbac`
  * `private_service_connect_enabled`

  
Pipeline start latency | `datafusion.googleapis.com/pipeline/v2/pipeline_start_latency` | The time taken for the pipeline to reach _Running_ state. | 

  * `program`
  * `provisioner`
  * `cluster_state`
  * `compute_profile_id`
  * `complete_state`
  * `enable_rbac`
  * `private_service_connect_enabled`

  
Provisioning latency | `datafusion.googleapis.com/pipeline/v2/dataproc/provisioning_latency` | The Managed Service for Apache Spark cluster provisioning latency. | 

  * `provisioner`
  * `enable_rbac`
  * `private_service_connect_enabled`

  
Dataproc API requests | `datafusion.googleapis.com/pipeline/v2/dataproc/api_request_count` | The cumulative count of Dataproc API requests. | 

  * `provisioner`
  * `method`
  * `response_code`
  * `region`
  * `launch_mode`
  * `image_version`
  * `enable_rbac`
  * `private_service_connect_enabled`

  
Pipeline preview run time | `datafusion.googleapis.com/pipeline/v2/preview_duration` | Time taken to complete preview. | 

  * `complete_state`
  * `enable_rbac`
  * `private_service_connect_enabled`

  
Pipeline bytes written | `datafusion.googleapis.com/pipeline/v2/write_bytes_count` | The cumulative count of bytes written by a pipeline. | 

  * `enable_rbac`
  * `private_service_connect_enabled`

  
Pipeline bytes read | `datafusion.googleapis.com/pipeline/v2/read_bytes_count` | The cumulative count of bytes read by a pipeline. | 

  * `enable_rbac`
  * `private_service_connect_enabled`

  
Pipeline bytes shuffled | `datafusion.googleapis.com/pipeline/v2/shuffle_bytes_count` | The cumulative count of bytes shuffled in a pipeline. | 

  * `enable_rbac`
  * `private_service_connect_enabled`

  
Plugin records processed in | `datafusion.googleapis.com/pipeline/v2/plugin/incoming_records_count` | Cumulative count of records entering a plugin. | 

  * `enable_rbac`
  * `private_service_connect_enabled`
  * `stage_name`

  
Plugin records processed out | `datafusion.googleapis.com/pipeline/v2/plugin/outgoing_records_count` | The cumulative count of records exiting a plugin.  | 

  * `enable_rbac`
  * `private_service_connect_enabled`
  * `stage_name`

  
  
## Cloud Data Fusion Instance monitored-resource labels

Starting with Cloud Data Fusion version 6.11.1.1, the `InstanceV3` (`datafusion.googleapis.com/InstanceV3`) monitored resource is the default resource type for instance-level metrics. All new instances and instances upgraded to version 6.11.1.1 or later automatically emit metrics and logs using `InstanceV3`. The `InstanceV3` resource structure differs from the previous version by removing the `org_id` and `namespace` labels.

By default, the emission of `InstanceV2` metrics is disabled in Cloud Data Fusion version 6.11.1.1 and later. However, you can re-enable `InstanceV2` emission alongside `InstanceV3` using the Cloud Data Fusion REST API if you require backward compatibility for existing dashboards or queries.

**Note:** Metrics associated with pipeline execution continue to use the `datafusion.googleapis.com/PipelineV2` monitored resource.

You can filter and aggregate the metrics with the following _Cloud Data Fusion Instance_ monitored-resource labels.

### InstanceV3 monitored-resource labels

Label name | Description  
---|---  
`resource_container` | The ID of the customer project.  
`location` | The zone or region where the instance is hosted.  
`edition` | The edition of the instance.  
`is_private_ip_enabled` | Whether the instance uses an internal IP address.  
`version` | The Cloud Data Fusion data plane version of the instance.  
`instance_id` | The Cloud Data Fusion instance ID.  
  
### InstanceV2 monitored-resource labels

Label name | Description  
---|---  
`resource_container` | The ID of the customer project.  
`org_id` | The ID of the organization that the customer project belongs to.  
`location` | The zone or region where the instance is hosted.  
`edition` | The edition of the instance.  
`is_private_ip_enabled` | Whether the instance uses an internal IP address.  
`version` | The Cloud Data Fusion data plane version of the instance.  
`instance_id` | The Cloud Data Fusion instance ID.  
`namespace` | The namespace name.  
  
## Instance metric labels

Filter and aggregate the metrics with the following Cloud Data Fusion metric labels in Monitoring.

### InstanceV3 metric labels

Name | Metric | Description | Metric labels  
---|---|---|---  
Service status | `datafusion.googleapis.com/instance/v3/service_available` | The availability of Cloud Data Fusion services. | 

  * `service`
  * `enable_rbac`
  * `private_service_connect_enabled`

  
Deployed pipeline count | `datafusion.googleapis.com/instance/v3/pipelines` | The number of deployed pipelines. | 

  * `enable_rbac`
  * `private_service_connect_enabled`
  * `maintenance_window_enabled`

  
Concurrent pipelines running count | `datafusion.googleapis.com/instance/v3/concurrent_pipelines_running` | The number of pipelines running concurrently. | 

  * `enable_rbac`
  * `private_service_connect_enabled`

  
Concurrent pipeline launches count | `datafusion.googleapis.com/instance/v3/concurrent_pipelines_launched` | The number of pipelines in either _Provisioning_ or _Starting_ state. | 

  * `enable_rbac`
  * `private_service_connect_enabled`

  
CDAP REST API requests received | `datafusion.googleapis.com/instance/v3/api_request_count` | The cumulative count of REST API requests received by a service in the backend. | 

  * `service`
  * `handler`
  * `method`
  * `enable_rbac`
  * `private_service_connect_enabled`

  
CDAP REST API responses sent | `datafusion.googleapis.com/instance/v3/api_response_count` | The cumulative count of REST API responses sent by a service in the backend. | 

  * `service`
  * `handler`
  * `method`
  * `response_code`
  * `enable_rbac`
  * `private_service_connect_enabled`

  
Authorization check count | `datafusion.googleapis.com/instance/v3/authorization_check_count` | The cumulative count of authorization checks made by the access enforcer. | 

  * `enable_rbac`
  * `type`
  * `private_service_connect_enabled`

  
Authorization check time | `datafusion.googleapis.com/instance/v3/authorization_check_time` | The latency of authorization checks made by the access enforcer. | 

  * `enable_rbac`
  * `type`
  * `private_service_connect_enabled`

  
Draft pipeline count | `datafusion.googleapis.com/instance/v3/draft_pipelines` | The number of draft pipelines. | 

  * `enable_rbac`
  * `private_service_connect_enabled`

  
Namespace count | `datafusion.googleapis.com/instance/v3/namespaces` | The number of namespaces. | 

  * `enable_rbac`
  * `private_service_connect_enabled`

  
  
### InstanceV2 metric labels

Name | Metric | Description | Metric labels  
---|---|---|---  
Service status | `datafusion.googleapis.com/instance/v2/service_available` | The availability of Cloud Data Fusion services. | 

  * `service`
  * `enable_rbac`
  * `private_service_connect_enabled`

  
Deployed pipeline count | `datafusion.googleapis.com/instance/v2/pipelines` | The number of deployed pipelines. | 

  * `enable_rbac`
  * `private_service_connect_enabled`
  * `maintenance_window_enabled`

  
Concurrent pipelines running count | `datafusion.googleapis.com/instance/v2/concurrent_pipelines_running` | The number of pipelines running concurrently. | 

  * `enable_rbac`
  * `private_service_connect_enabled`

  
Concurrent pipeline launches count | `datafusion.googleapis.com/instance/v2/concurrent_pipelines_launched` | The number of pipelines in either _Provisioning_ or _Starting_ state. | 

  * `enable_rbac`
  * `private_service_connect_enabled`

  
CDAP REST API requests received | `datafusion.googleapis.com/instance/v2/api_request_count` | The cumulative count of REST API requests received by a service in the backend. | 

  * `service`
  * `handler`
  * `method`
  * `enable_rbac`
  * `private_service_connect_enabled`

  
CDAP REST API responses sent | `datafusion.googleapis.com/instance/v2/api_response_count` | The cumulative count of REST API responses sent by a service in the backend. | 

  * `service`
  * `handler`
  * `method`
  * `response_code`
  * `enable_rbac`
  * `private_service_connect_enabled`

  
Authorization check count | `datafusion.googleapis.com/instance/v2/authorization_check_count` | The cumulative count of authorization checks made by the access enforcer. | 

  * `enable_rbac`
  * `type`
  * `private_service_connect_enabled`

  
Authorization check time | `datafusion.googleapis.com/instance/v2/authorization_check_time` | The latency of authorization checks made by the access enforcer. | 

  * `enable_rbac`
  * `type`
  * `private_service_connect_enabled`

  
Draft pipeline count | `datafusion.googleapis.com/instance/v2/draft_pipelines` | The number of draft pipelines. | 

  * `enable_rbac`
  * `private_service_connect_enabled`

  
Namespace count | `datafusion.googleapis.com/instance/v2/namespaces` | The number of namespaces. | 

  * `enable_rbac`
  * `private_service_connect_enabled`

  
  
## Manage InstanceV2 metric emission

For Cloud Data Fusion instances running version 6.11.1.1 or later, `InstanceV2` metric emission is disabled by default. If you need to maintain backward compatibility with dashboards or alerts using the old format, you can re-enable `InstanceV2` metrics using the Cloud Data Fusion REST API.

### Enable InstanceV2 metrics

To enable the emission of `InstanceV2` metrics, use the [`instances.patch`](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances/patch) method with `enable_instance_v2_metrics` set to `true`:
    
    
      curl -X PATCH \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      "https://datafusion.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID?updateMask=monitoring_config" \
      --data '{"monitoringConfig": {"enable_instance_v2_metrics": true}}'
    

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID
  * `LOCATION`: the [location](https://cloud.google.com/data-fusion/pricing#supported_regions) of your instance
  * `INSTANCE_ID`: the ID of your Cloud Data Fusion instance



### Disable InstanceV2 metrics

To disable `InstanceV2` metrics and revert to the default behavior (emitting only `InstanceV3` metrics), use the [`instances.patch`](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances/patch) method with `enable_instance_v2_metrics` set to `false`:
    
    
      curl -X PATCH \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      "https://datafusion.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID?updateMask=monitoring_config" \
      --data '{"monitoringConfig": {"enable_instance_v2_metrics": false}}'
    

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID
  * `LOCATION`: the [location](https://cloud.google.com/data-fusion/pricing#supported_regions) of your instance
  * `INSTANCE_ID`: the ID of your Cloud Data Fusion instance



## Migrate Cloud Monitoring queries from InstanceV2 to InstanceV3

Starting with Cloud Data Fusion version 6.11.1.1, the `InstanceV3` (`datafusion.googleapis.com/InstanceV3`) monitored resource is the default resource type for instance-level metrics. If you have existing Monitoring dashboards, charts, or alert policies that target `InstanceV2`, you can update them to use the `InstanceV3` resource type and metric paths.

To migrate your queries, follow these steps:

  1. Change resource type: Update `resource.type` from `datafusion.googleapis.com/InstanceV2` to `datafusion.googleapis.com/InstanceV3`.

  2. Update metric names: Change the metric paths from `.../instance/v2/...` to `.../instance/v3/...`.

  3. Remove labels: Remove any filters or aggregations based on `resource.labels.org_id` or `resource.labels.namespace`, as these labels are not present in `InstanceV3`.




For example, if the following is your existing `InstanceV2` query:
    
    
    fetch datafusion.googleapis.com/InstanceV2
    | metric 'datafusion.googleapis.com/instance/v2/pipelines'
    | filter resource.labels.instance_id == 'my-instance'
    | group_by 1m, [value_pipelines_mean: mean(value.pipelines)]
    | every 1m
    

Update it as follows:
    
    
    fetch datafusion.googleapis.com/InstanceV3
    | metric 'datafusion.googleapis.com/instance/v3/pipelines'
    | filter resource.labels.instance_id == 'my-instance'
    | group_by 1m, [value_pipelines_mean: mean(value.pipelines)]
    | every 1m
    

## What's next

  * Learn more about [viewing Cloud Data Fusion metrics in Monitoring](https://docs.cloud.google.com/data-fusion/docs/how-to/metrics-views).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
