---
url: https://docs.cloud.google.com/vmware-engine/docs/concepts-monitoring/
title: Overview of VMware Engine monitoring \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:59:46.305427+00:00
---

# Overview of VMware Engine monitoring  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/concepts-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Overview of VMware Engine monitoring

This document provides an overview of the different methods for monitoring Google Cloud VMware Engine private clouds. It describes the recommended preparation, day-1 operations to enable effective monitoring, and day-2 capabilities available for operations.

Monitoring your VMware Engine private clouds helps you operate your environment efficiently, troubleshoot errors, and optimize performance, both at the project level (all private clouds within a project) and for individual private clouds.

You can monitor resources (private clouds, nodes) created in your Google Cloud project using Google Cloud tools and mechanisms. You can also set up and integrate monitoring for VMware components and workload VMs running in your private cloud with Google Cloud tools.

## Email notifications using Essential Contacts for service events

VMware Engine service automatically sends emails to contacts in the appropriate notification categories configured in [Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts). The following table lists the Essential Contacts notification category and action owner for events that cause service impacts and trigger email notifications.

**Note:** These automatic emails form a strict subset of the events available through Cloud Logging. [ VMware component](https://docs.cloud.google.com/vmware-engine/docs/concepts-vmware-components) | Essential Contacts notification category | Action owner  
---|---|---  
VMware Engine node | `Technical` | `VMware Engine Service Operations`  
VMware vCenter | `Technical` | `VMware Engine Service Operations`  
VMware NSX Manager | `Technical` | `VMware Engine Service Operations`  
VMware HCX | `Technical` | `VMware Engine Service Operations`  
vSAN utilization | `Technical` | `Customer`  
Cluster auto-scale | `Technical` | `Issue dependent`  
Private cloud operations (create, delete, add and remove nodes) | `Technical` | `Issue dependent`  
Stretched private cloud issues | `Technical` | `VMware Engine Service Operations`  
  
### Use of Essential Contacts by other VMware Engine features

Other VMware Engine features also use service-related automatic email notifications, such as [Update Center](https://docs.cloud.google.com/vmware-engine/docs/update-center), which supports day-2 operations.

## Set up email alerts

You can set up VMware Engine to notify a user about important events that may impact the resources in your project and private cloud, or changes to your private cloud configuration. To add a contact, do the following:

  1. In the Google Cloud console, go to the **Essential Contacts** page.

[Go to Essential Contacts](https://console.cloud.google.com/iam-admin/essential-contacts)

  2. Click **Select a project** and then select the organization, folder, or project that contains the provisioned private cloud that you want to add a contact to.

  3. Click person_add **Add contact**.

![Screenshot of the Essential Contacts page Add Contact menu option](https://docs.cloud.google.com/static/resource-manager/img/essential-contacts-add-contact.png)

  4. In the **Email** and **Confirm email** fields, enter the email address of the contact.

  5. From the **Notification categories** drop-down menu, select the notification categories that you want the contact to receive communications for. For a list of notification categories and recommended contacts, see [Identifying contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts#notification-categories) on this page.

  6. Click **Save**.




## Monitor VMware Engine in your project through Cloud Logging

VMware Engine service-related issues cover certain conditions and are logged in Cloud Logging. The email notification indicates whether you should take action to resolve the issue.

The [log severity](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#logseverity) conveys the severity of the issues. You can use Cloud Logging to enable [log-based alerting policies](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts) to receive notifications. The following table lists the classes of available logs for VMware Engine and the severity of the reported events:

The following table lists the available logs for VMware Engine and the [severity](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#logseverity) of the reported events:

[ VMware component](https://docs.cloud.google.com/vmware-engine/docs/concepts-vmware-components) | Issue notification | Resolution notification | Action owner  
---|---|---|---  
VMware Engine node | `ALERT` | `NOTICE` | `VMware Engine Service Operations`  
VMware vCenter | `CRITICAL` | `NOTICE` | `VMware Engine Service Operations`  
VMware NSX Manager | `CRITICAL` | `NOTICE` | `VMware Engine Service Operations`  
VMware HCX | `CRITICAL` | `NOTICE` | `VMware Engine Service Operations`  
vSAN utilization | `ALERT` | `Not applicable` | `Customer`  
Cluster auto-scale | `Issue dependent` | `Issue dependent` | `Issue dependent`  
Private cloud operations (create, delete, add and remove nodes) | `Issue dependent` | `Issue dependent` | `Issue dependent`  
Stretched private cloud issues | `ALERT` | `NOTICE` | `VMware Engine Service Operations`  
  
You can access logs for VMware Engine in the following ways:

  * In [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), by using the following log name:

    * `projects/PROJECT_ID/logs/vmwareengine.googleapis.com%2Falerts`
  * In the Google Cloud console, by going to the [**Dashboard** page](https://console.cloud.google.com/vmwareengine/dashboard).




For more information about receiving notifications using logs, see [Configure log-based alerting policies](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts) in the Google Cloud Observability documentation.

### Use of Cloud Logging by other VMware Engine features

Other VMware Engine features also generate service-related logs, such as [Update Center](https://docs.cloud.google.com/vmware-engine/docs/update-center), which supports day-2 operations.

## Monitor project resources - inventory and usage

Many VMware Engine resources are available in [Google Cloud asset inventory and search](https://docs.cloud.google.com/asset-inventory/docs/overview) for asset discovery and tracking changes. See [Asset inventory services for VMware Engine](https://docs.cloud.google.com/vmware-engine/docs/concepts-asset-inventory-services) for more details.

VMware Engine resources are subject to [Cloud Audit Logging](https://docs.cloud.google.com/logging/docs/audit), recording administrator activities and access. For more details, see [Google Cloud VMware Engine audit logging](https://docs.cloud.google.com/vmware-engine/docs/audit-logging).

## Monitor VMware Engine private clouds

You can choose Cloud Monitoring or a third-party tool mentioned in this section to monitor your VMware Engine private clouds. This section uses a decision-making flow to help you choose the method that best suits your needs. If you prefer a visual guide, see Decision tree in this document. For information on how to maintain your private cloud's configuration health by identifying and resolving configuration drift, see [Maintain private cloud configuration health](https://docs.cloud.google.com/vmware-engine/docs/maintain-private-cloud-configuration-health).

To choose a method to monitor your private cloud, consider the following questions:

  1. Do you want to centralize infrastructure logs from VMware components and use an external log monitoring system?

     * **Yes** : See Forward syslog messages to a remote server in this document.

     * **No** : Go to the next question.

  2. Do you want infrastructure and workload monitoring, as well as proactive issue detection and troubleshooting recommendations?

     * **Yes** : See Identify and fix issues with VMware Aria Operations in this document.

     * **No** : Go to the next question.

  3. Do you want to track resource usage, set alerts, and receive notifications about virtual machine (VM) instance events using a Google Cloud product?

     * **Yes** : See View performance data or set alerts with Monitoring in this document.

     * **No** : See Monitor your environment with vCenter monitoring tools in this document.




### Forward syslog messages to a remote server

VMware Engine lets you forward syslog messages generated by your VMware environment to a remote syslog server. This lets you centralize your log data so that you can monitor and analyze your infrastructure.

For more information, see [Forwarding syslog messages to a remote server](https://docs.cloud.google.com/vmware-engine/docs/environment/howto-forward-syslog).

### Identify and fix issues with VMware Aria Operations

VMware Aria Operations is a VMware product that provides detailed insights into your VMware vCenter environments. VMware Aria Operations uses advanced analytics to help you identify issues, forecast usage, and recommend corrective actions to ensure optimal performance, availability, and efficiency in your virtual infrastructure.

For more information, see [Configuring VMware Aria Operations](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-vmware-aria-operations).

### View performance data or set alerts with Monitoring

You can use [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) to monitor performance data, as well as set alerts for specific events or errors, within your private clouds.

If you want to use Monitoring in your private clouds, you must first forward metrics from your private clouds by defining collectors, sources, and destinations in BindPlane. For more information, see [Setting up Monitoring with a standalone agent](https://docs.cloud.google.com/vmware-engine/docs/environment/howto-cloud-monitoring).

To monitor your private clouds, you can use one or both of the following Monitoring features described in this document:

  * To view a high-level overview of key resources, or view a more focused view of the usage of your resources, use Monitoring dashboards.

  * To receive an alert every time a specific event happens in your private clouds, use Monitoring alerts.




#### Use Monitoring dashboards

Monitoring dashboards help you monitor the performance of your infrastructure by aggregating information from multiple standalone agent sources. If you want to view the analytics of your private clouds with minimal setup and configuration, then use the predefined dashboards that Monitoring automatically installs for the resources in your project. Otherwise, if you want to view analytics from multiple sources or create a customized view of your infrastructure performance, use custom dashboards.

For more information, see [Dashboards overview](https://docs.cloud.google.com/monitoring/dashboards) in the Monitoring documentation.

#### Use Monitoring alerts

Monitoring alerts let you use metrics from your standalone agent integration to trigger a notification based on custom thresholds or incidents. For example, you can set up Monitoring to send you an email every time a VM is created in your private cloud.

For more information, see [Alerting overview](https://docs.cloud.google.com/monitoring/alerts) in the Monitoring documentation.

### Monitor your environment with vCenter monitoring tools

vCenter gives you a comprehensive suite of tools to monitor and troubleshoot your VMware environment. You can use vCenter monitoring tools to gain insight into the performance, health, and capacity of your private clouds, as well as to set alerts using log files.

For more information, see [About vSphere Monitoring and Performance](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.monitoring.doc/GUID-A8B06BE0-E5FC-435C-B12F-A31618B21E2C.html) in the VMware documentation.

### Decision tree

The following diagram guides you through the factors to consider when deciding your monitoring method for your VMware Engine private clouds:

![Decision tree to choose a monitoring method for your private clouds.](https://docs.cloud.google.com/vmware-engine/images/gcve-monitor-decision-tree.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
