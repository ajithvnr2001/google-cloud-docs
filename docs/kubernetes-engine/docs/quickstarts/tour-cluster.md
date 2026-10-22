---
url: https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/tour-cluster/
title: Explore your cluster and workload \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:12.116641+00:00
---

# Explore your cluster and workload  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/tour-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Explore your cluster and workload

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

View and learn about the some of the workload settings and resources that you deployed in one of our quickstarts.

This follow-up tutorial delves deeper into some Kubernetes concepts such as Pods and Services, though doesn't assume that you have previous Kubernetes experience.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/freetrial?redirectPath=/kubernetes/list/overview?walkthrough_id=kubernetes--tour-cluster)

* * *

## Before you begin

Ensure that you've followed the steps in one of these quickstarts to create a cluster and deploy a sample app:

  * [Create a cluster and deploy a workload in the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/create-cluster).
  * [Create a cluster and deploy a workload using Terraform](https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/create-cluster-using-terraform)



### Required roles

To get the permissions that you need to interact with clusters and workloads, ask your administrator to grant you the [Kubernetes Engine Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.viewer) (`roles/container.viewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View Pod details

In Kubernetes, a [Pod](https://kubernetes.io/docs/concepts/workloads/pods/) is the smallest deployable unit of computing that you can create and manage. Like all Kubernetes workloads, the sample application deployment consists of Pods (in this case, one Pod with no additional replicas) wrapping containerized applications (in this case, one container). In this section, we'll take a look at what you can learn in the Google Cloud console about the sample app's Pod.

  1. First, ensure that you're on the sample app's **Deployment details** page (you might still be there if you've just finished the previous tutorial). If you're not on that page:

     1. In the Google Cloud console, go to the GKE **Workloads** page.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload/overview)

     2. In the **Name** column, click the name of the app you deployed, **hello-world-app** (if you deployed with the Google Cloud console) or **example-hello-app-deployment** (for the Terraform deployment).

  2. In the **Overview** tab, you can view more details about the sample app workload, including:

     * **Replicas** : The number of Pod replicas that are currently running in your workload.

     * **Pod specification** : The version of this Deployment, and the sample app's container.

  3. The **Managed pods** table links to configuration data and performance metrics for each running Pod replica.




## View Services

A Kubernetes [Service](https://kubernetes.io/docs/concepts/services-networking/service/) is how you provide networking endpoints for a Pod or Pods. When you deployed your workload, you created a load balancing Service that directs external traffic to your workload. This Service is what let you access the sample app's web interface after you deployed the application.

To view your workload's Service:

  1. Go to the **Exposing services** table in the **Deployment details** page. This shows you any Services that your workload exposes.

  2. In the **Name** column of the **Exposing services** table, click the name of the example app's Service. The name is **hello-world-app-service** if you deployed the app in the Google Cloud console or **example-hello-app-loadbalancer** if you deployed with Terraform.

  3. In the **Service details** page, you can learn more about the Service, including:

     * The Service's **external endpoints** : the IP address or addresses that you can use to access the Service. You used this IP address to visit the app's web interface in the previous quickstart.
     * The **ports** the Service uses.
     * More details about the service's **load balancer** , including the cluster IP address that the load balancer sends traffic to. You can click the load balancer name to find even more information, such as its frontend and backend details.

**Where's the YAML?** The desired state of all Kubernetes objects is specified declaratively, typically using YAML — GKE is no different. To view the YAML specifications for the example deployment, click the **YAML** tab in the **Deployment details** or **Service details** page. Any changes you make to the deployment using the Google Cloud console are automatically reflected in the YAML. You can even edit the YAML in this view to make real-time changes, or download it if you want to adapt it for your own projects. 

## What's next

  * Try our more in-depth [Learning path: Scalable apps](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps).
  * Learn how to get started with real life cluster administration in our [Cluster administration overview](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-admin-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
