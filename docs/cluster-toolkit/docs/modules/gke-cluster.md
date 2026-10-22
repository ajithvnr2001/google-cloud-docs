---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-cluster/
title: Create a GKE cluster \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:24.681248+00:00
---

# Create a GKE cluster  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Create a GKE cluster Stay organized with collections  Save and categorize content based on your preferences. 

The `gke-cluster` module lets you create a Google Kubernetes Engine (GKE) cluster. By using this module, you automate the provisioning of managed Kubernetes environments. This automation provides a scalable and secure foundation for your containerized workloads.

For the complete list of inputs and outputs for this module, see the [`gke-cluster` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/scheduler/gke-cluster#inputs) page in the Google Kubernetes Engine GitHub repository.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Google Kubernetes Engine. For installation instructions, see [Set up Google Kubernetes Engine](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. For a working example of a blueprint configured for GKE, see the [`examples/hpc-gke.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/hpc-gke.yaml) file. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).
  * To view a complete list of blueprints that support GKE, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page, click the **Select scheduler** menu and then select **GKE**.
  * The `gke-cluster` module does not create a full active cluster or execute the workload. It provisions a managed GKE cluster to host your containerized workloads.



### Required roles

To get the permissions that you need to create the GKE cluster and node pools, ask your administrator to grant you the following IAM roles on your project: 

  * [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a GKE cluster

The following example creates a GKE cluster and a Virtual Private Cloud (VPC) network that supports GKE. To view the complete configuration, see the [`examples/hpc-gke.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/hpc-gke.yaml) example on GitHub.
    
    
      - id: network1
        source: modules/network/vpc
        settings:
          subnetwork_name: gke-subnet
          secondary_ranges:
            gke-subnet:
            - range_name: pods
              ip_cidr_range: 10.4.0.0/14
            - range_name: services
              ip_cidr_range: 10.0.32.0/20
    
      - id: gke_cluster
        source: modules/scheduler/gke-cluster
        use: [network1]
    
    

### Create a VPC network

This module creates a [VPC-native cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips). A VPC-native cluster uses alias IP addresses, which require the subnetwork to have secondary IP address ranges for pods and services. In the preceding example, the `vpc` module creates these secondary ranges. By default, the `gke-cluster` module searches for ranges that have the `pods` and `services` names. You can configure these names by using the `pods_ip_range_name` setting and the `services_ip_range_name` setting.

### Configure multi-networking

To activate [multi-networking](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-bandwidth-gpudirect-tcpx#create-gke-environment), supply the `multivpc` module to the `gke-cluster` module. When you supply a `multivpc` module, the cluster turns on multi-networking and [GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2).

The following example demonstrates how to configure this relationship:
    
    
      - id: network
        source: modules/network/vpc
        settings:
          subnetwork_name: gke-subnet
          secondary_ranges:
            gke-subnet:
            - range_name: pods
              ip_cidr_range: 10.4.0.0/14
            - range_name: services
              ip_cidr_range: 10.0.32.0/20
    
      - id: multinetwork
        source: modules/network/multivpc
        settings:
          network_name_prefix: multivpc-net
          network_count: 8
          global_ip_address_range: 172.16.0.0/12
          subnetwork_cidr_suffix: 16
    
      - id: gke-cluster
        source: modules/scheduler/gke-cluster
        use: [network, multinetwork]
        settings:
          cluster_name: $(vars.deployment_name)
    
    

To view a complete multi-networking implementation, see the [`examples/gke-a3-megagpu/gke-a3-megagpu.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a3-megagpu/gke-a3-megagpu.yaml) example on GitHub.

## Enable the GKE Inference Gateway

If you set the `enable_inference_gateway` setting to `true`, then the module turns on the `HttpLoadBalancing` add-on and deploys the Inference Gateway custom resource definitions (CRDs). To use this feature, your VPC network must contain a subnetwork that has the `purpose` attribute set to a value of `REGIONAL_MANAGED_PROXY`.

For more information, see [About GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/serve-with-gke-inference-gateway).

## Enable CSI drivers for storage

The `gke-cluster` module supports the activation of Container Storage Interface (CSI) drivers by using the following settings:

  * `enable_filestore_csi`: Supports [Filestore](https://docs.cloud.google.com/filestore/docs) storage.
  * `enable_gcsfuse_csi`: Supports [Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/gcs-fuse) storage.
  * `enable_managed_lustre_csi`: Supports [Google Cloud Managed Lustre](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managed-lustre) storage.



If you plan to use specific storage modules in your deployment, you must set the corresponding CSI driver setting to `true`.

## Define the GKE version

By default, the `gke-cluster` module provisions clusters using the `1.31.` version prefix. If your workload requires a different GKE version, you must override this default behavior by specifying a new prefix in the `version_prefix` setting.

## Limitations

The current implementation of creating GKE clusters in Google Kubernetes Engine using this module has the following limitations:

  * Autopilot is disabled.
  * Auto-provisioning of new node pools is disabled.
  * Network policies are unsupported.
  * General add-on configuration is unsupported.
  * Only regional clusters are supported.



## What's next

  * For the complete list of inputs and outputs for this module, see the [`gke-cluster` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/scheduler/gke-cluster#inputs) page in the Google Kubernetes Engine GitHub repository.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
