---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/hybrid-cluster-creation/
title: Create hybrid clusters \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:16.362033+00:00
---

# Create hybrid clusters  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/hybrid-cluster-creation/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Create hybrid clusters Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/creating-clusters/hybrid-cluster-creation)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/hybrid-cluster-creation)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



In Google Distributed Cloud, hybrid clusters perform the dual role of an admin cluster and a user cluster. They run workloads, and at the same time, manage other clusters, and themselves.

Hybrid clusters eliminate the need to run a separate admin cluster in resource-constrained scenarios, and can provide highly available (HA) reliability. In an HA hybrid cluster, if one node fails, then others will take its place.

Hybrid clusters are different from standalone clusters in that they can also manage other clusters. Standalone clusters can't create or manage other clusters.

When you create hybrid clusters, there is some tradeoff between flexibility and security, however. Since hybrid clusters manage themselves, running workloads on the same cluster increases the risk of security exposure to sensitive administrative data, like SSH keys.

You create a hybrid cluster with a high availability (HA) control plane using the `bmctl` command. The `bmctl` command can be run on a separate workstation or on one of the hybrid cluster nodes.

## Prerequisites

  * Latest `bmctl` is downloaded (`gs://anthos-baremetal-release/bmctl/1.16.8/linux-amd64/bmctl`) from Cloud Storage.
  * Workstation running `bmctl` has network connectivity to all nodes in the target hybrid cluster.
  * Workstation running `bmctl` has network connectivity to the control plane VIP of the target hybrid cluster.
  * SSH key used to create the hybrid cluster is available to root, or there is SUDO user access on all nodes in the target hybrid cluster.
  * Connect-register service account is configured for use with Connect.



See the [Google Distributed Cloud quickstart](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/quickstart) for expanded step-by-step instructions for creating a hybrid cluster.

## Enable SELinux

If you want to enable SELinux to secure your containers, you must make sure that SELinux is enabled in `Enforced` mode on all your host machines. Starting with Google Distributed Cloud release 1.9.0 or later, you can enable or disable SELinux before or after cluster creation or cluster upgrades. SELinux is enabled by default on Red Hat Enterprise Linux (RHEL) and CentOS. If SELinux is disabled on your host machines or you aren't sure, see [Securing your containers using SELinux](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/configure-selinux) for instructions on how to enable it.

Google Distributed Cloud supports SELinux in only RHEL and CentOS systems.

## Log into gcloud and create a hybrid cluster config file

  1. Login to gcloud as a user using `gcloud auth application-default` login:
    
    gcloud auth application-default login
    

You need to have a Project Owner/Editor role to use the automatic API enablement and Service Account creation features, described below. You can also add the following IAM roles to the user: 
     * Service Account Admin
     * Service Account Key Admin
     * Project IAM Admin
     * Compute Viewer
     * Service Usage Admin
Alternatively, if you already have a service account with those roles, run: 
    
    export GOOGLE_APPLICATION_CREDENTIALS=JSON_KEY_FILE
    

JSON_KEY_FILE specifies the path to your service account JSON key file. 
  2. Get your Cloud project id to use with cluster creation:
    
    export CLOUD_PROJECT_ID=$(gcloud config get-value project)
    




### Create the hybrid cluster with `bmctl`

After you've logged into gcloud and have your project set up, you can create the cluster config file with the `bmctl` command. Note that in this example, all service accounts are automatically created by the `bmctl create config` command:
    
    
    bmctl create config -c HYBRID_CLUSTER_NAME --enable-apis \
        --create-service-accounts --project-id=CLOUD_PROJECT_ID
    

Here's an example to create a config file for a hybrid cluster called `hybrid1` associated with project ID `my-gcp-project`: 
    
    
    bmctl create config -c hybrid1 --create-service-accounts --project-id=my-gcp-project
    

The file is written to `bmctl-workspace/hybrid1/hybrid1.yaml`.

As an alternative to automatically enabling APIs and creating service accounts, you can also provide your existing service accounts with proper IAM permissions. Thie means you can skip the automatic service account creation in the previous step in the `bmctl` command:
    
    
    bmctl create config -c hybrid1
    

