---
url: https://docs.cloud.google.com/compute/docs/vm-extensions/monitor-vm-extensions/
title: Monitor VM extensions \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:36.513579+00:00
---

# Monitor VM extensions  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/vm-extensions/monitor-vm-extensions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Monitor VM extensions Stay organized with collections  Save and categorize content based on your preferences. 

Monitoring the health and performance of your VM extensions helps you manage resource usage and resolve issues across your fleet of Compute Engine instances. You can use Cloud Monitoring dashboards to visualize resource usage such as CPU or memory consumption, and configure alerting policies to receive notifications when an event, such as an installation failure, occurs.

This document describes how to monitor VM extensions managed by VM Extension Manager on your Compute Engine instances by using Cloud Monitoring, and helps you do the following:

  * Understand the available metrics for VM extensions
  * Build custom monitoring dashboards
  * Set up alerting policies



## Before you begin

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




## Before you begin

Before monitoring your extensions, ensure that you have completed the following:

  * [Install VM extensions](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy) by creating extension policies.
  * Review the basics about [VM Extension Manager](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager).
  * Review [Monitoring retention periods](https://docs.cloud.google.com/monitoring/quotas#data_retention_policy) and [Monitoring pricing](https://cloud.google.com/stackdriver/pricing#monitoring-costs).



## Required IAM roles

To get the permissions that you need to monitor metrics and create dashboards, ask your administrator to grant you the following IAM roles on your project.

To get the permissions that you need to monitor metrics and manage dashboards, ask your administrator to grant you the following IAM roles: 

  * To view metrics and dashboards: [](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer)[Monitoring Viewer](https://docs.cloud.google.com/monitoring/access-control#monitoring.viewer) (`roles/monitoring.viewer`) on the project 
  * To create and manage dashboards and alerting policies: [](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor)[Monitoring Editor](https://docs.cloud.google.com/monitoring/access-control#monitoring.editor) (`roles/monitoring.editor`) on the project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to monitor metrics and manage dashboards. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to monitor metrics and manage dashboards:

  * To view dashboards: `monitoring.dashboards.get` on the project 
  * To create dashboards: `monitoring.dashboards.create` on the project 
  * To set up alerts: `monitoring.alertPolicies.create` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

## Available metrics for VM extensions

The following metrics are available for monitoring your VM extensions in Monitoring:

Metric name | Metric type | Description  
---|---|---  
VM Extension Enforcement Status | `compute.googleapis.com/vm_extensions/extension/enforcement_status` | The enforcement status of a Compute Engine VM extension. Labels include `extension_name` and `status`. For a list of extension names, see [supported extensions](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#supported-extensions). Possible values for `status` are the following:

  * `ENFORCEMENT_STATE_UNSPECIFIED`
  * `INSTALLING`
  * `INSTALL_FAILED`
  * `INSTALLED`
  * `ROLLING_BACK`
  * `ROLLBACK_FAILED`
  * `ROLLED_BACK`
  * `INCOMPATIBLE`
  * `REMOVING`
  * `SERVICE_DISABLED`
  * `APPLYING_CONFIG`

  
VM Extension Health Status | `compute.googleapis.com/vm_extensions/extension/health_status` | The health status of a VM extension. Labels include `extension_name` and `status`. For a list of extension names, see [supported extensions](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#supported-extensions). Possible values for `status` are the following: 

  * `HEALTH_STATUS_UNSPECIFIED`
  * `STARTING`
  * `RUNNING`
  * `STOPPING`
  * `STOPPED`
  * `CRASHED`

  
VM Extension CPU Max Usage | `compute.googleapis.com/vm_extensions/extension/cpu/max_usage` | Max CPU time used by the VM extension expressed as a percentage.  
VM Extension Memory Max Used Bytes | `compute.googleapis.com/vm_extensions/extension/memory/used_bytes` | Max memory usage of the VM extension in bytes.  
  
## Build custom monitoring dashboards

You can build Monitoring dashboards with the most relevant VM extension charts for your use case. To add a chart to a dashboard, follow these steps:

  1. In the Google Cloud console, select **Monitoring** : 

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. In the navigation pane, select **Dashboards**.
  3. Click **Create dashboard**.
  4. Click **Add widget**.
  5. In the **Add widget** window, for **Data** , select **Metric**.
  6. To select the metric, expand the **Select a metric** menu and then do the following: 
     1. For the **Active resources** , select **VM Instance**.
     2. For the **Metric category** , select **Vm_extensions**.
     3. For the **Metric** , select a metric, such as **VM Extension Health Status**. For a list of available metrics, see Available metrics for monitoring VM extensions.
     4. Click **Apply**.



You can add as many charts to the dashboard as you like. For more information, see [Create and manage custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards).

## Set up alerting policies

Monitoring lets you create alerts and receive notifications when a metric crosses a specified threshold. For example, you can receive a notification when an extension's health status changes to `CRASHED`.

  1. In the Google Cloud console, select **Monitoring**. 

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. In the navigation pane, select **Alerting**.
  3. Click **Create policy**.
  4. On the **Create alerting policy** page, define the alerting conditions and notification channels. 
     1. To select the metric, expand the **Select a metric** menu and then do the following: 
        1. For the **Active resources** , select **VM Instance**.
        2. For the **Metric category** , select **Vm_extensions**.
        3. For the **Metric** , select a metric, such as **VM Extension Enforcement Status**. For a list of available metrics, see Available metrics for monitoring VM extensions.
        4. Click **Apply**.
     2. Configure the trigger conditions, such as checking if the `status` label is `INSTALL_FAILED`.
  5. Follow the prompts to add notification channels and name the policy.
  6. Click **Create policy**.



For more information, see [Create alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui).

## What's next

  * [View VM extension logs](https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-logs)
  * [Manage VM extensions by using extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions)
  * [Learn about Monitoring](https://docs.cloud.google.com/monitoring/docs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
