---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/hybrid-cluster-creation/
title: Create hybrid clusters \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:26.563483+00:00
---

# Create hybrid clusters  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/hybrid-cluster-creation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Create hybrid clusters Stay organized with collections  Save and categorize content based on your preferences. 

In Google Distributed Cloud, hybrid clusters perform the dual role of an admin cluster and a user cluster. They run workloads, and at the same time, manage other clusters, and themselves.

Hybrid clusters eliminate the need to run a separate admin cluster in resource-constrained scenarios, and can provide highly available (HA) reliability. In an HA hybrid cluster, if one node fails, then others will take its place.

Hybrid clusters are different from standalone clusters in that they can also manage other clusters. Standalone clusters can't create or manage other clusters.

When you create hybrid clusters, there is some tradeoff between flexibility and security, however. Since hybrid clusters manage themselves, running workloads on the same cluster increases the risk of security exposure to sensitive administrative data, like SSH keys.

You create a hybrid cluster with a high availability (HA) control plane using the `bmctl` command. The `bmctl` command can be run on a separate workstation or on one of the hybrid cluster nodes.

## Prerequisites

  * Latest `bmctl` is downloaded (`gs://anthos-baremetal-release/bmctl/1.36.100-gke.144/linux-amd64/bmctl`) from Cloud Storage.
  * Workstation running `bmctl` has network connectivity to all nodes in the target hybrid cluster.
  * Workstation running `bmctl` has network connectivity to the control plane VIP of the target hybrid cluster.
  * SSH key used to create the hybrid cluster is available to root, or there is SUDO user access on all nodes in the target hybrid cluster.
  * Connect-register service account is configured for use with Connect.



See the [Google Distributed Cloud quickstart](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/quickstart) for expanded step-by-step instructions for creating a hybrid cluster.

## Enable SELinux

If you want to enable SELinux to secure your containers, you must make sure that SELinux is enabled in `Enforced` mode on all your host machines. Starting with Google Distributed Cloud release 1.9.0 or later, you can enable or disable SELinux before or after cluster creation or cluster upgrades. SELinux is enabled by default on Red Hat Enterprise Linux (RHEL). If SELinux is disabled on your host machines or you aren't sure, see [Securing your containers using SELinux](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-selinux) for instructions on how to enable it.

Google Distributed Cloud supports SELinux in only RHEL systems.

## Log into gcloud and create a cluster configuration file

  1. Log into the gcloud CLI as a user using `gcloud auth application-default login`:
         
         gcloud auth application-default login
         

You need to have a Project Owner or Editor role to use the automatic API enablement and Service Account creation features, described in the following sections.

You can also add the following IAM roles to the user:

     * Service Account Admin
     * Service Account Key Admin
     * Project IAM Admin
     * Compute Viewer
     * Service Usage Admin

Alternatively, if you already have a service account with those roles, run:
    
    export GOOGLE_APPLICATION_CREDENTIALS=JSON_KEY_FILE
    

Replace `JSON_KEY_FILE` with the path of your service account JSON key file.

  2. Get your Google Cloud project ID to use with cluster creation:
         
         export CLOUD_PROJECT_ID=$(gcloud config get-value project)
         




### Create the cluster configuration file with `bmctl`

After you've logged into the gcloud CLI and have your project set up, you can create the cluster configuration file with the `bmctl` command.

To create a cluster configuration file:

  1. Run the following command creates the cluster configuration file, creates all needed service accounts, and enables all required APIs:
         
         bmctl create config -c CLUSTER_NAME</var> --enable-apis \
             --create-service-accounts --project-id=CLOUD_PROJECT_ID
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster you're creating.
     * `CLOUD_PROJECT_ID`: the ID of your Google Cloud project.

By default, the configuration file is written to `bmctl-workspace/CLUSTER_NAME/CLUSTER_NAME.yaml`.

If you've already enabled APIs and created service accounts, you can create configuration files without enabling APIs and creating service accounts. You also aren't required to use the `--project-id` flag. However, you'll need to specify credentials in your configuration file manually.

For more information about command options, see [create config](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/bmctl#create_config).




## Edit the cluster configuration file

Now that you have a cluster configuration file, edit it to make the following changes:

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
         

  2. Register your clusters to a [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs). The project ID that you specified in the `bmctl create config` command is automatically added to the `gkeConnect.projectID` field in the cluster configuration file. This project is referred to as the [fleet host project](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts#fleet-host-project).

     * If you created your configuration file, using the automatic API enablement and Service Account creation features, you can skip this step.
     * If you created the configuration file without using the automatic API enablement and Service Account creation features, reference the downloaded service account JSON keys in the corresponding `gkeConnectAgentServiceAccountKeyPath` and `gkeConnectRegisterServiceAccountKeyPath` fields of the cluster configuration file.
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

Pod density is also limited by your cluster's available IP resources. For details, see [Pod networking](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/network-reqs#pod_networking).




## Create the hybrid cluster with the cluster configuration

Use the `bmctl` command to create the cluster:
    
    
    bmctl create cluster -c CLUSTER_NAME
    

Replace `CLUSTER_NAME` with the name you used when you created the cluster configuration file the previous section.

The following shows an example of the command to create a cluster named `hybrid1`:
    
    
    bmctl create cluster -c hybrid1
    

## Sample hybrid cluster configurations

For example hybrid cluster configurations, see [Hybrid clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/config-samples#hybrid_clusters) in the Cluster configuration samples.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
