---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/microservices/
title: Microservices \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:31.110821+00:00
---

# Microservices  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/microservices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Microservices Stay organized with collections  Save and categorize content based on your preferences. 

This document introduces microservices and describes the types of microservices supported by Cloud Monitoring.

The term _microservice_ means different things to different people. For some, the microservice corresponds with the "boxes" drawn on the whiteboard when talking about system architecture. Others refer to a more formal [definition](https://en.wikipedia.org/wiki/Microservices) that describes a network-addressable endpoint with functionality determined by its external-facing API that can be developed, deployed, and operated independently from other microservices in the system. Still others base their understanding on the microservice concept provided by their development platform, like the [App Engine services](https://docs.cloud.google.com/appengine/docs/standard/python/an-overview-of-app-engine#services) or the [Cloud Service Mesh service](https://cloud.google.com/products/service-mesh).

Our goal is not to force a definition of _microservice_ upon you. Instead, we want to help you monitor your systems at scale during your digital transformation by providing service-oriented monitoring tools to support you and your architecture. We want to work with you to adopt best practices for monitoring systems without changing a single line of code.

To help you monitor your microservices, Cloud Monitoring does the following:

  * Auto-detects microservices when possible
  * Provides a guided experience for defining Google Kubernetes Engine- and Cloud Run-based microservices
  * Offers a fully custom solution for maximum flexibility



## Auto-discovered microservices

Some modern development frameworks offer opinionated concepts of a microservice. In architectures that use such frameworks, Cloud Monitoring automatically detects when services are deployed, updated, or deleted. Monitoring accomplishes this detection through constant analysis of the metadata stream produced by a project.

Cloud Monitoring can automatically detect microservices built using the following development frameworks:

  * [App Engine](https://docs.cloud.google.com/appengine): App Engine has a strong notion of microservice, called an App Engine service (and formerly a _module_). Each service is distinguished by its own [`app.yaml`](https://docs.cloud.google.com/appengine/docs/standard/nodejs/config/appref) configuration file.

  * [Cloud Service Mesh](https://cloud.google.com/products/service-mesh): Cloud Monitoring supports service meshes built atop a single GKE cluster. In this configuration, a Cloud Service Mesh service corresponds directly to a [GKE service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service). All Cloud Service Mesh services, both user-managed and system-managed, are automatically detected.




### Dashboards for auto-discovered microservices

A service dashboard is automatically created for all auto-discovered microservices. The dashboard contains the metadata details of the service, the alert timeline, the status of your service-level objectives (SLOs), and logs related to the service. Each of these components is described in more detail in [Using microservice dashboards](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/svc-dashboard).

![Service dashboard for auto-discovered microservices.](https://docs.cloud.google.com/static/stackdriver/docs/solutions/slo-monitoring/images/svcmon-msvc-db-autodetect.png)

**Note:** The alert timeline and SLO list will be empty since no SLOs or SLO alerts have been defined. To get the most out of your service dashboard, create SLOs and set alerts on them as described in [Creating an SLO](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/create-slo).

## GKE, Cloud Run and custom services

**Note:** In Cloud Monitoring, a _service_ is a construct that you can associate with SLOs and alerting policies. Several of the resources for which you might create Monitoring services are also referred to as _services_ , but with different meanings, like [_GKE services_](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service) or [_Cloud Run services_](https://docs.cloud.google.com/run/docs/resource-model#services). 

Cloud Monitoring can identify _potential_ or _candidate_ services for the following types:

  * GKE namespaces
  * GKE services
  * GKE workloads
  * Cloud Run services



However, there may be many such candidates, and you don't necessarily want to create SLOs on all of them. Monitoring creates a list of candidate services, and you identify the services you want to treat as Monitoring services by selecting them from the list. Monitoring then creates the service infrastructure for you.

When no existing service type accommodates an application for which you want to create SLOs, you can define a custom service.

For more information about identifying candidate services and creating custom services, see [Defining a microservice](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/define-svc).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
