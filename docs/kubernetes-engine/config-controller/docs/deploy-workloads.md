---
url: https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/deploy-workloads/
title: Deploy third-party workloads on Config Controller \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:10.131309+00:00
---

# Deploy third-party workloads on Config Controller  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/deploy-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Controller ](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/overview)



Send feedback 

#  Deploy third-party workloads on Config Controller Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to deploy your own workloads on Config Controller clusters.

This page is for IT administrators and Operators who manage the lifecycle of the underlying tech infrastructure and plan capacity, and deploy apps and services to production. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Before you begin

Before you start, make sure you have performed the following tasks:

  1. Set up [Config Controller](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/setup).
  2. If your Config Controller cluster is on a GKE version earlier than version 1.27, [upgrade your cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrading_the_cluster) to version 1.27 or later.



## Enable node auto-provisioning on Standard clusters

You must enable [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning) to deploy your own workloads on Config Controller clusters. This allows for workload separation between your workloads and the Google-managed workloads installed by default on Config Controller clusters.

If you use Autopilot clusters, you don't need to enable node auto-provisioning because GKE automatically manages node scaling and provisioning.

### gcloud

To enable node auto-provisioning, run the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        **--enable-autoprovisioning** \
        --min-cpu MINIMUM_CPU \
        --min-memory MIMIMUM_MEMORY \
        --max-cpu MAXIMUM_CPU \
        --max-memory MAXIMUM_MEMORY \
        --autoprovisioning-scopes=https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/devstorage.read_only
    

Replace the following:

  * `CLUSTER_NAME`: the name of your Config Controller cluster.
  * `MINIMUM_CPU`: the minimum number of cores in the cluster.
  * `MINIMUM_MEMORY`: the minimum number of gigabytes of memory in the cluster.
  * `MAXIMUM_CPU`: the maximum number of cores in the cluster.
  * `MAXIMUM_MEMORY`: the maximum number of gigabytes of memory in the cluster.



### Console

To enable node auto-provisioning, perform the following steps:

  1. Go to the **Google Kubernetes Engine** page in Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click the name of the cluster.

  3. In the **Automation** section, for **Node auto-provisioning** , click edit **Edit**.

  4. Select the **Enable node auto-provisioning** checkbox.

  5. Set the minimum and maximum CPU and memory usage for the cluster.

  6. Click **Save changes**.




For more information on configuring node auto-provisioning, such as setting defaults, see [Configure node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning).

## Deploy your workload

When you deploy your workloads, Config Controller automatically enables GKE Sandbox to provide an extra layer of security to prevent untrusted code from affecting the host kernel on your cluster nodes. For more information, see [About GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods).

You can deploy a workload by writing a workload manifest file and then running the following command:
    
    
    kubectl apply -f WORKLOAD_FILE

Replace `WORKLOAD_FILE` with the manifest file, such as `my-app.yaml`.

Confirm that your workload is running on the auto-provisioned nodes:

  1. Get the list of nodes created for your workload:
         
         kubectl get nodes

  2. Inspect a specific node:
         
         kubectl get nodes NODE_NAME -o yaml

Replace `NODE_NAME` with the name of the node that you want to inspect.




## Limitations

  * GKE Sandbox: GKE Sandbox works well with many applications, but not all. For more information, see [GKE Sandbox limitations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods#limitations).
  * Control plane security: when granting permission for your workloads, use the principle of least privilege to grant only the permissions that you need. If your workload becomes compromised, the workload can use overly-permissive permissions to change or delete Kubernetes resources.
  * Control plane availability: if your workloads cause increased traffic in a short time, the cluster control plane might become unavailable until the traffic decreases.
  * Control plane resizing: GKE automatically resizes the control plane as needed. If your workload causes a large load increase (for example, installing thousands of CRD objects), GKE's automatic resizing might not be able to keep up with the load increase.
  * Quotas: when deploying workloads, you should be aware of GKE's [quotas and limits](https://docs.cloud.google.com/kubernetes-engine/quotas) and not exceed them.
  * Network access to control plane and nodes: Config Controller uses private nodes with Master Authorized Networks Enabled, Private Endpoint Enabled, and Public Access Disabled. For more information, see [GKE network security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#restrict_network_access_to_the_control_plane_and_nodes).



## What's next

  * Learn more about Config Controller best practices: [Config Controller scalability](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/scalability), [Config Controller sharding](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/sharding), and [Configuring Config Controller for high availability](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/availability)
  * [Troubleshoot Config Controller](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/troubleshoot)
  * [Monitor Config Controller](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/monitor)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
