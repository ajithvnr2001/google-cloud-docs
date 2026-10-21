---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-security/
title: GKE Autopilot security measures \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:43:07.792437+00:00
---

# GKE Autopilot security measures  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  GKE Autopilot security measures Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

This page describes the security features, configurations, and settings in Google Kubernetes Engine (GKE) Autopilot mode. This information is for Security specialists who want to understand the security constraints that Google applies in Autopilot mode, and the security features that are available for use in Autopilot. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before reading this page, familiarize yourself with the following:

  * [General overview of GKE security](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)
  * [General overview of Autopilot mode and Standard mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)



## Terminology

In GKE, you can use Autopilot by creating an Autopilot cluster or by running a workload in an Autopilot _ComputeClass_ in any Standard cluster. This page describes security measures for Autopilot in both of these situations by using the following terminology:

Autopilot cluster
    The entire cluster uses Autopilot mode.
Autopilot workloads in Standard clusters
    The cluster uses Standard mode, and you run specific workloads in Autopilot by using ComputeClasses.

## Security measures in Autopilot

**Best practice** : Use Autopilot clusters for comprehensive enforcement of the Autopilot security measures.

GKE applies various security best practices and settings by default in Autopilot mode, including many of the recommendations in the security overview and in [Harden your cluster security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster).

In Autopilot clusters, GKE strictly enforces all of the measures on this page by default. This default configuration makes Autopilot clusters the recommended way to use GKE. For Autopilot workloads in Standard clusters, GKE enforces the security measures in the following sections on a **best-effort basis**.

### Enforcement of Kubernetes Pod Security Standards

The Kubernetes project has a set of security guidelines named the _Pod Security Standards_ that define the following policies:

  * **Privileged** : No access restrictions. Not used in Autopilot.
  * **Baseline** : Prevents known privilege escalation pathways. Allows most workloads to run without significant changes.
  * **Restricted** : Highest level of security. Requires significant changes to most workloads.



In Autopilot mode, GKE enforces Pod security constraints by using Kubernetes admission controllers. The default Autopilot Pod admission policy includes all of the recommendations in the Baseline level of the Pod Security Standards, with some modifications for usability. Additionally, the default admission policy includes many constraints from the Restricted level of the Pod Security Standards, but avoids restrictions that would block a majority of your workloads from running.

To apply additional restrictions to comply with the full Restricted policy, you can optionally use the [PodSecurity admission controller](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/podsecurityadmission) in specific namespaces.

The following table describes how the controls in the default Autopilot admission policy compare to the controls in the Baseline and the Restricted levels of the Pod Security Standards. For more information about each control in this table, see the corresponding entry in [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/).

When evaluating compliance, we considered how the constraints apply to your own workloads. This excludes verified Google Cloud partner workloads and system workloads that require specific privileges to function.

