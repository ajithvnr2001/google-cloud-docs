---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-multinetwork-loadbalancer-services/
title: Deploy multi-network LoadBalancer Services \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:27:38.179502+00:00
---

# Deploy multi-network LoadBalancer Services  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-multinetwork-loadbalancer-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Deploy multi-network LoadBalancer Services Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document shows how to expose multi-network Pods to internal or external clients by creating Google Cloud regional external passthrough Network Load Balancer and internal passthrough Network Load Balancer resources in GKE. It describes the required configuration, capabilities, and limitations of multi-network `LoadBalancer` Services.

If you connect workloads to multiple VPC networks, use a Kubernetes Service of type `LoadBalancer` to route traffic to Pods on a specific secondary network. When you create the Service, GKE creates a passthrough Network Load Balancer to manage this traffic.

For more information about multi-networking in GKE, see [About multi-network support for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-multinetwork-support-for-pods).

## How multi-network LoadBalancer services work

To expose a multi-network workload, create a `Service` of `type: LoadBalancer`. The Service must include a special selector that targets Pods based on the network of their secondary interface. Add an annotation to specify whether to create an internal or external load balancer.

The `networking.gke.io/network` label in the selector filters endpoints by network. This label ensures that the load balancer only sends traffic to the Pod interfaces connected to the specified network.

## Limitations

Multi-network load balancers have the following limitations:

  * Services that use `externalTrafficPolicy: Cluster` aren't supported.
  * Services that target `hostNetwork` Pods aren't supported.
  * IPv6 and dual-stack networking aren't supported.
  * You can't change the network of an existing Service.
  * Only Layer 3 networks are supported.
  * Load balancers based on target pools or instance group backends aren't supported.
  * ClusterIP and NodePort Services aren't supported on secondary (non-default) networks.



## Before you begin

Before you begin, complete the following tasks:

  1. Follow the steps in [Set up multi-network support for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods) to prepare your VPC networks and create a GKE cluster with an additional network.
  2. Ensure that your cluster has subsetting for Layer 4 Internal Load Balancers enabled. To enable this feature, use the `--enable-l4-ilb-subsetting` flag when you create or update the cluster.
  3. Ensure that your cluster is running GKE version 1.36 or later.



## Deploy multi-network Pods

