---
url: https://docs.cloud.google.com/service-mesh/v1.27/docs/operate-and-maintain/advanced-load-balancing-istio/
title: Advanced Load Balancing on GKE Clusters \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:39:19.243830+00:00
---

# Advanced Load Balancing on GKE Clusters  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.27/docs/operate-and-maintain/advanced-load-balancing-istio/

You are viewing v1.27 Service Mesh documentation.

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
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.27/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.27/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Advanced Load Balancing on GKE Clusters

This page shows you how to configure advanced load balancing on GKE clusters for managed Cloud Service Mesh (TD) users using the Kubernetes API. For the corresponding user guide to configure advanced load balancing using the Google Cloud API, see [Set up advanced load balancing](https://docs.cloud.google.com/service-mesh/v1.27/docs/service-routing/set-up-advanced-load-balancing).

You can use advanced load balancing to:

  * Keep traffic to a service zonal until local capacity is exhausted.
  * Send traffic to the service in a "primary" location with failover to a secondary location when sufficient endpoints in the primary location become unhealthy.
  * Control when failover happens (based on percentage of healthy hosts).



## Limitations

  * [General limitations](https://docs.cloud.google.com/service-mesh/v1.27/docs/service-routing/advanced-load-balancing-overview#limitations) around using advanced load balancing on Google Cloud apply.
  * This feature is only available to managed Cloud Service Mesh users using Traffic Director as control plane and requires data plane version 1.19.10-asm.22 or later.
  * Not all the fields in [GCPTrafficDistributionPolicy](https://github.com/GoogleCloudPlatform/gke-gateway-api/blob/main/apis/networking/v1/gcptrafficdistributionpolicy_types.go) and [GCPBackendPolicy](https://github.com/GoogleCloudPlatform/gke-gateway-api/blob/main/apis/networking/v1/gcpbackendpolicy_types.go) are supported for managedCloud Service Mesh (TD). The supported fields are as follows:

    * GCPTrafficDistributionPolicy 
      * ServiceLbAlgorithm
      * AutoCapacityDrain
      * FailoverConfig
    * GCPBackendPolicy 
      * MaxRatePerEndpoint
      * BackendPreference

All the fields not listed are unsupported fields and a policy with at least an unsupported field configured doesn't take effect in Cloud Service Mesh .

  * Advanced load balancing can only be applied to Kubernetes services backed by workloads running on Google Cloud. External services or workloads (like ServiceEntry) are not supported.

  * The load balancing policies can only be applied to individual Kubernetes services. Namespace-wide/mesh-wide load balancing policies are not supported.

  * Only QPS capacity is supported.

  * Only GKE versions >= 1.31.1 are supported.

  * Service mesh advanced load balancing policies must only be applied to services that only serves mesh traffic. It must not be applied to services serving as [GKE Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api) backends. The traffic behaviors are undefined when an advanced load balancing traffic target a Kubernetes service serving both mesh traffic and traffic from a GKE Gateway.




## Configure advanced load balancing

You can use the following custom resources to configure advanced load balancing on GKE. You can find the detailed resource definition in the [gke-gateway-api repo](https://github.com/GoogleCloudPlatform/gke-gateway-api/tree/main/config/crd).

### GCPTrafficDistributionPolicy

GCPTrafficDistributionPolicy configures the service-level load balancing policy for Kubernetes services. It lets you:

  * Choose a custom load balancing algorithm. Supported algorithms are described in [the advanced load balancing table](https://docs.cloud.google.com/service-mesh/v1.27/docs/service-routing/advanced-load-balancing-overview#algorithm-comparison).
  * Enable [auto capacity draining](https://docs.cloud.google.com/service-mesh/v1.27/docs/service-routing/advanced-load-balancing-overview#auto-capacity-drain).
  * Tune [failover health threshold](https://docs.cloud.google.com/service-mesh/v1.27/docs/service-routing/advanced-load-balancing-overview#customize-failover).



If multiple GCPTrafficDistributionPolicies target the same service, the oldest policy will be enforced.

### GCPBackendPolicy

GCPBackendPolicy configures service backends properties which impact load balancing behavior, including:

  * Service backend capacity.
  * Designating [preferred backends](https://docs.cloud.google.com/service-mesh/v1.27/docs/service-routing/advanced-load-balancing-overview#preferred-backends).



If multiple GCPBackendPolicies target the same service in a cluster, the oldest policy will be enforced.

### Policy Status

Both GCPTrafficDistributionPolicy and GCPBackendPolicy have a status field indicating the attachment status of the policy.

For example, running `kubectl describe gcpbackendpolicies example-policy -n example` would yield an output similar to:
    
    
    ...
    Status:
      Ancestors:
        Ancestor Ref:
          Group:
          Kind:       Service
          Name:       example-svc
          Namespace:  example
        Conditions:
          Last Transition Time:  2024-10-13T01:15:03Z
          Message:
          Observed Generation:   1
          Reason:                Attached
          Status:                True
          Type:                  Attached
        Controller Name:         gsmconfig.gke.io/controller
    

## Preliminary setup

Before you can complete this guide you must [provision Cloud Service Mesh on a GKE cluster](https://docs.cloud.google.com/service-mesh/v1.27/docs/onboarding/provision-control-plane).

  1. Check the CRDs are installed:
         
         kubectl get crd
         

The output is similar to:
         
         ...
         gcptrafficdistributionpolicies.networking.gke.io   2024-07-18T21:50:12Z
         gcpbackendpolicies.networking.gke.io               2024-07-18T21:50:12Z
         ...
         

  2. Install the GCPBackendPolicy CRD if it's not already installed:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/gke-gateway-api/refs/heads/main/config/crd/networking.gke.io_gcpbackendpolicies.yaml
         

  3. Install the GCPTrafficDistributionPolicy CRD if it's not already installed:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/gke-gateway-api/refs/heads/main/config/crd/networking.gke.io_gcptrafficdistributionpolicies.yaml
         




The example policies in this user guide target Service foo in namespace foo for demonstration purposes. You can run the following command to create the test service and namespace, or if you prefer, you can use your own service and namespace:
    
    
    kubectl apply -f - <<EOF
    kind: Namespace
    apiVersion: v1
    metadata:
      name: foo
      labels:
        istio-injection: enabled
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: foo
      namespace: foo
    spec:
      replicas: 2
      selector:
        matchLabels:
          app: test-backend
      template:
        metadata:
          labels:
            app: test-backend
        spec:
          containers:
          - name: whereami
            image: gcr.io/google-samples/whereami:v1.2.23
            ports:
            - containerPort: 8080
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: foo
      namespace: foo
    spec:
      selector:
        app: test-backend
      ports:
      - port: 8080
        targetPort: 8080
    EOF
    

## Configuring the load balancing algorithm

By default, traffic to a service is evenly distributed to every single healthy service backend in a Cloud Service Mesh service mesh. You can create the following GCPTrafficDistributionPolicy so that traffic is distributed to the closest zone up to the backend capacity:
    
    
    kubectl apply -f - <<EOF
    apiVersion: networking.gke.io/v1
    kind: GCPTrafficDistributionPolicy
    metadata:
      name: lb-policy
      namespace: foo
    spec:
      targetRefs:
      - kind: Service
        group: ""
        name: foo-service
      default:
        serviceLbAlgorithm: WATERFALL_BY_ZONE
    EOF
    

**Note:** Settings in GCPTrafficDistributionPolicy take precedence over the ones in core Kubernetes Service API.

By default, service backends are treated as if they have infinite capacity. When there are sufficient healthy hosts in the local/closest zone, traffic will never be distributed outside of the local/closest zone for a certain client locality. You can optionally configure the capacity of your service backend using GCPBackendPolicy so that a single zone doesn't get overloaded.
    
    
    kubectl apply -f - <<EOF
    apiVersion: networking.gke.io/v1
    kind: GCPBackendPolicy
    metadata:
      name: backend-policy
      namespace: foo
    spec:
      targetRef:
        kind: Service
        group: ""
        name: foo-backend
      default:
        maxRatePerEndpoint: 5
    EOF
    

## Tuning failover behavior

By default, failover won't be triggered as long as a sufficient percentage of hosts are healthy in the _primary backends_. For more information on primary backends and other terminology, see the [Advanced load balancing overview](https://docs.cloud.google.com/service-mesh/v1.27/docs/service-routing/advanced-load-balancing-overview#customize-failover). GCPTrafficDistributionPolicy lets you configure the healthy host percentage threshold until traffic is shifted away from _primary backends_ to _failover backends_. Failover is triggered sooner with a larger threshold. For example, if you want failover to be triggered as soon as the percentage of healthy hosts drop below 90% in the _primary backends_ , you can configure the following GCPTrafficDistributionPolicy:
    
    
    kubectl apply -f - <<EOF
    apiVersion: networking.gke.io/v1
    kind: GCPTrafficDistributionPolicy
    metadata:
      name: lb-policy
      namespace: foo
    spec:
      targetRefs:
      - kind: Service
        group: ""
        name: foo-service
      default:
       failoverConfig:
         failoverHealthThreshold: 90
    EOF
    

## Configuring advanced load balancing in a multi-cluster service mesh

GCPTrafficDistributionPolicy and GCPBackendPolicy are applied at different scope in a multi-cluster service mesh.

When a GCPTrafficDistributionPolicy targets a multi-cluster service, it defines the service level load balancing behavior across all clusters. Only one GCPTrafficDistributionPolicy needs to be created for a particular multi-cluster service. If you are using Istio API to configure your service mesh, you can create GCPTrafficDistributionPolicy in any cluster in the fleet. You can check if a policy conflicts with another policy by inspecting its policy status.

When a GCPBackendPolicy targets a multi-cluster service, it defines backend level settings (for example, per-pod capacity) for the backend pods selected by its targeting servicein its local cluster. For the same multi-cluster service, it's possible to define different backend level settings in different clusters.

In the following example, a GCPTrafficDistributionPolicy is created in cluster A to define the load balancing algorithm to be used across the fleet while GCPBackendPolicies are in each cluster. Both GCPBackendPolicy configures a capacity of 10qps per pod for the backend pods in their local cluster while the GCPBackendPolicy in cluster A configures the backend pods in cluster A as [preferred backend](https://docs.cloud.google.com/service-mesh/v1.27/docs/service-routing/advanced-load-balancing-overview#preferred-backends).

Together, these policies configures the load balancing behaviors for in-mesh traffic sent to Service foo:

  * Traffic from anywhere prefers backends in cluster A until backend pods in cluster A need to handle 10 qps per pod. 
    * This behavior is mainly defined by the GCPBackendPolicy that set `backendPreference` to `PREFERRED` in cluster A.
  * Traffic exceeding the configured capacity of the backends in cluster A is routed using algorithm `WATERFALL_BY_ZONE` to cluster B. For a more detailed explanation of preferred backends, see [Advanced load balancing overview](https://docs.cloud.google.com/service-mesh/v1.27/docs/service-routing/advanced-load-balancing-overview#preferred-backends). 
    * This behavior is mainly defined by the GCPTrafficDistributionPolicy, which defines the algorithm, in cluster A and GCPBackendPolicy, which define the backend capacity, in both cluster A and B.



![Advanced load balancing multi-cluster service mesh](https://docs.cloud.google.com/static/service-mesh/v1.27/docs/images/advanced-lb-multi-cluster-service-mesh.svg)

**Note:** This section demonstrates Cloud Service Mesh capability to load balance traffic across multiple clusters. For demonstration purposes, deploy the sample Service foo and its backend pods in both clusters.

In Istio, regular Kubernetes services implicitly become "multi-cluster" when there are multi clusters in the service mesh and the service is created across cluster boundaries.. While the following GCPTrafficDistributionPolicy targets the regular Kubernetes service foo, it applies to the multi-cluster service foo consisting of corresponding workloads in two clusters. 

  1. Create the GCPTrafficDistributionPolicy for cluster A:
         
         kubectl apply --context cluster-a-context -f - <<EOF
         kind: GCPTrafficDistributionPolicy
         apiVersion: networking.gke.io/v1
         metadata:
         name: foo-traffic-distribution-policy
         namespace: foo
         spec:
           targetRefs:
           - kind: Service
             group: ""
             name: foo-service
           default:
             serviceLbAlgorithm: WATERFALL_BY_ZONE
         
         EOF
         

  2. Create the GCPBackendPolicy for cluster A:
         
         kubectl apply --context cluster-a-context -f - <<EOF
         kind: GCPBackendPolicy
         apiVersion: networking.gke.io/v1
         metadata:
         name: foo-backend-policy
         namespace: foo
         spec:
           default:
             maxRatePerEndpoint: 100
             backendPreference: PREFERRED
           targetRef:
             group: ""
             kind: Service
             name: foo-service
         EOF
         

  3. Create the GCPBackendPolicy for cluster B:
         
         kubectl apply --context cluster-b-context -f - <<EOF
         kind: GCPBackendPolicy
         apiVersion: networking.gke.io/v1
         metadata:
         name: foo-backend-policy
         namespace: foo
         spec:
           default:
             maxRatePerEndpoint: 10
           targetRef:
             group: ""
             kind: Service
             name: foo-service
         EOF
         




## What's Next

  * Learn more about [Advanced load balancing](https://docs.cloud.google.com/service-mesh/v1.27/docs/service-routing/advanced-load-balancing-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
