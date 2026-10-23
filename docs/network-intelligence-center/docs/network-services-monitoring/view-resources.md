---
url: https://docs.cloud.google.com/network-intelligence-center/docs/network-services-monitoring/view-resources/
title: View resources and metrics \u00a0|\u00a0 Network Intelligence Center - Network Services Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:30.282056+00:00
---

# View resources and metrics  |  Network Intelligence Center - Network Services Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/network-services-monitoring/view-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Network Services Monitoring ](https://docs.cloud.google.com/network-intelligence-center/docs/network-services-monitoring)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/network-services-monitoring/overview)



#  View resources and metrics Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to view resources such as Google Kubernetes Engine services and their associated metrics in Network Services Monitoring.

## Before you begin

To view resources and metrics in Network Services Monitoring, complete the following steps.

### Enable ambient metrics in GKE

To generate and collect ambient metrics, enable ambient networking and enable metrics generation (`ambient-network-metrics=enabled`) by following steps in [Prepare GKE ambient networking](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-ambient-networking).

### Grant required roles and permissions

To get the permissions that you need to view resources and resource details in Network Services Monitoring, ask your administrator to grant you the following IAM roles on your project: 

  * View discovered resources: [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`) 
  * View App Hub details and GKE details: 
    * [App Hub Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.viewer) (`roles/apphub.viewer`)
    * [Kubernetes Engine Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.viewer) (`roles/container.viewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to view resources and resource details in Network Services Monitoring. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view resources and resource details in Network Services Monitoring:

  * View discovered resources: 
    * `resourcemanager.projects.get`
    * `monitoring.timeSeries.list`
  * View App Hub details and GKE details: 
    * `apphub.discoveredServices.get`
    * `apphub.services.list`
    * `container.clusters.get`
    * `container.services.get`
    * `container.deployments.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View resources and metrics

In Network Services Monitoring, you can view resources such as GKE services and analyze them by using their [associated network metrics](https://docs.cloud.google.com/network-intelligence-center/docs/network-services-monitoring/metrics-reference).

### View resources

To view all discovered resources, do the following:

  1. In the Google Cloud console, go to the **Network Services Monitoring** page.

[Go to Network Services Monitoring](https://console.cloud.google.com/net-intelligence/service-monitoring/active-services)

  2. View active and inactive resources:

     1. To view active resources, on the **Active Discovered Resources** tab, select a time interval. This tab lists resources that generated traffic within the selected interval.
     2. To view inactive resources, on the **Inactive Discovered Resources** tab, select a region and a time interval. This tab lists resources that are discovered by the App Hub API but didn't generate traffic within the selected interval.



### View resource details

To view metrics and metadata for a specific resource, do the following:

  1. On the **Active Discovered Resources** tab, click a resource name.

  2. On the **Overview** tab of the resource details page, view any of the following sections:

     * Service dependency map: view the visual mapping of inbound and outbound connections for the selected resource. To view traffic, click **Traffic** , and to view errors, click **Errors**.
     * **Inbound** and **Outbound** : click the **Inbound** or **Outbound** tab in the **Connections** table to inspect the specific sources or destinations for all of the resource's connections.
     * **Resource Details** : view resource metadata.
     * **Additional Diagnostics:** use links to Access logs, Application Monitoring, App Hub, Flow Analyzer, and VPC Flow Logs.
  3. To view time-series charts for inbound and outbound traffic, open connection count, and connection health, click the **Dashboard** tab and select a time interval. You can view additional time-series charts by clicking **Show more** in the **Connections** table or clicking the connection lines in the topology graph.




## What's next

  * Register services and workloads in [App Hub](https://docs.cloud.google.com/app-hub/docs/overview)
  * [Investigate applications, services, and workloads](https://docs.cloud.google.com/monitoring/docs/application-monitoring) in Application Monitoring



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
