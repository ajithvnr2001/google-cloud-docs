---
url: https://docs.cloud.google.com/workload-manager/docs/observe/sap/prerequisites/
title: Prerequisites for SAP observability \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:07:04.100116+00:00
---

# Prerequisites for SAP observability  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/observe/sap/prerequisites/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Prerequisites for SAP observability Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the prerequisites for setting up the observability service in Workload Manager that helps you monitor your SAP workloads running on Google Cloud.

Prerequisite | Description  
---|---  
**Enable APIs** | Enable the following APIs in your Google Cloud project:  


  * [Workload Manager API](https://console.cloud.google.com/apis/library/workloadmanager.googleapis.com)
  * [Cloud Monitoring API](https://console.cloud.google.com/apis/library/monitoring.googleapis.com)
  * [Cloud Logging API](https://console.cloud.google.com/apis/library/logging.googleapis.com)
  * [Cloud Asset API](https://console.cloud.google.com/apis/library/cloudasset.googleapis.com)

  
**Grant IAM roles and permissions to the service agent** | Grant the required roles and permissions to the Workload Manager service agent. For more information, see Workload Manager service agent roles and permissions.  
**Grant IAM roles and permissions to users** | Users who view the observability dashboards must have or be granted the required roles and permissions. For more information, see IAM roles and permissions for the user.  
**Configure each VM that runs the SAP system** | Grant required roles to the service account attached to the VM and configure access scopes. For more information, see Configure each VM to send the required information.  
**(Recommended) Install and configure Ops agent** | Install the Ops Agent and configure the agent to collect the infrastructure metrics. For more information, see Install and configure Ops Agent.  
  
## Enable the Workload Manager API

The Workload Manager API must be enabled in the project where you want to monitor your SAP workloads. For more information, see [Enable Workload Manager](https://docs.cloud.google.com/workload-manager/docs/enable#enable).

## Enable additional APIs

Workload Manager uses data stored in other cloud services. In addition to the Workload Manager API, you must enable the following APIs in each project:

  * Cloud Monitoring API
  * Cloud Logging API
  * Cloud Asset API



These APIs are checked automatically when accessing the observability service within Workload Manager. If they are not enabled, then users with the necessary permissions can enable them while accessing observability dashboards.

There are also a variety of APIs that are likely already enabled in order to run an SAP workload on Google Cloud. These APIs can vary based on your chosen configuration and workloads that are being run.

## Workload Manager service agent IAM permissions and roles

Workload Manager uses a service agent, which needs the necessary permissions to access metrics and information from Cloud Monitoring, Cloud Logging, and other information that is displayed on the observability dashboards for SAP.

The following IAM roles must be assigned to the Workload Manager service agent, which has the email [`service-PROJECT_NUMBER@gcp-sa-workloadmanager.iam.gserviceaccount.com`](http://gcp-sa-workloadmanager.iam.gserviceaccount.com). Alternatively, you can create custom roles that contain the necessary permissions and assign them to the Workload Manager service agent.

**IAM role** | **Required IAM permissions**  
---|---  
Workload Manager service agent | 

  * `workloadmanager.insights.listSapSystems`
  * `serviceusage.services.use`
  * `cloudasset.assets.listResource`
  * `cloudasset.assets.listIamPolicy`
  * `cloudasset.assets.listOrgPolicy`
  * `cloudasset.assets.listOSInventories`
  * `cloudasset.assets.listAccessPolicy`
  * `serviceusage.services.use`

  
  
When navigating to the observability dashboard, Workload Manager checks if the Workload Manager service agent has the required role. Users who have the necessary permissions can grant the missing roles.

## IAM roles and permissions for the user

To view systems and workloads in the observability dashboards of Workload Manager, you need to grant the following IAM roles to the user.

**IAM role** | **Required IAM permissions**  
---|---  
Workload Manager Workload Viewer | 

  * `resourcemanager.projects.get`
  * `resourcemanager.projects.list`
  * `workloadmanager.discoveredprofiles.get`
  * `workloadmanager.discoveredprofiles.list`
  * `workloadmanager.discoveredprofiles.getHealth`

  
  
In addition to the Workload Manager Workload Viewer role, the user must be granted the following roles to use all features in the observability service.

To view all the relevant observability information for SAP, grant the following roles:

  * Monitoring Viewer (`roles/monitoring.viewer`)
  * Logs Viewer (`roles/logging.viewer`)



To create custom dashboards, grant the following role:

  * Monitoring Editor (`roles/monitoring.editor`)



Additional permissions might be required to use the optional features. For example, the Application and Database dashboards include a list of VMs in each layer and a link to SSH, but permissions for SSH connection must be granted in addition to other roles.

## Configure each VM to send the required information

The following steps must be completed on each Compute Engine VM in an SAP system that you want to include on the observability dashboards.

### Service account

The service account that is attached to each VM instance needs to have the following IAM roles in order to call the required Google Cloud APIs for the agents to collect and send the necessary information.

**IAM role name** | **IAM role**  
---|---  
Compute Viewer | `roles/compute.viewer`  
Monitoring Viewer | `roles/monitoring.viewer`  
Monitoring Metric Writer | `roles/monitoring.metricWriter`  
Secret Manager Secret Accessor* | `roles/secretmanager.secretAccessor`  
Workload Manager Insights Writer | `roles/workloadmanager.insightWriter`  
  
*Only required on SAP HANA instances and if you are storing the necessary read-access credentials using Secret Manager. This role is not required on non-HANA instances or on HANA instances if authenticating using `hdbuserstore` keys.

### API access scope

If you attach the Compute Engine default service account to the VMs, you must set the access scope that controls the level of access the VM has to Cloud APIs.

[Verify that the Access Scope](https://docs.cloud.google.com/compute/docs/instances/change-service-account#changeserviceaccountandscopes) on any instance using the Compute Engine default service account is either set to **Allow full access to all Cloud APIs** or has access to the following APIs at a minimum if you are controlling using the **Set access for each API** option:

**API** | **Access required**  
---|---  
Compute Engine API | Read-only or Read Write  
Monitoring API | Write Only or Full  
Logging API | Write Only or Full  
Cloud Platform | Enabled  
  
## Install and configure Ops Agent

To collect the underlying infrastructure metrics and to send these metrics to Cloud Monitoring and Cloud Logging for observability, you must [install the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/install-index) on every VM that runs your SAP system.

Although the Ops Agent isn't required for calculating the system health of your SAP workload, Google Cloud recommends installing it because it powers the following widgets on the observability dashboard:

  * **Top Processes by Memory**
  * **Memory Usage per VM**
  * **Swap Utilization**
  * **Swap I/O Operations**



After installation, configure the Ops Agent's `hostmetrics` settings. The default collection interval for host metrics is `60s`. For more information, see [Changing the collection interval in the metrics receivers](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration#receiver-hostmetrics-metrics).

**Note:** To avoid incurring costs for additional Cloud Monitoring features that you might not want to use, disable those features in Ops Agent.

## What's next

  * Learn how to [configure Agent for SAP for observability](https://docs.cloud.google.com/workload-manager/docs/observe/sap/configure-agent).
  * Learn how to [observe an SAP workload](https://docs.cloud.google.com/workload-manager/docs/observe/sap/view-dashboards).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
