---
url: https://docs.cloud.google.com/service-mesh/v1.22/docs/canonical-service-best-practices/
title: Canonical Service Best Practices \u00a0|\u00a0 Cloud Service Mesh v1.22 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:04:43.307801+00:00
---

# Canonical Service Best Practices  |  Cloud Service Mesh v1.22  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.22/docs/canonical-service-best-practices/

You are viewing archived v1.22 Service Mesh documentation.

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
  * [ v1.22 ](https://docs.cloud.google.com/service-mesh/v1.22/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.22/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Canonical Service Best Practices

**Note:** Canonical Services are supported automatically in Cloud Service Mesh version 1.6.8 and higher.

[Canonical Services](https://docs.cloud.google.com/service-mesh/v1.22/docs/canonical-service) allow you to navigate many different configurations. For the best experience with Cloud Service Mesh Service Dashboards, consider the following standard practices when setting up your services:

  * Reserve a unique service [namespace, name] across the whole mesh.
  * Define one software application per Canonical Service. 
    * Don't group Canonical Services across environments (for example, prod/stage/dev).
    * Use [Cloud Monitoring dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards) for higher-level views of multiple services.
  * Plan for Canonical Services to be long-lived in production.



## Reserve a unique service [namespace, name] across the whole mesh

If a Canonical Service deployed in one cluster or region has the same Kubernetes namespace and Canonical Service name as one deployed in another cluster or region, Cloud Service Mesh assumes that it is the same logical service.

This behavior is consistent with the [fleet principle of "sameness"](https://cloud.google.com/anthos/multicluster-management/fleets#sameness), which says that a namespace should have the same meaning and represent the same entity across the entire fleet.

**Important:** Make sure that logically different services (for example, payment accounting API and payment transaction API) don't use the same [namespace, name] pair (e.g., "payments/api") because they inadvertently join into one Service Dashboard. Note that this conceptual joining occurs even across regional boundaries. Moreover, the function of the services may be impacted.

## One software application per Canonical Service

Canonical Services are meant to represent a single logical service or microservice. They are meant to span _homogenous_ binaries/workloads that represent the same software application and business function.

While you could define a Canonical Service to group several conceptually different microservices together, the Service Dashboards wouldn't provide their full value.The Service Dashboards would display an aggregation of dissimilar components which may individually be performing and configured very differently. It would be difficult or even impossible to understand the health, performance, and configuration of the whole.

The following are not necessarily bad practices, but your Canonical Service may be too big if:

  * There is network traffic between different workloads within a single Canonical Service.
  * A Canonical Service comprises multiple workloads that are deployed on different release schedules.
  * Different teams within your organization are responsible for operating different pieces of a single Canonical Service.



### Don't group a Canonical Service across environments

Many technology organizations employ multiple deployment environments to ensure software quality and limit risk. These environments most often include dev, test, staging, prod, or some subset.

Even if you deploy the same conceptual service across each of your various environments, it is bad practice to make them a single Canonical Service. These services are not the same and don't represent the same level of operational concern or focus for your organization.

For example, a failure on a critical production service may cause 3AM pages and firefights. You don't want to alert anybody if the "dev" deployment fails in the middle of the night. The same goes for understanding performance, capacity, and release safety.

**Important:** We recommend that you separate services in your various environments into **separate** Canonical Services. You can do this in one of three ways.

From the easiest but least rigorous, to the highest-effort but most powerful, there are three ways to separate services into different environments:

  1. Separate using multiple **service names** , for example, `payments-prod` and `payments-test`.
  2. Separate using multiple **namespaces** , for example `billing-team` and `billing-team-test`.
  3. Separate using multiple [fleets](https://docs.cloud.google.com/anthos/multicluster-management/fleets), one for each environment.



### Prefer Cloud Monitoring custom dashboards for arbitrary aggregations

Rather than artificially bloating Canonical Services into larger scopes for aggregate data, use [Cloud Monitoring dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards) to create higher-level views of multiple logical services at once.

## Canonical Services are meant to be long-lived

Outside of development, exploration, and testing use cases, Canonical Services should represent global, high-level logical services. These services are slow-changing and tend to be long-lived. This longevity includes not changing service names. While you can change their names, doing so impacts metrics, SLOs, and logs. However, you can freely adjust the `Display name` field without disruption.

A new Canonical Service often represents new or updated software while a Canonical Service going away often represents a service deprecation. Your ability to see the historical performance of your service, plan, and project capacity all depend on maintaining a single notion of that service in Cloud Service Mesh for the duration of its life.

Note that this contrasts to lower-level resources like VM instances, Kubernetes Pods/Deployments, and even whole clusters, which often come and go as part of updating and maintaining production systems.

## What's next

  * [Learn more about Canonical Services](https://docs.cloud.google.com/service-mesh/v1.22/docs/canonical-service).
  * [Learn how to define a Canonical Service](https://docs.cloud.google.com/service-mesh/v1.22/docs/define-canonical-service).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
