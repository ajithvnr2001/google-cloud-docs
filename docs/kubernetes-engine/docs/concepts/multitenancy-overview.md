---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multitenancy-overview/
title: Cluster multi-tenancy \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:32.159040+00:00
---

# Cluster multi-tenancy  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multitenancy-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Cluster multi-tenancy Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains cluster multi-tenancy on Google Kubernetes Engine (GKE). This includes clusters shared by different users at a single organization, and clusters that are shared by per-customer instances of a software as a service (SaaS) application. Cluster multi-tenancy is an alternative to managing many single-tenant clusters.

This page also summarizes the Kubernetes and GKE features that can be used to manage multi-tenant clusters.

## What is multi-tenancy?

A multi-tenant cluster is shared by multiple users and/or workloads which are referred to as "tenants". The operators of multi-tenant clusters must isolate tenants from each other to minimize the damage that a compromised or malicious tenant can do to the cluster and other tenants. Also, cluster resources must be fairly allocated among tenants.

When you plan a multi-tenant architecture you should consider the layers of resource isolation in Kubernetes: cluster, namespace, node, Pod, and container. You should also consider the security implications of sharing different types of resources among tenants. For example, scheduling Pods from different tenants on the same node could reduce the number of machines needed in the cluster. On the other hand, you might need to prevent certain workloads from being colocated. For example, you might not allow untrusted code from outside of your organization to run on the same node as containers that process sensitive information.

