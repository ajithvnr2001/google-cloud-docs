---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/restrict-resources-access-by-namespace/
title: Enable access and view cluster resources by namespace \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:43:10.067236+00:00
---

# Enable access and view cluster resources by namespace  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/restrict-resources-access-by-namespace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Enable access and view cluster resources by namespace Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to restrict view access to cluster resources based on specific namespaces, and how users with restricted access can view these resources on the Google Cloud console. This scenario is common for organizations that run [multi-tenant](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multitenancy-overview) Google Kubernetes Engine (GKE) clusters.

This page is for Security specialists and Operators who want to provide users with restricted access to cluster resources for specific namespaces. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before reading this page, ensure that you're familiar with the following namespace concepts:

  * [Organizing Kubernetes with Namespaces](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-organizing-with-namespaces)
  * [Enterprise multi-tenancy best practices](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/enterprise-multitenancy#create-namespaces)



## Enable namespace-restricted access to cluster resources

You can use tenant permissions to restrict user interactions with the cluster on the Google Cloud console. You grant users the [`roles/container.clusterViewer`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/iam#predefined) IAM permission as well as [role-based access control (RBAC) permissions](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control) to view resources in specific namespaces.

**Note:** By default, the Google Cloud console expects users to have view access to all namespaces in all clusters (that is, users have the `roles/container.viewer` IAM permission). If the user only has access to specific namespaces, they should follow the steps described in View namespace-restricted resources in the Google Cloud console.

To learn more about using namespaces, see [Organizing Kubernetes with Namespaces](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-organizing-with-namespaces) and [Enterprise multi-tenancy best practices](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/enterprise-multitenancy#create-namespaces).

## View namespace-restricted resources in the Google Cloud console

If you have limited IAM or RBAC permissions and want to view namespace-restricted resources on the Google Cloud console, follow these steps:

  1. Go to the **Workloads** page in the Google Cloud console.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload/overview)

  2. Click the **Namespace** drop-down list.

  3. Click add **Add filter**.

  4. Enter the namespace you want to access, then click **Save**.

  5. Click **OK**.




The list will be filtered to show the selected namespace.

## Share saved views

You can also save the filtered list as a named _saved view_. The saved view will persist across sessions, and can be shared with other users.

To share a saved view, follow these steps:

  1. Select the saved view from the **Saved view** drop-down list.
  2. Next to the **Saved view** drop-down list, click more_vert, then click **Share**.
  3. Click content_copy to copy the URL in the **Share view** dialog. You can share this URL with other users who need access to the same cluster and namespaces.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
