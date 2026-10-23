---
url: https://docs.cloud.google.com/service-mesh/v1.24/docs/operate-and-maintain/hybrid-mesh/
title: Set up a hybrid mesh \u00a0|\u00a0 Cloud Service Mesh v1.24 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:57.798645+00:00
---

# Set up a hybrid mesh  |  Cloud Service Mesh v1.24  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.24/docs/operate-and-maintain/hybrid-mesh/

You are viewing archived v1.24 Service Mesh documentation.

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
  * [ v1.24 ](https://docs.cloud.google.com/service-mesh/v1.24/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.24/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up a hybrid mesh

**Preview — Hybrid and mesh**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.24/docs/overview).

This page explains how to set up a hybrid mesh for the following platforms:

  * Hybrid: GKE on Google Cloud and Google Distributed Cloud (software only) for VMware
  * Hybrid: GKE on Google Cloud and Google Distributed Cloud (software only) for bare metal



By following these instructions you set up two clusters, but you can extend this process to incorporate any number of clusters into your mesh.

## Prerequisites

  * All clusters must be registered to the same [fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
  * All GKE clusters must be in a [shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) configuration on the same network.
  * The cluster's Kubernetes control plane address and the gateway address need to be reachable from every cluster in the mesh. The Google Cloud project in which GKE clusters are located should be allowed to create [external load balancing types](https://docs.cloud.google.com/load-balancing/docs/org-policy-constraints). We recommend that you use [authorized networks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks) and [VPC firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls) to restrict the access.
  * Private clusters, including GKE private clusters, are not supported. If you use On-Premises clusters including Google Distributed Cloud (software only) for VMware and Google Distributed Cloud (software only) for bare metal, the Kubernetes control plane address and the gateway address need to be reachable from pods in GKE clusters. We recommend that you use [CloudVPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) to connect the GKE cluster's subnet with the On-Premises cluster's network.
  * If you use Istio CA, use the same custom root certificate for all clusters.



## Before you begin

You need access to the kubeconfig files for all the clusters that you are setting up in the mesh. For the GKE cluster, in order to create a new kubeconfig file for the cluster, you can export `KUBECONFIG` env with the complete path of file as value in your terminal and generate the kubeconfig entry.

**Warning:** Only use kubeconfig files from trusted sources. Using a specially-crafted kubeconfig file could result in malicious code execution or file exposure. If you must use an untrusted kubeconfig file, inspect it carefully first, much as you would a shell script.

### Set up environment variables and placeholders

You need the following environment variables when you install the east-west gateway.

  1. Create an environment variable for the project number. In the following command, replace FLEET_PROJECT_ID with the project ID of the [fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
         
         export PROJECT_NUMBER=$(gcloud projects describe FLEET_PROJECT_ID --format="value(projectNumber)")
         

  2. Create an environment variable for the mesh identifier.
         
         export MESH_ID="proj-${PROJECT_NUMBER}"
         

  3. Create environment variables for the network names.

     * GKE clusters default to the cluster network name:

export NETWORK_1="PROJECT_ID-CLUSTER_NETWORK"

     * Other clusters use `default`:

export NETWORK_2="default"

Note that If you installed Cloud Service Mesh on other clusters with different values for `--network_id`, then you should pass the same values to value to NETWORK_2.




## Install the east-west gateway

  1. Install a gateway in CLUSTER_1 (your GKE cluster) that is dedicated to [east-west](https://en.wikipedia.org/wiki/East-west_traffic) traffic to CLUSTER_2 (your on-premise cluster):
         
         asm/istio/expansion/gen-eastwest-gateway.sh \
             --mesh ${MESH_ID} \
             --network ${NETWORK_1}  \
             --revision asm-1246-12 | \
             ./istioctl --kubeconfig=PATH_TO_KUBECONFIG_1 install -y -f -
         

Note that this gateway is public on the Internet by default. Production systems might require additional access restrictions, for example firewall rules, to prevent external attacks.

  2. Install a gateway in CLUSTER_2 that is dedicated to east-west traffic for CLUSTER_1.
         
         asm/istio/expansion/gen-eastwest-gateway.sh \
             --mesh ${MESH_ID} \
             --network ${NETWORK_2} \
             --revision asm-1246-12 | \
             ./istioctl --kubeconfig=PATH_TO_KUBECONFIG_2 install -y -f -
         




## Expose services

Since the clusters are on separate networks, you need to expose all services (`\*.local`) on the east-west gateway in both clusters. While this gateway is public on the internet, services behind it can only be accessed by services with a trusted mTLS certificate and workload ID, just as if they were on the same network.

Expose services via the east-west gateway for every cluster
    
    
        kubectl --kubeconfig=PATH_TO_KUBECONFIG_1 apply -n istio-system -f \
            asm/istio/expansion/expose-services.yaml
        kubectl --kubeconfig=PATH_TO_KUBECONFIG_2 apply -n istio-system -f \
            asm/istio/expansion/expose-services.yaml
    

## Enable endpoint discovery

**Note:** For more information on endpoint discovery, refer to [Endpoint discovery with multiple control planes](https://istio.io/v1.24/docs/ops/deployment/deployment-models/#endpoint-discovery-with-multiple-control-planes).

Run the `asmcli create-mesh` command to enable endpoint discovery. This example only shows two clusters, but you can run the command to enable endpoint discovery on additional clusters, subject to the [GKE Hub service limit](https://docs.cloud.google.com/anthos/fleet-management/docs/quotas).
    
    
      ./asmcli create-mesh \
          FLEET_PROJECT_ID \
          PATH_TO_KUBECONFIG_1 \
          PATH_TO_KUBECONFIG_2
    

## Verify multi-cluster connectivity

See [Injecting sidecar proxies](https://docs.cloud.google.com/service-mesh/v1.24/docs/onboarding/kubernetes-workloads#inject_sidecar_proxies).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