Control | Baseline policy compliance | Restricted policy compliance | Additional information  
---|---|---|---  
HostProcess |  |  | Autopilot blocks HostProcess.  
Host namespaces |  |  | Autopilot blocks host namespaces. Some containers from [verified partners](https://docs.cloud.google.com/kubernetes-engine/docs/resources/autopilot-partners#allowlisted-partner-workloads) are allowed to use host namespaces.  
Privileged containers |  |  | Autopilot blocks privileged containers by default. Autopilot allows privileged containers from verified partners for purposes such as running security and monitoring tooling.  
Linux capabilities |  |  | Autopilot workloads can only access the capabilities specified in the Baseline Pod Security Standard by default. You can manually enable the following capabilities:

  * `NET_RAW` for ping and `SYS_PTRACE` for debugging: Add to Pod SecurityContext
  * `NET_ADMIN` for service meshes such as Istio: Specify `--workload-policies=allow-net-admin` in your cluster creation command.

Autopilot also allows some verified partner workloads to set dropped capabilities.  
HostPath volumes | Partially complies | Partially complies | Autopilot allows containers to request read-only access to `/var/log` for debugging, but denies all other read or write access.  
HostPorts |  |  | Setting specific host ports is disallowed, which mitigates some [scheduling issues](https://kubernetes.io/docs/concepts/configuration/overview/#services), and prevents accidental or deliberate direct network exposure of services. You can manually set up [random host port assignment](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-hostport) from a known range to support direct-connection networking applications such as game servers.  
AppArmor |  |  | The AppArmor docker-default security profile is [automatically applied to Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs/how-to/secure-apparmor).  
SELinux |  |  | SELinux isn't applied because AppArmor is already applied. SELinux is also not mandatory in the Pod Security Standards.  
`/proc` mount type |  |  | In GKE version 1.33 and later, if the Pod securityContext sets `procMount` to `Unmasked`, Autopilot rejects the Pod. In versions earlier than 1.33, Autopilot automatically overwrites the value in the `procMount` field to `Default`.  
seccomp profile |  |  | Autopilot applies the `RuntimeDefault` seccomp profile to all workloads. You can manually override this setting for specific workloads by setting the profile to `Unconfined` in the Pod specification.  
sysctls |  |  | GKE does not set the --allowed-unsafe-sysctls kubelet flag so pods with unsafe sysctls fail to schedule. For additional protection, as of 11 July 2023, new 1.27+ clusters also have a policy rule to enforce the securityContext settings and reject Pods that use unsafe sysctls.  
Volume types |  |  | Autopilot allows only the volume types in the Restricted policy with the following additions: HostPath volumes with read-only access to `/var/log` for debugging, gcePersistentDisk for Compute Engine persistent disks, and nfs for network file system volumes.  
Privilege escalation |  |  | This setting only provides protection to containers that aren't running as root. Industry surveys show that 76% of containers run as root, so Autopilot allows running as root to enable most workloads. This setting is also useful in _de-privileging_ workloads to non-root by allowing use of file system capabilities to work around [deficiencies with Kubernetes root capability handling](https://github.com/kubernetes/kubernetes/issues/56374).  
Run as non-root |  |  | [Industry surveys](https://sysdig.com/2022-cloud-native-security-and-usage-report/) show that 76% of containers run as root, so Autopilot allows running as root to enable most workloads.  
Run as non-root user |  |  | Containers can set `runAsUser` to `0`. [Industry surveys](https://sysdig.com/2022-cloud-native-security-and-usage-report/) show that 76% of containers run as root, so Autopilot allows running as root to enable most workloads  
  
### Built-in security configurations

In addition to the Pod Security Standards, Google applies many security settings in Autopilot based on industry best practices and our expertise. These built-in security configurations are strictly applied in Autopilot clusters.

In Standard clusters, GKE automatically applies many of these configurations on a _best-effort basis_ to Autopilot workloads in the cluster. You can optionally apply all of these configurations in your Standard cluster by [enabling every Autopilot policy for that cluster](https://docs.cloud.google.com/kubernetes-engine/security/autopilot-cluster-policies-standard), which forces all of the workloads in the Standard cluster to use Autopilot mode.

The following table describes some of the security configurations that Autopilot applies for you:

Configuration | Description  
---|---  
Host options | 

  * No `hostNetwork`, because GKE manages your nodes.
  * [Random `hostPort` assignment](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-hostport).
  * No [`hostPath`](https://kubernetes.io/docs/concepts/storage/volumes/#hostpath) volumes in **write** mode. You can use hostPath volumes in read mode for `/var/log/` path prefixes.
  * No [host namespaces](https://kubernetes.io/docs/concepts/security/pod-security-standards/).

  
Linux capabilities | You can use the following [Linux capabilities](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-capabilities-for-a-container):
    
    
    "SETPCAP", "MKNOD", "AUDIT_WRITE", "CHOWN", "DAC_OVERRIDE", "FOWNER", "FSETID", "KILL", "SETGID", "SETUID", "NET_BIND_SERVICE", "SYS_CHROOT", "SETFCAP", "SYS_PTRACE"

You can also manually enable the following capabilities:

  * `NET_RAW` for ping: Add to Pod `SecurityContext`.
  * `SYS_PTRACE` for debugging: Add to Pod `SecurityContext`.
  * `NET_ADMIN` for service meshes such as Istio: Use [`--workload-policies=allow-net-admin`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies) when you create a cluster or update an existing cluster. After that, add the capability to the Pod `SecurityContext`. This capability grants broad access to network operations such as write access to routing tables and firewalls. An attacker could potentially use this access to perform privilege escalation attacks in your cluster. For details, see [the CAP_NET_ADMIN manpage](https://man7.org/linux/man-pages/man7/capabilities.7.html).

  
Privileged containers | Containers can't run in [Privileged mode](https://kubernetes.io/docs/concepts/workloads/pods/#privileged-mode-for-containers) unless the container is deployed by a [Google Cloud partner](https://docs.cloud.google.com/kubernetes-engine/docs/resources/autopilot-partners#allowlisted-partner-workloads). Privileged containers can make changes to the underlying node, such as changing the kubelet. This access could increase the impact of a Pod compromise.  
GKE-managed namespaces | As a security measure, Autopilot doesn't allow deploying workloads in GKE-managed namespaces, such as `kube-system`.  
Container isolation | Autopilot enforces the following restrictions on containers to limit the impact of container escape vulnerabilities. **Linux capabilities and kernel security**

  * Autopilot applies the `RuntimeDefault` [seccomp profile](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/seccomp-in-gke#denied-defaults) to all Pods in the cluster unless the Pods use [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods). GKE Sandbox enforces host isolation and ignores seccomp rules specified in the Pod manifest. The sandbox is considered the security boundary for GKE Sandbox Pods.
  * Autopilot drops the `CAP_NET_RAW` Linux capability for all containers. This permission is not often used, and has been the subject of multiple escape vulnerabilities. The `ping` command might fail inside your containers because this capability is dropped. You can manually re-enable this capability by setting it in your Pod SecurityContext.
  * Autopilot drops the `CAP_NET_ADMIN` Linux capability for all containers. To re-enable this capability, specify the [`--workload-policies=allow-net-admin`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies) flag in your cluster creation or update command. `NET_ADMIN` is required by some workloads such as Istio.
  * Autopilot clusters enable [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity), which prevents Pod access to sensitive metadata on the node.
  * Autopilot blocks Kubernetes Services that set the [`spec.externalIPs`](https://kubernetes.io/docs/concepts/services-networking/service/#external-ips) field to protect against [CVE-2020-8554](https://docs.cloud.google.com/kubernetes-engine/docs/security-bulletins#GCP-2020-015).
  * Autopilot allows only the following [types of volumes](https://kubernetes.io/docs/concepts/storage/volumes/#volume-types):
        
        "configMap", "csi", "downwardAPI", "emptyDir", "gcePersistentDisk", "nfs", "persistentVolumeClaim", "projected", "secret"

Other types of volumes are blocked because they require node privileges. HostPath volumes are blocked by default, but containers can request read-only access to `/var/log` paths for debugging.

  
Pod-level security policy enforcement | Autopilot supports enforcement mechanisms for Pod-level security policies such as the [`PodSecurity` admission controller](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/podsecurityadmission), [Gatekeeper](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies-with-gatekeeper), or [Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller). However, you might not need to use any of these if the built-in security configurations described on this page already meet your requirements.  
SSH to nodes | Autopilot blocks SSH access to nodes. GKE handles all operational aspects of the nodes, including node health and all Kubernetes components running on the nodes. You can still connect remotely to your running containers using the Kubernetes `exec` functionality to execute commands in your containers for debugging, including connecting to an interactive shell, for example with `kubectl exec -it deploy/YOUR_DEPLOYMENT -- sh`.  
User impersonation | Autopilot supports [user impersonation](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#user-impersonation) for all user-defined users and groups. In Autopilot clusters only, system users and groups (like the `kube-apiserver` user and the `system:masters` group) can't be impersonated. Because user impersonation restrictions happen in the control plane, this constraint isn't enforced in Standard clusters, even when workloads use an Autopilot ComputeClass. We strongly discourage the impersonation of system users and groups in GKE.  
Mutating dynamic admission webhooks | In Autopilot clusters only, GKE modifies mutating webhooks to exclude resources in managed namespaces, such as `kube-system`, from being intercepted. Because admission control happens in the cluster control plane, this constraint isn't enforced in Standard clusters, even when workloads use an Autopilot ComputeClass. Autopilot also rejects webhooks that specify one or more of the following resources, and any sub-resources of those resources.
    
    
    - group: ""
      resource: nodes
    - group: ""
      resource: persistentVolumes
    - group: certificates.k8s.io
      resource: certificatesigningrequests
    - group: authentication.k8s.io
      resource: tokenreviews

You can't use the asterisk (`*`) wildcard for resources or groups to bypass this restriction.  
ValidatingAdmissionPolicies | In Autopilot clusters only, GKE modifies `ValidatingAdmissionPolicy` objects to exclude resources in managed namespaces, such as `kube-system`, from being intercepted. Because admission control happens in the cluster control plane, this constraint isn't enforced in Standard clusters, even when workloads use an Autopilot ComputeClass. Autopilot also rejects `ValidatingAdmissionPolicy` objects that specify one or more of the following resources, and any sub-resources of those resources.
    
    
    - group: ""
      resource: nodes
    - group: ""
      resource: persistentVolumes
    - group: certificates.k8s.io
      resource: certificatesigningrequests
    - group: authentication.k8s.io
      resource: tokenreviews

You can't use the asterisk (`*`) wildcard for resources or groups to bypass this restriction.  
MutatingAdmissionPolicies | In Autopilot clusters only, GKE modifies `MutatingAdmissionPolicy` objects to exclude resources in managed namespaces, such as `kube-system`, from being intercepted. Because admission control happens in the cluster control plane, this constraint isn't enforced in Standard clusters, even when workloads use an Autopilot ComputeClass. Autopilot also rejects `MutatingAdmissionPolicy` objects that specify one or more of the following resources, and any sub-resources of those resources.
    
    
    - group: ""
      resource: nodes
    - group: ""
      resource: persistentVolumes
    - group: certificates.k8s.io
      resource: certificatesigningrequests
    - group: authentication.k8s.io
      resource: tokenreviews

You can't use the asterisk (`*`) wildcard for resources or groups to bypass this restriction.  
Certificate signing requests | You can create CertificateSigningRequests in Autopilot to create certificates that are signed by the cluster certificate authority. To prevent interference with system components, Autopilot clusters reject CertificateSigningRequests for known privileged identities, such as system groups, system agents, or Google-managed IAM service agents. This constraint doesn't apply in Standard clusters, which let you create CertificateSigningRequests for known privileged identities.  
GKE security features | Autopilot clusters enable recommended GKE security features for you. For a list of enabled and optional security features, refer to [security features in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/resources/autopilot-standard-feature-comparison#security).  
Node operating system | Autopilot uses Container-Optimized OS with `containerd` as the node operating system. Container-Optimized OS is created and managed by Google.  
GKE version upgrades | Autopilot clusters are enrolled in a GKE release channel upon creation, and automatic upgrades are always enabled. Google automatically upgrades your control plane and nodes to the latest qualified version in the release channel over time.  
  
## Security boundaries in Autopilot

Autopilot provides access to the Kubernetes API but removes permissions to use some highly privileged Kubernetes features, such as privileged Pods. The goal is to limit the ability to access, modify, or directly control the node virtual machine (VM). Autopilot implements these restrictions to limit workloads from having low-level access to the node VM, so that Google Cloud can offer full management of nodes, and a Pod-level [SLA](https://cloud.google.com/kubernetes-engine/sla).

**Important:** The security boundary for GKE nodes is the single-tenant VM. The ability to access the node VM from Pods is not considered a security boundary for Autopilot. Any node-level access is inconsistent with the security goals of GKE Autopilot and is not supported. Google might remove any node-level access without notice.

Our intent is to prevent unintended access to the node VM. We accept submissions to that effect through the [Google Vulnerability Reward Program (VRP)](https://www.google.com/about/appsecurity/reward-program/) and will reward reports at the discretion of the Google VRP reward panel.

By design, privileged users such as cluster administrators have full control of any GKE cluster. As a security best practice, we recommend that you avoid granting powerful GKE or Kubernetes privileges widely and instead use namespace administrator delegation wherever possible as described in our [multi-tenancy guidance](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/enterprise-multitenancy).

Autopilot provisions single-tenant VMs in your project for your exclusive use. On each individual VM, your Autopilot workloads might run together, sharing a security-hardened kernel. Since the shared kernel represents a single security boundary, we recommend that if you require strong isolation, such as high-risk or untrusted workloads, run your workloads on [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) Pods to provide multi-layer security protection.

## Security recommendations based on use case

The following sections provide you with links and recommendations to plan, implement, and manage the security of your Autopilot clusters depending on your use case.

### Plan cluster security

Use case | Resources  
---|---  
Understand how GKE as a platform approaches security | 

  * For a high-level overview of cluster security, read the [GKE security overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview).
  * To understand how we secure the Kubernetes control plane, read [Control plane security](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/control-plane-security).
  * To understand the GKE in-cluster trust model, read [Cluster trust](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-trust).

  
Understand your role in hardening your environment | Learn about the [shared responsibility model](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/shared-responsibility).  
View Google's recommendations for hardening measures and incident response | 

  * For hardening best practices, read the [GKE hardening guide](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster).
  * For guidance on responding to security incidents, read [Mitigating security incidents](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/security-mitigations).

  
Understand how GKE implements audit logging | 

  * Read the [GKE audit policy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy).
  * Learn about the [audit logs that GKE creates](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging).

  
  
### Authenticate and authorize

After setting up your Autopilot clusters, you might need to authenticate your users and applications to use resources such as the Kubernetes API or Google Cloud APIs.

Use case | Resources  
---|---  
Authenticate users or applications to the cluster API server | 

  * To authenticate users, read [Authenticating users](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication#authenticating_users).
  * To authenticate applications, read [Authenticating applications](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication#authenticating_applications), which provides steps for authenticating from apps in the same cluster, in other Google Cloud environments, or in external environments.

  
Authenticate applications to Google Cloud APIs and services | Autopilot clusters let you use Workload Identity Federation for GKE to securely authenticate your workloads to Google Cloud APIs by configuring Kubernetes service accounts to act as IAM service accounts. For instructions, refer to [Configure applications to use Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#authenticating_to).  
Authorize actions at the project level | To authorize actions across clusters at the project level, use IAM. You can grant or deny access to specific GKE and Kubernetes API resources using IAM roles and permissions. For instructions, refer to [Create IAM policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/iam).  
Authorize actions at the cluster level | To authorize actions on Kubernetes API resources in specific clusters, use the built-in Kubernetes role-based access control (RBAC) mechanism. For instructions, refer to [Authorize actions in clusters using RBAC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control).  
Authorize actions at the organization level | You can use Google Cloud Organization Policy Service to enforce constraints on specific operations on GKE resources across your Google Cloud organization. For instructions, refer to [Restrict actions on GKE resources using custom organization policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/custom-org-policies).  
  
### Harden clusters and workloads

If you have specialized isolation or hardening requirements beyond the pre-configured Autopilot measures, consider the following resources:

Use case | Resources  
---|---  
Restrict public access to your cluster endpoint | Configure the network isolation of your Autopilot clusters and disable the external endpoint of the cluster control plane. For instructions, refer to [Configure the control plane access](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#configure-control-plane-access).  
Restrict cluster access to specific networks | Use [control plane authorized networks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks) to specify IP address ranges that can access your cluster.  
Store sensitive information outside your cluster | Storing sensitive data in an external, encrypted storage provider with versioning enabled is a common compliance requirement and a best practice. Use Secret Manager to store your data and access it from your Autopilot clusters using Workload Identity Federation for GKE. For instructions, refer to [Access secrets stored outside GKE clusters using Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/workload-identity-secrets).  
Verify container images before deployment to your cluster | Use Binary Authorization to check the integrity of the container images referenced in your Pod manifests at deploy time. For instructions, refer to [Verify container images at deploy time using Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/configure-policy-gke).  
  
### Monitor your security posture

After setting up your clusters and deploying your workloads, you should set up and configure monitoring and logging so that you have observability over your cluster security posture. We recommend that you do all of the following:

  * Enroll your clusters in the [GKE security posture dashboard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard) to audit workloads for concerns such as problematic security configurations or vulnerabilities in your container operating system packages and get actionable mitigation information.
  * Get notified about new security bulletins and upgrade events using [cluster notifications](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-notifications).
  * Observe your clusters using the [GKE dashboard](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/observing) in Cloud Monitoring or the [Observability tab](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics) in GKE.
  * Learn how to [view](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/using-logs) and [manage](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/managing-logs) your GKE audit logs in Cloud Logging.



## What's next

  * Read the [GKE security overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview).
  * Read the [GKE hardening guide](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster).
  * Subscribe to [security bulletins](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins) and [release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
