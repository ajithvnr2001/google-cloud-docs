---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/kubernetes-network-policies/
title: Configuring Kubernetes network policies \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:38:03.352907+00:00
---

# Configuring Kubernetes network policies  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/kubernetes-network-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Configuring Kubernetes network policies Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.15 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.15 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/kubernetes-network-policies.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/kubernetes-network-policies.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/kubernetes-network-policies.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/kubernetes-network-policies.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/kubernetes-network-policies.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/kubernetes-network-policies.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/kubernetes-network-policies.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/kubernetes-network-policies.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/kubernetes-network-policies.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/kubernetes-network-policies.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/kubernetes-network-policies.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/kubernetes-network-policies.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/kubernetes-network-policies.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/kubernetes-network-policies.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/kubernetes-network-policies.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/kubernetes-network-policies.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/kubernetes-network-policies.html)



This topic explains how to use Kubernetes network policies to secure Cassandra and Redis pods within an Apigee Hybrid Cluster . 

##  Overview 

When you want to control traffic flow at the IP address or port level (OSI layer 3 or 4), then you can use Kubernetes Network Policies for applications in your cluster. Network Policies are an application-centric construct you can use to specify how a pod is allowed to communicate with other pods in your cluster. 

In Apigee hybrid you can use Kubernetes Network Policies to isolate Cassandra pods so that only pods that are intended to communicate with Cassandra are allowed to, such as the Runtime, Synchronizer, and Mart pods. Other pods in the cluster like Ingres and Watcher pods that do not need to communicate with Cassandra are blocked from doing so. 

If you have no restrictions on which pods can interact within your cluster, you do not need to use Kubernetes network policies. 

##  Prerequisites 

  * Enable network policies in your cluster. 
    * **GKE** : See [Enabling network policy enforcement](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy#enabling_network_policy_enforcement). 
    * **EKS** : See [Installing the Calico network policy engine add-on](https://docs.aws.amazon.com/eks/latest/userguide/calico.html). 
    * **AKS** : See [Secure traffic between pods using network policies in Azure Kubernetes Service (AKS) ](https://docs.microsoft.com/en-us/azure/aks/use-network-policies). 
    * Other platforms: look for instructions to enable network policies on your cluster from your specific platform vendor. 
  * A currently running Apigee hybrid cluster, version 1.8 or newer. 



## Procedure

Download and extract the `apigeectl` release package.

**Note:** `apigeectl` is only supported for Apigee hybrid versions 1.11 and older. The following command will download the latest release of `apigeectl` for Apigee hybrid version 1.11.

###  Linux 
    
    
    curl -LO \
      https://storage.googleapis.com/apigee-release/hybrid/apigee-hybrid-setup/**1.11.2** /apigeectl_linux_64.tar.gz

###  Mac OS 
    
    
    curl -LO \
      https://storage.googleapis.com/apigee-release/hybrid/apigee-hybrid-setup/**1.11.2** /apigeectl_mac_64.tar.gz

###  Windows 
    
    
    curl -LO ^
       https://storage.googleapis.com/apigee-release/hybrid/apigee-hybrid-setup/**1.11.2** /apigeectl_windows_64.zip

The configuration files for the Kubernetes network policies for Cassandra and Redis are in the following directory structure within the `apigeectl` directory: 
    
    
      └── apigeectl
          └── examples
              └── network-policies
                  └── securing-cassandra-redis-pods
                      ├── README.md
                      ├── base
                      │   └── cluster-scoped-communication
                      │       ├── cassandra
                      │       │   ├── kustomization.yaml
                      │       │   ├── networkpolicy-cassandra-allow-controller.yaml
                      │       │   ├── networkpolicy-cassandra-allow-intranode.yaml
                      │       │   ├── networkpolicy-cassandra-allow-mart.yaml
                      │       │   ├── networkpolicy-cassandra-allow-runtime.yaml
                      │       │   ├── networkpolicy-cassandra-alow-sync.yaml
                      │       │   ├── networkpolicy-cassandra-create-user.yaml
                      │       │   ├── networkpolicy-cassandra-monitoring.yaml
                      │       │   └── networkpolicy-cassandra-remove-dc.yaml
                      │       └── redis
                      │           ├── kustomization.yaml
                      │           ├── networkpolicy-redis-envoy.yaml
                      │           └── networkpolicy-redis.yaml
                      └── overlays
                          └── ORG_NAME
                              └── kustomization.yaml

Where `ORG_NAME` is the name of your Apigee organization.

  1. Label the namespace with the following command: 
         
         kubectl label namespace APIGEE_NAMESPACE app=apigee

**Note** : Note: You can use any namespace. `apigee` is the default namespace. If you use a different namespace, be sure to replace APIGEE_NAMESPACE with the name of your namespace in the following commands.
  2. Apply the network policies with the following command: 
         
         kubectl apply -k ${APIGEECTL_HOME}/examples/network-policies/securing-cassandra-redis-pods/overlays/ORG_NAME

  3. Validate that the network policies were applied with the following command: 
         
         kubectl get netpol -n APIGEE_NAMESPACE

The following network policies should be created in the APIGEE_NAMESPACE namespace: 
         
         NAME                        POD-SELECTOR              AGE
               cassandra-from-mart         app=apigee-cassandra      4d5h
               cassandra-from-runtime      app=apigee-cassandra      4d5h
               cassandra-from-sync         app=apigee-cassandra      4d5h
               cassandra-to-cassandra      app=apigee-cassandra      4d5h
               controller-to-cassandra     app=apigee-cassandra      4d5h
               redis-from-redisenvoy       app=apigee-redis          3d18h
               redisenvoy-from-runtime     app=apigee-redis-envoy    3d18h
             




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
