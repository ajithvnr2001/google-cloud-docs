---
url: https://docs.cloud.google.com/service-mesh/v1.28/docs/define-canonical-service/
title: Defining a Canonical Service \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:31:06.575547+00:00
---

# Defining a Canonical Service  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.28/docs/define-canonical-service/

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

# Defining a Canonical Service

**Note:** Canonical Services are supported automatically in Cloud Service Mesh version 1.6.8 and higher.

[Canonical Services](https://docs.cloud.google.com/service-mesh/v1.28/docs/canonical-service) is a group of workloads that implement the same service(s) and API(s). For supported workload types, Cloud Service Mesh automatically creates Canonical Service resources based on existing information from the Kubernetes API Server. This page explains what labels automatically define Canonical Services and how you can manually adjust the boundaries of your services. The currently supported workload instance types are:

  * Kubernetes Pods (including via Kubernetes Deployments, Kube Run Services, etc.)
  * Virtual Machine instances
  * Mesh-external services (specifically, ServiceEntry resources with a location of `MESH_EXTERNAL`)



## What defines Canonical Services

Cloud Service Mesh determines the Canonical Service membership by reading the `service.istio.io/canonical-name` [label](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) on the Kubernetes configuration resource associated with each workload instance:

  * For Pods, the label is in the Kubernetes Pod resource
  * For VMs, the label in the Istio [WorkloadEntry](https://istio.io/v1.28/docs/reference/config/networking/workload-entry/) resource
  * For external services, the label is in the Istio [ServiceEntry](https://istio.io/v1.28/docs/reference/config/networking/service-entry/) resource



Canonical Services have the same [Kubernetes namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) as their associated workload instances and cannot span namespaces.

## Automatic labeling rules

Cloud Service Mesh automatically groups your Pod- and VM-based workloads into Canonical Services with no action on your part. You only need to take action to:

  * Adjust labels for user/reader clarity
  * Override the default behavior.



### Automatic labeling in Kubernetes Pods

Canonical Services focus around the Kubernetes `app.kubernetes.io/name` and `app` labels. Note that the former label takes precedence. If you use either of these two labels on your workloads, no further work is required.

### Automatic labeling in Virtual Machines

To build Canonical Services on your VMs, you must add your VMs to a service mesh by configuring a [WorkloadEntry resource](https://istio.io/latest/docs/reference/config/networking/workload-entry/) in your Kubernetes API server.

## Manually labeling

To manually apply or override a Canonical Service label apply the `service.istio.io/canonical-name` label to supported workload resource configurations. In order for an external service to be recognized as a Canonical Service, you must manually label the applicable ServiceEntry.

### Manual labeling in Kubernetes Pods

To deploy many Pods at once using a [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/), set the `service.istio.io/canonical-name` label on the PodTemplateSpec:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-deployment
      namespace: my-namespace
    spec:
      replicas: 3
      template:
        metadata:
          labels:
            **service.istio.io/canonical-name : my-service**
        spec:
          containers:
            ...
    

To label the Canonical Service of a single Pod, add the `service.istio.io/canonical-name` label to the `labels` section of your Pod configuration:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: my-test-pod
      namespace: my-namespace
      labels:
        **service.istio.io/canonical-name : my-service**
    spec:
      ...
    

### Label virtual machines manually

To label the Canonical Service of a single VM/WorkloadEntry, add the `service.istio.io/canonical-name` label to the "labels" section of your WorkloadEntry configuration:
    
    
    apiVersion: networking.istio.io/v1alpha3
    kind: WorkloadEntry
    metadata:
      name: my-vm-123
      namespace: my-namespace
      labels:
        **service.istio.io/canonical-name : my-service**
    spec:
      ...
    

### Label external services manually

To label the Canonical Service of a single external service/ServiceEntry, add the `service.istio.io/canonical-name` label to the "labels" section of your ServiceEntry configuration:
    
    
    apiVersion: networking.istio.io/v1alpha3
    kind: ServiceEntry
    metadata:
      name: example-com
      namespace: my-namespace
      labels:
        **service.istio.io/canonical-name : an-external-service**
    spec:
       location: MESH_EXTERNAL
      ...
    

## What's next

  * [Learn about Canonical Services](https://docs.cloud.google.com/service-mesh/v1.28/docs/canonical-service)
  * [Learn about best practices in Canonical Services](https://docs.cloud.google.com/service-mesh/v1.28/docs/canonical-service-best-practices)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
