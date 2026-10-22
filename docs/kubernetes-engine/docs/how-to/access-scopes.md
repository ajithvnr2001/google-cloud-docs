---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/access-scopes/
title: Access scopes in GKE \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:21.240353+00:00
---

# Access scopes in GKE  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/access-scopes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Access scopes in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes the default access scopes granted to nodes in Google Kubernetes Engine (GKE) clusters. By reading this page, you learn about the default access scopes that are granted to clusters, and how you can configure custom access scopes, if required.

This page is for Security specialists and Operators who create and manage clusters, and must understand the default access that is granted to clusters and how to modify that access if needed. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## What are access scopes?

Access scopes are the legacy method of granting permissions for your nodes, and for workloads running on your nodes if the workloads use [application default credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials). Access scopes define the OAuth scopes used in API calls from client libraries or the gcloud CLI.

We recommend that you don't specify your own access scopes. Instead, you should use [IAM permissions](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) or [Kubernetes role-based access control (RBAC)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control) to grant access to specific IAM service accounts or Kubernetes service accounts.

## Default access scopes

When you create a new GKE cluster, Google Cloud assigns a default set of access scopes to nodes based on the service account used by the nodes. These access scopes enable specific functionality for GKE. You can also set access scopes manually using the `--scopes` flag when you create [Standard clusters](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create#--scopes), [Autopilot clusters](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--scopes), or [node pools](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--scopes). You can't modify the access scopes on existing node pools. Instead, create a new node pool with the new scopes and migrate workloads to that node pool.

The following sections describe the default access scopes that GKE adds to nodes based on whether you specify a custom service account, and whether you manually specify access scopes.

### Autopilot clusters

Service account | Did you manually specify access scopes? | Access scopes that GKE adds  
---|---|---  
Compute Engine default service account | No | 

  * `https://www.googleapis.com/auth/devstorage.read_only`
  * `https://www.googleapis.com/auth/service.management.readonly`
  * `https://www.googleapis.com/auth/servicecontrol`
  * `https://www.googleapis.com/auth/trace.append`
  * `https://www.googleapis.com/auth/logging.write`: added if Cloud Logging is enabled
  * `https://www.googleapis.com/auth/monitoring`: added if Cloud Monitoring is enabled

  
Yes | Manually specified scopes  
Custom service account | No | `https://www.googleapis.com/auth/cloud-platform`  
Yes | Manually specified scopes  
  
### Standard clusters

Service account | Manually-specified access scopes? | GKE access scopes  
---|---|---  
Compute Engine default service account | No | 

  * `https://www.googleapis.com/auth/devstorage.read_only`
  * `https://www.googleapis.com/auth/service.management.readonly`
  * `https://www.googleapis.com/auth/servicecontrol`
  * `https://www.googleapis.com/auth/trace.append`
  * `https://www.googleapis.com/auth/logging.write`: added if Cloud Logging is enabled
  * `https://www.googleapis.com/auth/monitoring`: added if Cloud Monitoring is enabled

  
Yes | 

  * Manually specified scopes
  * `https://www.googleapis.com/auth/monitoring.write`
  * `https://www.googleapis.com/auth/logging.write`: added if Cloud Logging is enabled
  * `https://www.googleapis.com/auth/monitoring`: added if Cloud Monitoring is enabled

  
Custom service account | No | 

  * `https://www.googleapis.com/auth/userinfo.email`
  * `https://www.googleapis.com/auth/cloud-platform`

  
Yes | 

  * Manually specified scopes
  * `https://www.googleapis.com/auth/monitoring.write`
  * `https://www.googleapis.com/auth/logging.write`: added if Cloud Logging is enabled
  * `https://www.googleapis.com/auth/monitoring`: added if Cloud Monitoring is enabled

  
  
## Configure a custom service account for workloads

[IAM](https://docs.cloud.google.com/iam/docs/overview) is the access control system for granting authorized roles to users and service accounts within your Google Cloud project. A [service account](https://docs.cloud.google.com/iam/docs/service-accounts) is a special Google Account that performs tasks, such as deploying applications, on your behalf. You use IAM to create a service account, then use IAM policy bindings to secure the account.

If your workloads require access to Compute Engine, grant the service account the [Compute Engine Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.admin) role. If your workloads need to pull private images from Artifact Registry, see [Configuring access control for Artifact Registry repositories](https://docs.cloud.google.com/artifact-registry/docs/access-control).

### Create a service account

To create a custom service account named `kubernetes-engine-node-sa`, run the following commands:
    
    
    export NODE_SA_NAME=kubernetes-engine-node-sa
    gcloud iam service-accounts create $NODE_SA_NAME \
      --display-name "GKE Node Service Account"
    export NODE_SA_EMAIL=`gcloud iam service-accounts list --format='value(email)' \
      --filter='displayName:GKE Node Service Account'`
    

**Note:** These commands export two variables, `$NODE_SA_NAME` and `$NODE_SA_EMAIL`, that are used in commands documented later on this page.

### Grant minimal roles

To configure the service account with the _minimal_ necessary roles and permissions for your GKE node to function, run the following commands, where `$PROJECT` is your [project ID](https://support.google.com/cloud/answer/6158840):
    
    
    export PROJECT=`gcloud config get-value project`
    gcloud projects add-iam-policy-binding $PROJECT \
      --member serviceAccount:$NODE_SA_EMAIL \
      --role roles/monitoring.metricWriter
    gcloud projects add-iam-policy-binding $PROJECT \
      --member serviceAccount:$NODE_SA_EMAIL \
      --role roles/monitoring.viewer
    gcloud projects add-iam-policy-binding $PROJECT \
      --member serviceAccount:$NODE_SA_EMAIL \
      --role roles/logging.logWriter
    

### Grant additional roles

**Caution:** The `compute.admin` role shouldn't be granted to this service account unless necessary. Granting this role allows workloads to create, delete, read metadata on, and access nodes using SSH, among other operations.

To grant the service account the [Compute Engine Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.admin) role, run the following command:
    
    
    gcloud projects add-iam-policy-binding $PROJECT \
      --member serviceAccount:$NODE_SA_EMAIL \
      --role roles/compute.admin
    

To learn how to grant service accounts access to private images stored in Artifact Registry, see [Granting access to Google Kubernetes Engine clusters](https://docs.cloud.google.com/artifact-registry/docs/access-control#gke).

### Create a cluster or node pool with the custom service account

To create a cluster that uses the custom service account, run the following command:
    
    
    gcloud container clusters create --service-account=$NODE_SA_EMAIL
    

To create a node pool in an existing cluster:
    
    
    gcloud container node-pools create --service-account=$NODE_SA_EMAIL
    

**Note:** You can also find the service account's email address by running the following command: 
    
    
    gcloud iam service-accounts list --format='value(email)' \
          --filter='displayName:Node Service Account'
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