To attach Pods to an additional network, create a Deployment with the `networking.gke.io/interfaces` annotation. This annotation specifies the networks and interfaces for the Pods.

  1. Save the following manifest as `web-app-deployment.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: web-app
           labels:
             app: web-app
         spec:
           replicas: 3
           selector:
             matchLabels:
               app: web-app
           template:
             metadata:
               labels:
                 app: web-app
               annotations:
                 networking.gke.io/default-interface: 'eth1'
                 networking.gke.io/interfaces: '[
                   {"interfaceName":"eth0","network":"default"},
                   {"interfaceName": "eth1","network": "dmz"}
                 ]'
         spec:
           containers:
           - name: whereami
             image: us-docker.pkg.dev/google-samples/containers/gke/whereami:v1
             ports:
             - containerPort: 8080
         

This manifest creates a Deployment named `web-app` with three Pods. The Pods have two interfaces: `eth0` connected to the `default` network and `eth1` connected to the `dmz` network. The `networking.gke.io/default-interface` annotation sets `eth1` as the default interface for the Pods.

  2. Apply the manifest to your cluster:
         
         kubectl apply -f web-app-deployment.yaml
         




If you use a non-default interface for your Service, you must configure routing within the Pod. To configure routing, add an `initContainer` to your Pod specification that has the `NET_ADMIN` capability.

The following example shows an `initContainer` that adds a default route for the `eth1` interface:
    
    
    initContainers:
          - name: init-routes-busybox
            image: busybox
            command: ['sh', '-c', 'ip route add default dev eth1 table 200 && ip rule add from 172.16.1.0/24 table 200']
            securityContext:
              capabilities:
                add: ["NET_ADMIN"]
    

In the `initContainer` command, replace `172.16.1.0/24` with the secondary IP address range of your Pod network.

## Deploy an internal LoadBalancer Service

To expose the `web-app` Deployment on the `dmz` network, create an internal LoadBalancer Service.

  1. Save the following manifest as `internal-lb-service.yaml`:
         
         apiVersion: v1
         kind: Service
         metadata:
           name: web-app-internal-lb
           namespace: default
           annotations:
             networking.gke.io/load-balancer-type: "Internal"
         spec:
           externalTrafficPolicy: Local
           ports:
           -   port: 80
             protocol: TCP
             targetPort: 8080
           selector:
             networking.gke.io/network: dmz
             app: web-app
           type: LoadBalancer
         

This manifest creates a Service with the following properties:

     * `networking.gke.io/load-balancer-type: "Internal"`: Specifies an internal passthrough Network Load Balancer.
     * `selector`: Selects Pods with the label `app: web-app` that are connected to the `dmz` network.
  2. Apply the manifest to your cluster:
         
         kubectl apply -f internal-lb-service.yaml
         




## Deploy an external LoadBalancer Service

To expose the `web-app` Deployment to external clients, create an external LoadBalancer Service.

  1. Save the following manifest as `external-lb-service.yaml`:
         
         apiVersion: v1
         kind: Service
         metadata:
           name: web-app-external-lb
           namespace: default
           annotations:
             cloud.google.com/l4-rbs: "enabled"
         spec:
           externalTrafficPolicy: Local
           ports:
           -   port: 80
             protocol: TCP
             targetPort: 8080
           selector:
             networking.gke.io/network: dmz
             app: web-app
           type: LoadBalancer
         

This manifest creates a Service with the following properties:

     * `cloud.google.com/l4-rbs: "enabled"`: specifies a backend service-based external passthrough Network Load Balancer. In GKE 1.37 and later, this configuration is the default and the annotation is not required.
     * `selector`: selects Pods with the label `app: web-app` that are connected to the `dmz` network.
  2. Apply the manifest to your cluster:
         
         kubectl apply -f external-lb-service.yaml
         




## Verify the Services

After you deploy the Services, verify that the load balancers are created and configured correctly.

  1. Check the status of the Services:
         
         kubectl get services
         

The output is similar to the following:
         
         NAME                  TYPE           CLUSTER-IP    EXTERNAL-IP     PORT(S)        AGE
         web-app-external-lb   LoadBalancer   10.8.47.77    35.239.57.231   80:31550/TCP   5m
         web-app-internal-lb   LoadBalancer   10.8.43.251   172.16.0.43     80:32628/TCP   6m
         kubernetes            ClusterIP      10.8.32.1     <none>          443/TCP        43h
         

The `EXTERNAL-IP` address for the internal load balancer belongs to the `dmz` network.

  2. List the forwarding rules in your project:
         
         gcloud compute forwarding-rules list
         

The output is similar to the following:
         
         NAME                                                   REGION        IP_ADDRESS     IP_PROTOCOL  TARGET
         af901673cc0f24907a6aa8c3ce4afc21                       us-central1   35.239.57.231  TCP          us-central1/backendServices/k8s2-xhvzqabw-default-web-app-external-lb-u4xbs4ot
         k8s2-tcp-xhvzqabw-default-web-app-internal-lb-vp1x1d6a us-central1   172.16.0.43    TCP          us-central1/backendServices/k8s2-xhvzqabw-default-web-app-internal-lb-vp1x1d6a
         

  3. Describe the forwarding rule for the internal load balancer to verify that it is attached to the correct network:
         
         gcloud compute forwarding-rules describe k8s2-tcp-xhvzqabw-default-web-app-internal-lb-vp1x1d6a --region=$REGION
         

Replace `REGION` with the region of your cluster.

The output is similar to the following. Verify that the `network` and `subnetwork` fields match the details of the `dmz` network.
         
         IPAddress: 172.16.0.43
         IPProtocol: TCP
         ...
         loadBalancingScheme: INTERNAL
         name: k8s2-tcp-xhvzqabw-default-web-app-internal-lb-vp1x1d6a
         network: https://www.googleapis.com/compute/v1/projects/projectId/global/networks/dmz-vpc
         ...
         subnetwork: https://www.googleapis.com/compute/v1/projects/projectId/regions/us-central1/subnetworks/dmz-subnet
         




## Test the load balancers

  1. To test the external load balancer, send a request to its external IP address:
         
         curl EXTERNAL_LB_IP:80
         

Replace `EXTERNAL_LB_IP` with the external IP address of the `web-app-external-lb` Service.

  2. To test the internal load balancer, send a request from a host in the same VPC as the load balancer:
         
         curl INTERNAL_LB_IP:80
         

Replace `INTERNAL_LB_IP` with the IP address of the `web-app-internal-lb` Service.




## Troubleshooting

This section describes how to troubleshoot issues with multi-network load balancers.

### Load balancer creation fails

If load balancer creation fails, check the Service events for error messages:
    
    
    kubectl describe service SERVICE_NAME
    

Replace `SERVICE_NAME` with the name of your Service.

An error message such as `network some-other-network does not exist` indicates that the network specified in the Service selector isn't defined in the cluster. Verify that the network exists:
    
    
    kubectl get networks
    

If the network exists, verify that the `Network` object correctly references a valid `GKENetworkParamSet` resource. To check for configuration errors, inspect the `Network` resource status:
    
    
    kubectl get networks NETWORK_NAME -o yaml
    

Replace `NETWORK_NAME` with the name of your network.

In a valid configuration, both the `ParamsReady` and `Ready` conditions are `True`. If `ParamsReady` isn't `True`, make sure that the `parametersRef` in the `Network` specification correctly matches the name, kind, and group of an existing `GKENetworkParamSet` resource.

If the `Network` resource is correct but still isn't ready, check the status of the referenced `GKENetworkParamSet` for errors, such as a missing subnet:
    
    
    kubectl get gkenetworkparamsets GNP_NAME -o yaml
    

Replace `GNP_NAME` with the name of your `GKENetworkParamSet`.

### Load balancer has no backends

If the load balancer is provisioned but has no healthy backends, do the following:

  1. Verify that a node pool exists with network interfaces in the network that the Service uses.
  2. Verify that the Pods selected by the Service are running.
  3. Check the endpoints for the Service:
         
         kubectl describe endpointslice -l kubernetes.io/service-name=SERVICE_NAME
         

The `multinet-endpointslice-controller.gke.io` controller creates the multi-network endpoints. The Pod IP addresses listed in the EndpointSlice belong to the network that the Service uses. If the EndpointSlice has no endpoints, verify that the Service selector labels match running Pods and that the network selector matches the network of the Pods.




## What's next

  * Learn about [multi-network support for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-multinetwork-support-for-pods).
  * Learn about [multi-network Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-multinetwork-loadbalancer-services).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
