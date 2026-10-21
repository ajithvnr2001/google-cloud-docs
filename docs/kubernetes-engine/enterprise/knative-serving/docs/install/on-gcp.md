---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/on-gcp/
title: Installing Knative serving on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:21:24.751737+00:00
---

# Installing Knative serving on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/on-gcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Installing Knative serving on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to install Knative serving in your GKE clusters on Google Cloud. Knative serving now uses Cloud Service Mesh and GKE Enterprise fleets. [Learn what's new and changed with Knative serving fleet installations](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install). Warning: Performing the steps on this page will perform a new installation of Knative serving and irreversibly overwrite your previous non-fleet installation. Do not proceed with the following steps in your [clusters for which you previously enabled Knative serving](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/setup).   
  
For previous "free-trial" installations of Knative serving, you must first [upgrade Knative serving to use GKE Enterprise fleets](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/on-gcp/upgrade). 

Use this page to install the default components of Knative serving on your GKE clusters in Google Cloud with the following configuration:

  * Knative serving on Google Cloud is configured for public clusters by default.

  * Cloud Monitoring metrics for GKE Enterprise on Google Cloud clusters are enabled by default.




## Before you begin

  * To install Knative serving in private clusters on Google Cloud, you must perform a [custom installation](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/on-gcp/custom).

  * You must ensure that you meet the [installation prerequisites](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/on-gcp/prerequisites).

  * If Knative serving is installed in your cluster, you must ensure that the "_GKE add-on_ " does not exist before you perform these fleet component installation steps. If you have the "_add-on_ " installed, you must instead [follow the steps for upgrading to GKE Enterprise fleets](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/on-gcp/upgrade). 

#### Check if the "_GKE add-on_ " is installed.

To check if your installation of Knative serving is the "_GKE add-on_ ", run the following command: 
        
        gcloud container clusters describe \
        CLUSTER_NAME \
        --region CLUSTER_LOCATION \
        --project PROJECT_ID --format='get(addonsConfig.cloudRunConfig)'

Replace: 

    * CLUSTER_NAME with the name of your cluster.
    * CLUSTER_LOCATION with the [location](https://docs.cloud.google.com/compute/docs/regions-zones#identifying_a_region_or_zone) where your cluster is located.
    * PROJECT_ID with the ID of your Google Cloud project.

Results: 

    * **"_GKE add-on_ " not installed**: 
      * Nothing is returned to your terminal if the add-on was never installed.
      * `disabled=true` is returned if the add-on was previously uninstalled.
    * **"_GKE add-on_ " is installed**: If the add-on is installed in your cluster, the configuration details for the add-on are returned. Example: `loadBalancerType=LOAD_BALANCER_TYPE_EXTERNAL`

Example:
     The following example demonstrates that Knative serving was installed in the `my-addon-cluster` cluster through the "_GKE add-on_ ", which is configured to handle external traffic: 
    
    gcloud container clusters describe **my-addon-cluster** \
    --region **us-central1-c** --project **my-gcp-project** \
    --format='get(addonsConfig.cloudRunConfig)'

Response: 
    
    loadBalancerType=LOAD_BALANCER_TYPE_EXTERNAL




## Installing Knative serving

To install the default components of Knative serving:

  1. Enable Knative serving in your fleet:
         
         gcloud container fleet cloudrun enable --project=PROJECT_ID
         

Replace PROJECT_ID with the ID of your Google Cloud project.

For details and additional options, see the [gcloud container fleet cloudrun enable](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/cloudrun/enable) reference.

  2. Optional: Verify that the Knative serving feature component is enabled:

### Console

View if the Knative serving component is **Enabled** in the Google Cloud console:

[Go to Feature Manager](https://console.cloud.google.com/kubernetes/features)

### Command line

View if the `appdevexperience` state is `ACTIVE`:
         
         gcloud container fleet features list  --project=PROJECT_ID
         

Replace PROJECT_ID with the ID of your Google Cloud project.

For details and additional options, see the [gcloud container fleet features list](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/features/list) reference.

Result:
         
         NAME               STATE
         appdevexperience   ACTIVE
         

  3. For each GKE Enterprise cluster where you want to install Knative serving, run the corresponding command: 
         
         gcloud container fleet cloudrun apply --gke-cluster=CLUSTER_LOCATION/CLUSTER_NAME
         

Replace the following:

     * CLUSTER_LOCATION with the [region or zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) in which your cluster is located.
     * CLUSTER_NAME with the ID of your cluster or the fully qualified identifier for the cluster. 

For details and additional options, see the [gcloud container fleet cloudrun apply](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/cloudrun/apply) reference.

  4. Verify that Knative serving has been enabled in your cluster: 
     1. Open the Google Cloud console: 

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

     2. Click on the name of your cluster to open the details pane. 

     3. Run this command to check if you can see the Knative serving version details: `kubectl get all -n knative-serving -o 'go-template={{index .metadata.labels "serving.knative.dev/release"}}'`
     4. Verify that all Knative serving specific deployments are in running status under `knative-serving` and `appdevexperience` namespaces. 



## What's next

[Set up your installation of Knative serving](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/setup).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
