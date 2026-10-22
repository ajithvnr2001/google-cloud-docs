---
url: https://docs.cloud.google.com/architecture/manage-and-scale-windows-networking/
title: Manage and scale networking for Windows applications that run on managed Kubernetes \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:04.324856+00:00
---

# Manage and scale networking for Windows applications that run on managed Kubernetes  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/manage-and-scale-windows-networking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Manage and scale networking for Windows applications that run on managed Kubernetes Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-08-14 UTC

This reference architecture provides a highly available and scalable solution that uses [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview) and [Envoy gateways](https://gateway.envoyproxy.io/) to manage network traffic for Windows applications that run on [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview). It explains how to manage that network traffic by using a service that can route traffic to Pods and to an [open-source xDS-compliant proxy](https://www.envoyproxy.io/docs/envoy/latest/api/api). Using an architecture like this can help to reduce costs and improve network management.

This document is intended for cloud architects, network administrators and IT professionals who are responsible for designing and managing Windows applications running on GKE.

## Architecture

The following diagram shows an architecture for managing networking for Windows applications running on GKE using Cloud Service Mesh and Envoy gateways:

![Data flows through an internal Application Load Balancer and an Envoy gateway.](https://docs.cloud.google.com/static/architecture/images/manage-and-scale-windows-networking-archdiagram.svg)

The architecture includes the following components:

  * A regional GKE cluster with both Windows and Linux node pools.
  * Two Windows applications running in two separate GKE Pods. 
    * Each application is exposed by a `ClusterIP`-type Kubernetes Service and a [network endpoint group (NEG)](https://docs.cloud.google.com/load-balancing/docs/negs).
  * Cloud Service Mesh creates and manages the traffic routes to the NEGs for each GKE Pod. Each route is mapped to a specific `scope`. That `scope` [uniquely identifies a Cloud Service Mesh ingress gateway](https://docs.cloud.google.com/service-mesh/docs/service-routing/set-up-ingress-gateway#config-gateway).
  * HTTP routes that map to the backend services for Cloud Service Mesh.
  * [Envoy](https://www.envoyproxy.io/docs/envoy/latest/intro/what_is_envoy) container Pods that act as an Envoy Gateway to the GKE cluster.
  * Envoy gateways that run on Linux nodes. The gateways are configured to direct traffic to the Windows applications through the services that correspond to those applications. Envoy is configured to use the `scope` parameter to load the configuration details of the relevant Cloud Service Mesh services.
  * An [internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal) that terminates SSL traffic and directs all external incoming traffic to the Envoy gateways.



## Products used

This reference architecture uses the following Google Cloud and third-party products:

### Google Cloud products

  * [ Cloud Load Balancing](https://cloud.google.com/load-balancing): A portfolio of high performance, scalable, global and regional load balancers. 
  * [ Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine): A Kubernetes service that you can use to deploy and operate containerized applications at scale using Google's infrastructure. 
  * [ Cloud Service Mesh](https://cloud.google.com/service-mesh): A suite of tools that helps you monitor and manage a reliable service mesh on-premises or on Google Cloud.



### Third-party products

  * [Envoy Gateway](https://gateway.envoyproxy.io/): Manages an Envoy proxy as a standalone or Kubernetes-based application gateway.
  * [Gateway API](https://gateway-api.sigs.k8s.io/): An official Kubernetes project focused on L4 and L7 routing in Kubernetes.



## Use case

The main use case for this reference architecture is to manage network traffic for Windows applications that run on GKE. This architecture provides the following benefits:

**Simplified network management** : Cloud Service Mesh and Envoy gateways provide simplified network management through a centralized control plane that manages network traffic to applications. These applications can be either Linux or Windows applications that run on GKE or Compute Engine. Using this simplified network management scheme reduces the need for manual configuration.

**Enhanced scalability and availability** : To meet your changing demands, use Cloud Service Mesh and Envoy gateways to scale your Linux and Windows applications. You can also use Envoy gateways to provide high availability for your applications by load balancing traffic across multiple Pods.

**Improved security** : Use Envoy gateways to add security features to your Linux and Windows applications, such as SSL termination, authentication, and rate limiting.

**Reduced costs** : Both Cloud Service Mesh and Envoy gateways can help reduce the costs of managing network traffic for Linux and Windows applications.

## Design considerations

This section provides guidance to help you develop an architecture that meets your specific requirements for security, reliability, cost, and efficiency.

### Security

  * **Secured networking** : The architecture uses an internal Application Load Balancer to encrypt incoming traffic to the Windows containers. Encryption in transit helps to prevent data leakage.
  * **Windows containers** : Windows containers help provide a secure and isolated environment for containerized applications.



### Reliability

  * **Load balancing** : The architecture uses multiple layers of Cloud Load Balancing to distribute traffic across the Envoy gateways and the Windows containers.
  * **Fault tolerance** : This architecture is fault tolerant with no single point of failure. This design helps to ensure that it's always available, even if one or more of the components fails.
  * **Autoscaling** : The architecture uses autoscaling to automatically scale the number of Envoy gateways and Windows containers based on the load. Autoscaling helps to ensure that the gateways, and the applications, can handle spikes in traffic without experiencing performance issues.
  * **Monitoring** : The architecture uses [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus) and Cloud Operations to monitor the health of the Envoy gateways and Windows containers. Monitoring helps you identify issues early and potentially prevent them from disrupting your applications.



### Cost optimization

  * **Choose the right instance types for your workloads** : Consider the following factors when choosing instance types: 
    * The number of vCPUs and memory your applications require
    * The expected traffic load for your applications
    * The need for users to have highly available applications
  * **Use autoscaling** : Autoscaling can help you save money by automatically scaling your Windows workloads vertically and horizontally.

    * Vertical scaling tunes container requests and limits according to customer use.

      * Automate vertical scaling with [vertical Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler).
    * Horizontal scaling adds or removes Kubernetes Pods to meet demand.

      * Automate horizontal scaling with [horizontal Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler).
  * **Use Cloud Service Mesh and Envoy gateways** : Cloud Service Mesh and Envoy gateways can help you save money by efficiently routing traffic to your Windows applications. Using more efficient routing can help reduce the amount of bandwidth you must purchase. It can also help improve the performance of those applications.

  * **Use shared Virtual Private Cloud (VPC) networks** : Shared Virtual Private Cloud networks let you share a single VPC across multiple projects. Sharing can help you save money by reducing the number of VPCs that you need to create and manage.




### Operational efficiency

  * **Multiple domains with a single internal load balancer** : The architecture uses internal Application Load Balancers to offload SSL traffic. Each HTTPS target proxy can support multiple SSL certificates ([up to the supported maximum](https://docs.cloud.google.com/load-balancing/docs/quotas#target_proxies)) to manage multiple applications with different domains.
  * **Infrastructure as Code (IaC)** : To manage the infrastructure, the architecture can be deployed using IaC. IaC helps to ensure that your infrastructure is consistent and repeatable.



## Deployment

To deploy this architecture, see [Deploy Windows applications running on managed Kubernetes](https://docs.cloud.google.com/architecture/manage-and-scale-windows-networking/deployment).

## What's next

  * Learn more about the Google Cloud products used in this design guide: 
    * [GKE networking best practices](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/networking)
    * [Best practices for running cost effective Kubernetes applications on GKE](https://docs.cloud.google.com/architecture/best-practices-for-running-cost-effective-kubernetes-applications-on-gke#observe_your_gke_clusters_and_watch_for_recommendations)
    * [Cloud Service Mesh control plane observability](https://docs.cloud.google.com/service-mesh/docs/control-plane-observability)
    * [Using self-managed SSL certificates with load balancers](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs)
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Eitan Eibschutz](https://www.linkedin.com/in/eitaneibschutz) | Staff Technical Solutions Consultant

Other contributors: 

  * [John Laham](https://www.linkedin.com/in/lahamjohn) | Solutions Architect
  * [Kaslin Fields](https://www.linkedin.com/in/kaslinfields) | Developer Advocate
  * [Maridi (Raju) Makaraju](https://www.linkedin.com/in/mmraju) | Supportability Tech Lead
  * [Valavan Rajakumar](https://www.linkedin.com/in/valavanr) | Key Enterprise Architect
  * [Victor Moreno](https://www.linkedin.com/in/vimoreno) | Product Manager, Cloud Networking



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-08-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-08-14 UTC."],[],[]] 