## Edit the cluster config file

Now that you have a cluster config file, edit it to make the following changes:

  1. Provide the SSH private key to access the hybrid cluster nodes:
         
         # bmctl configuration variables. Because this section is valid YAML but not a valid Kubernetes
         # resource, this section can only be included when using bmctl to
         # create the initial admin/hybrid cluster. Afterwards, when creating user clusters by directly
         # applying the cluster and node pool resources to the existing cluster, you must remove this
         # section.
         gcrKeyPath: bmctl-workspace/.sa-keys/my-gcp-project-anthos-baremetal-gcr.json
         sshPrivateKeyPath: /path/to/your/ssh_private_key
         gkeConnectAgentServiceAccountKeyPath: bmctl-workspace/.sa-keys/my-gcp-project-anthos-baremetal-connect.json
         gkeConnectRegisterServiceAccountKeyPath: bmctl-workspace/.sa-keys/my-gcp-project-anthos-baremetal-register.json
         cloudOperationsServiceAccountKeyPath: bmctl-workspace/.sa-keys/my-gcp-project-anthos-baremetal-cloud-ops.json
         

  2. Register your clusters to a [fleet](https://docs.cloud.google.com/anthos/fleet-management/docs). The project ID that you specified in the `bmctl create config` command is automatically added to the `gkeConnect.projectID` field in the cluster config file. This project is referred to as the [fleet host project](https://docs.cloud.google.com/anthos/fleet-management/docs/fleet-concepts#fleet-host-project).

     * If you created your config file, using the automatic API enablement and Service Account creation features, you can skip this step.
     * If you created the config file without using the automatic API enablement and Service Account creation features, reference the downloaded service account JSON keys in the corresponding `gkeConnectAgentServiceAccountKeyPath` and `gkeConnectRegisterServiceAccountKeyPath` fields of the cluster config file.
  3. Change the config to specify a cluster type of `hybrid` instead of `admin`:
         
         spec:
           # Cluster type. This can be:
           #   1) admin:  to create an admin cluster. This can later be used to create user clusters.
           #   2) user:   to create a user cluster. Requires an existing admin cluster.
           #   3) hybrid: to create a hybrid cluster that runs admin cluster components and user workloads.
           #   4) standalone: to create a cluster that manages itself, runs user workloads, but does not manage other clusters.
           type: hybrid
         

  4. Change the config to specify a multi-node, high availability control plane. You want to specify an odd number of nodes to be able to have a majority quorum for HA:
         
         # Control plane configuration
           controlPlane:
             nodePoolSpec:
               nodes:
               # Control plane node pools. Typically, this is either a single machine
               # or 3 machines if using a high availability deployment.
               - address: 10.200.0.4
               - address: 10.200.0.5
               - address: 10.200.0.6
         

**Note:** If you have an even number of nodes temporarily while adding or removing nodes for maintenance or replacement, your deployment maintains HA as long as you have enough quorum.
  5. Specify the pod density of cluster nodes:
         
         ....
         # NodeConfig specifies the configuration that applies to all nodes in the cluster.
         nodeConfig:
           # podDensity specifies the pod density configuration.
           podDensity:
             # maxPodsPerNode specifies at most how many pods can be run on a single node.
             maxPodsPerNode: 250
         ....
         

For hybrid clusters, allowable values for `maxPodsPerNode` are `32-250` for HA clusters and `64-250` for non-HA clusters. The default value for `maxPodsPerNode` if unspecified is `110`. Once the cluster is created, this value cannot be updated.

Pod density is also limited by your cluster's available IP resources. For details, see [Pod networking](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/network-reqs#pod_networking).




## Create the hybrid cluster with the cluster config

Use the `bmctl` command to deploy the cluster: 
    
    
    bmctl create cluster -c CLUSTER_NAME
    

CLUSTER_NAME specifies cluster name you created in the previous section.

The following shows an example of the command to create a config file for a cluster called `hybrid1`:
    
    
    bmctl create cluster -c hybrid1
    

## Sample hybrid cluster configurations

For example hybrid cluster configurations, see [Hybrid clusters](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/config-samples#hybrid_clusters) in the Cluster configuration samples.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
