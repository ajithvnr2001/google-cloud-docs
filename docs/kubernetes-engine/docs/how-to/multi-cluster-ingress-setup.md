---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-ingress-setup/
title: Setting up Multi Cluster Ingress \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:18.632110+00:00
---

# Setting up Multi Cluster Ingress  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-ingress-setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Setting up Multi Cluster Ingress Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Note:** This guide is for the previous Multi-cluster Ingress API (which relies on MultiClusterIngress and MultiClusterService resources). If you are deploying load balancers that use the newer Kubernetes Gateway API (Gateway and HTTPRoute resources), _do not follow this guide_. You must follow [Prepare your environment for multi-cluster Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-environment-multi-cluster-gateways) instead, because Gateway API requires distinct prerequisites and strict cluster initialization sequencing.

This page shows you how to route traffic across multiple Google Kubernetes Engine (GKE) clusters in different regions using [Multi Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress), with an example using two clusters.

For a detailed comparison between Multi Cluster Ingress (MCI), Multi-cluster Gateway (MCG), and load balancer with Standalone Network Endpoint Groups (LB and Standalone NEGs), see [Choose your multi-cluster load balancing API for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-mc-lb-api).

To learn more about deploying Multi Cluster Ingress, see [Deploying Ingress across clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-ingress).

These steps require elevated permissions and should be performed by a GKE administrator.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Requirements and limitations

Multi Cluster Ingress has the following requirements.

  * Google Cloud CLI version requirements:

