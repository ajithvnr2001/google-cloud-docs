---
url: https://docs.cloud.google.com/memorystore/docs/memcached/monitor-instances/
title: Monitor Memcached instances \u00a0|\u00a0 Memorystore for Memcached \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:19.593372+00:00
---

# Monitor Memcached instances  |  Memorystore for Memcached  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/monitor-instances/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-overview)



Send feedback 

#  Monitor Memcached instances Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to monitor your Memorystore for Memcached instance's performance.

Monitoring allows you to check in on your instances to make sure they're behaving as desired. This guide covers a few basic examples of monitoring Memcached instances. In addition to the types of monitoring covered here, Memorystore for Memcached is compatible with open source Memcached, so you can use existing Memcached monitoring tools from Compute Engine VMs to monitor your instances.

## Monitoring instances in the Google Cloud console

To view an instance's core metrics:

  1. Go to the **Memorystore for Memcached** page in the Google Cloud console.   
[Memorystore for Memcached](https://console.cloud.google.com/memorystore/memcached/instances)
  2. Click the Instance ID of the instance you'd like to view.



You can monitor several metrics by visiting an instance's **Instance details** page in the Google Cloud console. By default, the graph shows the instance's current memory usage and its max capacity. Other metrics available in the Google Cloud console are: Active Connections, Memory Usage, CPU Usage Time, Hit Ratio, Items, Eviction Count, Operation Count, Received Bytes, Sent Bytes, Uptime, Unused Memory, Get Operations, Set Operations, and Delete Operations.

To change the metrics shown on the graph, use the dropdown in its upper left corner. To change the time frame, select a different period of time in the upper right corner of the graph.

## Using Cloud Monitoring

[Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) is a monitoring service that allows you to view metrics such as uptime for your Memcached instances. For more details about all Memorystore for Memcached metrics available from Cloud Monitoring, see the [Monitoring reference documentation](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#gcp-memcache).

### Signing up for Cloud Monitoring

To access the monitoring console, click **Monitoring** in the Google Cloud console navigation pane:

[Go to Google Cloud console](https://console.cloud.google.com/)

For pricing information, see [Cloud Monitoring pricing](https://cloud.google.com/stackdriver/pricing).

### Viewing instance uptime, restart, and failover information in Monitoring

To view instance uptime information, use Metrics Explorer:

  1. Go to the Google Cloud console, login and navigate to the project with your Memcached instances:

[Go to Google Cloud console](https://console.cloud.google.com/)

  2. Select **Monitoring** from the left navigation menu.

  3. In **Monitoring** , if the navigation pane isn't expanded, click **Expand** _last_page_. This button is located on the lower left of the console.

  4. If **Metrics Explorer** is shown in the navigation pane, click **Metrics Explorer**. Otherwise, select **Resources** and then select **Metrics Explorer**.

  5. In the **Find resource type and metric** field, enter `memcache.googleapis.com/node/uptime`.




Your graph looks something like this:

![Graph of instance uptime](https://docs.cloud.google.com/static/memorystore/img/stackdriver-graph-redis-uptime.png)

  * Each line indicates a single instance.
  * Up and to the right indicates Memcached is up.
  * A drop off indicates a restart.
  * Missing data indicates unavailability.
  * Below your graph, there's a color-coded key that indicates which line belongs to which instance. As you hover over the key, the corresponding line on the graph is highlighted.



You can change the time horizon in the upper-right hand corner as well as add filters to tailor the information you're seeing to a particular region, project, instance, or node.

### Viewing operations per second

To view an instance's operations per second, use Metrics Explorer:

  1. Go to the Google Cloud console, login and navigate to the project with your Memcached instances:

[Go to Google Cloud console](https://console.cloud.google.com/)

  2. Select **Monitoring** from the left navigation menu.

  3. In **Monitoring** , if the navigation pane isn't expanded, click **Expand** _last_page_. This button is located on the lower left of the console.

  4. If **Metrics Explorer** is shown in the navigation pane, click **Metrics Explorer**. Otherwise, select **Resources** and then select **Metrics Explorer**.

  5. Select **Memcached instance** as the resource type.

  6. Enter `memcache.googleapis.com/node/operation_count` in the **Find resource type and metric** field.

  7. Choose **Sum** from the aggregation drop-down menu.




## Creating a dashboard to monitor Memcached memory usage

  1. In the Google Cloud console, select **Monitoring** , or use the following button:

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. Select **Dashboards > Create Dashboard**.

  3. Provide a name for the dashboard, e.g. "Memcached Dashboard", and click **Confirm**.

  4. Click **Add Chart**.

     1. Provide a chart title. For example, "Memcached Memory Usage".

     2. In the search box labeled **Find resource type and metric** , search for "Memorystore Memcached Node", and select the metric.

        1. Enter "Cache memory" as the metric type. 
           1. In the Filter box, add a filter for instance_id and select the instance you want to monitor.
           2. If you want to monitor the usage of all the Memorystore instances in your project, use Group by and select instance_id.
  5. Click **Save**. You can access this dashboard from the dashboards tab in the Monitoring UI.




### Setting a Monitoring alert for a metric

This section explains how to set an alert in Monitoring for an individual metric.

To create an alert for a metric:

  1. In the Google Cloud console, select **Monitoring** , or use the following button:

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. Click **Alerting** from the left navigation menu.

  3. Click the **Create Policy** button.

  4. Enter a Policy name.

  5. Click **Add Condition**.

     1. Provide a name for the condition, for example "Memory Usage Alert".
     2. Under **Target** , select Memorystore Memcached Node instance resource type. 
        1. Select the desired metric. For example, select "Memory Usage".
     3. Under **Configuration** , choose your desired condition. 
        1. For example, for Memory Usage you can choose **Any time the series violates**.
     4. Select values for **Condition triggers if** , **Threshold** , and duration (labeled as **For**). 
        1. For example, use the **Condition** , _is above_ , and set **Threshold** to the equivalent, in bytes, of 80% of your instance size. Set **For** to 1 minute initially to understand the usage pattern.
     5. Click **Add**.
  6. Set up a notification channel:

     1. Click the **Add notification channel** button. 
        * Option 1) Choose _Email_ from the **Notification Channel Type** menu. 
          * Enter the email address where you want your alerts sent.
        * Option 2) See [Creating channels](https://docs.cloud.google.com/monitoring/support/notification-options#creating_channels) for instructions on setting up other types of notification channels.
  7. Click the **Save** button.




## Viewing Memcached logs

Memcached produces logs that Cloud Logging captures.

### Viewing audit logs

  1. Go to the **Logs Explorer** page in the Google Cloud console.

[Logs Explorer](https://console.cloud.google.com/logs)

  2. To view the audit logs, select **Audited Resource > memcached.googleapis.com** from the resources drop-down.




## What's next

  * View available [Memcached metrics](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-metrics).
  * View available [Memcached configurations](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-configs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
