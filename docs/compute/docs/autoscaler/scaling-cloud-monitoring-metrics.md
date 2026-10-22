---
url: https://docs.cloud.google.com/compute/docs/autoscaler/scaling-cloud-monitoring-metrics/
title: Scale based on Monitoring metrics \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:33.141873+00:00
---

# Scale based on Monitoring metrics  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/autoscaler/scaling-cloud-monitoring-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Scale based on Monitoring metrics Stay organized with collections  Save and categorize content based on your preferences. 

Autoscaling based on [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) metrics lets you adjust the capacity needed according to measurements from your app. When you autoscale a MIG based on a metric, the autoscaler creates VMs when the metric value increases and deletes VMs when the value decreases.

For example, you can define how many VMs you need per user count, latency, or the number of messages in a Pub/Sub subscription. You can use either the [built-in metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp) provided by the Monitoring service, or the [custom metrics](https://docs.cloud.google.com/monitoring/custom-metrics) that you export from your application.

This document describes how to autoscale a [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) based on Monitoring metrics.

You can also autoscale a MIG based on [CPU utilization](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-cpu), [load balancing serving capacity](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-load-balancing), or [schedules](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-schedules).

## Before you begin

  * Read about autoscaler [fundamentals](https://docs.cloud.google.com/compute/docs/autoscaler#fundamentals).
  * Read about Monitoring metrics concepts used in an autoscaling configuration.
  * If you want to autoscale based on an [Ops Agent metric](https://docs.cloud.google.com/monitoring/api/metrics_opsagent), install the [Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent).
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Limitations

Scaling based on Monitoring metrics is restricted by the [limitations for all autoscalers](https://docs.cloud.google.com/compute/docs/autoscaler#specifications) as well as by the following limitations:

  * You can configure autoscaling based on up to 5 Monitoring metrics per MIG.
  * You can autoscale based on metrics that have `INT64` or `DOUBLE` value types only. Other [value types](https://docs.cloud.google.com/monitoring/api/v3/kinds-and-types#value-types) are not supported.
  * You cannot configure the same metric more than once in an autoscaling policy.



## Configure autoscaling based on Monitoring metrics

You can use a Monitoring metric value for autoscaling in two different ways:

  * **Utilization target** : If you want the autoscaler to maintain a metric at a specific value, configure a _utilization target_. The autoscaler creates VMs when the metric value is above the target and deletes VMs when the metric value is below the target. This is useful for metrics like network traffic, memory or disk usage, or average latency of your application. The following diagram shows how an autoscaler adds and removes VMs in response to a metric value to maintain a utilization target.

![Autoscaler adding and removing VMs to maintain a utilization target.](https://docs.cloud.google.com/static/compute/images/autoscaler/global-metrics-utilization-target.svg)

  * **Single instance assignment** : If you want to autoscale based on how much work is available to assign to each VM, configure a _single instance assignment_. The single instance assignment that you specify represents how much work you expect each VM to handle. The autoscaler divides the metric value by the single instance assignment value to calculate how many VMs are needed. For example, if the metric is equal to 100 and the single instance assignment is 5, then the autoscaler creates 20 VMs in the MIG. This is useful for metrics that reflect the amount of work like Pub/Sub queue length or batch jobs count. Single instance assignment does not apply to metrics that come from each VM. The following diagram shows the proportional relationship between the metric value and the number of VMs when scaling with single instance assignment.

![The proportional relationship between metric value and number of instances.](https://docs.cloud.google.com/static/compute/images/autoscaler/global-metrics-instance-assignment.svg)




### Autoscale to maintain a metric at a target value

When you want to maintain a metric at a target value, specify a utilization target. The autoscaler creates VMs when the metric value is above the target and deletes VMs when the metric value is below the target.

  * If the metric comes from each VM in your MIG, then the autoscaler takes the average metric value across all VMs in the MIG and compares it with the utilization target. For example, if you want to autoscale using the [`tcp_connections` metric](https://docs.cloud.google.com/monitoring/api/metrics_agent#agent-network) that gives the number of TCP connections on a VM, then the autoscaler takes an average number of TCP connections across all VMs in the MIG to compare with the target. When you use such metrics that originate from a VM, the MIG cannot scale in to zero because the autoscaler requires at least one VM to publish a metric value.

  * If the metric applies to the whole MIG and does not come from the VMs in your MIG, then the autoscaler compares the metric value with the utilization target. For example, you can use a [custom metric](https://docs.cloud.google.com/monitoring/custom-metrics) that measures the latency of your application. When you use such metrics that apply to the whole MIG, the MIG can scale in to zero instances , provided that you set the minimum number of instances to `0` and the [necessary conditions](https://docs.cloud.google.com/compute/docs/autoscaler/understanding-autoscaler-decisions#scale-in-to-zero) are met.




When your metric has multiple values, apply a filter to autoscale using an individual value from the metric. For more details about metric filters and other fields that you can use in your configuration, see Monitoring metrics concepts.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.autoscalers.create` on the project
  * `compute.instanceGroupManagers.use` on the project



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. If you don't have a managed instance group, [create one](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances). Otherwise, click the name of a MIG from the list to open that instance group page.

  3. Click **Edit**. 

  4. Click **Group size & autoscaling** to expand the section.

  5. If autoscaling configuration doesn't exist, click **Configure autoscaling**. 

By default, the autoscaling configuration adds a signal based on **CPU utilization**. If you don't require this signal, you can edit it to change the signal type.

  6. In the **Autoscaling signals** section, if a signal for a Monitoring metric exists, you can click to edit it, or click **Add a signal** to add one.
  7. Set the **Signal type** to **Cloud Monitoring metric**.

  8. Click **Configure**. In the **Resource and metric** pane that opens, do the following:

     1. Click **Select a metric**. 
        1. Select the metric that you want to use for autoscaling. You can filter the metrics based on any keywords—for example, memory, bytes, disk.
        2. Click **Apply**. The pane displays a chart that shows the data from the selected metric.
     2. If you want to use specific data from the metric, add a filter based on labels as follows:

        1. In the **Filters** section, click **Add a filter**.
        2. Select a **Label** and enter a **Value**.
        3. Click **Done**. The chart refreshes to show you the filtered value of the metric.
**Note:** The filter `project_id=PROJECT_ID` is added by default because you can use the metric values from the resources in the current project only. If you selected a metric that comes from each VM (`gce_instance`), then an additional filter `instance_group=MIG_NAME` is also added because you can autoscale based on the metric values from the VMs in the current MIG only.
     3. To view the aggregated value of metric that will be used to autoscale your MIG, toggle the **Show aggregation in chart** button. The chart refreshes to show the aggregated value.

     4. In the **Metric target options for autoscaling** section, select **Utilization target**.

     5. Provide the following:

        1. **Utilization target** : Specify the value that the autoscaler must maintain. This must be a positive number. For example, both 24.5 and 100 are acceptable values.
        2. **Utilization target type** : Select a target type that corresponds to the metric's kind of measurement. For accurate comparisons, if the utilization target is measured per seconds, then use **Delta / second** as the target type. Likewise, use **Delta / min** for a utilization target measured per minutes. 
           * **Gauge** : The autoscaler calculates the average value of the data collected in the last couple of minutes and compares that to the utilization target.
           * **Delta / min** : The autoscaler calculates the average rate of growth per minute and compares that to the utilization target.
           * **Delta / second** : The autoscaler calculates the average rate of growth per second and compares that to the utilization target.
     6. When you've finished configuring the metric, click **Select**.

  9. Review the metric details and click **Done**.

  10. To complete the configuration, click **Save**.




###  gcloud 

To configure autoscaling based on Monitoring metrics, use the [`set-autoscaling` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-autoscaling).

**Note:** If autoscaling is already enabled for a MIG, the [`set-autoscaling` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-autoscaling) overwrites the existing autoscaler to the new specifications.

Use the following command to autoscale based on a Monitoring metric with a utilization target.
    
    
    gcloud compute instance-groups managed set-autoscaling MIG_NAME \
      --max-num-replicas=MAX_INSTANCES \
      --min-num-replicas=MIN_INSTANCES \
      --update-stackdriver-metric=METRIC_URL \
      --stackdriver-metric-utilization-target=TARGET_VALUE \
      --stackdriver-metric-utilization-target-type=TARGET_TYPE
    

If your metric has multiple values and you want to use an individual value for autoscaling, then use the `--stackdriver-metric-filter` flag as given in the following command.
    
    
    gcloud compute instance-groups managed set-autoscaling MIG_NAME \
      --max-num-replicas=MAX_INSTANCES \
      --min-num-replicas=MIN_INSTANCES \
      --update-stackdriver-metric=METRIC_URL \
      --stackdriver-metric-utilization-target=TARGET_VALUE \
      --stackdriver-metric-utilization-target-type=TARGET_TYPE \
      **--stackdriver-metric-filter=" METRIC_FILTER"**
    

Replace the following:

  * `MIG_NAME`: the MIG in which you want to add an autoscaler.
  * `MAX_INSTANCES`: the maximum number of VMs that the MIG can have.
  * `MIN_INSTANCES`: the minimum number of VMs that the MIG needs to have.
  * `METRIC_URL`: a protocol-free URL of a Monitoring metric. For example, `compute.googleapis.com/instance/uptime`. If you use a custom metric, it must meet the custom metric requirements.
  * `TARGET_VALUE`: the metric value that the autoscaler attempts to maintain.
  * `TARGET_TYPE`: the value type for the metric. 
    * `gauge` the autoscaler computes the average value of the data collected in the last couple of minutes and compares that to the utilization target.
    * `delta-per-minute` the autoscaler calculates the average rate of growth per minute and compares that to the utilization target.
    * `delta-per-second` the autoscaler calculates the average rate of growth per second and compares that to the utilization target. For accurate comparisons, if you set the utilization target in seconds, use `delta-per-second` as the target type. Likewise, use `delta-per-minute` for a utilization target in minutes.
  * `METRIC_FILTER`: apply a filter to use an individual value from a metric having multiple values and to specify the monitored resource type. If you use a metric that comes from each VM, you don't have to specify the monitored resource type because [`gce_instance`](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance) is used as default. For other metrics, use `resource.type` in the filter expression to specify the monitored resource. To learn more about metric filter, see Monitoring metrics concepts.



To see a full list of available commands and flags for the gcloud CLI, see the [`gcloud` reference](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed).

###  REST 

**Note:** Although autoscaling is a feature of managed instance groups, it is a separate API resource. Keep that in mind when you construct API requests for autoscaling.

To configure autoscaling based on Monitoring metrics for a zonal MIG, use the [`autoscalers`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/autoscalers) resource or, for a regional MIG, use the [`regionAutoscalers`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers) resource.

Make the following call to autoscale a zonal MIG based on a Monitoring metric with a utilization target.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/autoscalers
    {
     "name": "AUTOSCALER_NAME",
     "target": "zones/ZONE/instanceGroupManagers/MIG_NAME",
     "autoscalingPolicy": {
      "maxNumReplicas": MAX_INSTANCES,
      "minNumReplicas": MIN_INSTANCES,
      "customMetricUtilizations": [
        {
          "metric": "METRIC_URL",
          "utilizationTarget": TARGET_VALUE,
          "utilizationTargetType": TARGET_TYPE
        }
      ],
     }
    }
    

If your metric has multiple values and you want to use an individual value for autoscaling, then use the `filter` parameter as given in the following API call.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/autoscalers
    {
     "name": "AUTOSCALER_NAME",
     "target": "zones/ZONE/instanceGroupManagers/MIG_NAME",
     "autoscalingPolicy": {
      "maxNumReplicas": MAX_INSTANCES,
      "minNumReplicas": MIN_INSTANCES,
      "customMetricUtilizations": [
        {
          "metric": "METRIC_URL",
          "utilizationTarget": TARGET_VALUE,
          "utilizationTargetType": TARGET_TYPE,
          **"filter": " METRIC_FILTER"**
        }
      ],
     }
    }
    

Replace the following:

  * `PROJECT_ID`: your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `ZONE`: the zone where the MIG is located.
  * `AUTOSCALER_NAME`: the name of the autoscaler.
  * `MIG_NAME`: the MIG in which you want to add an autoscaler.
  * `MAX_INSTANCES`: the maximum number of VMs that the MIG can have.
  * `MIN_INSTANCES`: the minimum number of VMs that the MIG needs to have.
  * `METRIC_URL`: a protocol-free URL of a Monitoring metric. For example, `compute.googleapis.com/instance/uptime`. If you use a custom metric, it must meet the custom metric requirements.
  * `TARGET_VALUE`: the metric value that the autoscaler attempts to maintain.
  * `TARGET_TYPE`: the value type for the metric. 
    * `GAUGE`: The autoscaler computes the average value of the data collected in the last couple of minutes and compares that to the utilization target.
    * `DELTA_PER_MINUTE` The autoscaler calculates the average rate of growth per minute and compares that to the utilization target.
    * `DELTA_PER_SECOND` The autoscaler calculates the average rate of growth per second and compares that to the utilization target. For accurate comparisons, if you set the utilization target in seconds, use `DELTA_PER_SECOND` as the target type. Likewise, use `DELTA_PER_MINUTE` for a utilization target in minutes.
  * `METRIC_FILTER`: apply a filter to use an individual value from a metric with multiple values and to specify the monitored resource type. If you use a metric that comes from each VM, you don't have to specify the monitored resource type because [`gce_instance`](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance) is used as default. For other metrics, you must specify the monitored resource using `resource.type` selector. To learn more about metric filter, see Monitoring metrics concepts.



### Autoscale based on work available for each VM in a MIG

When you want to autoscale based on the quantity of work that is available for each VM in a MIG, specify a single instance assignment. The value of the single instance assignment that you set indicates how much work you expect each VM to handle. The autoscaler divides the metric value by the single instance assignment value to calculate how many VMs are needed.

A metric value of `0` indicates that there is no work for your MIG to complete. If your MIG's minimum number of instances is set to `0` and your metric value drops to `0`, then the MIG scales in to `0` until the metric value increases.

When your metric has multiple values, apply a filter to autoscale using an individual value from the metric. For more details about metric filters and other fields that you can use in your configuration, see Monitoring metrics concepts.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.autoscalers.create` on the project
  * `compute.instanceGroupManagers.use` on the project



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. If you don't have a managed instance group, [create one](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances). Otherwise, click the name of a MIG from the list to open that instance group page.

  3. Click **Edit**. 

  4. Click **Group size & autoscaling** to expand the section.

  5. If autoscaling configuration doesn't exist, click **Configure autoscaling**. 

By default, the autoscaling configuration adds a signal based on **CPU utilization**. If you don't require this signal, you can edit it to change the signal type.

  6. In the **Autoscaling signals** section, if a signal for a Monitoring metric exists, you can click to edit it, or click **Add a signal** to add one.
  7. Set the **Signal type** to **Cloud Monitoring metric**.

  8. Click **Configure**. In the **Resource and metric** pane that opens, do the following:

     1. Click **Select a metric**. 
        1. Select the metric that you want to use for autoscaling. You can filter the metrics based on any keywords—for example, memory, bytes, disk.
        2. Click **Apply**. The pane displays a chart that shows the data from the selected metric.
     2. If you want to use specific data from the metric, add a filter based on labels as follows:

        1. In the **Filters** section, click **Add a filter**.
        2. Select a **Label** and enter a **Value**.
        3. Click **Done**. The chart refreshes to show you the filtered metric value.
**Note:** The filter `project_id=PROJECT_ID` is added by default because you can use the metric values from the resources in the current project only.
     3. To view the aggregated value of metric that will be used to autoscale your MIG, toggle the **Show aggregation in chart** button. The chart refreshes to show the aggregated value.

     4. In the **Metric target options for autoscaling** section, select **Single VM instance assignment**.

     5. Provide a **Single instance assignment** value that represents the amount of work to assign to each VM in the MIG.

     6. When you've finished configuring the metric, click **Select**.

  9. Review the metric details and click **Done**.

  10. To complete the configuration, click **Save**.




###  gcloud 

To configure autoscaling based on Monitoring metrics, use the [`set-autoscaling` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-autoscaling).

**Note:** If autoscaling is already enabled for a MIG, the [`set-autoscaling`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-autoscaling) command overwrites the existing autoscaler to the new specifications.

In the command, specify the `--stackdriver-metric-single-instance-assignment` flag to indicate the amount of work that you expect each VM in the group to handle.

The following command creates an autoscaler based on work assignment for each VM.
    
    
    gcloud compute instance-groups managed set-autoscaling MIG_NAME \
        --max-num-replicas=MAX_INSTANCES \
        --min-num-replicas=MIN_INSTANCES \
        --update-stackdriver-metric=METRIC_URL \
        --stackdriver-metric-filter="METRIC_FILTER" \
        --stackdriver-metric-single-instance-assignment=INSTANCE_ASSIGNMENT
    

Replace the following:

  * `MIG_NAME`: the name of the MIG to autoscale.
  * `MAX_INSTANCES`: the maximum number of VMs that the MIG can have.
  * `MIN_INSTANCES`: the minimum number of VMs that the MIG needs to have.
  * `METRIC_URL`: a protocol-free URL of a Monitoring metric. For example, `compute.googleapis.com/instance_group/size`. If you use a custom metric, it must meet the custom metric requirements.
  * `METRIC_FILTER`: apply a filter to use an individual value from a metric with multiple values and to specify the monitored resource type. To learn more about metric filter, see Monitoring metrics concepts.
  * `INSTANCE_ASSIGNMENT`: the amount of work to assign to each VM instance in the MIG.



###  REST 

**Note:** Although autoscaling is a feature of managed instance groups, [autoscalers](https://docs.cloud.google.com/compute/docs/reference/v1/autoscalers) are a separate API resource. Keep that in mind when you construct API requests for autoscaling.

To configure autoscaling based on Monitoring metrics for a zonal MIG, use the [`autoscalers`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/autoscalers) resource or, for a regional MIG, use the [`regionAutoscalers`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers) resource.

Use the `singleInstanceAssignment` parameter to specify the amount of work that you expect each VM to handle.

For example, make the following call to create an autoscaler that scales a zonal MIG based on the instance assignment.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/autoscalers
    
    {
     "name": "AUTOSCALER_NAME",
     "target": "zones/ZONE/instanceGroupManagers/MIG_NAME",
     "autoscalingPolicy": {
      "maxNumReplicas": MAX_INSTANCES,
      "minNumReplicas": MIN_INSTANCES,
      "customMetricUtilizations": [
        {
          "metric": "METRIC_URL",
          "filter": "METRIC_FILTER",
          "singleInstanceAssignment": INSTANCE_ASSIGNMENT
        }
      ],
     }
    }
    

Replace the following:

  * `PROJECT_ID`: your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `ZONE`: the zone where the MIG is located.
  * `AUTOSCALER_NAME`: the name of the autoscaler.
  * `MIG_NAME`: the name of the MIG to autoscale.
  * `MAX_INSTANCES`: the maximum number of VMs that the MIG can have.
  * `MIN_INSTANCES`: the minimum number of VMs that the MIG needs to have.
  * `METRIC_URL`: a protocol-free URL of a Monitoring metric. For example, `compute.googleapis.com/instance_group/size`. If you use a custom metric, it must meet the custom metric requirements.
  * `METRIC_FILTER`: apply a filter to use an individual value from a metric with multiple values and to specify the monitored resource type. To learn more about metric filter, see Monitoring metrics concepts.
  * `INSTANCE_ASSIGNMENT`: the amount of work to assign to each VM instance in the MIG.



## Examples for autoscaling based on metrics

This section provides some examples of metrics used for autoscaling. For a complete list of metrics, see [Google Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp).

### Autoscale based on a custom metric

There might be a situation when the metric providing a relevant signal does not represent a total amount of available work or another resource applicable to the group, but instead an average, a percentile, or some other statistical property. For this example, assume that you scale based on the group's average processing latency.

Assume the following setup:

  * A zonal MIG named `our-instance-group` is assigned to perform a particular task. The group is located in zone `us-central1-a`.
  * You have a [Monitoring custom metric](https://docs.cloud.google.com/monitoring/custom-metrics) that exports a value that you would like to maintain at a particular level. For this example, assume the metric represents the average latency of processing queries assigned to the group. 
    * The custom metric is named: `custom.googleapis.com/example_average_latency`.
    * The custom metric has a label with a key named `group_name` and value equal to the MIG's name, `our-instance-group`.
    * The custom metric exports data for the [global monitored resource](https://docs.cloud.google.com/monitoring/api/resources#tag_global), that is, it is not associated with any specific VM.



You have determined that when the metric value is above some specific value, you need to add more VMs to the group to handle the load, while when it is below that value, you can free up some resources. You want the autoscaler to gradually add or remove VMs at a rate that is proportional to how much the metric is above or below the target. For this example, assume that you have determined your target value to be `250 delta/sec`.

You can configure autoscaling for the group using a utilization target of `250`, which represents the rate of change of the metric value that the autoscaler will attempt to maintain:

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of your MIG from the list to open the instance group overview page.

  3. Click **Edit**. 

  4. Click **Group size & autoscaling** to expand the section.

  5. If autoscaling configuration doesn't exist, click **Configure autoscaling**. 

By default, the autoscaling configuration adds a signal based on **CPU utilization**. If you don't require this signal, you can edit it to change the signal type.

  6. In the **Autoscaling signals** section, if a signal for a Monitoring metric exists, you can click to edit it, or click **Add a signal** to add one.
  7. Set the **Signal type** to **Cloud Monitoring metric**.

  8. Click **Configure**. The **Resource and metric** pane opens.

     1. Click **Select a metric**. 
        1. Choose your metric from **Global > Custom metrics**.
        2. Click **Apply**.
     2. In the **Filters** section, do the following: 
        1. Click **Add a filter**.
        2. In the **Label** drop-down, select `group_name`.
        3. In the **Value** field, provide `our-instance-group`.
        4. Click **Done**. The chart refreshes to show the filtered value from the metric.
     3. In the **Metric target options for autoscaling** section, do the following: 
        1. Select **Utilization target**.
        2. Enter the utilization target value as 250.
        3. Set the utilization target type to **Delta / sec**.
     4. After you've configured the metric, click **Select**.
  9. Review the metric details and then click **Done**.

  10. When you've finished, click **Save**.




###  gcloud 
    
    
    gcloud compute instance-groups managed set-autoscaling our-instance-group \
      --zone=us-central1-a \
      --max-num-replicas=50 \
      --min-num-replicas=0 \
      --update-stackdriver-metric=**custom.googleapis.com/example_average_latency** \
      --stackdriver-metric-filter=**"metric.labels.group_name = \"our-instance-group\" AND resource.type = \"global\""** \
      --stackdriver-metric-utilization-target=250 \
      --stackdriver-metric-utilization-target-type=delta-per-second

###  REST 
    
    
    POST https://compute.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/autoscalers
    {
    "name": "our-instance-group-autoscaler",
    "target": "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/instanceGroupManagers/our-instance-group",
    "autoscalingPolicy": {
      "maxNumReplicas": 50,
      "minNumReplicas": 0,
      "customMetricUtilizations": [
        {
          "filter": **"metric.labels.group_name=\"our-instance-group\" AND resource.type = \"global\""** ,
          "utilizationTargetType": "delta-per-second",
          "utilizationTarget": 250.0,
          "metric": **"custom.googleapis.com/example_average_latency"**
        }
      ]
    }
    }
    

### Autoscale based on unacknowledged messages in Pub/Sub

To configure autoscaling based on unacknowledged messages in a [Pub/Sub](https://docs.cloud.google.com/pubsub/docs) subscription, use the `subscription/num_undelivered_messages` metric provided by [`pubsub`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-pubsub) and filter by the `subscription ID`.

The `subscription/num_undelivered_messages` metric exports the total number of messages in the subscription, including messages that are being processed but that are not yet acknowledged. Using a metric that does not include the messages being processed is not recommended because such a metric can drop-down to 0 when there is still work being done, which prompts autoscaling to scale in and possibly interrupt the actual work.

If you don't have a subscription, you can create a [pull](https://docs.cloud.google.com/pubsub/docs/create-subscription), [push](https://docs.cloud.google.com/pubsub/docs/create-push-subscription), or [BigQuery](https://docs.cloud.google.com/pubsub/docs/create-bigquery-subscription) subscription before you configure autoscaling.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of your MIG from the list to open the instance group overview page.

  3. Click **Edit**. 

  4. Click **Group size & autoscaling** to expand the section.

  5. If autoscaling configuration doesn't exist, click **Configure autoscaling**. 

By default, the autoscaling configuration adds a signal based on **CPU utilization**. If you don't require this signal, you can edit it to change the signal type.

  6. In the **Autoscaling signals** section, if a signal for a Monitoring metric exists, you can click to edit it, or click **Add a signal** to add one.
  7. Set the **Signal type** to **Cloud Pub/Sub queue**.

  8. Select a **Topic**. If you want a new topic, click **Create a topic** to [create one](https://docs.cloud.google.com/pubsub/docs/admin).

  9. Select the **Subscription** based on which you want to autoscale your MIG. If you want a new subscription, click **Create a subscription** to [create one](https://docs.cloud.google.com/pubsub/docs/create-subscription).

  10. In the **Number of messages to assign to each VM** field, specify the number of unacknowledged messages that you expect each VM to handle.

  11. Click **Done**.

  12. When you've finished, click **Save**.




###  gcloud 
    
    
    gcloud compute instance-groups managed set-autoscaling MIG_NAME \
      --max-num-replicas=MAX_INSTANCES \
      --min-num-replicas=MIN_INSTANCES \
      --update-stackdriver-metric=**pubsub.googleapis.com/subscription/num_undelivered_messages** \
      --stackdriver-metric-filter=**"resource.type=\"pubsub_subscription\" AND resource.labels.subscription_id=\" SUBSCRIPTION_ID\""** \
      --stackdriver-metric-single-instance-assignment=NUMBER_OF_MESSAGES_TO_ASSIGN_TO_EACH_VM

###  REST 

To configure autoscaling for a zonal MIG, use the [`autoscalers`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/autoscalers) resource or, for a regional MIG, use the [`regionAutoscalers`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers) resource.

For example, make the following call to create an autoscaler for a zonal MIG.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/autoscalers
    {
    "name": "AUTOSCALER_NAME",
    "target": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME",
    "autoscalingPolicy": {
      "maxNumReplicas": MAX_INSTANCES,
      "minNumReplicas": MIN_INSTANCES,
      "customMetricUtilizations": [
        {
          "singleInstanceAssignment": NUMBER_OF_MESSAGES_TO_ASSIGN_TO_EACH_VM,
          "filter": **"resource.type = \"pubsub_subscription\" AND resource.labels.subscription_id=\" SUBSCRIPTION_ID\""**,
          "metric": **"pubsub.googleapis.com/subscription/num_undelivered_messages"**
        }
      ]
    }
    }
    

### Autoscale based on incoming network traffic

To configure autoscaling based on the incoming network traffic to VMs in your MIG, use the `instance/network/received_bytes_count` metric provided by [`compute`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-compute).

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of your MIG from the list to open the instance group overview page.

  3. Click **Edit**. 

  4. Click **Group size & autoscaling** to expand the section.

  5. If autoscaling configuration doesn't exist, click **Configure autoscaling**. 

By default, the autoscaling configuration adds a signal based on **CPU utilization**. If you don't require this signal, you can edit it to change the signal type.

  6. In the **Autoscaling signals** section, if a signal for a Monitoring metric exists, you can click to edit it, or click **Add a signal** to add one.
  7. Set the **Signal type** to **Cloud Monitoring metric**.

  8. Click **Configure**. The **Resource and metric** pane opens.

     1. Click **Select a metric**. 
        1. Select **VM Instance > Instance > Received bytes** (`compute.googleapis.com/instance/network/received_bytes_count`).
        2. Click **Apply**.
     2. In the **Metric target options for autoscaling** section, do the following: 
        1. Make sure that **Utilization target** is selected.
        2. Enter a utilization target value.
        3. Set a utilization target type.
     3. After you've configured the metric, click **Select**.
  9. Review the metric details and then click **Done**.

  10. When you've finished, click **Save**.




###  gcloud 
    
    
    gcloud compute instance-groups managed set-autoscaling MIG_NAME \
      --max-num-replicas=MAX_INSTANCES \
      --min-num-replicas=MIN_INSTANCES \
      --update-stackdriver-metric=**compute.googleapis.com/instance/network/received_bytes_count** \
      --stackdriver-metric-utilization-target=TARGET_VALUE \
      --stackdriver-metric-utilization-target-type=TARGET_TYPE
    

###  REST 
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/autoscalers
    {
    "name": "AUTOSCALER_NAME",
    "target": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME",
    "autoscalingPolicy": {
      "maxNumReplicas": MAX_INSTANCES,
      "minNumReplicas": MIN_INSTANCES,
      "customMetricUtilizations": [
        {
          "utilizationTargetType": "TARGET_TYPE",
          "utilizationTarget": TARGET_VALUE,
          "metric": **"compute.googleapis.com/instance/network/received_bytes_count"**
        }
      ]
    }
    }
    

### Autoscale based on memory usage

To configure autoscaling based on the percent of used memory, specify the `percent_used` metric provided by the [memory](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-memory) Ops Agent metrics. You should filter the metric by `state` to use only the `used` memory state. If you don't specify the filter, then the autoscaler takes the sum of memory usage by all memory states labeled as `buffered`, `cached`, `free`, `slab`, and `used`.

**Note:** The `memory/percent_used` metric is an [Ops Agent metric](https://docs.cloud.google.com/monitoring/api/metrics_opsagent). You must install the [Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent) before you configure autoscaling based on this metric.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of your MIG from the list to open the instance group overview page.

  3. On the instance group overview page, click **Edit**. 

  4. Click **Group size & autoscaling** to expand the section.

  5. If autoscaling configuration doesn't exist, click **Configure autoscaling**. 

By default, the autoscaling configuration adds a signal based on **CPU utilization**. If you don't require this signal, you can edit it to change the signal type.

  6. In the **Autoscaling signals** section, if a signal for a Monitoring metric exists, you can click to edit it, or click **Add a signal** to add one.
  7. Set the **Signal type** to **Cloud Monitoring metric**.

  8. Click **Configure**. The **Resource and metric** pane opens.

     1. Click **Select a metric**. 
        1. Select **VM Instance > Memory > Memory utilization** (`agent.googleapis.com/memory/percent_used`).
        2. Click **Apply**.
     2. In the **Filters** section, do the following: 
        1. Click **Add a filter**.
        2. In the **Label** drop-down, choose the **state** metric label.
        3. In the **Value** field, type **used**.
        4. Click **Done**.
     3. In the **Metric target options for autoscaling** section, do the following: 
        1. Make sure that **Utilization target** is selected.
        2. Enter a utilization target value.
        3. Set the utilization target type to **Gauge**.
     4. After you've configured the metric, click **Select**.
  9. Review the metric details and then click **Done**.

  10. When you've finished, click **Save**.




###  gcloud 
    
    
    gcloud compute instance-groups managed set-autoscaling MIG_NAME \
      --max-num-replicas=MAX_INSTANCES \
      --min-num-replicas=MIN_INSTANCES \
      --update-stackdriver-metric=**agent.googleapis.com/memory/percent_used** \
      --stackdriver-metric-filter=**"metric.labels.state = \"used\""** \
      --stackdriver-metric-utilization-target-type=gauge \
      --stackdriver-metric-utilization-target=TARGET_VALUE  \
    

###  REST 
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/autoscalers
    {
    "name": "AUTOSCALER_NAME",
    "target": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME",
    "autoscalingPolicy": {
      "maxNumReplicas": MAX_INSTANCES,
      "minNumReplicas": MIN_INSTANCES,
      "customMetricUtilizations": [
      {
        "filter": "metric.labels.state=\"used\"",
        "utilizationTargetType": "GAUGE",
        "utilizationTarget": TARGET_VALUE,
        "metric": **"agent.googleapis.com/memory/percent_used"**
      }
      ]
    }
    }
    

### Autoscale based on disk I/O

To configure autoscaling based on the total count of disk I/O operations, use the `operation_count` metric provided by the [disk](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-disk) Ops Agent metrics. If you want to scale based on read or write operations, filter the metric using the `direction` label. Similarly, to scale based on disk operations in a particular device, use the `device` label in the metric filter.

**Note:** The `disk/operation_count` metric is an [Ops Agent metric](https://docs.cloud.google.com/monitoring/api/metrics_opsagent). You must install the [Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent) before you configure autoscaling based on this metric.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of your MIG from the list to open the instance group overview page.

  3. On the instance group overview page, click **Edit**. 

  4. Click **Group size & autoscaling** to expand the section.

  5. If autoscaling configuration doesn't exist, click **Configure autoscaling**. 

By default, the autoscaling configuration adds a signal based on **CPU utilization**. If you don't require this signal, you can edit it to change the signal type.

  6. In the **Autoscaling signals** section, if a signal for a Monitoring metric exists, you can click to edit it, or click **Add a signal** to add one.
  7. Set the **Signal type** to **Cloud Monitoring metric**.

  8. Click **Configure**. The **Resource and metric** pane opens.

     1. Click **Select a metric**. 
        1. Select **VM instance > Disk > Disk operations** (`agent.googleapis.com/disk/operation_count`).
        2. Click **Apply**.
     2. In the **Metric target options for autoscaling** section, do the following: 
        1. Make sure that **Utilization target** is selected.
        2. Enter a utilization target value.
        3. Set a utilization target type.
     3. After you've configured the metric, click **Select**.
  9. Review the metric details and then click **Done**.

  10. When you've finished, click **Save**.




###  gcloud 
    
    
    gcloud compute instance-groups managed set-autoscaling MIG_NAME \
      --max-num-replicas=MAX_INSTANCES  \
      --min-num-replicas=MIN_INSTANCES  \
      --update-stackdriver-metric=**agent.googleapis.com/disk/operation_count** \
      --stackdriver-metric-utilization-target=TARGET_VALUE  \
      --stackdriver-metric-utilization-target-type=TARGET_TYPE
    

###  REST 
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/autoscalers
    {
    "name": "AUTOSCALER_NAME",
    "target": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME",
    "autoscalingPolicy": {
      "maxNumReplicas": MAX_INSTANCES,
      "minNumReplicas": MIN_INSTANCES,
      "customMetricUtilizations": [
      {
        "utilizationTargetType": "TARGET_TYPE",
        "utilizationTarget": TARGET_VALUE,
        "metric": **"agent.googleapis.com/disk/operation_count"**
      }
      ]
    }
    }
    

### Autoscale based on size of another MIG

You can autoscale a MIG based on the size of another MIG within the same project. For example, you can have multi-tier application with a frontend MIG that [autoscales based on a load balancer](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-load-balancing) and a backend MIG that autoscales proportionally to the frontend. Use a single instance assignment to define how many backend VMs are needed for every frontend VM. If you need 1 backend VM for every 4 frontend VMs, then set the single instance assignment to 4 in the backend MIG.

To autoscale a MIG (MIG_1) based on the size of another MIG (MIG_2), use the `instance_group/size` metric provided by [`compute`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-compute).

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of your MIG from the list to open the instance group overview page.

  3. On the instance group overview page, click **Edit**. 

  4. Click **Group size & autoscaling** to expand the section.

  5. If autoscaling configuration doesn't exist, click **Configure autoscaling**. 

By default, the autoscaling configuration adds a signal based on **CPU utilization**. If you don't require this signal, you can edit it to change the signal type.

  6. In the **Autoscaling signals** section, if a signal for a Monitoring metric exists, you can click to edit it, or click **Add a signal** to add one.
  7. Set the **Signal type** to **Cloud Monitoring metric**.

  8. Click **Configure**. The **Resource and metric** pane opens.

     1. Click **Select a metric**
        1. Select **Instance Group > Instance_group > Instance group size** (`compute.googleapis.com/instance_group/size`).
        2. Click **Apply**.
     2. In the **Filters** section, do the following: 
        1. Click **Add a filter**.
        2. In the **Label** drop-down, choose the **instance_group_name** resource label.
        3. In the **Value** field, type the name of the MIG (MIG_2) based on which you want to autoscale your MIG.
        4. Click **Done**.
     3. In the **Metric target options for autoscaling** section, do the following: 
        1. Select **Single VM instance assignment**.
        2. In the Single VM instance assignment field, enter `4`, if you want to keep 1 VM in your current MIG (MIG_1) for every 4 VMs in MIG_2.
     4. After you've configured the metric, click **Select**.
  9. Review the metric details and then click **Done**.

  10. When you've finished, click **Save**.




###  gcloud 
    
    
    gcloud compute instance-groups managed set-autoscaling MIG_1 \
      --max-num-replicas=MAX_INSTANCES \
      --min-num-replicas=MIN_INSTANCES \
      --update-stackdriver-metric=**compute.googleapis.com/instance_group/size** \
      --stackdriver-metric-filter=**"resource.type = \"instance_group\" AND resource.labels.location = \" ZONE|REGION\" AND resource.labels.instance_group_name = \"MIG_2\""** \
      --stackdriver-metric-single-instance-assignment=4
    

###  REST 
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/autoscalers
    {
    "name": "AUTOSCALER_NAME",
    "target": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_1",
    "autoscalingPolicy": {
      "maxNumReplicas": MAX_INSTANCES,
      "minNumReplicas": MIN_INSTANCES,
      "customMetricUtilizations": [
        {
          "singleInstanceAssignment": 4,
          "filter": **"resource.type = \"instance_group\" AND resource.labels.location = \" ZONE|REGION\" AND resource.labels.instance_group_name = \"MIG_2\""**,
          "metric": **"compute.googleapis.com/instance_group/size"**
        }
      ]
    }
    }
    

### Autoscale based on a metric from a different project

You can autoscale a MIG based on metrics from a different project. To allow your project to access metrics from another project, you must [add the other project to the metric scope](https://docs.cloud.google.com/monitoring/settings/multiple-projects) of your current project.

After you configure the metric scope, you can use metrics from the other project by specifying the metric's project ID in your filter using the `resource.labels.project_id` label.

When using metrics from a different project, the following limitations also apply:

  * You can only configure the metric using the gcloud CLI or REST. The Google Cloud console isn't supported.

  * You can only use those metrics that apply to the whole MIG. Metrics that come from each VM in your MIG are not supported.




The following example shows how to autoscale a zonal MIG (`MIG_1`) based on the size of another MIG (`MIG_2`) located in a different project.

###  gcloud 
    
    
    gcloud compute instance-groups managed set-autoscaling MIG_1 \
      --max-num-replicas=MAX_INSTANCES \
      --min-num-replicas=MIN_INSTANCES \
      --update-stackdriver-metric=**compute.googleapis.com/instance_group/size** \
      --stackdriver-metric-filter=**"resource.type = \"instance_group\" AND resource.labels.project_id = \" PROJECT_ID_OF_MIG_2\" AND resource.labels.instance_group_name = \"MIG_2\""** \
      --stackdriver-metric-single-instance-assignment=1 \
      --zone=ZONE
    

Replace the following:

  * `MIG_1`: the name of the MIG to autoscale.
  * `MAX_INSTANCES`: the maximum number of VMs that the MIG can have.
  * `MIN_INSTANCES`: the minimum number of VMs that the MIG needs to have.
  * `PROJECT_ID_OF_MIG_2`: the ID of the project containing the metric.
  * `MIG_2`: the name of the MIG providing the metric.
  * `ZONE`: the zone containing the MIG to autoscale.



###  REST 
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID_OF_MIG_1/zones/ZONE/autoscalers
    {
      "name": "AUTOSCALER_NAME",
      "target": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID_OF_MIG_1/zones/ZONE/instanceGroupManagers/MIG_1",
      "autoscalingPolicy": {
        "maxNumReplicas": MAX_INSTANCES,
        "minNumReplicas": MIN_INSTANCES,
        "customMetricUtilizations": [
          {
            "singleInstanceAssignment": 1,
            "filter": **"resource.type = \"instance_group\" AND resource.labels.project_id = \" PROJECT_ID_OF_MIG_2\" AND resource.labels.instance_group_name = \"MIG_2\""**,
            "metric": **"compute.googleapis.com/instance_group/size"**
          }
        ]
      }
    }
    

Replace the following:

  * `PROJECT_ID_OF_MIG_1`: the ID of the project containing the MIG to autoscale.
  * `ZONE`: the zone containing the MIG to autoscale.
  * `AUTOSCALER_NAME`: the name of the autoscaler that you're configuring.
  * `MIG_1`: the name of the MIG to autoscale.
  * `MAX_INSTANCES`: the maximum number of VMs that the MIG can have.
  * `MIN_INSTANCES`: the minimum number of VMs that the MIG needs to have.
  * `PROJECT_ID_OF_MIG_2`: the ID of the project containing the metric.
  * `MIG_2`: the name of the MIG providing the metric.



## Monitoring metrics concepts

This section provides a brief description of the Monitoring metrics concepts that you need to know while configuring autoscaling based on Monitoring metrics.

  * **Metric identifier** or **Metric URL** : The metric name in the form of a protocol-free URL. You can find URLs for built-in metrics URL from the [metric list](https://docs.cloud.google.com/monitoring/api/metrics_gcp).

For example, the URL of a Pub/Sub metric that gives the number of unacknowledged messages is `pubsub.googleapis.com/subscription/num_undelivered_messages`.

  * **Monitored resource type** : The source of metric value. You can find the monitored resource type of a metric from the [metric list](https://docs.cloud.google.com/monitoring/api/metrics_gcp).

For example, the monitored resource type of the `pubsub.googleapis.com/subscription/num_undelivered_messages` metric is [`pubsub_subscription`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-pubsub). For more details about each monitored resource type, see [Monitored resource types](https://docs.cloud.google.com/monitoring/api/resources).

  * **Metric filter** : When your metric has multiple values, a filter enables the autoscaler to identify a specific metric value from the set of possible metric values. Use the labels defined on a [metric](https://docs.cloud.google.com/monitoring/api/metrics_gcp) and a [monitored resource type](https://docs.cloud.google.com/monitoring/api/resources) to filter the values. If you want to explore your metric values with different filters, you can try them in the [metrics explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).

For example, the following screenshot shows `pubsub.googleapis.com/subscription/num_undelivered_messages` metric that gives the number of unacknowledged messages in all available subscriptions. Each line on the chart indicates a subscription.

![Metric explorer showing metric values without filter.](https://docs.cloud.google.com/static/compute/images/autoscaler/metric-without-filter.svg)

Without a filter, the autoscaler takes the sum of metric values from all subscriptions. To autoscale based on a single subscription, apply a filter on the`subscription_id` label defined for the `pubsub_subscription`. The following screenshot shows a single subscription after applying the filter.

![Metric explorer showing filtered metric value.](https://docs.cloud.google.com/static/compute/images/autoscaler/metric-with-filter.svg)




### Metric filtering requirements

When you use a metric that has multiple values (categorized using [labels](https://docs.cloud.google.com/monitoring/api/v3/metric-model#generic-label-info)), you can apply a filter to autoscale based on specific values from the metric. If the filter returns multiple values, then the values are added together. For best results, create a filter that is specific enough to return a single value.

Autoscaler filtering for metrics is compatible with the [Monitoring filter syntax](https://docs.cloud.google.com/monitoring/api/v3/filters). The filter must meet the following requirements:

  * You must wrap the value of a filter in double quotes.
  * You must use the direct equality comparison operator (`=`).
  * You must use the `AND` operator to join different filter criteria.

For example: `--stackdriver-metric-filter="resource.type=\"pubsub_subscription\" AND resource.labels.subscription_id=\"our-subscription\""`.

  * You must use direct values. You cannot use wildcards or functions in the filter.

For example, you cannot use `resource.labels.zone = starts_with("us-")`.

  * You cannot use [resource metadata labels](https://docs.cloud.google.com/stackdriver/docs/deprecations/metadata-labels) that store metadata about a monitored resource.




For a full reference of metric labels and monitored resource labels that you can filter on, see [metrics list](https://docs.cloud.google.com/monitoring/api/metrics_gcp) and [monitored resources list](https://docs.cloud.google.com/monitoring/api/resources).

### Custom metric requirements

To use custom metrics, you must first create a custom metric that is associated with one of the [monitored-resource types](https://docs.cloud.google.com/monitoring/custom-metrics#which-resource).

A custom metric used for autoscaling must have the following properties:

  * If the autoscaling configuration uses data from each VM in the group, set up instances in your MIG so that each VM exports the custom metric. The exported values from each VM must be associated with a [`gce_instance`](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance) monitored resource, which contains the following labels: 
    * `zone` with the name of the zone the instance is in.
    * `instance_id` with the value of unique numerical ID assigned to the VM.
  * The metric must export data at least every 60 seconds. If you export data more often than every 60 seconds, the autoscaler can respond to load changes more quickly. If you export your data less frequent than every 60 seconds, the autoscaler might not respond to load changes quickly enough.
  * The metric must export data that is of `INT64` or `DOUBLE` value type.



For information about creating a custom metric, see [Using custom metrics](https://docs.cloud.google.com/monitoring/custom-metrics/labeled).

## What's next

  * Learn about [managing autoscalers](https://docs.cloud.google.com/compute/docs/autoscaler/managing-autoscalers).
  * Learn [how autoscalers make decisions](https://docs.cloud.google.com/compute/docs/autoscaler/understanding-autoscaler-decisions).
  * Learn how to use [multiple autoscaling signals](https://docs.cloud.google.com/compute/docs/autoscaler/multiple-policies) to scale your group.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
