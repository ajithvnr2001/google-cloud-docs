---
url: https://docs.cloud.google.com/memorystore/docs/redis/monitor-instances/
title: Monitor instances \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:33:57.130845+00:00
---

# Monitor instances  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/monitor-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Monitor instances Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to monitor your Memorystore for Redis instance's performance.

Monitoring allows you to check in on your instances to make sure they're behaving as desired. This guide covers a few basic examples of monitoring Redis instances. In addition to the types of monitoring covered here, Memorystore for Redis is compatible with open source Redis, so you can use existing Redis monitoring tools from Compute Engine VMs to monitor your instances. 

## Monitoring instances in the Google Cloud console

To view an instance's core metrics:

  1. Go to the **Memorystore for Redis** page in the Google Cloud console.   
[Memorystore for Redis](https://console.cloud.google.com/memorystore/redis/instances)
  2. Click the Instance ID of the instance you'd like to view.



You can monitor several metrics by visiting an instance's **Monitoring** page in the Google Cloud console. The Memorystore for Redis monitoring page shows a chart for CPU seconds, memory usage/max memory, network bytes in/out, among others.

When you [scale an instance](https://docs.cloud.google.com/memorystore/docs/redis/about-scaling-instances), there might be a gap of several minutes when the [core metrics](https://docs.cloud.google.com/memorystore/docs/redis/monitor-instances#monitoring-instances-console) for the instance don't appear. During this time, the instance is available. After the time interval completes, the metrics appear.

## Monitoring instances with Cloud Monitoring

[Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) is a monitoring service that allows you to view metrics such as uptime for your Redis instances. For more details about all Memorystore for Redis metrics available from Cloud Monitoring, see the [Monitoring reference documentation](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-redis).

### Signing up for Cloud Monitoring

To access the monitoring console, click **Monitoring** in the Google Cloud console navigation pane:

[Go to Google Cloud console](https://console.cloud.google.com/)

For pricing information, see [Cloud Monitoring pricing](https://cloud.google.com/stackdriver/pricing).

### Viewing instance uptime, restart, and failover information in Google Cloud Observability

To view instance uptime information, use Metrics Explorer:

  1. Go to the Google Cloud console, login and navigate to the project with your Redis instances:

[Go to Google Cloud console](https://console.cloud.google.com/)

  2. Select **Monitoring** from the left navigation menu.

  3. In **Monitoring** , if the navigation pane isn't expanded, click **Expand** _last_page_. This button is located on the lower left of the console.

  4. If **Metrics Explorer** is shown in the navigation pane, click **Metrics Explorer**. Otherwise, select **Resources** and then select **Metrics Explorer**.

  5. Select `redis_instance` as the resource type and `redis/server/uptime` as the metric.




Your graph looks something like this:

![Graph of instance uptime](https://docs.cloud.google.com/static/memorystore/img/stackdriver-graph-redis-uptime.png)

  * Each line indicates a single instance.
  * Up and to the right indicates Redis is up.
  * A drop off indicates a restart.
  * Missing data indicates unavailability.
  * Below your graph, there's a color-coded key that indicates which line belongs to which instance. As you hover over the key, the corresponding line on the graph is highlighted.



For Standard Tier instances, there will be two entries with the same name but different colors in the key below the graph. The primary instance is the line with the highest uptime. You can identify a failover by looking for a spot on the graph where the primary instance's line drops off to zero and the replica's line continues to rise, indicating it has become the new primary instance.

You can change the time horizon in the upper-right hand corner as well as add filters to tailor the information you're seeing to a particular region, project, instance, or replica.

### Viewing operations per second

To view an instance's operations per second, use Metrics Explorer:

  1. Go to the Google Cloud console, login and navigate to the project with your Redis instances:

[Go to Google Cloud console](https://console.cloud.google.com/)

  2. Select **Monitoring** from the left navigation menu.

  3. In **Monitoring** , if the navigation pane isn't expanded, click **Expand** _last_page_. This button is located on the lower left of the console.

  4. If **Metrics Explorer** is shown in the navigation pane, click **Metrics Explorer**. Otherwise, select **Resources** and then select **Metrics Explorer**.

  5. Select **Redis instance** as the resource type.

  6. Select **Calls** as the desired metric.

  7. Choose **Sum** from the aggregation drop-down menu.




Calls is a metric surfaced by Memorystore for Redis that mimics the Redis `instantaneous_ops_per_sec` metric when you set the aggregation to sum.

## Set alerts in the Memorystore for Redis page

You can quickly enable recommended alert policies in the Memorystore for Redis page in the Google Cloud console.

**Note:** You can only set notifications using these instructions once. After creating an alerting policy using the Memorystore for Redis UI, you can only create or modify alerting policies using the dedicated Monitoring page in the Google Cloud console.

### Set an alert for _high system memory usage ratio_

  1. Go to the **Memorystore for Redis** page in the Google Cloud console.

[Memorystore for Redis](https://console.cloud.google.com/memorystore/redis/instances)

  2. Click the instance ID.

  3. Click **Create Alert Policy**.

  4. Select **Cloud Memorystore Redis Instance System Memory Usage Ratio**.

  5. **(Optional)** Modify the threshold for the alert trigger. We recommend that you keep the 80% system memory usage ratio threshold, however, if you want, you can adjust the threshold trigger.

     1. Click **Show options**.

     2. Enter a decimal value between 0 and 1 to indicate the threshold percentage. For example .35 indicates 35%.

  6. Under **Configure notifications** , select your notification channel.

  7. If you want to enable an alerting policy for [_high Redis engine CPU utilization_](https://docs.cloud.google.com/memorystore/docs/redis/monitor-instances#set_an_alert_for_high_redis_engine_cpu_utilization) or [_failover_](https://docs.cloud.google.com/memorystore/docs/redis/monitor-instances#set_an_alert_for_failover) using the Memorystore UI, do so before proceeding to the next step.

  8. Click **Create policies**.




### Set an alert for _high Redis engine CPU utilization_

  1. Go to the **Memorystore for Redis** page in the Google Cloud console.

[Memorystore for Redis](https://console.cloud.google.com/memorystore/redis/instances)

  2. Click the instance ID.

  3. Click **Create Alert Policy**.

  4. Select **Cloud Memorystore Redis Instance CPU Seconds**.

  5. **(Optional)** Modify the threshold for the alert trigger. We recommend that you keep the 90% CPU utilization threshold, however, if you want, you can adjust the threshold trigger.

     1. Click **Show options**.

     2. Enter a decimal value between 0 and 1 to indicate the threshold percentage. For example .35 indicates 35%.

  6. Under **Configure notifications** , select your notification channel.

  7. If you want to enable an alerting policy for [_high system memory usage ratio_](https://docs.cloud.google.com/memorystore/docs/redis/monitor-instances#set_an_alert_for_high_system_memory_usage_ratio) or [_failover_](https://docs.cloud.google.com/memorystore/docs/redis/monitor-instances#set_an_alert_for_failover) using the Memorystore UI, do so before proceeding to the next step.

  8. Click **Create policies**.




### Set an alert for _failover_

  1. Go to the **Memorystore for Redis** page in the Google Cloud console.

[Memorystore for Redis](https://console.cloud.google.com/memorystore/redis/instances)

  2. Click the instance ID.

  3. Click **Create Alert Policy**.

  4. Select **Cloud Memorystore Redis Instance Uptime**.

  5. Under **Configure notifications** , select your notification channel.

  6. If you want to enable an alerting policy for [_high system memory usage ratio_](https://docs.cloud.google.com/memorystore/docs/redis/monitor-instances#set_an_alert_for_high_system_memory_usage_ratio) or [_high Redis engine CPU utilization_](https://docs.cloud.google.com/memorystore/docs/redis/monitor-instances#set_an_alert_for_high_redis_engine_cpu_utilization) using the Memorystore UI, do so before proceeding to the next step.

  7. Click **Create policies**.




## Monitoring your instance's memory usage

You can monitor how much available memory you have in your Redis instance with a Monitoring dashboard. You can also set a Monitoring alert to notify you when your Redis memory reaches a customizable threshold.

### Creating a dashboard to monitor Redis memory usage

  1. In the Google Cloud console, select **Monitoring** , or use the following button:

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. Select **Dashboards > Create Dashboard**.

  3. Provide a name for the chart, e.g. "Redis Dashboard", and click **Confirm**.

  4. Click **Add Chart**.

     1. Provide a chart title. For example, "Redis Memory Usage".

     2. In the search box labeled **Find resource type and metric** , search for "Cloud Memorystore Redis Instance", and select it.

        1. Enter **Maximum Memory** as the metric type. 
           1. In the Filter box, add a filter for instance_id and select the instance you want to monitor.
           2. If you want to monitor the usage of all the Memorystore instances in your project, use "Group by" and select instance_id.
     3. Click **Add Metric** , select "Cloud Memorystore Redis Instance" as the resource type, and "Used Memory" as the metric.

        1. In the Filter box, add a filter for instance_id and select the instance you want to monitor.
        2. If you want to monitor the usage of all the Memorystore instances in your project, use Group by and select instance_id.
  5. Click **Save**. You can access this dashboard from the dashboards tab in Monitoring UI.




### Setting a Monitoring alert for memory usage

You can set an alert in Monitoring to notify you if the Used Memory metric exceeds a threshold that you set.

To create an alert for the Used Memory metric:

  1. In the Google Cloud console, select **Monitoring** , or use the following button:

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. Select **Alerting > Create a Policy**.

  3. Enter a **Policy name** such as "High Redis memory usage alert".

  4. Add a condition for Used Memory threshold:

     1. Click **Add Condition**.
     2. Provide a name for the condition, for example "Used Memory Alert".
     3. Under **Target** , select Cloud Memorystore Redis instance resource type. 
        1. For the Metric, select "Used Memory".
     4. Under **Configuration** , choose **Any time the series violates**.
     5. Set **Condition** to **Is above**.
     6. Set **Threshold** to the equivalent, in bytes, of 50% of your instance size. 
        1. When your memory usage exceeds 50%, you should regularly monitor your memory usage and consider [scaling up the instance](https://docs.cloud.google.com/memorystore/docs/redis/scaling-instances) if your memory usage rises dramatically.
     7. Set **For** to 1 minute initially to understand the usage pattern; you can increase this threshold to a higher number as the usage stabilizes.
     8. Click **Add**.
  5. Set the appropriate notification channel.

  6. Click the **Save** button.




You are now notified anytime the threshold is violated.

You can access this alerting policy from the **Alerting** tab in the Monitoring UI.

### Setting a Monitoring alert for system memory usage ratio

You should set an alert in Monitoring to notify you if the **system memory usage ratio** metric exceeds 80%.

To create an alert for the system memory usage ratio metric:

  1. In the Google Cloud console, select **Monitoring** , or use the following button:

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. Select **Alerting > Create a Policy**.

  3. Enter a **Policy name** such as "System memory usage ratio alert".

  4. Add a condition for the system memory usage ratio threshold:

     1. Click **Add Condition**.
     2. Provide a name for the condition, for example "System Memory Usage Ratio Alert".
     3. Under **Target** , select Cloud Memorystore Redis instance resource type. 
        1. For the Metric, select "System Memory Usage Ratio".
     4. Under **Configuration** , choose **Any time the series violates**.
     5. Set **Condition** to **Is above**.
     6. Set **Threshold** to `0.8`, which represents 80% of your system memory. 
        1. When your system memory usage exceeds 80%, follow the best practices for [Managing your system memory usage ratio](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#manage_your_system_memory_usage_ratio).
     7. Optionally, use the **Filter** field to set an alert for a single instance ID. If you choose not to filter to a specific instance, the alert will notify you any time a Memorystore for Redis instance in your project has a system memory usage ratio exceeding 80%.
     8. Click the **Add button**.
  5. Set the appropriate notification channel.

  6. Click the **Save** button.




You are now notified anytime the system memory usage ratio exceeds 80%.

## Viewing Redis logs

Redis produces logs that Cloud Logging captures.

### Viewing audit logs

  1. Go to the **Logs Explorer** page in the Google Cloud console.

  2. To view the audit logs, select **Audited Resource > redis.googleapis.com** from the resources drop-down.




### Viewing activity logs

  1. Go to the **Logs Explorer** page in the Google Cloud console.

[Logs Explorer](https://console.cloud.google.com/logs)

  2. To view the activity logs, select **Cloud Memorystore Redis instance** from the resources drop-down.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
