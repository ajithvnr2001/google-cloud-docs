---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/admin-cluster-creation/
title: Create admin clusters \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:39.295963+00:00
---

# Create admin clusters  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/admin-cluster-creation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Create admin clusters Stay organized with collections  Save and categorize content based on your preferences. 

In Google Distributed Cloud, you set up admin clusters to manage other clusters securely. You can create, update, upgrade, or delete user clusters from admin clusters. The user clusters run workloads separately from administration, so sensitive information is protected.

Admin clusters managing multi-cluster workloads can provide highly available (HA) reliability. In an HA cluster, if one control plane node fails, other nodes will continue to work.

An admin cluster in a multi-cluster environment provides the best fundamental security. Because access to administration data is separated from workloads, those who access user workloads have no access to sensitive administrative data, like SSH keys and service account data. As a result, there is some trade-off between security and the resources required, since a separate admin cluster means you need dedicated resources for management and workloads.

You create an admin cluster using the `bmctl` command. After you create an admin cluster, you create [user clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/user-cluster-creation) to run workloads.

Prerequisites:

  * Latest `bmctl` is downloaded (`gs://anthos-baremetal-release/bmctl/1.36.100-gke.144/linux-amd64/bmctl`) from Cloud Storage.
  * Workstation running `bmctl` has network connectivity to all nodes in the target user clusters.
  * Workstation running `bmctl` has network connectivity to the cluster API server (control plane VIP).
  * SSH key used to create the Admin cluster is available to either `root` or a [non-root user with passwordless `sudo` privileges](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/update-clusters#set_a_login_user) on all nodes in the target admin cluster.
  * Connect-register service account is configured for use with Connect.



See the Google Distributed Cloud [quickstart](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/quickstart) for expanded step-by-step instructions for creating a _hybrid_ cluster. Creating an admin cluster is similar to creating a hybrid cluster, except you don't run workloads on the admin cluster.

## Enable SELinux

If you want to enable SELinux to secure your containers, you must make sure that SELinux is enabled in `Enforced` mode on all your host machines. Starting with Google Distributed Cloud release 1.9.0 or later, you can enable or disable SELinux before or after cluster creation or cluster upgrades. SELinux is enabled by default on Red Hat Enterprise Linux (RHEL). If SELinux is disabled on your host machines or you aren't sure, see [Securing your containers using SELinux](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-selinux) for instructions on how to enable it.

Google Distributed Cloud supports SELinux in only RHEL systems.

## Log into the gcloud CLI and create an admin cluster config file

  1. Set the default credentials that Google Distributed Cloud can use to create the cluster with the following command:
         
         gcloud auth application-default login
         

  2. To use the automatic API enablement and service account creation features in this page, grant the Project Owner role to that principal. If the principal can't have the Project Owner role, complete the next step.

  3. To ensure the cluster creation can succeed without granting the Project Owner role, add the following IAM roles to the principal:

     * Service Account Admin
     * Service Account Key Admin
     * Project IAM Admin
     * Compute Viewer
     * Service Usage Admin

If the principal is a service account with those roles, you can run:
    
    export GOOGLE_APPLICATION_CREDENTIALS=JSON_KEY_FILE
    

Replace `JSON_KEY_FILE` with the path to your service account's JSON key file.

  4. Get the ID of your Google Cloud project and store it in an environment variable to use it for cluster creation:
         
         export CLOUD_PROJECT_ID=$(gcloud config get-value project)
         




### Create an admin cluster config with `bmctl`

After you've logged into the gcloud CLI and have your project set up, you can create the cluster config file with the `bmctl` command.

**Note:** New clusters must be registered to a [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs). Preflight checks will evaluate Google Cloud connectivity, enabled APIs, and role permissions for service accounts.

In the following example, all service accounts are automatically created by the `bmctl create config` command:
    
    
    bmctl create config -c ADMIN_CLUSTER_NAME --enable-apis \
        --create-service-accounts --project-id=CLOUD_PROJECT_ID
    

Replace the following:

  * ADMIN_CLUSTER_NAME: the name of the new cluster.
  * CLOUD_PROJECT_ID: your Google Cloud project ID or the `$CLOUD_PROJECT_ID` environment variable.



Here's an example to create a configuration file for a admin cluster called `admin1` associated with project ID `my-gcp-project`:
    
    
    bmctl create config -c admin1 --create-service-accounts --enable-apis --project-id=my-gcp-project
    

The file is written to `bmctl-workspace/admin1/admin1.yaml`.

As an alternative to automatically enabling APIs and creating service accounts, you can also provide your existing service accounts with proper IAM permissions. This means you can skip the automatic service account creation in the previous example in the `bmctl` command:
    
    
    bmctl create config -c admin1 --project-id=my-gcp-project
    

## Edit the cluster configuration file

Now that you have a cluster configuration file, edit it to make the following changes:

  1. Provide the SSH private key to access the admin cluster nodes:
         
         # bmctl configuration variables. Because this section is valid YAML but not a valid Kubernetes
         # resource, this section can only be included when using bmctl to
         # create the initial admin/admin cluster. Afterwards, when creating user clusters by directly
         # applying the cluster and node pool resources to the existing cluster, you must remove this
         # section.
         gcrKeyPath: bmctl-workspace/.sa-keys/my-gcp-project-anthos-baremetal-gcr.json
         sshPrivateKeyPath: /path/to/your/ssh_private_key
         gkeConnectAgentServiceAccountKeyPath: bmctl-workspace/.sa-keys/my-gcp-project-anthos-baremetal-connect.json
         gkeConnectRegisterServiceAccountKeyPath: bmctl-workspace/.sa-keys/my-gcp-project-anthos-baremetal-register.json
         cloudOperationsServiceAccountKeyPath: bmctl-workspace/.sa-keys/my-gcp-project-anthos-baremetal-cloud-ops.json
         

  2. Register your clusters to a fleet. The project ID that you specified in the `bmctl create config` command is automatically added to the `gkeConnect.projectID` field in the cluster configuration file. This project is referred to as the [fleet host project](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts#fleet-host-project).

     * If you created your configuration file using the automatic API enablement and Service Account creation features, you can skip this step.

     * If you created the configuration file without using the automatic API enablement and Service Account creation features, reference the downloaded service account JSON keys in the corresponding `gkeConnectAgentServiceAccountKeyPath` and `gkeConnectRegisterServiceAccountKeyPath` fields of the cluster configuration file.

     * Optionally, you can add [`gkeConnect.location`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#gkeconnect-location) to the cluster spec to specify the Google Cloud region in which the Fleet and the Connect services run. This regional membership restricts fleet service traffic to your region. If you include `gkeConnect.location` in the cluster spec, the region that you specify must be the same as the region configured in `clusterOperations.location`. If the regions aren't the same, cluster creation fails.

  3. Check to make sure the config specifies a cluster type of `admin` (the default value):
         
         spec:
           # Cluster type. This can be:
           #   1) admin:  to create an admin cluster. This can later be used to create user clusters.
           #   2) user:   to create a user cluster. Requires an existing admin cluster.
           #   3) hybrid: to create a hybrid cluster that runs admin cluster components and user workloads.
           #   4) standalone: to create a cluster that manages itself, runs user workloads, but does not manage other clusters.
           type: admin
         

  4. If the GKE On-Prem API is enabled in your Google Cloud project, all clusters in the project are [enrolled in the GKE On-Prem API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/enroll-cluster) automatically in the region configured in `clusterOperations.location`.

     * If you want to enroll all clusters in the project in the GKE On-Prem API, be sure to do the steps in [Before you begin](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/enroll-cluster#before_you_begin) to activate and use the GKE On-Prem API in the project.

     * If you don't want to enroll the cluster in the GKE On-Prem API, include this section and set `gkeOnPremAPI.enabled` to `false`. If you don't want to enroll any clusters in the project, disable `gkeonprem.googleapis.com` (the service name for the GKE On-Prem API) in the project. For instructions, see [Disabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#disabling).

  5. Change the configuration file to specify a multi-node, high availability control plane. Specify an odd number of nodes to have a majority quorum for HA:
         
         # Control plane configuration
           controlPlane:
             nodePoolSpec:
               nodes:
               # Control plane node pools. Typically, this is either a single machine
               # or 3 machines if using a high availability deployment.
               - address: 10.200.0.4
               - address: 10.200.0.5
               - address: 10.200.0.6
         

**Note:** If you have an even number of nodes temporarily while ading or removing nodes for maintenance or replacement, your deployment maintains HA as long as you have enough quorum.
  6. Specify the pod density of cluster nodes:
         
         ....
         # NodeConfig specifies the configuration that applies to all nodes in the cluster.
         nodeConfig:
           # podDensity specifies the pod density configuration.
           podDensity:
             # maxPodsPerNode specifies at most how many pods can be run on a single node.
             maxPodsPerNode: 250
         ....
         

For admin clusters, allowable values for `maxPodsPerNode` are `32-250` for HA clusters and `64-250` for non-HA clusters. The default value if unspecified is `110`. Once the cluster is created, this value cannot be updated.

Pod density is also limited by your cluster's available IP resources. For details, see [Pod networking](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/network-reqs#pod_networking).




## Create the admin cluster with the cluster config

Use the `bmctl` command to deploy the cluster: 
    
    
    bmctl create cluster -c ADMIN_CLUSTER_NAME
    

ADMIN_CLUSTER_NAME specifies the cluster name created in the previous section.

The following shows an example of the command to create a cluster called `admin1`:
    
    
    bmctl create cluster -c admin1
    

## Sample admin cluster configurations

For example admin cluster configurations, see [Admin clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/config-samples#admin_clusters) in the Cluster configuration samples.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
