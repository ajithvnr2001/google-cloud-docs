---
url: https://docs.cloud.google.com/service-mesh/legacy/in-cluster/observability/canonical-service/
title: Canonical Service \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:47.987212+00:00
---

# Canonical Service  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/in-cluster/observability/canonical-service/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Canonical Service

**Note:** Canonical Services are supported automatically in Cloud Service Mesh version 1.6.8 and higher.

This page explains what a Canonical Service is in Cloud Service Mesh.

## What is a Canonical Service?

Cloud Service Mesh supports Canonical Services, a conceptual and architectural model for representing your production workloads as a singular service that is easier to observe and manage. These workloads can span multiple clusters, disparate backend platforms, and different schemas and configurations.

**For Kubernetes users:** Canonical Service is roughly analogous to the Kubernetes "app" concept and the Application CRD.

**For Serverless users:** Canonical Service is very similar to [App Engine service](https://docs.cloud.google.com/appengine/docs/flexible/java/an-overview-of-app-engine#services) and [Cloud Run service](https://docs.cloud.google.com/run/docs/resource-model#services) concepts. The one difference is that Google Serverless services are inherently regional whereas Canonical Services are a global / multi-region abstraction.

For example, the following scenarios all describe ways that you might refer to a Canonical Service:

  * A service has an outage.
  * A service runs both on-premise and on a public cloud.
  * Deploying a new revision of a service.
  * The service Foo is sending too much traffic and may exceed our capacity.



Canonical Services exist within a single Mesh, which in Cloud Service Mesh means that they are also unique within a [fleet](https://docs.cloud.google.com/anthos/multicluster-management/fleets) and a Google Cloud Project (all of which are one-to-one with Mesh).

A given workload is only allowed to be part of one Canonical Service.

You can determine the full scope of a Canonical Service from the group of workloads that define it including:

  * **Hostnames and IP addresses**
  * **Network(s)**
  * **Network and security policies**
  * **Routing and load balancing**
  * **VM and container images**
  * **Physical or virtual infrastructure**
  * **Geographic region(s)**
  * **CI/CD system**
  * **Source code**
  * **Telemetry**
  * **Service level objectives and alerts**



You can view dashboards that display these operational details for each service on the [GKE Enterprise Services page](https://console.cloud.google.com/anthos/services).

## Canonical Service requirements and limitations

Each Canonical Service exists inside of a single Kubernetes or Istio namespace and cannot cross namespace boundaries.

You must give a Canonical Service a unique name within its parent namespace. For more information, see [defining a Canonical Service](https://docs.cloud.google.com/service-mesh/legacy/in-cluster/observability/defining-canonical-service).

Canonical Services can exist across multiple clusters and regions. While it is possible to break down resources and telemetry by cluster and region, those are not factors in determining the scope or uniqueness of a service.

Therefore, the unique identity of a Canonical Service is determined by:
    
    
    mesh id + namespace + canonical name.
    

## Revisions

Revisions refer to incremental changes to a service which you can use to distinguish and identify different "versions" or "releases" of your services.

Differentiate between revisions of a Canonical Service by labeling an individual workload with its "canonical revision." This label is an arbitrary string that you can define. While the label may be set automatically in some cases, you or the CI/CD system that deploys the service must apply the label. For guidance on setting this label, see [Defining a Canonical Service](https://docs.cloud.google.com/service-mesh/legacy/in-cluster/observability/defining-canonical-service).

Note that multiple revisions can be in production at the same time. Running multiple revisions at once is most often used to accomplish:

  * The progressive roll-out of a new binary, a new configuration, or both across all of the instances of one's service. In this case, both the old and new revisions are live during the transition.
  * An "A/B test" or "live experiment," in which two different versions of the service are exposed to subsets of downstream callers to test the effect of a change.



## What's next

  * [Defining a Canonical Service](https://docs.cloud.google.com/service-mesh/legacy/in-cluster/observability/defining-canonical-service).
  * [Canonical Services best practices](https://docs.cloud.google.com/service-mesh/legacy/in-cluster/observability/canonical-service-best-practices).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
