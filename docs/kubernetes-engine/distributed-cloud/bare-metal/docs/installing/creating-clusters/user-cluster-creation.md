---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/user-cluster-creation/
title: Create user clusters \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:43.247655+00:00
---

# Create user clusters  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/user-cluster-creation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Create user clusters Stay organized with collections  Save and categorize content based on your preferences. 

In Google Distributed Cloud, user clusters run your workloads, and in a [multi-cluster architecture](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/create-clusters-overview), user clusters are created and managed by an admin cluster.

Once you've created an admin cluster, calling the `bmctl create config` command creates a YAML file you can edit to define your user cluster. To apply the configuration and create the user cluster, use the `bmctl create cluster` command. Preflight checks are applicable to the user clusters created with `bmctl create cluster` command.

Keeping workloads off the admin cluster protects sensitive administrative data, like SSH keys stored in the admin cluster, from those who don't need access to that information. Additionally, keeping user clusters separate from each other provides good general security for your workloads.

## Prerequisites

  * Latest `bmctl` is downloaded (`gs://anthos-baremetal-release/bmctl/1.36.100-gke.144/linux-amd64/bmctl`) from Cloud Storage.
  * Working admin cluster with access to the cluster API server (the `controlPlaneVIP`).
  * Admin cluster nodes have network connectivity to all nodes on the target user cluster.
  * Workstation running `bmctl` has network connectivity to all nodes in the target user clusters.
  * The admin workstation can establish an SSH connection to each of the user cluster nodes.
  * Connect-register service account is configured on the admin cluster for use with Connect.



## Enable SELinux

If you want to enable SELinux to secure your containers, you must make sure that SELinux is enabled in `Enforced` mode on all your host machines. Starting with Google Distributed Cloud release 1.9.0 or later, you can enable or disable SELinux before or after cluster creation or cluster upgrades. SELinux is enabled by default on Red Hat Enterprise Linux (RHEL). If SELinux is disabled on your host machines or you aren't sure, see [Securing your containers using SELinux](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-selinux) for instructions on how to enable it.

Google Distributed Cloud supports SELinux in only RHEL systems.

## Create a user cluster configuration file

