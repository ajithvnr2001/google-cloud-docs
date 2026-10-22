---
url: https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/developer-platform-controls/
title: Developer platform controls \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:10.011359+00:00
---

# Developer platform controls  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/developer-platform-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Developer platform controls Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-12-13 UTC

This section describes the controls that are used in the developer platform.

## Platform identity, roles, and groups

Access to Google Cloud services requires Google Cloud identities. The blueprint uses [fleet Workload Identity Federation for GKE](https://docs.cloud.google.com/anthos/fleet-management/docs/use-workload-identity) to map the Kubernetes service accounts that are used as identities for pods to Google Cloud service accounts that control access to Google Cloud services. To help protect against cross-environment escalations, each environment has a separate identity pool (known as a set of trusted identity providers) for its Workload Identity Federation for GKE accounts.

### Platform personas

When you deploy the blueprint, you create three types of user groups: a developer platform team, an application team (one team per application), and a security operations team.

The developer platform team is responsible for development and management of the developer platform. The members of this team are the following:

  * **Developer platform developers:** These team members extend the blueprint and integrate it into existing systems. This team also creates new application templates.
  * **Developer platform administrator:** This team is responsible for the following: 
    * Approving the creation of new tenants teams.
    * Performing scheduled and unscheduled tasks that affect multiple tenants, including the following:
    * Approving the promotion of applications to the nonproduction environment and the production environment.
    * Coordinating infrastructure updates.
    * Making platform-level capacity plans.



A tenant of the developer platform is a single software development team and those responsible for the operation of that software. The tenant team consists of two groups: application developers and application operators. The duties of the two groups of the tenant team are as follows:

  * **Application developers:** This team writes and debugs application code. They are sometimes also called _software engineers_ or _full-stack developers_. Their responsibilities include the following: 
    * Performing testing and quality assurance on an application component when it is deployed into the development environment.
    * Managing application-owned cloud resources (such as databases and storage buckets) in the development environment.
    * Designing database or storage schemas for use by applications.
  * **Application operators or site reliability engineers (SREs):** This team manages the reliability of applications that are running in the production environments, and the safe advancement of changes made by application developers into production. They are sometimes called _service operators_ , _systems engineers_ , or _system administrators_. Their responsibilities include the following: 
    * Planning application-level capacity needs.
    * Creating alerting policies and setting service level objectives (SLOs) for services.
    * Diagnosing service issues using logs and metrics that are specific to that application.
    * Responding to alerts and pages, such as when a service doesn't meet its SLOs.
    * Working with a group or several groups of application developers.
    * Approving deployment of new versions to production.
    * Managing application-owned cloud resources in the non-production and production environments (for example, backups and schema updates).



## Platform organization structure

The enterprise application blueprint uses the organization structure that is provided by the enterprise foundation blueprint. The following diagram shows how the enterprise application blueprint projects fit within the structure of the foundation blueprint.

![The blueprint projects and folders.](https://docs.cloud.google.com/static/architecture/blueprints/enterprise-application-blueprint/images/eab-org-structure.svg)

### Platform projects

The following table describes the additional projects, beyond those provided by the foundation blueprint, that the application blueprint needs for deploying resources, configurations, and applications.

Folder | Project | Description  
---|---|---  
`common` | `eab-infra-cicd` | Contains the [multi-tenant infrastructure pipeline](https://docs.cloud.google.com/architecture/blueprints/security-foundations/deploying-resources#multi-tenant-infrastructure) to deploy the tenant infrastructure.  
| `eab-app-factory` | Contains the [application factory ](https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/deployment-methodology#application-factory), which is used to create single-tenant application architecture and continuous integration and continuous deployment (CI/CD) pipelines. This project also contains the [Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/concepts/hierarchical-repo) that's used for GKE cluster configuration.  
| `eab-{tenant}-cicd` | Contains the application CI/CD pipelines, which are in independent projects to enable separation between development teams. There is one pipeline for each application.  
`development`,  
`nonproduction`,  
`production` | `eab-gke` | Contains the GKE clusters for the developer platform and the logic that is used to register clusters for fleet management.  
| `eab-{tenant`}(`1-n`) | Contains any single-tenant application services such as databases or other managed services that are used by an application team.  
  
## Platform cluster architecture

The blueprint deploys applications across three environments: development, non-production, and production. Each environment is associated with a fleet. In this blueprint, a fleet is a project that includes one or more clusters. However, fleets can also group several projects. A fleet provides a logical security boundary for administrative control. A fleet provides a way to logically group and normalize Kubernetes clusters, and makes administration of infrastructure easier.

The following diagram shows two GKE clusters, which are created in each environment to deploy applications. The two clusters act as identical GKE clusters in two different [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) to provide multi-region resiliency. To take advantage of fleet capabilities, the blueprint uses the concept of [sameness](https://docs.cloud.google.com/anthos/fleet-management/docs/fleet-concepts#sameness) across namespace objects, services, and identity.

![Blueprint clusters.](https://docs.cloud.google.com/static/architecture/blueprints/enterprise-application-blueprint/images/eab-cluster-architecture.svg)

The enterprise application blueprint uses GKE clusters with private spaces enabled through [Private Service Connect access to the control plane](https://cloud.google.com/blog/products/containers-kubernetes/understanding-gkes-new-control-plane-connectivity) and [private node pools](https://cloud.google.com/blog/products/containers-kubernetes/understanding-gkes-new-control-plane-connectivity) to remove potential attack surfaces from the internet. Neither the cluster [nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#nodes) nor the [control plane](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#control_plane) has a public endpoint. The cluster nodes run [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs) to limit their attack surface and the cluster nodes use [Shielded GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-nodes) to limit the ability of an attacker to impersonate a node.

Administrative access to the GKE clusters is enabled through the Connect gateway. As part of the blueprint deployment, one Cloud NAT instance is used for each environment to give pods and Config Sync a mechanism to access resources on the internet such as the GitHub. Access to the GKE clusters is controlled by [Kubernetes RBAC authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) that is based on [Google Groups for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#google-groups-for-gke). Groups let you control identities using a central identity management system that's controlled by identity administrators.

## Platform GKE components

The developer platform uses [GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) and related components to enable you to build, deliver, and manage the lifecycle of your applications.

The GKE components that are used in the blueprint deployment are the following:

  * GKE for container management
  * [Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller) for policy management and enforcement



The related components that are used in the blueprint deployment are the following:

  * [Cloud Service Mesh](https://cloud.google.com/products/service-mesh) for service management
  * [Binary Authorization](https://docs.cloud.google.com/binary-authorization) for container image attestation
  * [GKE Gateway controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api) for the multi-cluster gateway controller for GKE clusters



### Platform fleet management

[Fleets](https://docs.cloud.google.com/kubernetes-engine/docs/fleets-overview#introducing_fleets) provide you with the ability to manage multiple GKE clusters in a single unified way. [Fleet team management](https://docs.cloud.google.com/anthos/fleet-management/docs/team-management#fleet_team_management_overview) makes it easier for platform administrators to provision and manage infrastructure resources for developer platform tenants. Tenants have scoped control of resources within their own namespace, including their applications, logs, and metrics.

To provision subsets of fleet resources on a per-team basis, administrators can use _team scopes_. Team scopes let you define subsets of fleet resources for each team, with each team scope associated with one or more fleet member clusters.

Fleet namespaces provide control over who has access to specific namespaces within your fleet. The application uses two GKE clusters that are deployed on one fleet, with three team scopes, and each scope having one fleet namespace.

The following diagram shows the fleet and scope resources that correspond to sample clusters in an environment, as implemented by the blueprint.

![Blueprint fleet and scope resources.](https://docs.cloud.google.com/static/architecture/blueprints/enterprise-application-blueprint/images/eab-fleet-scopes.svg)

## Platform networking

For networking, GKE clusters are deployed in a Shared VPC that's created as part of the enterprise foundation blueprint. GKE clusters require multiple IP address ranges to be assigned in the development, non-production, and production environments. Each GKE cluster that's used by the blueprint needs separate IP address ranges allocated for the nodes, pods, services, and control plane. AlloyDB for PostgreSQL instances also requires separate IP address ranges.

The following table describes the VPC subnets and IP address ranges that are used in the different environments to deploy the blueprint clusters. For the development environment in _Application GKE cluster region 2_ , the blueprint deploys only one IP address space even though there is IP address space allocated for two development GKE clusters.

Resource | IP address range type | Development | Nonproduction | Production  
---|---|---|---|---  
Application GKE cluster region 1 | Primary IP address range | 10.0.64.0/24 | 10.0.128.0/24 | 10.0.192.0/24  
Pod IP address range | 100.64.64.0/24 | 100.64.128.0/24 | 100.64.192.0/24  
Service IP address range | 100.0.80.0/24 | 100.0.144.0/24 | 100.0.208.0/24  
GKE control plane IP address range | 10.16.0.0/21 | 10.16.8.0/21 | 10.16.16.0/21  
Application GKE cluster region 2 | Primary IP address range | 10.1.64.0/24 | 10.1.128.0/24 | 10.1.192.0/24  
Pod IP address range | 100.64.64.0/24 | 100.64.128.0/24 | 100.64.192.0/24  
Service IP address range | 100.1.80.0/24 | 100.1.144.0/24 | 100.1.208.0/24  
GKE control plane IP address range | 10.16.0.0/21 | 10.16.8.0/21 | 10.16.16.0/21  
AlloyDB for PostgreSQL | Database IP address range | 10.9.64.0/18 | 10.9.128.0/18 | 10.9.192.0/18  
  
If you need to design your own IP address allocation scheme, see [IP address management in GKE](https://cloud.google.com/blog/products/containers-kubernetes/ip-address-management-in-gke) and [GKE IPv4 address planning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-ip-address-mgmt-strategies).

## Platform DNS

The blueprint uses [Cloud DNS for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns) to provide DNS resolution for pods and Kubernetes services. Cloud DNS for GKE is a managed DNS that doesn't require a cluster-hosted DNS provider.

In the blueprint, Cloud DNS is configured for [VPC scope](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns#dns_scopes). VPC scope lets services in all GKE clusters in a project share a single DNS zone. A single DNS zone lets services be resolved across clusters, and VMs or pods outside the cluster can resolve services within the cluster.

#### Platform firewalls

GKE automatically creates [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) when creating [GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules#cluster-fws), [GKE services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules#service-fws), [GKE Gateway firewalls](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules#gateway-fws), and [GKE Ingress firewalls](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules#ingress-fws) that allow clusters to operate in your environments. The priority for all the automatically created firewall rules is 1000. These rules are needed as the enterprise foundation blueprint has a default rule to block traffic in the Shared VPC.

### Platform access to Google Cloud services

Because the blueprint applications use private clusters, [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access) provides access to Google Cloud services.

## Platform high availability

The blueprint was designed to be resilient to both zone and region outages. Resources needed to keep applications running are spread across two regions. You select the regions that you want to deploy the blueprint to. Resources that are not in the critical path for serving and responding to load are only one region or are global. The following table describes the resources and where they are deployed.

Location | Region 1 | Region 2 | Global  
---|---|---|---  
Environments with resources in this location | 

  * `common`
  * `development`
  * `nonproduction`
  * `production`

| 

  * `nonproduction`
  * `production`

| 

  * `common`
  * `development`
  * `nonproduction`
  * `production`

  
Projects with resources in this location | 

  * `eab-gke-{env}`
  * `eab-infra-cicd`
  * `eab-{ns}-cicd`

| 

  * `eab-gke-{env}`
  * `eab-{ns}-cicd (only for the Artifact Registry mirror)`

| 

  * `eab-gke-{env}`

  
Resource types in this location | 

  * GKE cluster (applications and the Gateway configuration)
  * Artifact Registry
  * AlloyDB for PostgreSQL
  * Cloud Build
  * Cloud Deploy

| 

  * GKE cluster (applications only)
  * Artifact Registry
  * AlloyDB for PostgreSQL

| 

  * Cloud Logging
  * Cloud Monitoring
  * Cloud Load Balancing
  * Fleet scopes
  * Fleet namespaces

  
  
The following table summarizes how different components react to a region outage or a zone outage, and how you can mitigate these effects.

Failure scope | External services effects | Database effects | Build and deploy effects | Terraform pipelines effects  
---|---|---|---|---  
A zone of Region 1 | Available. | Available.The [standby instance](https://docs.cloud.google.com/alloydb/docs/test-high-availability) becomes active with zero RPO. | Available, manual change might be needed.You might need to restart any `terraform apply` command that was in progress, but completed during the outage. | Available, manual change might be needed.You might need to restart any `terraform apply` command that was in progress, but completed during the outage.  
A zone of Region 2 | Available. | Available. | Available. | Available, manual change might be needed.You might need to restart any `terraform apply` command that was in progress, but completed during the outage.  
Region 1 | Available. | Manual change needed.An operator must [promote the secondary cluster](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/work-with-cross-region-replication#promote-secondary-cluster) manually. | Unavailable. | Unavailable.  
Region 2 | Available. | Available. | Available, manual change might be neededBuilds remain available. You might need to deploy new builds manually. Existing builds might not complete successfully. | Available.  
  
Cloud provider outages are only one source of downtime. High availability also depends on processes and operations that help make mistakes less likely. The following table describes all the decisions made in the blueprint that relate to high availability and the reasons for those decisions.

Blueprint decision | Availability impact  
---|---  
**Change management**  
Use GitOps and IaC. | Supports peer review of changes and supports reverting quickly to previous configurations.  
Promote changes gradually through environments. | Lowers the impact of software and configuration errors.  
Make non-production and production environments similar. | Ensures that differences don't delay discovery of an error. Both environments are dual-region.  
Change replicated resources one region at a time within an environment. | Ensures that issues that aren't caught by gradual promotion only affect half of the run-time infrastructure.  
Change a service in one region at a time within an environment. | Ensures that issues that aren't caught by gradual promotion only affect half of the service replicas.  
**Replicated compute infrastructure**  
Use a regional cluster control plane. | Regional control plane is available during upgrade and resize.  
Create a multi-zone node pool. | A cluster node pool has at least three nodes spread across three zones. For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones).   
Configure a Shared VPC network. | The Shared VPC network covers two regions. A regional failure only affects network traffic to and from resources in the failing region.  
Replicate the image registry. | Images are stored in Artifact Registry, which is configured to replicate to multiple regions so that a cloud region outage doesn't prevent application scale-up in the surviving region.  
**Replicated services**  
Deploy service replicas to two regions. | In case of a regional outage, a Kubernetes service remains available in the production and non-production environments.  
Use rolling updates to service changes within a region. | You can update Kubernetes services using a rolling update deployment pattern which reduces risk and downtime.  
Configure three replicas in a region for each service. | A Kubernetes service has at least three replicas (pods) to support rolling updates in the production and non-production environment.  
Spread the deployment's pods across multiple zones. | Kubernetes services are spread across VMs in different zones using an [anti-affinity](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#node-affinity) stanza. A single-node disruption or full zone outage can be tolerated without incurring additional cross-region traffic between dependent services.  
**Replicated storage**  
Deploy multi-zone database instances. | AlloyDB for PostgreSQL offers high availability in a region. Its primary instance's redundant nodes are located in two different zones of the region. The primary instance maintains regional availability by triggering an automatic failover to the standby zone if the active zone encounters an issue. Regional storage helps provide data durability in the event of a single-zone loss. For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones).   
Replicate databases cross-region. | AlloyDB for PostgreSQL uses cross-region replication to provide disaster recovery capabilities. The database asynchronously replicates your primary cluster's data into secondary clusters that are located in separate Google Cloud regions.  
**Operations**  
Provision applications for twice their expected load. | If one cluster fails (for example, due to a regional service outage), the portion of the service that runs in the remaining cluster can fully absorb the load.  
Repair nodes automatically. | The clusters are configured with [node auto repair](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-repair). If a node's consecutive health checks fail repeatedly over an extended time period, GKE initiates a repair process for that node.  
Ensure node pool upgrades are application-aware. | Deployments define a [pod disruption budget](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/upgrading-clusters#set-tolerance) with `maxUnavailable: 1` to allow [parallel node pool upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/upgrading-clusters#reduce-disruption) in large clusters. No more than one of three (in the development environment) or one of six (in non-production and production) replicas are unavailable during node pool upgrades.  
Automatically restart deadlocked services. | The deployment backing a service defines a [liveness probe](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-setting-up-health-checks-with-readiness-and-liveness-probes), which identifies and restarts deadlocked processes.  
Automatically check for replicas to be ready. | The deployment backing a service defines a [readiness probe](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-setting-up-health-checks-with-readiness-and-liveness-probes), which identifies when an application is ready to serve after starting. A readiness probe eliminates the need for manual checks or timed-waits during rolling updates and node pool upgrades.  
  
The reference architecture is designed for applications with zonal and regional high availability requirements. Ensuring high availability does incur some costs (for example, standby spare costs or cross-region replication costs). The [Alternatives](https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/deploy-blueprint#alternatives-default) section describes some ways to mitigate these costs.

## Platform quotas, performance limits, and scaling limits

You can control quotas, performance, and scaling of resources in the developer platform. The following list describes some items to consider:

  * The base infrastructure requires numerous projects, and each additional tenant requires four projects. You might need to request additional project quota before deploying and before adding more tenants.
  * There is a limit of 100 MultiClusterGateway resources for each project. Each internet-facing Kubernetes service on the developer platform requires one MultiClusterGateway.
  * Cloud Logging has a limit of 100 buckets in a project. The per-tenant log access in the blueprint relies on a bucket for each tenant.
  * To create more than 20 tenants, you can request an increase to the project's quota for Scope and Scope Namespace resources. For instructions on viewing quotas, see [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage). Use a filter to find the `gkehub.googleapis.com/global-per-project-scopes` and `gkehub.googleapis.com/global-per-project-scope-namespaces` quota types.



## What's next

  * Read about [service architecture](https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/service-architecture) (next document in this series).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-12-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-12-13 UTC."],[],[]] 
