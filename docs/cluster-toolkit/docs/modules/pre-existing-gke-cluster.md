---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/pre-existing-gke-cluster/
title: Use an existing GKE cluster \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:32:40.778690+00:00
---

# Use an existing GKE cluster  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/pre-existing-gke-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Use an existing GKE cluster Stay organized with collections  Save and categorize content based on your preferences. 

The `pre-existing-gke-cluster` module lets you discover a Google Kubernetes Engine (GKE) cluster that already exists in Google Cloud. By using this module, you can extract cluster attributes to uniquely identify the cluster for use by other modules. The module outputs align with the [`gke-cluster`](https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-cluster) module, which lets you use the `pre-existing-gke-cluster` module as a direct substitute.

For the complete list of inputs and outputs for this module, see the [`pre-existing-gke-cluster` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/scheduler/pre-existing-gke-cluster#inputs) page in the Cluster Toolkit GitHub repository.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. To view a working example of a blueprint configured for the `pre-existing-gke-cluster` module, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page, click the **Select scheduler** menu and then select **GKE**. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).



### Required roles

To get the permissions that you need to discover the existing GKE cluster, ask your administrator to grant you the [Kubernetes Engine Cluster Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.clusterViewer) (`roles/container.clusterViewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Use an existing GKE cluster

The following example demonstrates how to discover an existing GKE cluster named `my-gke-cluster` in the `us-central1` region.
    
    
    - id: existing-gke-cluster
      source: modules/scheduler/pre-existing-gke-cluster
      settings:
        project_id: $(vars.project_id)
        cluster_name: my-gke-cluster
        region: us-central1
    
    - id: compute_pool
      source: modules/compute/gke-node-pool
      use: [existing-gke-cluster]
    
    

By using the `use` keyword, the `gke-node-pool` module accepts the `cluster_id` input variable. This variable identifies the existing GKE cluster that hosts the new GKE node pool.

**Note:** The module infers the `project_id` setting and the `region` setting from the deployment variables of the same name. We include them in the preceding example for clarity.

### Configure multi-networking

To create network objects in your GKE cluster, you can supply a [`multivpc` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/multivpc) to the `pre-existing-gke-cluster` module instead of applying a manifest manually.
    
    
      - id: network
        source: modules/network/vpc
    
      - id: multinetwork
        source: modules/network/multivpc
        settings:
          network_name_prefix: multivpc-net
          network_count: 8
          global_ip_address_range: 172.16.0.0/12
          subnetwork_cidr_suffix: 16
    
      - id: existing-gke-cluster
        source: modules/scheduler/pre-existing-gke-cluster
        use: [multinetwork]
        settings:
          # Multi-networking must be enabled in advance during cluster creation.
          cluster_name: $(vars.deployment_name)
    
    

## What's next

  * For the complete list of inputs and outputs for this module, see the [`pre-existing-gke-cluster` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/scheduler/pre-existing-gke-cluster#inputs) page in the Cluster Toolkit GitHub repository.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