Although Kubernetes cannot guarantee perfectly secure isolation between tenants, it does offer features that may be sufficient for specific use cases. You can separate each tenant and their Kubernetes resources into their own [namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/). You can then use [policies](https://kubernetes.io/docs/concepts/policy/) to enforce tenant isolation. Policies are usually scoped by namespace and can be used to restrict API access, to constrain resource usage, and to restrict what containers are allowed to do.

The tenants of a multi-tenant cluster share:

  * [Extensions](https://kubernetes.io/docs/concepts/extend-kubernetes/extend-cluster/), [controllers](https://kubernetes.io/docs/reference/glossary/?fundamental=true#term-controller), add-ons, and [custom resource definitions](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) (CRDs).
  * The cluster [control plane](https://kubernetes.io/docs/concepts/architecture/control-plane-node-communication/). This implies that the cluster operations, security, and auditing are centralized.



Operating a multi-tenant cluster has several advantages over operating multiple, single-tenant clusters:

  * Reduced management overhead
  * Reduced resource fragmentation
  * No need to wait for cluster creation for new tenants



## Multi-tenancy use cases

This section describes how you could configure a cluster for various multi-tenancy use cases.

### Enterprise multi-tenancy

In an enterprise environment, the tenants of a cluster are distinct teams within the organization. Typically, each tenant has a corresponding namespace. Alternative models of multi-tenancy with a tenant per cluster, or a tenant per Google Cloud project, are harder to manage. Network traffic within a namespace is unrestricted. Network traffic between namespaces must be explicitly allowed. These policies can be enforced using Kubernetes network policy.

The users of the cluster are divided into three different roles, depending on their privilege:

Cluster administrator
    This role is for administrators of the entire cluster, who manage all tenants. Cluster administrators can create, read, update, and delete any policy object. They can create namespaces and assign them to namespace administrators.
Namespace administrator
    This role is for administrators of specific, single tenants. A namespace administrator can manage the users in their namespace.
Developer
    Members of this role can create, read, update, and delete namespaced non-policy objects like [Pods](https://kubernetes.io/docs/concepts/workloads/pods), [Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/), and [Ingresses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress). Developers only have these privileges in the namespaces they have access to.

![](https://docs.cloud.google.com/static/kubernetes-engine/images/enterprise-multitenancy.svg)

For information on setting up multiple multi-tenant clusters for an enterprise organization, see [Best practices for enterprise multi- tenancy](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/enterprise-multitenancy).

### SaaS provider multi-tenancy

The tenants of a SaaS provider's cluster are the per-customer instances of the application, and the SaaS's control plane. To take advantage of namespace-scoped policies, the application instances should be organized into their own namespaces, as should components of the SaaS's control plane. End users can't interact with the Kubernetes control plane directly, they use the SaaS's interface instead, which in turn interacts with the Kubernetes control plane.

For example, a blogging platform could run on a multi-tenant cluster. In this case, the tenants are each customer's blog instance and the platform's own control plane. The platform's control plane and each hosted blog would all run in separate namespaces. Customers would create and delete blogs, update the blogging software versions through the platform's interface with no visibility into how the cluster operates.

![](https://docs.cloud.google.com/static/kubernetes-engine/images/saas-multitenancy.svg)

## Multi-tenancy policy enforcement

GKE and Kubernetes provide several features that can be used to manage multi-tenant clusters. The following sections give an overview of these features.

### Access control

GKE has two access control systems: Identity and Access Management (IAM) and role-based access control (RBAC). IAM is Google Cloud's access control system for managing authentication and authorization for Google Cloud resources. You use IAM to grant users access to GKE and Kubernetes resources. RBAC is built into Kubernetes and grants granular permissions for specific resources and operations within your clusters.

Refer to the [Access control overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/access-control) for more information about these options and when to use each.

Refer to the [RBAC how-to guide](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control) and the [IAM how-to guide](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/iam) to learn how to use these access control systems.

You can use IAM and RBAC permissions together with namespaces to restrict user interactions with cluster resources on Google Cloud console. For more information, see [ Enable access and view cluster resources by namespace](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/restrict-resources-access-by-namespace). 

### Network policies

Cluster [network policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/) give you control over the communication between your cluster's Pods. Policies specify which namespaces, labels, and IP address ranges a Pod can communicate with.

See the [network policy how-to](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy) for instructions on enabling network policy enforcement on GKE.

Follow the [network policy tutorial](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/network-policy) to learn how to write network policies.

### Resource quotas

Resource quotas manage the amount of resources used by the objects in a namespace. You can set quotas in terms of CPU and memory usage, or in terms of object counts. Resource quotas let you ensure that no tenant uses more than its assigned share of cluster resources.

Refer to the [resource quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas) documentation for more information.

### Policy-based Pod admission control

To prevent Pods that violate your security boundaries from running in your cluster, use an admission controller. Admission controllers can check Pod specifications against policies that you define, and can prevent Pods that violate those policies from running in your cluster.

GKE supports the following types of admission control:

  * [Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-policy-controller): Declare pre-defined or custom policies and enforce them in clusters at scale using fleets. Policy Controller is an implementation of the open source [Gatekeeper open policy agent](https://github.com/open-policy-agent/gatekeeper) and is a feature of GKE Enterprise.
  * [PodSecurity admission controller](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/podsecurityadmission): Enforce pre-defined policies that correspond to the [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) in individual clusters or in specific namespaces.



### Pod anti-affinity

**Warning:** Pod anti-affinity rules can be circumvented by malicious tenants. The example below should only be used with clusters with trusted tenants, or with tenants who don't have direct access to the Kubernetes control plane.

You can use [Pod anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity) to prevent Pods from different tenants from being scheduled on the same node. Anti-affinity constraints are based on Pod [labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/). For example, the Pod specification below describes a Pod with the label `"team": "billing"`, and an anti-affinity rule that prevents the Pod from being scheduled alongside Pods without the label.
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: bar
      labels:
        team: "billing"
    spec:
      affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - topologyKey: "kubernetes.io/hostname"
            labelSelector:
              matchExpressions:
              - key: "team"
                operator: NotIn
                values: ["billing"]
    

The drawback to this technique is that malicious users could circumvent the rule by applying the `team: billing` label to an arbitrary Pod. Pod anti-affinity alone cannot securely enforce policy on clusters with untrusted tenants.

Refer to the [Pod anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity) documentation for more information.

### Dedicated nodes with taints and tolerations

**Warning:** Policies enforced by node taints and tolerations can be circumvented by malicious tenants. The example below should only be used with clusters with trusted tenants, or with tenants who don't have direct access to the Kubernetes control plane.

Node taints are another way to control workload scheduling. You can use node taints to reserve specialized nodes for use by certain tenants. For example, you can dedicate [GPU equipped nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus) to the specific tenants whose workloads require GPUs. For Autopilot clusters, node tolerations are supported only for [workload separation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-separation). Node taints are automatically added by node auto-provisioning as needed.

To dedicate a [node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools) to a certain tenant, apply a taint with `effect: "NoSchedule"` to the node pool. Then only Pods with a corresponding toleration can be scheduled to nodes in the node pool.

The drawback to this technique is that malicious users could add a toleration to their Pods to get access to the dedicated node pool. Node taints and tolerations alone cannot securely enforce policy on clusters with untrusted tenants.

For more information, see [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) in the Kubernetes documentation.

### GKE Sandbox

[GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) provides an extra layer of security for multi-tenant clusters by isolating untrusted workloads from the host kernel on your cluster nodes. GKE Sandbox uses [gVisor](https://gvisor.dev/docs/), an open source container sandboxing technology, to provide a separate user-space kernel for each Pod.

GKE Sandbox is especially useful for SaaS providers or organizations that run untrusted code, because it helps prevent a malicious tenant from escaping its container or affecting the host kernel. For more information, see [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods).

### Multi-tenant memory management

The Linux kernel ensures that memory pages allocated to new processes are zero-filled (sanitized) at the time of allocation. That process also applies to container creation, and prevents a new container from reading residual data left in memory by a previous container. However, this is a logical boundary managed by the host operating system. Attackers who break out of a container, or users with root privileges on the node VM, can bypass these protections to access the raw memory contents of other containers.

To harden this boundary, use GKE Sandbox to protect against container breakouts, use an admission policy to restrict Pods from accessing the host, and limit direct access to nodes.

Standard GPU and TPU resources _do not_ automatically sanitize their High Bandwidth Memory (HBM), Static Ram (SRAM), or Control Registers between Pod assignments. Residual data from a previous workload might persist in the accelerator's memories. If the VM is not rebooted between workloads the configuration is suitable only for trusted multi-tenancy, where all workloads scheduled on the same accelerator share the same security sensitivity.

For workloads without mutual trust, a VM reboot is required to clear accelerator memory between each scheduled workload. Deleting the VM will also cause memory to be cleared before the accelerator is re-attached to a new VM. For more information about accelerator configuration and sharing, see the GKE [TPU](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus) and [GPU](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/timesharing-gpus) documentation.

### Sharing accelerators such as GPUs and TPUs

Sharing GPU or TPU accelerators between Pods carries additional risk. GPUs and TPUs might or might not provide protections against shared access. These protections can depend on hardware version, driver version, and runtime system configuration. The following table highlights different approaches and the risk associated with each.

Pods that trust each other can decide to accept a broad spectrum of risk. The table indicates the risk level for each level of isolation.

Architecture | Primary Attack Surface | Security Summary  
---|---|---  
Pods on the same node directly share an accelerator, including GPU time-sharing and NVIDIA MPS. | GPU Memory & Global State | Pods are vulnerable to each other, and must trust each other.  
Pods on the same node directly share an accelerator and use GKE Sandbox, including GPU time-sharing and NVIDIA MPS. | GPU Memory & Host Driver | GKE Sandbox isolates the workload kernel from the host kernel. Although gVisor reduces the GPU attack surface exposed to the application, it does not provide separation inside the GPU environment, which remains shared. For more information see: [GPU Support - Security](https://gvisor.dev/docs/user_guide/gpu/#security).  
Pods on the same node have dedicated accelerators, including NVIDIA MIGs. | Host Kernel (via Driver) | Pods might still be compromised by accelerator or driver vulnerabilities that enable escalation to the host kernel.  
Pods on the same node have dedicated accelerators, including NVIDIA MIGs, and use GKE Sandbox. | Host Driver Interface (nvproxy) | GKE Sandbox isolates the kernel, but the host GPU driver interface (`nvproxy`) remains a shared attack surface. A driver exploit might allow host kernel escape. Side-channel leaks between MIG instances are also possible.  
Each Pod runs on a dedicated node, which has dedicated accelerators. | VM Boundary / Hypervisor | Recommended for untrusted workloads. Any compromise is contained to one VM.  
  
## What's next

  * Learn more about [best practices for enterprise multi-tenancy](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/enterprise-multitenancy).
  * Learn more about [fleet management](https://docs.cloud.google.com/kubernetes-engine/docs/fleets-overview).
  * Learn how to [enable access and view cluster resources by namespace](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/restrict-resources-access-by-namespace).
  * Learn how to [control communication between Pods and Services using network policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy).
  * Learn how to [set up multi-tenant logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-tenant-logging).
  * Learn how to [configure GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
