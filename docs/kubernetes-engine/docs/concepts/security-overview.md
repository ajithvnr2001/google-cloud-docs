---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview/
title: GKE security overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:41.469109+00:00
---

# GKE security overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  GKE security overview Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Google Kubernetes Engine (GKE) provides many ways to help secure your [workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-workloads-overview). Protecting workloads in GKE involves many layers of the stack, including the contents of your container image, the container runtime, the cluster network, and access to the cluster API server.

It's best to take a layered approach to protecting your clusters and workloads. You can apply the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege) to the level of access provided to your users and your application. In each layer, your organization might need to make different tradeoffs to allow the right level of flexibility and security to securely deploy and maintain your workloads. For example, some security settings might be too constraining for certain types of applications or use cases to function without significant refactoring.

This document provides an overview of each layer of your infrastructure, and shows how you can configure its security features to best suit your needs.

This document is for Security specialists who define, govern and implement policies and procedures to protect an organization's data from unauthorized access. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

**Note:** GKE Autopilot clusters implement many security configurations for you. For details, refer to [Autopilot security capabilities](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-security).

## Authentication and authorization

Kubernetes supports [two types of authentication](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#users-in-kubernetes):

  1. **User accounts** are accounts that are known to Kubernetes, but are not managed by Kubernetes - for example, you cannot create or delete them using `kubectl`.
  2. **Service accounts** are accounts that are created and managed by Kubernetes, but can only be used by Kubernetes-created entities, [such as pods](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/).



In a GKE [cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture), Kubernetes user accounts are managed by Google Cloud, and may be one of the following two types:

  1. [Google Account](https://support.google.com/accounts/answer/27441)
  2. [Google Cloud service account](https://docs.cloud.google.com/compute/docs/access/service-accounts)



Once authenticated, you need to authorize these identities to create, read, update or delete Kubernetes resources.

Despite the similar names, Kubernetes service accounts and Google Cloud service accounts are different entities. Kubernetes service accounts are part of the cluster in which they are defined and are typically used within that cluster. By contrast, Google Cloud service accounts are part of a Google Cloud project, and can easily be granted permissions both within clusters and to Google Cloud project clusters themselves, as well as to any Google Cloud resource using [Identity and Access Management (IAM)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/iam-integration#managing_iam_roles). This makes Google Cloud service accounts more powerful than Kubernetes service accounts; in order to follow the security principle of least privilege, you should consider using Google Cloud service accounts only when their capabilities are required.

To configure more granular access to Kubernetes resources at the cluster level or within Kubernetes namespaces, you use [Role-Based Access Control (RBAC)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control). RBAC allows you to create detailed policies that define which operations and resources you allow users and service accounts to access. With RBAC, you can control access for Google Accounts, Google Cloud service accounts, and Kubernetes service accounts. To further simplify and streamline your authentication and authorization strategy for GKE, you should ensure that the [legacy Attribute Based Access Control](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters#legacyabac) is disabled so that Kubernetes RBAC and IAM are the sources of truth.

For more information:

  * Read the [GKE RBAC documentation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control).
  * Learn about supported authentication methods when connecting to the Kubernetes API server in [Authenticating to the Kubernetes API server](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication).



## Control plane security

In GKE, the [Kubernetes control plane components](https://kubernetes.io/docs/concepts/overview/components/#control-plane-components) are managed and maintained by Google. The control plane components host the software that runs the Kubernetes control plane, including the API server, scheduler, controller manager, and the etcd API. If the cluster runs etcd database instances on the control plane VMs, these instances are also managed and maintained by Google.

You can access the control plane using a DNS-based endpoint (recommended), IP-based endpoints, or both. If you use IP-based endpoints, you can protect the Kubernetes API server by using [authorized networks](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#how_authorized_networks_work) and not enabling the external endpoint of the control plane. This lets you assign an internal IP address to the control plane and disable access on the external IP address. If you use a DNS-based endpoint, you can use IAM and [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) to secure your control plane access with both identity and network-aware policies.

You can handle cluster authentication in Google Kubernetes Engine by using IAM as the identity provider. For information on authentication, see [Authenticating to the Kubernetes API server](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication).

Another way to help secure your control plane is to make sure that you are doing [credential rotation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/credential-rotation) on a regular basis. When credential rotation is initiated, the SSL certificates and cluster certificate authority are rotated. This process is automated by GKE and also helps ensure that your control plane IP address rotates.

For more information:

  * Read more about [control plane security](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/control-plane-security).
  * Read the [Role-Based Access Control documentation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control).
  * Follow the [Credential Rotation guide](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/credential-rotation).



## Node security

GKE deploys your workloads on Compute Engine instances running in your Google Cloud project. These instances are attached to your GKE cluster as [nodes](https://kubernetes.io/docs/concepts/architecture/nodes/). The following sections show you how to leverage the node-level security features available to you in Google Cloud.

### Container-Optimized OS

By default, GKE [nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#nodes) use Google's [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits) as the operating system on which to run Kubernetes and its components. Container-Optimized OS implements several [advanced features](https://docs.cloud.google.com/container-optimized-os/docs/concepts/security) for enhancing the security of GKE clusters, including:

  * Locked-down firewall
  * Read-only filesystem where possible
  * Limited user accounts and disabled root login



GKE Autopilot nodes always use Container-Optimized OS as the operating system.

**Warning:** Loading kernel modules that aren't shipped with Container-Optimized OS is unsupported. Doing so can lead to security vulnerabilities and reliability issues.

### Node upgrades

A best practice is to patch your OS on a regular basis. From time to time, security issues in the container runtime, Kubernetes itself, or the node operating system might require you to upgrade your nodes more urgently. When you upgrade your node, the node's software is upgraded to their latest versions.

GKE clusters support [automatic upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-upgrades). In Autopilot clusters, automatic upgrades are always enabled. You can also [manually upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) the nodes in a Standard cluster.

### Protect nodes from untrusted workloads

For clusters that run unknown or untrusted workloads, a good practice is to protect the operating system on the node from the untrusted workload running in a Pod.

For example, [multi-tenant clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multitenancy-overview) such as software-as-a-service (SaaS) providers often execute unknown code submitted by their users. Security research is another application where workloads may need stronger isolation than nodes provide by default.

You can enable [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods) on your cluster to isolate untrusted workloads in sandboxes on the node. GKE Sandbox is built using [gVisor](https://gvisor.dev/), an open source project.

### Secure instance metadata

GKE uses [_instance metadata_](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata) from the underlying Compute Engine instances to provide nodes with credentials and configurations that are used to bootstrap nodes and to connect to the control plane. This metadata contains sensitive information that Pods on the node don't need access to, such as the node's service account key.

You can lock down sensitive instance metadata paths by using [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity). Workload Identity Federation for GKE enables the [GKE metadata server](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity#metadata_server) in your cluster, which filters requests to sensitive fields such as `kube-env`.

Workload Identity Federation for GKE is always enabled in Autopilot clusters. In Standard clusters, Pods have access to instance metadata unless you manually enable Workload Identity Federation for GKE.

## Network security

Most workloads running in GKE need to communicate with other services that could be running either inside or outside of the cluster. You can use several different methods to control what traffic is allowed to flow through your clusters and their Pods.

### Limit Pod-to-Pod communication

By default, all Pods in a cluster can be reached over the network via their Pod IP address. Similarly, by default, egress traffic allows outbound connections to any address accessible in the VPC into which the cluster was deployed.

Cluster administrators and users can lock down the ingress and egress connections created to and from the Pods in a namespace by using [network policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/). By default, when there are no network policies defined, all ingress and egress traffic is allowed to flow into and out of all Pods. Network policies allow you to use tags to define the traffic flowing through your Pods.

Once a network policy is applied in a namespace, all traffic is dropped to and from Pods that don't match the configured labels. As part of your creation of clusters and/or namespaces, you can apply [the default deny traffic to both ingress and egress](https://kubernetes.io/docs/concepts/services-networking/network-policies/#default-deny-all-ingress-and-all-egress-traffic) of every Pod to ensure that all new workloads added to the cluster must explicitly authorize the traffic they require.

For more information:

  * Read more about [network policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy)
  * Follow the [network policy tutorial](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/network-policy)
  * Read more about [default policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/#default-policies)



### Filter load balanced traffic

To load balance your Kubernetes Pods with a [network load balancer](https://docs.cloud.google.com/compute/docs/load-balancing/network), you need to create a Service of type `LoadBalancer` that matches your Pod's labels. With the Service created, you will have an external-facing IP that maps to ports on your Kubernetes Pods. Filtering authorized traffic is achieved at the node level by [kube-proxy](https://kubernetes.io/docs/reference/generated/kube-proxy/), which filters based on IP address.

To configure this filtering, you can use the `loadBalancerSourceRanges` configuration of the Service object. With this configuration parameter, you can provide a list of CIDR ranges that you would like to allow for access to the Service. If you do not configure `loadBalancerSourceRanges`, all addresses are allowed to access the Service via its external IP.

For cases in which external access to the Service is not required, consider using an [internal load balancer](https://docs.cloud.google.com/compute/docs/load-balancing/internal). The internal load balancer also respects the `loadBalancerSourceRanges` when it is necessary to filter out traffic from inside of the VPC.

For more information, follow the [internal load balancing tutorial](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing).

### Filter traffic outside of the cluster

To control the flow of network traffic between external entities and your cluster, use [Cloud Next Generation Firewall](https://docs.cloud.google.com/firewall/docs/about-firewalls). You can use firewall configurations to, for example, block outgoing traffic from your Pods to unapproved destinations.

Firewall configurations aren't enough to control which registries the container images in your cluster come from. To limit container image pulls to a set of approved registries, see [Block container images from unapproved registries](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#block-images-unapproved-registries).

## Secure your workloads

Kubernetes allows users to quickly provision, scale, and update container-based workloads. This section describes tactics that administrators and users can employ to limit the effect a running container can have on other containers in the same cluster, the nodes where containers can run, and the Google Cloud services enabled in users' projects.

### Limit privileges for containerized Pod processees

Limiting the privileges of containerized processes is important for the overall security of your cluster. GKE Autopilot clusters always restrict specific privileges, as described in [Autopilot security capabilities](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-security#built-in-security).

GKE also allows you to set security-related options via the [Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) on both Pods and containers. These settings allow you to change security settings of your processes like:

  * User and group to run as
  * Available Linux capabilities
  * Ability to escalate privileges



To enforce these restrictions at the cluster level rather than at the Pod or container levels, use the [PodSecurityAdmission controller](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/podsecurityadmission). Cluster administrators can use PodSecurityAdmission to ensure that all Pods in a cluster or namespace adhere to a pre-defined policy in the [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/). You can also set custom Pod security policies at the cluster level by using [Gatekeeper](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies-with-gatekeeper).

**Note:** You can't use these policies to override the built-in security configurations in GKE Autopilot.

The GKE node operating systems, both Container-Optimized OS and Ubuntu, [apply the default Docker AppArmor security policies](https://docs.cloud.google.com/container-optimized-os/docs/how-to/secure-apparmor#using_the_default_docker_apparmor_security_profile) to all containers started by Kubernetes. You can view the profile's template on [GitHub](https://github.com/moby/profiles/blob/c936cc7b4074219137bc0bee45670f5e4618d462/apparmor/template.go). Among other things, the profile **denies** the following abilities to containers:

  * Write files directly in `/proc/`
  * Write to files that are not in a process ID directory (`/proc/<number>`)
  * Write to files in `/proc/sys` other than `/proc/sys/kernel/shm*`
  * Mount filesystems

**Note:** [SELinux](https://selinuxproject.org/page/Main_Page) is not supported on GKE. Use [AppArmor](https://docs.cloud.google.com/container-optimized-os/docs/how-to/secure-apparmor) instead.**Note:** The default Docker AppArmor profile is applied by the container runtime at the node level, which means the profile is applied even if `container.apparmor.security.beta.kubernetes.io/container-name` annotations are missing from a Pod. As a result, security scanners that only examine Kubernetes API resources might falsely identify Pods without this annotation as missing an AppArmor profile, even though the AppArmor profile is applied at the node level.

For more information:

  * Read the [Pod Security Context documentation](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/).
  * Learn more about existing protections in the [Container-Optimized OS AppArmor documentation](https://docs.cloud.google.com/container-optimized-os/docs/how-to/secure-apparmor).



### Give Pods access to Google Cloud resources

Your containers and Pods might need access to other resources in Google Cloud. There are three ways to do this.

#### Workload Identity Federation for GKE (recommended)

The most secure way to authorize Pods to access Google Cloud resources is with [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity). Workload Identity Federation for GKE allows a Kubernetes service account to run as an IAM service account. Pods that run as the Kubernetes service account have the permissions of the IAM service account.

Workload Identity Federation for GKE can be used with [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods).

#### Node service account

In Standard clusters, your Pods can also authenticate to Google Cloud using the credentials of the [service account](https://docs.cloud.google.com/compute/docs/access/service-accounts) used by the node's Compute Engine virtual machine (VM).

**Caution:** Any Pod running in the cluster can use the node's service account credentials from the VM metadata. If you use this method, create and configure a custom service account that has the [minimum IAM roles](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa) that are required by the Pods running in the cluster.

This approach is not compatible with [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods) because GKE Sandbox blocks access to the Compute Engine metadata server.

#### Service account JSON key (not recommended)

**Caution:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

You can grant credentials for Google Cloud resources to applications by using the [service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys). This approach is strongly discouraged because of the difficulty of securely managing account keys.

If you choose this method, use custom IAM service accounts for each application so that applications have the minimal necessary permissions. Grant each service account the minimum IAM roles that are needed for its paired application to operate successfully. Keeping the service accounts application-specific makes it easier to revoke access in the case of a compromise without affecting other applications. After you have assigned your service account the correct IAM roles, you can create a JSON service account key, and then mount the key into your Pod using a Kubernetes [Secret](https://kubernetes.io/docs/concepts/configuration/secret/).

### Use Binary Authorization

[Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview) is a service on Google Cloud that provides software supply-chain security for applications that run in the cloud. Binary Authorization works with images that you deploy to GKE from Artifact Registry or another container image registry.

With Binary Authorization enforcement, you can ensure that internal processes that safeguard the quality and integrity of your software have successfully completed before an application is deployed to your production environment. For instructions about creating a cluster with Binary Authorization enabled, visit [Creating a cluster](https://docs.cloud.google.com/binary-authorization/docs/creating-cluster) in the [Binary Authorization documentation](https://docs.cloud.google.com/binary-authorization/docs).

With [Binary Authorization continuous validation (CV)](https://docs.cloud.google.com/binary-authorization/docs/overview-cv), you can ensure that container images associated with Pods are regularly monitored to ensure that they conform to your evolving internal processes.

## Audit logging

Audit logging provides a way for administrators to retain, query, process, and alert on events that occur in your GKE environments. Administrators can use the logged information to do forensic analysis, real-time alerting, or for cataloging how a fleet of GKE clusters are being used and by whom.

By default, GKE logs Admin Activity logs. You can optionally also log Data Access events, depending on the types of operations you are interested in inspecting.

For more information:

  * Follow the [GKE audit logging tutorial](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging).
  * Read more about [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit).



## Built-in security measures

GKE enforces specific restrictions on what you can do to system objects in your clusters. When you perform an operation like creating or patching a workload, an [admission webhook](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#what-are-admission-webhooks) named _warden-validating_ validates your request against a set of restricted operations and decides whether to allow the request.

Admission errors that are caused by this policy are similar to the following:
    
    
    GKE Warden rejected the request because it violates one or more constraints.
    

### Autopilot cluster security measures

Autopilot clusters apply multiple security settings based on our expertise and industry best practices. For details, see [Security measures in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-security#security-measures).

### Standard cluster security measures

Standard clusters are more permissive by default than Autopilot clusters. GKE Standard clusters have the following security settings:

  * You can't update the ServiceAccount used by GKE-managed system workloads, such as workloads in the `kube-system` namespace.
  * You can't bind the `cluster-admin` default ClusterRole to the `system:anonymous`, `system:unauthenticated`, or `system:authenticated` groups.
  * You can manually [enable specific Autopilot security policies in your Standard cluster](https://docs.cloud.google.com/kubernetes-engine/security/autopilot-cluster-policies-standard).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
