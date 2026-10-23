---
url: https://docs.cloud.google.com/compute/docs/instance-groups/monitor-instance-distribution/
title: Monitor instance distribution in MIGs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:56:05.310089+00:00
---

# Monitor instance distribution in MIGs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/monitor-instance-distribution/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Monitor instance distribution in MIGs Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the benefits, use cases, and the dashboard for monitoring virtual machine (VM) instance distribution in managed instance groups (MIGs). It also describes how to view the instance distribution for a specific MIG or across multiple MIGs, as well as how to customize and query the dashboard.

When your MIG uses [location flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs) to distribute instances across multiple zones, [instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility) to specify multiple compatible machine types, or both, the MIG dynamically selects and provisions instances based on real-time resource availability. To monitor this behavior in real-time, you can use a dashboard to track how your instances are distributed across zones and machine types over time. You can view this data for a single MIG or aggregated across multiple MIGs. The dashboard also shows you both the running (active) and not running (inactive) instances, and the total instance count over the period. You can interpret the dashboard metrics to diagnose capacity allocation, zonal balance, and fallback behavior.

## Benefits of monitoring instance distribution in MIGs

When your MIG deploys instances across multiple zones in a regional group, or when you specify multiple machine types and ranks in an instance flexibility policy, the actual distribution of locations and machine types changes dynamically depending on the resource availability.

Monitoring your runtime instance distribution helps you do the following:

  * **Improve obtainability and mitigate capacity constraints** : Verify if your MIG is successfully obtaining resources when scaling out. The creation of instances in fallback ranks shows that your instance flexibility policy is efficiently mitigating temporary capacity constraints. But, if your group consistently struggles to reach its target size despite these fallbacks, then consider expanding your allowed machine types or adding more zones to help reduce the probability of future resource availability errors.

  * **Verify location flexibility and zonal balance** : Confirm that a regional MIG is balancing capacity across zones as intended (`EVEN` or `BALANCED`), or observe how capacity shifts dynamically across zones when using `ANY` or `ANY_SINGLE_ZONE` target distribution shapes.

  * **Balance cost and performance** : By tracking which machine types are selected for MIGs with instance flexibility, you can better understand your spending and performance, as well as look for opportunities for improvement. For example, if your instances are consistently delivering higher performance than your workload requires, then consider investigating if your workload can tolerate prioritizing options with lower costs. Alternatively, if you notice performance issues, then, based on obtainability, you might consider prioritizing high-performance machine types rather than splitting your workload across more machines.




To learn more about how the monitoring dashboard helps with observability questions, see Interpret the dashboard in this document.

## Monitor MIG instance distribution

You can monitor the instance distribution in MIGs by using one of the following ways:

  * **To view the instance distribution for a specific MIG** , use the **Monitoring** tab on the MIG page. For instructions, see View instance distribution for a specific MIG.

  * **To view the instance distribution across multiple MIGs** , use the Cloud Monitoring dashboard for an aggregated view. For instructions, see View instance distribution across multiple MIGs.

  * **To integrate instance distribution data into custom dashboards** , query the underlying metrics programmatically by using PromQL. This code-based alternative lets you export data to external monitoring tools, such as Grafana. For instructions, see Programmatically query using PromQL.




## About the instance distribution dashboard

**Important:** The MIG instance distribution monitoring dashboard is intended for observability, not for troubleshooting. To identify the underlying causes of creation failures or capacity constraints, instead see [Troubleshooting resource availability errors](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-resource-availability).

The MIG instance distribution monitoring dashboard provides the following four specialized charts:

  * **Instance distribution by zone** : A chart displaying instance count grouped by zone, showing location flexibility and zonal distribution across your regions.

  * **Instance distribution by machine type** : A chart displaying instance count grouped by machine type, showing how your group allocates capacity across different machine types and sizes.

  * **Active versus inactive instances** : A chart displaying the number of instances grouped by whether they are active or inactive. An active instance is fully operational and running (`RUNNING`). An inactive instance is one that is not running but has not been deleted; this includes instances being created (`PROVISIONING`, `STAGING`), paused (`SUSPENDED`), or shut down (`STOPPED`, `TERMINATED`).

  * **Total instance count** : A chart displaying the total number of instances in the MIG over the period.




These charts rely on standard Compute Engine system metadata labels and metrics, such as `compute.googleapis.com/instance/cpu/utilization` and `metadata.system_labels.machine_type`. Cloud Monitoring automatically collects these system metrics and metadata labels for all Compute Engine instances. You don't need to install the Ops Agent or configure custom guest telemetry inside your instances to view these charts on the dashboard.

