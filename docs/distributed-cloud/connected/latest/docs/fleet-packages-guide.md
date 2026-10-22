---
url: https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/fleet-packages-guide/
title: Use fleet packages in Distributed Cloud connected \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:35.328941+00:00
---

# Use fleet packages in Distributed Cloud connected  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/fleet-packages-guide/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.13.0 (Latest) ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/overview)



Send feedback 

#  Use fleet packages in Distributed Cloud connected Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use Config Sync fleet packages in your Google Distributed Cloud connected environment. Fleet packages are a tool that uses a Git repository as the single source of truth for your cluster configuration.

Fleet packages in Distributed Cloud connected use the same underlying technology and commands as standard Google Kubernetes Engine clusters. The GKE documentation explains how to create and manage fleet packages in the page [Deploy fleet packages](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/fleet-packages). This page explains how to adapt that guide for your Distributed Cloud connected environment.

The following sections explain what you need to do differently for Distributed Cloud connected and which steps in the GKE documentation you can follow without changes.

## Requirements

Using Config Sync fleet packages in Distributed Cloud connected has the following requirements:

  * Because the rollout controller resides in the cloud, your Git repository must be reachable over the public internet. Internal or on-premises Git servers that are not publicly exposed are not supported.
  * Distributed Cloud connected only supports using fleet Workload Identity Federation to authenticate with Google Cloud services. Other Config Sync authentication methods, such as SSH keys or cookies, are not supported for the connection between your clusters and the versioned bundle repository. For more information, see [Workload Identity Cluster Authentication](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/wi-cluster-auth).
  * All clusters in a fleet must be in the same project. Distributed Cloud connected doesn't support registering clusters across multiple projects into a single central project for fleet management.
  * Your Kubernetes manifests must comply with the [Distributed Cloud connected workload limitations](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/deploy#workload-limitations). Manifests that violate these restrictions are blocked by the cluster admission controller.
  * Fleet packages require Config Sync version 1.16.0 or later.



## System behavior

Fleet packages in Distributed Cloud connected have the following behaviors:

  * Fleet packages transform your Kubernetes manifests into versioned OCI images. These images are stored in a managed Artifact Registry repository named `fleet-packages`, which is automatically created in your project. Your clusters pull these images directly from the repository to ensure consistent and reliable delivery.
  * Fleet packages inherit Config Sync's drift correction behavior. Manual changes made to resources on a cluster are automatically overwritten to match the versioned OCI bundles.
  * If a Distributed Cloud connected cluster enters [survivability mode](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/survivability), the Config Sync agent continues to enforce the last successfully synced configuration locally. However, any new rollouts or updates to the fleet package are paused until cloud connectivity is restored.
  * Fleet packages inherit Config Sync's automatic resource pruning behavior. When you create a new tag in your Git repository and update the fleet package configuration with the new tag to initiate a sync, the Config Sync agent deletes the corresponding resource from your cluster if you remove a manifest from your Git repository.
  * If multiple fleet packages manage the same resource, an ownership conflict occurs. If you attempt to delete a fleet package while it is in an ownership conflict, the deletion might stall. To resolve this issue, modify one of the competing fleet packages to remove the conflicting resource before you attempt to delete the package.



## Distributed Cloud connected prerequisites

Before following the steps in [Deploy fleet packages](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/fleet-packages), ensure that your Distributed Cloud connected environment and user permissions are properly configured.

### Networking and security

Your networking environment must meet the following requirements:

  * **VPC Service Controls**. If your project is protected by a VPC service perimeter, ensure that your Cloud Build and Config Delivery service agents, for example, `service-PROJECT_NUMBER@gcp-sa-configdelivery.iam.gserviceaccount.com`, are authorized to cross the perimeter and pull images from Artifact Registry. For more information, see [Configure VPC Service Controls integration](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/deploy#vpc-sc-integration).
  * **Egress access**. Your Distributed Cloud connected clusters must have egress access to `us-central1-docker.pkg.dev`. Fleet packages store your manifest bundles as OCI images in Artifact Registry. The clusters must be able to pull these images directly from Artifact Registry.



### Repository setup

The Artifact Registry repository containing your manifest bundles must be in the same project as the fleet package, and it must be located in `us-central1`.

### Required permissions

To complete the steps in the Distributed Cloud connected environment, you must have the following IAM roles on the project:

  * **Config Delivery Admin** (`roles/configdelivery.admin`): required to create and manage fleet packages and rollouts
  * **Developer Connect Admin** (`roles/developerconnect.admin`): required to create and manage repository connections
  * **Project IAM Admin** (`roles/resourcemanager.projectIamAdmin`): required to grant necessary roles to the service account



For more information about granting roles, see [Grant, change, and revoke access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

### Required APIs

You need to enable APIs for repository connections and secure communication with Distributed Cloud connected clusters. To enable the required APIs, run the following [`gcloud services enable`](https://docs.cloud.google.com/sdk/gcloud/reference/services/enable) command:
    
    
    gcloud services enable anthosconfigmanagement.googleapis.com \
        configdelivery.googleapis.com \
        cloudbuild.googleapis.com \
        connectgateway.googleapis.com \
        developerconnect.googleapis.com \
        artifactregistry.googleapis.com
    

These APIs are required for the following components:

  * `anthosconfigmanagement.googleapis.com`: manages the Config Sync agent on your clusters
  * `configdelivery.googleapis.com`: coordinates the rollout of Kubernetes resources across your fleet of clusters
  * `cloudbuild.googleapis.com`: fetches your Kubernetes manifests from Git and packages them into versioned bundles
  * `connectgateway.googleapis.com`: provides a secure connection between the Config Delivery service and your Distributed Cloud connected clusters
  * `developerconnect.googleapis.com`: enables secure connections to your external Git repository host
  * `artifactregistry.googleapis.com`: stores the versioned package bundles as OCI images in your project



### Required cluster RBAC permissions

You must grant the RBAC permissions described in this section to the Config Delivery service agent (P4SA) on your cluster so that it can manage Config Sync objects.

To grant these permissions, apply the following manifest to your cluster:
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: fleet-packages-impersonator
    rules:
    - apiGroups:
      - ""
      resourceNames:
      - P4SA_EMAIL
      resources:
      - users
      verbs:
      - impersonate
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: fleet-packages-impersonator-binding
    roleRef:
      kind: ClusterRole
      name: fleet-packages-impersonator
      apiGroup: rbac.authorization.k8s.io
    subjects:
    - kind: ServiceAccount
      name: connect-agent-sa
      namespace: gke-connect
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: fleetpackages-configsync-admin
    rules:
    - apiGroups:
      - "configsync.gke.io"
      resources:
      - rootsyncs
      - reposyncs
      verbs:
      - "*"
    - apiGroups:
      - "kpt.dev"
      resources:
      - resourcegroups
      verbs:
      - "*"
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: fleet-packages-configsync-admin-binding
    subjects:
    - kind: User
      name: P4SA_EMAIL
    roleRef:
      kind: ClusterRole
      name: fleetpackages-configsync-admin
      apiGroup: rbac.authorization.k8s.io
    

Replace `P4SA_EMAIL` with your Config Delivery Service Agent email, which typically follows this format: `service-PROJECT_NUMBER@gcp-sa-configdelivery.iam.gserviceaccount.com`.

### Default environment settings

The Config Delivery API for fleet packages is only supported in `us-central1`. To make sure that your commands route correctly, use the [`gcloud config set`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) command to set your default project and location:

  1. Set your default project:
         
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with your Google Cloud project ID.

  2. Set the default location for fleet packages. All Cloud Build repository connections used with fleet packages must be in the `us-central1` region.
         
         gcloud config set config_delivery/location us-central1
         




## Procedural differences

Use the following table to understand how to apply the steps in [Deploy fleet packages](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/fleet-packages) to your Distributed Cloud connected environment.

Standard step | Distributed Cloud connected adjustment  
---|---  
**Register clusters to a fleet** | Skip this step. Distributed Cloud connected clusters are automatically registered to a fleet in your project when they are created.  
**Install Config Sync** | Follow the standard steps, but we recommend using the **Install on entire fleet (fleet default)** method. Configure this method in the **Hub** or **Fleet** settings in the Google Cloud console. This implementation ensures that any existing or future Distributed Cloud connected nodes in your zone automatically receive the Config Sync agent.  
  
For the authentication member type, you must select **Workload Identity**.  
  
The service account that you use for Workload Identity must have the `roles/artifactregistry.reader` role on the project so that the Config Sync agent can pull manifest bundles from the managed `fleet-packages` repository.  
**Configure cluster RBAC** | For Distributed Cloud connected, you must explicitly grant RBAC permissions to the Config Delivery service agent (P4SA) on your clusters. See Required cluster RBAC for details.  
**Create a service account** | Follow the instructions to create a service account for Cloud Build and grant the required permissions. The service account must be in the same project as your fleet package. We recommend that you use the following commands: 

  1. Create the service account by running the [`gcloud iam service-accounts create`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/create) command: 
         
         gcloud iam service-accounts create "SERVICE_ACCOUNT_NAME"
                 

Replace `SERVICE_ACCOUNT_NAME` with a name for the service account. 
  2. Add the mandatory Identity and Access Management roles by running the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command for each of the following roles. For more information about IAM, see the [IAM overview](https://docs.cloud.google.com/iam/docs/overview). 
     * `roles/configdelivery.resourceBundlePublisher`: allows the service account to create and manage resource bundles and releases
     * `roles/cloudbuild.connectionUser`: allows the service account to use the Cloud Build repository connection
     * `roles/logging.logWriter`: allows the service account to write build logs
     * `roles/artifactregistry.writer`: allows the service account to push versioned package bundles to Artifact Registry
     * `roles/developerconnect.connectionUser`: allows the service account to use the Developer Connect connection
The service account also needs permission to read from your connected Git repository on your Git provider. For information about how to authorize the connection, see [Connect to a repository](https://docs.cloud.google.com/build/docs/repositories). 

  
**Identify membership name** | When a command asks for a `MEMBERSHIP_NAME`, use the name of your Distributed Cloud connected cluster. You can find the cluster name by running the [`gcloud container fleet memberships list`](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/list) command.  
**Identify a cluster** | Before you target a cluster with a fleet package, if your workloads require host-level networking configuration, such as HugePages or SR-IOV, apply and verify the [`NodeSystemConfigUpdate`](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/deploy#configure_the_nodesystemconfigupdate_resources) resources on every node in the cluster.   
**Identify Git tags** | The rollout controller requires Git tags to be in a full semantic version format (`major.minor.patch`). For example, `v1.0.0` is valid, whereas `v1` is not.  
**Target specific clusters** | Although clusters are auto-registered, you must [manually add labels](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/update#--update-labels) to the cluster memberships if you want to target subsets of clusters by using label selectors.  
**Deployment strategies** | Use labels and variants to target specific clusters. For Distributed Cloud connected, membership metadata variables, like project and location, used in your variant templates refer to the cloud-side resources associated with your Distributed Cloud connected cluster.  
  
The following Distributed Cloud-specific membership metadata is available for use in variant templates: 

  * `cluster_name`: the name of your Distributed Cloud connected cluster
  * `location`: the Google Cloud region associated with the cluster
  * `project`: the project ID where the cluster is registered
  * `labels`: any [labels you have applied](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/update#--update-labels) to the cluster membership

  
  
## Shared procedures

For the following operational tasks, the command syntax and service behavior are the same for Distributed Cloud connected and standard GKE. When following these instructions, use the settings and values defined in the table in the Procedural differences section of this document.

  * [Create a fleet package](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/fleet-packages#create): Define the `FleetPackage` resource to fetch and deploy your configuration.
  * [Update a fleet package](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/fleet-packages#update): Modify your package to rollout changes or update settings.
  * [Manage fleet package rollouts](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/fleet-packages#manage): Suspend, resume, or abort active rollouts.
  * [Inspect resource bundles and releases](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/fleet-packages#inspect-bundles-releases): Debug variant generation and versioning. Resource bundles are containers for your configurations, and releases are versioned instances of those bundles. To verify successful delivery to your Distributed Cloud connected hardware, use the [`gcloud container fleet memberships get-credentials`](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/get-credentials) command to [obtain access to your cluster](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/clusters#credentials), and then use `kubectl` to [inspect the `RootSync` status on the cluster](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitor-rootsync-reposync).
  * [Delete a fleet package](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/fleet-packages#delete): Remove a fleet package and its managed resources. To ensure a clean removal, verify that the managed `RootSync` objects associated with the fleet package are removed from your clusters.



## Monitoring and troubleshooting

To more effectively monitor deployments, use the `--format` flag with the `gcloud` command to get detailed status messages during a rollout.

For example, run the following [`gcloud container fleet packages rollouts describe`](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/packages/rollouts/describe) command to view a detailed status message for every cluster in your fleet:
    
    
    gcloud container fleet packages rollouts describe ROLLOUT_NAME \
        --fleet-package=FLEET_PACKAGE_NAME \
        --format=json
    

Replace the following values:

  * `ROLLOUT_NAME`: The name of the rollout.
  * `FLEET_PACKAGE_NAME`: The name of the fleet package.



If a build fails or gets stuck, you can find a link to the streaming logs for the Cloud Build job in the output of the [`gcloud container fleet packages list`](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/packages/list) command. If a rollout remains in a `PENDING` or `STALLED` state, check your Distributed Cloud connected hardware connectivity, as described in [Troubleshoot Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/troubleshooting).

For more information about diagnosing errors related to Cloud Build, see [Troubleshooting build errors](https://docs.cloud.google.com/build/docs/troubleshooting).

### Verify on-cluster sync status

To verify that your cluster is successfully syncing with the fleet package, examine the `RootSync` resource on the cluster. The name of the `RootSync` object on the cluster is identical to the `FLEET_PACKAGE_NAME` you chose for your package.

To check the status, run the following command:
    
    
    kubectl get rootsync FLEET_PACKAGE_NAME -n config-management-system
    

A successful sync displays a `SYNCED` status. If you see an `Error` status, to get more details, run the following command:
    
    
    kubectl describe rootsync FLEET_PACKAGE_NAME -n config-management-system
    

For more information, see [Monitor RootSync and RepoSync objects](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitor-rootsync-reposync) in the GKE documentation.

For help decoding specific error codes in the output, see the [Config Sync errors reference](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/errors). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
