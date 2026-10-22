---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster/
title: Best practices for hardening your cluster's security \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:27.944028+00:00
---

# Best practices for hardening your cluster's security  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Best practices for hardening your cluster's security Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document provides best practices for improving the security of your Google Kubernetes Engine (GKE) environments. Security specialists who define, govern, and implement policies and procedures can use these best practices to protect their organization's data.

For a consolidated overview of all GKE best practices, see [Best practices for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices). 

You should already be familiar with the following:

  * [General overview of GKE security](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)
  * [GKE cluster architecture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture)



New GKE clusters implement many of the best practices in this document by default. Autopilot mode clusters have a stricter default security posture than Standard mode clusters.

To implement and enforce the best practices in this document across your organization, consider the following services:

  * [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview): automatically check whether your clusters implement many of these best practices and check for other common misconfigurations.
  * [Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview): enforce specific best practices on GKE resource in an organization, folder, or project. Specific sections in this document have links to the Google Cloud console for you to apply [managed constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#managed-constraints) for those recommendations.



## Google Cloud environment design

The following sections describe security measures that you should consider when you plan and design your resources in Google Cloud. Cloud architects should use these recommendations when planning and defining Google Cloud architecture.

Best practices

Plan your Google Cloud resource structure

Plan multi-tenant environments

Use Tags to group Google Cloud resources

Plan your VPC networks

Design an incident response plan

### Plan your Google Cloud resource structure

**Recommended** : implement the [enterprise foundations blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations), which is a complete foundation for your enterprise environment based on our best practices.

The architecture of your Google Cloud organizations, folders, and projects affects your security posture. Design these foundational resources in a way that enables governance and security controls at scale across your services.

### Plan multi-tenant environments

**Recommended** : implement Google Cloud and GKE best practices for multi-tenant enterprise platforms.

Many GKE customers manage distributed teams, with separate engineering workflows and responsibilities. These _multi-tenant environments_ must have shared infrastructure that all of your developers can use, while restricting access to components based on roles and responsibilities. The enterprise application blueprint builds on the [enterprise foundations blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations) to help you to deploy internal developer platforms in multi-tenant environments.

For more information, see the following documents:

  * [Deploy an enterprise developer platform on Google Cloud](https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint)
  * [Best practices for enterprise multi-tenancy](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/enterprise-multitenancy)



### Use tags to group Google Cloud resources

**Recommended** : use tags to organize GKE resources for conditional policy enforcement and improved accountability across your teams.

Tags are metadata that you can attach to resources in your organizations, folders, and projects to identify business dimensions across your Google Cloud resource hierarchy. You can attach tags to GKE clusters and node pools, and then use those tags to conditionally apply IAM policies and firewall policies.

For more information, see the following documents:

  * [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview)
  * [Manage GKE resources using Tags](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tags)



### Plan your VPC networks

**Recommended** : implement Google Cloud and GKE best practices for VPC network design.

Your VPC network design and the features that you use impact your network security. Plan your networks based on your Google Cloud resource hierarchy and your security objectives. For more information, see the following documents:

  * [Best practices and reference architectures for VPC design](https://docs.cloud.google.com/architecture/best-practices-vpc-design)
  * [Best practices for GKE networking](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/networking#vpc-design)



### Design an incident response plan

**Recommended** : create and maintain an incident response plan that meets your security and reliability goals.

Security incidents can occur even when you implement every possible security control. An incident response plan helps you to identify potential gaps in your security controls, respond quickly and effectively to various types of incidents, and reduce downtime during an outage. For more information, see the following documents:

  * [Mitigate security incidents](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/security-mitigations)
  * [Well-Architected Framework: Security, privacy, and compliance pillar](https://docs.cloud.google.com/architecture/framework/security)



## Google Cloud network security

The following sections provide security recommendations for your VPC networks. Network architects and network administrators should apply these recommendations to reduce the attack surface at the network level and to limit the impact of unintended network access.

Best practices

Use least-privilege firewall rules

Use Shared VPC for cross-project traffic

Use separate networks to isolate environments

### Use least-privilege firewall rules

**Recommended** : when you create firewall rules, use the principle of least privilege to provide access only for the required purpose. Ensure that your firewall rules don't conflict with, or override, the GKE default firewall rules when possible.

GKE creates [default VPC firewall rules](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules) to enable system functionality and to enforce good security practices. If you create permissive firewall rules with a higher priority than a default firewall rule (for example, a firewall rule that allows all ingress traffic for debugging), your cluster is at risk of unintended access.

### Use Shared VPC for cross-project traffic

**Recommended** : use Shared VPC to let resources in multiple projects communicate with each other by using internal IP addresses.

Resources in different projects in your organization might need to communicate with each other. For example, frontend services in a GKE cluster in one project might need to communicate with backend Compute Engine instances in a different project.

For more information, see the following documents:

  * [Shared VPC overview](https://docs.cloud.google.com/vpc/docs/shared-vpc)
  * [Configure clusters with Shared VPC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc)



### Use separate networks to isolate environments

**Recommended** : use separate Shared VPC networks for staging, test, and production environments.

Isolate your development environments from each other to reduce the impact and risk of unauthorized access or disruptive bugs. For more information, see [Multiple host projects](https://docs.cloud.google.com/vpc/docs/shared-vpc#example_multiple_host_projects).

## Immutable security settings

The following sections provide security recommendations that you can configure only when you create clusters or node pools. You can't update existing clusters or node pools to change these settings. Platform admins should apply these recommendations to new clusters and node pools.

### Use least-privilege IAM node service accounts

**Recommended** : use a custom IAM service account for your GKE clusters and node pools instead of using the default Compute Engine service account.

GKE uses IAM service accounts that are attached to your nodes to run system tasks like logging and monitoring. At a minimum, these _node service accounts_ must have the [Kubernetes Engine Default Node Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.defaultNodeServiceAccount) (`roles/container.defaultNodeServiceAccount`) role on your project. By default, GKE uses the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account), which is automatically created in your project, as the node service account. 

If you use the Compute Engine default service account for other functions in your project or organization, the service account might have more permissions than GKE needs, which could expose you to security risks. 

**Best practice:** Instead of using the Compute Engine default service account, create a _custom service account_ for your nodes to use and give it only the permissions that GKE needs to run system tasks. For more information, see [Configure a custom node service account](https://docs.cloud.google.com/kubernetes-engine/security/configure-node-service-accounts#configure-custom-account). 

The service account that's attached to your nodes should be used only by system workloads that perform tasks like logging and monitoring. For your own workloads, provision identities using [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity). 

To enforce this recommendation in your organization, use the `constraints/container.managed.disallowDefaultComputeServiceAccount` [managed Organization Policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#managed-constraints). To review this managed constraint in the Google Cloud console, go to the **Policy details** page. 

[Go to Policy details](https://console.cloud.google.com/projectselector2/iam-admin/orgpolicies/container-managed.disallowDefaultComputeServiceAccount?supportedpurview=project,folder,organizationId)

### Use a Container-Optimized OS node image

**Recommended** : unless you have a specific requirement to use Ubuntu or Windows, use the Container-Optimized OS node image for your nodes.

Container-Optimized OS is built, optimized, and hardened specifically for running containers. Container-Optimized OS is the only supported node image for Autopilot mode, and is the default node image for Standard mode.

For more information, see the following documents:

  * [Container-Optimized OS security overview](https://docs.cloud.google.com/container-optimized-os/docs/concepts/security)
  * [Containerd node images](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/using-containerd)
  * [Specify a node image](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-images)



## Node security configuration

The following sections provide security recommendations for GKE node configuration. Platform admins and security engineers should apply these recommendations to improve the integrity of your GKE nodes.

Best practices

Use Shielded GKE Nodes

Disable the insecure kubelet read-only port

### Use Shielded GKE Nodes

**Recommended** : enable Shielded GKE Nodes, secure boot, and integrity monitoring in all clusters and node pools.

Shielded GKE Nodes provides verifiable identity and integrity checks that improve the security of your nodes. Shielded GKE Nodes and features like node integrity monitoring and secure boot are always enabled in Autopilot clusters. In Standard clusters, do the following:

  * Don't disable Shielded GKE Nodes in your clusters.
  * Enable secure boot in all of your node pools.
  * Don't disable integrity monitoring in your node pools.



For more information about how to enable these features, see [Using Shielded GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-nodes).

**Note:** In Container-Optimized OS, secure boot doesn't change whether you can load unsigned modules. If you want to change that setting for Container-Optimized OS nodes, [Configure secure kernel module loading](https://docs.cloud.google.com/kubernetes-engine/security/secure-modules-cos). To enforce this recommendation in your organization, use the `constraints/container.managed.enableShieldedNodes` [managed Organization Policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#managed-constraints). To review this managed constraint in the Google Cloud console, go to the **Policy details** page. 

[Go to Policy details](https://console.cloud.google.com/projectselector2/iam-admin/orgpolicies/container-managed.enableShieldedNodes?supportedpurview=project,folder,organizationId)

### Disable the insecure kubelet read-only port

**Recommended** : disable the `kubelet` read-only port and switch any workloads that use port `10255` to use the more secure port `10250` instead.

The `kubelet` process running on nodes serves a read-only API using the insecure port `10255`. Kubernetes doesn't perform any authentication or authorization checks on this port. The `kubelet` serves the same endpoints on the more secure, authenticated port `10250`.

For more information, see [Disable the `kubelet` read-only port in GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/disable-kubelet-readonly-port).

To enforce this recommendation in your organization, use the `constraints/container.managed.disableInsecureKubeletReadOnlyPort` [managed Organization Policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#managed-constraints). To review this managed constraint in the Google Cloud console, go to the **Policy details** page. 

[Go to Policy details](https://console.cloud.google.com/projectselector2/iam-admin/orgpolicies/container-managed.disableInsecureKubeletReadOnlyPort?supportedpurview=project,folder,organizationId)

### Disable node self-registration

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Recommended** : use a trusted control plane component to create `Node` objects instead of the `kubelet`.

By default, the `kubelet` process in a new GKE node registers the node with the control plane after the control plane returns an approved CertificateSigningRequest. This self-registration workflow creates a security risk where a compromised `kubelet` could register new nodes with malicious taints or labels, such as in [CVE-2025-5187](https://nvd.nist.gov/vuln/detail/CVE-2025-5187).

If you use Shielded GKE Nodes, which is enabled by default in all GKE clusters, you can prevent the `kubelet` from registering nodes. Instead, a trusted control plane component creates new `Node` objects in the Kubernetes API after the control plane returns an approved CertificateSigningRequest. GKE rejects any attempt by the `kubelet` to create `Node` objects.

For more information, see [control plane node creation](https://docs.cloud.google.com/kubernetes-engine/security/control-plane-node-creation).

## Access control

The following sections provide recommendations for restricting unauthorized access in your cluster. Security engineers and identity and account admins should apply these recommendations to reduce your attack surface and to limit the impact of unauthorized access.

Best practices

Restrict access to cluster API discovery

Place teams and environments in separate namespaces or clusters

Use the principle of least privilege in access policies

Use Workload Identity Federation for GKE to access Google Cloud APIs

Use groups to manage access

Restrict anonymous access to cluster endpoints

### Restrict access to cluster API discovery

**Recommended** : restrict access to your control plane and nodes from the internet to prevent unintended access to cluster API discovery endpoints.

By default, Kubernetes creates clusters with a permissive set of [default API discovery roles](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/rbac#default-roles-groups). These default roles give broad access to information about a cluster's APIs to various default groups, such as `system:authenticated`. These default roles don't represent a meaningful level of security for GKE clusters. For example, the `system:authenticated` group, which can read information about APIs like CustomResources, is assigned to any authenticated user (including anyone with a Google account).

To restrict access to your cluster discovery APIs, do the following:

  * **Restrict access to the control plane** : use only the DNS-based endpoint for control plane access. If you use IP-based endpoints, restrict access to a set of known address ranges by configuring authorized networks.
  * **Configure private nodes** : disable the external IP addresses of your nodes, so that clients outside of your network can't access the nodes.



For more information, see [About network isolation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation).

If you don't enable these network isolation features, treat all API discovery information (especially the schema of CustomResources, APIService definitions, and discovery information hosted by extension API servers) as publicly disclosed.

### Place teams and environments in separate namespaces or clusters

Give teams least-privilege access to Kubernetes by creating separate [namespaces](https://kubernetes.io/docs/tasks/administer-cluster/namespaces/) or clusters for each team and environment. For each namespace or cluster, assign cost centers and labels for [accountability and chargeback](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering).

You can use IAM and RBAC permissions together with namespaces to restrict user interactions with cluster resources on Google Cloud console. For more information, see [ Enable access and view cluster resources by namespace](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/restrict-resources-access-by-namespace). 

### Use the principle of least privilege in access policies

**Recommended** : give developers only the access that they need to deploy and manage applications in their namespace, especially in production environments. When you design your access control policies, map out the tasks that your users need to do in the cluster and give them only the permissions that allow them to do those tasks.

In GKE, you can use IAM and Kubernetes role-based access control (RBAC) to give permissions on resources. These access control mechanisms work together. To reduce the complexity of managing access, do the following:

  * To give access to your project or to Google Cloud resources, use [IAM roles](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/iam#roles).

  * To give access to Kubernetes resources in your cluster, such as namespaces, use [RBAC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control).




For more information about planning and designing IAM and RBAC policies, see the following documents:

  * [Use IAM securely](https://docs.cloud.google.com/iam/docs/using-iam-securely)
  * [Best practices for GKE RBAC](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/rbac)



### Use Workload Identity Federation for GKE to access Google Cloud APIs

**Recommended** : to access Google Cloud resources from your GKE workloads, use [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity).

Workload Identity Federation for GKE is the recommended way to authenticate to Google Cloud APIs. You can grant IAM roles on various resources to principals in your cluster, such as specific Kubernetes ServiceAccounts or Pods. Workload Identity Federation for GKE also protects sensitive metadata on your nodes and provides a more secure authentication workflow than alternatives like static token files.

Workload Identity Federation for GKE is always enabled in Autopilot clusters. In Standard clusters, enable Workload Identity Federation for GKE for all clusters and node pools. Additionally, follow these recommendations:

  * If you use Google Cloud client libraries in your application code, then don't distribute Google Cloud credentials to your workloads. Code that uses client libraries automatically retrieves credentials for Workload Identity Federation for GKE.
  * Use a separate namespace and ServiceAccount for every workload that needs a distinct identity. Grant IAM permissions to specific ServiceAccounts.



For more information, see [Authenticate to Google Cloud APIs from GKE workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity).

To enforce this recommendation in your organization, use the `constraints/container.managed.enableWorkloadIdentityFederation` [managed Organization Policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#managed-constraints). To review this managed constraint in the Google Cloud console, go to the **Policy details** page. 

[Go to Policy details](https://console.cloud.google.com/projectselector2/iam-admin/orgpolicies/container-managed.enableWorkloadIdentityFederation?supportedpurview=project,folder,organizationId)

### Use groups to manage access

**Recommended** : in your access policies, give permissions to groups of users instead of to individuals.

When you manage users in groups, your identity management system and identity administrators can centrally control identities by modifying user membership in various groups. This type of management negates the need to update your RBAC or IAM policies every time that a specific user needs updated permissions.

You can specify Google Groups in your IAM or RBAC policies. For more information, see the following documents:

  * [Configure Google Groups for RBAC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/google-groups-rbac)
  * [IAM principals](https://docs.cloud.google.com/iam/docs/principals-overview#google-group)

To enforce this recommendation in your organization, use the `constraints/container.managed.enableGoogleGroupsRBAC` [managed Organization Policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#managed-constraints). To review this managed constraint in the Google Cloud console, go to the **Policy details** page. 

[Go to Policy details](https://console.cloud.google.com/projectselector2/iam-admin/orgpolicies/container-managed.enableGoogleGroupsRBAC?supportedpurview=project,folder,organizationId)

### Restrict anonymous access to cluster endpoints

**Recommended** : prevent anonymous requests to all cluster endpoints except for health check endpoints, in all Autopilot and Standard clusters.

By default, Kubernetes assigns the `system:anonymous` user and the `system:unauthenticated` group to [anonymous requests](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#anonymous-requests) to cluster endpoints. If your RBAC policies give this user or group additional permissions, an anonymous user might be able to compromise the security of a service or the cluster itself.

In GKE version 1.32.2-gke.1234000 and later, you can limit the set of endpoints that anonymous requests can reach to only the `/healthz`, `/livez`, and `/readyz` Kubernetes API server health check endpoints. Anonymous access to these health check endpoints is required to verify that a cluster is operating correctly.

To limit anonymous access to cluster endpoints, specify `LIMITED` for the `--anonymous-authentication-config` flag when you use the gcloud CLI or the GKE API to create or update Standard and Autopilot clusters. GKE rejects anonymous requests to cluster endpoints that aren't the health check endpoints during authentication. Anonymous requests don't reach the endpoints, even if your RBAC policies grant access to anonymous users and groups. Rejected requests return an HTTP status of `401`.

In GKE version 1.35.0-gke.1171000 and later, anonymous access to non-health-check endpoints is denied by default only on newly created clusters.

To enforce this recommendation in your organization, folder, or project by using an organization policy, create a custom constraint with the `resource.anonymousAuthenticationConfig.mode` condition. For more information and for an example constraint, see [Restrict actions on GKE resources using custom organization policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/custom-org-policies#example_constraints).

Don't rely on this capability alone to secure your cluster. Implement additional security measures like the following:

  * [Network isolation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation)
  * [Avoid default roles and groups](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/rbac#default-roles-groups)



## GKE network security

The following sections provide recommendations to improve network security in your clusters. Network administrators and security engineers should apply these recommendations to protect workloads and infrastructure from unintended external or internal access.

Best practices

Restrict access to the control plane

Isolate your nodes from the internet

Restrict network traffic among Pods

### Restrict access to the control plane

**Recommended** : enable the DNS-based endpoint for control plane access and disable all IP-based control plane endpoints.

By default, external entities, such as clients on the internet, can reach your control plane. You can restrict who can access your control plane by configuring [network isolation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation).

To isolate your control plane, do one of the following:

  * **Use only the DNS-based endpoint (recommended)** : enable the DNS-based endpoint for the control plane and disable internal and external IP-based endpoints. All control plane access must use the DNS-based endpoint. You can use [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) to control who can access the DNS-based endpoint.

To enforce this recommendation in your organization, use the `constraints/container.managed.enableControlPlaneDNSOnlyAccess` [managed Organization Policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#managed-constraints). To review this managed constraint in the Google Cloud console, go to the **Policy details** page. 

[Go to Policy details](https://console.cloud.google.com/projectselector2/iam-admin/orgpolicies/container-managed.enableControlPlaneDNSOnlyAccess?supportedpurview=project,folder,organizationId)

  * **Disable the external IP-based endpoint** : remove the external IP address of the control plane. Clients that are outside your VPC network can't use the external IP address to access the control plane.

This option works well if you use technologies like [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview) and [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) to connect your company network to your VPC network.

  * **Use authorized networks with the external IP-based endpoint** : restrict access to the external IP-based endpoint to only a trusted range of source IP addresses.

This option works well if you don't have existing VPN infrastructure, or if you have remote users or branch offices that access your clusters by using the public internet.




In most scenarios, use only the DNS-based endpoint for control plane access. If you have to enable the IP-based endpoint, use [authorized networks](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#how_authorized_networks_work) to limit control plane access to the following entities:

  * The IP address ranges that you specify.
  * GKE nodes in the same VPC network as the cluster.
  * Google-reserved IP addresses for cluster management purposes.



### Isolate your nodes from the internet

By default, all GKE nodes have an external IP address that clients on the internet can reach. To remove this external IP address, [enable private nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#enable-private-nodes).

To enforce this recommendation in your organization, use the `constraints/container.managed.enablePrivateNodes` [managed Organization Policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#managed-constraints). To review this managed constraint in the Google Cloud console, go to the **Policy details** page. 

[Go to Policy details](https://console.cloud.google.com/projectselector2/iam-admin/orgpolicies/container-managed.enablePrivateNodes?supportedpurview=project,folder,organizationId)

### Restrict network traffic among Pods

**Recommended** : control Pod-to-Pod network traffic by using NetworkPolicies, a service mesh, or both.

By default, every Pod in your cluster can communicate with every other Pod. Restricting network access among services makes it much more difficult for attackers to move laterally in your cluster. Your services also gain some protection against accidental or deliberate denial-of-service incidents. Depending on your requirements, use one or both of the following methods to restrict Pod-to-Pod traffic:

  * [Use Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/onboarding/provision-control-plane) if you want features like load balancing, service authorization, throttling, quota, and metrics. A service mesh is useful if you have large numbers of distinct services that have complex interactions with each other.
  * [Use Kubernetes NetworkPolicies](https://kubernetes.io/docs/tasks/administer-cluster/declare-network-policy/) if you want a basic traffic flow control mechanism. To verify that your NetworkPolicies work as expected, configure [network policy logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy-logging).

To enforce this recommendation in your organization, use the `constraints/container.managed.enableNetworkPolicy` [managed Organization Policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#managed-constraints). To review this managed constraint in the Google Cloud console, go to the **Policy details** page. 

[Go to Policy details](https://console.cloud.google.com/projectselector2/iam-admin/orgpolicies/container-managed.enableNetworkPolicy?supportedpurview=project,folder,organizationId)




## Sensitive data protection

The following sections provide recommendations for encrypting data and protecting sensitive information like credentials. Security engineers and platform admins should apply these recommendations to reduce the risk of unintended access to critical data.

Best practices

Encrypt workload data in use

Store secrets outside of your cluster

### Encrypt workload data in use

Use hardware-based memory encryption to protect data that's in use by your workloads by using Confidential GKE Nodes. You can choose a Confidential Computing technology based on your requirements. For more information, see [Encrypt workload data in-use with Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes).

### Store secrets outside of your cluster

**Recommended** : use an external secret manager like Secret Manager to store sensitive data, such as API keys, outside of your cluster.

In Kubernetes, you can store sensitive data in Secrets in your cluster. You can use Secrets to provide confidential data to applications without including that data in the application code. However, storing this data in your cluster has risks like the following:

  * Anyone who can create Pods in a namespace can read the data of any Secret in that namespace.
  * Anyone with RBAC or IAM access to read all Kubernetes API objects can read Secrets.



Because of these risks, create Secrets in your cluster only when you can't provide that data to your workloads in any other way. We recommend the following methods, in order of preference, to store and access your sensitive data:

  * **Secret Manager client libraries** : programmatically access secrets from your application code by using the Secret Manager API with Workload Identity Federation for GKE. For more information, see [Access secrets stored outside GKE clusters using client libraries](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/workload-identity-secrets).
  * **Secret Manager data as mounted volumes** : provide sensitive data to your Pods as mounted volumes by using the Secret Manager add-on for GKE. This method is useful if you can't modify your application code to use the Secret Manager client libraries. For more information, see [Use Secret Manager add-on with Google Kubernetes Engine](https://docs.cloud.google.com/secret-manager/docs/secret-manager-managed-csi-component).
  * **Third-party secret management tools** : third-party tools like HashiCorp Vault provide secret management capabilities for Kubernetes workloads. These tools require more initial configuration than Secret Manager, but are a more secure option than creating Secrets in the cluster. To configure a third-party tool for secret management, see the provider's documentation. Additionally, consider the following recommendations:

    * If the third-party tool runs in a cluster, use a different cluster than the cluster that runs your workloads.
    * Use Cloud Storage or Spanner to store the tool's data.
    * Use an internal passthrough Network Load Balancer to expose the third-party secret management tool to Pods that run in your VPC network.
  * **Use Kubernetes Secrets (not recommended)** : if none of the preceding options is suitable for your use case, you can store the data as Kubernetes Secrets. Google Cloud [encrypts data at the storage layer by default](https://docs.cloud.google.com/docs/security/encryption/default-encryption). This default storage-layer encryption includes the database that stores the state of your cluster, which is based on either etcd or Spanner. Additionally, you can encrypt these Secrets at the application-layer with a key that you manage. For more information, see [Encrypt secrets at the application layer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/encrypting-secrets).




## Workload security

The following sections provide recommendations for improving the security of your cluster against workload issues. Security engineers and platform admins should apply these recommendations to improve the protection of GKE infrastructure from workloads.

Best practices

Isolate workloads by using GKE Sandbox

Restrict workload access by using RBAC

### Isolate workloads by using GKE Sandbox

**Recommended** : use [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) to prevent malicious code from affecting the host kernel on your cluster nodes.

You can run containers in a _sandboxed_ environment to mitigate against most container escape attacks, also called local privilege escalation attacks. As described in [GKE security bulletins](https://docs.cloud.google.com/kubernetes-engine/security-bulletins), this type of attack lets an attacker gain access to the host VM of the container. The attacker can use this host access to access other containers on the same VM. [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) can help to limit the impact of these attacks.

Use GKE Sandbox in scenarios like the following:

  * You have workloads that run untrusted code.
  * You want to limit the impact if an attacker compromises a container in the workload.



For more information, see [Harden workload isolation with GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods).

### Restrict workload access by using RBAC

**Recommended** : design and implement good RBAC policies to reduce the risk of unauthorized access from workloads.

Kubernetes Pods use the identity provided by a ServiceAccount to perform various actions, such as accessing resources in other namespaces or reading data in Secrets. Use RBAC to restrict the permissions of ServiceAccounts based on the requirements of the corresponding workloads. To reduce the risk of unauthorized access from workloads, implement the [RBAC best practices](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/rbac).

## Policy-based enforcement

The following sections provide recommendations for using policies to enforce security constraints across multiple resources. Identity and account admins and security engineers should apply these recommendations to maintain the compliance of clusters and workloads with organizational security requirements.

Best practices

Enforce policies across the Google Cloud resource hierarchy

Enforce policies during workload admission

### Enforce policies across the Google Cloud resource hierarchy

**Recommended** : to enforce security practices in your organization, folder, or project, use [Organization Policy Service](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/custom-org-policies).

With Organization Policy, you can centrally define constraints and enforce them at various levels of your resource hierarchy. Various Google Cloud products publish [managed constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#managed-constraints) that let you apply best practice recommendations for that product. For example, GKE publishes managed constraints for many of the best practices in this document.

For more information about how to enable Organization Policy, see [Creating and managing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).

### Enforce policies during workload admission

**Recommended** : use an admission controller like Policy Controller or the PodSecurity admission controller to review incoming API requests and enforce policies on those requests.

[Admission controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) intercept authenticated, authorized requests to the Kubernetes API to perform validation or mutation tasks before allowing a resource to persist in the API.

You can use the following methods for admission control in GKE clusters:

  * [Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview): control workload admission at scale across multiple GKE clusters.
  * [PodSecurity admission controller](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/podsecurityadmission): enforce the Kubernetes [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) by applying predefined policies to entire clusters or to specific namespaces.



## Cluster management

The following sections provide recommendations for managing your clusters over time, such as upgrading, monitoring, and configuring logs. Security engineers, platform admins, and SREs should use these recommendations to maintain the security posture of the GKE platform.

Best practices

Upgrade your GKE infrastructure regularly

Monitor your resources for security issues

Enable security bulletin notifications

Configure log collection

### Upgrade your GKE infrastructure regularly

**Recommended** : keep your GKE version up to date to access new security features and apply security patches. Use release channels, accelerated patch auto-upgrades, and automatic node upgrades.

Kubernetes and GKE frequently release new patch versions that include security improvements and vulnerability fixes. For all clusters, GKE [automatically upgrades the control plane](https://docs.cloud.google.com/kubernetes-engine/upgrades#automatic_cp_upgrades) to more stable minor versions and patch versions.

To ensure that your GKE cluster runs an up-to-date version, do the following:

  * Enroll your clusters in a [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels). Autopilot clusters are always enrolled in a release channel.
  * For clusters that are in a release channel, enable [accelerated patch auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#accelerated-patch) to get security patch versions as soon as they're available in your release channel.
  * For Standard clusters that aren't in a release channel, [enable automatic node upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades). Node auto-upgrade is enabled by default for clusters created using the Google Cloud console since June 2019, and for clusters created using the GKE API starting on November 11, 2019.
  * If you use maintenance policies, use a [maintenance window](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#maintenance_windows) to let GKE auto-upgrade your nodes at least once a month.
  * For node pools that don't use node auto-upgrades, upgrade the node pools at least once a month on your own schedule.
  * Track the [GKE security bulletins](https://docs.cloud.google.com/kubernetes-engine/docs/security-bulletins) and the [GKE release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes) for information about security patches.



### Enable security bulletin notifications

**Recommended** : configure notifications for new security bulletins that affect your cluster.

When security bulletins are available that are relevant to your cluster, GKE publishes notifications about those events as messages to Pub/Sub topics that you configure. You can receive these notifications on a Pub/Sub subscription, [integrate with third-party services](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/cluster-notifications-slack), and [receive notifications in Cloud Logging](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications#viewing-logging).

To enforce this recommendation in your organization, use the `constraints/container.managed.enableSecurityBulletinNotifications` [managed Organization Policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#managed-constraints). To review this managed constraint in the Google Cloud console, go to the **Policy details** page. 

[Go to Policy details](https://console.cloud.google.com/projectselector2/iam-admin/orgpolicies/container-managed.enableSecurityBulletinNotifications?supportedpurview=project,folder,organizationId)

### Configure log collection

**Recommended** : to reduce operational overhead and to maintain a consolidated view of your logs, implement a consistent logging strategy across your clusters. Don't disable log collection in your Standard clusters.

GKE clusters send specific [logs to Google Cloud Observability](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/observability#default). You can optionally configure the collection of additional types of logs. In addition to system and workload logs, all GKE clusters send the following audit logs to Logging:

  * **Kubernetes audit logs** : a chronological record of calls that have been made to the Kubernetes API server. Kubernetes audit log entries are useful for investigating suspicious API requests, for collecting statistics, or for creating monitoring alerts for unwanted API calls.
  * **GKE audit logs** : a record of administrative and access activities for the GKE API.



For more information, see the following documents:

  * [About GKE logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs)
  * [Google Kubernetes Engine audit logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging-container)
  * [Kubernetes audit logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging)

To enforce this recommendation in your organization, use the `constraints/container.managed.enableCloudLogging` [managed Organization Policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#managed-constraints). To review this managed constraint in the Google Cloud console, go to the **Policy details** page. 

[Go to Policy details](https://console.cloud.google.com/projectselector2/iam-admin/orgpolicies/container-managed.enableCloudLogging?supportedpurview=project,folder,organizationId)

### Monitor your resources for security issues

Use the [GKE security posture dashboard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard) and [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview) to monitor your clusters and workloads for potential issues. You can use these services to check for active vulnerabilities, threats, and security bulletins that affect your GKE infrastructure.

## Default security configurations

The following sections describe options that are configured by default in new clusters to mitigate specific security concerns, like vulnerabilities or risks. Security engineers and platform admins should validate that existing clusters use these settings.

Best practices

Leave legacy client authentication methods disabled

Leave ABAC disabled

Leave the DenyServiceExternalIPs admission controller enabled

### Leave legacy client authentication methods disabled

**Recommended** : disable legacy API server authentication methods like static certificates and passwords.

There are several [methods of authenticating](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication) to the Kubernetes API server. In GKE, the supported methods are service account bearer tokens, OAuth tokens, and X.509 client certificates. The gcloud CLI uses OAuth tokens to authenticate users for GKE.

Legacy authentication methods like static passwords are disabled, because these methods increase the attack surface for cluster compromises. In Autopilot clusters, you can't enable or use these authentication methods.

Use one of the following methods to authenticate to the Kubernetes API server:

  * **Users** : use the gcloud CLI to let GKE authenticate users, generate OAuth access tokens for the cluster, and keep the tokens up-to-date.
  * **Applications** : use Workload Identity Federation to let applications in Google Cloud or in other environments authenticate to your cluster.



For more information about how to authenticate and how to disable legacy authentication methods, see [Authenticate to the Kubernetes API server](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication).

To enforce this recommendation in your organization, use the `constraints/container.managed.disableLegacyClientCertificateIssuance` [managed Organization Policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#managed-constraints). To review this managed constraint in the Google Cloud console, go to the **Policy details** page. 

[Go to Policy details](https://console.cloud.google.com/projectselector2/iam-admin/orgpolicies/container-managed.disableLegacyClientCertificateIssuance?supportedpurview=project,folder,organizationId)

### Leave ABAC disabled

**Recommended** : use IAM and RBAC to control access in GKE. Don't enable attribute-based access control (ABAC).

ABAC is a legacy authorization method that's disabled by default in all GKE clusters, and can't be enabled in Autopilot clusters.

To enforce this recommendation in your organization, use the `constraints/container.managed.disableABAC` [managed Organization Policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#managed-constraints). To review this managed constraint in the Google Cloud console, go to the **Policy details** page. 

[Go to Policy details](https://console.cloud.google.com/projectselector2/iam-admin/orgpolicies/container-managed.disableABAC?supportedpurview=project,folder,organizationId)

### Leave the DenyServiceExternalIPs admission controller enabled

**Recommended** : don't disable the [DenyServiceExternalIPs admission controller](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#denyserviceexternalips).

This admission controller blocks Services from using ExternalIPs and mitigates [GCP-2020-015](https://docs.cloud.google.com/kubernetes-engine/security-bulletins#gcp-2020-015). This admission controller is enabled by default in clusters that were created on GKE version 1.21 and later. For cluster that were originally created on an earlier GKE version, enable the admission controller:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=LOCATION \
        --no-enable-service-externalips
    

To enforce this recommendation in your organization, use the `constraints/container.managed.denyServiceExternalIPs` [managed Organization Policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#managed-constraints). To review this managed constraint in the Google Cloud console, go to the **Policy details** page. 

[Go to Policy details](https://console.cloud.google.com/projectselector2/iam-admin/orgpolicies/container-managed.denyServiceExternalIPs?supportedpurview=project,folder,organizationId)

## What's next

  * Read the [GKE security overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview).
  * Review the [GKE shared responsibility model](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/shared-responsibility).
  * Learn more about [access control](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/access-control) in GKE.
  * Read the [GKE network overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview).
  * Read the [GKE multi-tenancy overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multitenancy-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