**Note:** The **GCE MIG Instance Distribution Monitoring** dashboard in Cloud Monitoring is designed specifically for MIGs. You cannot use this dashboard to monitor location or instance flexibility of independent instances created using the [`bulkInsert` method](https://docs.cloud.google.com/compute/docs/instances/multiple/about-bulk-creation).

To view instance distribution data scoped to a specific MIG or across multiple MIGs, see View instance distribution.

### Required roles

  * To get the permissions that you need to view dashboards by using the Google Cloud console, ask your administrator to grant you the following IAM roles on your project: 

    * To view the dashboard in Cloud Monitoring: [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`) 
    * To navigate to a MIG's Monitoring tab in Compute Engine: [Compute Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`) 

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about roles, see [Control access with Identity and Access Management](https://docs.cloud.google.com/monitoring/access-control).




## View instance distribution

You can view the instance distribution dashboard for a specific MIG or aggregated data across multiple MIGs.

### View instance distribution for a specific MIG

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of the MIG that you want to monitor.

  3. Click the **Monitoring** tab.

  4. In the navigation panel of the **Monitoring** tab, select **Instance distribution**.




### View instance distribution across multiple MIGs

To observe the instance distribution across all your MIGs at once, use the preconfigured dashboard in Cloud Monitoring. By default, this dashboard aggregates data across all MIGs in your project.

  1. In the Google Cloud console, go to the **Monitoring** > **Dashboards** page. 

[Go to Dashboards](https://console.cloud.google.com/monitoring/dashboards)

  2. In the **Filter** , search for **GCE MIG Instance Distribution Monitoring** dashboard and select it. You can also find this dashboard in the **Type** menu > **Google Services** category.

  3. Optional: If your project contains multiple MIGs and you want to narrow down the aggregated view, then use the dashboard's filter variables to filter by region, zone, or instance_group.




## Customize the Cloud Monitoring dashboard

You can customize the instance distribution dashboard in Cloud Monitoring, but you cannot modify the view within a specific MIG's **Monitoring** tab.

In Cloud Monitoring, to modify the dashboard's charts, apply filters, or configure custom layout structures, you must first copy the preconfigured dashboard.

  1. In the Google Cloud console, go to the **Monitoring** > **Dashboards** page.

[Go to Dashboards](https://console.cloud.google.com/monitoring/dashboards)

  2. In the **Filter** , search for the **GCE MIG Instance Distribution Monitoring** dashboard and select it. You can also find this dashboard in the **Type** menu > **Google Services** category.

  3. Click **Copy dashboard**.

  4. Edit the copied dashboard to modify its name, charts, layout, or to apply filters as required.




You can view your copied or customized dashboard in the **Type** menu > **Custom** category.

For more information about customizing the dashboard, see the following pages in the Cloud Monitoring documentation:

  * To modify the data that each chart displays, see [Update the query of a widget](https://docs.cloud.google.com/monitoring/dashboards/filter-permanent#apply-permanent-filter).

  * To customize the dashboard, see [Create a custom dashboard by copying a Google Cloud service dashboard](https://docs.cloud.google.com/monitoring/charts/predefined-dashboards#customize-gc-dashboards).




### Apply dashboard filters

The **GCE MIG Instance Distribution Monitoring** dashboard includes built-in filter variables that let you drill down into specific subsets of your MIG:

  * **Region (`region`)**: Filter charts to show instances in one or more specific Google Cloud regions.

  * **Zone (`zone`)**: Filter charts to observe zonal distribution and verify whether instances are evenly balanced or shifting capacity across specific zones.

  * **Instance group (`instance_group`)**: Filter charts to isolate a single MIG when your project contains multiple MIGs.




To apply a filter in the Google Cloud console, on your copied dashboard, click **Filter** , select the filter property (such as `region`, `zone`, or `instance_group`), and select the chosen values.

For more information on using filters, see [Add temporary filters to a custom dashboard](https://docs.cloud.google.com/monitoring/charts/filter-dashboard) in the Cloud Monitoring documentation.

### Configure event annotations

When analyzing changes in instance distribution across zones and machine types, configuring annotations for lifecycle events or deployments helps you correlate capacity shifts with specific operational activities. For example, you can add annotations to chart timelines to highlight events, such as the following:

  * MIG configuration updates, such as modifying the target distribution shape, `instanceSelections`, or `rank` order.

  * Rolling updates or instance repairs initiated within the group.

  * Simulated or real zonal outage events.

  * Autoscaling decisions.




For more information about available event types and how to add annotations, see the following pages in the Cloud Monitoring documentation:

  * To learn more about the event types that you can add to the dashboard, see [Compute Engine event types](https://docs.cloud.google.com/monitoring/dashboards/event-types#compute-events).

  * To add annotations or overlay event markers on your dashboard chart, see [Configure dashboards to show events](https://docs.cloud.google.com/monitoring/dashboards/show-events#monitoring-dashboards).




## Interpret the dashboard

When viewing your MIG instance distribution dashboard, use the following guidance to answer common observability questions and interpret dynamic location and machine type behavior.

### Why are my instances running in specific zones or shifting across zones?

If the **Instance distribution by zone** chart indicates an uneven distribution across zones in a regional MIG or sudden capacity shifts across locations, check the following location flexibility factors:

  * **Target distribution shape** : Verify your configured [target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape). If your MIG is configured with `ANY` or `ANY_SINGLE_ZONE`, the MIG prioritizes zones where capacity or unused reservations are most readily available rather than balancing instances evenly. If your MIG uses `BALANCED`, the group attempts to keep instance counts balanced across zones, but might temporarily place instances in alternate zones if a specific zone experiences a temporary capacity shortage.

  * **Regional capacity redistribution** : During a temporary capacity shortage, due to events such as a localized zonal outage, a regional MIG configured for high availability automatically finds and allocates replacement instances in alternate zones within the region. The dashboard will reflect this location flexibility as a drop in instance count for the affected zone and a corresponding rise in alternate zones.




### Why is my MIG running on fallback machine types?

If your MIG uses instance flexibility and the **Instance distribution by machine type** chart shows that your group is actively creating and running instances on lower-preference (higher rank value) machine types instead of your primary selection, consider the following potential causes:

  * **Temporary resource constraints** : If primary machine types experience high demand or temporary resource constraints, the MIG automatically falls back to secondary selections to ensure your target capacity is obtained. Even when the preferred machine types are available again, the MIG keeps using the fallback machine types and doesn't proactively switch back to the preferred ones.

  * **Quota limitations** : Verify that your Google Cloud project has sufficient vCPU and resource quota for your preferred machine series in the selected region. If quota is exhausted for the primary machine type, then the MIG provisions from available secondary selections.




For more information, see [How a MIG selects machine types](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility#how_a_mig_selects_machine_types).

**Note:** When a MIG shifts across zones or falls back to a lower-preference machine type due to capacity or quota constraints, this dynamic behavior is normal and intended. It doesn't indicate an application or configuration error. To investigate the exact reason for individual instance creation attempts or fallback triggers, inspect the MIG error logs or activity log entries. For more information about logs, see [Compute Engine audit logging](https://docs.cloud.google.com/compute/docs/logging/audit-logging).

## Programmatically query using PromQL

To monitor the instance distribution in a MIG, you can also query the underlying metrics programmatically by using [PromQL for Cloud Monitoring](https://docs.cloud.google.com/monitoring/promql). Querying programmatically lets you integrate the instance distribution data into your custom observability dashboards or external monitoring tools, such as Grafana. You can use PromQL to query instances by zone, or by machine type.

Run the PromQL queries in the code editor as described in the following section.

### Access the code editor

You can access PromQL from the following pages in the Google Cloud console:

  * **Metrics Explorer**
  * **Add widget** when creating dashboards



To open the code editor when using Metrics Explorer, do the following:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the _code_ **PromQL** button.

  3. Type your query into the text field and click **Run Query**. The following sections provide example queries.




For more information about the code editor, see [Use the code editor for PromQL](https://docs.cloud.google.com/monitoring/promql/promql-in-monitoring) in the Cloud Monitoring documentation.

### Query active instances by zone

To query active instances by zone, run the following query in the code editor:
    
    
    count by (zone) (compute_googleapis_com:instance_cpu_utilization{metadata_system_instance_group="YOUR_MIG_NAME"})
    

Replace `YOUR_MIG_NAME` with the name of your MIG.

### Query active instances by machine type

To query active instances by machine type, run the following query in the code editor:
    
    
    count by (metadata_system_machine_type) (compute_googleapis_com:instance_cpu_utilization{metadata_system_instance_group="YOUR_MIG_NAME"})
    

Replace `YOUR_MIG_NAME` with the name of your MIG.

## What's next

  * Learn about [location flexibility in regional MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs).
  * Learn about [instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility).
  * [Add instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/configure-instance-flexibility) to a MIG.
  * [View instance flexibility configuration](https://docs.cloud.google.com/compute/docs/instance-groups/view-instance-flexibility-configuration) in a MIG.
  * Learn how to [create and manage custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards#create-custom-dashboard).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
