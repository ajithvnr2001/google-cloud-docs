---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-multinetwork-loadbalancer-services/
title: Multi-network LoadBalancer Services \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:02:48.298983+00:00
---

# Multi-network LoadBalancer Services  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-multinetwork-loadbalancer-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Multi-network LoadBalancer Services Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

GKE multi-networking lets you connect your workloads to multiple VPC networks. You can expose these multi-network Pods to internal or external clients by using a Kubernetes Service of `type: LoadBalancer`. GKE provisions a Google Cloud L4 load balancer for the Service that sends traffic to Pods on a specified secondary network.

This document explains how GKE implements `LoadBalancer` Services for multi-network Pods. It covers the required configuration, capabilities, and limitations of the feature.

## How multi-network LoadBalancer Services work

To expose a multi-network workload, you create a `Service` of `type: LoadBalancer`. This Service must include a special selector that targets Pods based on the network of their secondary interface. You also add an annotation to specify whether to create an internal or external load balancer.

The `networking.gke.io/network` label in the selector filters endpoints by network. This ensures that the load balancer only sends traffic to the Pod interfaces connected to the specified network.

### Internal LoadBalancer Service

To create an internal load balancer, add the `networking.gke.io/load-balancer-type: "Internal"` annotation to your Service manifest. The following example shows a Service that creates an internal load balancer to target Pods on the `dmz` network:
    
    
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
      - port: 80
        protocol: TCP
        targetPort: 8080
      selector:
        networking.gke.io/network: dmz
        app: web-app
      type: LoadBalancer
    

### External LoadBalancer Service

To create an external network load balancer, you must configure a backend service-based load balancer. In GKE 1.37 and later, this is the default behavior. In earlier versions, add the `cloud.google.com/l4-rbs: enabled` annotation to your Service manifest. The following example shows a Service that creates an external load balancer to target Pods on the `dmz` network:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: web-app-external-lb
      namespace: default
      annotations:
        cloud.google.com/l4-rbs: enabled
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
    

## Pod and network configuration

Your Pods must have an interface in the network that the `LoadBalancer` Service targets. You also must configure routing within the Pod so that it can correctly respond to requests on the appropriate network interface.

You can configure Pod routing in one of the following ways:

  * **Set a default interface** : Use the `networking.gke.io/default-interface` annotation on the Pod to set the secondary network interface as the default route.

  * **Configure policy-based routing** : Use an `initContainer` with the `NET_ADMIN` capability to configure routing rules inside the Pod.




The following example shows a `Deployment` manifest for Pods with an interface on the `dmz` network. The `networking.gke.io/default-interface` annotation sets the `dmz` interface (`eth1`) as the default route.
    
    
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
            networking.gke.io/interfaces: |-
              [
                {"interfaceName":"eth0","network":"default"},
                {"interfaceName": "eth1","network": "dmz"}
              ]
        spec:
          containers:
          -   name: whereami
            image: us-docker.pkg.dev/google-samples/containers/gke/whereami:v1
            ports:
            -   containerPort: 8080
    

## Verifying multi-network endpoints

GKE uses a dedicated controller, `multinet-endpointslice-controller.gke.io`, to manage endpoints for multi-network Services. This controller creates `EndpointSlice` objects for your multi-network Services. The IP addresses in these `EndpointSlice` objects belong to the secondary network specified in the Service selector.

If a load balancer has no healthy backends, inspect the `EndpointSlice` for the Service to verify that the controller has selected the correct Pod IP addresses. If the `EndpointSlice` has no endpoints, check that the Service selector labels match your running Pods and that the `networking.gke.io/network` selector matches the network of the Pods.

## Limitations

Multi-network `LoadBalancer` Services have the following limitations:

  * Internal load balancers require GKE subsetting.
  * Target pool or instance group-based load balancers are not supported.
  * Services that use `externalTrafficPolicy: Cluster` are not supported.
  * Services cannot target `hostNetwork` Pods.
  * IPv6 and dual-stack networking are not supported.
  * You cannot change the network of an existing Service.
  * Only Layer 3 networks are supported.



## What's next

  * Learn how to deploy multi-network services by following the [Multi-Network Services User Guide](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-multinetwork-loadbalancer-services). 
    * Read the [GKE Multi-Network User Guide](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods) for information on how to prepare VPCs and create a GKE cluster with additional networks.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
