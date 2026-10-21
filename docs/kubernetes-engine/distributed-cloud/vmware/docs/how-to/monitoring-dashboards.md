---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/monitoring-dashboards/
title: Creating dashboards \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:19:50.084991+00:00
---

# Creating dashboards  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/monitoring-dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Creating dashboards Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to create a set of recommended custom dashboards for monitoring your clusters created in Google Distributed Cloud (software only) for VMware.

**Note:** If Cloud Monitoring is enabled in your project, a set of predefined dashboards are automatically available. See [Use predefined dashbboards](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/predefined-dashboards) for details. Only proceed with samples in this document if your needs are not covered by the predefined dashboards.

## Permissions for creating dashboards

To create dashboards, your Google Account must have the following [permissions](https://docs.cloud.google.com/monitoring/access-control#dashboards_2) to create dashboards:

  * `monitoring.dashboards.create`
  * `monitoring.dashboards.delete`
  * `monitoring.dashboards.update`



You'll have these permissions if your account has one of the following roles. You can check your permissions ([in the Google Cloud console](https://console.cloud.google.com/iam-admin/roles)):

  * `monitoring.dashboardEditor`
  * `monitoring.editor`
  * Project `editor`
  * Project `owner`



In addition, to use `gcloud` (gcloud CLI) to create dashboards, your Google Account must have the `serviceusage.services.use` permission.

Your account will have this permission if it has one of the following roles:

  * `roles/serviceusage.serviceUsageConsumer`
  * `roles/serviceusage.serviceUsageAdmin`
  * `roles/owner`
  * `roles/editor`
  * Project `editor`
  * Project `owner`



## Recommended dashboards

After you create a cluster (admin or user), a best practice is to create the following dashboards with Cloud Monitoring to let your operations team monitor cluster health:

  * Control plane uptime dashboard
  * Pod status dashboard
  * Node status dashboard
  * VM health status dashboard
  * Node utilization dashboard
  * Anthos utilization dashboard



If your cluster also runs Windows Server OS nodes, you can [create the following dashboards](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-guide-for-windows-server-os-node-pools#windows_monitoring_agent) to monitor the status of Windows nodes and Pods:

  * Windows node status dashboard
  * Windows pod status dashboard



The dashboards are automatically created during admin cluster installation if Cloud Monitoring is enabled.

This section describes how to create these dashboards. For more information about the dashboard creation process described in the following sections, see [Managing dashboards by API](https://docs.cloud.google.com/monitoring/dashboards/api-dashboard).

#### Create a control plane uptime dashboard

The control plane consists of the API server, scheduler, controller manager, and etcd. To monitor the status of the control plane, create a dashboard that monitors the state of these components.

  1. Download the dashboard configuration: [`control-plane-uptime.json`](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/samples/control-plane-uptime.json).

  2. Create a custom dashboard with the configuration file by running the following command:
         
         gcloud monitoring dashboards create --config-from-file=control-plane-uptime.json

  3. In the Google Cloud console, select **Monitoring** , or use the following button:

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  4. Select **Resources > Dashboards** and view the dashboard named **GKE on-prem control plane uptime**. The control plane uptime of each user cluster is collected from separate namespaces within the admin cluster. The **namespace_name** field is the user cluster name.

  5. Optionally create [alerting policies](https://docs.cloud.google.com/monitoring/alerts).

Click to see a sample dashboard.

![](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/dashboard-control-plane-uptime.png)




#### Create a Pod status dashboard

To create a dashboard that includes the phase of each Pod, and the restart times and resource usage of each container, perform the following steps.

  1. Download the dashboard configuration: [`pod-status.json`](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/samples/pod-status.json).

  2. Create a custom dashboard with the configuration file by running the following command:
         
         gcloud monitoring dashboards create --config-from-file=pod-status.json

  3. In the Google Cloud console, select **Monitoring** , or use the following button:

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  4. Select **Resources > Dashboards** and view the dashboard named **GKE on-prem pod status**.

  5. Optionally create [alerting policies](https://docs.cloud.google.com/monitoring/alerts).

Click to see a sample dashboard.

![](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/dashboard-pod-status.png)




#### Create a node status dashboard

To create an node status dashboard to monitor the node condition, CPU, memory and disk usage, perform the following steps:

  1. Download the dashboard configuration: [`node-status.json`](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/samples/node-status.json).

  2. Create a custom dashboard with the configuration file by running the following command:
         
         gcloud monitoring dashboards create --config-from-file=node-status.json

  3. In the Google Cloud console, select **Monitoring** , or use the following button:

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  4. Select **Resources > Dashboards** and view the dashboard named **GKE on-prem node status**.

  5. Optionally create [alerting policies](https://docs.cloud.google.com/monitoring/alerts).

Click to see a sample dashboard.

![](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/dashboard-node-status.png)




#### Create a VM health status dashboard

A VM health status dashboard monitors CPU, memory, and disk resource contention signals for VMs in the admin cluster and user clusters.

To create an VM health status dashboard:

  1. Make sure `stackdriver.disableVsphereResourceMetrics` is set to false. See [User cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#stackdriver-disablevsphereresourcemetrics-field).

  2. Download the dashboard configuration: [`vm-health-status.json`](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/samples/vm-health-status.json).

  3. Create a custom dashboard with the configuration file by running the following command:
         
         gcloud monitoring dashboards create --config-from-file=vm-health-status.json

  4. In the Google Cloud console, select **Monitoring** , or use the following button:

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  5. Select **Resources > Dashboards** and view the dashboard named **GKE on-prem VM health status**.

  6. Optionally create [alerting policies](https://docs.cloud.google.com/monitoring/alerts).

Click to see a sample dashboard.

![](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/dashboard-vm-health-status.png)




#### Create a node utilization dashboard

A node utilization dashboard shows the following utilization in the cluster:

  * Node CPU allocation ratio
  * Available vCPUs to schedule Kubernetes workload
  * Node memory allocation ratio
  * Available memory to schedule k8s workload
  * Node disk utilization ratio



To create a node utilization dashboard:

  1. Download the dashboard configuration: [`node-utilization.json`](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/samples/node-utilization.json).

  2. Use this configuration file to create a custom dashboard by running the following command:
         
         gcloud monitoring dashboards create --config-from-file=node-utilization.json

  3. In the Google Cloud console, select **Monitoring** , or use the following button:

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  4. Select **Resources > Dashboards** and view the dashboard named **GKE on-prem node utilization**.

  5. Optionally create [alerting policies](https://docs.cloud.google.com/monitoring/alerts). 




#### Create an Anthos Utilization Metering dashboard

An Anthos Utilization Metering dashboard shows CPU and memory utilization in the clusters by namespace and Pod labels.

To create an Anthos Utilization Metering dashboard:

  1. Download the dashboard configuration: [`anthos-utilization.json`](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/samples/anthos-utilization.json).

  2. Use this configuration file to create a custom dashboard by running the following command:
         
         gcloud monitoring dashboards create --config-from-file=anthos-utilization.json

  3. In the Google Cloud console, select **Monitoring** , or use the following button:

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  4. Select **Resources > Dashboards** and view the dashboard named **Anthos Utilization Metering**.

  5. Optionally create [alerting policies](https://docs.cloud.google.com/monitoring/alerts).

Click to see a sample dashboard.

![](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/dashboard-anthos-utilization.png)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
