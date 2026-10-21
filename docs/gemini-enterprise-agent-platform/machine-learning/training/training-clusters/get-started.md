---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/training-clusters/get-started/
title: Get started with training clusters \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:16:41.952646+00:00
---

# Get started with training clusters  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/training-clusters/get-started/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Get started with training clusters Stay organized with collections  Save and categorize content based on your preferences. 

If you're interested in Gemini Enterprise Agent Platform training clusters contact your sales representative for access. 

Before you can deploy your first cluster on Gemini Enterprise Agent Platform training clusters, you must configure your Google Cloud project and environment. This guide covers all the necessary prerequisites, which fall into three main categories:

  * Project Access: Gaining access to the service, which is by invitation only.

  * Resource Configuration: Enabling APIs and setting up the required VPC network and storage services.

  * User Permissions: Granting the necessary IAM roles for cluster management and resource access.




Completing these steps prepares your project for a successful deployment.

## Prerequisites

To use training clusters, you must:

  1. **Allowlist your project** by contacting your sales representative for access.
  2. **Obtain capacity** for [GPU clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/process-overview#choose-a-consumption-option-and-obtain-capacity) in supported regions.
  3. **Enable the necessary APIs** , including the Compute Engine, Filestore, Cloud Storage, Managed Lustre (optional), [Hypercomputer Configuration Service](https://docs.cloud.google.com/ai-hypercomputer/docs), and Agent Platform APIs.
  4. **Configure networking** by ensuring an existing network meets specific conditions (for example, Google Private Access, firewall rules) or by creating a new VPC network and subnetwork.
  5. **Configure storage** by creating a zonal or regional Filestore instance to serve as the `/home` directory and optionally configuring a [Google Cloud managed Lustre instance](https://docs.cloud.google.com/managed-lustre/docs/overview).
  6. **Grant IAM permissions** to users for cluster management, storage access and SSH access to cluster nodes, as described in the IAM permissions section.



### Supported regions

**Note:** Issuing a request to any regions that aren't on this list causes an API error.

  * `us-central1`
  * `us-east1`
  * `us-east4`
  * `us-east5`
  * `us-south1`
  * `us-west1`
  * `us-west4`
  * `asia-southeast1`
  * `europe-west1`
  * `europe-west4`
  * `europe-north1`
  * `asia-south2`



### IAM permissions

  1. Grant the `roles/aiplatform.admin` role to users who will manage your training clusters.
  2. Grant the `roles/aiplatform.viewer` role to users who only need to view clusters and their configurations.
  3. Grant the following IAM roles to the user or service account that will manage (create, delete, and update) Managed Training clusters:

Role Name | Role ID  
---|---  
Compute Instance Admin (v1) | `roles/compute.instanceAdmin.v1`  
Logs Writer | `roles/logging.logWriter`  
Monitoring Metric Writer | `roles/monitoring.metricWriter`  
Service Account User | `roles/iam.serviceAccountUser`  
Service Networking Admin | `roles/servicenetworking.networksAdmin`  
  4. To allow the cluster's nodes to read from and write to Cloud Storage buckets using Google Cloud Storage FUSE, grant the Storage Object User role (`roles/storage.objectUser`) to the service account used by the VMs.

  5. For SSH access to the Slurm login nodes, grant the following permissions:

Permissions | Descriptions | Purpose  
---|---|---  
[Compute OS Login](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin#configure_users) | Sign in to a VM as a standard (non-administrator) user. If `sudo` is needed then use Compute OS Admin Login instead. | SSH to the deployed login node  
[IAP-secured Tunnel User](https://docs.cloud.google.com/iap/docs/managing-access) | Access Tunnel resources which use Identity-Aware Proxy. | SSH to the deployed login node  



### Enable APIs

  1. Enable the Google Compute Engine API:
         
         gcloud services enable compute.googleapis.com
         
         

  2. Enable the service networking since Filestore must be deployed before creating the cluster.
         
         gcloud services enable servicenetworking.googleapis.com
         

  3. Enable the Cloud Storage API:
         
         gcloud services enable storage.googleapis.com
         

  4. Enable the Lustre API (if using Lustre):
         
         gcloud services enable lustre.googleapis.com
         
         

  5. Enable the HCS API:
         
         gcloud services enable hypercomputecluster.googleapis.com
         
         

  6. Enable the [Gemini Enterprise API](https://console.cloud.google.com/):
         
         gcloud services enable aiplatform.googleapis.com
         
         

  7. Enable the [Cloud Resource Manager API](https://console.cloud.google.com/):
         
         gcloud services enable cloudresourcemanager.googleapis.com
         
         




## What's next

For a detailed guide on creating a training cluster and running your AI/ML workloads, contact your sales representative.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
