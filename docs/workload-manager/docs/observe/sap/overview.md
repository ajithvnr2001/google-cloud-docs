---
url: https://docs.cloud.google.com/workload-manager/docs/observe/sap/overview/
title: SAP observability overview \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:43.618612+00:00
---

# SAP observability overview  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/observe/sap/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  SAP observability overview Stay organized with collections  Save and categorize content based on your preferences. 

Workload Manager's observability service for SAP is a built-in monitoring solution for SAP workloads running on Google Cloud. This solution helps you improve issue detection, root cause analysis, and troubleshooting. It leverages the existing built-in alerting and monitoring features in Google Cloud. The observability service combines the infrastructure metrics and your SAP application metrics into a unified view to help correlate events and understand the health status of your SAP system across all its layers.

Workload Manager creates a logical representation of each SAP system, identified by the SAP system ID (SID), and provides a system-centric view of the workload. This lets you check the health and status of your workload at the system level, rather than the status of each underlying resource it consists of.

## Use cases

The observability service for SAP in Workload Manager is recommended for the following use cases:

  * Get a unified view of your SAP systems with an overall health status and sublayer health status.
  * See an overview of each SAP system, including the different layers and resources they consist of.
  * Perform troubleshooting and root cause analysis by using preconfigured dashboards, or viewing annotations for the occurrences of [predefined SAP events](https://docs.cloud.google.com/workload-manager/docs/observe/sap/view-dashboards#view-sap-events) on those dashboards, which help correlate events across the infrastructure and application layers.
  * View monitoring metrics for your infrastructure, operating system, and application on a single dashboard.
  * View upcoming host maintenance events for compute instances that are based on [supported machine types](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event#limitations) and belong to a specific SAP system.



## How it works

The following high-level architecture diagram shows how the information for observability dashboards is collected and sent to Workload Manager:

![Architecture for SAP observability in Workload Manager](https://docs.cloud.google.com/static/workload-manager/docs/observe/images/architecture.svg)

The following list shows the information sent by the components that are part of the observability service:

  * **Agent for SAP** :

    * Sends the following metrics to Cloud Monitoring:
    * Process Monitoring metrics
    * SAP HANA Monitoring metrics
    * Sends logs related to your SAP system to Cloud Logging.
    * Sends information on the underlying SAP system directly to Workload Manager.
  * **Ops Agent (Recommended):**

    * Sends infrastructure and guest OS information to Cloud Monitoring
  * **Cloud Asset Inventory:**

    * Provides the following instance metadata:
    * Maintenance events
    * Instances states
    * Instances machine types



## SAP system mapping

By default, the Agent for SAP only collects information about the underlying compute instance. In order to create a system-centric view and logical mapping of your SAP system, you need to configure additional features of the agent so that it can send the following information to Workload Manager:

  * Compute Engine instance name and number
  * Attached storage (disks, NFS)
  * Related load balancers, instance groups, health checks, forwarding rules, firewall rules
  * IP addresses
  * Database software name and version
  * Application software name and version
  * SAP system ID (SID): application and database



Workload Manager then performs a reconciliation process using the collected data to create a logical mapping of each SAP system which is referred to by its SID.

The following figure summarizes the system mapping in Workload Manager:

![SAP system mapping in Workload Manager](https://docs.cloud.google.com/static/workload-manager/docs/observe/images/system-mapping.svg)

## Pricing

The observability service for SAP in Workload Manager is available at no additional cost. However, the information for the observability dashboard comes from agents that are installed on each VM instance. These agents send data to Cloud Monitoring and Cloud Logging and you incur costs associated with these services.

The following table provides an estimated cost of the required features that must be enabled on each VM for SAP observability.

**Agent** | **Feature** | **Estimated monthly cost (per VM)**  
---|---|---  
Agent for SAP | [Process monitoring](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/process-monitoring) metrics, collected at the default frequency | $2.08  
Agent for SAP | [SAP HANA monitoring](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/monitoring-sap-hana) metrics, collected at the default frequency. | $0.56  
Ops Agent (Recommended) | Monitoring: [Agent metrics](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent) | No charge for default agent metrics.  
  
For more information, see [Agent for SAP pricing](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#pricing) and the [Ops agent pricing](https://docs.cloud.google.com/monitoring/agent/ops-agent#pricing). You can configure both agents to increase the frequency of metrics collection. You might incur more costs for the additional volume of metrics sent to Cloud Monitoring. In addition, both agents contain other features that might lead you incurring charges outside the scope of observability for SAP depending on the usage of those features.

You might also want to disable the [SAP HANA monitoring](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/config-commands#for_sap_hana_monitoring_metrics_collection) and [process monitoring](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/config-commands#for_process_monitoring_metrics_collection) metrics collection features in the agent to avoid any additional costs associated with Cloud Monitoring and Cloud Logging.

If you don't want to view any of your SAP workloads on the observability dashboard, then [remove the workload from the dashboard](https://docs.cloud.google.com/workload-manager/docs/observe/sap/view-dashboards#remove-dashboards).

## What's next

  * Read about [the supported SAP systems](https://docs.cloud.google.com/workload-manager/docs/observe/sap/supported-sap-systems).
  * Learn about [prerequisites for SAP observability](https://docs.cloud.google.com/workload-manager/docs/observe/sap/prerequisites).
  * Learn how to [observe an SAP workload](https://docs.cloud.google.com/workload-manager/docs/observe/sap/view-dashboards).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
