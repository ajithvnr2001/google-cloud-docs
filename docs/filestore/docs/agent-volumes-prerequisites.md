---
url: https://docs.cloud.google.com/filestore/docs/agent-volumes-prerequisites/
title: Set up Filestore agent volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:00:18.986534+00:00
---

# Set up Filestore agent volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/agent-volumes-prerequisites/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Set up Filestore agent volumes Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** The Filestore agent volumes feature is available to all Google Cloud customers for evaluation and non-production use. To request access for your Google Cloud project, submit the [Filestore agent volumes access request form](https://forms.gle/vYPkcFiZVoTjf7Ah7). Production support is offered on an allow list basis under a limited GA program. To check your eligibility or to request production support, use the access form. 

Before you create volume pools or provision volumes, you must configure Virtual Private Cloud (VPC) networking using Private Service Connect (PSC), enable the required APIs, and grant the appropriate IAM roles.

## Create a project and enable APIs

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Filestore APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=file.googleapis.com,serviceusage.googleapis.com,networkconnectivity.googleapis.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Filestore APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=file.googleapis.com,serviceusage.googleapis.com,networkconnectivity.googleapis.com)




### Required roles

To get the permissions that you need to set up Filestore agent volumes, ask your administrator to grant you the following IAM roles on your project: 

  * Configure Service Connection Policies and VPC networking: [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) 
  * View and manage Filestore instances and related resources, including volume pools and agent volumes: [Cloud Filestore Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.editor) (`roles/file.editor`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Initialize the service agent

If you haven't created a Filestore instance in your project, initialize the Filestore service agent by running the following command:
    
    
    gcloud beta services identity create \
        --service=file.googleapis.com \
        --project=PROJECT_ID
    

Replace `PROJECT_ID` with the ID of your Google Cloud project.

## Grant permissions to the service agent

To set up Filestore agent volumes, grant the Cloud Filestore Editor (`roles/file.editor`) role to the Filestore service agent:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="serviceAccount:service-PROJECT_NUMBER@cloud-filer.iam.gserviceaccount.com" \
        --role="roles/file.editor"
    

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `PROJECT_NUMBER`: the project number of your Google Cloud project.



## Configure Private Service Connect networking

Filestore agent volumes use [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) to connect managed storage infrastructure directly to your VPC network. Private Service Connect ensures private, high-bandwidth, and low-latency communication without requiring public IP addresses or VPC Network Peering configurations.

To create a service connection policy, run the following command:
    
    
    gcloud network-connectivity service-connection-policies create POLICY_NAME \
        --project=PROJECT_ID \
        --region=REGION \
        --network=projects/PROJECT_ID/global/networks/VPC_NETWORK \
        --subnets=SUBNET_NAME \
        --service-class=google-cloud-filestore
    

Replace the following:

  * `POLICY_NAME`: a name for the service connection policy, such as `filestore-agent-psc-policy`.
  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `REGION`: the region where the volume pool and workloads will reside, such as `us-central1`.
  * `VPC_NETWORK`: the name of an existing VPC network.
  * `SUBNET_NAME`: the name of a regular VPC subnet in the specified region where Private Service Connect endpoint IP addresses is to be allocated. An example can be the default subnet with the `--purpose` flag set to `PRIVATE`.



## Create a volume pool and StorageClass

A volume pool provides the shared storage capacity and IOPS for agent volumes. To dynamically provision volumes from your volume pool in GKE, create the volume pool and then define a Kubernetes `StorageClass` that references it.

### Create a volume pool

To create a sample volume pool, send an HTTP `POST` request to the `volumePools.create` endpoint:
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        -d '{
          "description": "Sample volume pool for agent volumes",
          "network": "projects/PROJECT_ID/global/networks/VPC_NETWORK",
          "defaultVolumeQuotaMib": 2048,
        }' \
        "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/volumePools?volumePoolId=VOLUME_POOL_ID"
    

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `VPC_NETWORK`: the name of your PSC-enabled VPC network.
  * `LOCATION`: the region where the volume pool is deployed, such as `us-central1`.
  * `VOLUME_POOL_ID`: an identifier for the volume pool, such as `my-volume-pool`.



For more information, see [Create and manage volume pools](https://docs.cloud.google.com/filestore/docs/create-volume-pools).

### Create a StorageClass

Create a `StorageClass` manifest named `volume-pool-sc.yaml` that references your volume pool:
    
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: volume-pool-sc
    provisioner: filestore.csi.storage.gke.io
    volumeBindingMode: Immediate
    reclaimPolicy: Delete
    allowVolumeExpansion: true
    parameters:
      volume-pool: "projects/<var>PROJECT_ID</var>/locations/<var>LOCATION</var>/volumePools/<var>VOLUME_POOL_ID</var>"
    

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the region where the volume pool is deployed.
  * `VOLUME_POOL_ID`: the identifier of your volume pool.



If you have an existing GKE cluster with the Filestore CSI driver installed, apply the `StorageClass`:
    
    
    kubectl apply -f volume-pool-sc.yaml
    

Otherwise, apply this manifest after setting up your cluster in [Set up GKE environment for Filestore agent volumes](https://docs.cloud.google.com/filestore/docs/use-filestore-agent-volumes-gke#create-storageclass).

## What's next

  * Create and manage [volume pools](https://docs.cloud.google.com/filestore/docs/create-volume-pools).
  * Configure [GKE environment for Filestore agent volumes](https://docs.cloud.google.com/filestore/docs/use-filestore-agent-volumes-gke).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
