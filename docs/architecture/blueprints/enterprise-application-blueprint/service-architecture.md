---
url: https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/service-architecture/
title: Service architecture \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:09.773375+00:00
---

# Service architecture  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/service-architecture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Service architecture Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-12-13 UTC

A Kubernetes service is an abstraction that lets you expose a set of pods as a single entity. Services are fundamental building blocks for exposing and managing containerized applications in a Kubernetes cluster. Services in this blueprint are architected in a standardized manner in consideration to namespaces, identity, service exposure, and service-to-service communication.

## Namespaces

Each namespace has its own set of resources, such as pods, services, and deployments. Namespaces let you organize your applications and isolate them from each other. The blueprint uses namespaces to group services by their purpose. For example, you can create a namespace for all your frontend services and a namespace for your backend services. This grouping makes it easier to manage your services and to control access to them.

## Service exposure

A service is exposed to the internet through the [GKE Gateway controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api). The GKE Gateway controller creates a load balancer using [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) in a [multi-cluster, multi-region configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-multi-cluster-gateways#external-gateway). Cloud Load Balancing uses Google's network infrastructure to provide the service with an [anycast IP address](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview#global_versus_regional_load_balancing) that enables low-latency access to the service. Client access to the service is done over HTTPS connections and client HTTP requests are redirected to HTTPS. The load balancer uses [Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs/overview) to manage public certificates. Services are further protected by Cloud Armour and Cloud CDN. The following diagram shows how services are exposed to the internet.

![Blueprint services that are exposed to the internet.](https://docs.cloud.google.com/static/architecture/blueprints/enterprise-application-blueprint/images/eab-service-exposure.svg)

## Cloud Service Mesh

The blueprint uses [Cloud Service Mesh](https://cloud.google.com/products/service-mesh) for mutual authentication and authorization for all communications between services. For this deployment, the Cloud Service Mesh uses [CA Service](https://docs.cloud.google.com/service-mesh/docs/security/security-overview#ca_service) for issuing [TLS certificates](https://docs.cloud.google.com/service-mesh/docs/security/security-overview#mutual_tls) to authenticate peers and to help ensure that only authorized clients can access a service. Using [mutual TLS (mTLS)](https://en.wikipedia.org/wiki/Mutual_authentication#mTLS) for authentication also helps ensure that all TCP communications between services are encrypted in transit. For service ingress traffic into the service mesh, the blueprint uses the GKE Gateway controller.

## Distributed services

A [distributed service](https://istio.io/latest/docs/ops/deployment/deployment-models/#multiple-clusters) is an abstraction of a Kubernetes service that runs in the same namespace across multiple clusters. A distributed service remains available even if one or more GKE clusters are unavailable, as long as any remaining healthy clusters are able to serve the load. To create a distributed service across clusters, Cloud Service Mesh provides Layer 4 and Layer 7 connectivity between an application's services on all clusters in the environment. This connectivity enables the Kubernetes services on multiple clusters to act as a single logical service. Traffic between clusters is only routed to another [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) if intra-region traffic cannot occur because of a regional failure.

## Service identity

Services running on GKE have identities that are associated with them. The blueprint configures Workload Identity Federation for GKE to let a [Kubernetes service account](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) act as a [Google Cloud service account](https://docs.cloud.google.com/iam/docs/service-accounts). Each instance of a distributed service within the same environment has a common identity which simplifies permission management. When accessing Google Cloud APIs, services that run as the Kubernetes service account automatically authenticate as the Google Cloud service account. Each service has only the minimal permissions necessary for the service to operate.

## What's next

  * Read about [logging and monitoring](https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/logging-monitoring) (next document in this series).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-12-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-12-13 UTC."],[],[]] 
