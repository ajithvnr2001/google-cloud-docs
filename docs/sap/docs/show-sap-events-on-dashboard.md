---
url: https://docs.cloud.google.com/sap/docs/show-sap-events-on-dashboard/
title: Show SAP events on Cloud Monitoring dashboards \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:12:37.866715+00:00
---

# Show SAP events on Cloud Monitoring dashboards  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/show-sap-events-on-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Show SAP events on Cloud Monitoring dashboards Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how you show annotations for events that occur in your SAP systems or the underlying infrastructure, on Cloud Monitoring dashboards and predefined observability dashboards. 

Viewing event annotations on Monitoring or observability dashboards can help you correlate the events with issues that you might experience in your SAP systems. For more information about event annotations, see [About event annotations](https://docs.cloud.google.com/monitoring/dashboards/show-events#about_event_annotations).

From version 3.7, Google Cloud's Agent for SAP automatically keeps track of certain changes in your SAP systems and the underlying infrastructure. For example, the agent tracks if the SAP HANA database in your SAP system stops or restarts, if the underlying Compute Engine starts or restarts. The agent's integration with Cloud Logging and Monitoring lets you show these events as annotations on Monitoring or predefined observability dashboards.

## Supported SAP event types

The following table describes the SAP event types that you can show as annotations on Monitoring or predefined observability dashboards:

Event type | Description  
---|---  
**SAP Availability** |  Provides information about the status of the following resources whenever they stop, start, or face any errors: SAP HANA, SAP NetWeaver, and the nodes and resources in Pacemaker-managed Linux high-availability (HA) clusters. Showing events of this type as annotations requires Google Cloud's Agent for SAP to collect the following [ Process Monitoring metrics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/process-monitoring#process_monitoring_metrics):

  * `sap/hana/service`
  * `sap/hana/availability`
  * `sap/nw/service`
  * `sap/nw/availability`
  * `sap/cluster/nodes`
  * `sap/cluster/resources`

  
**SAP Backint** |  Provides information about Backint based backup and recovery operations. Showing events of this type as annotations requires Google Cloud's Agent for SAP to collect the Backint metrics. For information about these metrics, see [ Backint metrics collection](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#backint_metrics_collection).  
**SAP Operations** |  Provides information about the status of data replication in SAP HANA high-availability (HA) systems. Showing events of this type as annotations requires Google Cloud's Agent for SAP to collect the following [ Process Monitoring metric](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/process-monitoring#process_monitoring_metrics): `sap/hana/ha/replication`.  
  
## Configure the Agent for SAP

To show SAP events as annotations on Monitoring or predefined observability dashboards, you need to install Google Cloud's Agent for SAP and configure it to emit the required set of metrics.

To do this, complete the following steps:

  1. Make sure that version 3.7 or later of Google Cloud's Agent for SAP is installed on the Compute Engine instances that host the SAP systems that you want to monitor.

For information about how to install the agent, see [Install and configure Google Cloud's Agent for SAP on a Compute Engine instance](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-vm). For information about how to update the agent, see [Update Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#agent4sap-update).

  2. Configure the agent as follows:

     * Set the `log_to_cloud` configuration property of the agent to the value `true`.

To set this value, connect to your Compute Engine instance by using SSH and then run the following command:
           
           sudo /usr/bin/google_cloud_sap_agent configure -setting=log_to_cloud -enable
           

     * Enable the collection of the required types of metrics.

For information about the metrics that are required for the supported SAP event types, see Supported SAP event types.




## Show SAP events on a dashboard

  1. In the Google Cloud project where events need to be shown on dashboards, grant the required IAM roles or permissions to the users who need to view and show the SAP events on dashboards.

For information about the required IAM roles and permissions, see the "Before you begin" section in [Show events on a dashboard](https://docs.cloud.google.com/monitoring/dashboards/show-events).

  2. Configure the Monitoring dashboard or predefined observability dashboard to show the required SAP events.

For information about how to configure the dashboard, see the "Show events" section in [Show events on a dashboard](https://docs.cloud.google.com/monitoring/dashboards/show-events).

For information about the SAP event types that you can show as annotations on dashboards, see Supported SAP event types.




## View SAP event details

When you view a chart on a dashboard, you see the selected SAP events when they occur in your SAP system. You can view additional information about that event by clicking the **View** button.

For more information about viewing event details, see the "View event details" section in the [Show events on a dashboard](https://docs.cloud.google.com/monitoring/dashboards/show-events).

The following example images show SAP events as annotations on dashboards:

  * The following example image shows events of types **SAP Availability** and **SAP Operations** that get triggered after a failover occurs in the Pacemaker-managed high-availability (HA) cluster, which includes the following:

    * Moving the SAP HANA database from the primary node of the cluster to the secondary node.
    * Reconnecting the old primary node as the secondary node in the cluster.
    * Enabling SAP HANA System Replication between the primary and secondary nodes in the cluster.

![Screenshot shows event annotations for the SAP Availability and SAP Operations event types.](https://docs.cloud.google.com/static/sap/docs/images/sap-availability-event-on-dashboard-ss.png)

  * The following example image shows events of type **SAP Backint** that get triggered after the successful creation of a [Backint](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery) based backup the SAP HANA data volume and partitions. The event annotation provides information about the throughput and size of the backup.

![Screenshot showing event annotations for the SAP Backint event type.](https://docs.cloud.google.com/static/sap/docs/images/backint-event-on-dashboard-ss.png)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
