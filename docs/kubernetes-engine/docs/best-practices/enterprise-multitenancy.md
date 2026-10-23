---
url: https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/enterprise-multitenancy/
title: Best practices for enterprise multi-tenancy \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:08.706957+00:00
---

# Best practices for enterprise multi-tenancy  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/enterprise-multitenancy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Best practices for enterprise multi-tenancy Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Multi-tenancy in Google Kubernetes Engine (GKE) refers to one or more clusters that are shared between tenants. In Kubernetes, a _tenant_ can be defined as any of the following:

  * A team responsible for developing and operating one or more workloads.
  * A set of related workloads, whether operated by one or more teams.
  * A single workload, such as a Deployment.



[Cluster multi-tenancy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multitenancy-overview#what_is_multi-tenancy) is often implemented to reduce costs or to consistently apply administration policies across tenants. However, incorrectly configuring a GKE cluster or its associated GKE resources can result in unachieved cost savings, incorrect policy application, or destructive interactions between different tenants' workloads.

This guide provides best practices to safely and efficiently set up multiple multi-tenant clusters for an enterprise organization. For a consolidated overview of all GKE best practices, see [Best practices for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices).

**Note:** For a summarized checklist of all the best practices, see the Checklist summary at the bottom of this guide. 

## Assumptions and requirements

The best practices in this guide are based on a multi-tenant use case for an enterprise environment, which has the following assumptions and requirements:

  * The organization is a single company that has many tenants (two or more application/service teams) that use Kubernetes and would like to share computing and administrative resources.
  * Each tenant is a single team developing a single workload.
  * Other than the application/service teams, there are other teams that also utilize and manage clusters, including platform team members, cluster administrators, auditors, etc.
  * The platform team owns the clusters and defines the amount of resources each tenant team can use; each tenant can request more.
  * Each tenant team should be able to deploy their application through the Kubernetes API without having to communicate with the platform team.
  * Each tenant should not be able to affect other tenants in the shared cluster, except via explicit design decisions like API calls, shared data sources, etc.



This setup will serve as a model from which we can demonstrate multi-tenant best practices. While this setup might not perfectly describe all enterprise organizations, it can be easily extended to cover similar scenarios.

**Note:** For Terraform modules and sample deployments, see the [GoogleCloudPlatform/gke-enterprise-mt](https://github.com/GoogleCloudPlatform/gke-enterprise-mt) GitHub repository. 

## Setting up folders, projects and clusters

**Best practices** :

Establish a folder and project hierarchy.  
Assign roles using IAM.  
Centralize network control with Shared VPCs.  
Create one cluster admin project per cluster.  
Make clusters private.  
Ensure the control plane for the cluster is regional.  
Ensure nodes in your cluster span at least three zones.  
Autoscale cluster nodes and resources.  
Schedule maintenance windows for off-peak hours.  
Set up an external Application Load Balancer with Ingress.  


For enterprise organizations deploying multi-tenant clusters in GKE, additional configuration is needed in other Google Cloud systems in order to manage the complexity which does not exist in simpler single-application, single-team Kubernetes deployments. This includes both project configuration for isolating administrative concerns as well as mapping organization structure to cloud identities and accounts and managing additional Google Cloud resources, such as databases, logging and monitoring, storage, and networking.

### Establish a folder and project hierarchy

To capture how your organization manages Google Cloud resources and to enforce a separation of concerns, use [folders](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#folders) and [projects](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects). Folders allow different teams to set policies that cascade across multiple projects, while projects can be used to segregate environments (for example, production vs. staging) and teams from each other. For example, most organizations have a team to manage network infrastructure and a different team to manage clusters. Each technology is considered a separate piece of the stack requiring its own level of expertise, troubleshooting and access.

A parent folder can contain up to 300 folders, and you can nest folders up to 10 levels deep. If you have over 300 tenants, you can arrange the tenants into nested hierarchies to stay within the limit. For more information about folders, see [Creating and Managing Folders](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders).

#### Demonstrating this practice

For our enterprise environment, we created three top-level folders dedicated to resources for each of the following teams:

  * **Network Team** : A folder dedicated for the network team to manage network resources. This folder contains subfolders for the tenant network and the cluster network(s), which we discuss further in the Centralize network control section. Each subfolder contains one project per environment (development, staging, and production) to host the virtual private clouds (VPCs) that provide all network connectivity in the organization.
  * **Cluster Team** : A folder dedicated for the platform team to manage clusters per environment. This folder contains a subfolder for each environment (development, staging, and production), each of which contains one or more projects to accommodate the clusters.
  * **Tenants** : A folder dedicated for managing tenants. This folder contains a subfolder for each tenant to host their non-cluster resources, each of which may contain one or more projects (or even subfolders) as required by the individual tenant.

[ ![Folder hierarchy](https://docs.cloud.google.com/static/kubernetes-engine/images/enterprise-folder-hierarchy.svg)](https://docs.cloud.google.com/static/kubernetes-engine/images/enterprise-folder-hierarchy.svg) **Figure 1:** Folder hierarchy

Note that we recommend per-environment projects for the network and tenant teams, but per-environment folders for the cluster team, where each folder groups projects for each environment (for example, the production folder contains production projects). The reason for this configuration is that the cluster team has specialized segregation needs, and projects are the primary method for segregating resources in Google Cloud. For example, the cluster team might choose to host only one cluster in each project for the following reasons: 

  * _Cluster configuration_ : Some configurations, such as Identity and Access Management (IAM), are per-project. Placing different clusters in different projects ensures that a misconfiguration in one project will not affect all clusters in an environment simultaneously, and allows you to progressively roll out and validate changes to your configuration.
  * _Workload security_ : By default, workloads running in different projects are far more segregated from one another than workloads in the same project. Hosting clusters in dedicated projects ensures that a compromised, misbehaving or malicious workload in one cluster has limited impact.
  * _Resource quota_ : Quotas are established and enforced per-project. Spreading clusters across projects limits the impact of a single workload (for example, in an autoscaled cluster) from exhausting the entire environment's limits.



It may still be useful to apply certain low-risk policies to "all production clusters", regardless of the projects in which they are segregated. The cluster team's per-environment folders allows these kinds of policies to be easily applied. These folders can also be used with aggregated log sinks, allowing for easy per-environment log exporting.

This recommended topology can easily be extended or simplified depending on your organization's needs. For example, smaller organizations with looser service level objectives (SLOs) may choose to keep all their per-environment clusters in a single project, in which case the per-environment folders are unnecessary. It is also valid to reduce the number of clusters to fit your needs.

### Assign roles using IAM

You can control access to Google Cloud resources through [IAM](https://docs.cloud.google.com/iam/docs/overview) policies. Start by identifying the groups needed for your organization and their scope of operations, then assign the appropriate [IAM role](https://docs.cloud.google.com/iam/docs/understanding-roles) to the group.

Use Google Groups to efficiently assign and manage IAM for users. 

#### Demonstrating this practice

For our enterprise environment, we defined the following groups and role assignments:

Group | Function | IAM roles  
---|---|---  
Org Admin | Organizes the structure of the resources used by the organization. | Organization Administrator, Billing Account Creator, Billing Account User, Shared VPC Admin, Project Creator  
Folder Admin | Creates and manages folders and projects in the organization's folders. | Folder Admin, Project Creator, Billing Account User  
Network Admin | Creates networks, VPCs, subnets, firewall rules, and IP Address Management (IPAM). | Compute Network Admin  
Security Admin | Manages all logs (and audit logs), secret management, isolation and incident response. | Compute Security Admin  
Auditor | Reviews security events logs and system configurations. | Private Logs Viewer  
Cluster Admin | Manages all clusters, including node pools, instances and system workloads. | Kubernetes Engine Admin  
Tenant Admin1 | Manages all tenant namespaces and tenant users. | Kubernetes Engine Viewer  
Tenant Developer1 | Manages and troubleshoots workloads in the tenant namespaces. | Kubernetes Engine Viewer  
  
1Tenant groups require additional access control in Kubernetes RBAC.↩

### Centralize network control

To maintain centralized control over network resources, such as subnets, routes, and firewalls, use [Shared VPC networks](https://docs.cloud.google.com/vpc/docs/shared-vpc). Resources in a Shared VPC can communicate with each other securely and efficiently across project boundaries using internal IPs. Each Shared VPC network is defined and owned by a centralized _host project_ , and can be used by one or more _service projects_.

Using Shared VPC and IAM, you can separate network administration from project administration. This separation helps you implement the principle of least privilege. For example, a centralized network team can administer the network without having any permissions into the participating projects. Similarly, the project admins can manage their project resources without any permissions to manipulate the shared network.

When you set up a Shared VPC, you must configure the subnets and their secondary IP ranges in the VPC. To determine the subnet size, you need to know the expected number of tenants, the number of Pods and Services they are expected to run, and the maximum and average Pod size. Calculating the total cluster capacity needed will allow for an understanding of the desired instance size, and this provides the total node count. With the total number of nodes, the total IP space consumed can be calculated, and this can provide the desired subnet size.

Here are some factors that you should also consider when setting up your network:

  * The maximum number of service projects that can be attached to a host project is [1,000](https://docs.cloud.google.com/vpc/docs/quota#shared-vpc), and the maximum number of Shared VPC host projects in a single organization is [100](https://docs.cloud.google.com/vpc/docs/quota#shared-vpc).
  * The Node, Pod, and Services [IP ranges](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#cluster_sizing) must all be unique. You cannot create a subnet whose primary and secondary IP address ranges overlap.
  * The maximum number of Pods and Services for a given GKE cluster is limited by the size of the cluster's secondary ranges.
  * The [maximum number of nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#node_limiters) in the cluster is limited by the size of the cluster's subnet's primary IP address range and the cluster's Pod address range.
  * For flexibility and more control over IP address management, you can [configure the maximum number of Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr) that can run on a node. By reducing the number of Pods per node, you also reduce the CIDR range allocated per node, requiring fewer IP addresses.



For information on network ranges in a VPC cluster, see [Creating a VPC-native cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#cluster_sizing).

Tenants that require further isolation for resources that run outside the shared clusters (such as dedicated Compute Engine VMs) may use their own VPC, which is peered to the Shared VPC run by the networking team. This provides additional security at the cost of increased complexity and numerous other limitations. For more information on peering, see [Using VPC Network Peering](https://docs.cloud.google.com/vpc/docs/using-vpc-peering). In the example below, all tenants have chosen to share a single (per-environment) tenant VPC.

#### Demonstrating this practice

Our organization has a dedicated network team to manage both the tenant networks and the cluster networks. The Cluster Network folder contains a host project for each environment to host a Shared VPC. This means that the development, staging, and production environments each have their own Shared VPC networks for their service projects to connect to. Each service project contains a cluster that is connected to the associated subnet for each environment.

The Tenant Network folder also contains a host project per environment, and each project hosts a Shared VPC. Tenants A and B are service projects of the tenant network host project and share the same subnet for their non-cluster resources, to reduce networking overhead/IP space and allow the network team to easily control the network and related resources. Each tenant network is peered to the corresponding cluster network in the same environment. 

[ ![Folder hierarchy](https://docs.cloud.google.com/static/kubernetes-engine/images/enterprise-project-architecture.svg)](https://docs.cloud.google.com/static/kubernetes-engine/images/enterprise-project-architecture.svg) **Figure 2:** Project architecture for Shared VPC networks  
To accommodate each cluster's potential future growth, we created the following CIDR ranges for our networks: Network | Subnet | CIDR Range | No. of addresses  
---|---|---|---  
Tenant Network | Tenant subnet | `10.0.0.0/16` | 65,536  
Each tenant per environment | `/22-/25` | 1024 - 128  
Development Network | Development subnet | `10.17.0.0/16` | 65,536  
Pod secondary IP range | `10.16.0.0/16` | 65,536  
Service secondary IP range | `10.18.0.0/16` | 65,536  
Control plane IP range | `10.19.0.0/28` | 16  
Staging Network | Staging subnet | `10.33.0.0/16` | 65,536  
Pod secondary IP range | `10.32.0.0/16` | 65,536  
Service secondary IP range | `10.34.0.0/16` | 65,536  
Control plane IP range | `10.35.0.0/28` | 16  
Production Network | Production subnet | `10.49.0.0/16` | 65,536  
Pod secondary IP range | `10.48.0.0/16` | 65,536  
Service secondary IP range | `10.50.0.0/16` | 65,536  
Control plane IP range | `10.51.0.0/28` | 16  
  
### Creating reliable and highly available clusters

Design your cluster architecture for high availability and reliability by implementing the following recommendations:

  * Create one cluster admin project per cluster to reduce the risk of project-level configurations (for example, IAM bindings) adversely affecting many clusters, and to help provide separation for quota and billing. Cluster admin projects are separate from _tenant_ projects, which individual tenants use to manage, for example, their Google Cloud resources.
  * [Configure your network isolation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation) to disable access to the nodes and manage access to the control plane. We also recommend configuring your network isolation for development and staging environments.
  * Ensure the control plane for the cluster is [regional](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters) to provide high availability for multi-tenancy; any disruptions to the control plane will impact tenants. Please note, there are [cost implications](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters#pricing) with running regional clusters. [Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview#comparison) are pre-configured as regional clusters.
  * Ensure the nodes in your cluster span at least three zones to achieve zonal reliability. For information about the cost of egress between zones in the same region, see the [network pricing](https://docs.cloud.google.com/vpc/network-pricing#general) documentation.

[ ![A private regional cluster with a regional control plane running in three zones](https://docs.cloud.google.com/static/kubernetes-engine/images/enterprise-regional-cluster-and-planes.svg)](https://docs.cloud.google.com/static/kubernetes-engine/images/enterprise-regional-cluster-and-planes.svg) **Figure 3:** A private regional cluster with a regional control plane running in three zones.

#### Autoscale cluster nodes and resources

To accommodate the demands of your tenants, automatically scale nodes in your cluster by enabling [autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler).

Autoscaling helps systems appear responsive and healthy when heavy workloads are deployed by various tenants in their namespaces, or to respond to zonal outages.

With Autopilot clusters, node pools are automatically scaled to meet the requirements of your workloads.

When you enable autoscaling, you specify the minimum and maximum number of nodes in a cluster based on the expected workload sizes. By specifying the maximum number of nodes, you can ensure there is enough space for all Pods in the cluster, regardless of the namespace they run in. Cluster autoscaling rescales node pools based on the min/max boundary, helping to reduce operational costs when the system load decreases, and avoid Pods going into a pending state when there aren't enough available cluster resources. To determine the maximum number of nodes, identify the maximum amount of CPU and memory that each tenant requires, and add those amounts together to get the total capacity that the cluster should be able to handle if all tenants were at the limit. Using the maximum number of nodes, you can then choose instance sizes and counts, taking into consideration the IP subnet space made available to the cluster.

Use Pod autoscaling to automatically scale Pods based on resource demands. [Horizontal Pod Autoscaler (HPA)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler) scales the number of Pod replicas based on CPU/memory utilization or custom metrics. [Vertical Pod Autoscaling (VPA)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler) can be used to automatically scale Pods resource demands. It should not be used with HPA unless custom metrics are available as the two autoscalers can compete with each other. For this reason, start with HPA and only later VPA when needed.

#### Determine the size of your cluster

When determining the size of your cluster, here are some important factors to consider:

  * The sizing of your cluster is dependent on the type of workloads you plan to run. If your workloads have greater density, the cost efficiency is higher but there is also a greater chance for resource contention.
  * The minimum size of a cluster is defined by the number of zones it spans: one node for a zonal cluster and three nodes for a regional cluster.
  * Per project, there is a maximum of 50 clusters per zone, plus 50 regional clusters per region.
  * Per cluster, the following maximum values apply to nodes:

    * 2,000 nodes per zone per node pool.
    * With the Google Kubernetes Engine Ingress controller, 1,000 nodes per zone per cluster.
    * Up to 5,000, 15,000, or 65,000 nodes per cluster. Not all node increases are automatic. Depending on your target node count, there are specific infrastructure requirements, and you might need to contact Cloud Customer Care. For detailed information, see [Cluster size limits and requirements](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-large-clusters#clusters-5k-nodes).
    * Up to 512 Pods per node in Standard clusters (dynamically set up to 256 in Autopilot clusters).
    * 200,000 Pods per cluster, and 400,000 containers per cluster.

Refer to the [Quotas and limits page](https://docs.cloud.google.com/kubernetes-engine/quotas) for additional information.




#### Schedule maintenance windows

To reduce downtimes during cluster/node upgrades and maintenance, schedule [maintenance windows](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions) to occur during off-peak hours. During upgrades, there can be temporary disruptions when workloads are moved to recreate nodes. To ensure minimal impact of such disruptions, schedule upgrades for off-peak hours and design your application deployments to handle partial disruptions seamlessly, if possible.

#### Set up an external Application Load Balancer with Ingress

To help with the management of your tenants' published [Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service) and the management of incoming traffic to those Services, create an [HTTP(s) load balancer](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) to allow a single ingress per cluster, where each tenant's Services are registered with the cluster's [Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress) resource. You can create and configure an HTTP(S) load balancer by creating a Kubernetes Ingress resource, which defines how traffic reaches your Services and how the traffic is routed to your tenant's application. By registering Services with the Ingress resource, the Services' naming convention becomes consistent, showing a single ingress, such as `tenanta.example.com` and `tenantb.example.com`.

## Securing the cluster for multi-tenancy

**Best practices** :

Control Pod communication with network policies.  
Run workloads with GKE Sandbox.  
Set up policy-based admission controls.  
Use Workload Identity Federation for GKE to grant access to Google Cloud services.  
Restrict network access to the control plane.  


### Control Pod communication with network policies

To control network communication between Pods in each of your cluster's namespaces, create [network policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy) based on your tenants' requirements. As an initial recommendation, you should block traffic between namespaces that host different tenants' applications. Your cluster administrator can apply a `deny-all` network policy to deny all ingress traffic to avoid Pods from one namespace accidentally sending traffic to Services or databases in other namespaces.

As an example, here's a network policy that restricts ingress from all other namespaces to the `tenant-a` namespace:
    
    
    apiVersion: networking.k8s.io/v1
    kind: NetworkPolicy
    metadata:
      name: deny-all
      namespace: tenant-a
    spec:
      podSelector:
        matchLabels:
    
      ingress:
      - from:
        - podSelector: {}
    

### Run workloads with GKE Sandbox

Clusters that run untrusted workloads are more exposed to security vulnerabilities than other clusters. Using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods), you can harden the isolation boundaries between workloads for your multi-tenant environment. For security management, we recommend starting with GKE Sandbox and then using policy-based admission controls to fill in any gaps.

GKE Sandbox is based on [gVisor](https://gvisor.dev/), an open source container sandboxing project, and provides additional isolation for multi-tenant workloads by adding an extra layer between your containers and host OS. Container runtimes often run as a privileged user on the node and have access to most system calls into the host kernel. In a multi-tenant cluster, one malicious tenant can gain access to the host kernel and to other tenant's data. GKE Sandbox mitigates these threats by reducing the need for containers to interact with the host by shrinking the attack surface of the host and restricting the movement of malicious actors.

GKE Sandbox provides two isolation boundaries between the container and the host OS:

  * A user-space kernel, written in Go, that handles system calls and limits interaction with the host kernel. Each Pod has its own isolated user-space kernel.
  * The user-space kernel also runs inside namespaces and seccomp filtering system calls.



### Set up policy-based admission controls

To prevent Pods that violate your security boundaries from running in your cluster, use an admission controller. Admission controllers can check Pod specifications against policies that you define, and can prevent Pods that violate those policies from running in your cluster.

GKE supports the following types of admission control:

  * [Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-policy-controller): Declare pre-defined or custom policies and enforce them in clusters at scale using fleets. Policy Controller is an implementation of the open source [Gatekeeper open policy agent](https://github.com/open-policy-agent/gatekeeper) and is a feature of GKE Enterprise.

  * [PodSecurity admission controller](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/podsecurityadmission): Enforce pre-defined policies that correspond to the [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) in individual clusters or in specific namespaces.




### Use Workload Identity Federation for GKE to grant access to Google Cloud services

To securely grant workloads access to Google Cloud services, enable [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) in the cluster. Workload Identity Federation for GKE helps administrators manage Kubernetes service accounts that Kubernetes workloads use to access Google Cloud services. When you create a cluster with Workload Identity Federation for GKE enabled, an identity namespace is established for the project that the cluster is housed in. The identity namespace allows the cluster to automatically authenticate service accounts for GKE applications by mapping the Kubernetes service account name to a virtual Google service account handle, which is used for IAM binding of tenant Kubernetes service accounts.

### Restrict network access to the control plane

To protect your control plane, restrict access to authorized networks. In GKE, when you enable [authorized networks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks), you can authorize up to 50 CIDR ranges and allow IP addresses only in those ranges to access your control plane. GKE already uses Transport Layer Security (TLS) and authentication to provide secure access to your control plane endpoint from the public internet. By using authorized networks, you can further restrict access to specified sets of IP addresses.

## Tenant provisioning

**Best practices** :

Create tenant projects.  
Use RBAC to refine tenant access.  
Create namespaces for isolation between tenants.  


### Create tenant projects

To host a tenant's non-cluster resources, create a service project for each tenant. These service projects contain logical resources specific to the tenant applications (for example, logs, monitoring, storage buckets, service accounts, etc.). All tenant service projects are connected to the Shared VPC in the tenant host project.

### Use RBAC to refine tenant access

Define finer-grained access to cluster resources for your tenants by using [Kubernetes RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/). On top of the read-only access initially granted with IAM to tenant groups, define namespace-wide Kubernetes RBAC roles and bindings for each tenant group.

Earlier we identified two tenant groups: tenant admins and tenant developers. For those groups, we define the following RBAC roles and access:

Group | Kubernetes  
RBAC role | Description  
---|---|---  
Tenant Admin | namespace admin | Grants access to list and watch deployments in their namespace. Grants access to add and remove users in the tenant group.  
Tenant Developer | namespace editor,  
namespace viewer | Grants access to create/edit/delete Pods, deployments, Services, configmaps in their namespace.  
  
In addition to creating RBAC roles and bindings that assign Google Workspace or Cloud Identity groups various permissions inside their namespace, Tenant admins often require the ability to manage users in each of those groups. Based on your organization's requirements, this can be handled by either delegating Google Workspace or Cloud Identity permissions to the Tenant admin to manage their own group membership or by the Tenant admin engaging with a team in your organization that has Google Workspace or Cloud Identity permissions to handle those changes.

#### Demonstrating this practice

For our enterprise model, we created a manifest with the following Kubernetes RBAC roles, binded to the tenant groups mentioned above:

  * **namespace admin** : Defined with the `admin` `ClusterRole` in a `RoleBinding` to allow read and write access for resources in its namespace, including the ability to create roles and role bindings in the namespace.
  * **namespace editor** : Defined with the `edit` `ClusterRole` in a `RoleBinding` to allow read/write access to Pods, deployments, Services, configmaps in the tenant namespace.
  * **namespace viewer** : Defined with the `view` `ClusterRole` in a `RoleBinding` to allow read-only access to Pods, deployments, Services, configmaps in the tenant namespace.

You can use IAM and RBAC permissions together with namespaces to restrict user interactions with cluster resources on Google Cloud console. For more information, see [ Enable access and view cluster resources by namespace](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/restrict-resources-access-by-namespace). 

#### Use Google Groups to bind permissions

To efficiently manage tenant permissions in a cluster, you can bind RBAC permissions to your [Google Groups](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#google-groups-for-gke). The membership of those groups are maintained by your Google Workspace administrators, so your cluster administrators do not need detailed information about your users.

As an example, we have a Google Group named `tenant-admins@mydomain.com` and a user named `admin1@mydomain.com` is a member of that group, the following binding provides the user with admin access to the `tenant-a` namespace:
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: RoleBinding
    metadata:
      namespace: tenant-a
      name: tenant-admin-rolebinding
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: Role
      name: tenant-admin
    subjects:
    - apiGroup: rbac.authorization.k8s.io
      kind: Group
      name: "tenant-admins@mydomain.com"
    

### Create namespaces

To provide a logical isolation between tenants that are on the same cluster, implement [namespaces](https://kubernetes.io/docs/tasks/administer-cluster/namespaces/). As part of the Kubernetes RBAC process, the cluster admin creates namespaces for each tenant group. The Tenant admin manages users (tenant developers) within their respective tenant namespace. Tenant developers are then able to use cluster and tenant specific resources to deploy their applications.

#### Avoid reaching namespace limits

The theoretical maximum number of namespaces in a cluster is 10,000, though in practice there are many factors that could prevent you from reaching this limit. For example, you might reach the cluster-wide maximum number of Pods (150,000) and nodes (5,000) before you reach the maximum number of namespaces; other factors (such as the number of Secrets) can further reduce the effective limits. As a result, a good initial rule of thumb is to only attempt to approach the theoretical limit of one constraint at a time, and stay approximately one order of magnitude away from the other limits, unless experimentation shows that your use cases work well. If you need more resources than can be supported by a single cluster, you should create more clusters. For information about Kubernetes scalability, see the [Kubernetes Scalability thresholds](https://github.com/kubernetes/community/blob/master/sig-scalability/configs-and-limits/thresholds.md) article.

#### Standardize namespace naming

To ease deployments across multiple environments that are hosted in different clusters, standardize the namespace naming convention you use. For example, avoid tying the environment name (development, staging, and production) to the namespace name and instead use the same name across environments. By using the same name, you avoid having to change the config files across environments.

#### Create service accounts for tenant workloads

Create a tenant-specific Google service account for each distinct workload in a tenant namespace. This provides a form of security, ensuring that tenants can manage service accounts for the workloads that they own/deploy in their respective namespaces. The Kubernetes service account for each namespace is mapped to one Google service account by using Workload Identity Federation for GKE.

### Enforce resource quotas

To ensure all tenants that share a cluster have fair access to the cluster resources, enforce [resources quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/). Create a resource quota for each namespace based on the number of Pods deployed by each tenant, and the amount of memory and CPU required by each Pod.

The following example defines a resource quota where Pods in the `tenant-a` namespace can request up to 16 CPU and 64 GB of memory, and the maximum CPU is 32 and the maximum memory is 72 GB.
    
    
    apiVersion: v1
    kind: ResourceQuota
    metadata:
      name: tenant-a
    spec:
      hard: "1"
        requests.cpu: "16"
        requests.memory: 64Gi
        limits.cpu: "32"
        limits.memory: 72Gi
    

## Monitoring, logging and usage

**Best practices** :

Track usage metrics.  
Provide tenant-specific logs.  


### Track usage metrics

To obtain cost breakdowns on individual namespaces and labels in a cluster, you can enable [GKE cost allocation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-allocations). GKE cost allocation tracks information about resource requests and resource usage of a cluster's workloads, which you can further break down by namespaces and labels. With GKE cost allocation, you can approximate the cost breakdown for departments/teams that are sharing a cluster, understand the usage patterns of individual applications (or even components of a single application), help cluster admins triage spikes in usage, and provide better capacity planning and budgeting.

When you enable GKE cost allocation, the cluster name and namespace of your GKE workloads appear in the labels field of the [billing export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup).

**Note:** GKE cost allocation is not supported in [Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview#add-ons).

### Provide tenant-specific logs

To provide tenants with log data specific to their project workloads, use Cloud Logging's [Log Router](https://docs.cloud.google.com/logging/docs/routing/overview). To create tenant-specific logs, the cluster admin creates a [sink](https://docs.cloud.google.com/logging/docs/routing/overview#sinks) to export log entries to a [log bucket](https://docs.cloud.google.com/logging/docs/buckets) created in the tenant's Google Cloud project.

For details on how to configure these types of logs, see [Multi-tenant logging on GKE](https://docs.cloud.google.com/stackdriver/docs/solutions/kubernetes-engine/multi-tenant-logging).

## Checklist summary

The following table summarizes the tasks that are recommended for creating multi-tenant clusters in an enterprise organization:

Area | Tasks  
---|---  
Organizational setup | 

  * Define your resource hierarchy.
  * Create folders based on your organizational hierarchy and environmental needs.
  * Create host and service projects for your clusters and tenants.

  
Identity and access management | 

  * Identify and create a set of Google Groups for your organization.
  * Assign users and IAM policies to the groups.
  * Refine tenant access with namespace-scoped roles and role bindings.
  * Grant tenant admin access to manage tenant users.

  
Networking | 

  * Create per-environment Shared VPC networks for the tenant and cluster networks.

  
High availability and reliability | 

  * Create one cluster admin project per cluster to reduce any adverse impacts to clusters.
  * Configure the network isolation of your cluster.
  * Ensure the control plane for the cluster is regional.
  * Span nodes for the cluster over at least three zones.
  * Enable cluster autoscaling and Pod autoscaling.
  * Specify maintenance windows to occur during off-peak hours.
  * Create an HTTP(s) load balancer to allow a single ingress per multi-tenant cluster.

  
Security | 

  * Create namespaces to provide isolation between tenants that are on the same cluster.
  * Create network policies to restrict communication between Pods.
  * Mitigate threats by running workloads on GKE Sandbox.
  * Use admission controls to only allow deploying Pods that meet your security baselines.
  * Enable Workload Identity Federation for GKE to manage Kubernetes service accounts and access.
  * Enable authorized networks to restrict access to the control plane.

  
Logging and monitoring | 

  * Enforce resource quotas for each namespace.
  * Track usage metrics with GKE cost allocation.
  * Set up tenant-specific logging.

  
  
## What's next

  * For more information on security, see [Hardening your cluster's security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster).
  * For more information on VPC networks, see [Best practices and reference architectures for VPC design](https://docs.cloud.google.com/solutions/best-practices-vpc-design).
  * For more enterprise best practices, see [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
