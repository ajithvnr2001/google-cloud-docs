---
url: https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/external-lb-gateway/
title: Expose an ingress gateway using an external load balancer \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:58.342487+00:00
---

# Expose an ingress gateway using an external load balancer  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/external-lb-gateway/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Expose an ingress gateway using an external load balancer

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

## Overview

With Cloud Service Mesh you can deploy and manage ingress gateways as part of your service mesh. You can further configure load balancing for your cluster with Cloud Service Mesh by using external load balancers (physical or software load balancers outside of the cluster) to send traffic to the ingress gateway.

This page shows you how to configure an external load balancer with Cloud Service Mesh. Alternatively, you can [set up ingress with multiple backend configs](https://github.com/GoogleCloudPlatform/gke-networking-recipes/tree/main/ingress/single-cluster/ingress-asm-multi-backendconfig).

## Before you begin 

To complete the steps in this document you need the following resources:

  * A Kubernetes cluster with Cloud Service Mesh installed.

  * An external load balancer that can access the nodes where your cluster is running. You configure this external load balancer to front the ingress gateway of your cluster using the load balancer's external IP address.




## Set up your environment

Run the following commands from a workstation that can access the cluster you intend to use. Make sure that the `kubectl` tool is configured to use the cluster context specific to your cluster.

  1. Set the environment variables.
         
         export ASM_INGRESSGATEWAY_NAMESPACE=asm-ingressgateway
         export ASM_INGRESSGATEWAY_DEPLOYMENT_NAME=asm-ingressgateway
         export ASM_INGRESSGATEWAY_SERVICE_NAME=asm-ingressgateway
         export ASM_INGRESSGATEWAY_NODE_LABEL=asm-ingressgateway
         

  2. Set the `IP address` of the external load balancer.
         
         export EXTERNAL_LB_IP_ADDRESS=EXTERNAL_LB_IP_ADDRESS
         

  3. [\Optional/] Label the ingress gateway nodes. This ensures that the gateway gets deployed to specific nodes in the cluster.
         
         kubectl label nodes INGRESSGATEWAY_NODE_IP ${ASM_INGRESSGATEWAY_NODE_LABEL}=
         

     * INGRESSGATEWAY_NODE_IP: is the node(s) in your Kubernetes cluster that hosts the ingress gateway. Run this `kubectl` command for as many ingress nodes you have.



## Create the ingress gateway

Before you complete the instructions in this section, you'll need to determine your control plane implementation. Use the instructions in [Identify control plane implementation](https://docs.cloud.google.com/service-mesh/docs/supported-features-managed#identify_control_plane_implementation) to do this.

  1. Create the namespace. This namespace is used to deploy the ingress gateway.
         
         kubectl create namespace ${ASM_INGRESSGATEWAY_NAMESPACE}
         



  1. Enable the namespace for injection. The steps depend on your [control plane implementation](https://docs.cloud.google.com/service-mesh/docs/check-control-plane-implementation).

### Managed (TD)

     1. Apply the default injection label to the namespace:
    
    kubectl label namespace ${ASM_INGRESSGATEWAY_NAMESPACE} \
        istio.io/rev- istio-injection=enabled --overwrite
    

### Managed (Istiod)

**Caution:** Managed Cloud Service Mesh using the `ISTIOD` control plane implementation is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). You must [modernize](https://docs.cloud.google.com/service-mesh/docs/modernization) all managed `ISTIOD` fleets to the `TRAFFIC_DIRECTOR` control plane implementation. 

**Recommended:** Run the following command to apply the default injection label to the namespace:
    
    kubectl label namespace ${ASM_INGRESSGATEWAY_NAMESPACE} \
          istio.io/rev- istio-injection=enabled --overwrite
    

**If you are an existing user with the Managed Istiod control plane:** We recommend that you use default injection, but revision-based injection is supported. Use the following instructions:

     1. Run the following command to locate the available release channels:
            
            kubectl -n istio-system get controlplanerevision
            

The output is similar to the following:
            
            NAME                AGE
            asm-managed-rapid   6d7h
            

NOTE: If two control plane revisions appear in the list above, remove one. Having multiple control plane channels in the cluster is not supported.

In the output, the value under the `NAME` column is the revision label that corresponds to the available [release channel](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel#anthos_service_mesh_versions_per_channel) for the Cloud Service Mesh version.

     2. Apply the revision label to the namespace:
            
            kubectl label namespace ${ASM_INGRESSGATEWAY_NAMESPACE} \
                istio-injection- istio.io/rev=REVISION_LABEL --overwrite
            

### In-cluster

**Caution:** In-cluster Cloud Service Mesh using the `ISTIOD` control plane on GKE on Google Cloud is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). Cloud Service Mesh with an in-cluster control plane on Google Distributed Cloud (software only) continues to be supported as described in [Supported platforms](https://docs.cloud.google.com/service-mesh/docs/supported-platforms#off-gcp). 

**Recommended:** Run the following command to apply the default injection label to the namespace:
    
    kubectl label namespace ${ASM_INGRESSGATEWAY_NAMESPACE} \
          istio.io/rev- istio-injection=enabled --overwrite
    

**We recommend that you use default injection, but revision-based injection is supported:** Use the following instructions:

     1. Use the following command to locate the revision label on `istiod`:
            
            kubectl get deploy -n istio-system -l app=istiod -o \
               jsonpath={.items[*].metadata.labels.'istio\.io\/rev'}'{"\n"}'
            

     2. Apply the revision label to the namespace. In the following command, `REVISION_LABEL` is the value of the `istiod` revision label that you noted in the previous step.
            
            kubectl label namespace ${ASM_INGRESSGATEWAY_NAMESPACE} \
                istio-injection- istio.io/rev=REVISION_LABEL --overwrite
            

  2. Apply the [ingress gateway manifest file](https://github.com/GoogleCloudPlatform/anthos-service-mesh-samples/blob/main/docs/ingress-gateway-external-lb/ingress-gateway.yaml).
         
         kubectl --namespace ${ASM_INGRESSGATEWAY_NAMESPACE} apply --filename https://raw.githubusercontent.com/GoogleCloudPlatform/anthos-service-mesh-samples/main/docs/ingress-gateway-external-lb/ingress-gateway.yaml
         

Expected output:
         
         serviceaccount/asm-ingressgateway created
         role.rbac.authorization.k8s.io/asm-ingressgateway created
         rolebinding.rbac.authorization.k8s.io/asm-ingressgateway created
         deployment.apps/asm-ingressgateway created
         service/asm-ingressgateway created
         poddisruptionbudget.policy/asm-ingressgateway created
         horizontalpodautoscaler.autoscaling/asm-ingressgateway created
         

  3. Patch the `ingressgateway` service with the external load balancer IP address.
         
         cat <<EOF > asm-external-ip-patch.yaml
         spec:
           externalIPs:
             - ${EXTERNAL_LB_IP_ADDRESS}
           loadBalancerIP: ${EXTERNAL_LB_IP_ADDRESS}
         EOF
         
         kubectl --namespace ${ASM_INGRESSGATEWAY_NAMESPACE} patch service/${ASM_INGRESSGATEWAY_SERVICE_NAME} --patch "$(cat asm-external-ip-patch.yaml)"
         

  4. [Optional] Patch the `ingressgateway` deployment for the ingress gateway nodes label affinity.
         
         cat <<EOF > asm-ingress-node-label-patch.yaml
         spec:
           template:
             spec:
               affinity:
                 nodeAffinity:
                   requiredDuringSchedulingIgnoredDuringExecution:
                     nodeSelectorTerms:
                     - matchExpressions:
                       - key: ${ASM_INGRESSGATEWAY_NODE_LABEL}
                         operator: Exists
         EOF
         
         kubectl --namespace ${ASM_INGRESSGATEWAY_NAMESPACE} patch deployment/${ASM_INGRESSGATEWAY_DEPLOYMENT_NAME} --patch "$(cat asm-ingress-node-label-patch.yaml)"
         




## Set up the external load balancer

In this section, you configure the external load balancer to connect with the ingress gateway from the cluster.

### Fetch ingress gateway `Service` port information

  1. Get the `NodePorts`.
         
         export HTTP_INGRESS_PORT=$(kubectl --namespace ${ASM_INGRESSGATEWAY_NAMESPACE} get service/${ASM_INGRESSGATEWAY_SERVICE_NAME} --output jsonpath='{.spec.ports[?(@.name=="http2")].nodePort}')
         export HTTPS_INGRESS_PORT=$(kubectl --namespace ${ASM_INGRESSGATEWAY_NAMESPACE} get service/${ASM_INGRESSGATEWAY_SERVICE_NAME} --output jsonpath='{.spec.ports[?(@.name=="https")].nodePort}')
         export STATUS_PORT=$(kubectl --namespace ${ASM_INGRESSGATEWAY_NAMESPACE} get service/${ASM_INGRESSGATEWAY_SERVICE_NAME} --output jsonpath='{.spec.ports[?(@.name=="status-port")].nodePort}')
         

  2. Display the `NodePorts`.
         
         echo HTTP_INGRESS_PORT=${HTTP_INGRESS_PORT}
         echo HTTPS_INGRESS_PORT=${HTTPS_INGRESS_PORT}
         echo STATUS_PORT=${STATUS_PORT}
         




### Configure the external load balancer

Use the `NodePorts` displayed in the previous step to configure connectivity between the external load balancer and the ingress gateway.

  1. Configure the health check in your load balancer configuration.
         
         hosts:    CLUSTER_NODE_IP
         Protocol: HTTP
         Port:     STATUS_PORT
         Path:     /healthz/ready
         

     * CLUSTER_NODE_IP: is the IP address of the nodes in your Kubernetes cluster that hosts the ingress gateway. This IP address must be reachable from your external load balancer. You may have to set up this configuration multiple times, once per cluster node.

     * STATUS_PORT: is the `NodePort` through which the ingress gateway's health status API is exposed. You can copy this information from the previous step. The value is the same for every node in the cluster.

  2. Configure node pools in your load balancer for routing `HTTP` and `HTTPS` traffic. Use the following `IP:PORT` configuration for traffic on port 80 (`HTTP`) and port 443 (`HTTPS`).
         
         80  ->  CLUSTER_NODE_IP:HTTP_INGRESS_PORT
         443 ->  CLUSTER_NODE_IP:HTTPS_INGRESS_PORT
         

     * CLUSTER_NODE_IP: is the IP address of the nodes in your Kubernetes cluster that hosts the ingress gateway. This IP address must be reachable from your external load balancer. You may have to set up this configuration multiple times, once per cluster node.

     * HTTP_INGRESS_PORT: is the `NodePort` through which the ingress gateway's HTTP traffic is exposed. You can copy this information from the previous step. The value is the same for every node in the cluster.

     * HTTPS_INGRESS_PORT: is the `NodePort` through which the ingress gateway's HTTPS traffic is exposed. You can copy this information from the previous step. The value is the same for every node in the cluster.




To verify your set up, ensure that the health checks on your load balancer are passing.

## What's next

  * Read more about [Installing and upgrading gateways](https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/gateways)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
