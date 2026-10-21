---
url: https://docs.cloud.google.com/service-mesh/v1.22/docs/gateway/prepare-gateway/
title: Prepare to setup the Gateway API for Cloud Service Mesh \u00a0|\u00a0 Cloud Service Mesh v1.22 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:38:37.229632+00:00
---

# Prepare to setup the Gateway API for Cloud Service Mesh  |  Cloud Service Mesh v1.22  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.22/docs/gateway/prepare-gateway/

You are viewing archived v1.22 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.22 ](https://docs.cloud.google.com/service-mesh/v1.22/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.22/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Prepare to setup the Gateway API for Cloud Service Mesh

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to install the required custom resource definitions for the gateway into your cluster.

## Limitations

  * Having a mix of `gateway` config-api and `istio` config-api clusters in the same fleet is not supported.
  * Multi-cluster service discovery and load balancing is not supported for `gateway` config-api clusters.
  * If a cluster is onboarded using the existing `--management automatic` flag then the cluster starts using the `istio` configuration API and cannot change to `gateway` API.
  * Only FQDNs are supported. Short names are not supported.



## Prerequisites

As a starting point, this guide assumes that you have already [created a Google Cloud project](https://docs.cloud.google.com/sdk/docs/install-sdk#before-you-begin) and [installed `kubectl`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#install_kubectl).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Kubernetes Engine, GKE Hub, and Cloud Service Mesh APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,gkehub.googleapis.com,mesh.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Kubernetes Engine, GKE Hub, and Cloud Service Mesh APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,gkehub.googleapis.com,mesh.googleapis.com)



  4. Generate a kubeconfig entry for your cluster:
    
    gcloud container clusters get-credentials CLUSTER_NAME --location LOCATION --project PROJECT_ID
    




where:

  * CLUSTER_NAME is the name of your cluster
  * LOCATION is the location of your cluster
  * PROJECT_ID is the project ID of your cluster



## Create and register a GKE cluster

  1. Create a GKE cluster:
         
         gcloud container clusters create CLUSTER_NAME \
         --location=LOCATION \
         --enable-ip-alias \
         --scopes=https://www.googleapis.com/auth/cloud-platform \
         --release-channel=regular \
         --project=PROJECT_ID \
         --gateway-api=standard
         

where:

     * CLUSTER_NAME is the name of your cluster
     * LOCATION is the location of your cluster
     * PROJECT_ID is the project ID of your cluster
  2. Enable Workload Identity Federation for GKE:
         
         gcloud container clusters update CLUSTER_NAME \
         --location LOCATION \
         --workload-pool=PROJECT_ID.svc.id.goog
         

  3. Run the GKE Metadata Server on your node:
         
         gcloud container node-pools update default-pool \
         --cluster=CLUSTER_NAME \
         --location=LOCATION \
         --workload-metadata=GKE_METADATA
         

  4. Register your cluster to a [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs#introducing_fleets):
         
         gcloud container hub memberships register CLUSTER_NAME \
         --gke-cluster LOCATION/CLUSTER_NAME \
         --project=PROJECT_ID
         

  5. Verify that the cluster is registered to the fleet:
         
         gcloud container hub memberships list --project=PROJECT_ID
         

The output is similar to:
         
         NAME            EXTERNAL_ID                             LOCATION
         my-cluster      91980bb9-593c-4b36-9170-96445c9edd39    us-west1
         




## Set up permissions

Note that the following commands grant permission to all authenticated users, but you can use Workload Identity Federation for GKE to grant permission to only select accounts.

  1. Grant the `trafficdirector.client` role:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member "group:PROJECT_ID.svc.id.goog:/allAuthenticatedUsers/" \
             --role "roles/trafficdirector.client"
         

  2. Grant the `container.developer` role:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
         --member "serviceAccount:service-PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com" \
         --role "roles/container.developer"
         

where PROJECT_NUMBER is your project number.

  3. Grant the `compute.networkAdmin` role:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
         --member "serviceAccount:service-PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com" \
         --role "roles/compute.networkAdmin"
         

where PROJECT_NUMBER is your project number.




## Enable Cloud Service Mesh

  1. Enable the mesh feature:
         
         gcloud container hub mesh enable --project PROJECT_ID
         

  2. Update the mesh to use the Gateway API:
         
         gcloud alpha container fleet mesh update \
         --config-api gateway \
         --memberships CLUSTER_NAME \
         --project PROJECT_ID
         

  3. Verify the update by describing the status of Cloud Service Mesh resource:
         
         gcloud alpha container fleet mesh describe
         




## Install custom resource definitions

Install the GRPCRoute custom resource definition (CRD):
    
    
    curl https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.1.0/config/crd/standard/gateway.networking.k8s.io_grpcroutes.yaml \
    | kubectl apply -f -
    

The output is similar to:
    
    
    customresourcedefinition.apiextensions.k8s.io/grpcroutes.gateway.networking.k8s.io created
    

## What's next

  * [Set up an Envoy sidecar service mesh on GKE](https://docs.cloud.google.com/service-mesh/v1.22/docs/gateway/set-up-envoy-mesh)
  * [Set up a proxyless gRPC service mesh on GKE](https://docs.cloud.google.com/service-mesh/v1.22/docs/gateway/proxyless-grpc-mesh)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
