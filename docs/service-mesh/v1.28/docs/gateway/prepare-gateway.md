---
url: https://docs.cloud.google.com/service-mesh/v1.28/docs/gateway/prepare-gateway/
title: Prepare to setup the Gateway API for Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:08:50.582612+00:00
---

# Prepare to setup the Gateway API for Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.28/docs/gateway/prepare-gateway/

You are viewing v1.28 Service Mesh documentation.

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
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.28/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.28/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Prepare to setup the Gateway API for Cloud Service Mesh 

This page describes how to install the required custom resource definitions for the gateway into your cluster.

## Limitations

  * Having a mix of `gateway` config-api and `istio` config-api clusters in the same fleet is not supported. Make sure the config-api is set to `gateway` for all the clusters in your fleet. Use the `gcloud container fleet mesh describe --project FLEET_PROJECT_ID` command to see what you have configured for your fleet. 
  * Multi-cluster service discovery and load balancing is not supported for `gateway` config-api clusters.
  * If a cluster is onboarded using the existing `--management automatic` flag then the cluster starts using the `istio` configuration API and cannot change to `gateway` API.
  * Only FQDNs are supported. Short names are not supported.



## Data plane management considerations

For new pods, Google manages which proxy version is injected. Note that the managed data plane relies on the Google Kubernetes Engine (GKE) release channel to determine the proxy version.

For existing pods, proxy management is done passively, driven by the natural lifecycle of the pods in the cluster. To trigger the update and re-inject new versions of the proxy, restart your workloads.

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




## Create and register a GKE cluster

### gcloud

Create a GKE cluster:
    
    
    gcloud container clusters create CLUSTER_NAME \
    --location=LOCATION \
    --enable-ip-alias \
    --scopes=https://www.googleapis.com/auth/cloud-platform \
    --release-channel=regular \
    --project=PROJECT_ID \
    --gateway-api=standard \
    --workload-pool=PROJECT_ID.svc.id.goog \
    --workload-metadata=GKE_METADATA
    

where:

  * CLUSTER_NAME is the name of your cluster
  * LOCATION is the location of your cluster
  * PROJECT_ID is the project ID of your cluster



### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click _add_box_ **Create**.

  3. In the **Standard** section, click **Configure**.

  4. In the **Cluster basics** section, complete the following:

     1. Enter the **Name** for your cluster.
     2. For the **Location type** , select a [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for your cluster.
  5. In the navigation pane, click **default-pool** under **Node Pools** section, and select **Security**.

  6. In the **Access scopes** list, select **Set access for each API** , and set **Cloud Platform** as **Enabled**.

  7. In the navigation pane, click **Networking**.

  8. In the **Load Balancer, Ingress, and Gateway** section, select **Enable Gateway API**.

  9. In the navigation pane, click **Advanced settings**.

  10. In the **Workload identity** row, verify that **Details** shows **Enabled**. If it shows **Disabled** , click _edit_ **Edit feature configuration** , select **Enable Workload Identity** , and then click **Save**.

  11. Click **Create**.




After the cluster is created,

  1. Register your cluster to a [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs#introducing_fleets):
         
         gcloud container fleet memberships register CLUSTER_NAME \
         --gke-cluster LOCATION/CLUSTER_NAME \
         --project=PROJECT_ID
         

  2. Verify that the cluster is registered to the fleet:
         
         gcloud container fleet memberships list --project=PROJECT_ID
         

The output is similar to:
         
         NAME            EXTERNAL_ID                             LOCATION
         my-cluster      91980bb9-593c-4b36-9170-96445c9edd39    us-west1
         




## Set up permissions

Note that the following commands grant permission to all authenticated users, but you can use Workload Identity Federation for GKE to grant permission to only select accounts. For details on how Workload Identity Federation for GKE works, see [About Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity). To configure Workload Identity Federation for GKE, see [Authenticate to Google Cloud APIs from GKE workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity).

Grant the `trafficdirector.client` role:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member "group:PROJECT_ID.svc.id.goog:/allAuthenticatedUsers/" \
        --role "roles/trafficdirector.client"
    

## Enable Cloud Service Mesh

  1. Enable the mesh feature:
         
         gcloud container fleet mesh enable --project PROJECT_ID
         

  2. Update the mesh to use the Gateway API:
         
         gcloud alpha container fleet mesh update \
         --config-api gateway \
         --memberships CLUSTER_NAME \
         --project PROJECT_ID
         

  3. Verify the update by describing the status of Cloud Service Mesh resource:
         
         gcloud alpha container fleet mesh describe \
         --project PROJECT_ID
         




## Set your fleet new memberships to use the Gateway API by default (optional)

Alternatively, you can create [fleet-level default settings](https://docs.cloud.google.com/service-mesh/v1.28/docs/onboarding/provision-control-plane#configure_your_fleet) for new GKE clusters registered to the fleet during cluster creation to be automatically configured with Gateway API.

  1. Create a YAML file specifying using Gateway API:
         
         echo "configapi: gateway" > mesh.yaml
         

**Note:** `management` and `config-api` shouldn't be configured at the same time.
  2. Update your mesh:
         
         gcloud alpha container fleet mesh update --project FLEET_PROJECT_ID \
             --fleet-default-member-config mesh.yaml
         

  3. Create a cluster and register them to your fleet in one step to use the default configuration:
         
         gcloud container clusters create CLUSTER_NAME \
             --project PROJECT_ID \
             --fleet-project FLEET_PROJECT_ID \
             --location=LOCATION \
         

  4. Enable Workload Identity Federation for GKE and run the GKE Metadata Server on your node.




## Install custom resource definitions

Generate a kubeconfig entry for your cluster: 
    
    
    gcloud container clusters get-credentials CLUSTER_NAME --location LOCATION --project PROJECT_ID
    

where:

  * CLUSTER_NAME is the name of your cluster
  * LOCATION is the location of your cluster
  * PROJECT_ID is the project ID of your cluster



Install the GRPCRoute custom resource definition (CRD):
    
    
    curl https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.1.0/config/crd/standard/gateway.networking.k8s.io_grpcroutes.yaml \
    | kubectl apply -f -
    

The output is similar to:
    
    
    customresourcedefinition.apiextensions.k8s.io/grpcroutes.gateway.networking.k8s.io created
    

## What's next

  * [Set up an Envoy sidecar service mesh on GKE](https://docs.cloud.google.com/service-mesh/v1.28/docs/gateway/set-up-envoy-mesh)
  * [Set up a proxyless gRPC service mesh on GKE](https://docs.cloud.google.com/service-mesh/v1.28/docs/gateway/proxyless-grpc-mesh)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