Multi Cluster Ingress is supported with Google Cloud CLI version 290.0.0 and later. However, [registering your clusters to a fleet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-ingress-setup#fleet-registration) requires Google Cloud CLI version 450.0.0 or higher. Hence ensure that your Google Cloud CLI version is upgraded to 450.0.0 or higher before registering your clusters to a fleet. For more information, see [Install the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk).




If you use Standard mode clusters, ensure that you meet the following requirements. Autopilot clusters already meet these requirements.

  * Clusters must have the `HttpLoadBalancing` add-on enabled. This add-on is enabled by default. You must not disable it because this add-on manages the Ingress controller, which is necessary for Multi Cluster Ingress to function.
  * Clusters must be [VPC-native](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips).
  * Clusters must have [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) enabled.



Multi Cluster Ingress has the following limitations:

  * Only supported with an [external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https).
  * Don't create Compute Engine load balancers in the same project with the prefix `mci-` that are not managed by Multi Cluster Ingress or they will be deleted. Google Cloud uses the prefix `mci-[6 char hash]` to manage the Compute Engine resources that Multi Cluster Ingress deploys.
  * Configuration of HTTPS requires a pre-allocated static IP address. HTTPS is not supported with ephemeral IP addresses.



## Overview

In this exercise, you perform the following steps:

  1. Select the pricing you want to use.
  2. Deploy clusters.
  3. Configure cluster credentials.
  4. Register the clusters to a [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs).
  5. Specify a config cluster. This cluster can be a dedicated control plane, or it can run other workloads.



The following diagram shows what your environment will look like after you complete the exercise:

![Cluster topology showing the relationships between regions, fleet, and project.](https://docs.cloud.google.com/static/kubernetes-engine/images/mci-topology.svg)

In the diagram, there are two GKE clusters named `gke-us` and `gke-eu` in the regions `europe-west1` and `us-central1`. The clusters are registered to a fleet so that the Multi Cluster Ingress controller can recognize them. A fleet lets you logically group and normalize your GKE clusters, making administration of infrastructure easier and enabling the use of multi-cluster features such as Multi Cluster Ingress. You can learn more about the benefits of fleets and how to create them in the [fleet management documentation](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs).

## Enable APIs

Enable the required APIs in your project:
    
    
    gcloud services enable \
        multiclusteringress.googleapis.com \
        gkehub.googleapis.com \
        container.googleapis.com \
        multiclusterservicediscovery.googleapis.com \
        --project=PROJECT_ID
    

**Note:** Your project is billed according to the number of backend Multi Cluster Ingress pods in your project.

## Deploy clusters

Create two GKE clusters named `gke-us` and `gke-eu` in the `europe-west1`and `us-central1` regions.

###  Autopilot 

  1. Create the `gke-us` cluster in the `us-central1` region:
         
         gcloud container clusters create-auto gke-us \
             --location=us-central1 \
             --release-channel=stable \
             --project=PROJECT_ID
         

Replace `PROJECT_ID` with your Google Cloud project ID.

  2. Create the `gke-eu` cluster in the `europe-west1` region:
         
         gcloud container clusters create-auto gke-eu \
             --location=europe-west1 \
             --release-channel=stable \
             --project=PROJECT_ID
         




###  Standard 

Create the two clusters with [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) enabled.

  1. Create the `gke-us` cluster in the `us-central1` region:
         
         gcloud container clusters create gke-us \
             --location=us-central1 \
             --enable-ip-alias \
             --workload-pool=PROJECT_ID.svc.id.goog \
             --release-channel=stable \
             --project=PROJECT_ID
         

Replace `PROJECT_ID` with your Google Cloud project ID.

  2. Create the `gke-eu` cluster in the `europe-west1` region:
         
         gcloud container clusters create gke-eu \
             --location=europe-west1 \
             --enable-ip-alias \
             --workload-pool=PROJECT_ID.svc.id.goog \
             --release-channel=stable \
             --project=PROJECT_ID
         




## Configure cluster credentials

Configure credentials for your clusters and rename the cluster contexts to make it easier to switch between clusters when deploying resources.

  1. Retrieve the credentials for your clusters:
         
         gcloud container clusters get-credentials gke-us \
             --location=us-central1 \
             --project=PROJECT_ID
         
         gcloud container clusters get-credentials gke-eu \
             --location=europe-west1 \
             --project=PROJECT_ID
         

The credentials are stored locally so that you can use your kubectl client to access the cluster API servers. By default, an auto-generated name is created for the credentials.

  2. Rename the cluster contexts:
         
         kubectl config rename-context gke_PROJECT_ID_us-central1_gke-us gke-us
         kubectl config rename-context gke_PROJECT_ID_europe-west1_gke-eu gke-eu
         




## Register clusters to a fleet

Register your clusters to your project's fleet as follows.

**Note:** You can also register clusters from the Google Cloud console. Learn more in [Register a GKE cluster to your fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke#console).

  1. Register your clusters:
         
         gcloud container fleet memberships register gke-us \
             --gke-cluster us-central1/gke-us \
             --enable-workload-identity \
             --project=PROJECT_ID
         
         gcloud container fleet memberships register gke-eu \
             --gke-cluster europe-west1/gke-eu \
             --enable-workload-identity \
             --project=PROJECT_ID
         

  2. Confirm that your clusters have successfully been registered to the fleet:
         
         gcloud container fleet memberships list --project=PROJECT_ID
         

The output is similar to the following:
         
         NAME                                  EXTERNAL_ID
         gke-us                                0375c958-38af-11ea-abe9-42010a800191
         gke-eu                                d3278b78-38ad-11ea-a846-42010a840114
         




After you register your clusters, GKE deploys the `gke-mcs-importer` Pod to your cluster.

You can learn more about registering clusters in [Register a GKE cluster to your fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke).

## Specify a config cluster

The config cluster is a GKE cluster you choose to be the central point of control for Ingress across the member clusters. This cluster must already be registered to the fleet. For more information, see [Config cluster design](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress#config_cluster_design).

**Note:** Even if you have zonal GKE clusters, Multi Cluster Ingress controller is only available in a region. To enable Multi Cluster Ingress, you must specify the region instead of the zone when you use the `--location` parameter.

Enable Multi Cluster Ingress and select `gke-us` as the config cluster:
    
    
    gcloud container fleet ingress enable \
        --config-membership=gke-us \
        --location=us-central1 \
        --project=PROJECT_ID
    

The config cluster takes up to 15 minutes to register. Successful output is similar to the following:
    
    
    Waiting for Feature to be created...done.
    Waiting for controller to start...done.
    

The unsuccessful output is similar to the following:
    
    
    Waiting for controller to start...failed.
    ERROR: (gcloud.container.fleet.ingress.enable) Controller did not start in 2 minutes. Please use the `describe` command to check Feature state for debugging information.
    

If a failure occurred in the previous step, then check the feature state:
    
    
    gcloud container fleet ingress describe \
        --project=PROJECT_ID
    

The successful output is similar to the following:
    
    
    createTime: '2021-02-04T14:10:25.102919191Z'
    membershipStates:
     projects/PROJECT_ID/locations/global/memberships/CLUSTER_NAME:
     state:
       code: ERROR
       description: '...is not a VPC-native GKE Cluster.'
       updateTime: '2021-08-10T13:58:50.298191306Z'
     projects/PROJECT_ID/locations/global/memberships/CLUSTER_NAME:
     state:
       code: OK
       updateTime: '2021-08-10T13:58:08.499505813Z'
    

To learn more about troubleshooting errors with Multi Cluster Ingress, see [Troubleshooting and operations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/troubleshooting-and-ops).

### Impact on live clusters

You can safely enable Multi Cluster Ingress using `gcloud container fleet ingress enable` on a live cluster, as it does not result in any downtime or impact to traffic on the cluster.

## Shared VPC

You can deploy a `MultiClusterIngress` resource for clusters in a Shared VPC network, but all the participating backend GKE clusters must be in the same project. Having GKE clusters in different projects using the same Cloud Load Balancing VIP is not supported.

In non-Shared VPC networks, the Multi Cluster Ingress controller manages firewall rules to allow health checks to pass from the load balancer to container workloads.

In a Shared VPC network, a host project administrator must manually create the firewall rules for load balancer traffic on behalf of the Multi Cluster Ingress controller.

The following command shows the firewall rule that you must create if your clusters are on a Shared VPC network. The source ranges are the ranges that load balancer uses to send traffic to backends. This rule must exist for the operational lifetime of a `MultiClusterIngress` resource.

If your clusters are on a Shared VPC network, create the firewall rule:
    
    
    gcloud compute firewall-rules create FIREWALL_RULE_NAME \
        --project=HOST_PROJECT \
        --network=SHARED_VPC \
        --direction=INGRESS \
        --allow=tcp:0-65535 \
        --source-ranges=130.211.0.0/22,35.191.0.0/16
    

Replace the following:

  * `FIREWALL_RULE_NAME`: the name of the new firewall rule that you choose.
  * `HOST_PROJECT`: the ID of the Shared VPC host project.
  * `SHARED_VPC`: the name of the Shared VPC network.



## Known issues

This section describes known issues for the Multi Cluster Ingress

### InvalidValueError for field config_membership

A known issue prevents the Google Cloud CLI from interacting with Multi Cluster Ingress. This issue was introduced in version 346.0.0 and was fixed in version 348.0.0. We don't recommend using the gcloud CLI versions 346.0.0 and 347.0.0 with Multi Cluster Ingress.

### Invalid value for field 'resource'

Google Cloud Armor cannot communicate with Multi Cluster Ingress [config clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress#architecture) running on the following GKE versions:

  * 1.18.19-gke.1400 and later
  * 1.19.10-gke.700 and later
  * 1.20.6-gke.700 and later



When you [configure a Google Cloud Armor security policy](https://docs.cloud.google.com/armor/docs/configure-security-policies), the following message appears:
    
    
    Invalid value for field 'resource': '{"securityPolicy": "global/securityPolicies/"}': The given policy does not exist
    

To avoid this issue, upgrade your config cluster to version 1.21 or later, or use the following command to update the BackendConfig `CustomResourceDefinition`:
    
    
    kubectl patch crd backendconfigs.cloud.google.com --type='json' -p='[{"op": "replace", "path": "/spec/versions/1/schema/openAPIV3Schema/properties/spec/properties/securityPolicy", "value":{"properties": {"name": {"type": "string"}}, "required": ["name" ],"type": "object"}}]'
    

## What's next

  * Learn how to [deploy Ingress across clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-ingress).
  * Learn more about [Multi Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress).
  * Learn how to [choose your multi-cluster load balancing API for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-mc-lb-api).
  * Learn more about [multi-cluster Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-gateways). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
