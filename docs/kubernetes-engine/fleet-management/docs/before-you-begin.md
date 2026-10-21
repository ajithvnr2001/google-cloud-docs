---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin/
title: General prerequisites \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:50:01.003111+00:00
---

# General prerequisites  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  General prerequisites Stay organized with collections  Save and categorize content based on your preferences. 

As you learned in the [fleet creation overview](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation), on-premises GKE clusters [on VMware](https://docs.cloud.google.com/anthos/clusters/docs/on-prem) and [on bare metal](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal), and [multicloud clusters](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud) (both on AWS and Azure) are automatically registered to your project fleet at cluster creation time. However, GKE clusters on Google Cloud and third-party Kubernetes clusters (attached clusters) must be manually registered to join your fleet. You can find more details about different registration options in the fleet creation overview.

This page describes the prerequisites and requirements for manually registering _any_ Kubernetes cluster to a Google Cloud fleet. There are also specific separate requirements for GKE clusters on Google Cloud and attached clusters. Once you have completed this guide, follow the instructions for the cluster type you want to register.

We recommend that you review the [general restrictions on cluster registration](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts/plan-fleets#fleet_and_resource_limitations) before you begin.

## Install command line tools

Ensure you have the following command line tools installed. If you are using Cloud Shell as your shell environment for interacting with Google Cloud, these tools are installed for you.

### Install the Google Cloud CLI

Google Cloud CLI is the command line interface (CLI) to Google Cloud. You can register clusters by using Google Cloud CLI or, depending on your cluster type, by using other tools such as Terraform or the Google Cloud console. However, even if you don't use it for cluster registration, `gcloud` is required or useful for many of the other setup steps in this guide.

  1. If you don't have it installed already, install the Google Cloud CLI following the [installation instructions](https://docs.cloud.google.com/sdk/install). We recommend using the most recent version of the Google Cloud CLI. You need version version 361.0.0 or higher to register clusters, and version 423.0.0 or higher if you want to use the non-legacy registration commands for GKE, with the [alpha or beta component installed](https://cloud.google.com/sdk/docs/components).

  2. Run the following command to log in to Google Cloud:
         
         gcloud auth login

  3. (Optional) Ensure that you have installed the `gcloud beta` component, if you plan to try alpha or beta features:
         
         gcloud components install beta 




### Install `kubectl`

While `kubectl` is not required to register a cluster, you may need it to grant the necessary role-based access control (RBAC) permissions to the user registering the cluster (if they are not the cluster owner), as well as for other platform-specific setup. You need a `kubectl` version no lower than the [minimum supported Kubernetes version](https://cloud.google.com/kubernetes-engine/docs/release-notes) of Google Kubernetes Engine (GKE).

We recommend installing `kubectl` with [Google Cloud CLI](https://docs.cloud.google.com/sdk/install).

To check the version of `kubectl`: 
    
    
    kubectl version

The client version is indicated by `gitVersion` of the output.

To install `kubectl`: 
    
    
    gcloud components install kubectl

## Enable APIs

You need to enable the following APIs in your fleet host project:

  * `container.googleapis.com`
  * `gkeconnect.googleapis.com`
  * `gkehub.googleapis.com`, also known as the Fleet API. This is the Google Cloud service that handles cluster registration and fleet membership.
  * `cloudresourcemanager.googleapis.com`



Pods in the cluster you want to register must be able to reach `googleapis.com` and `gkeconnect.googleapis.com` addresses, either directly or by using a configured proxy server.

If you want to [enable fleet Workload Identity](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/use-workload-identity) for your registration, you must also enable the following:

  * `iam.googleapis.com`



Non-project owners must be granted the `serviceusage.services.enable` permission before they can enable APIs.

**Note:** This permission allows non-project owners to enable any API in the project. If you do not want to grant that level of access, you can enable the list of APIs for each registration user in the project.

### gcloud

To enable these APIs, run the following command:
    
    
    gcloud services enable \
       --project=FLEET_HOST_PROJECT_ID \
       container.googleapis.com \
       gkeconnect.googleapis.com \
       gkehub.googleapis.com \
       cloudresourcemanager.googleapis.com \
       iam.googleapis.com
    

where:

  * FLEET_HOST_PROJECT_ID is the Google Cloud project ID in which you want to register clusters. [Learn how to find this value](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).



If you don't want to enable fleet Workload Identity, you can omit `iam.googleapis.com`.

To list APIs you've already enabled in your projects, follow the instructions in [Listing Services](https://docs.cloud.google.com/service-usage/docs/list-services#enabled) in the Service Usage documentation.

## Grant access permissions

Ensure that you have the appropriate access permissions to register a cluster. Cluster registration requires both permission to register the cluster to a fleet, and admin permissions on the cluster itself.

### Grant cluster registration permissions

Registering a cluster requires IAM permissions in your fleet host project to register clusters. If you have `roles/owner` in your fleet host project, you have this automatically and have all the access permissions you need to complete all registration tasks.

If you do not have `roles/owner` in your project, you need to be granted specific IAM roles before you can connect clusters to Google, as follows:

  * To register a cluster with fleet [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/use-workload-identity) for authentication to Google, you just need the following IAM role:

    * `roles/gkehub.admin`
  * [Some registration options outside Google Cloud](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/attached/previous-generation/before-you-begin#set_up_identity) require you to set up a service account for the cluster to use to authenticate to Google instead of Workload Identity. To register the cluster and manage this service account, you need the following set of roles:

    * `roles/gkehub.admin`
    * `roles/iam.serviceAccountAdmin`
    * `roles/iam.serviceAccountKeyAdmin`
    * `roles/resourcemanager.projectIamAdmin`



For a list of detailed permissions included in the `gkehub` roles, see [Connect IAM roles](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent#connect_iam_roles).

### gcloud

To grant an IAM role to a user, run the following command:
    
    
    gcloud projects add-iam-policy-binding FLEET_HOST_PROJECT_ID \
       --member user:GCP_EMAIL_ADDRESS \
       --role=ROLE
    

where:

  * FLEET_HOST_PROJECT_ID is the Google Cloud project ID in which you want to register clusters. [Learn how to find this value](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * GCP_EMAIL_ADDRESS is the account the user uses to log in to Google Cloud.
  * ROLE is the IAM role you want to grant, such as `roles/gkehub.admin`.



To learn more about how to grant IAM roles, refer to [Granting, Changing, and Revoking Access to Resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#updating-gcloud) in the IAM documentation.

### Grant cluster admin permissions

In addition to the permissions required to register a cluster, you also need admin permissions on the cluster itself. Depending on your cluster's location you can assign this permission by using IAM roles or Kubernetes role-based access control (RBAC).

**Note:** `cluster-admin` provides super-user access to perform any action on any resource in the cluster. Use caution when you assign this role to other users.

#### GKE clusters on Google Cloud

For GKE clusters on Google Cloud only, add the following IAM role to get admin permissions on the cluster, if you don't have it already (your user account is likely to have it if you created the cluster):

  * `roles/container.admin`



This IAM role includes the Kubernetes RBAC [`cluster-admin`](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles) role. For other cluster environments you need to grant this RBAC role using `kubectl`, as described in the next section. You can find out more about the relationship between IAM and RBAC roles in GKE in the [GKE documentation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#iam-interaction).

#### Clusters outside Google Cloud

For attaching third-party clusters outside Google Cloud, ensure the user registering the cluster has the Kubernetes RBAC [`cluster-admin`](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles) role.

### kubectl

If you created the cluster, you likely have this role. You can verify by running the following command:
    
    
    kubectl auth can-i '*' '*' --all-namespaces

If you or another user needs the role, create a ClusterRoleBinding resource in the cluster:
    
    
    kubectl create clusterrolebinding BINDING_NAME --clusterrole cluster-admin --user USER
    

where:

  * BINDING_NAME is a name that you choose for the ClusterRoleBinding resource.
  * USER is the identity used to authenticate against the cluster.



## What's next?

Follow the prerequisites guide for the cluster type you want to register:

  * [Prerequisites for GKE clusters on Google Cloud](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin/gke)
  * [Prerequisites for EKS clusters](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/attached/eks/reference/cluster-prerequisites)
  * [Prerequisites for AKS clusters](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/attached/aks/reference/cluster-prerequisites)
  * [Prerequisites for other attached cluster types](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/attached/previous-generation/before-you-begin)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