The configuration file for creating a user cluster is almost exactly the same as the one used for creating an admin cluster. The only difference is that you remove the local credentials configuration section to make the config a valid collection of Kubernetes resources. The configuration section is at the top of the file under the `bmctl configuration variables` section. For examples of user cluster configurations, see [User clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/config-samples#user_clusters) in the Cluster configuration samples.

By default, user clusters inherit their credentials from the admin cluster that manages them. You can selectively override some or all of these credentials.

  1. Create a user cluster configuration file with the `bmctl create config` command:
         
         bmctl create config -c USER_CLUSTER_NAME
         

For example, issue the following to create a configuration file for a user cluster called `user1`:
         
         bmctl create config -c user1
         

The file is written to `bmctl-workspace/user1/user1.yaml`. The generic path to the file is `bmctl-workspace/CLUSTER NAME/CLUSTER_NAME.yaml`.

  2. Edit the configuration file with the following changes:

     * Remove the local credentials file paths from the config:
           
           ...
             ~~gcrKeyPath : (path to Artifact Registry service account key)~~
             ~~sshPrivateKeyPath : (path to SSH private key, used for node access)~~
             ~~gkeConnectAgentServiceAccountKeyPath : (path to Connect agent service account key)~~
             ~~gkeConnectRegisterServiceAccountKeyPath : (path to Hub registration service account key)~~
             ~~cloudOperationsServiceAccountKeyPath : (path to Cloud Operations service account key)~~
           ...
           

     * Change the config to specify a cluster type of `user` instead of `admin`:
           
           ...
           spec:
             # Cluster type. This can be:
             #   1) admin:  to create an admin cluster. This can later be used to create
             #   user clusters.
             #   2) user:   to create a user cluster. Requires an existing admin cluster.
             #   3) hybrid: to create a hybrid cluster that runs admin cluster
             #   components and user workloads.
             #   4) standalone: to create a cluster that manages itself, runs user
             #   workloads, but does not manage other clusters.
             type: user
           ...
           

     * Register your clusters to a [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs) by specifying your project ID in the `gkeConnect.projectID` field. This project is referred to as the [fleet host project](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts#fleet-host-project).
           
           ...
           gkeConnect:
              projectID: my-project-123
           ...
           

       * Optionally, you can add [`gkeConnect.location`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#gkeconnect-location) to the cluster spec to specify the Google Cloud region in which the Fleet and the Connect services run. This regional membership restricts fleet service traffic to your region. If you include `gkeConnect.location` in the cluster spec, the region that you specify must be the same as the region configured in `clusterOperations.location`. If the regions aren't the same, cluster creation fails.
     * If the GKE On-Prem API is enabled in your Google Cloud project, all clusters in the project are [enrolled in the GKE On-Prem API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/enroll-cluster) automatically in the region configured in `clusterOperations.location`.

       * If you want to enroll all clusters in the project in the GKE On-Prem API, be sure to do the steps in [Before you begin](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/enroll-cluster#before_you_begin) to activate and use the GKE On-Prem API in the project.

       * If you don't want to enroll the cluster in the GKE On-Prem API, include this section and set `gkeOnPremAPI.enabled` to `false`. If you don't want to enroll any clusters in the project, disable `gkeonprem.googleapis.com` (the service name for the GKE On-Prem API) in the project. For instructions, see [Disabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#disabling).

     * Specify the IP address of the control plane node.
           
           ...
           # Sample control plane config
           controlPlane:
            nodePoolSpec:
              nodes:
              - address: 10.200.0.20
           ...
           

     * Ensure the admin and user cluster specifications for the load balancer VIPs and address pools are complementary, and don't overlap existing clusters. The following example shows a sample pair of admin and user cluster configurations, specifying load balancing and address pools:
           
           ...
           # Sample admin cluster config for load balancer and address pools
             loadBalancer:
               vips:
                 controlPlaneVIP: 10.200.0.49
                 ingressVIP: 10.200.0.50
               addressPools:
               - name: pool1
                 addresses:
                 - 10.200.0.50-10.200.0.70
           ...
           ...
           # Sample user cluster config for load balancer and address pools
           loadBalancer:
               vips:
                 controlPlaneVIP: 10.200.0.71
                 ingressVIP: 10.200.0.72
               addressPools:
               - name: pool1
                 addresses:
                 - 10.200.0.72-10.200.0.90
           ...
           

The rest of the user cluster configuration files are the same as the admin cluster config.

     * Specify the pod density of cluster nodes:
           
           ...
           # NodeConfig specifies the configuration that applies to all nodes in the cluster.
           nodeConfig:
             # podDensity specifies the pod density configuration.
             podDensity:
               # maxPodsPerNode specifies at most how many pods can be run on a single node.
               maxPodsPerNode: 110
           ...
           

For user clusters, allowable values for `maxPodsPerNode` are `32-250`. The default value if unspecified is `110`. Once the cluster is created, this value cannot be updated.

Pod density is also limited by your cluster's available IP resources. For details, see [Pod networking](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/network-reqs#pod_networking).




## Create the user cluster

Issue the `bmctl` command to apply the user cluster config and create the cluster:
    
    
    bmctl create cluster -c USER_CLUSTER_NAME --kubeconfig ADMIN_KUBECONFIG
    

Replace the following:

  * `USER_CLUSTER_NAME`: the cluster name created in the previous section.
  * `ADMIN_KUBECONFIG`: the path to the admin cluster kubeconfig file.



For example, for a user cluster named `user1`, and an admin cluster kubeconfig file with the path `kubeconfig bmctl-workspace/admin/admin-kubeconfig`, the command would be:
    
    
    bmctl create cluster -c user1 --kubeconfig bmctl-workspace/admin/admin-kubeconfig
    

## Sample user cluster configurations

For example user cluster configurations, see [User clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/config-samples#user_clusters) in the Cluster configuration samples.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
