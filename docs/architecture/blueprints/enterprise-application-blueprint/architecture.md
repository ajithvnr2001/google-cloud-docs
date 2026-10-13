---
url: https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/architecture/
title: Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:22:25.492038+00:00
---

# Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/architecture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Architecture Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-12-13 UTC

The following diagram shows the high-level architecture that is deployed by the blueprint for a single environment. You deploy this architecture across three separate environments: production, non-production, and development.

![The blueprint architecture.](https://docs.cloud.google.com/static/architecture/blueprints/enterprise-application-blueprint/images/eab-architecture.svg)

This diagram includes the following:

  * Cloud Load Balancing distributes application traffic across [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) to [Kubernetes service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service) objects. Behind each service is a logical grouping of related pods.
  * [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview#what_is_a_service_mesh) lets Kubernetes services communicate with each other.
  * Kubernetes services are grouped into tenants, which are represented as Kubernetes [namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/). Tenants are an abstraction that represent multiple users and workloads that operate in a cluster, with separate RBAC for access control. Each tenant also has its own project for tenant-specific cloud resources such as databases, storage buckets, and Pub/Sub subscriptions.
  * Namespaces with their own identities for accessing peer services and cloud resources. The identity is consistent across the same namespace in different clusters because of [fleet Workload Identity Federation for GKE](https://docs.cloud.google.com/anthos/fleet-management/docs/use-workload-identity). Each environment has a separate workload identity pool to mitigate privilege escalation between environments.
  * Each service has a dedicated pipeline that builds and deploys that service. The same pipeline is used to deploy the service into the development environment, then deploy the service into the non-production environment, and finally deploy the service into the production environment.



## Key architectural decisions for developer platform

The following table describes the architecture decisions that the blueprint implements.

Decision area | Decision | Reason  
---|---|---  
[Deployment archetype](https://docs.cloud.google.com/architecture/deployment-archetypes#what_is_a_deployment_archetype) | Deploy across multiple regions. | Permit availability of applications during region outages.  
[Organizational architecture](https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/developer-platform-controls#platform-organization) | Deploy on top of the enterprise foundation blueprint. | Use the organizational structure and security controls that are provided by the foundation.  
Use the three environment folders that are set up in the foundation: `development`, `nonproduction`, and `production`. | Provide isolation for environments that have different access controls.  
[Developer platform cluster architecture](https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/developer-platform-controls#platform-cluster) | Package and deploy applications as containers. | Support separation of responsibilities, efficient operations, and application portability.  
Run applications on GKE clusters. | Use a managed container service that is built by the company that pioneered containers.  
Replicate and run application containers in an active-active configuration. | Achieve higher availability and rapid progressive rollouts, improving development velocity.  
Provision the production environment with two GKE clusters in two different regions. | Achieve higher availability than a single cloud region.  
Provision the non-production environment with two GKE clusters in two different regions. | Stage changes to cross-regional settings, such as load balancers, before deployment to production.  
Provision the development environment with a single GKE cluster instance. | Helps reduce cost.  
Configure highly-available control planes for each GKE cluster. | Ensure that the cluster control plane is available during upgrade and resizing.  
Use the concept of [sameness](https://docs.cloud.google.com/anthos/fleet-management/docs/fleet-concepts#sameness) across namespaces, services, and identity in each GKE cluster. | Ensure that Kubernetes objects with the same name in different clusters are treated as the same thing. This normalization is done to make administering fleet resources easier.  
Enable private IP address spaces for GKE clusters through [Private Service Connect access to the control plane](https://cloud.google.com/blog/products/containers-kubernetes/understanding-gkes-new-control-plane-connectivity) and [private node pools](https://cloud.google.com/blog/products/containers-kubernetes/understanding-gkes-new-control-plane-connectivity). | Help protect the Kubernetes cluster API from scanning attacks.  
Enable administrative access to the GKE clusters through the [Connect gateway](https://docs.cloud.google.com/anthos/multicluster-management/gateway). | Use one command to fetch credentials for access to multiple clusters. Use groups and third-party identity providers to manage cluster access.  
Use [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) to provide GKE [pods](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview#pods) with access to resources with public IP addresses. | Improve the overall security posture of the cluster, because pods are not directly exposed to the internet, but are still able to access internet-facing resources.  
Configure nodes to use [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits) and [Shielded GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-nodes). | Limit the attack surface of the nodes.  
Associate each environment with a GKE [fleet](https://docs.cloud.google.com/kubernetes-engine/docs/fleets-overview). | Permit management of sets of GKE clusters as a unit.  
Use the [foundation infrastructure pipeline](https://github.com/terraform-google-modules/terraform-example-foundation/tree/master/5-app-infra) to deploy the [application factory](https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/deployment-methodology#application-factory), [fleet-scope pipeline](https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/deployment-methodology#fleet-scope-pipeline), and [multi-tenant infrastructure pipeline](https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/deployment-methodology#multi-tenant-infrastructure). | Provide a controllable, auditable, and repeatable mechanism to deploy application infrastructure.  
Configure GKE clusters using [GKE configuration and policy](https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/deployment-methodology#gke-configuration) management features. | Provide a service that allows configuration-as-code for GKE clusters.  
Use an [application factory](https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/deployment-methodology#application-factory) to deploy the application CI/CD pipelines used in the blueprint. | Provide a repeatable pattern to deploy application pipelines more easily.  
Use an [application CI/CD pipeline](https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/deployment-methodology#application-ci-cd) to build and deploy the blueprint application components. | Provide a controllable, auditable, and repeatable mechanism to deploy applications.  
Configure the application CI/CD pipeline to use [Cloud Build](https://docs.cloud.google.com/build), [Cloud Deploy](https://docs.cloud.google.com/deploy), and [Artifact Registry](https://docs.cloud.google.com/artifact-registry). | Use managed build and deployment services to optimize for security, scale, and simplicity.  
Use immutable containers across environments, and sign the containers with [Binary Authorization](https://docs.cloud.google.com/binary-authorization). | Provide clear code provenance and ensure that code has been tested across environments.  
Use [Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs/solutions/gke), which includes [Cloud Logging](https://docs.cloud.google.com/logging) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring). | Simplify operations by using an integrated managed service of Google Cloud.  
Enable [Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview) (a service in Security Command Center) to monitor the integrity of containers. | Use a managed service that enhances security by continually monitoring containers.  
Control access to the GKE clusters by [Kubernetes role-based access control (RBAC)](https://kubernetes.io/docs/reference/access-authn-authz/rbac/), which is based on [Google Groups for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/google-groups-rbac). | Enhance security by linking access control to Google Cloud identities.  
[Service architecture](https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/service-architecture) | Use a unique Kubernetes service account for each [Kubernetes service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service). This account acts as an IAM service account through the use of [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity). | Enhance security by minimizing the permissions each service needs to be provided.  
Expose services through the [GKE Gateway API](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api). | Simplify configuration management by providing a declarative-based and resource-based approach to managing ingress rules and load-balancing configurations.  
Run services as distributed services through the use of [Cloud Service Mesh](https://cloud.google.com/products/service-mesh) with [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service). | Provide enhanced security through enforcing authentication between services and also provides automatic fault tolerance by redirecting traffic away from unhealthy services.  
Use [cross-region replication](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/about-cross-region-replication) for AlloyDB for PostgreSQL. | Provide for high-availability in the database layer.  
[Network architecture](https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/developer-platform-controls#platform-networking) | Shared VPC instances are configured in each environment and GKE clusters are created in service projects. | Shared VPC provides centralized network configuration management while maintaining separation of environments.  
Use [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) in a [multi-cluster, multi-region configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-multi-cluster-gateways#external-gateway). | Provide a single anycast IP address to access regionalized GKE clusters for high availability and low-latency services.  
Use HTTPS connections for client access to services. Redirect any [client HTTP requests to HTTPS](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-global-http-https-redirect). | Help protect sensitive data in transit and help prevent person-in-the-middle-attacks.  
Use [Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs/overview) to manage public certificates. | Manage certificates in a unified way.  
Protect the web interface with [Google Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview). | Enhance security by protecting against common web application vulnerabilities and volumetric attacks.  
  
Your decisions might vary from the blueprint. For information about alternatives, see [Alternatives to default recommendations](https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/deploy-blueprint#alternatives-default).

## What's next

  * Read about [developer platform controls](https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/developer-platform-controls) (next document in this series).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-12-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-12-13 UTC."],[],[]] 
