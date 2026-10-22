---
url: https://docs.cloud.google.com/kubernetes-engine/security-bulletins/
title: Security bulletins \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:49.593534+00:00
---

# Security bulletins  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/security-bulletins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Resources ](https://docs.cloud.google.com/kubernetes-engine/resources)



Send feedback 

#  Security bulletins Stay organized with collections  Save and categorize content based on your preferences. 

This document describes security bulletins for Google Kubernetes Engine (GKE).

For dates prior to June 1, 2026, this document also describes security bulletins for Distributed Cloud (software only) for VMware and bare metal, and for GKE on AWS and GKE on Azure. To view more recent security bulletins and vulnerability fixes for these products, see the following documents:

  * [Distributed Cloud (software only) security bulletins](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/security-bulletins)
  * [GKE on AWS release notes](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/release-notes)
  * [GKE on Azure release notes](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/release-notes)

**Caution:** GKE on AWS and GKE on Azure are in maintenance mode and will be shut down on March 17, 2027.



Vulnerabilities are often kept secret under embargo until affected parties have had a chance to address them. In these cases, the release notes refer to "security updates" until the embargo is lifted. After the embargo ends, the release notes are updated to reflect the vulnerability the patch addressed.

**Note:** The vulnerabilities in these bulletins are more likely to impact multi-tenant workloads. For a technical description of security boundaries in GKE and how these impact workloads, see [Isolation at different layers of the Kubernetes stack](https://cloudplatform.googleblog.com/2018/05/Exploring-container-security-Isolation-at-different-layers-of-the-Kubernetes-stack.html).

When GKE issues a security bulletin that directly correlates to your cluster configuration or version, we might send you a [`SecurityBulletinEvent` cluster notification](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications#securitybulletin) that provides information about the vulnerability and actions that you can take, if applicable.

GKE platforms don't use components such as `ingress-nginx` and the CRI-O container runtime, and are unaffected by any vulnerabilities in those components. If you install components from other sources, refer to the security updates and patching advice of those components at the source. For example, starting in March 2026, [Ingress NGINX is retired](https://kubernetes.io/blog/2026/01/29/ingress-nginx-statement/). If you use Ingress NGINX, you should migrate to an alternative system as soon as possible.

For more information on how Google manages security vulnerabilities and patches for GKE, see [Security patching](https://docs.cloud.google.com/kubernetes-engine/docs/resources/security-patching).

[ Use this XML feed to subscribe to security bulletins for this page. rss_feed](https://cloud.google.com/feeds/gke-security-bulletins.xml)

## GCP-2026-061

**Published:** 2026-09-09  
**Reference:** [GHSA-p7v4-vr35-mj6f](https://github.com/containerd/containerd/security/advisories/GHSA-p7v4-vr35-mj6f)

Description | Severity  
---|---  
A security vulnerability [GHSA-p7v4-vr35-mj6f](https://github.com/containerd/containerd/security/advisories/GHSA-p7v4-vr35-mj6f) (CVE assignment pending) in containerd's CRI implementation allows a container restored from an untrusted checkpoint through the `CreateContainer` API to bypass the destination security context and execute with elevated privileges. When restoring a container from a checkpoint archive or annotated OCI image, CRIU restores process credentials, Linux capabilities, `no_new_privs`, and `seccomp` state directly from checkpoint data rather than enforcing the destination CRI `ContainerConfig`. An attacker who can run a container with a crafted checkpoint image can execute processes as the root user with full capabilities and no enforced `seccomp` filters despite restrictive security policies requested by the orchestrator. Additionally, containerd's CRI status reporting reflects the requested configuration rather than the actual restored process state, masking the privilege discrepancy from orchestrators. **GKE clusters are not vulnerable by default.** GKE node images do not include the `criu` tool. Implicit container restore is not supported without `criu` installed on the node. Standard container creation operations in GKE Standard and GKE Autopilot remain unaffected. GKE Autopilot clusters do not support custom runtime configuration and are not impacted. Additionally, [Pod snapshots in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/pod-snapshots) do not exercise the vulnerable implicit restore codepath. In updated containerd versions (2.3.4 and later, or 2.2.7 and later), implicit restore is disabled by default through the `enable_experimental_restore_via_create` configuration option. Version 2.4 of containerd will remove this codepath completely in favor of the explicit Pod-level restore API (KEP-5823). **Warning:** Administrators can manually re-enable the feature in containerd (2.3.4 and later, or 2.2.7 and later) by setting the `enable_experimental_restore_via_create` configuration option. However, doing so leaves this vulnerability present because containerd cannot enforce destination security policy while it restores the `criu` process.

#### What should I do?

Because GKE does not include the `criu` binary on default node images, no immediate cluster upgrades or configuration changes are required for default workloads. If you install custom runtime software or node tools on your nodes that include the `criu` binary, consider taking the following actions as appropriate for your environment:

  * **Re-create existing restored containers:** Stop, delete, and re-create any running containers that were restored from untrusted checkpoints.
  * **Disable experimental restore (containerd 2.3.4 and later, or 2.2.7 and later):** If operating nodes with containerd (2.3.4 and later, or 2.2.7 and later) and custom `criu` installations, ensure the `enable_experimental_restore_via_create` configuration option remains set to `false` in your containerd node configuration.
  * **Audit containerd logs:** If `criu` is installed, inspect node logs for implicit restore log entries containing search strings such as `"Found checkpoint of container"`, `"Prepared <id> for restore"`, or `"Restored container <id> successfully"`.
  * **Monitor deprecation warnings for containerd:** Look for the following deprecation warning event: `io.containerd.deprecation/cri-create-container-checkpoint-restore`.
  * **Restrict Pod creation permissions:** Ensure Kubernetes RBAC restricts Pod creation permissions (`create pods`) strictly to trusted users and service accounts.
  * **Enforce trusted image registries:** Ensure that the values for the Pod's `image:` field reference verified image repositories.
  * **Prepare for KEP-5823:** Update operational procedures to rely on explicit Pod-level Checkpoint or Restore APIs after they are available in future Kubernetes releases.

| Medium  
  
## GCP-2026-058

**Published:** 2026-09-02

Description | Severity  
---|---  
A missing project permission check in GKE Multi-Cloud `(CreateAttachedCluster, CreateAwsCluster, CreateAzureCluster)` APIs allowed an attacker to register an attached cluster into an arbitrary target project's Workload Identity Federation for GKE. This registration allowed unauthorized creation of Workload Identity tokens and impersonation of Kubernetes Service Accounts that have bindings in the target project through the Workload Identity Federation for GKE configuration. The attack would have required both of the following characteristics to be known:

  * Knowledge of the target project number (not project ID); and
  * Knowledge of at least one target namespace and Kubernetes service account pair that has been bound with `roles/iam.workloadIdentityUser`

We have verified that there was no exploitation of this vulnerability. This issue was reported through our [Vulnerability Reward Program](https://bughunters.google.com/about).

#### What should I do?

All GKE clusters were patched by adding the missing authorization check to the server. No action is required. | Critical  
  
## GCP-2026-037

**Published:** 2026-06-18

**Updated:** 2026-06-20

**Reference:** [CVE-2026-50195](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-50195), [CVE-2026-53488](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-53488), [CVE-2026-53492](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-53492), [CVE-2026-53489](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-53489), [CVE-2026-47262](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47262)

**2026-06-20 Update:** Added GKE patch versions containing the fixes for Container-Optimized OS node images for minor versions 1.35 and 1.36. Patches for Ubuntu node images are still pending and in progress.

**2026-06-19 Update:** Added GKE patch versions containing the fixes for Container-Optimized OS node images for minor versions from 1.30 to 1.34. Patches for Ubuntu node images and for minor version 1.35 and 1.36 for Container-Optimized OS node images are in progress.

Description | Severity  
---|---  
The following vulnerabilities have been discovered in containerd (the GKE container runtime). These vulnerabilities allow attackers with permissions to create Pods to bypass Kubernetes security boundaries and perform host compromise, cache poisoning, and denial of service. While these vulnerabilities are critical in the context of containerd, the requirement to have cluster privileges to create Pods to exploit them means they are considered High [according to GKE vulnerability classification](https://docs.cloud.google.com/kubernetes-engine/docs/resources/security-patching#how_vulnerabilities_are_classified).

  * **CVE-2026-50195 (Critical)** : containerd's CRI checkpoint import process fails to validate image references. An attacker with permissions to create Pods can use a crafted checkpoint image to poison the node's local image cache, causing other pods using an `IfNotPresent` pull policy to execute malicious code.
  * **CVE-2026-53488 (Critical)** : CRI plugin propagates labels from an image config to a container without validation. This may result in executing an arbitrary command on the host.
  * **CVE-2026-53492 (Critical)** : CRI implementation improperly trusts Container Device Interface (CDI) annotations during container restoration. This allows an attacker to inject arbitrary CDI configurations (such as host mounts and device nodes) into restored containers, bypassing resource allocation and device plugin enforcement.
  * **CVE-2026-53489 (High)** : CRI plugin restores container.log without validating a symlinked path, allowing an attacker to read arbitrary host files via `kubectl logs`.
  * **CVE-2026-47262 (Moderate)** : A vulnerability in containerd allows a maliciously crafted image to cause memory exhaustion (DoS) of the containerd process.

These vulnerabilities affect all GKE configurations using Container-Optimized OS and Ubuntu node images, including GKE Standard and GKE Autopilot clusters. **Note** : Because containerd resolves labels and CDI mounts on the host before invoking the gVisor sandbox runtime, GKE Sandbox (gVisor) does not protect against host compromise from these vectors.

#### What should I do?

**2026-06-20 Update:** The following GKE patch versions contain the fixes for Container-Optimized OS node images for minor versions from 1.30 to 1.36. Upgrade your Container-Optimized OS node pools to the following versions or later:

  * 1.36.0-gke.3545000 or later
  * 1.35.6-gke.1039000 or later
  * 1.34.9-gke.1021000 or later
  * 1.33.12-gke.1267000 or later
  * 1.32.13-gke.1823000 or later
  * 1.31.14-gke.2150000 or later
  * 1.30.14-gke.2726000 or later

Patches for Ubuntu node images are in progress.

* * *

Until patch versions are available, use the following mitigation guidelines:

  * Restrict Pod creation permissions (`create pods` in Kubernetes RBAC) only to trusted users, as critical vectors require pod creation or restoration capabilities.
  * Avoid using `IfNotPresent` or `Never` image pull policies for untrusted or critical workloads; use `Always` to force verification against a trusted registry.
  * Restrict or monitor use of checkpointing/restoration features in your clusters.

| High  
  
## GCP-2026-033

**Published:** 2026-05-14  
**Updated:** 2026-07-16  
**Reference:** [CVE-2026-46300](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46300)

**2026-07-16 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.30.14-gke.2710000
  * 1.31.14-gke.2116000
  * 1.32.13-gke.1829000
  * 1.33.13-gke.1011000
  * 1.34.9-gke.1131000
  * 1.35.6-gke.1127000
  * 1.36.2-gke.1346000



### GKE

**Updated:** 2026-07-16

Description | Severity  
---|---  
A container breakout vulnerability CVE-2026-46300 has been found in the Linux kernel, known as Fragnesia. It allows an unprivileged local attacker to escalate to root on the host. GKE Standard clusters with Ubuntu nodes are impacted. GKE Standard clusters with Container-Optimized OS nodes are not impacted. GKE Autopilot is not impacted. Clusters using GKE Sandbox aren't impacted.

#### What should I do?

Upstream kernel patches have only recently been released. Those patches are being built into GKE releases and this bulletin will be updated when they are available. In the interim, partial mitigations are available below. Containers do not provide a robust security boundary, as container breakout vulnerabilities pose a significant risk. For secure workload isolation, we recommend using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#gke_sandbox). If possible, migrate your workloads to run as non-root. If your container needs to be root, consider setting the `pod.spec.securityContext.seccompProfile.type` to `RuntimeDefault` for all workloads in your cluster. As an added security measure, we also recommend setting the `pod.spec.containers[*].securityContext.allowPrivilegeEscalation` to `false`.
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: default-pod
    spec:
      securityContext:
        seccompProfile:
          type: RuntimeDefault
      containers:
      - name: mycontainer
        image: ubuntu
        securityContext:
          allowPrivilegeEscalation: false

| Medium  
  
### GDC (VMware)

**Updated:** 2026-07-16

Description | Severity  
---|---  
A container breakout vulnerability CVE-2026-46300 has been found in the Linux kernel, known as Fragnesia. It allows an unprivileged local attacker to escalate to root on the host.

#### What should I do?

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Medium  
  
### GKE on AWS

**Updated:** 2026-07-16

Description | Severity  
---|---  
A container breakout vulnerability CVE-2026-46300 has been found in the Linux kernel, known as Fragnesia. It allows an unprivileged local attacker to escalate to root on the host.

#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Medium  
  
### GKE on Azure

**Updated:** 2026-07-16

Description | Severity  
---|---  
A container breakout vulnerability CVE-2026-46300 has been found in the Linux kernel, known as Fragnesia. It allows an unprivileged local attacker to escalate to root on the host.

#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Medium  
  
### GDC (bare metal)

**Updated:** 2026-07-16

Description | Severity  
---|---  
A container breakout vulnerability CVE-2026-46300 has been found in the Linux kernel, known as Fragnesia. It allows an unprivileged local attacker to escalate to root on the host.

#### What should I do?

**Note:** Patch versions and a severity assessment for GDC software for bare metal are in progress. We'll update this bulletin with that information when it's available. | Medium  
  
## GCP-2026-030

**Published:** 2026-05-11  
**Updated:** 2026-06-24  
**Reference:** [CVE-2026-43284](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-43284), [CVE-2026-43500](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-43500)

**2026-06-24 Update:** Added patch versions for GKE.

**2026-05-20 Update:** Added CVE-2026-43500 and added CVE IDs to exploit paths.

### GKE

**Updated:** 2026-06-24

Description | Severity  
---|---  
Container breakout vulnerabilities CVE-2026-43284 and CVE-2026-43500 have been found in the Linux kernel, known as DirtyFrag. They allow an unprivileged local attacker to escalate to root on the host. There are two exploit paths. rxrpc exploit path (CVE-2026-43500): Container-Optimized OS is not vulnerable because the vulnerable module is not compiled in. Ubuntu nodes are vulnerable. esp4 exploit path (CVE-2026-43284): Both Container-Optimized OS and Ubuntu are vulnerable, but the GKE default seccomp profile provides a mitigation that protects all Autopilot clusters and Standard clusters with [Autopilot-managed node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools#autopilot-node-pools). The esp4 exploit path requires the user to have the ability to make the unshare syscall to obtain CAP_NET_ADMIN. Containers that use the `RuntimeDefault` SeccompProfile can’t call unshare and are unaffected. Containers that grant CAP_NET_ADMIN explicitly are affected. Containers using GKE Sandbox are not impacted.

#### What should I do?

**2026-06-24 Update:** The following versions of GKE are updated with code to fix this vulnerability on Container-Optimized OS. Upgrade your Container-Optimized OS node pools to the following versions or later:

  * 1.30.14-gke.2558000
  * 1.31.14-gke.1967000
  * 1.32.13-gke.1829000
  * 1.33.12-gke.1059000
  * 1.34.8-gke.1218000
  * 1.35.5-gke.1057000
  * 1.36.0-gke.2459000



* * *

Upstream kernel patches have only recently been released. Those patches are being built into GKE releases and this bulletin will be updated when they are available. In the interim, partial mitigations are available below. We do not recommend relying on containers as a security boundary, container breakout vulnerabilities are very common. [Use GKE Sandbox instead](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#gke_sandbox). If possible, migrate your workloads to run as non-root. If your container needs to be root, consider setting the `pod.spec.securityContext.seccompProfile.type` to `RuntimeDefault` for all workloads in your cluster. As an added security measure we also recommend setting the `pod.spec.containers[*].securityContext.allowPrivilegeEscalation` to `false`.
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: default-pod
    spec:
      securityContext:
        seccompProfile:
          type: RuntimeDefault
      containers:
      - name: mycontainer
        image: ubuntu
        securityContext:
          allowPrivilegeEscalation: false

| Medium  
  
### GDC (VMware)

**Updated:** 2026-05-20

Description | Severity  
---|---  
Container breakout vulnerabilities CVE-2026-43284 and CVE-2026-43500 have been found in the Linux kernel, known as DirtyFrag. They allow an unprivileged local attacker to escalate to root on the host.

#### What should I do?

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

**Updated:** 2026-05-20

Description | Severity  
---|---  
Container breakout vulnerabilities CVE-2026-43284 and CVE-2026-43500 have been found in the Linux kernel, known as DirtyFrag. They allow an unprivileged local attacker to escalate to root on the host.

#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

**Updated:** 2026-05-20

Description | Severity  
---|---  
Container breakout vulnerabilities CVE-2026-43284 and CVE-2026-43500 have been found in the Linux kernel, known as DirtyFrag. They allow an unprivileged local attacker to escalate to root on the host.

#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

**Updated:** 2026-05-20

Description | Severity  
---|---  
Container breakout vulnerabilities CVE-22026-43284 and CVE-2026-43500 have been found in the Linux kernel, known as DirtyFrag. They allow an unprivileged local attacker to escalate to root on the host.

#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2026-027

**Published:** 2026-05-01  
**Reference:** [CVE-2026-23351](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-23351)

### GKE

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23351

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.35.3-gke.1389000
  * 1.34.6-gke.1154000
  * 1.33.10-gke.1115000
  * 1.32.13-gke.1258000
  * 1.31.14-gke.1723000
  * 1.30.14-gke.2320000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23351



#### What should I do?

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23351



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23351



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23351



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2026-026

**Published:** 2026-04-30  
**Updated:** 2026-05-04  
**Reference:** [CVE-2026-31431](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-31431)

**2026-05-04 Update:** Added patch versions for GKE.

### GKE

**Updated:** 2026-05-04

Description | Severity  
---|---  
A vulnerability in the Linux kernel ([CVE-2026-31431](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-31431)) allows an unprivileged local attacker to write to the system page cache, potentially leading to local privilege escalation and container escape. GKE Standard and Autopilot clusters are affected. Containers using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#gke_sandbox) are not impacted.

#### What should I do?

**2026-05-04 Update:** The following versions of GKE are updated with code to fix this vulnerability on Container-Optimized OS. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to the following versions or later:

  * 1.36.0-gke.1555000
  * 1.35.3-gke.1943000
  * 1.34.7-gke.1292000
  * 1.33.11-gke.1132000
  * 1.32.13-gke.1446000
  * 1.31.14-gke.1846000
  * 1.30.14-gke.2439000

If you don't see these versions in the Google Cloud console, then use the [`gcloud container clusters upgrade`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade) gcloud CLI command to specify the versions and upgrade your node pools in Standard clusters and your control plane in Autopilot clusters.

* * *

Upstream kernel patches have only recently been released. Those patches are being built into GKE releases and this bulletin will be updated when they are available. In the interim, mitigations are available below. We do not recommend relying on containers as a security boundary, container breakout vulnerabilities are very common. [Use GKE Sandbox instead](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#gke_sandbox). For immediate protection, [mitigation advice here](https://github.com/GoogleCloudPlatform/k8s-node-tools/tree/master/disable-algif-aead).

#### What vulnerabilities are being addressed?

The vulnerability, CVE-2026-31431, is a logic flaw in the Linux kernel's `authencesn` cryptographic template that chains `AF_ALG` and `splice()`. It allows an unprivileged local user to trigger a deterministic, controlled 4-byte write into the page cache of any readable file on the system. Because the page cache is shared across the host, an attacker can exploit this to achieve root privileges or escape container boundaries by corrupting the in-memory versions of setuid binaries or other sensitive files. | High  
  
### GDC (VMware)

Description | Severity  
---|---  
A vulnerability in the Linux kernel ([CVE-2026-31431](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-31431)) allows an unprivileged local attacker to write to the system page cache, potentially leading to local privilege escalation and container escape.

#### What should I do?

Upstream kernel patches have only recently been released. Those patches are being built into GKE releases and this bulletin will be updated when they are available. In the interim, mitigations are available below. We do not recommend relying on containers as a security boundary, container breakout vulnerabilities are very common. [Use GKE Sandbox instead](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#gke_sandbox). For immediate protection, [mitigation advice here](https://github.com/GoogleCloudPlatform/k8s-node-tools/tree/master/disable-algif-aead).

#### What vulnerabilities are being addressed?

The vulnerability, CVE-2026-31431, is a logic flaw in the Linux kernel's `authencesn` cryptographic template that chains `AF_ALG` and `splice()`. It allows an unprivileged local user to trigger a deterministic, controlled 4-byte write into the page cache of any readable file on the system. Because the page cache is shared across the host, an attacker can exploit this to achieve root privileges or escape container boundaries by corrupting the in-memory versions of sensitive files. | High  
  
### GKE on AWS

Description | Severity  
---|---  
A vulnerability in the Linux kernel ([CVE-2026-31431](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-31431)) allows an unprivileged local attacker to write to the system page cache, potentially leading to local privilege escalation and container escape.

#### What should I do?

Upstream kernel patches have only recently been released. Those patches are being built into GKE releases and this bulletin will be updated when they are available. In the interim, mitigations are available below. We do not recommend relying on containers as a security boundary, container breakout vulnerabilities are very common. [Use GKE Sandbox instead](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#gke_sandbox). For immediate protection, [mitigation advice here](https://github.com/GoogleCloudPlatform/k8s-node-tools/tree/master/disable-algif-aead).

#### What vulnerabilities are being addressed?

The vulnerability, CVE-2026-31431, is a logic flaw in the Linux kernel's `authencesn` cryptographic template that chains `AF_ALG` and `splice()`. It allows an unprivileged local user to trigger a deterministic, controlled 4-byte write into the page cache of any readable file on the system. Because the page cache is shared across the host, an attacker can exploit this to achieve root privileges or escape container boundaries by corrupting the in-memory versions of sensitive files. | High  
  
### GKE on Azure

Description | Severity  
---|---  
A vulnerability in the Linux kernel ([CVE-2026-31431](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-31431)) allows an unprivileged local attacker to write to the system page cache, potentially leading to local privilege escalation and container escape.

#### What should I do?

Upstream kernel patches have only recently been released. Those patches are being built into GKE releases and this bulletin will be updated when they are available. In the interim, mitigations are available below. We do not recommend relying on containers as a security boundary, container breakout vulnerabilities are very common. [Use GKE Sandbox instead](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#gke_sandbox). For immediate protection, [mitigation advice here](https://github.com/GoogleCloudPlatform/k8s-node-tools/tree/master/disable-algif-aead).

#### What vulnerabilities are being addressed?

The vulnerability, CVE-2026-31431, is a logic flaw in the Linux kernel's `authencesn` cryptographic template that chains `AF_ALG` and `splice()`. It allows an unprivileged local user to trigger a deterministic, controlled 4-byte write into the page cache of any readable file on the system. Because the page cache is shared across the host, an attacker can exploit this to achieve root privileges or escape container boundaries by corrupting the in-memory versions of sensitive files. | High  
  
### GDC (bare metal)

Description | Severity  
---|---  
A vulnerability in the Linux kernel ([CVE-2026-31431](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-31431)) allows an unprivileged local attacker to write to the system page cache, potentially leading to local privilege escalation and container escape.

#### What should I do?

GDC software for bare metal does not bundle an operating system in its distribution. Customers are responsible for installing and maintaining a supported Linux distribution on physical hardware. To protect your cluster, check with your OS vendor to see if your underlying Linux distribution is affected, and apply the appropriate kernel updates. As an immediate mitigation, [mitigation advice here](https://github.com/GoogleCloudPlatform/k8s-node-tools/tree/master/disable-algif-aead).

#### What vulnerabilities are being addressed?

The vulnerability, CVE-2026-31431, is a logic flaw in the Linux kernel's `authencesn` cryptographic template that chains `AF_ALG` and `splice()`. It allows an unprivileged local user to trigger a deterministic, controlled 4-byte write into the page cache of any readable file on the system. Because the page cache is shared across the host, an attacker can exploit this to achieve root privileges or escape container boundaries by corrupting the in-memory versions of sensitive files. | High  
  
## GCP-2026-025

**Published:** 2026-04-30  
**Reference:** [CVE-2026-23274](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-23274)

### GKE

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23274

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.35.3-gke.1389000
  * 1.34.6-gke.1154000
  * 1.33.10-gke.1115000
  * 1.32.13-gke.1258000
  * 1.31.14-gke.1723000
  * 1.30.14-gke.2320000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23274



#### What should I do?

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23274



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23274



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23274



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2026-024

**Published:** 2026-04-28  
**Reference:** [CVE-2025-38248](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38248)

### GKE

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2025-38248

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.35.2-gke.1485000
  * 1.34.5-gke.1153000
  * 1.33.9-gke.1117000
  * 1.32.13-gke.1090000
  * 1.31.14-gke.1526000
  * 1.30.14-gke.2192000

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Ubuntu node pools to one of the following patch versions or later:

  * 1.35.2-gke.1485000
  * 1.34.5-gke.1153000
  * 1.33.9-gke.1117000
  * 1.32.13-gke.1090000
  * 1.31.14-gke.1526000
  * 1.30.14-gke.2154000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2025-38248



#### What should I do?

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2025-38248



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2025-38248



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2025-38248



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2026-023

**Published:** 2026-04-28  
**Updated:** 2026-05-07  
**Reference:** [CVE-2026-23074](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-23074)

**2026-05-07 Update:** Added patch versions for Ubuntu node pools on GKE.

### GKE

**Updated:** 2026-05-07

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23074

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2026-05-07 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Ubuntu node pools to the following versions or later:

  * 1.30.14-gke.2320000
  * 1.31.14-gke.1723000
  * 1.32.13-gke.1258000
  * 1.33.10-gke.1115000
  * 1.34.6-gke.1154000
  * 1.35.3-gke.1234000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.35.2-gke.1485000
  * 1.34.5-gke.1076000
  * 1.33.9-gke.1060000
  * 1.32.13-gke.1059000
  * 1.31.14-gke.1476000
  * 1.30.14-gke.2117000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23074



#### What should I do?

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23074



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23074



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23074



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2026-022

**Published:** 2026-04-16  
**Reference:** [CVE-2026-23209](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-23209)

### GKE

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23209

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.35.2-gke.1485000
  * 1.34.5-gke.1153000
  * 1.33.9-gke.1060000
  * 1.32.13-gke.1059000
  * 1.31.14-gke.1599000
  * 1.30.14-gke.2215000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23209



#### What should I do?

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23209



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23209



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23209



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2026-020

**Published:** 2026-04-14  
**Reference:** [CVE-2026-23231](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-23231)

### GKE

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23231

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.35.2-gke.1485000
  * 1.34.5-gke.1153000
  * 1.33.10-gke.1067000
  * 1.32.13-gke.1205000
  * 1.31.14-gke.1681000
  * 1.30.14-gke.2286000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23231



#### What should I do?

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23231



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23231



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23231



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2026-018

**Published:** 2026-04-07  
**Updated:** 2026-04-15  
**Reference:** [CVE-2026-23111](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-23111)

**2026-04-15 Update:** Added patch versions for Ubuntu nodes with GKE.

### GKE

**Updated:** 2026-04-15

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23111

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2026-04-15 Update** : The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.35.3-gke.1234000
  * 1.34.6-gke.1154000
  * 1.33.10-gke.1115000
  * 1.32.13-gke.1258000
  * 1.31.14-gke.1723000
  * 1.30.14-gke.2320000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.35.2-gke.1485000
  * 1.34.5-gke.1153000
  * 1.33.9-gke.1060000
  * 1.32.13-gke.1059000
  * 1.31.14-gke.1599000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23111



#### What should I do?

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23111



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23111



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23111



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2026-017

**Published:** 2026-04-02  
**Reference:** [CVE-2026-23273](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-23273)

### GKE

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23273

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.35.2-gke.1485000
  * 1.34.5-gke.1153000
  * 1.33.9-gke.1060000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23273



#### What should I do?

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23273



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23273



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2026-23273



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2026-016

**Published:** 2026-03-27  
**Updated:** 2026-03-31  
**Reference:** [CVE-2025-38616](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38616)

**2026-03-31 Update:** Added patch versions for Ubuntu nodes with GKE.

### GKE

**Updated:** 2026-03-31

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38616

GKE Standard and Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2026-03-31 Update** : The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.35.2-gke.1485000
  * 1.34.5-gke.1153000
  * 1.33.9-gke.1117000
  * 1.32.13-gke.1090000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.35.2-gke.1269000
  * 1.34.4-gke.1193000
  * 1.33.8-gke.1169000
  * 1.32.12-gke.1127000
  * 1.31.14-gke.1376000
  * 1.30.14-gke.2192000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38616



#### What should I do?

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38616



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38616



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38616



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2026-014

**Published:** 2026-03-14  
**Updated:** 2026-03-25  
**Reference:** [CVE-2025-38678](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38678)

**2026-03-25 Update:** Added patch versions for Ubuntu nodes with GKE.

### GKE

**Updated:** 2026-03-25

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38678

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2026-03-25 Update** : The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.35.2-gke.1485000
  * 1.34.5-gke.1076000
  * 1.33.9-gke.1060000
  * 1.32.13-gke.1059000
  * 1.31.14-gke.1476000
  * 1.30.14-gke.2117000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.35.2-gke.1269000
  * 1.34.4-gke.1193000
  * 1.33.8-gke.1169000
  * 1.32.12-gke.1127000
  * 1.31.14-gke.1376000
  * 1.30.14-gke.2192000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38678



#### What should I do?

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38678



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38678



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38678



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2026-007

**Published:** 2026-02-09  
**Updated:** 2026-03-25  
**Reference:** [CVE-2025-40297](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-40297)

**2026-03-25 Update:** Added patch versions for Ubuntu nodes with GKE.

### GKE

**Updated:** 2026-03-25

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-40297

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2026-03-25 Update** : The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.35.2-gke.1269000
  * 1.34.4-gke.1193000
  * 1.33.8-gke.1169000
  * 1.32.13-gke.1059000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.35.0-gke.2398000
  * 1.32.11-gke.1174000
  * 1.33.5-gke.2392000
  * 1.34.3-gke.1318000
  * 1.31.14-gke.1243000
  * 1.30.14-gke.1922000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-40297



#### What should I do?

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-40297



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-40297



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-40297



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2026-006

**Published:** 2026-01-29

**Updated:** 2026-02-20

**Reference:**[CVE-2025-15467](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-15467)

**2026-02-20 Update:** Added patch versions for GKE.

### GKE

**Updated:** 2026-02-20

Description | Severity  
---|---  
Multiple security vulnerabilities have been identified in the OpenSSL library. The most significant finding is CVE-2025-15467, a critical vulnerability that might allow for remote code execution (RCE) or denial of service (DoS) attacks via network-based vectors. GKE control plane and infrastructure is not vulnerable. GKE core infrastructure, including the Kubernetes API Server and Kubelet, remains unaffected. These services use [BoringCrypto](https://github.com/boringcrypto) (a security-hardened module derived from [BoringSSL](https://boringssl.googlesource.com/boringssl/+/fed35d32245ee4563691d21f55c12b4f8dac840a/crypto/fipsmodule/FIPS.md)), which does not contain the vulnerable code found in the standard OpenSSL distribution. GKE Nodes: The [OpenSSL](https://www.openssl.org/) library included in the GKE Node OS images (Container-Optimized OS and Ubuntu) contains the vulnerable code. While the control plane is secure, software running within your nodes or administrative tools on the host OS might be at risk. Updated GKE versions will include will the latest version of OpenSSL, which addresses the following CVEs:

  * [CVE-2025-11187](https://openssl-library.org/news/vulnerabilities/#CVE-2025-11187)
  * [CVE-2025-15467](https://openssl-library.org/news/vulnerabilities/#CVE-2025-15467)
  * [CVE-2025-15468](https://openssl-library.org/news/vulnerabilities/#CVE-2025-15468)
  * [CVE-2025-15469](https://openssl-library.org/news/vulnerabilities/#CVE-2025-15469)
  * [CVE-2025-66199](https://openssl-library.org/news/vulnerabilities/#CVE-2025-66199)
  * [CVE-2025-68160](https://openssl-library.org/news/vulnerabilities/#CVE-2025-68160)
  * [CVE-2025-69418](https://openssl-library.org/news/vulnerabilities/#CVE-2025-69418)
  * [CVE-2025-69419](https://openssl-library.org/news/vulnerabilities/#CVE-2025-69419)
  * [CVE-2025-69420](https://openssl-library.org/news/vulnerabilities/#CVE-2025-69420)
  * [CVE-2025-69421](https://openssl-library.org/news/vulnerabilities/#CVE-2025-69421)
  * [CVE-2026-22795](https://openssl-library.org/news/vulnerabilities/#CVE-2026-22795)
  * [CVE-2026-22796](https://openssl-library.org/news/vulnerabilities/#CVE-2026-22796)



#### What should I do?

**2026-02-20 Update:** The following versions of GKE are updated with code to fix this vulnerability. Upgrade your GKE node pools to the following versions or later: 

  * 1.35.0-gke.2398000
  * 1.34.3-gke.1318000
  * 1.33.5-gke.2392000
  * 1.32.11-gke.1264000



* * *

There is no action at this time. This security bulletin will be updated when new GKE versions are available that use the patched version of OpenSSL. | High  
  
### GDC (VMware)

Description | Severity  
---|---  
Multiple security vulnerabilities have been identified in the OpenSSL library. The most significant finding is CVE-2025-15467, a critical vulnerability that might allow for remote code execution (RCE) or denial of service (DoS) attacks via network-based vectors. GDC software for VMware control plane and infrastructure is not vulnerable. GDC software for VMware core infrastructure, including the Kubernetes API Server and Kubelet, remains unaffected. These services use [BoringCrypto](https://github.com/boringcrypto) (a security-hardened module derived from [BoringSSL](https://boringssl.googlesource.com/boringssl/+/fed35d32245ee4563691d21f55c12b4f8dac840a/crypto/fipsmodule/FIPS.md)), which does not contain the vulnerable code found in the standard OpenSSL distribution. GDC software for VMware Nodes: The [OpenSSL](https://www.openssl.org/) library included in the GDC software for VMware Node OS images (Container-Optimized OS and Ubuntu) contains the vulnerable code. While the control plane is secure, software running within your nodes or administrative tools on the host OS might be at risk. Updated GDC software for VMware versions will include will the latest version of OpenSSL, which addresses the following CVEs:

  * [CVE-2025-11187](https://openssl-library.org/news/vulnerabilities/#CVE-2025-11187)
  * [CVE-2025-15467](https://openssl-library.org/news/vulnerabilities/#CVE-2025-15467)
  * [CVE-2025-15468](https://openssl-library.org/news/vulnerabilities/#CVE-2025-15468)
  * [CVE-2025-15469](https://openssl-library.org/news/vulnerabilities/#CVE-2025-15469)
  * [CVE-2025-66199](https://openssl-library.org/news/vulnerabilities/#CVE-2025-66199)
  * [CVE-2025-68160](https://openssl-library.org/news/vulnerabilities/#CVE-2025-68160)
  * [CVE-2025-69418](https://openssl-library.org/news/vulnerabilities/#CVE-2025-69418)
  * [CVE-2025-69419](https://openssl-library.org/news/vulnerabilities/#CVE-2025-69419)
  * [CVE-2025-69420](https://openssl-library.org/news/vulnerabilities/#CVE-2025-69420)
  * [CVE-2025-69421](https://openssl-library.org/news/vulnerabilities/#CVE-2025-69421)
  * [CVE-2026-22795](https://openssl-library.org/news/vulnerabilities/#CVE-2026-22795)
  * [CVE-2026-22796](https://openssl-library.org/news/vulnerabilities/#CVE-2026-22796)



#### What should I do?

There is no action at this time. This security bulletin will be updated when new Google Distributed Cloud versions are available that use the patched version of OpenSSL. | High  
  
### GKE on AWS

Description | Severity  
---|---  
Multiple security vulnerabilities have been identified in the OpenSSL library. The most significant finding is CVE-2025-15467, a critical vulnerability that might allow for remote code execution (RCE) or denial of service (DoS) attacks via network-based vectors. GKE on AWS control plane and infrastructure is not vulnerable. GKE on AWS core infrastructure, including the Kubernetes API Server and Kubelet, remains unaffected. These services use [BoringCrypto](https://github.com/boringcrypto) (a security-hardened module derived from [BoringSSL](https://boringssl.googlesource.com/boringssl/+/fed35d32245ee4563691d21f55c12b4f8dac840a/crypto/fipsmodule/FIPS.md)), which does not contain the vulnerable code found in the standard OpenSSL distribution. GKE on AWS Nodes: The [OpenSSL](https://www.openssl.org/) library included in the GKE on AWS Node OS images (Container-Optimized OS and Ubuntu) contains the vulnerable code. While the control plane is secure, software running within your nodes or administrative tools on the host OS might be at risk. Updated GKE on AWS versions will include will the latest version of OpenSSL, which addresses the following CVEs:

  * [CVE-2025-11187](https://openssl-library.org/news/vulnerabilities/#CVE-2025-11187)
  * [CVE-2025-15467](https://openssl-library.org/news/vulnerabilities/#CVE-2025-15467)
  * [CVE-2025-15468](https://openssl-library.org/news/vulnerabilities/#CVE-2025-15468)
  * [CVE-2025-15469](https://openssl-library.org/news/vulnerabilities/#CVE-2025-15469)
  * [CVE-2025-66199](https://openssl-library.org/news/vulnerabilities/#CVE-2025-66199)
  * [CVE-2025-68160](https://openssl-library.org/news/vulnerabilities/#CVE-2025-68160)
  * [CVE-2025-69418](https://openssl-library.org/news/vulnerabilities/#CVE-2025-69418)
  * [CVE-2025-69419](https://openssl-library.org/news/vulnerabilities/#CVE-2025-69419)
  * [CVE-2025-69420](https://openssl-library.org/news/vulnerabilities/#CVE-2025-69420)
  * [CVE-2025-69421](https://openssl-library.org/news/vulnerabilities/#CVE-2025-69421)
  * [CVE-2026-22795](https://openssl-library.org/news/vulnerabilities/#CVE-2026-22795)
  * [CVE-2026-22796](https://openssl-library.org/news/vulnerabilities/#CVE-2026-22796)



#### What should I do?

There is no action at this time. This security bulletin will be updated when new GKE on AWS versions are available that use the patched version of OpenSSL. | High  
  
### GKE on Azure

Description | Severity  
---|---  
Multiple security vulnerabilities have been identified in the OpenSSL library. The most significant finding is CVE-2025-15467, a critical vulnerability that might allow for remote code execution (RCE) or denial of service (DoS) attacks via network-based vectors. GKE on Azure control plane and infrastructure is not vulnerable. GKE on Azure core infrastructure, including the Kubernetes API Server and Kubelet, remains unaffected. These services use [BoringCrypto](https://github.com/boringcrypto) (a security-hardened module derived from [BoringSSL](https://boringssl.googlesource.com/boringssl/+/fed35d32245ee4563691d21f55c12b4f8dac840a/crypto/fipsmodule/FIPS.md)), which does not contain the vulnerable code found in the standard OpenSSL distribution. GKE on Azure Nodes: The [OpenSSL](https://www.openssl.org/) library included in the GKE on Azure Node OS images (Container-Optimized OS and Ubuntu) contains the vulnerable code. While the control plane is secure, software running within your nodes or administrative tools on the host OS might be at risk. Updated GKE on Azure versions will include will the latest version of OpenSSL, which addresses the following CVEs:

  * [CVE-2025-11187](https://openssl-library.org/news/vulnerabilities/#CVE-2025-11187)
  * [CVE-2025-15467](https://openssl-library.org/news/vulnerabilities/#CVE-2025-15467)
  * [CVE-2025-15468](https://openssl-library.org/news/vulnerabilities/#CVE-2025-15468)
  * [CVE-2025-15469](https://openssl-library.org/news/vulnerabilities/#CVE-2025-15469)
  * [CVE-2025-66199](https://openssl-library.org/news/vulnerabilities/#CVE-2025-66199)
  * [CVE-2025-68160](https://openssl-library.org/news/vulnerabilities/#CVE-2025-68160)
  * [CVE-2025-69418](https://openssl-library.org/news/vulnerabilities/#CVE-2025-69418)
  * [CVE-2025-69419](https://openssl-library.org/news/vulnerabilities/#CVE-2025-69419)
  * [CVE-2025-69420](https://openssl-library.org/news/vulnerabilities/#CVE-2025-69420)
  * [CVE-2025-69421](https://openssl-library.org/news/vulnerabilities/#CVE-2025-69421)
  * [CVE-2026-22795](https://openssl-library.org/news/vulnerabilities/#CVE-2026-22795)
  * [CVE-2026-22796](https://openssl-library.org/news/vulnerabilities/#CVE-2026-22796)



#### What should I do?

There is no action at this time. This security bulletin will be updated when new GKE on Azure versions are available that use the patched version of OpenSSL. | High  
  
### GDC (bare metal)

Description | Severity  
---|---  
Several security issues have been discovered in OpenSSL. The most critical is CVE-2025-15467, which could be used to execute a denial of service or remote code execution attack over the internet. GDC software for bare metal is not vulnerable to this threat. GDC software for bare metal uses [BoringCrypto](https://github.com/boringcrypto) for network facing services such as the Kubernetes apiserver and Kubelet, and BoringCrypto is not affected by this vulnerability. BoringCrypto is extracted from [BoringSSL](https://boringssl.googlesource.com/boringssl/+/fed35d32245ee4563691d21f55c12b4f8dac840a/crypto/fipsmodule/FIPS.md), a fork of [OpenSSL](https://www.openssl.org/) focused on security hardening and performance. GDC software for bare metal does not provide a node OS. Customers are responsible for installing and maintaining a supported Linux distribution on physical hardware before installing the GKE software.

#### What should I do?

Update your Linux OS image to one that includes the latest Open SSL distribution. | High  
  
## GCP-2026-003

**Published:** 2026-01-09  
**Updated:** 2026-03-25  
**Reference:** [CVE-2025-39964](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-39964)

**2026-03-25 Update:** Added patch versions for Ubuntu nodes with GKE.

### GKE

**Updated:** 2026-03-25

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-39964

GKE Standard and Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2026-03-25 Update** : The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.35.1-gke.1396000
  * 1.34.4-gke.1047000
  * 1.33.8-gke.1026000
  * 1.32.12-gke.1026000
  * 1.31.14-gke.1336000
  * 1.30.14-gke.1991000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.34.1-gke.3556000
  * 1.30.14-gke.1719000
  * 1.31.13-gke.1139000
  * 1.29.15-gke.2467000
  * 1.33.5-gke.1862000
  * 1.32.9-gke.1239000
  * 1.28.15-gke.3163000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-39964



#### What should I do?

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-39964



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-39964



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-39964



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2026-002

**Published:** 2026-01-07  
**Updated:** 2026-03-25  
**Reference:** [CVE-2025-40215](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-40215)

**2026-03-25 Update:** Added patch versions for Ubuntu nodes with GKE.

### GKE

**Updated:** 2026-03-25

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-40215

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2026-03-25 Update** : The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.35.2-gke.1269000
  * 1.34.4-gke.1193000
  * 1.33.8-gke.1169000
  * 1.32.13-gke.1059000
  * 1.31.14-gke.1423000
  * 1.30.14-gke.2071000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.32.9-gke.1632000
  * 1.29.15-gke.2553000
  * 1.33.5-gke.1956000
  * 1.34.1-gke.3556000
  * 1.31.14-gke.1081000
  * 1.30.14-gke.1794000
  * 1.28.15-gke.3225000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-40215



#### What should I do?

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-40215



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-40215



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-40215



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2026-001

**Published:** 2026-01-07  
**Reference:** [CVE-2025-40214](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-40214)

### GKE

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-40214

GKE Standard and Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.32.9-gke.1632000
  * 1.28.15-gke.3225000
  * 1.33.5-gke.1956000
  * 1.34.1-gke.3556000
  * 1.30.14-gke.1794000
  * 1.31.14-gke.1081000
  * 1.29.15-gke.2553000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-40214



#### What should I do?

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-40214



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-40214



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-40214



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-074

**Published:** 2025-12-05  
**Reference:** [CVE-2025-39965](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-39965)

### GKE

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-39965

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.32.9-gke.1330000
  * 1.34.1-gke.2541000
  * 1.33.5-gke.1350000
  * 1.31.13-gke.1231000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-39965



#### What should I do?

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-39965



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-39965



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-39965



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-071

**Published:** 2025-12-02  
**Updated:** 2026-03-25  
**Reference:** [CVE-2025-40019](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-40019)

**2026-03-25 Update:** Added patch versions for Ubuntu nodes with GKE.

**2025-12-11 Update:** Added patch versions and a severity rating for GDC (VMware).

### GKE

**Updated:** 2026-03-25

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-40019

GKE Standard and Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2026-03-25 Update** : The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.35.1-gke.1396000
  * 1.34.4-gke.1047000
  * 1.33.8-gke.1026000
  * 1.32.12-gke.1026000
  * 1.31.14-gke.1476000
  * 1.30.14-gke.2117000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.28.15-gke.2966000
  * 1.32.9-gke.1330000
  * 1.33.5-gke.1350000
  * 1.29.15-gke.2236000
  * 1.31.13-gke.1231000
  * 1.30.14-gke.1525000
  * 1.34.1-gke.2541000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2025-12-11

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-40019



#### What should I do?

The following versions of GDC (VMware) are updated with code to fix this vulnerability. Upgrade your GDC (VMware) clusters to the following versions or later:

  * 1.31.1100-gke.40



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | High  
  
### GKE on AWS

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-40019



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-40019



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-40019



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-070

**Published:** 2025-12-02  
**Updated:** 2026-03-25  
**Reference:** [CVE-2025-40018](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-40018)

**2026-03-25 Update:** Added patch versions for Ubuntu nodes with GKE.

**2025-12-11 Update:** Added patch versions and a severity rating for GDC (VMware).

### GKE

**Updated:** 2026-03-25 

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-40018

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2026-03-25 Update** : The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.35.1-gke.1396000
  * 1.34.4-gke.1047000
  * 1.33.8-gke.1026000
  * 1.32.12-gke.1026000
  * 1.31.14-gke.1336000
  * 1.30.14-gke.1991000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.32.9-gke.1330000
  * 1.29.15-gke.2236000
  * 1.30.14-gke.1525000
  * 1.31.13-gke.1231000
  * 1.34.1-gke.2541000
  * 1.28.15-gke.2966000
  * 1.33.5-gke.1350000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2025-12-11

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-40018



#### What should I do?

The following versions of GDC (VMware) are updated with code to fix this vulnerability. Upgrade your GDC (VMware) clusters to the following versions or later:

  * 1.31.1100-gke.40



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | High  
  
### GKE on AWS

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-40018



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-40018



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-40018



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-066

**Published:** 2025-11-10  
**Updated:** 2025-11-27  
**Reference:** [CVE-2025-31133](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-31133), [CVE-2025-52565](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-52565), [CVE-2025-52881](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-52881)

**2025-11-27 Update:** Added patch versions for GKE and GDC (bare metal).

### GKE

**Updated:** 2025-11-27

Description | Severity  
---|---  
Several security issues have been discovered in runc, an open source software component used for running containers on GKE. The vulnerabilities (CVE-2025-31133, CVE-2025-52565, and CVE-2025-52881) allow an attacker to execute a full container breakout, leading to root privilege escalation on the host node. An actor with privileges to deploy a malicious container image can exploit these vulnerabilities. These vulnerabilities affect GKE Standard clusters running either Container-Optimized OS (COS) or Ubuntu node images, as well as Autopilot clusters. Node pools using GKE Sandbox are not affected and Windows node pools are not affected.

#### What should I do?

**2025-11-27 Update:** The following versions of GKE are updated with code to fix these vulnerabilities on Container-Optimized OS. Upgrade your GKE node pools to the following versions or later: 

  * 1.34.1-gke.3355000
  * 1.33.5-gke.1791000
  * 1.32.9-gke.1548000
  * 1.31.13-gke.1454000
  * 1.30.14-gke.1719000
  * 1.29.15-gke.2467000
  * 1.28.15-gke.3163000

The following GKE versions have been updated with code to fix these vulnerabilities on Ubuntu. Upgrade your GKE node pools to the following versions or later:

  * 1.33.5-gke.1791000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions).

* * *

GKE is developing new versions that include the fixes for these vulnerabilities. This bulletin will be updated once these new versions are available. | High  
  
### GDC (VMware)

Description | Severity  
---|---  
Several security issues have been discovered in runc, an open source software component used for running containers on GKE. The vulnerabilities (CVE-2025-31133, CVE-2025-52565, and CVE-2025-52881) allow an attacker to execute a full container breakout, leading to root privilege escalation on the host node. An actor with privileges to deploy a malicious container image can exploit these vulnerabilities. **What should I do?** GKE is developing new versions that include the fixes for these vulnerabilities. This bulletin will be updated once these new versions are available. | High  
  
### GKE on AWS

Description | Severity  
---|---  
Several security issues have been discovered in runc, an open source software component used for running containers on GKE. The vulnerabilities (CVE-2025-31133, CVE-2025-52565, and CVE-2025-52881) allow an attacker to execute a full container breakout, leading to root privilege escalation on the host node. An actor with privileges to deploy a malicious container image can exploit these vulnerabilities. **What should I do?** GKE is developing new versions that include the fixes for these vulnerabilities. This bulletin will be updated once these new versions are available. | High  
  
### GKE on Azure

Description | Severity  
---|---  
Several security issues have been discovered in runc, an open source software component used for running containers on GKE. The vulnerabilities (CVE-2025-31133, CVE-2025-52565, and CVE-2025-52881) allow an attacker to execute a full container breakout, leading to root privilege escalation on the host node. An actor with privileges to deploy a malicious container image can exploit these vulnerabilities. **What should I do?** GKE is developing new versions that include the fixes for these vulnerabilities. This bulletin will be updated once these new versions are available. | High  
  
### GDC (bare metal)

**Updated:** 2025-11-27

Description | Severity  
---|---  
Several security issues have been discovered in runc, an open source software component used for running containers on GKE. The vulnerabilities (CVE-2025-31133, CVE-2025-52565, and CVE-2025-52881) allow an attacker to execute a full container breakout, leading to root privilege escalation on the host node. An actor with privileges to deploy a malicious container image can exploit these vulnerabilities.

#### What should I do?

**2025-11-27 Update:** The following versions of GDC (bare metal) are updated with code to fix this vulnerability. Upgrade your GDC (bare metal) clusters to these versions or later:

  * 1.31.1000-gke.44



* * *

GKE is developing new versions that include the fixes for these vulnerabilities. This bulletin will be updated once these new versions are available. | High  
  
## GCP-2025-063

**Published:** 2025-10-28  
**Updated:** 2025-11-17  
**Reference:** [CVE-2025-39682](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-39682)

**2025-10-30 Update:** Added patch versions and a severity rating for GDC software for VMware.

### GKE

**Updated:** 2025-11-17

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-39682

GKE Standard and Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2025-11-17 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later: 

  * 1.32.9-gke.1462000
  * 1.33.5-gke.1697000
  * 1.34.1-gke.2909000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.33.5-gke.1162000
  * 1.32.9-gke.1072000
  * 1.28.15-gke.2751000
  * 1.34.1-gke.1127000
  * 1.30.14-gke.1267000
  * 1.31.13-gke.1023000
  * 1.29.15-gke.1936000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2025-10-30

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-39682



#### What should I do?

**2025-10-30 Update:** The following versions of GDC software for VMware are updated with code to fix this vulnerability. Upgrade your GDC software for VMware clusters to these versions or later:

  * 1.31.1000-gke.44



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-39682



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-39682



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-39682



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-062

**Published:** 2025-10-22  
**Updated:** 2025-10-30  
**Reference:** [CVE-2024-58240](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-58240)

**2025-10-30 Update:** Added patch versions for Ubuntu nodes on GKE, and patch versions and a severity rating for GDC software for VMware.

### GKE

**Updated:** 2025-10-30

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-58240

GKE Standard and Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2025-10-30 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to these versions or later:

  * 1.28.15-gke.2740000
  * 1.29.15-gke.1979000
  * 1.30.14-gke.1267000
  * 1.31.13-gke.1040000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.32.9-gke.1010000
  * 1.28.15-gke.2740000
  * 1.29.15-gke.1936000
  * 1.31.12-gke.1220000
  * 1.30.14-gke.1267000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2025-10-30

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-58240



#### What should I do?

**2025-10-30 Update:** The following versions of GDC software for VMware are updated with code to fix this vulnerability. Upgrade your GDC software for VMware clusters to these versions or later:

  * 1.31.1000-gke.44



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | High  
  
### GKE on AWS

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-58240



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-58240



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-58240



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-057

**Published:** 2025-10-17  
**Updated:** 2025-11-11  
**Reference:** [CVE-2025-38618](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38618)

**2025-11-11 Update:** Added patch versions for Ubuntu node pools in GKE.

**2025-10-27 Update:** Added patch versions and a severity rating for GDC software for VMware.

### GKE

**Updated:** 2025-11-11

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38618

GKE Standard and Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2025-11-11 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.28.15-gke.2767000
  * 1.29.15-gke.2002000
  * 1.30.14-gke.1349000
  * 1.31.13-gke.1123000
  * 1.32.9-gke.1207000
  * 1.33.5-gke.1308000
  * 1.34.1-gke.2037000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.30.14-gke.1267000
  * 1.31.13-gke.1023000
  * 1.29.15-gke.1936000
  * 1.33.5-gke.1162000
  * 1.32.9-gke.1072000
  * 1.28.15-gke.2751000
  * 1.34.1-gke.1127000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2025-10-27

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38618



#### What should I do?

**2025-10-27 Update:** The following versions of GDC software for VMware are updated with code to fix this vulnerability. Upgrade your GDC software for VMware clusters to these versions or later:

  * 1.31.1000-gke.44



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | High  
  
### GKE on AWS

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38618



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38618



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38618



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-056

**Published:** 2025-10-16  
**Updated:** 2026-03-24  
**Reference:** [CVE-2025-39946](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-39946)

**2026-03-24 Update:** Added patch versions for Ubuntu nodes with GKE.

**2025-11-13 Update:** Added patch versions for GDC software for VMware.

### GKE

**Updated:** 2026-03-24

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-39946

GKE Standard and Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2026-03-24 Update** : The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.35.2-gke.1269000
  * 1.34.4-gke.1193000
  * 1.33.8-gke.1169000
  * 1.32.13-gke.1059000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.32.9-gke.1108000
  * 1.29.15-gke.1989000
  * 1.31.13-gke.1023000
  * 1.30.14-gke.1336000
  * 1.28.15-gke.2751000
  * 1.34.1-gke.1279000
  * 1.33.5-gke.1162000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2025-11-13

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-39946



#### What should I do?

**2025-11-13 Update:** The following versions of GDC software for VMware are updated with code to fix this vulnerability. Upgrade your GDC software for VMware clusters to the following versions or later: 

  * 1.31.1100-gke.40



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | High  
  
### GKE on AWS

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-39946



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-39946



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-39946



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-055

**Published:** 2025-10-15  
**Updated:** 2025-11-11  
**Reference:** [CVE-2025-38617](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38617)

**2025-11-11 Update:** Added patch versions for Ubuntu node pools in GKE.

**2025-10-16 Update:** Added patch versions and a severity rating for GDC software for VMware.

### GKE

**Updated:** 2025-11-11

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38617

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2025-11-11 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.28.15-gke.2767000
  * 1.29.15-gke.2002000
  * 1.30.14-gke.1349000
  * 1.31.13-gke.1123000
  * 1.32.9-gke.1207000
  * 1.33.5-gke.1308000
  * 1.34.1-gke.2037000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.28.15-gke.2610000
  * 1.32.9-gke.1010000
  * 1.33.4-gke.1350000
  * 1.29.15-gke.1835000
  * 1.31.12-gke.1220000
  * 1.30.14-gke.1267000
  * 1.34.1-gke.1127000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2025-10-16

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38617



#### What should I do?

**2025-10-16 Update:** The following versions of GDC software for VMware are updated with code to fix this vulnerability. Upgrade your GDC software for VMware clusters to the following versions or later:

  * 1.31.1000-gke.44



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | High  
  
### GKE on AWS

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38617



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38617



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38617



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-050

**Published:** 2025-09-10  
**Updated:** 2025-11-11  
**Reference:** [CVE-2025-38500](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38500)

**2025-11-11 Update:** Added patch versions for Ubuntu node pools in GKE.

**2025-10-16 Update:** Added patch versions and a severity rating for GDC software for VMware.

### GKE

**Updated:** 2025-11-11

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38500

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2025-11-11 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.32.9-gke.1207000
  * 1.33.5-gke.1308000
  * 1.34.1-gke.2037000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.33.4-gke.1036000
  * 1.32.8-gke.1026000
  * 1.31.12-gke.1014000
  * 1.30.14-gke.1108000
  * 1.29.15-gke.1820000
  * 1.28.15-gke.2599000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2025-10-16

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38500



#### What should I do?

**2025-10-16 Update:** The following versions of GDC software for VMware are updated with code to fix this vulnerability. Upgrade your GDC software for VMware clusters to the following versions or later:

  * 1.31.1000-gke.44



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | High  
  
### GKE on AWS

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38500



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38500



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38500



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-047

**Published:** 2025-08-27  
**Updated:** 2025-09-25  
**Reference:** [CVE-2025-38350](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38350)

**2025-09-25 Update:** Added patch versions for Ubuntu node pools on GKE.

### GKE

**Updated:** 2025-09-25

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38350

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2025-09-25 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.28.15-gke.2697000
  * 1.29.15-gke.1936000
  * 1.30.14-gke.1150000
  * 1.31.12-gke.1110000 
  * 1.32.8-gke.1170000
  * 1.33.4-gke.1245000
  * 1.34.0-gke.1662000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.28.15-gke.2527000
  * 1.32.7-gke.1016000
  * 1.33.3-gke.1392000
  * 1.29.15-gke.1713000
  * 1.31.11-gke.1064000
  * 1.30.14-gke.1011000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38350



#### What should I do?

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38350



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38350



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38350



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-046

**Published:** 2025-08-23  
**Updated:** 2025-11-11  
**Reference:** [CVE-2025-38477](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38477)

**2025-11-11 Update:** Added patch versions for Ubuntu node pools in GKE.

**2025-10-16 Update:** Added patch versions and a severity rating for GDC software for VMware.

### GKE

**Updated:** 2025-11-11

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38477

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2025-11-11 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.28.15-gke.2767000
  * 1.29.15-gke.2002000
  * 1.30.14-gke.1349000
  * 1.31.13-gke.1123000
  * 1.32.9-gke.1207000
  * 1.33.5-gke.1308000
  * 1.34.1-gke.2037000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.32.7-gke.1016000
  * 1.33.3-gke.1392000
  * 1.29.15-gke.1713000
  * 1.30.14-gke.1011000
  * 1.31.11-gke.1064000
  * 1.28.15-gke.2527000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2025-10-16

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38477



#### What should I do?

**2025-10-16 Update:** The following versions of GDC software for VMware are updated with code to fix this vulnerability. Upgrade your GDC software for VMware clusters to the following versions or later:

  * 1.31.1000-gke.44



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | High  
  
### GKE on AWS

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38477



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38477



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38477



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-041

**Published:** 2025-07-21  
**Updated:** 2025-11-10  
**Reference:** [CVE-2025-37890](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-37890)

**2025-11-10 Update:** Added patch versions for GDC software for VMware.

### GKE

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Ubuntu nodes: 

  * CVE-2025-37890

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Ubuntu node pools to one of the following patch versions or later:

  * 1.28.15-gke.2461000
  * 1.29.15-gke.1614000
  * 1.30.12-gke.1372000
  * 1.31.10-gke.1067000
  * 1.32.6-gke.1060000
  * 1.33.2-gke.1384000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2025-11-10

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Ubuntu nodes: 

  * CVE-2025-37890



#### What should I do?

**2025-11-10 Update:** The following versions of GDC software for VMware are updated with code to fix this vulnerability. Upgrade your GDC software for VMware clusters to the following versions or later: 

  * 1.31.300-gke.81



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Ubuntu nodes: 

  * CVE-2025-37890



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Ubuntu nodes: 

  * CVE-2025-37890



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Ubuntu nodes: 

  * CVE-2025-37890



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-039

**Published:** 2025-07-15  
**Updated:** 2025-11-10  
**Reference:** [CVE-2025-38083](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38083)

**2025-11-10 Update:** Added patch versions for GDC software for VMware.

**2025-08-28 Update:** Added patch versions for Ubuntu node pools on GKE.

### GKE

**Updated:** 2025-08-28

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38083

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2025-08-28 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.28.15-gke.2564000
  * 1.29.15-gke.1773000
  * 1.30.14-gke.1036000
  * 1.31.11-gke.1101000
  * 1.32.7-gke.1079000
  * 1.33.3-gke.1392000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.32.6-gke.1013000
  * 1.29.15-gke.1607000
  * 1.31.10-gke.1021000
  * 1.30.12-gke.1333000
  * 1.33.2-gke.1240000
  * 1.28.15-gke.2456000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2025-11-10

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38083



#### What should I do?

**2025-11-10 Update:** The following versions of GDC software for VMware are updated with code to fix this vulnerability. Upgrade your GDC software for VMware clusters to the following versions or later: 

  * 1.31.300-gke.81



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | High  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38083



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38083



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38083



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-038

**Published:** 2025-07-09  
**Updated:** 2025-09-25  
**Reference:** [CVE-2025-37752](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-37752)

**2025-09-25 Update:** Added patch versions for Ubuntu node pools on GKE.

### GKE

**Updated:** 2025-09-25

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-37752

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2025-09-25 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.28.15-gke.2697000
  * 1.29.15-gke.1936000
  * 1.30.14-gke.1150000
  * 1.31.12-gke.1110000 
  * 1.32.8-gke.1170000
  * 1.33.4-gke.1245000
  * 1.34.0-gke.1662000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.33.1-gke.1584000
  * 1.32.4-gke.1603000
  * 1.31.9-gke.1176000
  * 1.30.12-gke.1208000
  * 1.28.15-gke.2303000
  * 1.29.15-gke.1415000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-37752



#### What should I do?

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-37752



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-37752



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-37752



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-036

**Published:** 2025-07-01  
**Updated:** 2025-11-10  
**Reference:** [CVE-2025-38001](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38001)

**2025-11-10 Update:** Added patch versions for GDC software for VMware.

**2025-07-21 Update:** Added patch versions for Ubuntu node pools on GKE.

### GKE

**Updated:** 2025-07-21

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38001

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2025-07-21 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your GKE Ubuntu node pools to the following versions or later: 

  * 1.28.15-gke.2461000
  * 1.29.15-gke.1614000
  * 1.30.12-gke.1372000
  * 1.31.10-gke.1067000
  * 1.32.6-gke.1060000
  * 1.33.2-gke.1384000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.33.1-gke.1959000
  * 1.30.12-gke.1279000
  * 1.31.9-gke.1287000
  * 1.28.15-gke.2428000
  * 1.29.15-gke.1549000
  * 1.32.4-gke.1698000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2025-11-10

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38001



#### What should I do?

**2025-11-10 Update:** The following versions of GDC software for VMware are updated with code to fix this vulnerability. Upgrade your GDC software for VMware clusters to the following versions or later: 

  * 1.31.300-gke.81



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | High  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38001



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38001



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38001



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-035

**Published:** 2025-06-17  
**Updated:** 2025-11-10  
**Reference:** [CVE-2025-37997](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-37997)

**2025-11-10 Update:** Added patch versions for GDC software for VMware.

**2025-07-21 Update:** Added patch versions for Ubuntu node pools on GKE.

### GKE

**Updated:** 2025-07-21

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-37997

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2025-07-21 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your GKE Ubuntu node pools to the following versions or later: 

  * 1.28.15-gke.2461000
  * 1.29.15-gke.1614000
  * 1.30.12-gke.1372000
  * 1.31.10-gke.1067000
  * 1.32.6-gke.1060000
  * 1.33.2-gke.1384000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.28.15-gke.2403000
  * 1.31.9-gke.1176000
  * 1.30.12-gke.1246000
  * 1.29.15-gke.1523000
  * 1.33.1-gke.1545000
  * 1.27.16-gke.2874000
  * 1.32.4-gke.1603000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2025-11-10

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-37997



#### What should I do?

**2025-11-10 Update:** The following versions of GDC software for VMware are updated with code to fix this vulnerability. Upgrade your GDC software for VMware clusters to the following versions or later: 

  * 1.31.300-gke.81



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-37997



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-37997



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-37997



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-034

**Published:** 2025-06-17  
**Updated:** 2025-07-21  
**Reference:** [CVE-2025-38000](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38000)

**2025-07-21 Update:** Added patch versions for Ubuntu node pools on GKE.

### GKE

**Updated:** 2025-07-21

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38000

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2025-07-21 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your GKE Ubuntu node pools to the following versions or later: 

  * 1.28.15-gke.2461000
  * 1.29.15-gke.1614000
  * 1.30.12-gke.1372000
  * 1.31.10-gke.1067000
  * 1.32.6-gke.1060000
  * 1.33.2-gke.1384000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.33.1-gke.1545000
  * 1.27.16-gke.2874000
  * 1.32.4-gke.1603000
  * 1.28.15-gke.2403000
  * 1.30.12-gke.1246000
  * 1.31.9-gke.1176000
  * 1.29.15-gke.1523000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38000



#### What should I do?

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38000



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38000



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-38000



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-033

**Published:** 2025-06-06  
**Reference:** N/A

### GKE

Description | Severity  
---|---  
A security issue was discovered where attackers might be able to bypass [workload isolation](https://cloud.google.com/kubernetes-engine/docs/how-to/isolate-workloads-dedicated-nodes#avoiding-privesc) restrictions on GKE clusters. Only clusters relying on node isolation to separate workloads inside a cluster are affected. Note that node isolation should never be used as a primary security boundary.  To exploit this vulnerability, attackers must first gain access to the kubelet node client credentials. Access to these credentials typically requires root permissions on the host and access to the host filesystem. For most systems, this means you need both an application vulnerability to gain access to the workload and a container breakout vulnerability to gain access to the host. Attackers with access to such credentials could do the following: 

  * Attackers could re-register the node with the same name, but with different values for certain fields in the Node object. Specifically, an attacker could set `.spec.providerID` to point to a different instance in the cluster, causing the GKE control plane to delete the referenced Compute Engine instance. 
  * Attackers could also change `.spec.taints` to affect workload scheduling. When implementing node isolation as a security control, you must use labels and label selectors with the `node-restriction.kubernetes.io/` prefix to prevent compromised nodes from manipulating scheduling behavior. 



#### What should I do?

Implement the following changes to address this issue: **Upgrade your GKE cluster and optionally implement validating admission policy** Address the provider ID issue by upgrading your GKE clusters to a patched version. The following versions of GKE or later have been updated to address the `providerID` issue: 

  * 1.33.1-gke.1386000
  * 1.32.4-gke.1533000
  * 1.31.9-gke.1119000
  * 1.30.12-gke.1208000

Optionally, if you cannot upgrade, implement the following validating admission policy on your cluster to mitigate the `providerID` issue: 
    
    
    apiVersion: admissionregistration.k8s.io/v1
    kind: ValidatingAdmissionPolicy
    metadata:
      name: validate-node-providerid
    spec:
      failurePolicy: Fail
      matchConstraints:
        resourceRules:
        - apiGroups:   [""]
          apiVersions: ["v1"]
          operations:  ["CREATE", "UPDATE"]
          resources:   ["nodes"]
      matchConditions:
      - name: "has-providerid"
        expression: "has(object.spec.providerID)"
      validations:
      - expression: "object.spec.providerID == '' || object.spec.providerID.endsWith('/' + object.metadata.name)"
        message: "node.spec.providerID must match the node name"
    ---
    apiVersion: admissionregistration.k8s.io/v1
    kind: ValidatingAdmissionPolicyBinding
    metadata:
      name: validate-node-providerid-binding
    spec:
      policyName: validate-node-providerid
      validationActions: [Deny]

**Use node restricted labels when isolating workloads to specific nodes as a security control** If you are using labels for node isolation, as described in [Kubernetes documentation](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#node-isolation-restriction), use node restricted labels (for example, labels of the form `node-restriction.kubernetes.io/example-constraint`) in node affinity and node selector terms used for workload isolation.  Kubelet node credentials are prevented from applying such labels by the [NodeRestriction](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#noderestriction) admission controller. The NodeRestriction admission controller is built into Kubernetes and enabled on all GKE clusters.  **GKE restricts the scope of node credentials on newly created nodes for new clusters** As an additional hardening measure, new clusters starting from GKE version 1.33.1-gke.1386000 restrict the scope of node credentials on newly created nodes. Node credentials are bound to the Compute Engine instance originally provisioned for the Node. After the instance is deleted, attackers are prevented from using such compromised credentials to register the Node, with attacker controlled taints or `providerID` values. You can create a new cluster with version 1.33.1-gke.1386000 or later for newly-created nodes to have this additional hardening.  | Medium  
  
### GDC (VMware)

Description | Severity  
---|---  
A security issue was discovered where attackers might be able to bypass [workload isolation](https://cloud.google.com/kubernetes-engine/docs/how-to/isolate-workloads-dedicated-nodes#avoiding-privesc) restrictions on GKE clusters.

#### What should I do?

No action required. This issue is specific to how GKE nodes are provisioned and managed on Compute Engine, and does not apply to GDC (VMware). | None  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSA security issue was discovered where attackers might be able to bypass [workload isolation](https://cloud.google.com/kubernetes-engine/docs/how-to/isolate-workloads-dedicated-nodes#avoiding-privesc) restrictions on GKE clusters.

#### What should I do?

##### GKE on AWS

No action required. This issue is specific to how GKE nodes are provisioned and managed on Compute Engine, and does not apply to GKE on AWS.

##### GKE on AWS (previous generation)

No action required. This issue is specific to how GKE nodes are provisioned and managed on Compute Engine, and does not apply to GKE on AWS (previous generation). | None  
  
### GKE on Azure

Description | Severity  
---|---  
A security issue was discovered where attackers might be able to bypass [workload isolation](https://cloud.google.com/kubernetes-engine/docs/how-to/isolate-workloads-dedicated-nodes#avoiding-privesc) restrictions on GKE clusters.

#### What should I do?

No action required. This issue is specific to how GKE nodes are provisioned and managed on Compute Engine, and does not apply to GKE on Azure. | None  
  
### GDC (bare metal)

Description | Severity  
---|---  
A security issue was discovered where attackers might be able to bypass [workload isolation](https://cloud.google.com/kubernetes-engine/docs/how-to/isolate-workloads-dedicated-nodes#avoiding-privesc) restrictions on GKE clusters.

#### What should I do?

No action required. This issue is specific to how GKE nodes are provisioned and managed on Compute Engine, and does not apply to GDC (bare metal). | None  
  
## GCP-2025-032

**Published:** 2025-06-03  
**Updated:** 2025-07-21  
**Reference:** [CVE-2025-37798](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-37798)

**2025-07-21 Update:** Added patch versions for Ubuntu node pools on GKE.

### GKE

**Updated:** 2025-07-21

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-37798

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2025-07-21 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your GKE Ubuntu node pools to the following versions or later: 

  * 1.28.15-gke.2461000
  * 1.29.15-gke.1614000
  * 1.30.12-gke.1372000
  * 1.31.10-gke.1067000
  * 1.32.6-gke.1060000
  * 1.33.2-gke.1384000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.29.15-gke.1415000
  * 1.30.12-gke.1168000
  * 1.31.9-gke.1044000
  * 1.27.16-gke.2771000
  * 1.28.15-gke.2303000
  * 1.32.4-gke.1415000
  * 1.33.1-gke.1107000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-37798



#### What should I do?

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-37798



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-37798



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-37798



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-031

**Published:** 2025-06-03  
**Updated:** 2025-08-26  
**Reference:** [CVE-2025-37797](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-37797)

**2025-08-26 Update:** Added patch versions for Ubuntu node pools on GKE.

### GKE

**Updated:** 2025-08-26

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-37797

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2025-08-26 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.28.15-gke.2507000
  * 1.29.15-gke.1686000
  * 1.30.14-gke.1011000
  * 1.31.11-gke.1064000
  * 1.32.7-gke.1079000
  * 1.33.3-gke.1392000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.32.4-gke.1415000
  * 1.28.15-gke.2303000
  * 1.27.16-gke.2820000
  * 1.33.1-gke.1107000
  * 1.29.15-gke.1415000
  * 1.31.9-gke.1044000
  * 1.30.12-gke.1168000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-37797



#### What should I do?

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-37797



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-37797



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-37797



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-022

**Published:** 2025-05-01  
**Updated:** 2025-05-22  
**Reference:** [CVE-2025-21702](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21702)

**2025-05-22 Update:** Added patch versions for Ubuntu node pools on GKE. 

### GKE

**Updated:** 2025-05-22

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-21702

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2025-05-22 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your GKE Ubuntu node pools to the following versions or later: 

  * 1.27.16-gke.2771000
  * 1.28.15-gke.2239000
  * 1.29.15-gke.1325000
  * 1.30.12-gke.1086000
  * 1.31.8-gke.1113000
  * 1.32.4-gke.1236000
  * 1.33.0-gke.1868000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.29.15-gke.1193000
  * 1.30.11-gke.1157000
  * 1.31.7-gke.1265000
  * 1.32.3-gke.1785000
  * 1.28.15-gke.2072000
  * 1.27.16-gke.2650000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-21702



#### What should I do?

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-21702



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-21702



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-21702



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-021

**Published:** 2025-04-29  
**Updated:** 2025-06-02  
**Reference:** [CVE-2025-21971](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21971)

**2025-06-02 Update:** Added patch versions for Ubuntu node pools on GKE.

### GKE

**Updated:** 2025-06-02

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-21971

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2025-06-02 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your GKE Ubuntu node pools to the following versions or later: 

  * 1.27.16-gke.2820000
  * 1.28.15-gke.2303000
  * 1.29.15-gke.1415000
  * 1.30.12-gke.1168000
  * 1.31.9-gke.1044000
  * 1.32.4-gke.1415000
  * 1.33.1-gke.1107000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.28.15-gke.2142000
  * 1.30.11-gke.1157000
  * 1.31.7-gke.1265000
  * 1.32.3-gke.1785000
  * 1.29.15-gke.1193000
  * 1.27.16-gke.2682000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-21971



#### What should I do?

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-21971



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-21971



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-21971



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-019

**Published:** 2025-04-25  
**Updated:** 2025-06-26  
**Reference:** [CVE-2025-21701](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21701)

**2025-06-26 Update:** Added patch versions for GDC (VMware).

**2025-05-22 Update:** Added patch versions for Ubuntu node pools on GKE.

### GKE

**Updated:** 2025-05-22

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2025-21701

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2025-05-22 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your GKE Ubuntu node pools to the following versions or later: 

  * 1.27.16-gke.2771000
  * 1.28.15-gke.2239000
  * 1.29.15-gke.1325000
  * 1.30.12-gke.1086000
  * 1.31.8-gke.1113000
  * 1.32.4-gke.1236000
  * 1.33.0-gke.1868000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.27.16-gke.2440000
  * 1.28.15-gke.1844000
  * 1.29.14-gke.1018000
  * 1.30.10-gke.1042000
  * 1.31.6-gke.1020000
  * 1.32.1-gke.1729000

**Note:** Patched Ubuntu versions will be released soon. You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2025-06-26

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2025-21701



#### What should I do?

**2025-06-26 Update:** The following versions of GDC software for VMware are updated with code to fix this vulnerability. Upgrade your GDC software for VMware clusters to the following versions or later: 

  * 1.32.0-gke.1087
  * 1.31.300-gke.81
  * 1.30.700-gke.56



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2025-21701



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2025-21701



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2025-21701



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-018

**Published:** 2025-04-23  
**Updated:** 2025-10-09  
**Reference:** [CVE-2025-40364](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-40364)

**2025-10-09 Update:** added patch versions for Ubuntu nodes.

### GKE

**Updated:** 2025-10-09

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2025-40364

GKE Standard and Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2025-10-09 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.32.8-gke.1170000
  * 1.33.4-gke.1350000
  * 1.34.0-gke.1662000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.27.16-gke.2573000
  * 1.28.15-gke.2003000
  * 1.29.15-gke.1017000
  * 1.30.10-gke.1227000
  * 1.31.6-gke.1221000
  * 1.32.2-gke.1652000

**Note:** Patched Ubuntu versions will be released soon. You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2025-40364



#### What should I do?

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2025-40364



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2025-40364



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2025-40364



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-017

**Published:** 2025-04-17  
**Updated:** 2025-05-22  
**Reference:** [CVE-2025-21756](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21756)

**2025-05-22 Update:** Added patch versions for Ubuntu node pools on GKE.

**2025-05-05 Update:** Added patch versions for GDC software for VMware.

### GKE

**Updated:** 2025-05-22

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-21756

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2025-05-22 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your GKE Ubuntu node pools to the following versions or later: 

  * 1.27.16-gke.2771000
  * 1.28.15-gke.2239000
  * 1.29.15-gke.1325000
  * 1.30.12-gke.1086000
  * 1.31.8-gke.1113000
  * 1.32.4-gke.1236000
  * 1.33.0-gke.1868000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.31.6-gke.1221000
  * 1.30.11-gke.1093000
  * 1.29.15-gke.1134000
  * 1.27.16-gke.2650000
  * 1.32.3-gke.1170000
  * 1.28.15-gke.2097000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2025-05-05

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-21756



#### What should I do?

**2025-05-05 Update:** The following versions of GDC software for VMware are updated with code to fix this vulnerability. Upgrade your GDC software for VMware clusters to the following versions or later: 

  * 1.31.400-gke.110
  * 1.29.1300-gke.98



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | High  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-21756



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-21756



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-21756



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-016

**Published:** 2025-04-16  
**Updated:** 2025-05-22  
**Reference:** [CVE-2023-52927](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52927)

**2025-05-22 Update:** Added patch versions for Ubuntu GKE nodes.

**2025-04-29 Update:** Added patch versions for GDC software for VMware.

### GKE

**Updated:** 2025-05-22

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2023-52927

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2025-05-22 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your GKE Ubuntu node pools to the following versions or later: 

  * 1.27.16-gke.2771000
  * 1.28.15-gke.2239000
  * 1.29.15-gke.1325000
  * 1.30.12-gke.1086000
  * 1.31.8-gke.1113000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.31.6-gke.1064000
  * 1.28.15-gke.2097000
  * 1.32.2-gke.1652000
  * 1.27.16-gke.2650000
  * 1.29.15-gke.1134000
  * 1.30.11-gke.1093000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2025-04-29

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2023-52927



#### What should I do?

**2025-04-29 Update:** The following versions of GDC software for VMware are updated with code to fix this vulnerability. Upgrade your GDC software for VMware clusters to the following versions or later: 

  * 1.31.400-gke.110
  * 1.30.800-gke.66



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | High  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2023-52927



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2023-52927



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2023-52927



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-015

**Published:** 2025-04-15  
**Updated:** 2025-05-22  
**Reference:** [CVE-2025-21700](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21700)

**2025-05-22 Update:** Added patch versions for Ubuntu node pools on GKE.

**2025-04-17 Update:** Added patch versions for GDC (VMware). Updated GDC (VMware) severity from Pending to High.

### GKE

**Updated:** 2025-05-22

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-21700

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2025-05-22 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your GKE Ubuntu node pools to the following versions or later: 

  * 1.27.16-gke.2771000
  * 1.28.15-gke.2239000
  * 1.29.15-gke.1325000
  * 1.30.12-gke.1086000
  * 1.31.8-gke.1113000
  * 1.32.4-gke.1236000
  * 1.33.0-gke.1868000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.32.2-gke.1652000
  * 1.28.15-gke.1844000
  * 1.30.10-gke.1070000
  * 1.31.6-gke.1064000
  * 1.27.16-gke.2451000
  * 1.29.14-gke.1067000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2025-04-17

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-21700



#### What should I do?

**2025-04-17 Update:** The following versions of GDC software for VMware are updated with code to fix this vulnerability. Upgrade your GDC software for VMware clusters to the following versions or later: 

  * 1.30.600-gke.68
  * 1.29.1100-gke.82
  * 1.31.300-gke.81



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | High  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-21700



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-21700



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-21700



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-014

**Published:** 2025-04-10  
**Updated:** 2025-05-22  
**Reference:** [CVE-2025-21703](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21703)

**2025-05-22 Update:** Added patch versions for Ubuntu node pools on GKE.

**2025-05-05 Update:** Added patch versions for GDC software for VMware.

### GKE

**Updated:** 2025-05-22

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-21703

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2025-05-22 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your GKE Ubuntu node pools to the following versions or later: 

  * 1.27.16-gke.2771000
  * 1.28.15-gke.2239000
  * 1.29.15-gke.1325000
  * 1.30.12-gke.1086000
  * 1.31.8-gke.1113000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.32.3-gke.1170000
  * 1.29.15-gke.1017000
  * 1.27.16-gke.2573000
  * 1.28.15-gke.2003000
  * 1.30.10-gke.1227000
  * 1.31.6-gke.1221000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2025-05-05

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-21703



#### What should I do?

**2025-05-05 Update:** The following versions of GDC software for VMware are updated with code to fix this vulnerability. Upgrade your GDC software for VMware clusters to the following versions or later: 

  * 1.29.1300-gke.98
  * 1.31.300-gke.81
  * 1.30.800-gke.66



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | High  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-21703



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-21703



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2025-21703



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-013

**Published:** 2025-03-24  
**Reference:**[CVE-2025-1974](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-1974)

### GKE

Description | Severity  
---|---  
Several security issues have been discovered in the NGINX Ingress Controller, `ingress-nginx`, an open source software component that runs inside Kubernetes clusters to help manage network traffic coming into the cluster. The most critical is CVE-2025-1974. For the full details and a complete list, see the [Kubernetes CVE feed](https://kubernetes.io/docs/reference/issues-security/official-cve-feed/). These issues affect `ingress-nginx`. If you do not have `ingress-nginx` installed on your cluster, you are not affected. GKE clusters **do not** use `ingress-nginx`, and are not impacted by these security issues unless you have installed `ingress-nginx` on your cluster. If you have installed `ingress-nginx` on your GKE cluster, you may be vulnerable to these security issues. Using CVE-2025-1974, an unauthenticated attacker with access to the Pod network can achieve arbitrary code execution in the context of the `ingress-nginx` controller. This can lead to disclosure of Secrets that are accessible to the controller. When using the default configuration of `ingress-nginx`, the controller can access all Secrets in the entire cluster.

#### What should I do?

  1. Check if your GKE clusters are using `ingress-nginx` by using one of the following commands:
     * Check an individual cluster:
           
           kubectl get pods --all-namespaces --selector app.kubernetes.io/name=ingress-nginx

     * Check multiple clusters at once using a [Cloud Asset Inventory resource search query](https://docs.cloud.google.com/asset-inventory/docs/search-resources):
           
           gcloud asset search-all-resources \
               --scope='organizations/ORGANIZATION_ID' \
               --asset-types='k8s.io/Pod' \
               --query='labels."app.kubernetes.io/name"="ingress-nginx"'

Replace `ORGANIZATION_ID` with your organization resource ID. For details, see [Getting your organization resource ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).
  2. Upgrade `ingress-nginx` to a patched version. For details, see [the official Kubernetes CVE feed](https://kubernetes.io/docs/reference/issues-security/official-cve-feed/).
  3. Read about [customizing network isolation in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation). To reduce risks from untrusted networks, consider using [private nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#enable-private-node-level) and ensuring that you have restrictive [firewall configurations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#add_firewall_rules) in place.

| None  
  
### GDC (VMware)

Description | Severity  
---|---  
Several security issues have been discovered in the NGINX Ingress Controller, `ingress-nginx`, an open source software component that runs inside Kubernetes clusters to help manage network traffic coming into the cluster. The most critical is CVE-2025-1974. For the full details and a complete list, see the [Kubernetes CVE feed](https://kubernetes.io/docs/reference/issues-security/official-cve-feed/). These issues affect `ingress-nginx`. If you do not have `ingress-nginx` installed on your cluster, you are not affected. GDC software for VMware clusters **do not** use `ingress-nginx`, and are not impacted by these security issues unless you have installed `ingress-nginx` on your cluster. If you have installed `ingress-nginx` on your GDC software for VMware cluster, you may be vulnerable to these security issues. Using CVE-2025-1974, an unauthenticated attacker with access to the Pod network can achieve arbitrary code execution in the context of the `ingress-nginx` controller. This can lead to disclosure of Secrets that are accessible to the controller. When using the default configuration of `ingress-nginx`, the controller can access all Secrets in the entire cluster.

#### What should I do?

  1. Check if your GDC software for VMware clusters are using `ingress-nginx`:
         
         kubectl get pods --all-namespaces --selector app.kubernetes.io/name=ingress-nginx

  2. Upgrade `ingress-nginx` to a patched version. For details, see [the official Kubernetes CVE feed](https://kubernetes.io/docs/reference/issues-security/official-cve-feed/).

| None  
  
### GKE on AWS

Description | Severity  
---|---  
Several security issues have been discovered in the NGINX Ingress Controller, `ingress-nginx`, an open source software component that runs inside Kubernetes clusters to help manage network traffic coming into the cluster. The most critical is CVE-2025-1974. For the full details and a complete list, see the [Kubernetes CVE feed](https://kubernetes.io/docs/reference/issues-security/official-cve-feed/). These issues affect `ingress-nginx`. If you do not have `ingress-nginx` installed on your cluster, you are not affected. GKE on AWS clusters **do not** use `ingress-nginx`, and are not impacted by these security issues unless you have installed `ingress-nginx` on your cluster. If you have installed `ingress-nginx` on your GKE on AWS cluster, you may be vulnerable to these security issues. Using CVE-2025-1974, an unauthenticated attacker with access to the Pod network can achieve arbitrary code execution in the context of the `ingress-nginx` controller. This can lead to disclosure of Secrets that are accessible to the controller. When using the default configuration of `ingress-nginx`, the controller can access all Secrets in the entire cluster.

#### What should I do?

  1. Check if your GKE on AWS clusters are using `ingress-nginx`:
         
         kubectl get pods --all-namespaces --selector app.kubernetes.io/name=ingress-nginx

  2. Upgrade `ingress-nginx` to a patched version. For details, see [the official Kubernetes CVE feed](https://kubernetes.io/docs/reference/issues-security/official-cve-feed/).

| None  
  
### GKE on Azure

Description | Severity  
---|---  
Several security issues have been discovered in the NGINX Ingress Controller, `ingress-nginx`, an open source software component that runs inside Kubernetes clusters to help manage network traffic coming into the cluster. The most critical is CVE-2025-1974. For the full details and a complete list, see the [Kubernetes CVE feed](https://kubernetes.io/docs/reference/issues-security/official-cve-feed/). These issues affect `ingress-nginx`. If you do not have `ingress-nginx` installed on your cluster, you are not affected. GKE on Azure clusters **do not** use `ingress-nginx`, and are not impacted by these security issues unless you have installed `ingress-nginx` on your cluster. If you have installed `ingress-nginx` on your GKE on Azure cluster, you may be vulnerable to these security issues. Using CVE-2025-1974, an unauthenticated attacker with access to the Pod network can achieve arbitrary code execution in the context of the `ingress-nginx` controller. This can lead to disclosure of Secrets that are accessible to the controller. When using the default configuration of `ingress-nginx`, the controller can access all Secrets in the entire cluster.

#### What should I do?

  1. Check if your GKE on Azure clusters are using `ingress-nginx`:
         
         kubectl get pods --all-namespaces --selector app.kubernetes.io/name=ingress-nginx

  2. Upgrade `ingress-nginx` to a patched version. For details, see [the official Kubernetes CVE feed](https://kubernetes.io/docs/reference/issues-security/official-cve-feed/).

| None  
  
### GDC (bare metal)

Description | Severity  
---|---  
Several security issues have been discovered in the NGINX Ingress Controller, `ingress-nginx`, an open source software component that runs inside Kubernetes clusters to help manage network traffic coming into the cluster. The most critical is CVE-2025-1974. For the full details and a complete list, see the [Kubernetes CVE feed](https://kubernetes.io/docs/reference/issues-security/official-cve-feed/). These issues affect `ingress-nginx`. If you do not have `ingress-nginx` installed on your cluster, you are not affected. GDC software for bare metal clusters **do not** use `ingress-nginx`, and are not impacted by these security issues unless you have installed `ingress-nginx` on your cluster. If you have installed `ingress-nginx` on your GDC software for bare metal cluster, you may be vulnerable to these security issues. Using CVE-2025-1974, an unauthenticated attacker with access to the Pod network can achieve arbitrary code execution in the context of the `ingress-nginx` controller. This can lead to disclosure of Secrets that are accessible to the controller. When using the default configuration of `ingress-nginx`, the controller can access all Secrets in the entire cluster.

#### What should I do?

  1. Check if your GDC software for bare metal clusters are using `ingress-nginx`:
         
         kubectl get pods --all-namespaces --selector app.kubernetes.io/name=ingress-nginx

  2. Upgrade `ingress-nginx` to a patched version. For details, see [the official Kubernetes CVE feed](https://kubernetes.io/docs/reference/issues-security/official-cve-feed/).

| None  
  
## GCP-2025-012

**Published:** 2025-04-10  
**Updated:** 2025-04-10  
**Reference:** [CVE-2024-53164](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53164)

**2025-04-10 Update:** Added patch versions for Ubuntu GKE nodes and for GDC software for VMware.

### GKE

**Updated:** 2025-04-10

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-53164

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2025-04-10 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later: 

  * 1.31.6-gke.1064000
  * 1.27.16-gke.2451000
  * 1.28.15-gke.1844000
  * 1.29.14-gke.1067000
  * 1.30.10-gke.1070000
  * 1.32.2-gke.1652000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.27.16-gke.2451000
  * 1.32.2-gke.1182000
  * 1.29.14-gke.1067000
  * 1.30.10-gke.1070000
  * 1.31.6-gke.1064000
  * 1.28.15-gke.1844000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2025-04-10

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-53164



#### What should I do?

**2025-04-10 Update:** The following versions of GDC software for VMware are updated with code to fix this vulnerability. Upgrade your GDC software for VMware clusters to the following versions or later: 

  * 1.29.1100-gke.82
  * 1.31.200-gke.58
  * 1.30.500-gke.126



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | High  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-53164



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-53164



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-53164



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-010

**Published:** 2025-03-05  
**Updated:** 2025-06-02  
**Reference:** [CVE-2024-56770](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-56770)

**2025-06-02 Update:** Added patch versions for GKE.

**2025-04-10 Update:** Added patch versions for GDC software for VMware.

### GKE

**Updated:** 2025-06-02

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-56770

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2025-06-02 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your GKE Ubuntu node pools to the following versions or later: 

  * 1.27.16-gke.2732000
  * 1.28.15-gke.2192000
  * 1.29.15-gke.1274000
  * 1.30.12-gke.1151000
  * 1.31.8-gke.1113000
  * 1.32.4-gke.1415000
  * 1.33.1-gke.1107000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.27.16-gke.2387000
  * 1.28.15-gke.1612000
  * 1.29.13-gke.1006000
  * 1.30.8-gke.1261000
  * 1.31.5-gke.1023000
  * 1.32.1-gke.1729000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2025-04-10

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-56770



#### What should I do?

**2025-04-10 Update:** The following versions of GDC software for VMware are updated with code to fix this vulnerability. Upgrade your GDC software for VMware clusters to the following versions or later: 

  * 1.31.200-gke.58
  * 1.30.500-gke.126
  * 1.29.1100-gke.82



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | High  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-56770



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-56770



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-56770



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-009

**Published:** 2025-03-05  
**Reference:**[CVE-2024-53269](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53269), [CVE-2024-53270](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53270), [CVE-2024-53271](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53271)

### GKE

Description | Severity  
---|---  
The Envoy project recently announced several new security vulnerabilities ([CVE-2024-53269](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53269), [CVE-2024-53270](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53270), and [CVE-2024-53271](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53271)) that could allow an attacker to crash Envoy. GKE minor versions 1.31 and 1.32 using [Identity Service for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/oidc) are affected. GKE Autopilot clusters and clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) are also affected.

#### What should I do?

Upgrade your GKE clusters and node pools to one of the following versions or later:

  * 1.31.3-gke.1162000
  * 1.32.0-gke.1448000

We recommend that you [manually upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your cluster even if you have node auto-upgrade enabled. A recent feature of [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions) allows you to apply a patch without having to unsubscribe from a channel. This lets you secure your nodes until the new version becomes the default for your specific release channel. | High  
  
### GDC (VMware)

Description | Severity  
---|---  
The Envoy project recently announced several new security vulnerabilities ([CVE-2024-53269](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53269), [CVE-2024-53270](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53270), and [CVE-2024-53271](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53271)) that could allow an attacker to crash Envoy. GDC software for VMware versions 1.31, 1.30, and 1.29 using Cloud Service Mesh version 1.23.3-asm.3 are affected.

#### What should I do?

The following versions of GDC software for VMware have been updated with code to fix this vulnerability. We recommend that you upgrade your admin and user clusters to one of the following GDC software for VMware versions:

  * 1.31.200
  * 1.30.600
  * 1.29.1000

| High  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe Envoy project recently announced several new security vulnerabilities ([CVE-2024-53269](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53269), [CVE-2024-53270](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53270), and [CVE-2024-53271](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53271)) that could allow an attacker to crash Envoy. GKE on AWS does not ship with Envoy and is not affected.

#### What should I do?

No action is required. | None  
  
### GKE on Azure

Description | Severity  
---|---  
The Envoy project recently announced several new security vulnerabilities ([CVE-2024-53269](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53269), [CVE-2024-53270](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53270), and [CVE-2024-53271](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53271)) that could allow an attacker to crash Envoy. GKE on Azure does not ship with Envoy and is not affected.

#### What should I do?

No action is required. | None  
  
### GDC (bare metal)

Description | Severity  
---|---  
The Envoy project recently announced several new security vulnerabilities ([CVE-2024-53269](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53269), [CVE-2024-53270](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53270), and [CVE-2024-53271](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53271)) that could allow an attacker to crash Envoy.

#### What should I do?

The following versions of GDC software for bare metal have been updated with code to fix this vulnerability. We recommend that you upgrade your clusters to one of the following GDC software for bare metal versions:

  * 1.31.200-gke.59
  * 1.30.600-gke.69
  * 1.29.1100-gke.84

| High  
  
## GCP-2025-008

**Published:** 2025-02-19  
**Updated:** 2025-04-10  
**Reference:** [CVE-2024-53141](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53141)

**2025-04-10 Update:** Added patch versions for GDC software for VMware.

### GKE

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-53141

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.27.16-gke.2296000
  * 1.28.15-gke.1673000
  * 1.29.13-gke.1038000
  * 1.30.9-gke.1009000
  * 1.31.5-gke.1023000
  * 1.32.1-gke.1729000

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Ubuntu node pools to one of the following patch versions or later:

  * 1.27.16-gke.2342000
  * 1.28.15-gke.1720000
  * 1.29.13-gke.1109000
  * 1.30.9-gke.1127000
  * 1.31.5-gke.1169000
  * 1.32.1-gke.1729000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2025-04-10

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-53141



#### What should I do?

**2025-04-10 Update:** The following versions of GDC software for VMware are updated with code to fix this vulnerability. Upgrade your GDC software for VMware clusters to the following versions or later: 

  * 1.31.200-gke.58
  * 1.30.600-gke.68
  * 1.29.1100-gke.82



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | High  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-53141



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-53141



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-53141



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-006

**Published:** 2025-01-23  
**Reference:** N/A

### GKE

Description | Severity  
---|---  
A security issue was discovered in the [Google Secret Manager Provider for Secret Store CSI Driver](https://github.com/GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp). To exploit this vulnerability, an attacker must be able to do the following: 

  1. Create Pods on nodes where the CSI driver is running. 
  2. Create Secrets in the same namespaces as those Pods. 
  3. Mount Secrets Store CSI volumes on the Pod with the `nodePublishSecretRef` option set. 
  4. Provide a malicious Application Default Credential configuration in the Secret. 
  5. Reference the Secret in the `nodePublishSecretRef` option on the volume mount.

By following these steps, an attacker could trick the CSI driver into leaking the Kubernetes service account token of the CSI driver to a URL controlled by the attacker.  The Secret Manager Provider can be used in two ways with a GKE cluster. The [Secret Manager add-on for GKE](https://docs.cloud.google.com/secret-manager/docs/secret-manager-managed-csi-component) is a managed feature available on GKE clusters. Alternatively, as a GKE user you can [install](https://github.com/GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp/blob/main/deploy/provider-gcp-plugin.yaml) the open source [Google Secret Manager Provider for Secret Store CSI Driver](https://github.com/GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp) on your GKE cluster. In both cases, the provider allows a Kubernetes Pod to access secrets stored in Google Cloud Secret Manager as files mounted to the Pod as a volume.  The fixes for both the managed GKE Secret Manager add-on and open source Secret Manager Provider disable the use of nodePublishSecretRef to avoid this issue. This was determined not to impact any existing usage of the GKE Secret Manager add-on. A very small number of GKE clusters using the open source Secret Manager Provider with nodePublishSecretRef might see an impact. The [open source patch](https://github.com/GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp/pull/486) makes it possible to re-enable the nodePublishSecretRef feature via the `ALLOW_NODE_PUBLISH_SECRET` environment variable, if necessary. 

#### What should I do?

Do either of following depending on how your GKE cluster uses the Secret Manager Provider: **Managed GKE Secret Manager add-on** If you're using the [managed GKE add-on](https://docs.cloud.google.com/secret-manager/docs/secret-manager-managed-csi-component), upgrade your GKE cluster to a patched version. The following versions of GKE are updated with code to fix this vulnerability. Upgrade your node pools to the following versions or later: 

  * 1.27.16-gke.2051000
  * 1.28.15-gke.1362000
  * 1.29.11-gke.1012000
  * 1.30.6-gke.1596000
  * 1.31.1-gke.1846000

To receive the fix as quickly as possible, we recommend [manually upgrading](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your cluster and Standard node pools to a patched GKE version. GKE [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions) allow you to patch before the new version becomes an auto-upgrade target on your selected release channel.  **Open source Secret Manager Provider** If you're using the [open source Secret Manager provider](https://github.com/GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp), upgrade to [1.7.0.](https://github.com/GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp/releases/tag/v1.7.0) If you use the [Helm Chart](https://github.com/GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp/tree/main/charts/secrets-store-csi-driver-provider-gcp), the latest version already refers to 1.7.0. If you base your installation directly on the [deploy/provider-gcp-plugin.yaml](https://github.com/GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp/blob/main/deploy/provider-gcp-plugin.yaml) file, note that the image has also been updated in that file.  | Medium  
  
### GDC (VMware)

Description | Severity  
---|---  
A vulnerability in the [Google Secret Manager Provider for Secret Store CSI Driver](https://github.com/GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp) allows an attacker with Pod and Secret creation permissions in a namespace to exfiltrate the CSI driver's Kubernetes service account token by mounting a malicious volume on a Pod. 

#### What should I do?

If you have manually installed the open source Secret Manager Provider, you might be affected. See instructions regarding the open source Secret Manager Provider on the [GKE](https://docs.cloud.google.com/kubernetes-engine/security-bulletins#gcp-2025-006-gke) tab. GDC (VMware) clusters are otherwise not affected as they don't offer a managed add-on, so no further action is required. | Medium  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWS A vulnerability in the [Google Secret Manager Provider for Secret Store CSI Driver](https://github.com/GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp) allows an attacker with Pod and Secret creation permissions in a namespace to exfiltrate the CSI driver's Kubernetes service account token by mounting a malicious volume on a Pod.

#### What should I do?

If you have manually installed the open source Secret Manager Provider, you might be affected. See instructions regarding the open source Secret Manager Provider on the [GKE](https://docs.cloud.google.com/kubernetes-engine/security-bulletins#gcp-2025-006-gke) tab. GKE on AWS clusters are otherwise not affected as they don't offer a managed add-on, so no further action is required. | Medium  
  
### GKE on Azure

Description | Severity  
---|---  
A vulnerability in the [Google Secret Manager Provider for Secret Store CSI Driver](https://github.com/GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp) allows an attacker with Pod and Secret creation permissions in a namespace to exfiltrate the CSI driver's Kubernetes service account token by mounting a malicious volume on a Pod. 

#### What should I do?

If you have manually installed the open source Secret Manager Provider, you might be affected. See instructions regarding the open source Secret Manager Provider on the [GKE](https://docs.cloud.google.com/kubernetes-engine/security-bulletins#gcp-2025-006-gke) tab. GKE on Azure clusters are otherwise not affected as they don't offer a managed add-on, so no further action is required. | Medium  
  
### GDC (bare metal)

Description | Severity  
---|---  
A vulnerability in the [Google Secret Manager Provider for Secret Store CSI Driver](https://github.com/GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp) allows an attacker with Pod and Secret creation permissions in a namespace to exfiltrate the CSI driver's Kubernetes service account token by mounting a malicious volume on a Pod. 

#### What should I do?

If you have manually installed the open source Secret Manager Provider, you might be affected. See instructions regarding the open source Secret Manager Provider on the [GKE](https://docs.cloud.google.com/kubernetes-engine/security-bulletins#gcp-2025-006-gke) tab. GDC (bare metal) clusters are otherwise not affected as they don't offer a managed add-on, so no further action is required. | Medium  
  
## GCP-2025-003

**Published:** 2025-01-09  
**Updated:** 2025-01-23  
**Reference:** [CVE-2024-50264](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-50264)

**2025-01-23 Update:** Added patch versions for Ubuntu node pools on GKE.

### GKE

**Updated:** 2025-01-23

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-50264

GKE Standard and Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2025-01-23 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to one of the following versions or later:

  * 1.27.16-gke.2270000
  * 1.28.15-gke.1641000
  * 1.29.13-gke.1006000
  * 1.30.8-gke.1282000
  * 1.31.5-gke.1023000
  * 1.32.1-gke.1002000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.27.16-gke.2081000
  * 1.28.15-gke.1480000
  * 1.29.12-gke.1055000
  * 1.30.8-gke.1051000
  * 1.31.4-gke.1072000
  * 1.32.0-gke.1448000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-50264



#### What should I do?

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-50264



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-50264



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-50264



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-002

**Published:** 2025-01-09  
**Updated:** 2025-01-23  
**Reference:** [CVE-2024-53057](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53057)

**2025-01-23 Update:** Added patch versions for Ubuntu node pools on GKE.

**2025-01-22 Update:** Added patch versions for GDC (VMware). Updated GDC (VMware) severity from Pending to Medium.

### GKE

**Updated:** 2025-01-23

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-53057

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2025-01-23 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to one of the following versions or later:

  * 1.27.16-gke.2270000
  * 1.28.15-gke.1641000
  * 1.29.13-gke.1006000
  * 1.30.8-gke.1282000
  * 1.31.5-gke.1023000
  * 1.32.1-gke.1002000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.27.16-gke.1836000
  * 1.28.15-gke.1342000
  * 1.29.11-gke.1012000
  * 1.30.7-gke.1077000
  * 1.31.3-gke.1056000
  * 1.32.0-gke.1448000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2025-01-22

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-53057



#### What should I do?

**2025-01-22 Update:** The following versions of GDC (VMware) are updated with code to fix this vulnerability. Upgrade your GDC (VMware) clusters to the following versions or later:

  * 1.29.900-gke.181
  * 1.31.0-gke.889
  * 1.30.400-gke.133



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Medium  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-53057



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-53057



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-53057



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2025-001

**Published:** 2025-01-08  
**Updated:** 2025-01-23  
**Reference:** N/A

**2025-01-23 Update:** Updated the **Affected resources** section in the [GKE](https://docs.cloud.google.com/kubernetes-engine/security-bulletins#gcp-2025-001-gke) tab.

**2025-01-08 Update:** Corrected the start date and time of the issue.

### GKE

**Updated:** 2025-01-23

Description | Severity  
---|---  
**2025-01-23 Update:** Updated the **Affected resources** section. **2025-01-08 Update:** The actual start date and time of the issue was 2024-12-04 at 22:47 UTC.

* * *

A security issue was introduced on 2024-12-08 at 13:44 UTC and resolved on 2025-01-04 at 04:00 UTC. This security issue impacted resources in VPCs with GKE Multi-Cluster Gateway (MCG) configured. MCG is an optional feature that is used by a small subset of GKE customers. We are individually notifying customers who had the feature enabled during that time period. Multi-Cluster Gateway (MCG) is a GKE feature that allows customers to load balance traffic across multiple clusters. To perform that function, MCG needs to make changes to the project-level Google Cloud firewall. An error inside MCG resulted in the creation of an ingress firewall rule that allowed TCP traffic to all IPs (0.0.0.0/0) and ports inside the VPC. Steps have been taken to prevent errors of this type in the future. As the firewall is a VPC-level allow list, the following types of resources might have been network reachable during the time period:

  * Customer applications running on GKE worker nodes accessible through public IPs.
  * Customer applications running on Compute Engine virtual machines (VMs) with public IPs.
  * Any other Google Cloud resources in the same VPC as the cluster with public IPs and listening ports.

GKE worker nodes, Compute Engine VMs, and other resources that were only using private IPs might have been more broadly accessible within their VPC, but they would not have been accessible to the Internet. Applications protected by the following mechanisms would've reduced or eliminated their exposure:

  * Equal or higher priority `DENY` firewall rules (MCG sets firewall rules priority to 1000 by default)
  * Service mesh using identity-based authorization
  * Application-level authorization



#### Affected resources

**2025-01-23 Update:** GKE fleets (or hubs) using MCG in shared VPC service projects are not affected by the issue as firewall rules are not managed from shared VPC service projects.

* * *

Resources residing in VPCs with GKE MCG configured and listening on public IPs were affected. The resources affected include, but are not limited to, applications running on GKE worker nodes.

#### What should I do?

The issue has been resolved across all impacted VPCs by fixing the incorrect firewall configuration. The rules created in error have been automatically modified with the appropriate source ranges (130.211.0.0/22, 35.191.0.0/16) to allow the ingress traffic coming from Google Cloud health check infrastructure, and, optionally, your proxy-only subnet ranges for Internal Gateways. To know more about the firewall rules automatically created by MCG in your project(s), see [GKE Gateway firewall rules.](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules#gateway-fws) You can, optionally, confirm resolution by checking the managed firewall rules on VPCs using GKE MCG. Confirm a source range is set on managed firewall rules that use the prefix `gkemcg1-l7-`. Inspect these rules and confirm a source range is set. To list the MCG managed firewall rules in your current environment, run the following command:
    
    
    gcloud compute firewall-rules list --format="json" --filter="name:gkemcg1-l7-*" | jq -r '.[] | "\(.name): \(.sourceRanges // "No source range")"' | awk -F: '{if ($2 ~ /No source range|^\s*$/) print "Rule "$1" has an EMPTY or MISSING source range."; else print "Rule "$1" has source range(s): "$2;}'

To search logs for updates to MCG managed firewall configurations, use the [Logs Explorer](https://console.cloud.google.com/logs/query) with the below query:
    
    
    protoPayload.serviceName="compute.googleapis.com"
              resource.type="gce_firewall_rule"
              protoPayload.resourceName=~"projects/[^/]+/global/firewalls/gkemcg1-"
              -operation.last="true"

To list the MCG managed firewall rules across your organization, run the following command to query Cloud Asset Inventory:
    
    
    gcloud asset search-all-resources
              --scope='organizations/'
              --asset-types='compute.googleapis.com/Firewall'
              --query 'name: //compute.googleapis.com/projects/*/*/firewalls/gkemcg*'

The following additional controls provide defense in depth against untrusted networks and can be considered to strengthen security posture:

  * Use [private GKE nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#enable-private-nodes-cluster) to ensure your nodes only get private IPs.
  * Use [explicit `DENY` firewall policies](https://docs.cloud.google.com/firewall/docs/network-firewall-policy-examples#deny-all-external-connections-except-to-specific-ports) where possible.
  * Use [hierarchical firewall policy](https://docs.cloud.google.com/firewall/docs/firewall-policies-examples#example_2_deny_all_external_connections_except_to_certain_ports) to override VPC level firewall configurations.
  * Use [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs) to provide authentication and authorization.
  * Use in-application authentication and authorization.
  * Use [Organization Policy Service](https://docs.cloud.google.com/firewall/docs/custom-constraints) to block firewall rules that allow all traffic. To do so, create a [constraint for denying all traffic firewall rules](https://github.com/GoogleCloudPlatform/gke-policy-library/blob/main/gke-custom-org-policy/samples/disable_allow_all_traffic_firewals.yaml), and apply it with a policy.

We recommend reviewing configurations and logs to identify any applications or services that might have been exposed during the previously mentioned time period that should not have been exposed. You can use the following tools to check inbound traffic to your resources running in Google Cloud:

  * [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/access-flow-logs#flow-logs-queries) for visibility into network throughput and performance
  * [Cloud Logging](https://docs.cloud.google.com/logging/docs) to search and analyze logging data and events from Google Cloud services and applications configured to send logs
  * [Firewall Rules Logging](https://docs.cloud.google.com/firewall/docs/firewall-rules-logging) to audit, verify, and analyze the effects of your firewall rules
  * [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings) for visibility into security findings indicating suspicious network activity
  * Your application logs

| High  
  
### GDC (VMware)

Description | Severity  
---|---  
A security issue was discovered that impacts Multi-Cluster Gateway (MCG), a GKE feature that allows customers to load balance traffic across multiple clusters. GDC (VMware) clusters do not support MCG and are not affected.

#### What should I do?

No action required. | None  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSA security issue was discovered that impacts Multi-Cluster Gateway (MCG), a GKE feature that allows customers to load balance traffic across multiple clusters. GKE on AWS clusters do not support MCG and are not affected.

#### What should I do?

No action required. | None  
  
### GKE on Azure

Description | Severity  
---|---  
A security issue was discovered that impacts Multi-Cluster Gateway (MCG), a GKE feature that allows customers to load balance traffic across multiple clusters. GKE on Azure clusters do not support MCG and are not affected.

#### What should I do?

No action required. | None  
  
### GDC (bare metal)

Description | Severity  
---|---  
A security issue was discovered that impacts Multi-Cluster Gateway (MCG), a GKE feature that allows customers to load balance traffic across multiple clusters. GDC (bare metal) clusters do not support MCG and are not affected.

#### What should I do?

No action required. | None  
  
## GCP-2024-062

**Published:** 2024-12-02  
**Updated:** 2025-01-22  
**Reference:** [CVE-2024-46800](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46800)

**2025-01-22 Update:** Added patch versions for GDC (VMware). Updated GDC (VMware) severity from Pending to High.

**2024-12-12 Update:** Added patch versions for Ubuntu node pools on GKE.

### GKE

**Updated:** 2024-12-12

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-46800

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2024-12-12 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.28.15-gke.1342000
  * 1.29.10-gke.1280000
  * 1.30.6-gke.1596000
  * 1.31.3-gke.1023000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.27.16-gke.1576000
  * 1.28.14-gke.1217000
  * 1.29.9-gke.1496000
  * 1.30.5-gke.1355000
  * 1.31.1-gke.1678000

**Note:** Patched Ubuntu versions will be released soon. You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2025-01-22

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-46800



#### What should I do?

**2025-01-22 Update:** The following versions of GDC (VMware) are updated with code to fix this vulnerability. Upgrade your GDC (VMware) clusters to the following versions or later:

  * 1.29.900-gke.181
  * 1.31.0-gke.889
  * 1.30.400-gke.133



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | High  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-46800



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-46800



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-46800



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2024-061

**Published:** 2024-11-25  
**Reference:**[CVE-2024-10220](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-10220)

### GKE

Description | Severity  
---|---  
A security issue discovered in Kubernetes clusters could result in remote code execution using a `gitRepo` volume. If the git repository is maliciously constructed, a user with the ability to create a Pod and associate a `gitRepo` volume could execute arbitrary commands beyond the container boundary. 

#### What should I do?

Upgrade your GKE cluster and node pools to a patched version. The following GKE versions have been updated to fix this vulnerability: 

  * 1.27.16-gke.1008000
  * 1.28.12-gke.1052000
  * 1.29.7-gke.1008000
  * 1.30.3-gke.1225000
  * 1.31.0-gke.1058000

For security purposes, even with node auto-upgrade enabled, we recommend [manually upgrading](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) your cluster and node pools to a patched GKE version. GKE [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions) allow you to patch without having to unsubscribe or change release channels. This lets you secure your cluster and nodes before the new version becomes the default on your selected release channel. 

#### What vulnerabilities are addressed by this patch?

CVE-2024-10220 allows an attacker to create a Pod and associate a `gitRepo` volume to execute arbitrary commands beyond the container boundary.  | High  
  
### GDC (VMware)

Description | Severity  
---|---  
A security issue discovered in Kubernetes clusters could result in remote code execution using a `gitRepo` volume. If the git repository is maliciously constructed, a user with the ability to create a Pod and associate a `gitRepo` volume could execute arbitrary commands beyond the container boundary. 

#### What should I do?

**Note:** Patched versions of GDC (VMware) will be released soon. This security bulletin will be updated when new GDC (VMware) versions are available. | High  
  
### GKE on AWS

Description | Severity  
---|---  
A security issue discovered in Kubernetes clusters could result in remote code execution using a `gitRepo` volume. If the git repository is maliciously constructed, a user with the ability to create a Pod and associate a `gitRepo` volume could execute arbitrary commands beyond the container boundary.

#### What should I do?

**Note:** Patched versions of GKE on AWS will be released soon. This security bulletin will be updated when new GKE on AWS versions are available. | High  
  
### GKE on Azure

Description | Severity  
---|---  
A security issue discovered in Kubernetes clusters could result in remote code execution using a `gitRepo` volume. If the git repository is maliciously constructed, a user with the ability to create a Pod and associate a `gitRepo` volume could execute arbitrary commands beyond the container boundary.

#### What should I do?

**Note:** Patched versions of GKE on Azure will be released soon. This security bulletin will be updated when new GKE on Azure versions are available. | High  
  
### GDC (bare metal)

Description | Severity  
---|---  
A security issue discovered in Kubernetes clusters could result in remote code execution using a `gitRepo` volume. If the git repository is maliciously constructed, a user with the ability to create a Pod and associate a `gitRepo` volume could execute arbitrary commands beyond the container boundary.

#### What should I do?

**Note:** Patched versions of GDC (bare metal) will be released soon. This security bulletin will be updated when new GDC (bare metal) versions are available. | High  
  
## GCP-2024-057

**Published:** 2024-10-03  
**Updated:** 2024-11-19  
**Reference:** [CVE-2024-45016](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45016)

**2024-11-19 Update:** Added patch versions for Ubuntu node pools on GKE.

**2024-10-15 Update:** Added patch versions for GDC (VMware). Updated GDC (VMware) severity from Pending to Medium. Updated GKE severity from High to Medium.

### GKE

**Updated:** 2024-11-19

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-45016

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2024-11-19 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.27.16-gke.1784000
  * 1.28.15-gke.1080000
  * 1.29.10-gke.1155000
  * 1.30.6-gke.1059000
  * 1.31.2-gke.1354000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.27.16-gke.1478000
  * 1.28.14-gke.1099000
  * 1.29.9-gke.1177000
  * 1.30.5-gke.1145000

**Note:** Patched Ubuntu versions will be released soon. You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | Medium  
  
### GDC (VMware)

**Updated:** 2024-10-15

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-45016



#### What should I do?

**2024-10-15 Update:** The following versions of GDC (VMware) are updated with code to fix this vulnerability. Upgrade your GDC (VMware) clusters to the following versions or later:

  * 1.30.100-gke.96
  * 1.29.600-gke.109
  * 1.28.1000-gke.59



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Medium  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-45016



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-45016



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-45016



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2024-056

**Published:** 2024-09-27  
**Reference:**[CVE-2024-47076](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-47076), [CVE-2024-47175](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-47175), [CVE-2024-47176](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-47176), [CVE-2024-47177](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-47177)

### GKE

Description | Severity  
---|---  
A vulnerability chain (CVE-2024-47076, CVE-2024-47175, CVE-2024-47176, CVE-2024-47177) that could result in remote code execution was discovered in the CUPS printing system used by some Linux distributions. An attacker can exploit this vulnerability if the CUPS services are listening on UDP port 631 and they can connect to it.  GKE does not use the CUPS printing system and is not affected.

#### What should I do?

No action required | None  
  
### GDC (VMware)

Description | Severity  
---|---  
A vulnerability chain (CVE-2024-47076, CVE-2024-47175, CVE-2024-47176, CVE-2024-47177) that could result in remote code execution was discovered in the CUPS printing system used by some Linux distributions. An attacker can exploit this vulnerability if the CUPS services are listening on UDP port 631 and they can connect to it.  GDC software for VMware does not use the CUPS printing system and is not affected.

#### What should I do?

No action required | None  
  
### GKE on AWS

Description | Severity  
---|---  
A vulnerability chain (CVE-2024-47076, CVE-2024-47175, CVE-2024-47176, CVE-2024-47177) that could result in remote code execution was discovered in the CUPS printing system used by some Linux distributions. An attacker can exploit this vulnerability if the CUPS services are listening on UDP port 631 and they can connect to it.  GKE on AWS does not use the CUPS printing system and is not affected.

#### What should I do?

No action required | None  
  
### GKE on Azure

Description | Severity  
---|---  
A vulnerability chain (CVE-2024-47076, CVE-2024-47175, CVE-2024-47176, CVE-2024-47177) that could result in remote code execution was discovered in the CUPS printing system used by some Linux distributions. An attacker can exploit this vulnerability if the CUPS services are listening on UDP port 631 and they can connect to it.  GKE on Azure does not use the CUPS printing system and is not affected.

#### What should I do?

No action required | None  
  
### GDC (bare metal)

Description | Severity  
---|---  
A vulnerability chain (CVE-2024-47076, CVE-2024-47175, CVE-2024-47176, CVE-2024-47177) that could result in remote code execution was discovered in the CUPS printing system used by some Linux distributions. An attacker can exploit this vulnerability if the CUPS services are listening on UDP port 631 and they can connect to it.  GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution.

#### What should I do?

No action required | None  
  
## GCP-2024-054

**Published:** 2024-09-23  
**Reference:**[CVE-2024-5321](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-5321)

### GKE

Description | Severity  
---|---  
A security issue was discovered in Kubernetes clusters with Windows nodes where `BUILTIN\Users` may be able to read container logs and `AUTHORITY\Authenticated` Users may be able to modify container logs.  Any Kubernetes environment with Windows nodes is affected. Run `kubectl get nodes -l kubernetes.io/os=windows` to see if any Windows nodes are in use. 

#### Affected GKE versions

  * 1.27.15 and earlier
  * 1.28.11 and earlier
  * 1.29.6 and earlier
  * 1.30.2 and earlier



#### What should I do?

The following versions of GKE have been updated to fix this vulnerability. For security purposes, even if you have node auto-upgrade enabled, we recommend that you [manually upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your cluster and node pools to one of the following GKE versions or later:

  * 1.27.16-gke.1008000
  * 1.28.12-gke.1052000
  * 1.29.7-gke.1008000
  * 1.30.3-gke.1225000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). 

#### What vulnerabilities are being addressed?

CVE-2024-5321 | Medium  
  
### GDC (VMware)

Description | Severity  
---|---  
A security issue was discovered in Kubernetes clusters with Windows nodes where `BUILTIN\Users` may be able to read container logs and `AUTHORITY\Authenticated` Users may be able to modify container logs.  Any Kubernetes environment with Windows nodes is affected. Run `kubectl get nodes -l kubernetes.io/os=windows` to see if any Windows nodes are in use. 

#### What should I do?

Patch versions for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. 

#### What vulnerabilities are being addressed?

CVE-2024-5321 | Medium  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSA security issue was discovered in Kubernetes clusters with Windows nodes where `BUILTIN\Users` may be able to read container logs and `AUTHORITY\Authenticated` Users may be able to modify container logs.  GKE on AWS clusters do not support Windows nodes and are not affected.

#### What should I do?

No action required | None  
  
### GKE on Azure

Description | Severity  
---|---  
A security issue was discovered in Kubernetes clusters with Windows nodes where `BUILTIN\Users` may be able to read container logs and `AUTHORITY\Authenticated` Users may be able to modify container logs.  GKE on Azure clusters do not support Windows nodes and are not affected.

#### What should I do?

No action required | None  
  
### GDC (bare metal)

Description | Severity  
---|---  
A security issue was discovered in Kubernetes clusters with Windows nodes where `BUILTIN\Users` may be able to read container logs and `AUTHORITY\Authenticated` Users may be able to modify container logs.  GDC software for bare metal clusters do not support Windows nodes and are not affected.

#### What should I do?

No action required | None  
  
## GCP-2024-050

**Published:** 2024-09-04  
**Reference:**[CVE-2024-38063](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-38063)

### GKE

Description | Severity  
---|---  
A new remote code execution vulnerability (CVE-2024-38063) has been discovered in Windows. An attacker could remotely exploit this vulnerability by sending specially crafted IPv6 packets to a host. 

#### What should I do?

GKE does not support IPv6 on windows and is not affected by this CVE. No action is required.  | None  
  
### GDC (VMware)

Description | Severity  
---|---  
A new remote code execution vulnerability (CVE-2024-38063) has been discovered in Windows. An attacker could remotely exploit this vulnerability by sending specially crafted IPv6 packets to a host.

#### What should I do?

GDC software for VMware does not support IPv6 on windows and is not affected by this CVE. No action is required. | None  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSA new remote code execution vulnerability (CVE-2024-38063) has been discovered in Windows. An attacker could remotely exploit this vulnerability by sending specially crafted IPv6 packets to a host.

#### What should I do?

GKE on AWS is not affected by this CVE. No action is required.  | None  
  
### GKE on Azure

Description | Severity  
---|---  
A new remote code execution vulnerability (CVE-2024-38063) has been discovered in Windows. An attacker could remotely exploit this vulnerability by sending specially crafted IPv6 packets to a host.

#### What should I do?

GKE on Azure is not affected by this CVE. No action is required. | None  
  
### GDC (bare metal)

Description | Severity  
---|---  
A new remote code execution vulnerability (CVE-2024-38063) has been discovered in Windows. An attacker could remotely exploit this vulnerability by sending specially crafted IPv6 packets to a host.

#### What should I do?

GDC (bare metal) isn't affected by this CVE. No action is required.  | None  
  
## GCP-2024-049

**Published:** 2024-08-21  
**Updated:** 2024-11-01  
**Reference:** [CVE-2024-36978](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36978)

**2024-11-01 Update:** Added patch versions for Ubuntu node pools on GKE.

**2024-10-21 Update:** Added patch versions and updated Severity for GDC (VMware).

### GKE

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-36978

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2024-11-01 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.27.16-gke.1576000
  * 1.28.14-gke.1175000
  * 1.29.9-gke.1341000
  * 1.30.5-gke.1355000
  * 1.31.1-gke.1678000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.27.16-gke.1008000
  * 1.28.12-gke.1052000
  * 1.29.7-gke.1008000
  * 1.30.3-gke.1225000
  * 1.31.0-gke.1058000

**Note:** Patched Ubuntu versions will be released soon. You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2024-10-21

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-36978



#### What should I do?

**2024-10-21 Update:** The following versions of GDC software for VMware are updated with code to fix this vulnerability. Upgrade your GDC software for VMware clusters to the following versions or later: 

  * 1.28.1100-gke.91
  * 1.30.200-gke.101
  * 1.29.600-gke.109



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | High  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-36978



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-36978



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-36978



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2024-048

**Published:** 2024-08-20  
**Updated:** 2024-10-30  
**Reference:** [CVE-2024-41009](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41009)

**2024-10-30 Update:** Added patch versions for Ubuntu node pools on GKE.

**2024-10-25 Update:** Added patch versions and updated Severity for GDC (VMware).

### GKE

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-41009

GKE Standard and Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2024-10-30 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.27.16-gke.1576000
  * 1.28.14-gke.1175000
  * 1.29.9-gke.1341000
  * 1.30.5-gke.1355000
  * 1.31.1-gke.1678000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.27.16-gke.1008000
  * 1.28.12-gke.1052000
  * 1.29.7-gke.1008000
  * 1.30.3-gke.1225000
  * 1.31.0-gke.1058000

**Note:** Patched Ubuntu versions will be released soon. You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2024-10-25

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-41009



#### What should I do?

**2024-10-25 Update:** The following versions of GDC software for VMware are updated with code to fix this vulnerability. Upgrade your GDC software for VMware clusters to the following versions or later: 

  * 1.29.700-gke.110
  * 1.28.1100-gke.91
  * 1.30.200-gke.101



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | High  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-41009



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-41009



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-41009



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2024-047

**Published:** 2024-08-19  
**Updated:** 2024-10-30  
**Reference:** [CVE-2024-39503](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39503)

**2024-10-30 Update:** Added patch versions for Ubuntu node pools on GKE.

**2024-10-21 Update:** Added patch versions and updated Severity for GDC (VMware).

### GKE

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-39503

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2024-10-30 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.27.16-gke.1576000
  * 1.28.14-gke.1175000
  * 1.29.9-gke.1341000
  * 1.30.5-gke.1355000
  * 1.31.1-gke.1678000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.27.15-gke.1125000
  * 1.28.11-gke.1170000
  * 1.29.6-gke.1137000
  * 1.30.3-gke.1225000

**Note:** Patched Ubuntu versions will be released soon. You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2024-10-21

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-39503



#### What should I do?

**2024-10-21 Update:** The following versions of GDC software for VMware are updated with code to fix this vulnerability. Upgrade your GDC software for VMware clusters to the following versions or later: 

  * 1.30.200-gke.101
  * 1.29.600-gke.109
  * 1.28.1100-gke.91



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | High  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-39503



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-39503



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-39503



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2024-045

**Published:** 2024-07-17  
**Updated:** 2024-09-19  
**Reference:** [CVE-2024-26925](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26925)

**2024-09-19 Update:** Added patch versions for GDC (VMware).

**2024-08-21 Update:** Added patch versions for Ubuntu node pools on GKE.

### GKE

**Updated:** 2024-08-21

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26925

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2024-08-21 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.27.16-gke.1051000
  * 1.28.12-gke.1052000
  * 1.29.7-gke.1174000
  * 1.30.3-gke.1225000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.27.14-gke.1093000
  * 1.28.10-gke.1141000
  * 1.29.5-gke.1192000
  * 1.30.2-gke.1394000

**Note:** Patched Ubuntu versions will be released soon. You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2024-09-19

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26925



#### What should I do?

**2024-09-19 Update:** The following versions of GDC software for VMware are updated with code to fix this vulnerability. Upgrade your GDC software for VMware clusters to the following versions or later: 

  * 1.29.400
  * 1.28.900



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26925



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26925



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26925



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2024-044

**Published:** 2024-07-16  
**Updated:** 2024-10-30  
**Reference:** [CVE-2024-36972](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36972)

**2024-10-30 Update:** Added patch versions for Ubuntu node pools on GKE.

**2024-10-21 Update:** Added patch versions and updated Severity for GDC (VMware).

### GKE

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-36972

GKE Standard and Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2024-10-30 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.27.16-gke.1576000
  * 1.28.14-gke.1175000
  * 1.29.9-gke.1341000
  * 1.30.5-gke.1355000
  * 1.31.1-gke.1678000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.27.14-gke.1093000
  * 1.28.10-gke.1141000
  * 1.29.5-gke.1192000
  * 1.30.2-gke.1394000

**Note:** Patched Ubuntu versions will be released soon. You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2024-10-21

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-36972



#### What should I do?

**2024-10-21 Update:** The following versions of GDC software for VMware are updated with code to fix this vulnerability. Upgrade your GDC software for VMware clusters to the following versions or later: 

  * 1.30.200-gke.101
  * 1.29.600-gke.109
  * 1.28.1100-gke.91



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | High  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-36972



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-36972



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-36972



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2024-043

**Published:** 2024-07-16  
**Updated:** 2024-10-02  
**Reference:** [CVE-2024-26921](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26921)

**2024-10-02 Update:** Added patch versions for Ubuntu node pools on GKE.

**2024-09-20 Update:** Added patch versions for GDC (VMware).

### GKE

**Updated:** 2024-10-02

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26921

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2024-10-02 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later: 

  * 1.27.16-gke.1287000
  * 1.28.13-gke.1042000
  * 1.29.8-gke.1096000
  * 1.30.4-gke.1476000
  * 1.30.4-gke.1476000
  * 1.31.0-gke.1577000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.26.15-gke.1360000
  * 1.27.14-gke.1022000
  * 1.28.9-gke.1209000
  * 1.29.4-gke.1542000
  * 1.30.2-gke.1394000

**Note:** Patched Ubuntu versions will be released soon. You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2024-09-20

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26921



#### What should I do?

**2024-09-20 Update:** The following versions of GDC software for VMware are updated with code to fix this vulnerability. Upgrade your GDC software for VMware clusters to the following versions or later: 

  * 1.30.200
  * 1.29.500
  * 1.28.1000



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26921



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26921



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26921



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2024-042

**Published:** 2024-07-15  
**Updated:** 2024-07-18  
**Reference:** [CVE-2024-26809](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26809)

**2024-07-18 Update:** Clarified that Autopilot clusters in the default configuration aren't impacted.

### GKE

**Updated:** 2024-07-18

Description | Severity  
---|---  
**2024-07-18 Update:** The original version of this bulletin incorrectly stated that Autopilot clusters were impacted. Autopilot clusters in the default configuration _aren't impacted_ , but might be vulnerable if you explicitly set the seccomp Unconfined profile or allow the `CAP_NET_ADMIN` capability.

* * *

The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26809

GKE Standard and Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.27.13-gke.1166000
  * 1.28.9-gke.1209000
  * 1.29.4-gke.1542000

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Ubuntu node pools to one of the following patch versions or later:

  * 1.26.15-gke.1469000
  * 1.27.14-gke.1100000
  * 1.28.10-gke.1148000
  * 1.29.6-gke.1038000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26809



#### What should I do?

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26809



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26809



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26809



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2024-041

**Published:** 2024-07-08  
**Updated:** 2024-09-16  
**Reference:** [CVE-2023-52654](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52654), [CVE-2023-52656](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52656)

**2024-09-16 Update:** Added patch versions for GDC (VMware).

**2024-07-19 Update:** Added patch versions for Ubuntu node pools on GKE.

### GKE

**Updated:** 2024-07-19

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2023-52654
  * CVE-2023-52656

GKE Standard and Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2024-07-19 Update:** The following versions of GKE contain code to fix this vulnerability on Ubuntu. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Ubuntu node pools to one of the following patch versions or later:

  * 1.26.15-gke.1469000
  * 1.27.14-gke.1100000
  * 1.28.10-gke.1148000
  * 1.29.6-gke.1038000
  * 1.30.2-gke.1394000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.26.15-gke.1300000
  * 1.27.13-gke.1166000
  * 1.28.9-gke.1209000
  * 1.29.4-gke.1542000

**Note:** Patched Ubuntu versions will be released soon. You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2024-09-16

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2023-52654
  * CVE-2023-52656



#### What should I do?

**2024-09-16 Update:** The following versions of GDC software for VMware are updated with code to fix this vulnerability. Upgrade your GDC software for VMware clusters to the following versions or later: 

  * 1.29.200
  * 1.28.700
  * 1.16.11



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2023-52654
  * CVE-2023-52656



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2023-52654
  * CVE-2023-52656



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2023-52654
  * CVE-2023-52656



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2024-040

**Published:** 2024-07-01  
**Updated:** 2024-07-11  
**Reference:** [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387)

**2024-07-11 Update:** Added patch versions for GDC software for VMware, GKE on AWS, and GKE on Azure.

**2024-07-03 Update:** Added patch versions for GKE

**2024-07-02 Updates:**

  * Clarified that Autopilot clusters are impacted and will require user action.
  * Added impact assessments and mitigation steps for GDC (VMware), GKE on AWS, and GKE on Azure.
  * Corrected the GDC (bare metal) security bulletin to clarify that GDC (bare metal) isn't directly affected and that customers should check with OS vendors for patches.



### GKE

**Updated:** 2024-07-03

Description | Severity  
---|---  
**2024-07-03 Update:** An expedited rollout is in progress and is expected to make new patch versions available across all zones by July 3, 2024 at 5 PM US and Canadian Pacific Daylight Time (UTC-7). To get a notification as soon as a patch is available for your specific cluster, use [cluster notifications](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications#overview).

* * *

**2024-07-02 Update:** This vulnerability affects both Autopilot mode and Standard mode clusters. Each section that follows will tell you the modes to which that section applies.

* * *

A remote code execution vulnerability, [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387), was recently discovered in OpenSSH. The vulnerability exploits a race condition that could be used to obtain access to a remote shell, enabling attackers to gain root access to GKE nodes. At the time of publication, exploitation is believed to be difficult and take several hours per machine being attacked. We are not aware of any exploitation attempts. All supported versions of Container Optimized OS and Ubuntu images on GKE run versions of OpenSSH that are vulnerable to this issue. GKE clusters with public node IP addresses and SSH exposed to the Internet should be treated with the highest priority for mitigation. The GKE control plane is not vulnerable to this issue.

#### What should I do?

##### **2024-07-03 Update: Patch versions for GKE**

An expedited rollout is in progress and is expected to make new patch versions available across all zones by July 3, 2024 at 5 PM US and Canadian Pacific Daylight Time (UTC-7). Clusters and nodes with autoupgrade enabled will begin upgrading as the week progresses, but due to the severity of the vulnerability we recommend upgrading manually as follows to get patches as fast as possible. For both Autopilot and Standard clusters, [upgrade your control plane](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrade_cp) to a patched version. Additionally, for Standard mode clusters, [upgrade your node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrade_nodes) to a patched version. Autopilot clusters will begin upgrading your nodes to match the control plane version [as soon as possible](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades-autopilot#manual-upgrade). Patched GKE versions are available for every supported version to minimize the changes necessary to apply the patch. The version number of each new version is an increment on the final digit in the version number of a corresponding existing version. For example, if you are on 1.27.14-gke.1100000, you will upgrade to 1.27.14-gke.1100002 to get the fix with the smallest possible change. The following patched GKE versions are available:

  * 1.26.15-gke.1090004
  * 1.26.15-gke.1191001
  * 1.26.15-gke.1300001
  * 1.26.15-gke.1320002
  * 1.26.15-gke.1381001
  * 1.26.15-gke.1390001
  * 1.26.15-gke.1404002
  * 1.26.15-gke.1469001
  * 1.27.13-gke.1070002
  * 1.27.13-gke.1166001
  * 1.27.13-gke.1201002
  * 1.27.14-gke.1022001
  * 1.27.14-gke.1042001
  * 1.27.14-gke.1059002
  * 1.27.14-gke.1100002
  * 1.27.15-gke.1012003
  * 1.28.9-gke.1069002
  * 1.28.9-gke.1209001
  * 1.28.9-gke.1289002
  * 1.28.10-gke.1058001
  * 1.28.10-gke.1075001
  * 1.28.10-gke.1089002
  * 1.28.10-gke.1148001
  * 1.28.11-gke.1019001
  * 1.29.4-gke.1043004
  * 1.29.5-gke.1060001
  * 1.29.5-gke.1091002
  * 1.29.6-gke.1038001
  * 1.30.1-gke.1329003
  * 1.30.2-gke.1023004

To check whether a patch is available in your cluster zone or region, run the following command:
    
    
    gcloud container get-server-config --location=LOCATION

Replace `LOCATION` with your zone or region.

* * *

**2024-07-02 Update:** Both Autopilot mode and Standard mode clusters should be upgraded as soon as possible after patch versions are available.

* * *

A patched GKE version that includes an updated OpenSSH will be made available as soon as possible. This bulletin will be updated when patches are available. To receive a Pub/Sub notification when a patch is available for your channel, [enable cluster notifications](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications#overview). We recommend working through the following steps to check your cluster's exposure, and applying the mitigations described, as necessary.

#### Determine whether your nodes have public IP addresses

**2024-07-02 Update:** This section applies to both Autopilot and Standard clusters.

* * *

If a cluster is created with [`enable-private-nodes`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-private-nodes), nodes will be private, which mitigates the vulnerability by removing exposure to the Internet. Run the following command to determine if your cluster has private nodes enabled: 
    
    
    gcloud container clusters describe $CLUSTER_NAME \
    --format="value(privateClusterConfig.enablePrivateNodes)"

If the return value is True, all nodes are private nodes for this cluster and the vulnerability is mitigated. If the value is empty or false, continue on to apply one of the mitigations in the following sections. To find all clusters originally created with public nodes, use this [Cloud Asset Inventory query](https://docs.cloud.google.com/asset-inventory/docs/query-assets) in the project or organization:
    
    
    SELECT
      resource.data.name AS cluster_name,
      resource.parent AS project_name,
      resource.data.privateClusterConfig.enablePrivateNodes
    FROM
      `container_googleapis_com_Cluster`
    WHERE
      resource.data.privateClusterConfig.enablePrivateNodes is null OR
      resource.data.privateClusterConfig.enablePrivateNodes = false

#### Disallow SSH to the cluster nodes

**2024-07-02 Update:** This section applies to both Autopilot and Standard clusters.

* * *

The default network is pre-populated with a `default-allow-ssh` firewall rule to allow SSH access from the public Internet. To remove this access, you can: 

  * Optionally [create rules](https://docs.cloud.google.com/firewall/docs/using-firewalls#creating_firewall_rules) to allow any SSH access you need from trusted networks to GKE nodes or other Compute Engine VMs in the project.
  * Disable the default firewall rule with the following command:  
`gcloud compute firewall-rules update default-allow-ssh --disabled --project=$PROJECT`

If you have created any other firewall rules that may allow SSH through TCP on port 22, disable them, or limit the source IPs to trusted networks.  Verify that you can no longer [SSH to the cluster nodes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ssh-cluster-node) from the Internet. This firewall configuration mitigates the vulnerability.

#### Convert public node pools to private

**2024-07-02 Update:** For Autopilot clusters originally created as public clusters, you can place your workloads on private nodes [by using nodeSelectors](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/change-cluster-isolation#isolate_node_pool). However, Autopilot nodes that run system workloads on clusters that were originally created as public clusters will still be public nodes and should be protected by using the firewall changes described in the preceding section.

* * *

To best protect clusters originally created with public nodes, we recommend first disallowing SSH through the firewall as already described. If you are not able to disallow SSH through the firewall rules, you can convert public node pools on GKE Standard clusters to private by [following this guidance to isolate node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/change-cluster-isolation#isolate_node_pool).

#### Change SSHD configuration

**2024-07-02 Update:** This section only applies to Standard clusters. Autopilot workloads aren't allowed to modify node configuration.

* * *

If none of these mitigations can be applied, we have also [published a daemonset](https://github.com/GoogleCloudPlatform/k8s-node-tools/tree/master/ssh-server-config) that sets SSHD `LoginGraceTime` to zero, and restarts the SSH daemon. This daemonset can be applied to the cluster to mitigate the attack. Note that this configuration may increase the risk of denial of service attacks and may cause issues with legitimate SSH access. This daemonset should be removed after a patch has been applied. | Critical  
  
### GDC (VMware)

**Updated:** 2024-07-11

Description | Severity  
---|---  
**2024-07-11 Update:** The following versions of GDC software for VMware have been updated with code to fix this vulnerability. Upgrade your admin workstation, admin clusters, and user clusters (including node pools) to one of the following versions or later. For instructions, see [Upgrade a cluster or node pool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading).

  * 1.16.10-gke.36
  * 1.28.700-gke.151
  * 1.29.200-gke.245

The 2024-07-02 update to this bulletin incorrectly stated that all supported versions of Ubuntu images on GDC software for VMware run versions of OpenSSH that are vulnerable to this issue. Ubuntu images on GDC software for VMware version 1.16 clusters run versions of OpenSSH that are _not vulnerable_ to this issue. Ubuntu images in GDC software for VMware 1.28 and 1.29 _are vulnerable_. Container-Optimized OS images on all supported versions of GDC software for VMware are vulnerable to this issue.

* * *

**2024-07-02 Update:** All supported versions of Container-Optimized OS and Ubuntu images on GDC software for VMware run versions of OpenSSH that are vulnerable to this issue. GDC software for VMware clusters with public node IP addresses and SSH exposed to the Internet should be treated with the highest priority for mitigation.

* * *

A remote code execution vulnerability, [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387), was recently discovered in OpenSSH. The vulnerability exploits a race condition that could be used to obtain access to a remote shell, enabling attackers to gain root access to GKE nodes. At the time of publication, exploitation is believed to be difficult and take several hours per machine being attacked. We are not aware of any exploitation attempts.

#### What should I do?

**2024-07-02 Update:** A patched GDC software for VMware version that includes an updated OpenSSH will be made available as soon as possible. This bulletin will be updated when patches are available. We recommend that you apply the following mitigations as necessary.

##### Disallow SSH to the cluster nodes

You can change your infrastructure network setup to disallow SSH connectivity from untrusted sources, such as the public Internet.

##### Change sshd configuration

If you can't apply the preceding mitigation, we have [published a DaemonSet](https://github.com/GoogleCloudPlatform/k8s-node-tools/tree/master/ssh-server-config) that sets the sshd `LoginGraceTime` to zero and restarts the SSH daemon. This DaemonSet can be applied to the cluster to mitigate the attack. Note that this configuration might increase the risk of denial of service attacks and might cause issues with legitimate SSH access. Remove this DaemonSet after a patch has been applied.

* * *

**Note:** Patch versions for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Critical  
  
### GKE on AWS

**Updated:** 2024-07-11

Description | Severity  
---|---  
**2024-07-11 Update:** The following versions of GKE on AWS have been updated with code to fix this vulnerability: 

  * 1.27.14-gke.1200
  * 1.28.10-gke.1300
  * 1.29.5-gke.1100

Upgrade your GKE on AWS control plane and node pools to one of these patched versions or later. For instructions, see [Upgrade your AWS cluster version](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/upgrade-cluster) and [Update a node pool](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/update-node-pool).

* * *

**2024-07-02 Update:** All supported versions of Ubuntu images on GKE on AWS run versions of OpenSSH that are vulnerable to this issue. GKE on AWS clusters with public node IP addresses and SSH exposed to the Internet should be treated with the highest priority for mitigation.

* * *

A remote code execution vulnerability, [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387), was recently discovered in OpenSSH. The vulnerability exploits a race condition that could be used to obtain access to a remote shell, enabling attackers to gain root access to GKE nodes. At the time of publication, exploitation is believed to be difficult and take several hours per machine being attacked. We are not aware of any exploitation attempts.

#### What should I do?

**2024-07-02 Update:** A patched GKE on AWS version that includes an updated OpenSSH will be made available as soon as possible. This bulletin will be updated when patches are available. We recommend that you work through the following steps to check your cluster's exposure, and apply the described mitigations as necessary.

##### Determine whether your nodes have public IP addresses

GKE on AWS doesn't provision any machine with either public IP addresses or with firewall rules that allow traffic to port 22 by default. However, depending on your [subnet configuration](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-ip-addressing.html#vpc-public-ipv4-addresses), machines can automatically get a public IP address during provisioning. To check whether nodes are provisioned with public IP addresses, [look at the configuration of the subnet](https://docs.aws.amazon.com/vpc/latest/userguide/modify-subnets.html#view-subnet) that's associated with your AWS node pool resource.

##### Disallow SSH to the cluster nodes

Even though GKE on AWS doesn't allow traffic on port 22 on any node by default, customers can attach additional security groups to node pools, enabling inbound SSH traffic. We recommend that you [remove or scope down](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-security-groups.html#updating-security-group-rules) corresponding rules from the provided security groups.

##### Convert public node pools to private

To best protect clusters with public nodes, we recommend first disallowing SSH through your security group, as described in the previous section. If you can't disallow SSH through the security group rules, you can convert public node pools to private by [disabling the option to automatically assign public IPs to machines within a subnet](https://docs.aws.amazon.com/vpc/latest/userguide/modify-subnets.html#subnet-public-ip) and reprovisioning the node pool.

* * *

**Note:** Patch versions for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Critical  
  
### GKE on Azure

**Updated:** 2024-07-11

Description | Severity  
---|---  
**2024-07-11 Update:** The following versions of GKE on Azure have been updated with code to fix this vulnerability: 

  * 1.27.14-gke.1200
  * 1.28.10-gke.1300
  * 1.29.5-gke.1100

Upgrade your GKE on Azure control plane and node pools to one of these patched versions or later. For instructions, see [Upgrade your Azure cluster version](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/upgrade-cluster) and [Update a node pool](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/update-node-pool).

* * *

**2024-07-02 Update:** All supported versions of Ubuntu images on GKE on Azure run versions of OpenSSH that are vulnerable to this issue. GKE on Azure clusters with public node IP addresses and SSH exposed to the Internet should be treated with the highest priority for mitigation.

* * *

A remote code execution vulnerability, [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387), was recently discovered in OpenSSH. The vulnerability exploits a race condition that could be used to obtain access to a remote shell, enabling attackers to gain root access to GKE nodes. At the time of publication, exploitation is believed to be difficult and take several hours per machine being attacked. We are not aware of any exploitation attempts.

#### What should I do?

**2024-07-02 Update:** A patched GKE on Azure version that includes an updated OpenSSH will be made available as soon as possible. This bulletin will be updated when patches are available. We recommend that you work through the following steps to check your cluster's exposure, and apply the described mitigations as necessary.

##### Determine whether your nodes have public IP addresses

GKE on Azure doesn't provision any machine with either [public IP addresses](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses) or with firewall rules that allow traffic to port 22 by default. To review your Azure configuration to check whether there are any public IP addresses configured on your GKE on Azure cluster, run the following command:
    
    
    az network public-ip list -g CLUSTER_RESOURCE_GROUP_NAME -o tsv

##### Disallow SSH to the cluster nodes

Even though GKE on Azure doesn't allow traffic on port 22 on any node by default, customers can update NetworkSecurityGroup rules to node pools, enabling inbound SSH traffic from the public internet. We strongly recommend that you review the Network Security Groups (NSGs) associated with your Kubernetes clusters. If an NSG rule exists that allows unrestricted inbound traffic on port 22 (SSH), do one of the following:

  * **Remove the rule entirely** : If SSH access to the cluster nodes isn't required from the internet, remove the rule to eliminate potential attack vectors.
  * **Scope down the rule** : Restrict inbound access on port 22 to only the specific IP addresses or ranges that require it. This minimizes the exposed surface for potential attacks.



##### Convert public node pools to private

To best protect clusters with public nodes, we recommend first disallowing SSH through your security group, as described in the previous section. If you can't disallow SSH through the security group rules, you can convert public node pools to private by removing the public IP addresses associated with the VMs. To remove a public IP address from a VM and replace it with a private IP address configuration, see [Dissociate a public IP address from a an Azure VM](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/remove-public-ip-address-vm). **Impact:** Any existing connections using the public IP address will be disrupted. Ensure that you have alternative access methods in place, like a VPN or Azure Bastion.

* * *

**Note:** Patch versions for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Critical  
  
### GDC (bare metal)

**Updated:** 2024-07-02

Description | Severity  
---|---  
**2024-07-02 Update:** The original version of this bulletin for GDC software for bare metal incorrectly stated that patch versions were in progress. GDC software for bare metal is not directly affected because it doesn't manage the operating system SSH daemon or configuration. Patch versions are therefore the responsibility of the operating system provider, as described in the **What should I do?** section. 

* * *

A remote code execution vulnerability, [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387), was recently discovered in OpenSSH. The vulnerability exploits a race condition that could be used to obtain access to a remote shell, enabling attackers to gain root access to GKE nodes. At the time of publication, exploitation is believed to be difficult and take several hours per machine being attacked. We are not aware of any exploitation attempts.

#### What should I do?

**2024-07-02 Update:** Contact your OS provider to obtain a patch for the operating systems in use with GDC software for bare metal. Until you've applied the OS vendor patch, ensure that public reachable machines don't allow SSH connections from the internet. If that isn't possible, an alternative is to set the `LoginGraceTime` to zero and restart the sshd server:
    
    
    grep "^LoginGraceTime" /etc/ssh/sshd_config
                LoginGraceTime 0

Note that this configuration change might increase the risk of denial of service attacks and may cause issues with legitimate SSH access.

* * *

**Original 2024-07-01 text (see the preceding 2024-07-02 update for a correction):** **Note:** Patch versions for GDC software for bare metal are in progress. We'll update this bulletin with that information when it's available. | Critical  
  
## GCP-2024-039

**Published:** 2024-06-28  
**Updated:** 2024-09-25  
**Reference:** [CVE-2024-26923](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26923)

**2024-09-25 Update:** Added patch versions for GDC (VMware).

**2024-08-20 Update:** Added patch versions for Ubuntu node pools on GKE.

### GKE

**Updated:** 2024-08-20

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26923

GKE Standard and Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2024-08-20 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.27.16-gke.1051000
  * 1.28.12-gke.1052000
  * 1.29.7-gke.1174000
  * 1.30.3-gke.1225000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.26.15-gke.1360000
  * 1.27.14-gke.1022000
  * 1.28.9-gke.1289000
  * 1.29.5-gke.1010000

**Note:** Patched Ubuntu versions will be released soon. You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2024-09-25

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26923



#### What should I do?

**2024-09-25 Update:** The following versions of GDC software for VMware are updated with code to fix this vulnerability. Upgrade your GDC software for VMware clusters to the following versions or later: 

  * 1.29.400
  * 1.28.900



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26923



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26923



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26923



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2024-038

**Published:** 2024-06-26  
**Updated:** 2024-09-17  
**Reference:** [CVE-2024-26924](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26924)

**2024-09-17 Update:** Added patch versions for GDC (VMware).

**2024-08-06 Update:** Added patch versions for Ubuntu node pools on GKE.

### GKE

**Updated:** 2024-08-06

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26924

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2024-08-06 Update:** Added patch versions for Ubuntu node pools on GKE. The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.27.15-gke.1252000
  * 1.28.11-gke.1260000
  * 1.29.6-gke.1326000
  * 1.30.2-gke.1394003



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.26.15-gke.1360000
  * 1.27.14-gke.1022000
  * 1.28.9-gke.1289000
  * 1.29.5-gke.1010000

**Note:** Patched Ubuntu versions will be released soon. You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GDC (VMware)

**Updated:** 2024-09-17

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26924



#### What should I do?

**2024-09-17 Update:** The following versions of GDC software for VMware are updated with code to fix this vulnerability. Upgrade your GDC software for VMware clusters to the following versions or later: 

  * 1.29.400
  * 1.28.800
  * 1.16.11



* * *

**Note:** Patch versions and a severity assessment for GDC software for VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26924



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26924



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GDC (bare metal)

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26924



#### What should I do?

There is no action required. GDC software for bare metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2024-036

**Published:** 2024-06-18  
**Reference:** [CVE-2024-26584](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26584)

### GKE

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-26584

GKE Standard and Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.28.9-gke.1209000
  * 1.29.4-gke.1542000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GKE on VMware

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-26584



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-26584



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-26584



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-26584



#### What should I do?

There is no action required. GKE on Bare Metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2024-035

**Published:** 2024-06-12  
**Updated:** 2024-07-18  
**Reference:** [CVE-2024-26584](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26584)

**2024-07-18 Update:** Added patch versions for Ubuntu node pools on GKE and added a patch version for version 1.27 on Container-Optimized OS node pools.

### GKE

**Updated:** 2024-07-18

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26584

GKE Standard and Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2024-07-18 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Ubuntu node pools to one of the following patch versions or later:

  * 1.26.15-gke.1469000
  * 1.27.14-gke.1100000
  * 1.28.10-gke.1148000
  * 1.29.6-gke.1038000
  * 1.30.2-gke.1394000

The following version of GKE is updated with code to fix this vulnerability on Container-Optimized OS. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to the following patch version or later:

  * 1.27.15-gke.1125000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.28.9-gke.1209000
  * 1.29.4-gke.1542000

The following minor versions are affected but don't have a patch version available. We'll update this bulletin when patch versions are available:

  * 1.26
  * 1.27

**Note:** Patched Ubuntu versions will be released soon. You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GKE on VMware

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26584



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26584



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26584



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26584



#### What should I do?

There is no action required. GKE on Bare Metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2024-034

**Published:** 2024-06-11  
**Updated:** 2024-07-10  
**Reference:** [CVE-2024-26583](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26583)

**2024-07-10 Update:** Added patch versions for Container-Optimized OS nodes running minor version 1.26 and 1.27 and added patch versions for Ubuntu nodes.

### GKE

**Updated:** 2024-07-10

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-26583

GKE Standard and Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2024-07-10 Update:** The following versions of GKE are updated with code to fix this vulnerability. Upgrade your Ubuntu node pools to one of the following patch versions or later:

  * 1.26.15-gke.1444000
  * 1.27.14-gke.1096000
  * 1.28.10-gke.1148000
  * 1.29.5-gke.1041001
  * 1.30.1-gke.1156001

For minor versions 1.26 and 1.27, upgrade your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.26.15-gke.1404002
  * 1.27.14-gke.1059002



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.28.8-gke.1095000
  * 1.29.3-gke.1093000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GKE on VMware

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-26583



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-26583



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-26583



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2024-26583



#### What should I do?

There is no action required. GKE on Bare Metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2024-033

**Published:** 2024-06-10  
**Updated:** 2024-09-26  
**Reference:** [CVE-2022-23222](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23222)

**2024-09-26 Update:** Added patch versions for GDC (VMware).

### GKE

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2022-23222

GKE Standard and Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.26.15-gke.1381000
  * 1.27.14-gke.1022000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GKE on VMware

**Updated:** 2024-09-26

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2022-23222



#### What should I do?

**2024-09-26 Update:** The following versions of GDC software for VMware are updated with code to fix this vulnerability. Upgrade your GDC software for VMware clusters to the following versions or later: 

  * 1.28.900-gke.113
  * 1.29.400-gke.8



* * *

**Note:** Patch versions and a severity assessment for GKE on VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2022-23222



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2022-23222



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 

  * CVE-2022-23222



#### What should I do?

There is no action required. GKE on Bare Metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2024-031

**Published:** 2024-05-24  
**Reference:**[CVE-2024-4323](https://cve.mitre.org/cgi-bin/cvename.cgi?name=%20CVE-2024-4323)

### GKE

Description | Severity  
---|---  
A new vulnerability (CVE-2024-4323) has been discovered in Fluent Bit that could result in remote code execution. Fluent Bit versions 2.0.7 through 3.0.3 are affected. GKE doesn't use a vulnerable version of Fluent Bit, and is unaffected.

#### What should I do?

GKE isn't affected by this vulnerability. **No action is required.** | None  
  
### GKE on VMware

Description | Severity  
---|---  
A new vulnerability (CVE-2024-4323) has been discovered in Fluent Bit that could result in remote code execution. Fluent Bit versions 2.0.7 through 3.0.3 are affected. GKE on VMware doesn't use a vulnerable version of Fluent Bit, and is unaffected.

#### What should I do?

GKE on VMware isn't affected by this vulnerability. **No action is required.** | None  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSA new vulnerability (CVE-2024-4323) has been discovered in Fluent Bit that could result in remote code execution. Fluent Bit versions 2.0.7 through 3.0.3 are affected. GKE on AWS doesn't use a vulnerable version of Fluent Bit, and is unaffected.

#### What should I do?

GKE on AWS isn't affected by this vulnerability. **No action is required.** | None  
  
### GKE on Azure

Description | Severity  
---|---  
A new vulnerability (CVE-2024-4323) has been discovered in Fluent Bit that could result in remote code execution. Fluent Bit versions 2.0.7 through 3.0.3 are affected. GKE on Azure doesn't use a vulnerable version of Fluent Bit, and is unaffected.

#### What should I do?

GKE on Azure isn't affected by this vulnerability. **No action is required.** | None  
  
### GKE on Bare Metal

Description | Severity  
---|---  
A new vulnerability (CVE-2024-4323) has been discovered in Fluent Bit that could result in remote code execution. Fluent Bit versions 2.0.7 through 3.0.3 are affected. GKE on Bare Metal doesn't use a vulnerable version of Fluent Bit, and is unaffected.

#### What should I do?

GKE on Bare Metal isn't affected by this vulnerability. **No action is required.** | None  
  
## GCP-2024-030

**Published:** 2024-05-15  
**Updated:** 2024-07-18  
**Reference:** [CVE-2023-52620](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52620)

**2024-07-18 Update:** Added patch versions for Ubuntu node pools on GKE.

### GKE

**Updated:** 2024-07-18

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2023-52620

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2024-07-18 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Ubuntu node pools to one of the following patch versions or later:

  * 1.26.15-gke.1469000
  * 1.27.14-gke.1100000
  * 1.28.10-gke.1148000
  * 1.29.6-gke.1038000
  * 1.30.2-gke.1394000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.27.13-gke.1166000
  * 1.28.8-gke.1095000
  * 1.29.3-gke.1093000

**Note:** Patched Ubuntu versions will be released soon. You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GKE on VMware

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2023-52620



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2023-52620



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2023-52620



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2023-52620



#### What should I do?

There is no action required. GKE on Bare Metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2024-029

**Published:** 2024-05-14  
**Updated:** 2024-08-19  
**Reference:** [CVE-2024-26642](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26642)

**2024-08-19 Update:** Added patch versions for Ubuntu nodes.

### GKE

**Updated:** 2024-08-19

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26642

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2024-08-19 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.27.16-gke.1051000
  * 1.28.12-gke.1052000
  * 1.29.7-gke.1174000
  * 1.30.3-gke.1225000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.27.13-gke.1166000
  * 1.28.8-gke.1095000
  * 1.29.3-gke.1093000

**Note:** Patched Ubuntu versions will be released soon. You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GKE on VMware

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26642



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26642



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26642



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26642



#### What should I do?

There is no action required. GKE on Bare Metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2024-028

**Published:** 2024-05-13  
**Updated:** 2024-05-22  
**Reference:** [CVE-2024-26581](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26581)

**2024-05-22 Update:** Added patch versions for Ubuntu nodes.

### GKE

**Updated:** 2024-05-22

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26581

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2024-05-22 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.26.15-gke.1300000
  * 1.27.13-gke.1011000
  * 1.28.9-gke.1209000
  * 1.29.4-gke.1542000
  * 1.30.0-gke.1712000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.25.16-gke.1596000
  * 1.26.14-gke.1076000
  * 1.27.11-gke.1202000
  * 1.28.8-gke.1095000
  * 1.29.3-gke.1093000

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Ubuntu node pools to one of the following patch versions or later:

  * 1.26.15-gke.1300000
  * 1.28.9-gke.1209000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GKE on VMware

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26581



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26581



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26581



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26581



#### What should I do?

There is no action required. GKE on Bare Metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2024-027

**Published:** 2024-05-08  
**Updated:** 2024-09-25  
**Reference:** [CVE-2024-26808](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26808)

**2024-09-25 Update:** Added patch versions for GDC (VMware).

**2024-05-15 Update:** Added patch versions for GKE Ubuntu node pools.

**2024-05-09 Update:** Corrected severity from Medium to High and clarified that GKE Autopilot clusters in the default configuration are not impacted. 

### GKE

**Updated:** 2024-05-09, 2024-05-15

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26808

**2024-05-09 Update** : Corrected severity from Medium to High. The original bulletin stated Autopilot clusters are impacted, but this was incorrect. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp Unconfined profile or [allow `CAP_NET_ADMIN`.](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies)

* * *

GKE Standard and Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2024-05-15 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.26.15-gke.1323000
  * 1.27.13-gke.1206000
  * 1.28.10-gke.1000000
  * 1.29.3-gke.1282004
  * 1.30.0-gke.1584000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.27.8-gke.1067000
  * 1.28.8-gke.1095000
  * 1.29.3-gke.1093000

**Note:** Patched Ubuntu versions will be released soon. You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). |  High   
  
### GKE on VMware

**Updated:** 2024-09-25

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26808



#### What should I do?

**2024-09-25 Update:** The following versions of GDC software for VMware are updated with code to fix this vulnerability. Upgrade your GDC software for VMware clusters to the following versions or later: 

  * 1.28.600
  * 1.16.9



* * *

**Note:** Patch versions and a severity assessment for GKE on VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26808



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26808



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26808



#### What should I do?

There is no action required. GKE on Bare Metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2024-026

**Published:** 2024-05-07  
**Updated:** 2024-08-06  
**Reference:** [CVE-2024-26643](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26643)

**2024-08-06 Update:** Added patch versions for Ubuntu node pools on GKE.

**2024-05-09 Update:** Corrected severity from Medium to High.

### GKE

**Updated:** 2024-08-06

Description | Severity  
---|---  
**2024-05-09 Update:** Corrected severity from Medium to High.

* * *

The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26643

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2024-08-06 Update:** Added patch versions for Ubuntu node pools on GKE. The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. Upgrade your Ubuntu node pools to the following versions or later:

  * 1.27.15-gke.1252000
  * 1.28.11-gke.1260000
  * 1.29.6-gke.1326000
  * 1.30.2-gke.1394003



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.27.8-gke.1067000
  * 1.28.8-gke.1095000
  * 1.29.3-gke.1093000

**Note:** Patched Ubuntu versions will be released soon. You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). |  High   
  
### GKE on VMware

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26643



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26643



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26643



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26643



#### What should I do?

There is no action required. GKE on Bare Metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2024-024

**Published:** 2024-04-25  
**Updated:** 2024-07-18  
**Reference:** [CVE-2024-26585](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26585)

**2024-07-18 Update:** Added patch versions for Ubuntu node pools on GKE.

### GKE

**Updated:** 2024-07-18

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26585

GKE Standard and Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2024-07-18 Update:** The following versions of GKE are updated with code to fix this vulnerability on Ubuntu. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Ubuntu node pools to one of the following patch versions or later:

  * 1.26.15-gke.1469000
  * 1.27.14-gke.1100000
  * 1.28.10-gke.1148000
  * 1.29.6-gke.1038000
  * 1.30.2-gke.1394000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.25.16-gke.1759000
  * 1.26.15-gke.1158000
  * 1.27.12-gke.1190000
  * 1.28.8-gke.1175000
  * 1.29.3-gke.1282000

**Note:** Patched Ubuntu versions will be released soon. You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GKE on VMware

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26585



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26585



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26585



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-26585



#### What should I do?

There is no action required. GKE on Bare Metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2024-022

**Published:** 2024-04-03  
**Updated:** 2024-07-17  
**Reference:**[CVE-2023-45288](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45288)

**2024-07-17 Update:** Added patch versions for GKE on VMware.  
**2024-07-09 Update:** Added patch versions for GKE on Bare Metal.  
**2024-04-24 Update:** Added patch versions for GKE.

### GKE

**Updated:** 2024-04-24

Description | Severity  
---|---  
A Denial-of-Service (DoS) vulnerability (CVE-2023-45288) was recently discovered in multiple implementations of the HTTP/2 protocol, including the golang HTTP server used by Kubernetes. The vulnerability could lead to a DoS of the Google Kubernetes Engine (GKE) control plane. GKE clusters with authorized networks configured are protected by limiting network access, but all other clusters are affected. GKE Autopilot and Standard clusters are affected. **Note:** This bulletin is only for CVE-2023-45288 as it applies to the Kubernetes API server running on the GKE control plane. Other components that use the Go net/http2 package and that might also be vulnerable to CVE-2023-45288 are at a lower risk as they are not publicly exposed. Golang updates for components on GKE nodes are available on a regular update schedule.

#### What should I do?

**2024-04-24 Update:** Added patch versions for GKE. The following versions of GKE include the Golang security patches to fix this vulnerability. Upgrade your GKE clusters to the following versions or later:

  * 1.25.16-gke.1759000
  * 1.26.15-gke.1158000
  * 1.27.12-gke.1190000
  * 1.28.8-gke.1175000
  * 1.29.3-gke.1282000



* * *

The golang project released patches on April 3, 2024. We'll update this bulletin when GKE versions that incorporate these patches are available. To request a patch on an accelerated timeline, contact support.

##### Mitigate by configuring authorized networks for control plane access:

You can mitigate your clusters from this class of attacks by configuring authorized networks. Follow the instructions to [enable authorized networks for an existing cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks#add). To learn more about how authorized networks control access to the control plane, see [How authorized networks work](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks#how_authorized_networks_work). To see the default authorized network access, view the table in the [Access to control plane endpoints](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks#access_to_control_plane_endpoints) section.

#### What vulnerabilities are addressed by this patch?

The vulnerability (CVE-2023-45288) allows an attacker to execute a DoS attack on Kubernetes control plane. | High  
  
### GKE on VMware

**Updated:** 2024-07-17

Description | Severity  
---|---  
A Denial-of-Service (DoS) vulnerability (CVE-2023-45288) was recently discovered in multiple implementations of the HTTP/2 protocol, including the golang HTTP server used by Kubernetes. The vulnerability could lead to a DoS of the Google Kubernetes Engine (GKE) control plane.

#### What should I do?

**2024-07-17 Update:** Added patch versions for GKE on VMware. The following versions of GKE on VMware include code to fix this vulnerability. Upgrade your GKE on VMware clusters to the following versions or later:

  * 1.29.0
  * 1.28.500
  * 1.16.8



* * *

The golang project released patches on April 3, 2024. We'll update this bulletin when GKE on VMware versions that incorporate these patches are available. To request a patch on an accelerated timeline, contact support.

#### What vulnerabilities are addressed by this patch?

The vulnerability (CVE-2023-45288) allows an attacker to execute a DoS attack on Kubernetes control plane. | High  
  
### GKE on AWS

Description | Severity  
---|---  
A Denial-of-Service (DoS) vulnerability (CVE-2023-45288) was recently discovered in multiple implementations of the HTTP/2 protocol, including the golang HTTP server used by Kubernetes. The vulnerability could lead to a DoS of the Google Kubernetes Engine (GKE) control plane.

#### What should I do?

The golang project released patches on April 3, 2024. We'll update this bulletin when GKE on AWS versions that incorporate these patches are available. To request a patch on an accelerated timeline, contact support.

#### What vulnerabilities are addressed by this patch?

The vulnerability (CVE-2023-45288) allows an attacker to execute a DoS attack on Kubernetes control plane. | High  
  
### GKE on Azure

Description | Severity  
---|---  
A Denial-of-Service (DoS) vulnerability (CVE-2023-45288) was recently discovered in multiple implementations of the HTTP/2 protocol, including the golang HTTP server used by Kubernetes. The vulnerability could lead to a DoS of the Google Kubernetes Engine (GKE) control plane.

#### What should I do?

The golang project released patches on April 3, 2024. We'll update this bulletin when GKE on Azure versions that incorporate these patches are available. To request a patch on an accelerated timeline, contact support.

#### What vulnerabilities are addressed by this patch?

The vulnerability (CVE-2023-45288) allows an attacker to execute a DoS attack on Kubernetes control plane. | High  
  
### GKE on Bare Metal

**Updated:** 2024-07-09

Description | Severity  
---|---  
A Denial-of-Service (DoS) vulnerability (CVE-2023-45288) was recently discovered in multiple implementations of the HTTP/2 protocol, including the golang HTTP server used by Kubernetes. The vulnerability could lead to a DoS of the Google Kubernetes Engine (GKE) control plane.

#### What should I do?

**2024-07-09 Update:** Added patch versions for GKE on Bare Metal. The following versions of GKE on Bare Metal include code to fix this vulnerability. Upgrade your GKE on Bare Metal clusters to the following versions or later:

  * 1.29.100
  * 1.28.600
  * 1.16.9



* * *

The golang project released patches on April 3, 2024. We'll update this bulletin when GKE on Bare Metal versions that incorporate these patches are available. To request a patch on an accelerated timeline, contact support.

#### What vulnerabilities are addressed by this patch?

The vulnerability (CVE-2023-45288) allows an attacker to execute a DoS attack on Kubernetes control plane. | High  
  
## GCP-2024-018

**Published:** 2024-03-12  
**Updated:** 2024-05-06  
**Reference:** [CVE-2024-1085](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-1085)

**2024-05-06 Update:** Added patch versions for GKE Ubuntu node pools and removed an extra horizontal line element from the 2024-04-04 update.

**2024-04-04 Update:** Corrected minimum versions for GKE Container-Optimized OS node pools.

### GKE

**Updated:** 2024-05-06

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-1085

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2024-05-06 Update:** The following versions of GKE are updated with code to fix this vulnerability in Ubuntu. Upgrade your Ubuntu node pools to the following versions or later.

  * 1.26.15-gke.1158000
  * 1.27.12-gke.1190000
  * 1.28.8-gke.1175000
  * 1.29.3-gke.1093000



* * *

**2024-04-04 Update:** Corrected minimum versions for GKE Container-Optimized OS node pools. The minimum GKE versions containing the Container-Optimized OS fixes listed previously were incorrect. The following versions of GKE are updated with code to fix this vulnerability on Container-Optimized OS. Upgrade your Container-Optimized OS node pools to the following versions or later:

  * 1.25.16-gke.1520000
  * 1.26.13-gke.1221000
  * 1.27.10-gke.1243000
  * 1.28.8-gke.1083000
  * 1.29.3-gke.1054000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.25.16-gke.1518000
  * 1.26.13-gke.1219000
  * 1.27.10-gke.1240000
  * 1.28.6-gke.1433000
  * 1.29.1-gke.1716000

**Note:** Patched Ubuntu versions will be released soon. You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GKE on VMware

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-1085



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-1085



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-1085



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-1085



#### What should I do?

There is no action required. GKE on Bare Metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2024-017

**Published:** 2024-03-06  
**Reference:** [CVE-2023-3611](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3611)

### GKE

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2023-3611

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.24.14-gke.1027001
  * 1.25.10-gke.1027001
  * 1.26.5-gke.1021001
  * 1.27.3-gke.1001002

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Ubuntu node pools to one of the following patch versions or later:

  * 1.24.14-gke.1027001
  * 1.25.10-gke.1027001
  * 1.26.5-gke.1021001
  * 1.27.3-gke.1001002

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GKE on VMware

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2023-3611



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2023-3611



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2023-3611



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2023-3611



#### What should I do?

There is no action required. GKE on Bare Metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2024-014

**Published:** 2024-02-26  
**Reference:** [CVE-2023-3776](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3776)

### GKE

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2023-3776

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.24.14-gke.1027001
  * 1.25.10-gke.1027001
  * 1.26.5-gke.1014001
  * 1.27.3-gke.1001002
  * 1.28.0-gke.100

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Ubuntu node pools to one of the following patch versions or later:

  * 1.24.14-gke.1027001
  * 1.25.10-gke.1027001
  * 1.26.5-gke.1021001
  * 1.27.3-gke.1001002

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GKE on VMware

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2023-3776



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2023-3776



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2023-3776



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2023-3776



#### What should I do?

There is no action required. GKE on Bare Metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2024-013

**Published:** 2024-02-23  
**Reference:** [CVE-2023-3610](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3610)

### GKE

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2023-3610

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.27.3-gke.1001002
  * 1.28.0-gke.100

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Ubuntu node pools to one of the following patch versions or later:

  * 1.24.14-gke.1027001
  * 1.25.10-gke.1027001
  * 1.26.5-gke.1021001
  * 1.27.3-gke.1001002

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GKE on VMware

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2023-3610



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2023-3610



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2023-3610



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2023-3610



#### What should I do?

There is no action required. GKE on Bare Metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2024-012

**Published:** 2024-02-20  
**Reference:** [CVE-2024-0193](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0193)

### GKE

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-0193

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.27.10-gke.1149000
  * 1.28.6-gke.1274000
  * 1.29.1-gke.1388000

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Ubuntu node pools to one of the following patch versions or later:

  * 1.25.16-gke.1412001
  * 1.26.6-gke.1017002
  * 1.27.10-gke.1055001
  * 1.28.6-gke.1276000
  * 1.29.1-gke.1392000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GKE on VMware

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-0193



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-0193



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-0193



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2024-0193



#### What should I do?

There is no action required. GKE on Bare Metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2024-011

**Published:** 2024-02-15  
**Reference:** [CVE-2023-6932](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6932)

### GKE

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2023-6932

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies) Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.24.17-gke.2364001
  * 1.25.16-gke.1229000
  * 1.26.6-gke.1017002
  * 1.27.3-gke.1001003
  * 1.28.5-gke.1194000
  * 1.29.0-gke.1340000

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Ubuntu node pools to one of the following patch versions or later:

  * 1.25.16-gke.1412001
  * 1.26.6-gke.1017002
  * 1.27.10-gke.1055001
  * 1.28.6-gke.1276000
  * 1.29.1-gke.1221000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GKE on VMware

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2023-6932



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2023-6932



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2023-6932



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 

  * CVE-2023-6932



#### What should I do?

There is no action required. GKE on Bare Metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2024-010

**Published:** 2024-02-14  
**Updated:** 2024-04-17  
**Reference:** [CVE-2023-6931](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6931)

**2024-04-17 Update:** Added patch versions for GKE on VMware.

### GKE

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-6931

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.24.17-gke.2364001
  * 1.25.16-gke.1229000
  * 1.26.6-gke.1017002
  * 1.27.3-gke.1001003
  * 1.28.5-gke.1194000
  * 1.29.0-gke.1340000

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Ubuntu node pools to one of the following patch versions or later:

  * 1.25.16-gke.1412001
  * 1.26.6-gke.1017002
  * 1.27.10-gke.1055001
  * 1.28.6-gke.1276000
  * 1.29.1-gke.1221000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GKE on VMware

**Updated:** 2024-04-17

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-6931



#### What should I do?

**2024-04-17 Update:** Added patch versions for GKE on VMware.

* * *

The following versions of GKE on VMware are updated with code to fix this vulnerability. Upgrade your clusters to the following versions or later: 

  * 1.28.200
  * 1.16.6
  * 1.15.10



* * *

**Note:** Patch versions and a severity assessment for GKE on VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-6931



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-6931



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-6931



#### What should I do?

There is no action required. GKE on Bare Metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2024-008

**Published:** 2024-02-12  
**Reference:**[CVE-2023-5528](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5528)

### GKE

Description | Severity  
---|---  
CVE-2023-5528 allows an attacker to create pods and persistent volumes on Windows nodes in a way that enables admin privilege escalation on those nodes. GKE Standard clusters running [Windows Server](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#windows-server) nodes and using an in-tree storage plugin might be affected. GKE Autopilot clusters and GKE node pools using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) are not affected because they do not support Windows Server nodes. 

#### What should I do?

Determine if you have Windows Server nodes in use on your clusters:
    
    
    kubectl get nodes -l kubernetes.io/os=windows

Check audit logs for evidence of exploitation. Kubernetes audit logs can be audited to determine if this vulnerability is being exploited. Persistent Volume create events with local path fields containing special characters are a strong indication of exploitation. Update your GKE cluster and node pools to a patched version. The following versions of GKE have been updated to fix this vulnerability. Even if you have node auto-upgrade enabled, we recommend that you [manually upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your cluster and Windows Server node pools to one of the following GKE versions or later:

  * 1.24.17-gke.6100
  * 1.25.15-gke.2000
  * 1.26.10-gke.2000
  * 1.27.7-gke.2000 
  * 1.28.3-gke.1600

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions).

#### What vulnerabilities are addressed by this patch?

CVE-2023-5528 allows an attacker to create pods and persistent volumes on Windows nodes in a way that enables admin privilege escalation on those nodes. | High  
  
### GKE on VMware

Description | Severity  
---|---  
CVE-2023-5528 allows an attacker to create pods and persistent volumes on Windows nodes in a way that enables admin privilege escalation on those nodes. GKE on VMware clusters running [Windows Server](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/user-guide-for-windows-server-os-node-pools) nodes and using an in-tree storage plugin might be affected.

#### What should I do?

Determine if you have Windows Server nodes in use on your clusters:
    
    
    kubectl get nodes -l kubernetes.io/os=windows

Check audit logs for evidence of exploitation. Kubernetes audit logs can be audited to determine if this vulnerability is being exploited. Persistent Volume create events with local path fields containing special characters are a strong indication of exploitation. Update your GKE on VMware cluster and node pools to a patched version. The following versions of GKE on VMware have been updated to fix this vulnerability. Even if you have node auto-upgrade enabled, we recommend that you [manually upgrade](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/upgrading) your cluster and Windows Server node pools to one of the following GKE on VMware versions or later:

  * 1.28.100-gke.131
  * 1.16.5-gke.28
  * 1.15.8-gke.41



#### What vulnerabilities are addressed by this patch?

CVE-2023-5528 allows an attacker to create pods and persistent volumes on Windows nodes in a way that enables admin privilege escalation on those nodes. | High  
  
### GKE on AWS

Description | Severity  
---|---  
CVE-2023-5528 allows an attacker to create pods and persistent volumes on Windows nodes in a way that enables admin privilege escalation on those nodes. GKE on AWS clusters aren't affected.

#### What should I do?

No action required | None  
  
### GKE on Azure

Description | Severity  
---|---  
CVE-2023-5528 allows an attacker to create pods and persistent volumes on Windows nodes in a way that enables admin privilege escalation on those nodes. GKE on Azure clusters aren't affected.

#### What should I do?

No action required | None  
  
### GKE on Bare Metal

Description | Severity  
---|---  
CVE-2023-5528 allows an attacker to create pods and persistent volumes on Windows nodes in a way that enables admin privilege escalation on those nodes. GKE on Bare Metal clusters aren't affected.

#### What should I do?

No action required | None  
  
## GCP-2024-005

**Published:** 2024-01-31  
**Updated:** 2024-05-06  
**Reference:**[CVE-2024-21626](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21626)

**2024-05-06 Update** : Added patch versions for GKE on AWS and GKE on Azure.  
**2024-04-02 Update** : Added patch versions for GKE on Bare Metal  
**2024-03-06 Update** : Added patch versions for GKE on VMware  
**2024-02-28 Update** : Added patch versions for Ubuntu  
**2024-02-15 Update** : Clarified that the 1.25 and 1.26 Ubuntu patch versions in the 2024-02-14 update might cause unhealthy nodes.  
**2024-02-14 Update** : Added patch versions for Ubuntu  
**2024-02-06 Update:** Added patch versions for Container-Optimized OS.

### GKE

**Updated:** 2024-03-06

Description | Severity  
---|---  
A security vulnerability, CVE-2024-21626, has been discovered in `runc` where a user with permission to create Pods on Container-Optimized OS and Ubuntu nodes might be able to gain full access to the node filesystem. GKE Standard and Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2024-02-28 Update** : The following versions of GKE have been updated with code to fix this vulnerability in Ubuntu. Upgrade your Ubuntu node pools to one of the following patch versions or later:

  * 1.25.16-gke.1537000
  * 1.26.14-gke.1006000



* * *

**2024-02-15 Update** : Due to an issue, the following Ubuntu patch versions from the 2024-02-14 update might cause your nodes to enter an unhealthy state. Don't upgrade to the following patch versions. We'll update this bulletin when newer patch versions for Ubuntu are available for 1.25 and 1.26.

  * 1.25.16-gke.1497000
  * 1.26.13-gke.1189000

If you already upgraded to one of these patch versions, [manually downgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#downgrading_nodes) your node pool to an earlier version in your release channel.

* * *

**2024-02-14 Update** : The following versions of GKE have been updated with code to fix this vulnerability in Ubuntu. Upgrade your Ubuntu node pools to one of the following patch versions or later:

  * 1.25.16-gke.1497000
  * 1.26.13-gke.1189000
  * 1.27.10-gke.1207000
  * 1.28.6-gke.1369000
  * 1.29.1-gke.1575000



* * *

**2024-02-06 Update** : The following versions of GKE have been updated with code to fix this vulnerability in Container-Optimized OS. For security purposes, even if you have node auto-upgrade enabled, we recommend that you [manually upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your cluster and Container-Optimized OS node pools to one of the following GKE versions or later:

  * 1.25.16-gke.1460000
  * 1.26.13-gke.1144000
  * 1.27.10-gke.1152000
  * 1.28.6-gke.1289000
  * 1.29.1-gke.1425000

**Note** : We'll update this bulletin when Ubuntu patch versions are available.You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions).

* * *

We're updating GKE with code to fix this vulnerability. We'll update this bulletin when patch versions are available.

#### What vulnerabilities are addressed by this patch?

`runc` is a low-level tool for spawning and running Linux containers used in Kubernetes Pods. In `runc` versions prior to the patches released in this security bulletin, several file descriptors were inadvertently leaked into the `runc init` process that runs within a container. `runc` also did not verify that a container's final working directory was inside the container's mount namespace. A malicious container image or a user with permission to run arbitrary Pods could use a combination of the leaked file descriptors and lack of working directory validation to gain access to a node's host mount namespace and access the entire host filesystem and overwrite arbitrary binaries on the node. | High  
  
### GKE on VMware

**Updated:** 2024-03-06

Description | Severity  
---|---  
A security vulnerability, CVE-2024-21626, has been discovered in `runc` where a user with permission to create Pods on Container-Optimized OS and Ubuntu nodes might be able to gain full access to the node filesystem.

#### What should I do?

**2024-03-06 Update** : The following versions of GKE on VMware have been updated with code to fix this vulnerability. Upgrade your clusters to the following versions or later:

  * 1.28.200
  * 1.16.6
  * 1.15.9



* * *

Patch versions and a severity assessment for GKE on VMware are in progress. We'll update this bulletin with that information when it's available.

#### What vulnerabilities are addressed by this patch?

`runc` is a low-level tool for spawning and running Linux containers used in Kubernetes Pods. In `runc` versions prior to the patches released in this security bulletin, several file descriptors were inadvertently leaked into the `runc init` process that runs within a container. `runc` also did not verify that a container's final working directory was inside the container's mount namespace. A malicious container image or a user with permission to run arbitrary Pods could use a combination of the leaked file descriptors and lack of working directory validation to gain access to a node's host mount namespace and access the entire host filesystem and overwrite arbitrary binaries on the node. | High  
  
### GKE on AWS

**Updated:** 2024-05-06

Description | Severity  
---|---  
A security vulnerability, CVE-2024-21626, has been discovered in `runc` where a user with permission to create Pods on Container-Optimized OS and Ubuntu nodes might be able to gain full access to the node filesystem.

#### What should I do?

**2024-05-06 Update** : The following versions of GKE on AWS have been updated with patches for CVE-2024-21626:

  * 1.28.5-gke.1200
  * 1.27.10-gke.500
  * 1.26.13-gke.400



* * *

Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available.

#### What vulnerabilities are addressed by this patch?

`runc` is a low-level tool for spawning and running Linux containers used in Kubernetes Pods. In `runc` versions prior to the patches released in this security bulletin, several file descriptors were inadvertently leaked into the `runc init` process that runs within a container. `runc` also did not verify that a container's final working directory was inside the container's mount namespace. A malicious container image or a user with permission to run arbitrary Pods could use a combination of the leaked file descriptors and lack of working directory validation to gain access to a node's host mount namespace and access the entire host filesystem and overwrite arbitrary binaries on the node. | High  
  
### GKE on Azure

**Updated:** 2024-05-06

Description | Severity  
---|---  
A security vulnerability, CVE-2024-21626, has been discovered in `runc` where a user with permission to create Pods on Container-Optimized OS and Ubuntu nodes might be able to gain full access to the node filesystem.

#### What should I do?

**2024-05-06 Update** : The following versions of GKE on Azure have been updated with patches for CVE-2024-21626:

  * 1.28.5-gke.1200
  * 1.27.10-gke.500
  * 1.26.13-gke.400



* * *

Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available.

#### What vulnerabilities are addressed by this patch?

`runc` is a low-level tool for spawning and running Linux containers used in Kubernetes Pods. In `runc` versions prior to the patches released in this security bulletin, several file descriptors were inadvertently leaked into the `runc init` process that runs within a container. `runc` also did not verify that a container's final working directory was inside the container's mount namespace. A malicious container image or a user with permission to run arbitrary Pods could use a combination of the leaked file descriptors and lack of working directory validation to gain access to a node's host mount namespace and access the entire host filesystem and overwrite arbitrary binaries on the node. | High  
  
### GKE on Bare Metal

**Updated:** 2024-04-02

Description | Severity  
---|---  
A security vulnerability, CVE-2024-21626, has been discovered in `runc` where a user with permission to create Pods might be able to gain full access to the node filesystem.

#### What should I do?

**2024-04-02 Update** : The following versions of GKE on Bare Metal have been updated with code to fix this vulnerability. Upgrade your clusters to the following versions or later:

  * 1.28.200-gke.118
  * 1.16.6
  * 1.15.10



* * *

Patch versions and a severity assessment for GKE on Bare Metal are in progress. We'll update this bulletin with that information when it's available.

#### What vulnerabilities are addressed by this patch?

`runc` is a low-level tool for spawning and running Linux containers used in Kubernetes Pods. In `runc` versions prior to the patches released in this security bulletin, several file descriptors were inadvertently leaked into the `runc init` process that runs within a container. `runc` also did not verify that a container's final working directory was inside the container's mount namespace. A malicious container image or a user with permission to run arbitrary Pods could use a combination of the leaked file descriptors and lack of working directory validation to gain access to a node's host mount namespace and access the entire host filesystem and overwrite arbitrary binaries on the node. | High  
  
## GCP-2024-004

**Published:** 2024-01-24  
**Updated:** 2024-02-07  
**Reference:** [CVE-2023-6817](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6817)

**2024-02-07 Update:** Added patch versions for Ubuntu.

### GKE

**Updated:** 2024-02-07

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-6817

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies) Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2024-02-07 Update:** The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Ubuntu node pools to one of the following patch versions or later:

  * 1.25.16-gke.1458000
  * 1.26.13-gke.1143000
  * 1.27.10-gke.1152000
  * 1.28.6-gke.1276000
  * 1.29.1-gke.1221000



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.25.16-gke.1229000
  * 1.26.12-gke.1087000
  * 1.27.3-gke.1001003
  * 1.28.5-gke.1194000
  * 1.29.0-gke.1340000

**Note:** Patched Ubuntu versions will be released soon. You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GKE on VMware

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-6817



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-6817



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-6817



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-6817



#### What should I do?

There is no action required. GKE on Bare Metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2024-003

**Published:** 2024-01-19  
**Updated:** 2024-01-26  
**2024-01-26 Update:** Clarified the number of affected clusters and the actions that we took to help mitigate the impact.

### GKE

**Updated:** 2024-01-26

Description | Severity  
---|---  
**2024-01-26 Update** : Security research that found a small number of GKE clusters with a customer-created misconfiguration involving the `system:authenticated` group has now been published. The researcher's blog post refers to 1,300 clusters with some misconfigured bindings, and 108 with high privileges. We have worked closely with impacted customers to notify them and assist with removing their misconfigured bindings.

* * *

We have identified several clusters where users have granted Kubernetes privileges to the `system:authenticated` group, which includes all users with a Google account. These types of bindings are [not recommended](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/rbac#default-roles-groups), as they violate the principle of least privilege and grant access to very large groups of users. See guidance under 'What should I do' for instructions on how to find these types of bindings. Recently, a security researcher reported findings of clusters with RBAC misconfigurations through our vulnerability reporting program. Google's approach to authentication is to make authenticating to Google Cloud and GKE as simple and secure as possible without adding complex configuration steps. _Authentication_ just tells us who the user is; _Authorization_ is where access is determined. So the `system:authenticated` group in GKE that contains all users authenticated through Google's identity provider is working as intended and functions in the same way as the [IAM allAuthenticatedUsers identifier](https://docs.cloud.google.com/iam/docs/overview#all-authenticated-users). With this in mind we've taken several steps to reduce the risk of users making _authorization_ errors with the Kubernetes built-in users and groups, including `system:anonymous`, `system:authenticated`, and `system:unauthenticated`. All of these users/groups represent a risk to the cluster if granted permissions. We discussed some of the attacker activity targeting RBAC misconfigurations and available defenses [at Kubecon in November 2023](https://kccncna2023.sched.com/event/1R2tp/rbacdoors-how-cryptominers-are-exploiting-rbac-misconfigs-greg-castle-vinayak-goyal-google). To protect users from accidental authorization errors with these system users/groups, we have:

  * [By default blocked new bindings](https://cloud.google.com/kubernetes-engine/docs/best-practices/rbac#detect-prevent-default) of the highly privileged ClusterRole `cluster-admin` to User `system:anonymous`, Group `system:authenticated`, or Group `system:unauthenticated` in GKE version 1.28.
  * Built detection rules into [Event Threat Detection](https://cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules) (GKE_CONTROL_PLANE_CREATE_SENSITIVE_BINDING) as part of Security Command Center.
  * Built configurable prevention rules into Policy Controller with [K8sRestrictRoleBindings](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8srestrictrolebindings).
  * Sent email notifications to all GKE users with bindings to these users/groups asking them to review their configuration.
  * Built network authorization features and [made recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#restrict_network_access_to_the_control_plane_and_nodes) to restrict network access to clusters as a first layer of defense.
  * Raised awareness about this issue [through a talk at Kubecon in November 2023](https://kccncna2023.sched.com/event/1R2tp/rbacdoors-how-cryptominers-are-exploiting-rbac-misconfigs-greg-castle-vinayak-goyal-google).

Clusters that apply [authorized networks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks) restrictions have a first layer of defense: they cannot be attacked directly from the Internet. But we still recommend removing these bindings for defense in depth and to guard against errors in network controls.  
Note there are a number of cases where bindings to Kubernetes system users or groups are used intentionally: e.g. for [kubeadm bootstrapping](https://docs.cloud.google.com/kubernetes/design-proposals-archive/blob/main/cluster-lifecycle/bootstrap-discovery#implementation-details), the [Rancher dashboard](https://github.com/rancher/rancher/blob/a5f90f1f356c5d7b8f701a19be0fb3f1dcb42c20/pkg/data/dashboard/rbac.go#L12) and [Bitnami sealed secrets](https://github.com/bitnami-labs/sealed-secrets/commit/516503c3c5eb7a12786c6adb5fda681a372e2e5a). We have confirmed with those software vendors that those bindings are working as intended. We are investigating ways we can further protect against user RBAC misconfiguration with these system users/groups through prevention and detection.

#### What should I do?

To prevent any _new_ bindings of `cluster-admin` to User `system:anonymous`, Group `system:authenticated`, or Group `system:unauthenticated` users can upgrade to GKE v1.28 or later ([release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#September_18_2023)), where creation of those bindings are blocked. Existing bindings should be reviewed [following this guidance](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/rbac#detect-prevent-default). | Medium  
  
### GKE on VMware

No updates at this time.

### GKE on AWS

No updates at this time.

### GKE on Azure

No updates at this time.

### GKE on Bare Metal

No updates at this time.

## GCP-2024-002

**Published:** 2024-01-17  
**Updated:** 2024-02-20  
**Reference:** [CVE-2023-6111](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6111)

**2024-02-20 Update:** Added patch versions for GKE on VMware.

### GKE

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes. 

  * CVE-2023-6111

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies) Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.27.7-gke.1063001
  * 1.28.5-gke.1194000
  * 1.29.0-gke.1340000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GKE on VMware

**Updated:** 2024-02-20

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes. 

  * CVE-2023-6111



#### What should I do?

**2024-02-20 Update:** The following versions of GKE on VMware are updated with code to fix this vulnerability. Upgrade your clusters to the following versions or later: 1.28.100

* * *

**Note:** Patch versions and a severity assessment for GKE on VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes. 

  * CVE-2023-6111



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes. 

  * CVE-2023-6111



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes. 

  * CVE-2023-6111



#### What should I do?

There is no action required. GKE on Bare Metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2023-051

**Published:** 2023-12-28  
**Reference:** [CVE-2023-3609](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3609)

### GKE

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-3609

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.24.14-gke.1027001
  * 1.25.10-gke.1027001
  * 1.26.5-gke.1014001
  * 1.27.3-gke.1001002
  * 1.28.0-gke.100

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Ubuntu node pools to one of the following patch versions or later:

  * 1.24.14-gke.1027001
  * 1.26.5-gke.1021001
  * 1.27.3-gke.1001002

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GKE on VMware

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-3609



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-3609



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-3609



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-3609



#### What should I do?

There is no action required. GKE on Bare Metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2023-050

**Published:** 2023-12-27  
**Reference:** [CVE-2023-3389](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3389)

### GKE

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-3389

GKE Standard and Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.24.14-gke.1027001
  * 1.25.10-gke.1027001
  * 1.26.5-gke.1014001
  * 1.27.3-gke.1001002
  * 1.28.0-gke.100

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Ubuntu node pools to one of the following patch versions or later:

  * 1.24.14-gke.1027001
  * 1.25.10-gke.1027001
  * 1.26.5-gke.1014001
  * 1.27.3-gke.1001002
  * 1.28.1-gke.1002003

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GKE on VMware

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-3389



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-3389



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-3389



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-3389



#### What should I do?

There is no action required. GKE on Bare Metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2023-049

**Published:** 2023-12-20  
**Reference:** [CVE-2023-3090](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3090)

### GKE

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-3090

GKE Standard clusters are impacted. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp `Unconfined` profile or [allow `CAP_NET_ADMIN`.](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies) Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.24.14-gke.1027001
  * 1.25.12-gke.900
  * 1.26.5-gke.1014001
  * 1.27.4-gke.400
  * 1.28.0-gke.100

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Ubuntu node pools to one of the following patch versions or later:

  * 1.24.14-gke.1027001
  * 1.25.12-gke.900
  * 1.26.5-gke.1014001
  * 1.27.4-gke.900
  * 1.28.1-gke.1050000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GKE on VMware

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-3090



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWS.The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-3090



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-3090



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-3090



#### What should I do?

There is no action required. GKE on Bare Metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2023-048

**Published:** 2023-12-15  
**Updated:** 2023-12-21  
**Reference:** [CVE-2023-3390](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3390)

**2023-12-21 Update:** Clarify that GKE Autopilot clusters in the default configuration are not impacted.

### GKE

**Updated:** 2023-12-21

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-3390

**2023-12-21 Update** : The original bulletin stated Autopilot clusters are impacted, but this was incorrect. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp Unconfined profile or [allow `CAP_NET_ADMIN`.](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies) GKE Standard and Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.27.4-gke.400
  * 1.28.0-gke.100

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Ubuntu node pools to one of the following patch versions or later:

  * 1.24.14-gke.1027001
  * 1.25.12-gke.900
  * 1.26.5-gke.1014001
  * 1.27.4-gke.900
  * 1.28.1-gke.1050000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GKE on VMware

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-3390



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-3390



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-3390



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-3390



#### What should I do?

There is no action required. GKE on Bare Metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2023-047

**Published:** 2023-12-14

### GKE

Description | Severity  
---|---  
An attacker who has compromised the Fluent Bit logging container could combine that access with high privileges required by Cloud Service Mesh (on clusters that have enabled it) to escalate privileges in the cluster. The issues with Fluent Bit and Cloud Service Mesh have been mitigated and fixes are now available. These vulnerabilities are not exploitable on their own in GKE and require an initial compromise. We are not aware of any instances of exploitation of these vulnerabilities.  These issues were reported through our [Vulnerability Reward Program](https://bughunters.google.com/about). 

#### What should I do?

The following versions of GKE have been updated with code to fix these vulnerabilities in Fluent Bit and for users of managed Cloud Service Mesh. For security purposes, even if you have node auto-upgrade enabled, we recommend that you [manually upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your cluster and node pools to one of the following GKE versions or later: 

  * 1.25.16-gke.1020000
  * 1.26.10-gke.1235000
  * 1.27.7-gke.1293000
  * 1.28.4-gke.1083000

A recent feature of [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions) allows you to apply a patch without having to unsubscribe from a channel. This lets you secure your nodes until the new version becomes the default for your specific release channel  If your cluster uses in-cluster Cloud Service Mesh, you must [manually upgrade](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade) to one of the following versions ([release notes](https://docs.cloud.google.com/service-mesh/docs/release-notes#December_12_2023)): 

  * 1.17.8-asm.8
  * 1.18.6-asm.2
  * 1.19.5-asm.4

**What vulnerabilities are being addressed by this patch?** The vulnerabilities addressed by this bulletin require an attacker to compromise the Fluent Bit logging container. We are not aware of any existing vulnerabilities in Fluent Bit that would lead to this prerequisite condition for privilege escalation. We have patched these vulnerabilities as hardening measures to prevent a potential full attack chain in the future  GKE uses Fluent Bit to process logs for workloads running on clusters. Fluent Bit on GKE was also configured to collect logs for Cloud Run workloads. The volume mount configured to collect those logs gave Fluent Bit access to Kubernetes service account tokens for other Pods running on the node. The researcher used this access to discover a highly privileged service account token for clusters that have Cloud Service Mesh enabled. Cloud Service Mesh required high privileges to make necessary modifications to a cluster's configuration including the ability to create and delete Pods. The researcher used Cloud Service Mesh's privileged Kubernetes service account token to escalate their initial compromised privileges by creating a new pod with cluster-admin privileges  We have removed Fluent Bit's access to the service account tokens and have redesigned the functionality of Cloud Service Mesh to remove excess privileges.  | Medium  
  
### GKE on VMware

Description | Severity  
---|---  
Only GKE on VMware clusters using Cloud Service Mesh are affected. 

#### What should I do?

If your cluster uses in-cluster Cloud Service Mesh, you must [manually upgrade](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade) to one of the following versions ([release notes](https://docs.cloud.google.com/service-mesh/docs/release-notes#December_12_2023)): 

  * 1.17.8-asm.8
  * 1.18.6-asm.2
  * 1.19.5-asm.4



#### What vulnerabilities are addressed by this patch?

The vulnerabilities addressed by this bulletin require an attacker to first either compromise or otherwise break out of a container or have root on a cluster Node. We are not aware of any existing vulnerabilities that would lead to this prerequisite condition for privilege escalation. We have patched these vulnerabilities as hardening measures to prevent a potential full attack chain in the future.  Cloud Service Mesh required high privileges to make necessary modifications to a cluster's configuration including the ability to create and delete Pods. The researcher used Cloud Service Mesh's privileged Kubernetes service account token to escalate their initial compromised privileges by creating a new pod with cluster-admin privileges.  We have redesigned the functionality of Cloud Service Mesh to remove excessive privileges.  | Medium  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWS Only GKE on AWS clusters using Cloud Service Mesh are affected. 

#### What should I do?

If your cluster uses in-cluster Cloud Service Mesh, you must [manually upgrade](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade) to one of the following versions ([release notes](https://docs.cloud.google.com/service-mesh/docs/release-notes#December_12_2023)): 

  * 1.17.8-asm.8
  * 1.18.6-asm.2
  * 1.19.5-asm.4



#### What vulnerabilities are addressed by this patch?

The vulnerabilities addressed by this bulletin require an attacker to first either compromise or otherwise break out of a container or have root on a cluster Node. We are not aware of any existing vulnerabilities that would lead to this prerequisite condition for privilege escalation. We have patched these vulnerabilities as hardening measures to prevent a potential full attack chain in the future.  Cloud Service Mesh required high privileges to make necessary modifications to a cluster's configuration including the ability to create and delete Pods. The researcher used Cloud Service Mesh's privileged Kubernetes service account token to escalate their initial compromised privileges by creating a new pod with cluster-admin privileges.  We have redesigned the functionality of Cloud Service Mesh to remove excessive privileges.  | Medium  
  
### GKE on Azure

Description | Severity  
---|---  
Only GKE on Azure clusters using Cloud Service Mesh are affected. 

#### What should I do?

If your cluster uses in-cluster Cloud Service Mesh, you must [manually upgrade](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade) to one of the following versions ([release notes](https://docs.cloud.google.com/service-mesh/docs/release-notes#December_12_2023)): 

  * 1.17.8-asm.8
  * 1.18.6-asm.2
  * 1.19.5-asm.4



#### What vulnerabilities are addressed by this patch?

The vulnerabilities addressed by this bulletin require an attacker to first either compromise or otherwise break out of a container or have root on a cluster Node. We are not aware of any existing vulnerabilities that would lead to this prerequisite condition for privilege escalation. We have patched these vulnerabilities as hardening measures to prevent a potential full attack chain in the future.  Cloud Service Mesh required high privileges to make necessary modifications to a cluster's configuration including the ability to create and delete Pods. The researcher used Cloud Service Mesh's privileged Kubernetes service account token to escalate their initial compromised privileges by creating a new pod with cluster-admin privileges.  We have redesigned the functionality of Cloud Service Mesh to remove excessive privileges.  | Medium  
  
### GKE on Bare Metal

Description | Severity  
---|---  
Only GKE on Bare Metal clusters using Cloud Service Mesh are affected. 

#### What should I do?

If your cluster uses in-cluster Cloud Service Mesh, you must [manually upgrade](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade) to one of the following versions ([release notes](https://docs.cloud.google.com/service-mesh/docs/release-notes#December_12_2023)): 

  * 1.17.8-asm.8
  * 1.18.6-asm.2
  * 1.19.5-asm.4



#### What vulnerabilities are addressed by this patch?

The vulnerabilities addressed by this bulletin require an attacker to first either compromise or otherwise break out of a container or have root on a cluster Node. We are not aware of any existing vulnerabilities that would lead to this prerequisite condition for privilege escalation. We have patched these vulnerabilities as hardening measures to prevent a potential full attack chain in the future.  Anthos Service Mesh required high privileges to make necessary modifications to a cluster's configuration including the ability to create and delete Pods. The researcher used Cloud Service Mesh's privileged Kubernetes service account token to escalate their initial compromised privileges by creating a new pod with cluster-admin privileges.  We have redesigned the functionality of Cloud Service Mesh to remove excessive privileges.  | Medium  
  
## GCP-2023-046

**Published:** 2023-11-22  
**Updated:** 2024-03-04  
**Reference:** [CVE-2023-5717](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5717)

**2024-03-04 Update:** Added GKE versions for GKE on VMware.

**2024-01-22 Update:** Added Ubuntu patch versions.

### GKE

**Updated:** 2024-01-22

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-5717

GKE Standard and Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2024-01-22 Update** : The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Ubuntu node pools to one of the following patch versions or later:

  * 1.24.17-gke.2472000
  * 1.25.16-gke.1268000
  * 1.26.12-gke.1111000
  * 1.27.9-gke.1092000
  * 1.28.5-gke.1217000
  * 1.29.0-gke.138100



* * *

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.24.17-gke.2113000
  * 1.25.14-gke.1421000
  * 1.25.15-gke.1083000
  * 1.26.10-gke.1073000
  * 1.27.7-gke.1088000
  * 1.28.3-gke.1203000

**Note:** Patched Ubuntu versions will be released soon. You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GKE on VMware

**Updated:** 2024-02-29

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-5717



#### What should I do?

**2024-03-04 Update** : The following versions of GKE on VMware are updated with code to fix this vulnerability. Upgrade your clusters to the following versions or later:

  * 1.28.200
  * 1.16.5
  * 1.15.8

| High  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWS.The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-5717



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-5717



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-5717



#### What should I do?

There is no action required. GKE on Bare Metal isn't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2023-045

**Published:** 2023-11-20  
**Updated:** 2023-12-21  
**Reference:** [CVE-2023-5197](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5197)

**2023-12-21 Update:** Clarify that GKE Autopilot clusters in the default configuration are not impacted.

### GKE

**Updated:** 2023-12-21

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-5197

**2023-12-21 Update** : The original bulletin stated Autopilot clusters are impacted, but this was incorrect. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp Unconfined profile or [allow `CAP_NET_ADMIN`.](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies) GKE Standard and Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following patch versions or later:

  * 1.25.13-gke.1002003
  * 1.26.9-gke.1514000
  * 1.27.6-gke.1513000
  * 1.28.2-gke.1164000

The following minor versions are affected. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Ubuntu node pools to one of the following patch versions or later:

  * 1.24.16-gke.1005001
  * 1.25.13-gke.1002003
  * 1.26.9-gke.1548000
  * 1.27.7-gke.1039000
  * 1.28.3-gke.1061000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patch version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GKE on VMware

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-5197



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-5197



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-5197



#### What should I do?

**Note:** Patch versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-5197



#### What should I do?

There is no action required. GKE on Bare Metal aren't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2023-042

**Published:** 2023-11-13  
**Updated:** 2023-11-15  
**Reference:** [CVE-2023-4147](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4147)

**2023-11-15 Update:** Clarify that only the listed minor versions need to upgrade to a corresponding patched version for GKE.

### GKE

**Updated:** 2023-11-15

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4147

GKE Standard clusters are impacted. GKE Autopilot clusters aren't impacted. If you have Autopilot clusters that allow [`CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies), those clusters might be affected.Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) aren't impacted.

#### What should I do?

**2023-11-15 Update** : You only need to upgrade to one of the patched versions that are listed in this bulletin if you use that minor version in your nodes. For example, if you use GKE version 1.27, you should upgrade to the corresponding patched version. However, if you use GKE version 1.24, you don't need to upgrade to a patched version.

* * *

[Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following versions or later:

  * 1.27.5-gke.200
  * 1.28.2-gke.1157000

[Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Ubuntu node pools to one of the following versions or later:

  * 1.25.14-gke.1421000
  * 1.26.9-gke.1437000
  * 1.27.6-gke.1248000
  * 1.28.2-gke.1157000

You can apply patch versions from newer release channels if your cluster runs the same minor version in its own release channel. This feature lets you secure your nodes until the patched version becomes the default in your release channel. For details, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). | High  
  
### GKE on VMware

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4147



#### What should I do?

**Note:** Patched versions and a severity assessment for GKE on VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4147



#### What should I do?

**Note:** Patched versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4147



#### What should I do?

**Note:** Patched versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4147



#### What should I do?

There is no action required. GKE on Bare Metal aren't affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2023-041

**Published:** 2023-11-08  
**Updated:** 2023-11-21, 2023-12-05, 2023-12-21  
**Reference:** [CVE-2023-4004](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4004)

**2023-12-21 Update:** Clarify that GKE Autopilot clusters in the default configuration are not impacted.

**2023-12-05 Update:** Added additional GKE versions for Container-Optimized OS node pools.

**2023-11-21 Update:** Clarify that only the listed minor versions need to upgrade to a corresponding patch version for GKE.

### GKE

**Updated:** 2023-11-21, 2023-12-05, 2023-12-21

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4004

**2023-12-21 Update** : The original bulletin stated Autopilot clusters are impacted, but this was incorrect. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp Unconfined profile or [allow `CAP_NET_ADMIN`.](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies) Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) are not impacted.

#### What should I do?

**2023-12-05 Update:** Some GKE versions were previously missing. The following is an updated list of GKE versions that you can update your Container-Optimized OS to: 

  * 1.24.17-gke.200 or later
  * 1.25.13-gke.200 or later
  * 1.26.8-gke.200 or later
  * 1.27.4-gke.2300 or later
  * 1.28.1-gke.1257000 or later

**2023-11-21 Update:** You only need to upgrade to one of the patch versions that are listed in this bulletin if you use that minor version in your nodes. Minor versions that aren't listed aren't impacted. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following versions or later:

  * 1.27.4-gke.2300
  * 1.28.1-gke.1257000

[Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Ubuntu node pools to one of the following versions or later:

  * 1.24.14-gke.1027001
  * 1.25.13-gke.700
  * 1.26.8-gke.700
  * 1.27.5-gke.700
  * 1.28.1-gke.1050000

| High  
  
### GKE on VMware

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4004



#### What should I do?

**Note:** Patched versions and a severity assessment for GKE on VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4004



#### What should I do?

**Note:** Patched versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4004



#### What should I do?

**Note:** Patched versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4004



#### What should I do?

There is no action required. GKE on Bare Metal are not affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2023-040

**Published:** 2023-11-06  
**Updated:** 2023-11-21, 2023-12-21  
**Reference:** [CVE-2023-4921](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4921)

**2023-12-21 Update:** Clarify that GKE Autopilot clusters in the default configuration are not impacted.

**2023-11-21 Update:** Clarify that only the listed minor versions need to upgrade to a corresponding patch version for GKE.

### GKE

**Updated:** 2023-11-21, 2023-12-21

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4921

**2023-12-21 Update** : The original bulletin stated Autopilot clusters are impacted, but this was incorrect. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp Unconfined profile or [allow `CAP_NET_ADMIN`.](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies) Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) are not impacted.

#### What should I do?

**2023-11-21 Update:** You only need to upgrade to one of the patch versions that are listed in this bulletin if you use that minor version in your nodes. Minor versions that aren't listed aren't impacted. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following versions or later:

  * 1.24.14-gke.1027001
  * 1.25.14-gke.1351000
  * 1.26.9-gke.1345000
  * 1.27.6-gke.1389000

[Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Ubuntu node pools to one of the following versions or later:

  * 1.24.17-gke.2186000
  * 1.25.15-gke.1016000
  * 1.26.9-gke.1548000
  * 1.27.6-gke.1551000
  * 1.28.2-gke.1256000

| High  
  
### GKE on VMware

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4921



#### What should I do?

**Note:** Patched versions and a severity assessment for GKE on VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4921



#### What should I do?

**Note:** Patched versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4921



#### What should I do?

**Note:** Patched versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4921



#### What should I do?

There is no action required. GKE on Bare Metal are not affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2023-039

**Published:** 2023-11-06  
**Updated:** 2023-11-21, 2023-11-16  
**Reference:** [CVE-2023-4622](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4622)

**2023-11-21 Update:** Clarify that only the listed minor versions need to upgrade to a corresponding patch version for GKE.

**2023-11-16 Update:** The vulnerability associated with this security bulletin is [CVE-2023-4622](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4622). CVE-2023-4623 was incorrectly listed as the vulnerability in a previous version of the security bulletin.

### GKE

**Updated:** 2023-11-21, 2023-11-16

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4623

Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) are not impacted.

#### What should I do?

**2023-11-21 Update:** You only need to upgrade to one of the patch versions that are listed in this bulletin if you use that minor version in your nodes. Minor versions that aren't listed aren't impacted. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following versions or later:

  * 1.24.14-gke.1027001
  * 1.25.14-gke.1351000
  * 1.26.9-gke.1345000
  * 1.27.5-gke.1647000

[Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Ubuntu node pools to one of the following versions or later:

  * 1.24.17-gke.2186000
  * 1.25.15-gke.1016000
  * 1.26.9-gke.1548000
  * 1.27.6-gke.1551000
  * 1.28.2-gke.1256000

| High  
  
### GKE on VMware

**Updated:** 2023-11-16

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4623



#### What should I do?

**Note:** Patched versions and a severity assessment for GKE on VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

**Updated:** 2023-11-16

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4623



#### What should I do?

**Note:** Patched versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

**Updated:** 2023-11-16

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4623



#### What should I do?

**Note:** Patched versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Bare Metal

**Updated:** 2023-11-16

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4623



#### What should I do?

There is no action required. GKE on Bare Metal are not affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2023-038

**Published:** 2023-11-06  
**Updated:** 2023-11-21, 2023-12-21  
**Reference:** [CVE-2023-4623](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4623)

**2023-12-21 Update:** Clarify that GKE Autopilot clusters in the default configuration are not impacted.

**2023-11-21 Update:** Clarify that only the listed minor versions need to upgrade to a corresponding patch version for GKE.

### GKE

**Updated:** 2023-11-21, 2023-12-21

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4623

**2023-12-21 Update** : The original bulletin stated Autopilot clusters are impacted, but this was incorrect. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp Unconfined profile or [allow `CAP_NET_ADMIN`.](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies) Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) are not impacted.

#### What should I do?

**2023-11-21 Update:** You only need to upgrade to one of the patch versions that are listed in this bulletin if you use that minor version in your nodes. Minor versions that aren't listed aren't impacted. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following versions or later:

  * 1.24.14-gke.1027001
  * 1.25.14-gke.1351000
  * 1.26.9-gke.1345000
  * 1.27.6-gke.1389000

[Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Ubuntu node pools to one of the following versions or later:

  * 1.24.17-gke.2186000
  * 1.25.15-gke.1016000
  * 1.26.9-gke.1548000
  * 1.27.6-gke.1551000
  * 1.28.2-gke.1256000

| High  
  
### GKE on VMware

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4623



#### What should I do?

**Note:** Patched versions and a severity assessment for GKE on VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4623



#### What should I do?

**Note:** Patched versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4623



#### What should I do?

**Note:** Patched versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4623



#### What should I do?

There is no action required. GKE on Bare Metal are not affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2023-037

**Published:** 2023-11-06  
**Updated:** 2023-11-21, 2023-12-21  
**Reference:** [CVE-2023-4015](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4015)

**2023-12-21 Update:** Clarify that GKE Autopilot clusters in the default configuration are not impacted.

**2023-11-21 Update:** Clarify that only the listed minor versions need to upgrade to a corresponding patch version for GKE.

### GKE

**Updated:** 2023-11-21, 2023-12-21

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4015

**2023-12-21 Update** : The original bulletin stated Autopilot clusters are impacted, but this was incorrect. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp Unconfined profile or [allow `CAP_NET_ADMIN`.](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies) Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) are not impacted.

#### What should I do?

**2023-11-21 Update:** You only need to upgrade to one of the patch versions that are listed in this bulletin if you use that minor version in your nodes. Minor versions that aren't listed aren't impacted. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following versions or later:

  * 1.27.5-gke.1647000

[Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Ubuntu node pools to one of the following versions or later:

  * 1.24.14-gke.1027001
  * 1.25.13-gke.700
  * 1.26.8-gke.700
  * 1.27.5-gke.700
  * 1.28.1-gke.1050000

| High  
  
### GKE on VMware

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4015



#### What should I do?

**Note:** Patched versions and a severity assessment for GKE on VMware are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4015



#### What should I do?

**Note:** Patched versions and a severity assessment for GKE on AWS are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4015



#### What should I do?

**Note:** Patched versions and a severity assessment for GKE on Azure are in progress. We'll update this bulletin with that information when it's available. | Pending  
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4015



#### What should I do?

There is no action required. GKE on Bare Metal are not affected as it does not bundle an operating system in its distribution. | None  
  
## GCP-2023-035

**Published:** 2023-10-26  
**Updated:** 2023-11-21, 2023-12-21  
**Reference:** [CVE-2023-4206](https://cve.mitre.org/cgi-bin/cvename.cgi?name=cve-2023-4206), [CVE-2023-4207](https://cve.mitre.org/cgi-bin/cvename.cgi?name=cve-2023-4207), [CVE-2023-4208](https://cve.mitre.org/cgi-bin/cvename.cgi?name=cve-2023-4208), [CVE-2023-4128](https://cve.mitre.org/cgi-bin/cvename.cgi?name=cve-2023-4128)

**2023-12-21 Update:** Clarify that GKE Autopilot clusters in the default configuration are not impacted.

**2023-11-21 Update:** Clarify that only the listed minor versions need to upgrade to a corresponding patch version for GKE.

### GKE

**Updated:** 2023-11-21, 2023-12-21

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4206
  * CVE-2023-4207
  * CVE-2023-4208
  * CVE-2023-4128

**2023-12-21 Update** : The original bulletin stated Autopilot clusters are impacted, but this was incorrect. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp Unconfined profile or [allow `CAP_NET_ADMIN`.](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies) Autopilot clusters are impacted. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) are not impacted.

#### What should I do?

**2023-11-21 Update:** You only need to upgrade to one of the patch versions that are listed in this bulletin if you use that minor version in your nodes. Minor versions that aren't listed aren't impacted. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following versions or later:

  * 1.24.14-gke.1027001
  * 1.25.13-gke.1008000
  * 1.26.8-gke.1647000
  * 1.27.5-gke.200

[Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Ubuntu node pools to one of the following versions or later:

  * 1.24.14-gke.1027001
  * 1.25.13-gke.1706000
  * 1.26.8-gke.1647000
  * 1.27.5-gke.1648000
  * 1.28.1-gke.1050000

| High  
  
### GKE on VMware

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4206
  * CVE-2023-4207
  * CVE-2023-4208
  * CVE-2023-4128



#### What should I do?

**Note:** Patched versions will be released soon. | High  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4206
  * CVE-2023-4207
  * CVE-2023-4208
  * CVE-2023-4128



#### What should I do?

**Note:** Patched versions will be released soon. | High  
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4206
  * CVE-2023-4207
  * CVE-2023-4208
  * CVE-2023-4128



#### What should I do?

**Note:** Patched versions will be released soon. | High  
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-4206
  * CVE-2023-4207
  * CVE-2023-4208
  * CVE-2023-4128



#### What should I do?

There is no action required. GKE on Bare Metal are not affected as it does not bundle an operating system in its distribution. | High  
  
## GCP-2023-033

**Published:** 2023-10-24  
**Updated:** 2023-11-21, 2023-12-21  
**Reference:** [CVE-2023-3777](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3777)

**2023-12-21 Update:** Clarify that GKE Autopilot clusters in the default configuration are not impacted and GKE Sandbox workloads are not impacted.

**2023-11-21 Update:** Clarify that only the listed minor versions need to upgrade to a corresponding patch version for GKE.

### GKE

**Updated:** 2023-11-21, 2023-12-21

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-3777

**2023-12-21 Update** : The original bulletin stated Autopilot clusters are impacted, but this was incorrect. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp Unconfined profile or [allow `CAP_NET_ADMIN`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies). GKE Sandbox workloads are also not impacted.  Autopilot clusters are impacted. Clusters that use [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) are impacted.

#### What should I do?

**2023-11-21 Update:** You only need to upgrade to one of the patch versions that are listed in this bulletin if you use that minor version in your nodes. Minor versions that aren't listed aren't impacted. [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Container-Optimized OS node pools to one of the following versions or later:

  * 1.24.16-gke.2200
  * 1.25.12-gke.2200
  * 1.26.7-gke.2200
  * 1.27.4-gke.2300

[Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your Ubuntu node pools to one of the following versions or later:

  * 1.24.17-gke.700
  * 1.25.13-gke.700
  * 1.26.8-gke.700
  * 1.27.5-gke.700
  * 1.28.0-gke.100

| High  
  
### GKE on VMware

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-3777



#### What should I do?

**Note:** Patched versions will be released soon. |   
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThe following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-3777



#### What should I do?

**Note:** Patched versions will be released soon. |   
  
### GKE on Azure

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-3777



#### What should I do?

**Note:** Patched versions will be released soon. |   
  
### GKE on Bare Metal

Description | Severity  
---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 

  * CVE-2023-3777



#### What should I do?

There is no action required. GKE on Bare Metal is not affected as it does not bundle an operating system in its distribution. |   
  
## GCP-2023-030

**Published:** 2023-10-10  
**Updated:** 2024-03-20  
**Reference:**[CVE-2023-44487](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-44487)[CVE-2023-39325](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39325)

**2024-03-20 Update:** Added patch versions for GKE on AWS and GKE on Azure  
**2024-02-14 Update:** Added patch versions for GKE on VMware  
**2023-11-09 Update:** Added CVE-2023-39325. Updated GKE versions with the latest patches for CVE-2023-44487 and CVE-2023-39325.

### GKE

**Updated:** 2023-11-09

Description | Severity  
---|---  
A Denial-of-Service (DoS) vulnerability was recently discovered in multiple implementations of the HTTP/2 protocol (CVE-2023-44487), including the golang HTTP server used by Kubernetes. The vulnerability could lead to a DoS of the Google Kubernetes Engine (GKE) control plane. GKE clusters with authorized networks configured are protected by limiting network access, but all other clusters are affected.

#### What should I do?

**2023-11-09 Update:** We have released new versions of GKE that include the Go and Kubernetes security patches, which you can update your clusters to now. In the coming weeks we will release additional changes to the GKE control plane to further mitigate this issue.  The following GKE versions have been updated with patches for CVE-2023-44487 and CVE-2023-39325: 

  * 1.24.17-gke.2155000
  * 1.25.14-gke.1474000
  * 1.26.10-gke.1024000
  * 1.27.7-gke.1038000
  * 1.28.3-gke.1090000



* * *

We recommend that you apply the following mitigation as soon as possible and upgrade to the latest patched version when available. Golang patches will be released on October 10. Once available, we will build and qualify a new Kubernetes API server with those patches and make a GKE patched release. Once the GKE release is available, we will update this bulletin with guidance on which version to upgrade your control plane, and also make the patches visible within GKE [GKE security posture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard) when available for your cluster. To receive a Pub/Sub notification when a patch is available for your channel, [enable cluster notifications](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications#overview). A recent feature of [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions) allows you to apply a patch without having to unsubscribe from a channel. This lets you secure your nodes until the new version becomes the default for your release specific channel. **Mitigate by configuring authorized networks for control plane access:** You can add authorized networks for existing clusters. To learn more see, [authorized network for existing clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks#add). In addition to the authorized networks you add, there are preset IP addresses that can access the GKE control plane. To learn more about these addresses, see [Access to control plane endpoints](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks#access_to_control_plane_endpoints). The following items summarize the cluster isolation:

  * Private clusters with `--master-authorized-networks` and PSC-based clusters with `--master-authorized-networks` and `--no-enable-google-cloud` configured are the most isolated. 
  * Legacy public clusters with `--master-authorized-networks` and PSC-based clusters with `--master-authorized-networks` and `--enable-google-cloud` (default) configured are additionally accessible by the following: 
    * Public IP addresses of all Compute Engine VMs in Google Cloud 
    * Google Cloud platform IP addresses 



#### What vulnerabilities are addressed by this patch?

The vulnerability, CVE-2023-44487, allows an attacker to execute a denial-of-service attack on GKE control plane nodes. | High  
  
### GKE on VMware

**Updated:** 2024-02-14

Description | Severity  
---|---  
A Denial-of-Service (DoS) vulnerability was recently discovered in multiple implementations of the HTTP/2 protocol (CVE-2023-44487), including the golang HTTP server used by Kubernetes. The vulnerability could lead to a DoS of the Kubernetes control plane. GKE on VMware creates Kubernetes clusters that are not directly accessible to the Internet by default and are protected from this vulnerability.

#### What should I do?

**2024-02-14 Update:** The following versions of GKE on VMware are updated with code to fix this vulnerability. Upgrade your clusters to the following patch versions or later:

  * 1.28.100
  * 1.16.6
  * 1.15.8



* * *

If you have configured your GKE on VMware Kubernetes clusters to have direct access to the Internet or other untrusted networks, we recommend working with your firewall administrator to block or limit that access. We recommend that you upgrade to the latest patch version, when available, as soon as possible. Golang patches will be released on October 10. Once available, we will build and qualify a new Kubernetes API server with those patches and make a GKE patched release. Once the GKE release is available, we will update this bulletin with guidance on which version to upgrade your control plane to.

#### What vulnerabilities are addressed by this patch?

The vulnerability, CVE-2023-44487, allows an attacker to execute a denial-of-service attack on Kubernetes control plane nodes. | High  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSA Denial-of-Service (DoS) vulnerability was recently discovered in multiple implementations of the HTTP/2 protocol (CVE-2023-44487), including the golang HTTP server used by Kubernetes. The vulnerability could lead to a DoS of the Kubernetes control plane. GKE on AWS creates private Kubernetes clusters that are not directly accessible to the Internet by default and are protected from this vulnerability.

#### What should I do?

**2024-03-20 Update:** The following GKE on AWS versions have been updated with patches for CVE-2023-44487: 

  * 1.26.10-gke.600
  * 1.27.7-gke.600
  * 1.28.3-gke.700



* * *

If you have configured your GKE on AWS to have direct access to the Internet or other untrusted networks, we recommend working with your firewall administrator to block or limit that access. We recommend that you upgrade to the latest patch version, when available, as soon as possible. Golang patches will be released on October 10. Once available, we will build and qualify a new Kubernetes API server with those patches and make a GKE patched release. Once the GKE release is available, we will update this bulletin with guidance on which version to upgrade your control plane to.

#### What vulnerabilities are addressed by this patch?

The vulnerability, CVE-2023-44487, allows an attacker to execute a denial-of-service attack on Kubernetes control plane nodes. | High  
  
### GKE on Azure

Description | Severity  
---|---  
A Denial-of-Service (DoS) vulnerability was recently discovered in multiple implementations of the HTTP/2 protocol (CVE-2023-44487), including the golang HTTP server used by Kubernetes. The vulnerability could lead to a DoS of the Kubernetes control plane. GKE on Azure creates private Kubernetes clusters that are not directly accessible to the Internet by default and are protected from this vulnerability.

#### What should I do?

**2024-03-20 Update:** The following GKE on Azure versions have been updated with patches for CVE-2023-44487: 

  * 1.26.10-gke.600
  * 1.27.7-gke.600
  * 1.28.3-gke.700



* * *

If you have configured your GKE on Azure clusters to have direct access to the Internet or other untrusted networks, we recommend working with your firewall administrator to block or limit that access. We recommend that you upgrade to the latest patch version, when available, as soon as possible. Golang patches will be released on October 10. Once available, we will build and qualify a new Kubernetes API server with those patches and make a GKE patched release. Once the GKE release is available, we will update this bulletin with guidance on which version to upgrade your control plane to. 

#### What vulnerabilities are addressed by this patch?

The vulnerability, CVE-2023-44487, allows an attacker to execute a denial-of-service attack on Kubernetes control plane nodes. | High  
  
### GKE on Bare Metal

Description | Severity  
---|---  
A Denial-of-Service (DoS) vulnerability was recently discovered in multiple implementations of the HTTP/2 protocol (CVE-2023-44487), including the golang HTTP server used by Kubernetes. The vulnerability could lead to a DoS of the Kubernetes control plane. Anthos on Bare Metal creates Kubernetes clusters that are not directly accessible to the Internet by default and are protected from this vulnerability.

#### What should I do?

If you have configured your Anthos on Bare Metal Kubernetes clusters to have direct access to the Internet or other untrusted networks, we recommend working with your firewall administrator to block or limit that access. To learn more, see the [GKE on Bare Metal security overview](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/security-overview#network_security). We recommend that you upgrade to the latest patch version, when available, as soon as possible. Golang patches will be released on October 10. Once available, we will build and qualify a new Kubernetes API server with those patches and make a GKE patched release. Once the GKE release is available, we will update this bulletin with guidance on which version to upgrade your control plane to.

#### What vulnerabilities are addressed by this patch?

The vulnerability, CVE-2023-44487, allows an attacker to execute a denial-of-service attack on Kubernetes control plane nodes. | High  
  
## GCP-2023-026

**Published:** 2023-09-06  
**Reference:**[CVE-2023-3676](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3676), [CVE-2023-3955](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3955), [ CVE-2023-3893](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3893)

### GKE

Description | Severity  
---|---  
Three vulnerabilities (CVE-2023-3676, CVE-2023-3955, CVE-2023-3893) have been discovered in Kubernetes where a user that can create Pods on Windows nodes may be able to escalate to admin privileges on those nodes. These vulnerabilities affect the Windows versions of Kubelet and the Kubernetes CSI proxy. GKE clusters are only affected if they include Windows nodes.

#### What should I do?

The following versions of GKE have been updated with code to fix this vulnerability. For security purposes, even if you have node auto-upgrade enabled, we recommend that you [manually upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) your cluster and node pools to one of the following GKE versions:

  * 1.24.17-gke.200
  * 1.25.13-gke.200
  * 1.26.8-gke.200
  * 1.27.5-gke.200
  * 1.28.1-gke.200

The GKE control plane will be updated the week of 2023-09-04 to update the csi-proxy to version 1.1.3. If you update your nodes prior to the control plane update, you will need to update your nodes again after the update to take advantage of the new proxy. You can update the nodes again, even without changing the node version, by running the `gcloud container clusters upgrade` command and passing the `--cluster-version` flag with the same GKE version that the node pool is already running. You must use the gcloud CLI for this workaround. Note that this will cause an update regardless of [maintenance windows](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#node-recreation-maintenance-windows). A recent feature of [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions) allows you to apply a patch without having to unsubscribe from a channel. This lets you secure your nodes until the new version becomes the default for your specific release channel.

#### What vulnerabilities are addressed by this patch?

With CVE-2023-3676, a malicious actor could craft a Pod spec with host path strings that contain PowerShell commands. Kubelet lacks input sanitization and passes this crafted path string to the command executor as an argument where it would execute parts of the string as separate commands. These commands would run with the same administrative privileges as Kubelet has. With CVE-2023-3955, Kubelet grants users who can create Pods the ability to execute code at the same permission level as the Kubelet agent, privileged permissions. With CVE-2023-3893, a similar lack of input sanitation lets a user who can create Pods on Windows nodes running kubernetes-csi-proxy to escalate to admin privileges on those nodes. Kubernetes audit logs can be used to detect if this vulnerability is being exploited. Pod create events with embedded PowerShell commands are a strong indication of exploitation. ConfigMaps and Secrets that contain embedded PowerShell commands and are mounted into Pods are also a strong indication of exploitation. | High  
  
### GKE on VMware

Description | Severity  
---|---  
Three vulnerabilities (CVE-2023-3676, CVE-2023-3955, CVE-2023-3893) have been discovered in Kubernetes where a user that can create Pods on Windows nodes may be able to escalate to admin privileges on those nodes. These vulnerabilities affect the Windows versions of Kubelet and the Kubernetes CSI proxy. Clusters are only affected if they include Windows nodes.

#### What should I do?

Patched versions of GKE on VMware will be released soon. This security bulletin will be updated when new GKE on VMware versions are available.

#### What vulnerabilities are addressed by this patch?

With CVE-2023-3676, a malicious actor could craft a Pod spec with host path strings that contain PowerShell commands. Kubelet lacks input sanitization and passes this crafted path string to the command executor as an argument where it would execute parts of the string as separate commands. These commands would run with the same administrative privileges as Kubelet has. With CVE-2023-3955, Kubelet grants users who can create Pods the ability to execute code at the same permission level as the Kubelet agent, privileged permissions. With CVE-2023-3893, a similar lack of input sanitation lets a user who can create Pods on Windows nodes running kubernetes-csi-proxy to escalate to admin privileges on those nodes. Kubernetes audit logs can be used to detect if this vulnerability is being exploited. Pod create events with embedded PowerShell commands are a strong indication of exploitation. ConfigMaps and Secrets that contain embedded PowerShell commands and are mounted into Pods are also a strong indication of exploitation. | High  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSThree vulnerabilities (CVE-2023-3676, CVE-2023-3955, CVE-2023-3893) have been discovered in Kubernetes where a user that can create Pods on Windows nodes may be able to escalate to admin privileges on those nodes. These vulnerabilities affect the Windows versions of Kubelet and the Kubernetes CSI proxy.

#### What should I do?

GKE on AWS is not affected by these CVEs. No action is required. | None  
  
### GKE on Azure

Description | Severity  
---|---  
Three vulnerabilities (CVE-2023-3676, CVE-2023-3955, CVE-2023-3893) have been discovered in Kubernetes where a user that can create Pods on Windows nodes may be able to escalate to admin privileges on those nodes. These vulnerabilities affect the Windows versions of Kubelet and the Kubernetes CSI proxy.

#### What should I do?

GKE on Azure is not affected by these CVEs. No action is required. | None  
  
### GKE on Bare Metal

Description | Severity  
---|---  
Three vulnerabilities (CVE-2023-3676, CVE-2023-3955, CVE-2023-3893) have been discovered in Kubernetes where a user that can create Pods on Windows nodes may be able to escalate to admin privileges on those nodes. These vulnerabilities affect the Windows versions of Kubelet and the Kubernetes CSI proxy.

#### What should I do?

GKE on Bare Metal is not affected by these CVEs. No action is required. | None  
  
## GCP-2023-018

**Published:** 2023-06-27  
**Reference:**[CVE-2023-2235](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2235)

### GKE

Description | Severity  
---|---  
A new vulnerability (CVE-2023-2235) has been discovered in the Linux kernel that can lead to a privilege escalation on the node. GKE Autopilot clusters are affected as GKE Autopilot nodes always use Container-Optimized OS node images. GKE Standard clusters with versions 1.25 or later that are running Container-Optimized OS node images are affected. GKE clusters are not affected if they are running only Ubuntu node images, or running versions before 1.25, or using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods).

#### What should I do?

The following versions of GKE have been updated with code to fix this vulnerability. For security purposes, even if you have node auto-upgrade enabled, we recommend that you [manually upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your cluster and node pools to one of the following GKE versions:

  * 1.25.9-gke.1400
  * 1.26.4-gke.1500
  * 1.27.1-gke.2400

A recent feature of [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions) allows you to apply a patch without having to unsubscribe from a channel. This lets you secure your nodes until the new version becomes the default for your release specific channel.

#### What vulnerabilities are being addressed?

With CVE-2023-2235, the perf_group_detach function did not check the event's siblings' attach_state before calling add_event_to_groups(), but remove_on_exec made it possible to call list_del_event() on before detaching from their group, making it possible to use a dangling pointer causing a use-after-free vulnerability. | High  
  
### GKE on VMware

Description | Severity  
---|---  
A new vulnerability (CVE-2023-2235) has been discovered in the Linux kernel that can lead to a privilege escalation on the node. GKE on VMware clusters are affected.

#### What should I do?

**Note:** Patched versions of GKE on VMware will be released soon. This security bulletin will be updated when new GKE on VMware versions are available.

#### What vulnerabilities are being addressed?

With CVE-2023-2235, the perf_group_detach function did not check the event's siblings' attach_state before calling add_event_to_groups(), but remove_on_exec made it possible to call list_del_event() on before detaching from their group, making it possible to use a dangling pointer causing a use-after-free vulnerability. | High  
  
### GKE on AWS

Description | Severity  
---|---  
A new vulnerability (CVE-2023-2235) has been discovered in the Linux kernel that can lead to a privilege escalation on the node. GKE on AWS clusters are affected.

#### What should I do?

**Note:** Patched versions of GKE on AWS will be released soon. This security bulletin will be updated when new GKE on AWS versions are available.

#### What vulnerabilities are addressed by this patch?

With CVE-2023-2235, the perf_group_detach function did not check the event's siblings' attach_state before calling add_event_to_groups(), but remove_on_exec made it possible to call list_del_event() on before detaching from their group, making it possible to use a dangling pointer causing a use-after-free vulnerability. | High  
  
### GKE on Azure

Description | Severity  
---|---  
A new vulnerability (CVE-2023-2235) has been discovered in the Linux kernel that can lead to a privilege escalation on the node. GKE on Azure clusters are affected.

#### What should I do?

**Note:** Patched versions of GKE on Azure will be released soon. This security bulletin will be updated when new GKE on Azure versions are available.

#### What vulnerabilities are addressed by this patch?

With CVE-2023-2235, the perf_group_detach function did not check the event's siblings' attach_state before calling add_event_to_groups(), but remove_on_exec made it possible to call list_del_event() on before detaching from their group, making it possible to use a dangling pointer causing a use-after-free vulnerability. | High  
  
### GKE on Bare Metal

Description | Severity  
---|---  
A new vulnerability (CVE-2023-2235) has been discovered in the Linux kernel that can lead to a privilege escalation on the node. Google Distributed Cloud Virtual for Bare Metal is not affected by this CVE.

#### What should I do?

No action is required. | None  
  
## GCP-2023-017

**Published:** 2023-06-26  
**Updated:** 2023-07-11  
**Reference:**[CVE-2023-31436](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-31436)

**2023-07-11 Update:** New GKE versions have been updated to include the latest Ubuntu versions that patch CVE-2023-31436.

### GKE

**Updated:** 2023-07-11

Description | Severity  
---|---  
A new vulnerability (CVE-2023-31436) has been discovered in the Linux kernel that can lead to a privilege escalation on the node. GKE clusters, including Autopilot clusters, are affected. GKE clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) are not affected.

#### What should I do?

**2023-07-11 Update:** Ubuntu patch versions are available. The following GKE versions have been updated to include the latest Ubuntu versions that patch CVE-2023-31436: 

  * 1.23.17-gke.8200
  * 1.24.14-gke.2600
  * 1.25.10-gke.2700
  * 1.26.5-gke.2700
  * 1.27.2-gke.2700



* * *

The following versions of GKE have been updated with code to fix this vulnerability. For security purposes, even if you have node auto-upgrade enabled, we recommend that you [manually upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your cluster and node pools to one of the following GKE versions:

  * 1.22.17-gke.11400
  * 1.23.17-gke.6800
  * 1.24.14-gke.1200
  * 1.25.10-gke.1200
  * 1.26.5-gke.1200
  * 1.27.2-gke.1200

A recent feature of [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions) allows you to apply a patch without having to unsubscribe from a channel. This lets you secure your nodes until the new version becomes the default for your release specific channel.

#### What vulnerabilities are being addressed?

With CVE-2023-31436, an out-of-bounds memory access flaw was found in the Linux kernel's traffic control (QoS) subsystem in how a user triggers the qfq_change_class function with an incorrect MTU value of the network device used as lmax. This flaw allows a local user to crash or potentially escalate their privileges on the system. | High  
  
### GKE on VMware

Description | Severity  
---|---  
A new vulnerability (CVE-2023-31436) has been discovered in the Linux kernel that can lead to a privilege escalation on the node. GKE on VMware clusters are affected.

#### What should I do?

**Note:** Patched versions of GKE on VMware will be released soon. This security bulletin will be updated when new GKE on VMware versions are available.

#### What vulnerabilities are being addressed?

With CVE-2023-31436, an out-of-bounds memory access flaw was found in the Linux kernel's traffic control (QoS) subsystem in how a user triggers the qfq_change_class function with an incorrect MTU value of the network device used as lmax. This flaw allows a local user to crash or potentially escalate their privileges on the system. | High  
  
### GKE on AWS

Description | Severity  
---|---  
A new vulnerability (CVE-2023-31436) has been discovered in the Linux kernel that can lead to a privilege escalation on the node. GKE on AWS clusters are affected.

#### What should I do?

**Note:** Patched versions of GKE on AWS will be released soon. This security bulletin will be updated when new GKE on AWS versions are available.

#### What vulnerabilities are addressed by this patch?

With CVE-2023-31436, an out-of-bounds memory access flaw was found in the Linux kernel's traffic control (QoS) subsystem in how a user triggers the qfq_change_class function with an incorrect MTU value of the network device used as lmax. This flaw allows a local user to crash or potentially escalate their privileges on the system. | High  
  
### GKE on Azure

Description | Severity  
---|---  
A new vulnerability (CVE-2023-31436) has been discovered in the Linux kernel that can lead to a privilege escalation on the node. GKE on Azure clusters are affected. 

#### What should I do?

**Note:** Patched versions of GKE on Azure will be released soon. This security bulletin will be updated when new GKE on Azure versions are available.

#### What vulnerabilities are addressed by this patch?

With CVE-2023-31436, an out-of-bounds memory access flaw was found in the Linux kernel's traffic control (QoS) subsystem in how a user triggers the qfq_change_class function with an incorrect MTU value of the network device used as lmax. This flaw allows a local user to crash or potentially escalate their privileges on the system. | High  
  
### GKE on Bare Metal

Description | Severity  
---|---  
A new vulnerability (CVE-2023-31436) has been discovered in the Linux kernel that can lead to a privilege escalation on the node. Google Distributed Cloud Virtual for Bare Metal is not affected by this CVE.

#### What should I do?

No action is required. | None  
  
## GCP-2023-016

**Published:** 2023-06-26  
**Reference:** [CVE-2023-27496](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27496), [CVE-2023-27488](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27488), [CVE-2023-27493](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27493), [CVE-2023-27492](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27492), [CVE-2023-27491](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27491), [CVE-2023-27487](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27487)

### GKE

Description | Severity  
---|---  
A number of vulnerabilities have been discovered in Envoy, which is used in Cloud Service Mesh (ASM). These were reported separately as [GCP-2023-002](https://docs.cloud.google.com/support/bulletins#gcp-2023-002).  GKE does not ship with ASM and is not affected by these vulnerabilities. 

#### What should I do?

If you have separately installed ASM for your GKE clusters, please see [GCP-2023-002](https://docs.cloud.google.com/support/bulletins#gcp-2023-002).  | None  
  
### GKE on VMware

Description | Severity  
---|---  
A number of vulnerabilities (CVE-2023-27496, CVE-2023-27488, CVE-2023-27493, CVE-2023-27492, CVE-2023-27491, CVE-2023-27487), have been discovered in Envoy, which is used in Cloud Service Mesh in GKE on VMware, that allows a malicious attacker to cause a denial of service or crash Envoy. These were reported separately as [GCP-2023-002](https://docs.cloud.google.com/support/bulletins#gcp-2023-002), but we want to ensure that GKE Enterprise customers update their versions that include ASM. 

#### What should I do?

The following versions of GKE on VMware have been updated with code to fix this vulnerability. We recommend that you upgrade your admin and user clusters to one of the following GKE on VMware versions: 

  * 1.13.8
  * 1.14.5
  * 1.15.1



#### What vulnerabilities are addressed by this patch?

CVE-2023-27496: If Envoy is running with the OAuth filter enabled exposed, a malicious actor could construct a request which would cause denial of service by crashing Envoy.  CVE-2023-27488: Attackers can use this vulnerability to bypass auth checks when ext_authz is used.  CVE-2023-27493: Envoy configuration must also include an option to add request headers that were generated using inputs from the request, such as the peer certificate SAN.  CVE-2023-27492: Attackers can send large request bodies for routes that have Lua filter enabled and trigger crashes.  CVE-2023-27491: Attackers can send specifically crafted HTTP/2 or HTTP/3 requests to trigger parsing errors on HTTP/1 upstream service.  CVE-2023-27487: The header `x-envoy-original-path` should be an internal header, but Envoy does not remove this header from the request at the beginning of request processing when it is sent from an untrusted client.  | High  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWS A number of vulnerabilities (CVE-2023-27496, CVE-2023-27488, CVE-2023-27493, CVE-2023-27492, CVE-2023-27491, CVE-2023-27487), have been discovered in Envoy, which is used in Cloud Service Mesh. These were reported separately as [GCP-2023-002](https://docs.cloud.google.com/support/bulletins#gcp-2023-002).  GKE on AWS does not ship with ASM and is not affected. 

#### What should I do?

No action is required. | None  
  
### GKE on Azure

Description | Severity  
---|---  
A number of vulnerabilities (CVE-2023-27496, CVE-2023-27488, CVE-2023-27493, CVE-2023-27492, CVE-2023-27491, CVE-2023-27487), have been discovered in Envoy, which is used in Cloud Service Mesh. These were reported separately as [GCP-2023-002](https://docs.cloud.google.com/support/bulletins#gcp-2023-002).  GKE on Azure does not ship with ASM and is not affected. 

#### What should I do?

No action is required. | None  
  
### GKE on Bare Metal

Description | Severity  
---|---  
A number of vulnerabilities (CVE-2023-27496, CVE-2023-27488, CVE-2023-27493, CVE-2023-27492, CVE-2023-27491, CVE-2023-27487), have been discovered in Envoy, which is used in Cloud Service Mesh in GKE on Bare Metal, that allows a malicious attacker to cause a denial of service or crash Envoy. These were reported separately as [GCP-2023-002](https://docs.cloud.google.com/support/bulletins#gcp-2023-002), but we want to ensure that GKE Enterprise customers update their versions that include ASM. 

#### What should I do?

The following versions of GKE on Bare Metal have been updated with code to fix this vulnerability. We recommend that you upgrade your admin and user clusters to one of the following GKE on Bare Metal versions: 

  * 1.13.9
  * 1.14.6
  * 1.15.2



#### What vulnerabilities are addressed by this patch?

CVE-2023-27496: If Envoy is running with the OAuth filter enabled exposed, a malicious actor could construct a request which would cause denial of service by crashing Envoy.  CVE-2023-27488: Attackers can use this vulnerability to bypass auth checks when ext_authz is used.  CVE-2023-27493: Envoy configuration must also include an option to add request headers that were generated using inputs from the request, such as the peer certificate SAN.  CVE-2023-27492: Attackers can send large request bodies for routes that have Lua filter enabled and trigger crashes.  CVE-2023-27491: Attackers can send specifically crafted HTTP/2 or HTTP/3 requests to trigger parsing errors on HTTP/1 upstream service.  CVE-2023-27487: The header `x-envoy-original-path` should be an internal header, but Envoy does not remove this header from the request at the beginning of request processing when it is sent from an untrusted client.  | High  
  
## GCP-2023-015

**Published:** 2023-06-20  
**Reference:**[CVE-2023-0468](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0468)

### GKE

Description | Severity  
---|---  
A new vulnerability (CVE-2023-0468) has been discovered in version 5.15 of the Linux kernel that can lead to a denial of service on the node. GKE clusters, including Autopilot clusters, are affected. GKE clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) are not affected.

#### What should I do?

The following versions of GKE have been updated with code to fix this vulnerability. For security purposes, even if you have node auto-upgrade enabled, we recommend that you [manually upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your cluster and node pools to one of the following GKE versions:

  * 1.25.7-gke.1200
  * 1.26.2-gke.1200

A recent feature of [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions) allows you to apply a patch without having to unsubscribe from a channel. This lets you secure your nodes until the new version becomes the default for your release specific channel.

#### What vulnerabilities are being addressed?

In CVE-2023-0468, a use-after-free flaw was found in io_uring/poll.c in io_poll_check_events in the io_uring subcomponent in the Linux Kernel. This flaw may cause a NULL pointer dereference, and potentially a system crash leading to a denial of service. | Medium  
  
### GKE on VMware

Description | Severity  
---|---  
A new vulnerability (CVE-2023-0468) has been discovered in version 5.15 of the Linux kernel that can lead to a denial of service on the node. GKE on VMware uses version 5.4 of the Linux Kernel and is not affected by this CVE.

#### What should I do?

  * No action is needed

| None  
  
### GKE on AWS

Description | Severity  
---|---  
A new vulnerability (CVE-2023-0468) has been discovered in version 5.15 of the Linux kernel that can lead to a denial of service on the node. GKE on AWS is not affected by this CVE.

#### What should I do?

  * No action is needed

| None  
  
### GKE on Azure

Description | Severity  
---|---  
A new vulnerability (CVE-2023-0468) has been discovered in version 5.15 of the Linux kernel that can lead to a denial of service on the node. GKE on Azure is not affected by this CVE.

#### What should I do?

  * No action is needed

| None  
  
### GKE on Bare Metal

Description | Severity  
---|---  
A new vulnerability (CVE-2023-0468) has been discovered in version 5.15 of the Linux kernel that can lead to a denial of service on the node. Google Distributed Cloud Virtual for Bare Metal is not affected by this CVE.

#### What should I do?

  * No action is needed

| None  
  
## GCP-2023-014

**Published:** 2023-06-15  
**Updated:** 2023-08-11  
**Reference:**[CVE-2023-2727](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2727), [CVE-2023-2728](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2728)

**2023-08-11 Update:** Added patch versions for GKE on VMware, GKE on AWS, GKE on Azure, and GKE on Bare Metal

### GKE

Description | Severity  
---|---  
Two new security issues were discovered in Kubernetes where users may be able to launch containers that bypass policy restrictions when using ephemeral containers and either ImagePolicyWebhook (CVE-2023-2727) or the ServiceAccount admission plugin (CVE-2023-2728). GKE does not use ImagePolicyWebhook and is not affected by CVE-2023-2727.  All versions of GKE are potentially vulnerable to CVE-2023-2728. 

#### What should I do?

The following versions of GKE have been updated with code to fix this vulnerability. For security purposes, even if you have node auto-upgrade enabled, we recommend that you [manually upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your cluster and node pools to one of the following GKE versions:

  * 1.27.2-gke.1200
  * 1.26.5-gke.1200
  * 1.25.10-gke.1200
  * 1.24.14-gke.1200
  * 1.23.17-gke.6800

A recent feature of [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions) allows you to apply a patch without having to unsubscribe from a channel. This lets you secure your nodes until the new version becomes the default for your specific release channel.

#### What vulnerabilities are being addressed?

With CVE-2023-2727, users may be able to launch containers using images that are restricted by ImagePolicyWebhook when using ephemeral containers. Kubernetes clusters are only affected if the ImagePolicyWebhook admission plugin is used together with ephemeral containers. This CVE can also be mitigated by using validation webhooks, such as Gatekeeper and Kyverno, to enforce the same restrictions. In CVE-2023-2728, users may be able to launch containers that bypass the mountable secrets policy enforced by the ServiceAccount admission plugin when using ephemeral containers. The policy ensures that Pods running with a service account may only reference secrets specified in the service account's secrets field. Clusters are impacted by this vulnerability if:

  * The ServiceAccount admission plugin is used. 
  * The kubernetes.io/enforce-mountable-secrets annotation is used by a service account. This annotation is not added by default. 
  * Pods are using ephemeral containers.

| Medium  
  
### GKE on VMware

**Updated:** 2023-08-11

Description | Severity  
---|---  
Two new security issues were discovered in Kubernetes where users may be able to launch containers that bypass policy restrictions when using ephemeral containers and either ImagePolicyWebhook (CVE-2023-2727) or the ServiceAccount admission plugin (CVE-2023-2728) Anthos on VMware does not use ImagePolicyWebhook and is not affected by CVE-2023-2727. All versions of Anthos on VMware are potentially vulnerable to CVE-2023-2728.

#### What should I do?

**2023-08-11 Update:** The following versions of GKE on VMware have been updated with code to fix this vulnerability. Upgrade your admin and user clusters to one of the following GKE on VMware versions:

  * 1.13.10
  * 1.14.6
  * 1.15.3



* * *

**Note:** Patched versions of Anthos on VMware will be released soon. This security bulletin will be updated when new Anthos on VMware versions are available.

#### What vulnerabilities are being addressed?

With CVE-2023-2727, users may be able to launch containers using images that are restricted by ImagePolicyWebhook when using ephemeral containers. Kubernetes clusters are only affected if the ImagePolicyWebhook admission plugin is used together with ephemeral containers. This CVE can also be mitigated by using validation webhooks, such as Gatekeeper and Kyverno, to enforce the same restrictions. In CVE-2023-2728, users may be able to launch containers that bypass the mountable secrets policy enforced by the ServiceAccount admission plugin when using ephemeral containers. The policy ensures that Pods running with a service account may only reference secrets specified in the service account's secrets field. Clusters are impacted by this vulnerability if:

  * The ServiceAccount admission plugin is used. 
  * The kubernetes.io/enforce-mountable-secrets annotation is used by a service account. This annotation is not added by default. 
  * Pods are using ephemeral containers.

| Medium  
  
### GKE on AWS

**Updated:** 2023-08-11

Description | Severity  
---|---  
Two new security issues were discovered in Kubernetes where users may be able to launch containers that bypass policy restrictions when using ephemeral containers and either ImagePolicyWebhook (CVE-2023-2727) or the ServiceAccount admission plugin (CVE-2023-2728)  
Anthos on AWS does not use ImagePolicyWebhook and is not affected by CVE-2023-2727.   
All versions of Anthos on AWS are potentially vulnerable to CVE-2023-2728.  


#### What should I do?

**2023-08-11 Update:** The following version of GKE on AWS has been updated with code to fix this vulnerability. Upgrade your nodes to the following GKE on AWS version:

  * 1.15.2



* * *

**Note:** Patched versions of Anthos on AWS will be released soon. This security bulletin will be updated when new Anthos on VMware versions are available.

#### What vulnerabilities are being addressed?

With CVE-2023-2727, users may be able to launch containers using images that are restricted by ImagePolicyWebhook when using ephemeral containers. Kubernetes clusters are only affected if the ImagePolicyWebhook admission plugin is used together with ephemeral containers. This CVE can also be mitigated by using validation webhooks, such as Gatekeeper and Kyverno, to enforce the same restrictions. In CVE-2023-2728, users may be able to launch containers that bypass the mountable secrets policy enforced by the ServiceAccount admission plugin when using ephemeral containers. The policy ensures that Pods running with a service account may only reference secrets specified in the service account's secrets field. Clusters are impacted by this vulnerability if:

  * The ServiceAccount admission plugin is used. 
  * The kubernetes.io/enforce-mountable-secrets annotation is used by a service account. This annotation is not added by default. 
  * Pods are using ephemeral containers.

| Medium  
  
### GKE on Azure

**Updated:** 2023-08-11

Description | Severity  
---|---  
Two new security issues were discovered in Kubernetes where users may be able to launch containers that bypass policy restrictions when using ephemeral containers and either ImagePolicyWebhook (CVE-2023-2727) or the ServiceAccount admission plugin (CVE-2023-2728)  
Anthos on Azure does not use ImagePolicyWebhook and is not affected by CVE-2023-2727.   
All versions of Anthos on Azure are potentially vulnerable to CVE-2023-2728.  


#### What should I do?

**2023-08-11 Update:** The following version of GKE on Azure has been updated with code to fix this vulnerability. Upgrade your nodes to the following GKE on Azure version:

  * 1.15.2



* * *

**Note:** Patched versions of Anthos on Azure will be released soon. This security bulletin will be updated when new Anthos on Azure versions are available.

#### What vulnerabilities are being addressed?

With CVE-2023-2727, users may be able to launch containers using images that are restricted by ImagePolicyWebhook when using ephemeral containers. Kubernetes clusters are only affected if the ImagePolicyWebhook admission plugin is used together with ephemeral containers. This CVE can also be mitigated by using validation webhooks, such as Gatekeeper and Kyverno, to enforce the same restrictions. In CVE-2023-2728, users may be able to launch containers that bypass the mountable secrets policy enforced by the ServiceAccount admission plugin when using ephemeral containers. The policy ensures that Pods running with a service account may only reference secrets specified in the service account's secrets field. Clusters are impacted by this vulnerability if:

  * The ServiceAccount admission plugin is used. 
  * The kubernetes.io/enforce-mountable-secrets annotation is used by a service account. This annotation is not added by default. 
  * Pods are using ephemeral containers.

| Medium  
  
### GKE on Bare Metal

**Updated:** 2023-08-11

Description | Severity  
---|---  
Two new security issues were discovered in Kubernetes where users may be able to launch containers that bypass policy restrictions when using ephemeral containers and either ImagePolicyWebhook (CVE-2023-2727) or the ServiceAccount admission plugin (CVE-2023-2728)  
Anthos on Bare Metal does not use ImagePolicyWebhook and is not affected by CVE-2023-2727.   
All versions of Anthos on Bare Metal are potentially vulnerable to CVE-2023-2728.  


#### What should I do?

**2023-08-11 Update:** The following versions of Google Distributed Cloud Virtual for Bare Metal have been updated with code to fix this vulnerability. Upgrade your nodes to one of the following Google Distributed Cloud Virtual for Bare Metal versions:

  * 1.13.9
  * 1.14.7
  * 1.15.3



* * *

**Note:** Patched versions of Anthos on Bare Metal will be released soon. This security bulletin will be updated when new Anthos on VMware versions are available.

#### What vulnerabilities are being addressed?

With CVE-2023-2727, users may be able to launch containers using images that are restricted by ImagePolicyWebhook when using ephemeral containers. Kubernetes clusters are only affected if the ImagePolicyWebhook admission plugin is used together with ephemeral containers. This CVE can also be mitigated by using validation webhooks, such as Gatekeeper and Kyverno, to enforce the same restrictions. In CVE-2023-2728, users may be able to launch containers that bypass the mountable secrets policy enforced by the ServiceAccount admission plugin when using ephemeral containers. The policy ensures that Pods running with a service account may only reference secrets specified in the service account's secrets field. Clusters are impacted by this vulnerability if:

  * The ServiceAccount admission plugin is used. 
  * The kubernetes.io/enforce-mountable-secrets annotation is used by a service account. This annotation is not added by default. 
  * Pods are using ephemeral containers.

| Medium  
  
## GCP-2023-009

**Published:** 2023-06-06  
**Reference:**[CVE-2023-2878](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2878)

### GKE

Description | Severity  
---|---  
A new vulnerability (CVE-2023-2878) has been discovered in the secrets-store-csi-driver where an actor with access to the driver logs could observe service account tokens. These tokens could then potentially be exchanged with external cloud providers to access secrets stored in cloud vault solutions. GKE is not affected by this CVE.

#### What should I do?

While GKE is not affected, if you have installed the secrets-store-csi-driver component, you should update your installation with a patched version.

#### What vulnerabilities are addressed by this patch?

The vulnerability, CVE-2023-2878, was discovered in secrets-store-csi-driver where an actor with access to the driver logs could observe service account tokens. These tokens could then potentially be exchanged with external cloud providers to access secrets stored in cloud vault solutions. Tokens are only logged when TokenRequests is configured in the CSIDriver object and the driver is set to run at log level 2 or greater via the -v flag.  | None  
  
### GKE on VMware

Description | Severity  
---|---  
A new vulnerability (CVE-2023-2878) has been discovered in the secrets-store-csi-driver where an actor with access to the driver logs could observe service account tokens. These tokens could then potentially be exchanged with external cloud providers to access secrets stored in cloud vault solutions. GKE on VMware is not affected by this CVE.

#### What should I do?

While GKE on VMware is not affected, if you have installed the secrets-store-csi-driver component, you should update your installation with a patched version.

#### What vulnerabilities are addressed by this patch?

The vulnerability, CVE-2023-2878, was discovered in secrets-store-csi-driver where an actor with access to the driver logs could observe service account tokens. These tokens could then potentially be exchanged with external cloud providers to access secrets stored in cloud vault solutions. Tokens are only logged when TokenRequests is configured in the CSIDriver object and the driver is set to run at log level 2 or greater via the -v flag. | None  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSA new vulnerability (CVE-2023-2878) has been discovered in the secrets-store-csi-driver where an actor with access to the driver logs could observe service account tokens. These tokens could then potentially be exchanged with external cloud providers to access secrets stored in cloud vault solutions. GKE on AWS is not affected by this CVE.

#### What should I do?

While GKE on AWS is not affected, if you have installed the secrets-store-csi-driver component, you should update your installation with a patched version.

#### What vulnerabilities are addressed by this patch?

The vulnerability, CVE-2023-2878, was discovered in secrets-store-csi-driver where an actor with access to the driver logs could observe service account tokens. These tokens could then potentially be exchanged with external cloud providers to access secrets stored in cloud vault solutions. Tokens are only logged when TokenRequests is configured in the CSIDriver object and the driver is set to run at log level 2 or greater via the -v flag. | None  
  
### GKE on Azure

Description | Severity  
---|---  
A new vulnerability (CVE-2023-2878) has been discovered in the secrets-store-csi-driver where an actor with access to the driver logs could observe service account tokens. These tokens could then potentially be exchanged with external cloud providers to access secrets stored in cloud vault solutions. GKE on Azure is not affected by this CVE

#### What should I do?

While GKE on Azure is not affected, if you have installed the secrets-store-csi-driver component, you should update your installation with a patched version.

#### What vulnerabilities are addressed by this patch?

The vulnerability, CVE-2023-2878, was discovered in secrets-store-csi-driver where an actor with access to the driver logs could observe service account tokens. These tokens could then potentially be exchanged with external cloud providers to access secrets stored in cloud vault solutions. Tokens are only logged when TokenRequests is configured in the CSIDriver object and the driver is set to run at log level 2 or greater via the -v flag. | None  
  
### GKE on Bare Metal

Description | Severity  
---|---  
A new vulnerability (CVE-2023-2878) has been discovered in the secrets-store-csi-driver where an actor with access to the driver logs could observe service account tokens. These tokens could then potentially be exchanged with external cloud providers to access secrets stored in cloud vault solutions. GKE on Bare Metal is not affected by this CVE.

#### What should I do?

While GKE on Bare Metal is not affected, if you have installed the secrets-store-csi-driver component, you should update your installation with a patched version

#### What vulnerabilities are addressed by this patch?

The vulnerability, CVE-2023-2878, was discovered in secrets-store-csi-driver where an actor with access to the driver logs could observe service account tokens. These tokens could then potentially be exchanged with external cloud providers to access secrets stored in cloud vault solutions. Tokens are only logged when TokenRequests is configured in the CSIDriver object and the driver is set to run at log level 2 or greater via the -v flag. | None  
  
## GCP-2023-008

**Published:** 2023-06-05  
**Reference:**[CVE-2023-1872](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1872)

### GKE

Description | Severity  
---|---  
A new vulnerability (CVE-2023-1872) has been discovered in the Linux kernel that can lead to a privilege escalation to root on the node. GKE Standard and Autopilot clusters are affected. Clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) are not affected.

#### What should I do?

The following versions of GKE have been updated with code to fix this vulnerability. For security purposes, even if you have node auto-upgrade enabled, we recommend that you [manually upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your cluster and node pools to one of the following GKE versions: 

  * 1.22.17-gke.11400
  * 1.23.17-gke.5600
  * 1.24.13-gke.2500
  * 1.25.9-gke.2300
  * 1.26.5-gke.1200

A recent feature of [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions) allows you to apply a patch without having to unsubscribe from a channel. This lets you secure your nodes until the new version becomes the default for your release specific channel.

#### What vulnerabilities are addressed by this patch?

CVE-2023-1872 is a use-after-free vulnerability in the io_uring subsystem of the Linux kernel that can be exploited to achieve local privilege escalation. The `io_file_get_fixed` function lacks the presence of `ctx->uring_lock`, which can lead to a use-after-free vulnerability due to a race condition with fixed files becoming unregistered. | High  
  
### GKE on VMware

Description | Severity  
---|---  
A new vulnerability (CVE-2023-1872) has been discovered in the Linux kernel that can lead to a privilege escalation to root on the node.

#### What should I do?

**Note:** Patched versions of GKE on VMware will be released soon. This security bulletin will be updated when new GKE on VMware versions are available.

#### What vulnerabilities are addressed by this patch?

CVE-2023-1872 is a use-after-free vulnerability in the io_uring subsystem of the Linux kernel that can be exploited to achieve local privilege escalation. The `io_file_get_fixed` function lacks the presence of `ctx->uring_lock`, which can lead to a use-after-free vulnerability due to a race condition with fixed files becoming unregistered. | High  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSA new vulnerability (CVE-2023-1872) has been discovered in the Linux kernel that can lead to a privilege escalation to root on the node.

#### What should I do?

The following versions of GKE on AWS have been updated with code to fix these vulnerabilities:
* 1.15.1

#### What vulnerabilities are addressed by this patch?

CVE-2023-1872 is a use-after-free vulnerability in the io_uring subsystem of the Linux kernel that can be exploited to achieve local privilege escalation. The `io_file_get_fixed` function lacks the presence of `ctx->uring_lock`, which can lead to a use-after-free vulnerability due to a race condition with fixed files becoming unregistered. | High  
  
### GKE on Azure

Description | Severity  
---|---  
A new vulnerability (CVE-2023-1872) has been discovered in the Linux kernel that can lead to a privilege escalation to root on the node.

#### What should I do?

The following versions of GKE on Azure have been updated with code to fix these vulnerabilities:
* 1.15.1

#### What vulnerabilities are addressed by this patch?

CVE-2023-1872 is a use-after-free vulnerability in the io_uring subsystem of the Linux kernel that can be exploited to achieve local privilege escalation. The `io_file_get_fixed` function lacks the presence of `ctx->uring_lock`, which can lead to a use-after-free vulnerability due to a race condition with fixed files becoming unregistered. | High  
  
### GKE on Bare Metal

Description | Severity  
---|---  
A new vulnerability (CVE-2023-1872) has been discovered in the Linux kernel that can lead to a privilege escalation to root on the node. GKE on Bare Metal is not affected by this CVE.

#### What should I do?

No action required. | None  
  
## GCP-2023-005

**Published:** 2023-05-18  
**Updated:** 2023-06-06  
**Reference:**[CVE-2023-1281](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1281), [CVE-2023-1829](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1829)

**2023-06-06 Update:** New GKE versions have been updated to include the latest Ubuntu versions that patch CVE-2023-1281 and CVE-2023-1829.

### GKE

**Updated:** 2023-06-06

Description | Severity  
---|---  
Two new vulnerabilities (CVE-2023-1281, CVE-2023-1829) have been discovered in the Linux kernel that can lead to a privilege escalation to root on the node. GKE Standard clusters are affected. GKE Autopilot clusters and clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) are not affected.

#### What should I do?

**2023-06-06 Update:** Ubuntu patch versions are available. The following GKE versions have been updated to include the latest Ubuntu versions that patch CVE-2023-1281 and CVE-2023-1829:

  * 1.23.17-gke.6800 
  * 1.24.14-gke.1200 
  * 1.25.10-gke.1200 
  * 1.26.5-gke.1200 



* * *

The following versions of GKE have been updated with code to fix this vulnerability. For security purposes, even if you have node auto-upgrade enabled, we recommend that you [manually upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your cluster and node pools to one of the following GKE versions: 

  * 1.22.17-gke.8100
  * 1.23.17-gke.2300
  * 1.24.12-gke.1100
  * 1.25.8-gke.1000
  * 1.26.3-gke.1000

A recent feature of [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions) allows you to apply a patch without having to unsubscribe from a channel. This lets you secure your nodes until the new version becomes the default for your release specific channel.

#### What vulnerabilities are addressed by this patch?

Both CVE-2023-1281 and CVE-2023-1829 are use-after-free vulnerabilities in the Linux Kernel traffic control index filter (tcindex) that can be exploited to achieve local privilege escalation. With CVE-2023-1829, the tcindex_delete function does not properly deactivate filters in certain cases which can later lead to double freeing of a data structure. In CVE-2023-1281, the imperfect hash area can be updated while packets are traversing, which will cause a use-after-free when `tcf_exts_exec()` is called with the destroyed tcf_ext. A local attacker user can use this vulnerability to elevate its privileges to root. | High  
  
### GKE on VMware

Description | Severity  
---|---  
Two new vulnerabilities (CVE-2023-1281, CVE-2023-1829) have been discovered in the Linux kernel that can lead to a privilege escalation to root on the node.

#### What should I do?

**Note:** Patched versions of GKE on VMware will be released soon. This security bulletin will be updated when new GKE on VMware versions are available.

#### What vulnerabilities are addressed by this patch?

Both CVE-2023-1281 and CVE-2023-1829 are use-after-free vulnerabilities in the Linux Kernel traffic traffic control index filter (tcindex) that can be exploited to achieve local privilege escalation. With CVE-2023-1829, the tcindex_delete function does not properly deactivate filters in certain cases which can later lead to double freeing of a data structure. In CVE-2023-1281, the imperfect hash area can be updated while packets are traversing, which will cause a use-after-free when `tcf_exts_exec()` is called with the destroyed tcf_ext. A local attacker user can use this vulnerability to elevate its privileges to root. | High  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSTwo new vulnerabilities (CVE-2023-1281, CVE-2023-1829) have been discovered in the Linux kernel that can lead to a privilege escalation to root on the node.

#### What should I do?

**Note:** Patched versions of GKE on AWS will be released soon. This security bulletin will be updated when new GKE on AWS versions are available.

#### What vulnerabilities are addressed by this patch?

Both CVE-2023-1281 and CVE-2023-1829 are use-after-free vulnerabilities in the Linux Kernel traffic traffic control index filter (tcindex) that can be exploited to achieve local privilege escalation. With CVE-2023-1829, the tcindex_delete function does not properly deactivate filters in certain cases which can later lead to double freeing of a data structure. In CVE-2023-1281, the imperfect hash area can be updated while packets are traversing, which will cause a use-after-free when `tcf_exts_exec()` is called with the destroyed tcf_ext. A local attacker user can use this vulnerability to elevate its privileges to root. | High  
  
### GKE on Azure

Description | Severity  
---|---  
Two new vulnerabilities (CVE-2023-1281, CVE-2023-1829) have been discovered in the Linux kernel that can lead to a privilege escalation to root on the node.

#### What should I do?

**Note:** Patched versions of GKE on Azure will be released soon. This security bulletin will be updated when new GKE on Azure versions are available.

#### What vulnerabilities are addressed by this patch?

Both CVE-2023-1281 and CVE-2023-1829 are use-after-free vulnerabilities in the Linux Kernel traffic traffic control index filter (tcindex) that can be exploited to achieve local privilege escalation. With CVE-2023-1829, the tcindex_delete function does not properly deactivate filters in certain cases which can later lead to double freeing of a data structure. In CVE-2023-1281, the imperfect hash area can be updated while packets are traversing, which will cause a use-after-free when `tcf_exts_exec()` is called with the destroyed tcf_ext. A local attacker user can use this vulnerability to elevate its privileges to root. | High  
  
### GKE on Bare Metal

Description | Severity  
---|---  
Two new vulnerabilities (CVE-2023-1281, CVE-2023-1829) have been discovered in the Linux kernel that can lead to a privilege escalation to root on the node. GKE on Bare Metal are not affected by this CVE.

#### What should I do?

No action required. | None  
  
## GCP-2023-003

**Published:** 2023-04-11  
**Updated:** 2023-12-21  
**Reference:**[CVE-2023-0240](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0240), [CVE-2023-23586](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23586)

**2023-12-21 Update:** Clarify that GKE Autopilot clusters in the default configuration are not impacted.

### GKE

**Updated:** 2023-12-21

Description | Severity  
---|---  
**2023-12-21 Update** : The original bulletin stated Autopilot clusters are impacted, but this was incorrect. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp Unconfined profile or [allow `CAP_NET_ADMIN`.](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies) Two new vulnerabilities, CVE-2023-0240 and CVE-2023-23586, have been discovered in the Linux kernel that could allow an unprivileged user to escalate privileges. GKE clusters, including Autopilot clusters, with COS using Linux Kernel version 5.10 until 5.10.162 are affected. GKE clusters using Ubuntu images or using GKE Sandbox are unaffected.

#### What should I do?

The following versions of GKE have been updated with code to fix these vulnerabilities. For security purposes, even if you have node-autoupgrade enabled, we recommend that you manually upgrade your node pools to one of the following GKE versions:

  * 1.22.17-gke.4000
  * 1.23.16-gke.1100
  * 1.24.10-gke.1200

A recent feature of [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions) allows you to apply a patch without having to unsubscribe from a channel. This lets you secure your nodes until the new version becomes the default for your release specific channel.

#### What vulnerabilities are addressed by this patch?

Vulnerability 1 (CVE-2023-0240): A race condition in `io_uring` can lead to a full container break out to root on the node. Linux kernel versions 5.10 are affected until 5.10.162. Vulnerability 2 (CVE-2023-23586): A use after free (UAF) in `io_uring/time_ns` can lead to a full container break out to root on the node. Linux kernel versions 5.10 are affected until 5.10.162. | High  
  
### GKE on VMware

Description | Severity  
---|---  
Two new vulnerabilities, CVE-2023-0240 and CVE-2023-23586, have been discovered in the Linux kernel that could allow an unprivileged user to escalate privileges. GKE on VMware clusters with COS using Linux Kernel version 5.10 until 5.10.162 are affected. GKE Enterprise clusters using Ubuntu images are unaffected.

#### What should I do?

The following versions of GKE on VMware have been updated with code to fix these vulnerabilities:

  * 1.12.6
  * 1.13.5



#### What vulnerabilities are addressed by this patch?

Vulnerability 1 (CVE-2023-0240): A race condition in `io_uring` can lead to a full container break out to root on the node. Linux kernel versions 5.10 are affected until 5.10.162. Vulnerability 2 (CVE-2023-23586): A use after free (UAF) in `io_uring/time_ns` can lead to a full container break out to root on the node. Linux kernel versions 5.10 are affected until 5.10.162. | High  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSTwo new vulnerabilities, CVE-2023-0240 and CVE-2023-23586, have been discovered in the Linux kernel that could allow an unprivileged user to escalate privileges. GKE on AWS is not affected by these CVEs.

#### What should I do?

No action required. | None  
  
### GKE on Azure

Description | Severity  
---|---  
Two new vulnerabilities, CVE-2023-0240 and CVE-2023-23586, have been discovered in the Linux kernel that could allow an unprivileged user to escalate privileges. GKE on Azure is not affected by these CVEs

#### What should I do?

No action required. | None  
  
### GKE on Bare Metal

Description | Severity  
---|---  
Two new vulnerabilities, CVE-2023-0240 and CVE-2023-23586, have been discovered in the Linux kernel that could allow an unprivileged user to escalate privileges. GKE on Bare Metal is not affected by these CVEs.

#### What should I do?

No action required. | None  
  
## GCP-2023-001

**Published:** 2023-03-01  
**Updated:** 2023-12-21  
**Reference:**[CVE-2022-4696](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4696)

**2023-12-21 Update:** Clarify that GKE Autopilot clusters in the default configuration are not impacted.

### GKE

Description | Severity  
---|---  
**2023-12-21 Update** : The original bulletin stated Autopilot clusters are impacted, but this was incorrect. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp Unconfined profile or [allow `CAP_NET_ADMIN`.](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies) A new vulnerability (CVE-2022-4696) has been discovered in the Linux kernel that can lead to a privilege escalation on the node. GKE clusters, including Autopilot clusters, are impacted. GKE clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) are not affected.

#### What should I do?

The following versions of GKE have been updated with code to fix this vulnerability. For security purposes, even if you have node auto-upgrade enabled, we recommend that you [manually upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) your clusters and node pools to one of the following GKE versions:

  * 1.22.17-gke.3100
  * 1.23.16-gke.200
  * 1.24.9-gke.3200

A recent feature of [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions) allows you to apply a patch without having to unsubscribe from a channel. This lets you secure your nodes until the new version becomes the default for your release specific channel.

#### What vulnerabilities are addressed by this patch?

With CVE-2022-4696, a use-after-free flaw was found in io_uring and ioring_op_splice in the Linux kernel. This flaw allows a local user to create a local privilege escalation. | High  
  
### GKE on VMware

Description | Severity  
---|---  
A new vulnerability (CVE-2022-4696) has been discovered in the Linux kernel that can lead to a privilege escalation on the node. GKE on VMware running v1.12 and v1.13 are impacted. GKE on VMware running v1.14 or later are not affected.

#### What should I do?

The following versions of GKE on VMware have been updated with code to fix this vulnerability. We recommend that you upgrade your admin and user clusters to one of the following GKE on VMware versions:

  * 1.12.5
  * 1.13.5



#### What vulnerabilities are addressed by this patch?

With CVE-2022-4696, a use-after-free flaw was found in io_uring and ioring_op_splice in the Linux kernel. This flaw allows a local user to create a local privilege escalation. | High  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSA new vulnerability (CVE-2022-4696) has been discovered in the Linux kernel that can lead to a privilege escalation on the node. GKE on AWS is unaffected by this vulnerability.

#### What should I do?

No action is required. | None  
  
### GKE on Azure

Description | Severity  
---|---  
A new vulnerability (CVE-2022-4696) has been discovered in the Linux kernel that can lead to a privilege escalation on the node. GKE on Azure is unaffected by this vulnerability.

#### What should I do?

No action is required. | None  
  
### GKE on Bare Metal

Description | Severity  
---|---  
A new vulnerability (CVE-2022-4696) has been discovered in the Linux kernel that can lead to a privilege escalation on the node. GKE on Bare Metal is unaffected by this vulnerability.

#### What should I do?

No action is required. | None  
  
## GCP-2022-026

**Published:** 2023-01-11  
**Reference:**[CVE-2022-3786](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3786), [CVE-2022-3602](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3602)

### GKE

Description | Severity  
---|---  
Two new vulnerabilities (CVE-2022-3786 and CVE-2022-3602) have been discovered in OpenSSL v3.0.6 that can potentially cause a crash. While this has been rated a High in the NVD database, GKE endpoints use boringSSL or an older version of OpenSSL that is not affected, so the rating has been reduced to a Medium for GKE.

#### What should I do?

The following versions of GKE have been updated with code to fix this vulnerability: 

  * 1.25.4-gke.1600
  * 1.24.8-gke.401
  * 1.23.14-gke.401
  * 1.22.16-gke.1300
  * 1.21.14-gke.14100

A recent feature of [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions) allows you to apply a patch without having to unsubscribe from a channel. This lets you secure your nodes until the new version becomes the default for your release specific channel.

#### What vulnerabilities are addressed by this patch?

With CVE-2022-3786 and CVE-2022-3602, a buffer overrun can be triggered in X.509 certificate verification that can cause a crash that will result in a denial of service. To be exploited, this vulnerability requires either a CA to have signed a malicious certificate or for an application to continue certificate verification despite failure to construct a path to a trusted issuer. | Medium  
  
### GKE on VMware

Description | Severity  
---|---  
Two new vulnerabilities (CVE-2022-3786 and CVE-2022-3602) have been discovered in OpenSSL v3.0.6 that can potentially cause a crash.

#### What should I do?

GKE on VMware is not affected by this CVE as it does not use an impacted version of OpenSSL.

#### What vulnerabilities are addressed by this patch?

No action required. | None  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSTwo new vulnerabilities (CVE-2022-3786 and CVE-2022-3602) have been discovered in OpenSSL v3.0.6 that can potentially cause a crash.

#### What should I do?

GKE on AWS is not affected by this CVE as it does not use an impacted version of OpenSSL.

#### What vulnerabilities are addressed by this patch?

No action required. | None  
  
### GKE on Azure

Description | Severity  
---|---  
Two new vulnerabilities (CVE-2022-3786 and CVE-2022-3602) have been discovered in OpenSSL v3.0.6 that can potentially cause a crash.

#### What should I do?

GKE on Azure is not affected by this CVE as it does not use an impacted version of OpenSSL.

#### What vulnerabilities are addressed by this patch?

No action required. | None  
  
### GKE on Bare Metal

Description | Severity  
---|---  
Two new vulnerabilities (CVE-2022-3786 and CVE-2022-3602) have been discovered in OpenSSL v3.0.6 that can potentially cause a crash.

#### What should I do?

GKE on Bare Metal is not affected by this CVE as it does not use an impacted version of OpenSSL.

#### What vulnerabilities are addressed by this patch?

No action required. | None  
  
## GCP-2022-025

**Published:** 2022-12-21  
**Updated:** 2023-01-19, 2023-12-21  
**Reference:**[CVE-2022-2602](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2602)

**2023-12-21 Update:** Clarify that GKE Autopilot clusters in the default configuration are not impacted.

**2023-01-19 Update:** GKE version 1.21.14-gke.14100 is available.

### GKE

**Updated:** 2023-01-19

Description | Severity  
---|---  
**2023-12-21 Update** : The original bulletin stated Autopilot clusters are impacted, but this was incorrect. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp Unconfined profile or [allow `CAP_NET_ADMIN`.](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies) A new vulnerability (CVE-2022-2602) has been discovered in the io_uring subsystem in the Linux kernel that can allow an attacker to potentially execute arbitrary code. GKE clusters, including Autopilot clusters, are impacted. GKE clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) are not affected.

#### What should I do?

**2023-01-19 Update:** Version 1.21.14-gke.14100 is available. Upgrade your node pools to this version or later. 

* * *

The following versions of GKE have been updated with code to fix this vulnerability in an upcoming release. For security purposes, even if you have node auto-upgrade enabled, we recommend that you [manually upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your node pools to one of the following GKE versions:

  * Container-Optimized OS:
    * 1.22.16-gke.1300 and later
    * 1.23.14-gke.401 and later
    * 1.24.7-gke.900 and later
    * 1.25.4-gke.1600 and later
  * Ubuntu:
    * 1.22.15-gke.2500 and later
    * 1.23.13-gke.900 and later
    * 1.24.7-gke.900 and later
    * 1.25.3-gke.800 and later

**Note:** 1.21 patches are pending rollout. We will update this bulletin when the new version is available.A recent feature of [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-%0A%20%20%20%20%20%20%20%20%20%20patch-versions) allows you to apply a patch without having to unsubscribe from a channel. This lets you secure your nodes until the new version becomes the default for your release specific channel.

#### What vulnerabilities are addressed by this patch?

With CVE-2022-2602, a race condition between io_uring request processing and Unix socket garbage collection can cause a use-after-free vulnerability. A local attacker could use this to trigger a denial of service or possibly execute arbitrary code.  | High  
  
### GKE on VMware

Description | Severity  
---|---  
A new vulnerability (CVE-2022-2602) has been discovered in the io_uring subsystem in the Linux kernel that can allow an attacker to potentially execute arbitrary code. Versions 1.11, 1.12 and 1.13 of GKE on VMware are affected.

#### What should I do?

Upgrade your cluster to a patched version. The following versions of GKE on VMware contain code that fixes this vulnerability:

  * 1.13.2
  * 1.12.4
  * 1.11.5

**Note:** Some of these versions might not be available immediately, and will become available in upcoming releases.

#### What vulnerabilities are addressed by this patch?

With CVE-2022-2602, a race condition between io_uring request processing and Unix socket garbage collection can cause a use-after-free vulnerability. A local attacker could use this to trigger a denial of service or possibly execute arbitrary code.  | High  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSA new vulnerability (CVE-2022-2602) has been discovered in the io_uring subsystem in the Linux kernel that can allow an attacker to potentially execute arbitrary code.

#### What should I do?

The following current and previous generation versions of GKE on AWS have been updated with code to fix this vulnerability. We recommend that you upgrade your nodes to one of the following GKE on AWS versions:

  * Current generation:
    * 1.22.15-gke.100
    * 1.23.11-gke.300
    * 1.24.5-gke.200
  * Previous generation:
    * 1.22.15-gke.1400
    * 1.23.12-gke.1400
    * 1.24.6-gke.1300



#### What vulnerabilities are addressed by this patch?

With CVE-2022-2602, a race condition between io_uring request processing and Unix socket garbage collection can cause a use-after-free vulnerability. A local attacker could use this to trigger a denial of service or possibly execute arbitrary code.  | High  
  
### GKE on Azure

Description | Severity  
---|---  
A new vulnerability (CVE-2022-2602) has been discovered in the io_uring subsystem in the Linux kernel that can allow an attacker to potentially execute arbitrary code.

#### What should I do?

The following versions of GKE on Azure have been updated with code to fix this vulnerability. We recommend that you upgrade your nodes to one of the following GKE on Azure versions:

  * 1.22.15-gke.100
  * 1.23.11-gke.300
  * 1.24.5-gke.200



#### What vulnerabilities are addressed by this patch?

With CVE-2022-2602, a race condition between io_uring request processing and Unix socket garbage collection can cause a use-after-free vulnerability. A local attacker could use this to trigger a denial of service or possibly execute arbitrary code.  | High  
  
### GKE on Bare Metal

Description | Severity  
---|---  
A new vulnerability (CVE-2022-2602) has been discovered in the io_uring subsystem in the Linux kernel that can allow an attacker to potentially execute arbitrary code. GKE on Bare Metal is not affected by this CVE as it does not bundle an operating system in its distribution.

#### What should I do?

No action required. | None  
  
## GCP-2022-024

**Published:** 2022-11-09  
**Updated:** 2023-01-19  
**Reference:**[CVE-2022-2585](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2585), [CVE-2022-2588](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2588)

**2023-01-19 Update:** GKE version 1.21.14-gke.14100 is available. **2022-12-16 Update:** Added revised patch versions for GKE and GKE on VMware.

### GKE

**Updated:** 2023-01-19

Description | Severity  
---|---  
Two new vulnerabilities (CVE-2022-2585 and CVE-2022-2588) have been discovered in the Linux kernel that can lead to a full container break out to root on the node. GKE clusters, including Autopilot clusters, are impacted. GKE clusters using [GKE Sandbox](https://cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) are not affected.

#### What should I do?

**2023-01-19 Update:** Version 1.21.14-gke.14100 is available. Upgrade your node pools to this version or later.  **2022-12-16 Update:** A previous version of the bulletin has been revised due to a release regression. Please [manually upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your node pools to one of the following GKE versions: 

  * 1.22.16-gke.1300 and later
  * 1.23.14-gke.401 and later
  * 1.24.7-gke.900 and later
  * 1.25.4-gke.1600 and later

**Note:** Version 1.21.14-gke.9500 is pending rollout and may be superseded by a higher version number. We'll update this bulletin if a higher version number becomes available.

* * *

The following versions of GKE have been updated with code to fix this vulnerability. For security purposes, even if you have node-autoupgrade enabled, we recommend that you [manually upgrade](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) your node pools to one of the following GKE versions:

  * 1.21.14-gke.9500
  * 1.24.7-gke.900

Updates for GKE v1.22, 1.23 and 1.25 will be made available soon. This security bulletin will be updated when they become available. A recent feature of [release channels](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions) allows you to apply a patch without having to unsubscribe from a channel. This lets you secure your nodes until the new version becomes the default for your release specific channel.

#### What vulnerabilities are addressed by this patch?

  * With CVE-2022-2585, improper cleanup of timers in the posix cpu timer allows a use-after-free exploit depending on how timers are created and deleted.
  * With CVE-2022-2588, a use-after-free flaw was found in route4_change in the Linux kernel. This flaw allows a local user to crash the system and possibly lead to a local privilege escalation.

| High  
  
### GKE on VMware

**Updated:** 2022-12-16

Description | Severity  
---|---  
Two new vulnerabilities (CVE-2022-2585 and CVE-2022-2588) have been discovered in the Linux kernel that can lead to a full container break out to root on the node. Versions 1.13, 1.12 and 1.11 of GKE on VMware are affected.

#### What should I do?

**2022-12-16 Update:** The following versions of GKE on VMware have been updated with code to fix this vulnerability. We recommend that you upgrade your admin and user clusters to one of the following GKE on VMware versions: 

  * 1.13.2
  * 1.12.4
  * 1.11.6

**Note:** Some of these versions might not be available immediately, and will become available in upcoming releases.

* * *

  * Note: Versions of GKE on VMware that contain Container-Optimized OS patches will be released soon. This security bulletin will be updated when the GKE on VMware versions are available for download.



#### What vulnerabilities are addressed by this patch?

  * With CVE-2022-2585, improper cleanup of timers in the posix cpu timer allows a use-after-free exploit depending on how timers are created and deleted.
  * With CVE-2022-2588, a use-after-free flaw was found in route4_change in the Linux kernel. This flaw allows a local user to crash the system and possibly lead to a local privilege escalation.

| High  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSTwo new vulnerabilities (CVE-2022-2585 and CVE-2022-2588) have been discovered in the Linux kernel that can lead to a full container break out to root on the node. The following versions of Kubernetes on AWS may be affected:

  * 1.23: Versions older than 1.23.9-gke.800. Newer minor versions are not affected
  * 1.22: Versions older than 1.22.12-gke.1100. Newer minor versions are not affected

Kubernetes V1.24 is not affected.

#### What should I do?

We recommend that you upgrade your clusters to one of the following AWS Kubernetes versions:

  * 1.23: a version later than v1.23.9-gke.800
  * 1.22: a version later than 1.22.12-gke-1100



#### What vulnerabilities are being addressed?

With CVE-2022-2585, improper cleanup of timers in the posix cpu timer allows a use-after-free exploit depending on how timers are created and deleted. With CVE-2022-2588, a use-after-free flaw was found in route4_change in the Linux kernel. This flaw allows a local user to crash the system and possibly lead to a local privilege escalation. | High  
  
### GKE on Azure

Description | Severity  
---|---  
Two new vulnerabilities (CVE-2022-2585 and CVE-2022-2588) have been discovered in the Linux kernel that can lead to a full container break out to root on the node. The following versions of Kubernetes on Azure may be affected:

  * 1.23: Versions older than 1.23.9-gke.800. Newer minor versions are not affected.
  * 1.22: Versions older than 1.22.12-gke.1100. Newer minor versions are not affected.

Kubernetes V1.24 is not affected.

#### What should I do?

We recommend that you upgrade your clusters to one of the following Azure Kubernetes versions:

  * 1.23: a version later than v1.23.9-gke.800
  * 1.22: a version later than 1.22.12-gke-1100



#### What vulnerabilities are being addressed?

With CVE-2022-2585, improper cleanup of timers in the posix cpu timer allows a use-after-free exploit depending on how timers are created and deleted. With CVE-2022-2588, a use-after-free flaw was found in route4_change in the Linux kernel. This flaw allows a local user to crash the system and possibly lead to a local privilege escalation. | High  
  
### GKE on Bare Metal

Description | Severity  
---|---  
Two new vulnerabilities (CVE-2022-2585 and CVE-2022-2588) have been discovered in the Linux kernel that can lead to a full container break out to root on the node. GKE on Bare Metal is not affected by this CVE as it does not bundle an operating system in its distribution.

#### What should I do?

No action required. | None  
  
## GCP-2022-023

**Published:** 2022-11-04  
**Reference:**[CVE-2022-39278](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-39278)

### GKE

Description | Severity  
---|---  
A security vulnerability, CVE-2022-39278, has been discovered in Istio, which is used in Cloud Service Mesh, that allows a malicious attacker to crash the control plane.

#### What should I do?

Google Kubernetes Engine (GKE) doesn't ship with Istio and isn't affected by this vulnerability. However, if you have separately installed Cloud Service Mesh or Istio on your GKE cluster, refer to [GCP-2022-020](https://cloud.google.com/service-mesh/docs/security-bulletins#gcp-2022-020), the Cloud Service Mesh security bulletin on this CVE, for more information. | None  
  
### GKE on VMware

Description | Severity  
---|---  
A security vulnerability, CVE-2022-39278, has been discovered in Istio, which is used in Cloud Service Mesh in GKE on VMware, that allows a malicious attacker to crash the Istio control plane.

#### What should I do?

The following versions of GKE on VMware have been updated with code to fix this vulnerability. We recommend that you upgrade your admin and user clusters to one of the following GKE on VMware versions:

  * 1.11.4
  * 1.12.3
  * 1.13.1



#### What vulnerabilities are addressed by this patch?

With vulnerability CVE-2022-39278, the Istio control plane, `istiod`, is vulnerable to a request processing error, allowing a malicious attacker to send a specially crafted message which results in the control plane crashing when the validating webhook for a cluster is exposed publicly. This endpoint is served over TLS port 15017, but doesn't require any authentication from the attacker.  | High  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSA security vulnerability, CVE-2022-39278, has been discovered in Istio, which is used in Cloud Service Mesh, that allows a malicious attacker to crash the control plane. 

#### What should I do?

GKE on AWS isn't affected by this vulnerability and no action is required. | None  
  
### GKE on Azure

Description | Severity  
---|---  
A security vulnerability, CVE-2022-39278, has been discovered in Istio, which is used in Cloud Service Mesh, that allows a malicious attacker to crash the control plane.

#### What should I do?

GKE on Azure isn't affected by this vulnerability and no action is required. | None  
  
### GKE on Bare Metal

Description | Severity  
---|---  
A security vulnerability, CVE-2022-39278, has been discovered in Istio, which is used in Cloud Service Mesh in GKE on Bare Metal, that allows a malicious attacker to crash the Istio control plane.

#### What should I do?

The following versions of GKE on Bare Metal have been updated with code to fix this vulnerability. We recommend that you upgrade clusters to one of the following GKE on Bare Metal versions:

  * 1.11.7
  * 1.12.4
  * 1.13.1



#### What vulnerabilities are addressed by this patch?

With vulnerability CVE-2022-39278, the Istio control plane, `istiod`, is vulnerable to a request processing error, allowing a malicious attacker to send a specially crafted message which results in the control plane crashing when the validating webhook for a cluster is exposed publicly. This endpoint is served over TLS port 15017, but doesn't require any authentication from the attacker.  | High  
  
## GCP-2022-022-updated

**Published:** 2022-12-08  
**Reference:**[CVE-2022-20409](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-20409)

### GKE

**Updated:** 2022-12-14

Description | Severity  
---|---  
A new vulnerability, CVE-2022-20409, has been discovered in the Linux kernel that can lead to local privilege escalation. Google Kubernetes Engine (GKE) v1.22, v1.23, and v1.24 clusters, including Autopilot clusters, using Container-Optimized OS version 93 and 97 are impacted. Other supported [GKE versions](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule#schedule_for_release_channels) aren't affected. GKE clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) are unaffected.

#### What should I do?

**2022-12-14 Update:** A previous version of the bulletin has been revised due to a release regression. Please [manually upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your node pools to one of the following GKE versions: 

  * 1.22.15-gke.2500 and later
  * 1.23.13-gke.900 and later
  * 1.24.7-gke.900 and later



* * *

The following versions of GKE using Container-Optimized OS version 93 and 97 have been updated with code to fix this vulnerability in an upcoming release. For security purposes, even if you have node auto-upgrades enabled, we recommend that you [manually upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your node pools to one of the following GKE versions:

  * 1.22.15-gke.2300 and later
  * 1.23.13-gke.700 and later
  * 1.24.7-gke.700 and later

A recent feature of [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions) lets you apply a patch without having to unsubscribe from a channel. This feature lets you secure your nodes until the new version becomes the default for your release-specific channel. 

#### What vulnerabilities are addressed by this patch?

With CVE-2022-20409, the Linux Kernel has a vulnerability in io_identity_cow of the io_uring subsystem. There's a potential for memory corruption due to a Use-After-Free (UAF) vulnerability. A local attacker could use this memory corruption for denial of service (system crash) or possibly to execute arbitrary code. | High  
  
### GKE on VMware

**Updated:** 2022-12-14

Description | Severity  
---|---  
A new vulnerability, CVE-2022-20409, has been discovered in the Linux kernel that can lead to local privilege escalation.

#### What should I do?

**2022-12-14 Update:** The following versions of GKE on VMware for Ubuntu have been updated with code to fix this vulnerability. We recommend that you upgrade your nodes to one of the following GKE on VMware versions: 

  * 1.13.1 and later
  * 1.12.3 and later
  * 1.11.4 and later



* * *

#### What vulnerabilities are addressed by this patch?

With CVE-2022-20409, the Linux Kernel has a vulnerability in io_identity_cow of the io_uring subsystem. There's a potential for memory corruption due to a Use-After-Free (UAF) vulnerability. A local attacker could use this memory corruption for denial of service (system crash) or possibly to execute arbitrary code.  | High  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSA new vulnerability, CVE-2022-20409, has been discovered in the Linux kernel that could allow an unprivileged user to escalate to system execution privilege.

#### What should I do?

There's no action required. GKE on AWS doesn't use the affected versions of the Linux kernel. 

#### What vulnerabilities are addressed by this patch?

With CVE-2022-20409, the Linux Kernel has a vulnerability in io_identity_cow of the io_uring subsystem. There's a potential for memory corruption due to a Use-After-Free (UAF) vulnerability. A local attacker could use this memory corruption for denial of service (system crash) or possibly to execute arbitrary code.  | None  
  
### GKE on Azure

Description | Severity  
---|---  
A new vulnerability, CVE-2022-20409, has been discovered in the Linux kernel that could allow an unprivileged user to escalate to system execution privilege.

#### What should I do?

There's no action required. GKE on Azure doesn't use the affected versions of the Linux kernel. 

#### What vulnerabilities are addressed by this patch?

With CVE-2022-20409, the Linux Kernel has a vulnerability in io_identity_cow of the io_uring subsystem. There's a potential for memory corruption due to a Use-After-Free (UAF) vulnerability. A local attacker could use this memory corruption for denial of service (system crash) or possibly to execute arbitrary code.  | None  
  
### GKE on Bare Metal

Description | Severity  
---|---  
A new vulnerability, CVE-2022-20409, has been discovered in the Linux kernel that can lead to local privilege escalation.

#### What should I do?

  * There's no action required. GKE on Bare Metal isn't affected by this CVE as it doesn't bundle an operating system in its distribution.

| None  
  
## GCP-2022-021

**Published:** 2022-10-27  
**Updated:** 2023-01-19, 2023-12-21  
**Reference:**[CVE-2022-3176](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3176)

**2023-12-21 Update:** Clarify that GKE Autopilot clusters in the default configuration are not impacted.

**2023-01-19 Update:** GKE version 1.21.14-gke.14100 is available. **2022-12-15 Update:** Updated information that version 1.21.14-gke.9400 of Google Kubernetes Engine is pending rollout and may be superseded by a higher version number. **2022-11-21 Update:** Added patch versions for GKE on VMware, GKE on AWS, and GKE on Azure.

### GKE

**Updated:** 2023-01-19, 2023-12-21

Description | Severity  
---|---  
A new vulnerability, CVE-2022-3176, has been discovered in the Linux kernel that can lead to local privilege escalation. This vulnerability allows an unprivileged user to achieve full container breakout to root on the node.  **2023-12-21 Update** : The original bulletin stated Autopilot clusters are impacted, but this was incorrect. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp Unconfined profile or [allow `CAP_NET_ADMIN`.](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies) Google Kubernetes Engine (GKE) v1.21 clusters, including Autopilot clusters, using Container-Optimized OS version 89 are impacted. Later versions of GKE aren't affected. All Linux clusters with Ubuntu are affected. GKE clusters using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) are unaffected. 

#### What should I do?

**2023-01-19 Update:** Version 1.21.14-gke.14100 is available. Upgrade your node pools to this version or later.  **2022-12-15 Update:** Version 1.21.14-gke.9400 is pending rollout and may be superseded by a higher version number. We will update this doc when said new version is available. 

* * *

The following versions of GKE have been updated with code to fix this vulnerability in an upcoming release. For security purposes, even if you have node auto-upgrades enabled, we recommend that you [manually upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your node pools to one of the following GKE versions:

  * Container-Optimized OS:
    * 1.21.14-gke.7100 and later
  * Ubuntu:
    * 1.21.14-gke.9400 and later
    * 1.22.15-gke.2400 and later
    * 1.23.13-gke.800 and later
    * 1.24.7-gke.800 and later
    * 1.25.3-gke.700 and later

A recent feature of [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions) lets you apply a patch without having to unsubscribe from a channel. This feature lets you secure your nodes until the new version becomes the default for your release-specific channel. 

#### What vulnerabilities are addressed by this patch?

With CVE-2022-3176, the Linux Kernel has a vulnerability in the io_uring subsystem. Missing POLLFREE handling can lead to Use-After-Free (UAF) exploits that can be used for privilege escalation.  | High  
  
### GKE on VMware

**Updated:** 2022-11-21

Description | Severity  
---|---  
A new vulnerability, CVE-2022-3176, has been discovered in the Linux kernel that can lead to local privilege escalation. This vulnerability allows an unprivileged user to achieve full container breakout to root on the node.

#### What should I do?

  * Versions of GKE on VMware with Container-Optimized OS are unaffected. 

**2022-11-21 Update:** The following versions of GKE on VMware for Ubuntu have been updated with code to fix this vulnerability. We recommend that you upgrade your nodes to one of the following GKE on VMware versions: 

  * 1.12.3 and later
  * 1.13.1 and later
  * 1.11.5 and later



* * *

Versions of GKE on VMware that contain Ubuntu patches will be released soon. This security bulletin will be updated when the GKE on VMware versions are available for download.

#### What vulnerabilities are addressed by this patch?

With CVE-2022-3176, the Linux Kernel has a vulnerability in the io_uring subsystem. Missing POLLFREE handling can lead to Use-After-Free (UAF) exploits that can be used for privilege escalation.  | High  
  
### GKE on AWS

**Updated:** 2022-11-21

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSA new vulnerability, CVE-2022-3176, has been discovered in the Linux kernel that can lead to local privilege escalation. This vulnerability allows an unprivileged user to achieve full container breakout to root on the node.

#### What should I do?

**2022-11-21 Update:** The following current and previous generation versions of GKE on AWS have been updated with code to fix this vulnerability. We recommend that you upgrade your nodes to one of the following GKE on AWS versions:  **Current generation**

  * 1.21.14-gke.7100
  * 1.22.15-gke.100
  * 1.23.11-gke.300
  * 1.24.5-gke.200

**Previous generation**

  * 1.22.15-gke.1400
  * 1.23.12-gke.1400
  * 1.24.6-gke.1300



* * *

Versions of GKE on AWS that contain Ubuntu patches will be released soon. This security bulletin will be updated when the GKE on AWS versions are available for download.

#### What vulnerabilities are addressed by this patch?

With CVE-2022-3176, the Linux Kernel has a vulnerability in the io_uring subsystem. Missing POLLFREE handling can lead to Use-After-Free (UAF) exploits that can be used for privilege escalation.  | High  
  
### GKE on Azure

**Updated:** 2022-11-21

Description | Severity  
---|---  
A new vulnerability, CVE-2022-3176, has been discovered in the Linux kernel that can lead to local privilege escalation. This vulnerability allows an unprivileged user to achieve full container breakout to root on the node.

#### What should I do?

**2022-11-21 Update:** The following versions of GKE on Azure have been updated with code to fix this vulnerability. We recommend that you upgrade your nodes to one of the following GKE on Azure versions: 

  * 1.21.14-gke.7100
  * 1.22.15-gke.100
  * 1.23.11-gke.300
  * 1.24.5-gke.200



* * *

Versions of GKE on Azure that contain Ubuntu patches will be released soon. This security bulletin will be updated when the GKE on Azure versions are available for download.

#### What vulnerabilities are addressed by this patch?

With CVE-2022-3176, the Linux Kernel has a vulnerability in the io_uring subsystem. Missing POLLFREE handling can lead to Use-After-Free (UAF) exploits that can be used for privilege escalation.  | High  
  
### GKE on Bare Metal

Description | Severity  
---|---  
A new vulnerability, CVE-2022-3176, has been discovered in the Linux kernel that can lead to local privilege escalation. This vulnerability allows an unprivileged user to achieve full container breakout to root on the node.

#### What should I do?

No action required. GKE on Bare Metal isn't affected by this CVE as it doesn't bundle an operating system in its distribution.  | None  
  
## GCP-2022-018

**Published:** 2022-08-01  
**Updated:** 2022-09-14, 2023-12-21  
**Reference:**[CVE-2022-2327](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE2022-2327)

**2023-12-21 Update:** Clarify that GKE Autopilot clusters in the default configuration are not impacted.

**2022-09-14 Update:** Added patch versions for GKE on VMware, GKE on AWS, and GKE on Azure.

### GKE

**Updated:** 2023-12-21

Description | Severity  
---|---  
A new vulnerability (CVE-2022-2327) has been discovered in the Linux kernel that can lead to local privilege escalation. This vulnerability allows an unprivileged user to achieve a full container breakout to root on the node.

#### Technical details

**2023-12-21 Update** : The original bulletin stated Autopilot clusters are impacted, but this was incorrect. GKE Autopilot clusters in the default configuration are not impacted, but might be vulnerable if you explicitly set the seccomp Unconfined profile or [allow `CAP_NET_ADMIN`.](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies) GKE clusters, including Autopilot clusters, with Container-Optimized OS (COS) using Linux Kernel version 5.10 are affected. GKE clusters using Ubuntu images or using [GKE Sandbox](https://cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) are unaffected.

#### What should I do?

Upgrade your GKE clusters to a version that includes the fix. The Linux node images for COS have been updated along with GKE versions using those COS versions.  
  
For security purposes, even if you have the _node autoupgrade_ enabled, we recommend that you [manually upgrade](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your node pools to one of the following GKE versions:  
  
COS versions  


  * 1.22.12-gke.300


  * 1.23.8-gke.1900


  * 1.24.2-gke.1900

  
  
A recent feature of [release channels](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions) allows you to apply a patch without having to unsubscribe from a channel. This lets you upgrade your nodes to the patched version before that version becomes the default in your selected release channel.  


#### What vulnerabilities are addressed by this patch?

  * [CVE-2022-2327](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2327)

With CVE-2022-2327, the Linux kernel in version 5.10 has a vulnerability in the io_uring subsystem where various requests are missing item types (flags). Using these requests without the proper item types specified can cause privilege escalation to root.  | High  
  
### GKE on VMware

**Updated:** 2022-09-14

Description | Severity  
---|---  
A new vulnerability (CVE-2022-2327) has been discovered in the Linux kernel that can lead to local privilege escalation. This vulnerability allows an unprivileged user to achieve a full container breakout to root on the node.  Clusters with a Container Optimized OS (COS) image using GKE on VMware versions 1.10, 1.11, and 1.12 are affected. 

#### What should I do?

**2022-09-14 Update:** The following versions of GKE on VMware contain code that fixes this vulnerability. 

  * 1.10.6 or later
  * 1.11.3 or later
  * 1.12.1 or later



* * *

Versions of GKE on VMware that contain patches will be released soon. This security bulletin will be updated when the GKE on VMware versions are available for download. 

#### What vulnerabilities are addressed by this patch?

  * [CVE-2022-2327](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2327)

With CVE-2022-2327, the Linux kernel in version 5.10 has a vulnerability in the io_uring subsystem where various requests are missing item types (flags). Using these requests without the proper item types specified can cause privilege escalation to root.  | High  
  
### GKE on AWS

**Updated:** 2022-09-14

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSA new vulnerability (CVE-2022-2327) has been discovered in the Linux kernel that can lead to local privilege escalation. This vulnerability allows an unprivileged user to achieve a full container breakout to root on the node.

#### What should I do?

**2022-09-14 Update:** The following current and previous generation versions of GKE on AWS have been updated with code to fix this vulnerability. We recommend that you upgrade your nodes to one of the following GKE on AWS versions:  Current generation

  * 1.23.8-gke.1700
  * 1.22.12-gke.200
  * 1.21.14-gke.2100

Previous generation

  * 1.23.8-gke.2000
  * 1.22.12-gke.300
  * 1.21.14-gke.2100



* * *

Versions of GKE on AWS that contain patches will be released soon. This security bulletin will be updated when the GKE on AWS versions are available for download. 

#### What vulnerabilities are addressed by this patch?

  * [CVE-2022-2327](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2327)

With CVE-2022-2327, the Linux kernel in version 5.10 has a vulnerability in the io_uring subsystem where various requests are missing item types (flags). Using these requests without the proper item types specified can cause privilege escalation to root.  | High  
  
### GKE on Azure

**Updated:** 2022-09-14

Description | Severity  
---|---  
A new vulnerability (CVE-2022-2327) has been discovered in the Linux kernel that can lead to local privilege escalation. This vulnerability allows an unprivileged user to achieve a full container breakout to root on the node.

#### What should I do?

**2022-09-14 Update:** The following versions of GKE on Azure have been updated with code to fix this vulnerability. We recommend that you upgrade your nodes to one of the following GKE on Azure versions: 

  * 1.23.8-gke.1700
  * 1.22.12-gke.200
  * 1.21.14-gke.2100



* * *

Versions of GKE on Azure that contain patches will be released soon. This security bulletin will be updated when the GKE on Azure versions are available for download. 

#### What vulnerabilities are addressed by this patch?

  * [CVE-2022-2327](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2327)

With CVE-2022-2327, the Linux kernel in version 5.10 has a vulnerability in the io_uring subsystem where various requests are missing item types (flags). Using these requests without the proper item types specified can cause privilege escalation to root.  | High  
  
### Google Distributed Cloud Virtual for Bare Metal

Description | Severity  
---|---  
A new vulnerability (CVE-2022-2327) has been discovered in the Linux kernel that can lead to local privilege escalation. This vulnerability allows an unprivileged user to achieve a full container breakout to root on the node. 

#### What should I do?

There is no action required. Google Distributed Cloud Virtual for Bare Metal is not affected by this CVE as it does not bundle an operating system in its distribution.  | None  
  
## GCP-2022-017

**Published:** 2022-06-29  
**Updated:** 2022-11-22  
**Reference:**[CVE-2022-1786](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1786)  
**2022-11-22 Update:** Updated information about workloads using GKE Sandbox.  
**2022-07-21 Update:** Updated information that GKE on VMware COS images are affected.

### GKE

**Updated:** 2022-11-22

Description | Severity  
---|---  
**2022-11-22 update:** Workloads using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) are not affected by these vulnerabilities.

* * *

A new vulnerability (CVE-2022-1786) has been discovered in the Linux kernel versions 5.10 and 5.11. This vulnerability allows an unprivileged user with local access to the cluster to achieve a full container breakout to root on the node. Only clusters that run Container-Optimized OS are affected. GKE Ubuntu versions use either version 5.4 or 5.15 of the kernel and are not affected.

#### What should I do?

The versions of Linux node images for Container-Optimized OS for the following versions of GKE have been updated with code to fix this vulnerability. For security purposes, even if you have node-autoupgrade enabled, we recommend that you [manually upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) your node pools to one of the following upcoming GKE versions:

  * 1.22.10-gke.600
  * 1.23.7-gke.1400
  * 1.24.1-gke.1400

A recent [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-%0A%20%20%20%20%20%20%20%20%20%20patch-versions) feature allows you to apply a patch without having to unsubscribe from a channel. This lets you upgrade your nodes to the patched version before that version becomes the default in your selected release channel. 

#### What vulnerabilities are addressed by this patch?

With CVE-2022-1786, a use-after-free flaw was found in the Linux kernel's io_uring subsystem. If a user sets up a ring with IORING_SETUP_IOPOLL with more than one task completing submissions on the ring, a local user can crash or escalate their privileges on the system.  | High  
  
### GKE on VMware

**Updated:** 2022-07-14

Description | Severity  
---|---  
A new vulnerability (CVE-2022-1786) has been discovered in the Linux kernel versions 5.10 and 5.11. This vulnerability allows an unprivileged user with local access to the cluster to achieve a full container breakout to root on the node.

#### What should I do?

**2022-07-21 Update:** The following versions of GKE on VMware contain code that fixes this vulnerability.

##### COS

  * 1.10.5 or later
  * 1.11.2 or later
  * 1.12.0 or later

Some of these versions might not be available immediately, and will become available in upcoming releases.

* * *

##### Ubuntu

There is no action required. GKE on VMware does not use the affected versions of the Linux kernel. | None  
  
### GKE on AWS

Description | Severity  
---|---  
A new vulnerability (CVE-2022-1786) has been discovered in the Linux kernel versions 5.10 and 5.11. This vulnerability allows an unprivileged user with local access to the cluster to achieve a full container breakout to root on the node.

#### What should I do?

There is no action required. GKE on AWS does not use the affected versions of the Linux kernel.  | None  
  
### GKE on Azure

Description | Severity  
---|---  
A new vulnerability (CVE-2022-1786) has been discovered in the Linux kernel versions 5.10 and 5.11. This vulnerability allows an unprivileged user with local access to the cluster to achieve a full container breakout to root on the node.

#### What should I do?

There is no action required. GKE on Azure does not use the affected versions of the Linux kernel. | None  
  
### Google Distributed Cloud Virtual for Bare Metal

Description | Severity  
---|---  
A new vulnerability (CVE-2022-1786) has been discovered in the Linux kernel versions 5.10 and 5.11. This vulnerability allows an unprivileged user with local access to the cluster to achieve a full container breakout to root on the node.

#### What should I do?

There is no action required. Google Distributed Cloud Virtual for Bare Metal is not affected by this CVE as it does not bundle an operating system in its distribution. | None  
  
## GCP-2022-016

**Published:** 2022-06-23  
**Updated:** 2022-11-22  
**Reference:**[CVE-2022-29581](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29581), [CVE-2022-29582](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29582), [CVE-2022-1116](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1116)  
**2022-11-22 Update:** Added information about workloads running in Autopilot clusters.  
**2022-07-29 Update:** Updated versions for GKE on VMware, GKE on AWS, and GKE on Azure.

### GKE

**Updated:** 2022-11-22

Description | Severity  
---|---  
**2022-11-22 update:** Autopilot clusters are not affected by CVE-2022-29581 but are vulnerable to CVE-2022-29582 and CVE-2022-1116.

* * *

**2022-07-29 update:** Pods using GKE Sandbox are not vulnerable to these vulnerabilities.

* * *

Three new memory corruption vulnerabilities (CVE-2022-29581, CVE-2022-29582, CVE-2022-1116) have been discovered in the Linux kernel. These vulnerabilities allow an unprivileged user with local access to the cluster to achieve a full container breakout to root on the node. All Linux clusters (Container-Optimized OS and Ubuntu) are affected.

#### What should I do?

The versions of Linux node images for both Container-Optimized OS and Ubuntu for the following versions of GKE have been updated with code to fix this vulnerability. For security purposes, even if you have node auto-upgrade enabled, we recommend that you [manually upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your node pools to one of the following GKE versions:

  * Container-Optimized OS: 
    * 1.19.16-gke.13800
    * 1.20.15-gke.8000
    * 1.21.12-gke.1500
    * 1.22.9-gke.1300
    * 1.23.6-gke.1500
    * 1.24.1-gke.1400
  * Ubuntu: 
    * 1.20.15-gke.9600
    * 1.21.13-gke.900
    * 1.22.10-gke.600
    * 1.23.7-gke.1400
    * 1.24.1-gke.1400

A recent feature of [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions) allows you to apply a patch without having to unsubscribe from a channel. This lets you upgrade your nodes to the patched version before that version becomes the default in your selected release channel.

#### What vulnerabilities are addressed by this patch?

With CVE-2022-29582, the Linux kernel in versions prior to 5.17.3 has a use-after-free due to a race condition in io_uring timeouts. CVE-2022-29581 and CVE-2022-1116 are vulnerabilities where a local attacker can cause memory corruption in io_uring or net/sched in the Linux kernel to escalate privileges to root. | High  
  
### GKE on VMware

**Updated:** 2022-07-29

Description | Severity  
---|---  
**2022-07-29 Update:** The following versions of GKE on VMware contain code that fixes these vulnerabilities. 

  * 1.9.7 or later
  * 1.10.5 or later
  * 1.11.2 or later
  * 1.12.0 or later



* * *

Three new memory corruption vulnerabilities (CVE-2022-29581, CVE-2022-29582, CVE-2022-1116) have been discovered in the Linux kernel. These vulnerabilities allow an unprivileged user with local access to the cluster to achieve a full container breakout to root on the node. These vulnerabilities affect GKE on VMware v1.9 and later for Container-Optimized OS and Ubuntu images.

#### What should I do?

Versions of GKE on VMware that contain patches will be released soon. This security bulletin will be updated when the GKE on VMware versions are available for download.

#### What vulnerabilities are addressed by this patch?

With CVE-2022-29582, the Linux kernel in versions prior to 5.17.3 has a use-after-free due to a race condition in io_uring timeouts. CVE-2022-29581 and CVE-2022-1116 are vulnerabilities where a local attacker can cause memory corruption in io_uring or net/sched in the Linux kernel to escalate privileges to root. | High  
  
### GKE on AWS

**Updated:** 2022-07-29

Description | Severity  
---|---  
**2022-07-29 Update:** Update: The following current and previous generation versions of GKE on AWS have been updated with code to fix these vulnerabilities. We recommend that you upgrade your nodes to one of the following GKE on AWS versions: Current generation: 

  * 1.23.7-gke.1300
  * 1.22.10-gke.1500
  * 1.21.11-gke.1900

Previous generation: 
  * 1.23.7-gke.1500
  * 1.22.10-gke.1500
  * 1.21.13-gke.1600



* * *

**Note:** This section applies to both the current and previous generation of GKE on AWSThree new memory corruption vulnerabilities (CVE-2022-29581, CVE-2022-29582, CVE-2022-1116) have been discovered in the Linux kernel. These vulnerabilities allow an unprivileged user with local access to the cluster to achieve a full container breakout to root on the node. These vulnerabilities affect all versions of GKE on AWS.

#### What should I do?

Versions of GKE on AWS that contain patches will be released soon. This security bulletin will be updated when the GKE on AWS versions are available for download.

#### What vulnerabilities are addressed by this patch?

With CVE-2022-29582, the Linux kernel in versions prior to 5.17.3 has a use-after-free due to a race condition in io_uring timeouts. CVE-2022-29581 and CVE-2022-1116 are vulnerabilities where a local attacker can cause memory corruption in io_uring or net/sched in the Linux kernel to escalate privileges to root. | High  
  
### GKE on Azure

Description | Severity  
---|---  
**2022-07-29 Update:** Update: The following versions of GKE on Azure have been updated with code to fix these vulnerabilities. We recommend that you upgrade your nodes to one of the following GKE on Azure versions: 

  * 1.23.7-gke.1300
  * 1.22.10-gke.1500
  * 1.21.11-gke.1900



* * *

Three new memory corruption vulnerabilities (CVE-2022-29581, CVE-2022-29582, CVE-2022-1116) have been discovered in the Linux kernel. These vulnerabilities allow an unprivileged user with local access to the cluster to achieve a full container breakout to root on the node. These vulnerabilities affect all versions of GKE on Azure.

#### What should I do?

Versions of GKE on Azure that contain patches will be released soon. This security bulletin will be updated when the GKE on Azure versions are available for download.

#### What vulnerabilities are addressed by this patch?

With CVE-2022-29582, the Linux kernel in versions prior to 5.17.3 has a use-after-free due to a race condition in io_uring timeouts. CVE-2022-29581 and CVE-2022-1116 are vulnerabilities where a local attacker can cause memory corruption in io_uring or net/sched in the Linux kernel to escalate privileges to root. | High  
  
### Google Distributed Cloud Virtual for Bare Metal

Description | Severity  
---|---  
Three new memory corruption vulnerabilities (CVE-2022-29581, CVE-2022-29582, CVE-2022-1116) have been discovered in the Linux kernel. These vulnerabilities allow an unprivileged user with local access to the cluster to achieve a full container breakout to root on the node.

#### What should I do?

There is no action required. Google Distributed Cloud Virtual for Bare Metal is not affected by this vulnerability as it does not bundle an operating system in its distribution. | None  
  
## GCP-2022-014

**Published:** 2022-04-26  
**Updated:** 2022-11-22  
**2022-11-22 Update** : Added information about workloads running in Autopilot clusters.  
**2022-05-12 Update** : Updated patch versions for GKE on AWS and GKE on Azure.  
**Reference:**[CVE-2022-1055](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1055), [CVE-2022-27666](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27666)

### GKE

**Updated:** 2022-11-22

Description | Severity  
---|---  
**2022-11-22 update:** GKE Autopilot clusters and workloads running in [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) are unaffected by these vulnerabilities.

* * *

Two security vulnerabilities, [CVE-2022-1055](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1055) and [CVE-2022-27666](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27666) have been discovered in the Linux kernel. Each can lead to a local attacker being able to perform a container breakout, privilege escalation on the host, or both. These vulnerabilities affect all GKE node operating systems (Container-Optimized OS and Ubuntu). 

#### Technical details

In CVE-2022-1055, an attacker can exploit use-after-free in tc_new_tfilter() which allows a local attacker in the container to escalate privileges to root on node. In CVE-2022-27666, buffer overflow in esp/esp6_output_head allows a local attacker in the container to escalate privileges to root on the node.

#### What should I do?

The versions of Linux node images for the following versions of GKE have been updated with code to fix these vulnerabilities. Upgrade your clusters to one of the following upcoming GKE versions:

  * 1.19.16-gke.11000 and later
  * 1.20.15-gke.5200 and later
  * 1.21.11-gke.1100 and later
  * 1.22.8-gke.200 and later
  * 1.23.5-gke.1500 and later



#### What vulnerabilities are addressed by this patch?

  * [CVE-2022-1055](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1055)
  * [CVE-2022-27666](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27666)

| High  
  
### GKE on VMware

Description | Severity  
---|---  
Two security vulnerabilities, [CVE-2022-1055](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1055) and [CVE-2022-27666](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27666) have been discovered in the Linux kernel. Each can lead to a local attacker being able to perform a container breakout, privilege escalation on the host, or both. These vulnerabilities affect all GKE node operating systems (Container-Optimized OS and Ubuntu). 

#### Technical details

In CVE-2022-1055, an attacker can exploit use-after-free in tc_new_tfilter() which allows a local attacker in the container to escalate privileges to root on node. In CVE-2022-27666, buffer overflow in esp/esp6_output_head allows a local attacker in the container to escalate privileges to root on the node.

#### What should I do?

Upgrade your cluster to a patched version. The following GKE on VMware versions or newer contain the fix for this vulnerability:

  * 1.9.6 (upcoming)
  * 1.10.3
  * 1.11.0 (upcoming)



#### What vulnerabilities are addressed by this patch?

  * [CVE-2022-1055](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1055)
  * [CVE-2022-27666](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27666)

| High  
  
### GKE on AWS

**Updated:** 2022-05-12

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSTwo security vulnerabilities, [CVE-2022-1055](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1055) and [CVE-2022-27666](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27666) have been discovered in the Linux kernel. Each can lead to a local attacker being able to perform a container breakout, privilege escalation on the host, or both. These vulnerabilities affect all GKE node operating systems (Container-Optimized OS and Ubuntu). 

#### Technical details

In CVE-2022-1055, an attacker can exploit use-after-free in tc_new_tfilter() which allows a local attacker in the container to escalate privileges to root on node. In CVE-2022-27666, buffer overflow in esp/esp6_output_head allows a local attacker in the container to escalate privileges to root on the node.

#### What should I do?

**2022-05-12 Update:** The following current and previous generation versions of GKE on AWS have been updated with code to fix these vulnerabilities. We recommend that you upgrade your nodes to one of the following GKE on AWS versions:  **Current generation**

  * 1.21.11-gke.1100
  * 1.22.8-gke.1300

**Previous generation**

  * 1.20.15-gke.5200
  * 1.21.11-gke.1100
  * 1.22.8-gke.1300



* * *

Upgrade your cluster to a patched version. Patches will be available in an upcoming release. This bulletin will be updated when they are available.

#### What vulnerabilities are addressed by this patch?

  * [CVE-2022-1055](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1055)
  * [CVE-2022-27666](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27666)

| High  
  
### GKE on Azure

**Updated:** 2022-05-12

Description | Severity  
---|---  
Two security vulnerabilities, [CVE-2022-1055](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1055) and [CVE-2022-27666](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27666) have been discovered in the Linux kernel. Each can lead to a local attacker being able to perform a container breakout, privilege escalation on the host, or both. These vulnerabilities affect all GKE node operating systems (Container-Optimized OS and Ubuntu). 

#### Technical details

In CVE-2022-1055, an attacker can exploit use-after-free in tc_new_tfilter() which allows a local attacker in the container to escalate privileges to root on node. In CVE-2022-27666, buffer overflow in esp/esp6_output_head allows a local attacker in the container to escalate privileges to root on the node.

#### What should I do?

**2022-05-12 Update:** The following versions of GKE on Azure have been updated with code to fix these vulnerabilities. We recommend that you upgrade your nodes to one of the following GKE on Azure versions: 

  * 1.21.11-gke.1100
  * 1.22.8-gke.1300



* * *

Upgrade your cluster to a patched version. Patches will be available in an upcoming release. This bulletin will be updated when they are available.

#### What vulnerabilities are addressed by this patch?

  * [CVE-2022-1055](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1055)
  * [CVE-2022-27666](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27666)

| High  
  
### Google Distributed Cloud Virtual for Bare Metal

Description | Severity  
---|---  
Two security vulnerabilities, [CVE-2022-1055](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1055) and [CVE-2022-27666](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27666) have been discovered in the Linux kernel. Each can lead to a local attacker being able to perform a container breakout, privilege escalation on the host, or both. These vulnerabilities affect all GKE node operating systems (Container-Optimized OS and Ubuntu). 

#### Technical details

In CVE-2022-1055, an attacker can exploit use-after-free in tc_new_tfilter() which allows a local attacker in the container to escalate privileges to root on node. In CVE-2022-27666, buffer overflow in esp/esp6_output_head allows a local attacker in the container to escalate privileges to root on the node.

#### What should I do?

There is no action required. Google Distributed Cloud Virtual for Bare Metal is not affected by this CVE as it does not include Linux as part of its package. You should ensure that the node images you use are updated to versions that contain the fix for CVE-2022-1055 and CVE-2022-27666. 

#### What vulnerabilities are addressed by this patch?

  * [CVE-2022-1055](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1055)
  * [CVE-2022-27666](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27666)

| High  
  
## GCP-2022-013

**Published:** 2022-04-11  
**Updated:** 2022-04-20  
**Reference:**[CVE-2022-23648](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23648)  
**2022-04-22 Update:** Updated patch versions for Google Distributed Cloud Virtual for Bare Metal and GKE on VMware.

### GKE

Description | Severity  
---|---  
A security vulnerability, CVE-2022-23648, has been discovered in containerd's handling of path traversal in the OCI image volume specification. Containers launched through containerd's CRI implementation with a specially-crafted image configuration could gain full read access to arbitrary files and directories on the host. This vulnerability may bypass any policy-based enforcement on container setup (including a Kubernetes Pod Security Policy). This vulnerability affects all GKE node operating systems (Container-Optimized OS and Ubuntu) which use containerd by default. All GKE, Autopilot, and GKE Sandbox nodes are affected. 

#### What should I do?

The versions of Linux node images for the following versions of GKE have been updated with code to fix this vulnerability. For security purposes, even if you have node-autoupgrade enabled, we recommend that you [manually upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your nodes to one of the following GKE versions: 

  * 1.19.16-gke.9400
  * 1.20.15-gke.3600
  * 1.21.10-gke.1500
  * 1.22.7-gke.1500
  * 1.23.4-gke.1500

A recent feature of [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions) allows you to apply a patch without having to unsubscribe from a channel. This lets you secure your nodes until the new version becomes the default for your specific release channel. | Medium  
  
### GKE on VMware

**Updated:** 2022-04-22

Description | Severity  
---|---  
A security vulnerability, CVE-2022-23648, has been discovered in containerd's handling of path traversal in the OCI image volume specification. Containers launched through containerd's CRI implementation with a specially-crafted image configuration could gain full read access to arbitrary files and directories on the host. This vulnerability may bypass any policy-based enforcement on container setup (including a Kubernetes Pod Security Policy). This vulnerability affects all GKE on VMware with stackdriver enabled, which uses containerd. GKE on VMware versions 1.8, 1.9, and 1.10 are affected

#### What should I do?

**2022-04-22 Update:** The following versions of GKE on VMware contain code that fixes this vulnerability. Some of these versions might not be available immediately, and will become available in upcoming releases.

  * 1.9.5 or later
  * 1.10.3 or later
  * 1.11.0 or later

This list replaces the previously published list of versions below.

* * *

The following versions of GKE on VMware have been updated with code to fix this vulnerability. We recommend that you upgrade your nodes to one of the following GKE on VMware versions:

  * 1.8.8 or later
  * 1.9.5 or later
  * 1.10.2 or later

This CVE can be mitigated by setting IgnoreImageDefinedVolumes to true. | Medium  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSA security vulnerability, CVE-2022-23648, has been discovered in containerd's handling of path traversal in the OCI image volume specification. Containers launched through containerd's CRI implementation with a specially-crafted image configuration could gain full read access to arbitrary files and directories on the host. This vulnerability may bypass any policy-based enforcement on container setup (including a Kubernetes Pod Security Policy). All GKE on AWS versions are affected.

#### What should I do?

The following versions of GKE on AWS have been updated with code to fix this vulnerability. We recommend that you upgrade your nodes to one of the following GKE on AWS versions.

##### GKE on AWS (current generation)

  * **Version 1.22:** 1.22.8-gke.200
  * **Version 1.21:** 1.21.11-gke.100



##### GKE on AWS (previous generation)

  * **Version 1.22:** 1.22.8-gke.300
  * **Version 1.21:** 1.21.11-gke.100
  * **Version 1.20:** 1.20.15-gke.2200

This CVE can be mitigated by setting IgnoreImageDefinedVolumes to true. | Medium  
  
### GKE on Azure

Description | Severity  
---|---  
A security vulnerability, CVE-2022-23648, has been discovered in containerd's handling of path traversal in the OCI image volume specification. Containers launched through containerd's CRI implementation with a specially-crafted image configuration could gain full read access to arbitrary files and directories on the host. This vulnerability may bypass any policy-based enforcement on container setup (including a Kubernetes Pod Security Policy). All GKE on Azure versions are affected.

#### What should I do?

The following versions of GKE on Azure have been updated with code to fix this vulnerability. We recommend that you upgrade your nodes as follows:

  * **Version 1.22:** 1.22.8-gke.200
  * **Version 1.21:** 1.21.11-gke.100

This CVE can be mitigated by setting IgnoreImageDefinedVolumes to true. | Medium  
  
### Google Distributed Cloud Virtual for Bare Metal

**Updated:** 2022-04-22

Description | Severity  
---|---  
A security vulnerability, CVE-2022-23648, has been discovered in containerd's handling of path traversal in the OCI image volume specification. Containers launched through containerd's CRI implementation with a specially-crafted image configuration could gain full read access to arbitrary files and directories on the host. This vulnerability may bypass any policy-based enforcement on container setup (including a Kubernetes Pod Security Policy). This vulnerability affects all Google Distributed Cloud Virtual for Bare Metal which use containerd. Google Distributed Cloud Virtual for Bare Metal versions 1.8, 1.9, and 1.10 are affected

#### What should I do?

**2022-04-22 Update:** The following versions of Google Distributed Cloud Virtual for Bare Metal contain code that fixes this vulnerability. Some of these versions might not be available immediately, and will become available in upcoming releases.

  * 1.8.9 or later
  * 1.9.6 or later
  * 1.10.3 or later
  * 1.11.0 or later

This list replaces the previously published list of versions below.

* * *

The following versions of Google Distributed Cloud Virtual for Bare Metal have been updated with code to fix this vulnerability. We recommend that you upgrade your nodes to one of the following Google Distributed Cloud Virtual for Bare Metal versions:

  * 1.8.8 or later
  * 1.9.5 or later
  * 1.10.2 or later

This CVE can be mitigated by setting IgnoreImageDefinedVolumes to true. | Medium  
  
## GCP-2022-012

**Published:** 2022-04-07  
**Updated:** 2022-11-22  
**Reference:**[CVE-2022-0847](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0847)  
**2022-11-22 Update:** Updated information about workloads using GKE Sandbox.

### GKE

**Updated:** 2022-11-22

Description | Severity  
---|---  
**2022-11-22 update:** Workloads using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) are not affected by these vulnerabilities.

* * *

A security vulnerability, CVE-2022-0847, has been discovered in the Linux kernel version 5.8 and later that can potentially escalate container privileges to root. This vulnerability affects all GKE node pool versions v1.22 and later that use Container-Optimized OS images (Container-Optimized OS 93 and later). GKE node pools that use the Ubuntu OS are not affected. 

#### What should I do?

The versions of Linux node images for the following versions of GKE have been updated with code to fix this vulnerability. For security purposes, even if you have node-autoupgrade enabled, we recommend that you [manually upgrade](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your node pools to one of the following GKE versions: 

  * 1.22.7-gke.1500 and later
  * 1.23.4-gke.1600 and later

A recent feature of [release channels](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions) allows you to apply a patch version of other release channels without having to unsubscribe from a channel. This lets you secure your nodes until the new version becomes the default for your release specific channel.

#### What vulnerabilities are addressed by this patch?

CVE-2022-0847 relates to the PIPE_BUF_FLAG_CAN_MERGE flag that was introduced in version 5.8 of the Linux kernel. In this vulnerability, the "flags" member of the new pipe buffer structure was lacking proper initialization in the Linux kernel. An unprivileged local attacker can use this flaw to write to pages in the page cache backed by read only files and escalate their privileges. New versions of Container-Optimized OS that fix this issue have been integrated into the updated node pool versions of GKE. | High  
  
### GKE on VMware

Description | Severity  
---|---  
A security vulnerability, CVE-2022-0847, has been discovered in the Linux kernel version 5.8 and later that can potentially escalate privileges to root. This vulnerability affects GKE on VMware v1.10 for Container-Optimized OS images. Currently, GKE on VMware with Ubuntu is on kernel version 5.4 and is not vulnerable to this attack. 

#### What should I do?

The versions of Linux node images for the following versions of GKE on VMware have been updated with code to fix this vulnerability. We recommend that you upgrade your admin and user clusters to the following GKE on VMware version:

  * 1.10.3



#### What vulnerabilities are addressed by this patch?

CVE-2022-0847 relates to the PIPE_BUF_FLAG_CAN_MERGE flag that was introduced in version 5.8 of the Linux kernel. In this vulnerability, the "flags" member of the new pipe buffer structure was lacking proper initialization in the Linux kernel. An unprivileged local attacker can use this flaw to write to pages in the page cache backed by read only files and escalate their privileges. New versions of Container-Optimized OS that fix this issue have been integrated into the updated versions of GKE on VMware. | High  
  
### GKE on AWS

Description | Severity  
---|---  
**Note:** This section applies to both the current and previous generation of GKE on AWSA security vulnerability, CVE-2022-0847, has been discovered in the Linux kernel version 5.8 and later that can potentially escalate privileges to root. This vulnerability affects managed clusters of GKE on AWS v1.21 and clusters running on GKE on AWS (previous generation) v1.19, v1.20, v1.21, which use Ubuntu.

#### What should I do?

The versions of Linux node images for the following versions of GKE on AWS have been updated with code to fix this vulnerability. For managed GKE on AWS, we recommend that you upgrade your user clusters and nodepool to one of the following versions:

  * 1.21.11-gke.100

For k-lite GKE on AWS, we recommend that you [upgrade](https://cloud.google.com/anthos/clusters/docs/aws/how-to/upgrading) your AWSManagementService, AWSCluster and AWSNodePool objects to the following version:

  * 1.21.11-gke.100
  * 1.20.15-gke.2200



#### What vulnerabilities are addressed by this patch?

CVE-2022-0847 relates to the PIPE_BUF_FLAG_CAN_MERGE flag that was introduced in version 5.8 of the Linux kernel. In this vulnerability, the "flags" member of the new pipe buffer structure was lacking proper initialization in the Linux kernel. An unprivileged local attacker can use this flaw to write to pages in the page cache backed by read only files and escalate their privileges. | High  
  
### GKE on Azure

Description | Severity  
---|---  
A security vulnerability, CVE-2022-0847, has been discovered in the Linux kernel version 5.8 and later that can potentially escalate privileges to root. This vulnerability affects managed clusters of GKE on Azure v1.21 which use Ubuntu. 

#### What should I do?

The versions of Linux node images for the following versions of GKE on Azure have been updated with code to fix this vulnerability. We recommend that you upgrade your user clusters and nodepool to the following version:

  * 1.21.11-gke.100



#### What vulnerabilities are addressed by this patch?

CVE-2022-0847 relates to the PIPE_BUF_FLAG_CAN_MERGE flag that was introduced in version 5.8 of the Linux kernel. In this vulnerability, the "flags" member of the new pipe buffer structure was lacking proper initialization in the Linux kernel. An unprivileged local attacker can use this flaw to write to pages in the page cache backed by read only files and escalate their privileges. | High  
  
### Google Distributed Cloud Virtual for Bare Metal

Description | Severity  
---|---  
A security vulnerability, CVE-2022-0847, has been discovered in the Linux kernel version 5.8 and later that can potentially escalate privileges to root.

#### What should I do?

**There is no action required.** Google Distributed Cloud Virtual for Bare Metal is not affected by this CVE as it does not include Linux as part of its package. You should ensure that the node images you use are updated to versions that contain the fix for CVE-2022-0847. | High  
  
## GCP-2022-011

**Published:** 2022-03-22  
**Updated:** 2022-08-11  


**2022-08-11 Update:** Added more details about the effects of the SMT misconfiguration.

### GKE

Description | Severity  
---|---  
**Update 2022-08-11:** Added more information about the Simultaneous Multi-Threading (SMT) configuration. SMT was intended to be disabled, but was enabled on the versions listed. If you manually enabled SMT for a sandboxed node pool, SMT will remain manually enabled despite this issue.

* * *

There is a misconfiguration with Simultaneous Multi-Threading (SMT), also known as Hyper-threading, on GKE Sandbox images. The misconfiguration leaves nodes potentially exposed to side channel attacks such as Microarchitectural Data Sampling (MDS) (for more context, see [GKE Sandbox documentation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods#hyper-threading_is_disabled)). We do not recommend using the following affected versions: 

  * 1.22.4-gke.1501
  * 1.22.6-gke.300
  * 1.23.2-gke.300
  * 1.23.3-gke.600

If you manually [enabled SMT for a node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods#hyper-threading_is_disabled), then this issue does not affect your sandboxed nodes. 

####  What should I do?

Upgrade your nodes to one of the following versions:

  * 1.22.6-gke.1500 and later
  * 1.23.3-gke.1100 and later



#### What vulnerability is addressed by this patch?

GKE Sandbox nodes have SMT disabled by default, mitigating side-channel attacks. | Medium  
  
## GCP-2022-009

**Published:** 2022-03-01  
**Updated:** 2022-03-15

### GKE

Description | Severity  
---|---  
**Update 2022-03-15:** Added hardening guides for GKE on AWS and GKE on Azure. Added a section on persistence using webhooks.

* * *

Some unexpected paths to access the node VM on GKE Autopilot clusters could have been used to escalate privileges in the cluster. These issues have been fixed and **no further action is required**. The fixes address issues reported through our [Vulnerability Reward Program](https://bughunters.google.com/about). GKE Standard and GKE clusters users can optionally apply a similar hardening policy as described below.

#### Technical details

**Note:** The security boundary for GKE nodes is the single-tenant virtual machine, and as such the ability to access the node VM from pods is [not considered a security boundary for Autopilot](https://cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview#security-boundaries). Nodes are not shared between clusters or customers. Any actor taking advantage of these issues must first be granted access to the cluster itself with at least permissions to schedule pods.

##### Host access using third party policy exemptions

In order to allow Google Cloud to offer full management of nodes, and a Pod-level SLA, GKE Autopilot restricts some highly privileged Kubernetes primitives to limit workloads from having low-level access to the node VM. To set this in context: GKE Standard presents full access to the underlying compute, Autopilot presents limited access, and Cloud Run presents no access. Autopilot relaxes some of those restrictions for a [predefined list of third party tools](https://cloud.google.com/blog/products/containers-kubernetes/partner-devops-and-security-solutions-for-gke-autopilot) to allow customers to run those tools on Autopilot without modification. Using privileges to create pods with host path mounts, the researcher was able to run a privileged container in a pod that looked like one of these allowlisted third party tools to gain access to the host. The ability to schedule pods in this way is expected on GKE Standard, but not on GKE Autopilot, as it bypassed the host-access restrictions used to enable the SLA described previously.  **This issue was fixed by tightening the third party allow-listing pod specification.**

##### Privilege escalation from root-on-node

In addition to the host access, the `stackdriver-metadata-agent-cluster-level` and the `metrics-server` pods were identified as highly privileged. After gaining root-level access to the node, these services could be used to gain further control over the cluster. We have deprecated and removed the `stackdriver-metadata-agent` for both GKE Standard and Autopilot. This component is still in use on GKE on VMware and Google Distributed Cloud Virtual for Bare Metal. As a system hardening measure to prevent this type of attack in the future, we'll apply an Autopilot constraint in an upcoming release that prevents updates to the service account of various objects in the `kube-system` namespace. We developed a [Gatekeeper policy](https://github.com/open-policy-agent/gatekeeper-library/tree/master/library/general/noupdateserviceaccount) for you to apply similar protection to GKE Standard clusters and GKE clusters to prevent privileged workload self-modification. This policy is applied automatically for Autopilot clusters. For instructions, refer to the following hardening guides: 

  * [GKE Standard](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#restrict_self_modify)
  * [GKE on VMware](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/hardening-your-cluster#restrict_self_modify)
  * [Google Distributed Cloud Virtual for Bare Metal](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/hardening-your-cluster#restrict_self_modify)
  * **Update 2022-03-15:** [GKE on AWS](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/aws/concepts/security#restrict_self_modify)
  * **Update 2022-03-15:** [GKE on Azure](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/azure/concepts/security#restrict_self_modify)



* * *

##### **Addition 2022-03-15:** Persistence using mutating webhooks

Mutating webhooks were used in [the report](https://unit42.paloaltonetworks.com/gke-autopilot-vulnerabilities/) to establish a privileged foothold in the cluster post-compromise. These are standard parts of the Kubernetes API created by cluster admins, and were made visible to administrators when Autopilot added support for customer-defined webhooks.

* * *

##### Privileged service accounts in the default namespace

Autopilot policy enforcers previously allowlisted two service accounts in the default namespace: `csi-attacher` and `otelsvc` to give the service accounts special privileges. An attacker with high privileges, including permissions to create `ClusterRoleBinding` objects and with access to create pods in the default namespace, could use these service account names to access those additional privileges. These services were moved under the `kube-system` namespace to get the protection of existing Autopilot policy. GKE Standard clusters and GKE clusters are unaffected.

####  What should I do?

All GKE Autopilot clusters have had their policies updated to remove the unintended host access and **no further action is required**.  Further policy hardening will be applied to Autopilot in the coming weeks as a secondary protection. **No action is required.** GKE Standard clusters and GKE clusters are unaffected as users already have access to the host. As a system hardening measure, GKE Standard clusters and GKE clusters users can apply similar protection with a [Gatekeeper policy](https://github.com/open-policy-agent/gatekeeper-library/tree/master/library/general/noupdateserviceaccount) that prevents privileged workload self-modification. For instructions, refer to the following hardening guides: 

  * [GKE Standard](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#restrict_self_modify)
  * [GKE on VMware](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/hardening-your-cluster#restrict_self_modify)
  * [Google Distributed Cloud Virtual for Bare Metal](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/hardening-your-cluster#restrict_self_modify)
  * **Update 2022-03-15:** [GKE on AWS](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/aws/concepts/security#restrict_self_modify)
  * **Update 2022-03-15:** [GKE on Azure](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/azure/concepts/security#restrict_self_modify)

| Low  
  
## GCP-2022-008

**Published:** 2022-02-23  
**Updated:** 2022-04-28  
**Reference:** [CVE-2022-23606](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23606), [CVE-2022-21655](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21655), [CVE-2021-43826](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43826), [CVE-2021-43825](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43825), [CVE-2021-43824](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43824), [CVE-2022-21654](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21654), [CVE-2022-21657](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21657), [CVE-2022-21656](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21656)

### GKE

Description | Severity  
---|---  
The Envoy project recently discovered a set of vulnerabilities, [CVE-2022-23606](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23606), [CVE-2022-21655](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21655), [CVE-2021-43826](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43826), [CVE-2021-43825](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43825), [CVE-2021-43824](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43824), [CVE-2022-21654](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21654), [CVE-2022-21657](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21657), and [CVE-2022-21656](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21656) which may impact GKE clusters using _Anthos Service Mesh_ , _Istio-on-GKE_ , or custom Istio deployments.   
All issues listed below are fixed in Envoy release 1.21.1.  
**Technical Background**  
Additional details for these vulnerabilities are available [here](https://cloud.google.com/service-mesh/docs/security-bulletins#GCP-2022-007).  


#### What should I do?

GKE clusters running Anthos Service Mesh should upgrade to a supported version with fix to the above vulnerabilities   


  * **If you're using Anthos Service Mesh 1.12, upgrade to v1.12.4-asm.0.**
  * **If you're using Anthos Service Mesh 1.11, upgrade to v1.11.7-asm.1.**
  * **If you're using Anthos Service Mesh 1.10, upgrade to v1.10.6-asm.1**.

**If you're using Anthos Service Mesh v1.9 or below** , **your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to ASM 1.10 or above.**  
  
GKE clusters running Istio-on-GKE should upgrade to a supported version with fix to the above vulnerabilities   


  * **If you're using Istio-on-GKE 1.6, upgrade to v1.6.14-gke.8.**
  * **If you're using Istio-on-GKE 1.4.11, upgrade to v1.4.11-gke.4.**
  * **If you're using Istio-on-GKE 1.4.10, upgrade to v1.4.10-gke.23.**
  * **If you are using GKE 1.22 or higher, please use Istio GKE 1.4.10. Otherwise, use Istio-on-GKE 1.4.11.**

**Warning:** Istio-on-GKE is deprecated. _After**December 31, 2021** , the UI no longer supports this feature during the creation of new clusters. After **September 30, 2022** , Istio-on-GKE will no longer be supported in existing clusters. You can [migrate Istio on GKE to Anthos Service Mesh](https://docs.cloud.google.com/istio/docs/istio-on-gke/migrate-to-anthos-service-mesh) to continue using your service meshes. For more information, see the [migration FAQ](https://docs.cloud.google.com/istio/docs/istio-on-gke/migrate-to-anthos-service-mesh)._  
Envoy users managing their own Envoys or Istio should ensure that they are using Envoy release 1.21.1. Envoy users managing their own Envoys build the binaries from a source like GitHub and deploy them.

#### What vulnerabilities are addressed by this patch?

[CVE-2022-23606](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23606), [CVE-2022-21655](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21655), [CVE-2021-43826](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43826), [CVE-2021-43825](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43825), [CVE-2021-43824](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43824), [CVE-2022-21654](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21654), [CVE-2022-21657](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21657), and [CVE-2022-21656](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21656) | High  
  
### GKE on VMware

**Updated:** 2022-04-28

Description | Severity  
---|---  
Envoy recently released multiple security vulnerability fixes. GKE on VMware is impacted because Envoy is used with metrics-server. The Envoy CVEs we are fixing are listed below. We will update this bulletin with specific versions when they're available:  


  * **CVE-2021-43824** (CVSS score 6.5, Medium): Potential null pointer dereference when using JWT filter safe_regex match.  
Note: Although ASM/Istio-on-GKE do not support Envoy filters, you could be impacted if you use JWT filter regex _._
  * **CVE-2021-43825** (CVSS score 6.1, Medium): Use-after-free when response filters increase response data, and increased data exceeds downstream buffer limits.  
Note: Although ASM/Istio-on-GKE do not support Envoy filters, you could be impacted if you use a decompress filter.
  * **CVE-2021-43826** (CVSS score 6.1, Medium): Use-after-free when tunneling TCP over HTTP, if downstream disconnects during upstream connection establishment.  
Note: Although ASM/Istio-on-GKE do not support Envoy filters, you could be impacted if you use a tunneling filter.
  * **CVE-2022-21654** (CVSS score 7.3, High): Incorrect configuration handling allows mTLS session reuse without re-validation after validation settings have changed.  
Note: All ASM/Istio-on-GKE services using mTLS are impacted by this CVE.
  * **CVE-2022-21655** (CVSS score 7.5, High): Incorrect handling of internal redirects to routes with a direct response entry.  
Note: Although ASM/Istio-on-GKE do not support Envoy filters, you could be impacted if you use a direct response filter.
  * **CVE-2022-23606** (CVSS score 4.4, Medium): Stack exhaustion when a cluster is deleted via Cluster Discovery Service.  
Note: ASM 1.11+ are impacted by this CVE. ASM 1.10 and All Istio-on-GKE are not impacted by this CVE.
  * **CVE-2022-21657** (CVSS Score 3.1, Low): Envoy through 1.20.1 contains a remotely exploitable vulnerability due to X.509 Extended Key Usage and Trust Purposes bypass.
  * **CVE-2022-21656** (CVSS Score 3.1, Low): Envoy through 1.20.1 contains a remotely exploitable vulnerability due to X.509 subjectAltName matching (and nameConstraints) bypass. 

Istio recently released one security vulnerability fix. Anthos on VMware is impacted because Istio is used for ingress. The Istio CVEs we are fixing are listed below. We will update this bulletin with specific versions when they're available: **CVE-2022-23635** (CVSS score 7.5, High): Istiod crashes upon receiving requests with a specially crafted `authorization` header.  
Note: All ASM/Istio-on-GKE are impacted by this CVE.  
  
For the full descriptions and impacts of the above CVEs, please refer to the [security bulletins](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#GCP-2022-007). 

* * *

#### **2022-04-28 Addition:** What should I do?

The following versions of GKE on VMware fix these vulnerabilities: 

  * 1.9.5
  * 1.10.3
  * 1.11.0



* * *

#### What vulnerabilities are addressed by this patch?

[CVE-2022-23606](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23606), [CVE-2022-21655](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21655), [CVE-2021-43826](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43826), [CVE-2021-43825](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43825), [CVE-2021-43824](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43824), [CVE-2022-21654](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21654), [CVE-2022-21657](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21657), and [CVE-2022-21656](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21656) | High  
  
### Google Distributed Cloud Virtual for Bare Metal

Description | Severity  
---|---  
Envoy recently released multiple security vulnerability fixes. Anthos on Bare metal is impacted because Envoy is used for metrics-server. The Envoy CVEs we are fixing in release 1.10.3, 1.9.6, and 1.8.9 are listed below:  


  * **CVE-2021-43824** (CVSS score 6.5, Medium): Potential null pointer dereference when using JWT filter safe_regex match.  
Note: Although ASM/Istio-on-GKE do not support Envoy filters, you could be impacted if you use JWT filter regex.
  * **CVE-2021-43825** (CVSS score 6.1, Medium): Use-after-free when response filters increase response data, and increased data exceeds downstream buffer limits.  
Note: Although ASM/Istio-on-GKE do not support Envoy filters, you could be impacted if you use a decompress filter.
  * **CVE-2021-43826** (CVSS score 6.1, Medium): Use-after-free when tunneling TCP over HTTP, if downstream disconnects during upstream connection establishment.  
Note: Although ASM/Istio-on-GKE do not support Envoy filters, you could be impacted if you use a tunneling filter.
  * **CVE-2022-21654** (CVSS score 7.3, High): Incorrect configuration handling allows mTLS session reuse without re-validation after validation settings have changed.  
Note: All ASM/Istio-on-GKE services using mTLS are impacted by this CVE.
  * **CVE-2022-21655** (CVSS score 7.5, High): Incorrect handling of internal redirects to routes with a direct response entry.  
Note: Although ASM/Istio-on-GKE do not support Envoy filters, you could be impacted if you use a direct response filter.
  * **CVE-2022-23606** (CVSS score 4.4, Medium): Stack exhaustion when a cluster is deleted via Cluster Discovery Service.  
Note: ASM 1.11+ are impacted by this CVE. ASM 1.10 and All Istio-on-GKE are not impacted by this CVE.
  * **CVE-2022-21657** (CVSS Score 3.1, Low): Envoy through 1.20.1 contains a remotely exploitable vulnerability due to X.509 Extended Key Usage and Trust Purposes bypass.
  * **CVE-2022-21656** (CVSS Score 3.1, Low): Envoy through 1.20.1 contains a remotely exploitable vulnerability due to X.509 subjectAltName matching (and nameConstraints) bypass. 

Istio recently released one security vulnerability fix. Anthos on Bare metal is impacted because Istio is used for ingress. The Istio CVE we are fixing in release 1.10.3, 1.9.6, and 1.8.9 is listed below:  
  


  * **CVE-2022-23635** (CVSS score 7.5, High): Istiod crashes upon receiving requests with a specially crafted `authorization` header.  
_Note: All ASM/Istio-on-GKE are impacted by this CVE._

  
For the full descriptions and impacts of the above CVEs, please refer to the [security bulletins](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#GCP-2022-007). 

#### What vulnerabilities are addressed by this patch?

[CVE-2022-23606](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23606), [CVE-2022-21655](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21655), [CVE-2021-43826](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43826), [CVE-2021-43825](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43825), [CVE-2021-43824](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43824), [CVE-2022-21654](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21654), [CVE-2022-21657](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21657), and [CVE-2022-21656](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21656) | High  
  
## GCP-2022-006

**Published:** 2022-02-14  
**Updated:** 2022-05-16  
**2022-05-16 Update:** Added GKE version 1.19.16-gke.7800 or later to the list of versions that have code to fix this vulnerability.  
**2022-05-12 Update:** Updated patch versions for GKE, Google Distributed Cloud Virtual for Bare Metal, GKE on VMware, and GKE on AWS. Fixed an issue where the security bulletin for GKE on AWS was not displayed when it was added on 2022-02-23. 

### GKE

Description | Severity  
---|---  
A security vulnerability, CVE-2022-0492, has been discovered in the Linux kernel's `cgroup_release_agent_write` function. The attack uses unprivileged user namespaces and under certain circumstances this vulnerability can be exploitable for container breakout. 

####  What should I do?

**2022-05-16 Update:** In addition to the GKE versions mentioned in the 2022-05-12 update, GKE version 1.19.16-gke.7800 or later also contains code that fixes this vulnerability. 

* * *

**2022-05-12 Update:** The following versions of GKE contain code that fixes this vulnerability: 

  * 1.20.15-gke.5600 or later
  * 1.21.11-gke.1500 or later
  * 1.22.8-gke.1800 or later
  * 1.23.5-gke.1800 or later



* * *

**Update 2022-02-15:** Corrected gVisor statement. 

* * *

The vulnerability is found in the Linux kernel's `cgroup_release_agent_write` in the `kernel/cgroup/cgroup-v1.c` function and can be used as a container breakout. GKE is unaffected due to protection from the default AppArmor profile on Ubuntu and COS. However, some customers may still be vulnerable if they have loosened security restrictions on pods through modification of the Pod or container securityContext field e.g. by disabling/changing the AppArmor profile, which is not recommended. In addition to the default AppArmor profile, these features also protect against the vulnerability:

  * _GKE Autopilot_ is unaffected due to the default seccomp profile.
  * **Update 2022-02-15:** gVisor (_GKE Sandbox_) is unaffected as gVisor doesn't allow access to the vulnerable system call on the host.

Patches will be available in an upcoming release. This bulletin will be updated when they are available. 

#### What vulnerability is addressed by this patch?

CVE-2022-0492 | Low  
  
### GKE clusters on

Description | Severity  
---|---  
A security vulnerability, CVE-2022-0492, has been discovered in the Linux kernel's `cgroup_release_agent_write` function. The attack uses unprivileged user namespaces and under certain circumstances this vulnerability can be exploitable for container breakout. 

####  What should I do?

**2022-05-12 Update:** The following versions of GKE on VMware contain code that fixes this vulnerability.  Some of these versions might not be available immediately, and will become available in upcoming releases. **COS**

  * 1.8.8 or later
  * 1.9.5 or later
  * 1.10.2 or later
  * 1.11.0 or later

**Ubuntu**

  * 1.9.6 or later
  * 1.10.3 or later
  * 1.11.0 or later



* * *

The vulnerability is found in the Linux kernel's cgroup_release_agent_write in the kernel/cgroup/cgroup-v1.c function and can be used as a container breakout. GKE on VMware are unaffected due to protection from the default AppArmor profile on Ubuntu and COS. However, some customers may still be vulnerable if they have loosened security restrictions on pods through modification of the Pod or container securityContext field e.g. by disabling/changing the AppArmor profile, which is not recommended. Patches will be available in an upcoming release. This bulletin will be updated when they are available.

#### What vulnerability is addressed by this patch?

CVE-2022-0492 | Low  
  
### GKE on AWS

Description | Severity  
---|---  
A security vulnerability, CVE-2022-0492, has been discovered in the Linux kernel's `cgroup_release_agent_write` function. The attack uses unprivileged user namespaces and under certain circumstances this vulnerability can be exploitable for container breakout. 

####  What should I do?

**2022-05-12 Update:** The following versions of current and previous generation GKE on AWS contain code that fixes this vulnerability:  **Current generation**

  * 1.21.11-gke.1100
  * 1.22.8-gke.1300

**Previous generation**

  * 1.22.8-gke.1300
  * 1.21.11-gke.1100
  * 1.20.15-gke.5200



* * *

**Update 2022-02-23:** Added note for GKE on AWS. GKE on AWS previous and current generations are unaffected due to protection from the default AppArmor profile on Ubuntu. However, some customers may still be vulnerable if they have loosened security restrictions on pods through modification of the Pod or container securityContext field e.g. by disabling/changing the AppArmor profile, which is not recommended. Patches will be available in an upcoming release. This bulletin will be updated when they are available.

#### What vulnerability is addressed by this patch?

CVE-2022-0492 | Low  
  
### GKE Enterprise on

Description | Severity  
---|---  
A security vulnerability, CVE-2022-0492, has been discovered in the Linux kernel's `cgroup_release_agent_write` function. The attack uses unprivileged user namespaces and under certain circumstances this vulnerability can be exploitable for container breakout. 

####  What should I do?

**2022-05-12 Update:** The following versions of GKE on Azure contain code that fixes this vulnerability: 

  * 1.21.11-gke.1100
  * 1.22.8-gke.1300



* * *

GKE on Azure are unaffected due to protection from the default AppArmor profile on Ubuntu. However, some customers may still be vulnerable if they have loosened security restrictions on pods through modification of the Pod or container securityContext field e.g. by disabling/changing the AppArmor profile, which is not recommended. Patches will be available in an upcoming release. This bulletin will be updated when they are available.

#### What vulnerability is addressed by this patch?

CVE-2022-0492 | Low  
  
## GCP-2022-005

**Published:** 2022-02-11  
**Updated:** 2022-02-15  
**Reference:**[CVE-2021-43527](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43527)  


### GKE

Description | Severity  
---|---  
**Update 2022-02-15:** Some GKE versions mentioned in the original bulletin were combined with other fixes and had their version numbers incremented prior to release. Patches are available in the following GKE versions: 

  * 1.20.15-gke.300
  * 1.21.9-gke.300
  * 1.22.6-gke.1000



* * *

A security vulnerability, CVE-2021-43527, has been discovered in any binary that links to the vulnerable versions of libnss3 found in NSS (Network Security Services) versions prior to 3.73 or 3.68.1. Applications using NSS for certificate validation or other TLS, X.509, OCSP or CRL functionality may be impacted, depending on how NSS is used/configured. Both GKE COS and Ubuntu images have a vulnerable version installed, and need to be patched. Potentially, CVE-2021-43527 can have a wide impact across applications using NSS for handling signatures encoded within CMS, S/MIME, PKCS#7, or PKCS#12. As well as applications using NSS for certificate validation or other TLS, X.509, OCSP or CRL functionality may be impacted. Impact depends on how NSS is used/configured. GKE doesn't use libnss3 for any Internet-accessible APIs. The impact is limited to on-host code running outside containers, which is small due to the minimal design of Chrome OS. GKE code running inside containers using the golang distroless base image is unaffected.

#### What should I do?

The versions of Linux node images for the following versions of GKE have been updated with code to fix these vulnerabilities. Upgrade your control plane and nodes to one of the following GKE versions:

  * 1.18 version to be determined
  * 1.19.16-gke.6100
  * 1.20.15-gke.200
  * 1.21.9-gke.200
  * 1.22.6-gke.600
  * 1.23.3-gke.500

Are you using a GKE version older than 1.18? You are using a GKE version [ out of SLA](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule#schedule_for_static_no_channel_versions) and should consider upgrading to one of the supported versions. 

#### What vulnerability is addressed by this patch?

[CVE-2021-43527](https://nvd.nist.gov/vuln/detail/CVE-2021-43527) | Medium  
  
### GKE clusters on

Description | Severity  
---|---  
A security vulnerability, CVE-2021-43527, has been discovered in any binary that links to the vulnerable versions of libnss3 found in NSS (Network Security Services) versions prior to 3.73 or 3.68.1. Applications using NSS for certificate validation or other TLS, X.509, OCSP or CRL functionality may be impacted, depending on how they configure NSS. Both GKE on VMware COS and Ubuntu images have a vulnerable version installed, and need to be patched. Potentially, CVE-2021-43527 can have a wide impact across with applications using NSS for handling signatures encoded within CMS, S/MIME, PKCS \\#7, or PKCS \\#12. As well as applications using NSS for certificate validation or other TLS, X.509, OCSP or CRL functionality may be impacted. Impact depends on how they configure/use NSS. Anthos on VMware doesn't use libnss3 for any publicly accessible APIs, therefore the impact is limited and this CVE's severity for GKE on VMware is rated as Medium.

#### What should I do?

Note: Your clusters might not have these versions available immediately. Rollouts are expected to begin in a few weeks and take multiple days to be completed across all Google Cloud zones.The versions of Linux node images for the following versions of Anthos have been updated with code to fix these vulnerabilities. Upgrade your control plane and nodes to one of the following Anthos versions:

  * 1.8.7
  * 1.9.4
  * 1.10.2

Are you using an GKE on VMware version older than 1.18? You are using an Anthos version [out of SLA](https://docs.cloud.google.com/anthos/docs/support/getting-support#version_support_policy) and should consider upgrading to one of the supported versions.

#### What vulnerability is addressed by this patch?

[CVE-2021-43527](https://nvd.nist.gov/vuln/detail/CVE-2021-43527) | Medium  
  
### GKE Enterprise on

Description | Severity  
---|---  
A security vulnerability, CVE-2021-43527, has been discovered in any binary that links to the vulnerable versions of libnss3 found in NSS (Network Security Services) versions prior to 3.73 or 3.68.1. Applications using NSS for certificate validation or other TLS, X.509, OCSP or CRL functionality may be impacted, depending on how NSS is used/configured. Anthos clusters on Azure Ubuntu images have a vulnerable version installed, and need to be patched. Potentially, CVE-2021-43527 can have a wide impact across with applications using NSS for handling signatures encoded within CMS, S/MIME, PKCS#7, or PKCS#12. As well as applications using NSS for certificate validation or other TLS, X.509, OCSP or CRL functionality may be impacted. Impact depends on how they configure/use NSS. Anthos clusters on Azure doesn't use libnss3 for any publicly accessible APIs, therefore the impact is limited and this CVE's severity for Anthos on Azure is rated as Medium. 

#### What should I do?

Note: Your clusters might not have these versions available immediately. Rollouts are expected to begin in a few weeks and take multiple days to be completed across all Google Cloud zones.The versions of Linux node images for the following versions of GKE on Azure have been updated with code to fix these vulnerabilities. Upgrade your clusters to one of the following Anthos on Azure versions:

  * v1.21.6-gke.1500



#### What vulnerability is addressed by this patch?

[CVE-2021-43527](https://nvd.nist.gov/vuln/detail/CVE-2021-43527) | Medium  
  
## GCP-2022-004

**Published:** 2022-02-04  
**Reference:**[CVE-2021-4034](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-4034)  


### GKE

Description | Severity  
---|---  
A security vulnerability, [CVE-2021-4034](https://nvd.nist.gov/vuln/detail/CVE-2021-4034), has been discovered in pkexec, a part of the Linux policy kit package (polkit), that allows an authenticated user to perform a privilege escalation attack. PolicyKit is generally used only on Linux desktop systems to allow non-root users to perform actions such as rebooting the system, installing packages, restarting services etc, as governed by a policy.

####  What should I do?

GKE is unaffected because the vulnerable module, policykit-1, is not installed on COS or Ubuntu images used in GKE. **No action is required.** | None  
  
### GKE clusters on

Description | Severity  
---|---  
A security vulnerability, [CVE-2021-4034](https://nvd.nist.gov/vuln/detail/CVE-2021-4034), has been discovered in pkexec, a part of the Linux policy kit package (polkit), that allows an authenticated user to perform a privilege escalation attack. PolicyKit is generally used only on Linux desktop systems to allow non-root users to perform actions such as rebooting the system, installing packages, restarting services etc, as governed by a policy. The GKE Enterprise default configuration already gives users full "sudo" privileges, so this exploit does not change GKE Enterprise existing security posture

#### Technical details

For this bug to be exploitable, an attacker needs both a non-root shell on the node filesystem and to have the vulnerable version of pkexec installed. While GKE on VMware does include a version of policykit-1 in its release images, the GKE Enterprise default configuration allows passwordless sudo to anyone with shell access already, so this vulnerability does not give a user any more privileges than they already have.

####  What should I do?

No action is required. GKE on VMware is unaffected. | None  
  
### GKE clusters on

Description | Severity  
---|---  
GKE on AWS is **unaffected**. The vulnerable module, policykit-1, is not installed on Ubuntu images used by the current and previous versions of GKE on AWS. | None  
  
### GKE Enterprise on

Description | Severity  
---|---  
A security vulnerability, [CVE-2021-4034](https://nvd.nist.gov/vuln/detail/CVE-2021-4034), has been discovered in pkexec, a part of the Linux policy kit package (polkit), that allows an authenticated user to perform a privilege escalation attack. PolicyKit is generally used only on Linux desktop systems to allow non-root users to perform actions such as rebooting the system, installing packages, restarting services etc, as governed by a policy. The GKE Enterprise default configuration already gives users full "sudo" privileges, so this exploit does not change GKE Enterprise existing security posture

#### Technical details

For this bug to be exploitable, an attacker needs both a non-root shell on the node filesystem and to have the vulnerable version of pkexec installed. While GKE on Azure does include a version of policykit-1 in its release images, the GKE Enterprise default configuration allows passwordless sudo to anyone with shell access already, so this vulnerability does not give a user any more privileges than they already have.

#### What should I do?

No action is required. GKE on Azure is unaffected. | None  
  
### GKE clusters on

Description | Severity  
---|---  
Google Distributed Cloud Virtual for Bare Metal might be affected depending on packages that are installed on the customer-managed operating system. Scan your OS images and patch them if necessary. | None  
  
## GCP-2022-002

**Published:** 2022-02-01  
**Updated:** 2022-03-07  
**Reference:**[CVE-2021-4154](https://access.redhat.com/security/cve/cve-2021-4154), [CVE-2021-22600](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2021-22600), [CVE-2022-0185](https://ubuntu.com/security/CVE-2022-0185)  
**2022-02-04 Update:** Added sections for GKE on AWS and GKE on Azure. Added rollout updates for GKE and GKE on VMware. 

### GKE

**Updated:** 2022-03-07

Description | Severity  
---|---  
Three security vulnerabilities, [CVE-2021-4154](https://access.redhat.com/security/cve/cve-2021-4154), [CVE-2021-22600](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2021-22600), and [CVE-2022-0185](https://ubuntu.com/security/CVE-2022-0185), have been discovered in the Linux kernel, each of which can lead to either a container breakout, privilege escalation on the host, or both. These vulnerabilities affect all node operating systems (COS and Ubuntu) on GKE, GKE on VMware, GKE on AWS (current and previous generation), and GKE on Azure. Pods using [GKE Sandbox](https://cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) are not vulnerable to these vulnerabilities. See the [COS release notes](https://cloud.google.com/container-optimized-os/docs/release-notes/m89) for more details.

#### Technical details

In [CVE-2021-4154](https://access.redhat.com/security/cve/cve-2021-4154), an attacker can exploit the `fsconfig` system call parameter to trigger a use-after-free bug in the linux kernel, resulting in getting root privileges. This is a local privilege escalation attack that will lead to a container breakout.  [CVE-2021-22600](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2021-22600) is a double free exploit in packet_set_ring that can lead to a container escape to the host node.  With [CVE-2022-0185](https://ubuntu.com/security/CVE-2022-0185), a heap overflow bug in legacy_parse_param() may lead to an out-of-bounds write that will cause a container breakout. The exploitation path for this vulnerability that relies on the "unshare" syscall is blocked on GKE Autopilot clusters by default using seccomp filtering.  Users who have [manually enabled the default container runtime seccomp profile](https://kubernetes.io/docs/tutorials/security/seccomp/#create-pod-that-uses-the-container-runtime-default-seccomp-profile) on GKE Standard clusters are also protected. 

####  What should I do?

**2022-03-07 Update:** The versions of Linux node images for the following versions of GKE have been updated with code to fix all these vulnerabilities for both Ubuntu and COS images. Upgrade your control plane and nodes to one of the following GKE versions.

  * 1.18.20-gke.6101
  * 1.19.16-gke.8300
  * 1.20.15-gke.2500
  * 1.21.10-gke.400
  * 1.22.7-gke.900
  * 1.23.3-gke.1100



* * *

**2022-02-25 Update:** If you use Ubuntu node images, 1.22.6-gke.1000 does not address CVE-2021-22600. We will update this bulletin with Ubuntu patch versions when they are available.

* * *

**2022-02-23 Update:** The versions of Linux node images for the following versions of GKE have been updated with code to fix these vulnerabilities. Upgrade your clusters to one of the following GKE versions.

  * 1.18.20-gke.6101
  * 1.22.6-gke.1000
  * 1.23.3-gke.1100



* * *

**2022-02-04 Update: The rollout start date for GKE patch versions was February 2.** **Note:** Your clusters might not have these versions available immediately. Rollouts began on **February 2** and take four or more business days to be completed across all Google Cloud zones.

* * *

The versions of Linux node images for the following versions of GKE have been updated with code to fix these vulnerabilities. Upgrade your clusters to one of the following GKE versions. 

  * 1.19.16-gke.6100
  * 1.20.15-gke.300
  * 1.21.9-gke.300

If you use Ubuntu node images, these versions do not address CVE-2021-22600. We will update this bulletin with Ubuntu patch versions when they are available. 1.22 and 1.23 versions are also in progress. We will update this bulletin with specific versions when they're available. 

#### What vulnerability is addressed by this patch?

  * [CVE-2021-4154](https://access.redhat.com/security/cve/cve-2021-4154)
  * [CVE-2021-22600](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2021-22600)
  * [CVE-2022-0185](https://ubuntu.com/security/CVE-2022-0185)

| High  
  
### GKE clusters on

**Updated:** 2022-02-23

Description | Severity  
---|---  
Three security vulnerabilities, [CVE-2021-4154](https://access.redhat.com/security/cve/cve-2021-4154), [CVE-2021-22600](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2021-22600), and [CVE-2022-0185](https://ubuntu.com/security/CVE-2022-0185), have been discovered in the Linux kernel, each of which can lead to either a container breakout, privilege escalation on the host, or both. These vulnerabilities affect all node operating systems (COS and Ubuntu) on GKE, GKE on VMware, GKE on AWS (current and previous generation), and GKE on Azure. See the [COS release notes](https://cloud.google.com/container-optimized-os/docs/release-notes/m89) for more details.

#### Technical details

In [CVE-2021-4154](https://access.redhat.com/security/cve/cve-2021-4154), an attacker can exploit the `fsconfig` system call parameter to trigger a use-after-free bug in the linux kernel, resulting in getting root privileges. This is a local privilege escalation attack that will lead to a container breakout.  [CVE-2021-22600](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2021-22600) is a double free exploit in packet_set_ring that can lead to a container escape to the host node.  With [CVE-2022-0185](https://ubuntu.com/security/CVE-2022-0185), a heap overflow bug in legacy_parse_param() may lead to an out-of-bounds write that will cause a container breakout. Users who have [manually enabled the default container runtime seccomp profile](https://kubernetes.io/docs/tutorials/security/seccomp/#create-pod-that-uses-the-container-runtime-default-seccomp-profile) on GKE Standard clusters are also protected. 

####  What should I do?

**2022-02-23 Update:** version 1.10.2 (Fixes CVE-2021-22600, CVE-2021-4154, and CVE-2022-0185) is now scheduled for March 1.  **2022-02-23 Update:** Added patched versions addressing CVE-2021-2260. Version 1.10.1 does not address CVE-2021-22600 but does address the other vulnerabilities. Versions 1.9.4 and 1.10.2, both unreleased, will address CVE-2021-22600. The versions of Linux node images for the following versions of GKE on VMware have been updated with code to fix these vulnerabilities. Upgrade your clusters to one of the following GKE on VMware versions:

  * 1.10.1 (Fixes CVE-2021-4154 and CVE-2022-0185. Released February 10)
  * 1.8.7 (Fixes CVE-2021-22600, CVE-2021-4154, and CVE-2022-0185. Released February 17)
  * 1.9.4 (Fixes CVE-2021-22600, CVE-2021-4154, and CVE-2022-0185. Released February 23)
  * 1.10.2 (Fixes CVE-2021-22600, CVE-2021-4154, and CVE-2022-0185. Scheduled for February 24)



* * *

**2022-02-04 Update:** Added information about Ubuntu images not addressing CVE-2021-22600. If you use Ubuntu node images, the following versions do not address CVE-2021-22600. We will update this bulletin when patches are available.The versions of Linux node images for the following versions of GKE on VMware have been updated with code to fix these vulnerabilities. Upgrade your clusters to one of the following GKE on VMware versions: 

  * 1.10.1 (COS update only. Ubuntu patch will be in 1.10.2-scheduled for February 23)
  * 1.9.4 (scheduled for February 15)
  * 1.8.7 (scheduled for February 15)



#### What vulnerability is addressed by this patch?

  * [CVE-2021-4154](https://access.redhat.com/security/cve/cve-2021-4154)
  * [CVE-2021-22600](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2021-22600)
  * [CVE-2022-0185](https://ubuntu.com/security/CVE-2022-0185)

| High  
  
### GKE clusters on

Description | Severity  
---|---  
**Note:** This section applies to the current and previous generation of GKE on AWS.Three security vulnerabilities, [CVE-2021-4154](https://access.redhat.com/security/cve/cve-2021-4154), [CVE-2021-22600](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2021-22600), and [CVE-2022-0185](https://ubuntu.com/security/CVE-2022-0185), have been discovered in the Linux kernel, each of which can lead to either a container breakout, privilege escalation on the host, or both. These vulnerabilities affect all node operating systems (COS and Ubuntu) on GKE, GKE on VMware, GKE on AWS (current and previous generation), and GKE on Azure. See the [COS release notes](https://cloud.google.com/container-optimized-os/docs/release-notes/m89) for more details.

#### Technical details

In [CVE-2021-4154](https://access.redhat.com/security/cve/cve-2021-4154), an attacker can exploit the `fsconfig` system call parameter to trigger a use-after-free bug in the linux kernel, resulting in getting root privileges. This is a local privilege escalation attack that will lead to a container breakout.  [CVE-2021-22600](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2021-22600) is a double free exploit in packet_set_ring that can lead to a container escape to the host node.  With [CVE-2022-0185](https://ubuntu.com/security/CVE-2022-0185), a heap overflow bug in legacy_parse_param() may lead to an out-of-bounds write that will cause a container breakout. Users who have [manually enabled the default container runtime seccomp profile](https://kubernetes.io/docs/tutorials/security/seccomp/#create-pod-that-uses-the-container-runtime-default-seccomp-profile) on GKE Standard clusters are also protected. 

####  What should I do?

#### GKE on AWS

The versions of Linux node images for the following versions of GKE on AWS have been updated with code to fix these vulnerabilities. Upgrade your clusters to the following GKE on AWS version:

  * 1.21.6-gke.1500 and later (available in February)

If you use Ubuntu node images, this version does not address CVE-2021-22600. We will update this bulletin when patches are available.

* * *

#### GKE on AWS (previous generation)

The versions of Linux node images for the following versions of GKE on AWS (previous generation) have been updated with code to fix these vulnerabilities. Upgrade your clusters to one of the following GKE on AWS (previous generation) versions: 

  * 1.19.16-gke.5300
  * 1.20.14-gke.2000
  * 1.21.8-gke.2000

If you use Ubuntu node images, these versions do not address CVE-2021-22600. We will update this bulletin when patches are available.

#### What vulnerability is addressed by this patch?

  * [CVE-2021-4154](https://access.redhat.com/security/cve/cve-2021-4154)
  * [CVE-2021-22600](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2021-22600)
  * [CVE-2022-0185](https://ubuntu.com/security/CVE-2022-0185)

| High  
  
### GKE Enterprise on

Description | Severity  
---|---  
Three security vulnerabilities, [CVE-2021-4154](https://access.redhat.com/security/cve/cve-2021-4154), [CVE-2021-22600](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2021-22600), and [CVE-2022-0185](https://ubuntu.com/security/CVE-2022-0185), have been discovered in the Linux kernel, each of which can lead to either a container breakout, privilege escalation on the host, or both. These vulnerabilities affect all node operating systems (COS and Ubuntu) on GKE, GKE on VMware, GKE on AWS (current and previous generation), and GKE on Azure. See the [COS release notes](https://cloud.google.com/container-optimized-os/docs/release-notes/m89) for more details.

#### Technical details

In [CVE-2021-4154](https://access.redhat.com/security/cve/cve-2021-4154), an attacker can exploit the `fsconfig` system call parameter to trigger a use-after-free bug in the linux kernel, resulting in getting root privileges. This is a local privilege escalation attack that will lead to a container breakout.  [CVE-2021-22600](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2021-22600) is a double free exploit in packet_set_ring that can lead to a container escape to the host node.  With [CVE-2022-0185](https://ubuntu.com/security/CVE-2022-0185), a heap overflow bug in legacy_parse_param() may lead to an out-of-bounds write that will cause a container breakout. Users who have [manually enabled the default container runtime seccomp profile](https://kubernetes.io/docs/tutorials/security/seccomp/#create-pod-that-uses-the-container-runtime-default-seccomp-profile) on GKE Standard clusters are also protected. 

####  What should I do?

The versions of Linux node images for the following versions of GKE on Azure have been updated with code to fix these vulnerabilities. Upgrade your clusters to the following GKE on Azure version:

  * 1.21.6-gke.1500 and later (available in February)

If you use Ubuntu node images, this version does not address CVE-2021-22600. We will update this bulletin when patches are available.

#### What vulnerability is addressed by this patch?

  * [CVE-2021-4154](https://access.redhat.com/security/cve/cve-2021-4154)
  * [CVE-2021-22600](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2021-22600)
  * [CVE-2022-0185](https://ubuntu.com/security/CVE-2022-0185)

| High  
  
## GCP-2021-024

**Published:** 2021-10-21  
**Reference:**[CVE-2021-25742](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25742)  


### GKE

Description | Severity  
---|---  
A security issue was discovered in the Kubernetes **ingress-nginx** controller, [CVE-2021-25742](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25742). Ingress-nginx custom snippets allows retrieval of ingress-nginx service account tokens and secrets across all namespaces. 

#### What should I do?

This security issue does **not** impact your GKE cluster infrastructure or any GKE Enterprise environments cluster infrastructure. If you use ingress-nginx in your workload deployments, you should be aware of this security issue. See [ ingress-nginx Issue 7837](https://github.com/kubernetes/ingress-nginx/issues/7837) for more details.  | None  
  
### GKE clusters on

Description | Severity  
---|---  
A security issue was discovered in the Kubernetes **ingress-nginx** controller, [CVE-2021-25742](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25742). Ingress-nginx custom snippets allows retrieval of ingress-nginx service account tokens and secrets across all namespaces. 

#### What should I do?

This security issue does **not** impact your GKE cluster infrastructure or any GKE Enterprise environments cluster infrastructure. If you use ingress-nginx in your workload deployments, you should be aware of this security issue. See [ ingress-nginx Issue 7837](https://github.com/kubernetes/ingress-nginx/issues/7837) for more details.  | None  
  
### GKE clusters on

Description | Severity  
---|---  
A security issue was discovered in the Kubernetes **ingress-nginx** controller, [CVE-2021-25742](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25742). Ingress-nginx custom snippets allows retrieval of ingress-nginx service account tokens and secrets across all namespaces. 

#### What should I do?

This security issue does **not** impact your GKE cluster infrastructure or any GKE Enterprise environments cluster infrastructure. If you use ingress-nginx in your workload deployments, you should be aware of this security issue. See [ ingress-nginx Issue 7837](https://github.com/kubernetes/ingress-nginx/issues/7837) for more details.  | None  
  
### GKE clusters on

Description | Severity  
---|---  
A security issue was discovered in the Kubernetes **ingress-nginx** controller, [CVE-2021-25742](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25742). Ingress-nginx custom snippets allows retrieval of ingress-nginx service account tokens and secrets across all namespaces. 

#### What should I do?

This security issue does **not** impact your GKE cluster infrastructure or any GKE Enterprise environments cluster infrastructure. If you use ingress-nginx in your workload deployments, you should be aware of this security issue. See [ ingress-nginx Issue 7837](https://github.com/kubernetes/ingress-nginx/issues/7837) for more details.  | None  
  
## GCP-2021-019

**Published:** 2021-09-29  


### GKE

Description | Severity  
---|---  
There is a known issue where updating a `BackendConfig` resource using the `v1beta1` API that removes an active Google Cloud Armor security policy from its service.

#### Am I impacted?

If your `BackendConfig` has already been updated with the `v1beta1` API, your Google Cloud Armor security policy might have been removed. To determine if this has happened, **run the following command** :
    
    
    kubectl get backendconfigs -A -o json | \
    jq -r '.items[] | select(.spec.securityPolicy == {}) | .metadata | "\(.namespace)/\(.name)"'

  * **If the response returns output:** your cluster is impacted by the issue. The output of this command returns a list of `BackendConfig` resources (<namespace>/<name>) that are affected by the issue. 
  * **If the output is empty:** your `BackendConfig` has not been updated using the `v1beta1` API since the issue has been introduced. _Any future updates to your`BackendConfig` should only use `v1`_.

This issue affects the following GKE versions:

  * 1.18.19-gke.1400 to 1.18.20-gke.5100 (exclusive)
  * 1.19.10-gke.700 to 1.19.14-gke.300 (exclusive)
  * 1.20.6-gke.700 to 1.20.9-gke.900 (exclusive)
  * 1.21 to 1.21.1-gke.2700 (exclusive)

If you do not configure Google Cloud Armor on your Ingress resources via the `BackendConfig`, then this issue does not affect your clusters.

####  What should I do?

[Upgrade your GKE control plane](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrading_the_cluster) to one of the following updated versions that patches this issue and allows `v1beta1` `BackendConfig` resources to be used safely:

  * 1.21.1-gke.2700 and later
  * 1.20.9-gke.900 and later
  * 1.19.14-gke.300 and later
  * 1.18.20-gke.5100 and later

This issue can also be prevented by avoiding the deployment of `v1beta1` `BackendConfig` resources. If you configure Google Cloud Armor on your Ingress resources via the `BackendConfig` and you've found that you're impacted through the steps above, re-enable Google Cloud Armor by pushing an update to your current `BackendConfig` resource with the **cloud.google.com/v1** API version. To prevent this issue, **only make updates to your`BackendConfig` using the `v1` BackendConfig API**. Since the `v1` `BackendConfig` supports all the same fields as **`v1beta1`** and makes no breaking changes, the API field can be updated transparently. To do so, **replace** the **apiVersion** field of any active BackendConfig manifest with **cloud.google.com/v1** and **do not use cloud.google.com/v1beta1**. The following sample manifest describes a `BackendConfig` resource that uses the `v1`API:
    
    
    apiVersion: cloud.google.com/v1
    kind: BackendConfig
    metadata:
      name: my-backend-config
    spec:
      securityPolicy:
        name: "ca-how-to-security-policy"
    

If you have CI/CD systems or tools which regularly update `BackendConfig` resources, **ensure that you are using the cloud.google.com/v1 API group in those systems** | Low  
  
## GCP-2021-022

**Published:** 2021-09-23  


### GKE clusters on

Description | Severity  
---|---  
A vulnerability has been discovered in the GKE Enterprise Identity Service (AIS) LDAP module of GKE on VMware versions 1.8 and 1.8.1 where a seed key used in generating keys is predictable. With this vulnerability, an authenticated user could add arbitrary claims and escalate privileges indefinitely. 

#### Technical details

A recent addition to AIS code creates symmetric keys using golang's math/rand module, which is not suitable for security-sensitive code. The module is used in a way that will generate a predictable key. During identity verification, a secure token service (STS) key is generated that is subsequently encrypted with a symmetric key that is simple to derive.

####  What should I do?

This vulnerability only affects customers using AIS in GKE on VMware versions 1.8 and 1.8.1. For users of GKE on VMware 1.8, upgrade your clusters to the following version:

  * 1.8.2

| High  
  
## GCP-2021-021

**Published:** 2021-09-22  
**Reference:**[CVE-2020-8561](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8561)  


### GKE

Description | Severity  
---|---  
A security vulnerability, [CVE-2020-8561](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8561), has been discovered in Kubernetes where certain webhooks can be made to redirect `kube-apiserver` requests to private networks of that API server.

#### Technical details

With this vulnerability, actors who control the responses of `MutatingWebhookConfiguration` or `ValidatingWebhookConfiguration` requests are able to redirect `kube-apiserver` requests to private networks of the API server. If that user can view `kube-apiserver` logs when the log level is set to `10`, they can view the redirected responses and headers in the logs. This issue can be mitigated by changing certain parameters for the API server.

####  What should I do?

No action is required at this time. Currently available versions of GKE and GKE Enterprise have implemented the following mitigations that protect against this type of attack:

  * The `--profiling` flag for `kube-apiserver` is set to `false`.
  * The `kube-apiserver` log level is set below `10`.



#### What vulnerability is addressed by this patch?

CVE-2020-8561  | Medium  
  
### GKE clusters on

Description | Severity  
---|---  
A security vulnerability, [CVE-2020-8561](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8561), has been discovered in Kubernetes where certain webhooks can be made to redirect `kube-apiserver` requests to private networks of that API server.

#### Technical details

With this vulnerability, actors who control the responses of `MutatingWebhookConfiguration` or `ValidatingWebhookConfiguration` requests are able to redirect `kube-apiserver` requests to private networks of the API server. If that user can view `kube-apiserver` logs when the log level is set to `10`, they can view the redirected responses and headers in the logs. This issue can be mitigated by changing certain parameters for the API server.

####  What should I do?

No action is required at this time. Currently available versions of GKE and GKE Enterprise have implemented the following mitigations that protect against this type of attack:

  * The `--profiling` flag for `kube-apiserver` is set to `false`.
  * The `kube-apiserver` log level is set below `10`.



#### What vulnerability is addressed by this patch?

CVE-2020-8561  | Medium  
  
### GKE clusters on

Description | Severity  
---|---  
A security vulnerability, [CVE-2020-8561](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8561), has been discovered in Kubernetes where certain webhooks can be made to redirect `kube-apiserver` requests to private networks of that API server.

#### Technical details

With this vulnerability, actors who control the responses of `MutatingWebhookConfiguration` or `ValidatingWebhookConfiguration` requests are able to redirect `kube-apiserver` requests to private networks of the API server. If that user can view `kube-apiserver` logs when the log level is set to `10`, they can view the redirected responses and headers in the logs. This issue can be mitigated by changing certain parameters for the API server.

####  What should I do?

No action is required at this time. Currently available versions of GKE and GKE Enterprise have implemented the following mitigations that protect against this type of attack:

  * The `--profiling` flag for `kube-apiserver` is set to `false`.
  * The `kube-apiserver` log level is set below `10`.



#### What vulnerability is addressed by this patch?

CVE-2020-8561  | Medium  
  
### GKE clusters on

Description | Severity  
---|---  
A security vulnerability, [CVE-2020-8561](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8561), has been discovered in Kubernetes where certain webhooks can be made to redirect `kube-apiserver` requests to private networks of that API server.

#### Technical details

With this vulnerability, actors who control the responses of `MutatingWebhookConfiguration` or `ValidatingWebhookConfiguration` requests are able to redirect `kube-apiserver` requests to private networks of the API server. If that user can view `kube-apiserver` logs when the log level is set to `10`, they can view the redirected responses and headers in the logs. This issue can be mitigated by changing certain parameters for the API server.

####  What should I do?

No action is required at this time. Currently available versions of GKE and GKE Enterprise have implemented the following mitigations that protect against this type of attack:

  * The `--profiling` flag for `kube-apiserver` is set to `false`.
  * The `kube-apiserver` log level is set below `10`.



#### What vulnerability is addressed by this patch?

CVE-2020-8561  | Medium  
  
## GCP-2021-018

**Published:** 2021-09-15  
**Updated:** 2021-09-24  
**Reference:**[CVE-2021-25741](https://nvd.nist.gov/vuln/detail/CVE-2021-25741)  


2021-09-24 update: GKE on Bare Metal bulletin updated with additional patched versions.

2021-09-20 update: Bulletins added for GKE on Bare Metal

2021-09-16 update: Bulletins added for GKE on VMware

* * *

### GKE

Description | Severity  
---|---  
A security issue was [discovered in Kubernetes](https://groups.google.com/g/kubernetes-announce/c/-e9OlTcED5E), CVE-2021-25741, where a user may be able to create a container with subpath volume mounts to access files & directories outside of the volume, including on the host filesystem.

#### Technical details:

In CVE-2021-25741, the attacker can create a symbolic link from a mounted emptyDir to the root filesystem of the node ( / ), the kubelet will follow the symlink and mount the host root into the container. 

####  What should I do?

We recommend you to upgrade your node pools to one of the following versions or above to take advantage of the latest patches: 

  * 1.21.4-gke.301
  * 1.20.10-gke.301
  * 1.19.14-gke.301
  * 1.18.20-gke.4501

The following versions also contain the fix:

  * 1.21.3-gke.2001
  * 1.20.8-gke.2101
  * 1.20.9-gke.701
  * 1.20.9-gke.1001
  * 1.19.12-gke.2101
  * 1.19.13-gke.701
  * 1.18.20-gke.3001

| High  
  
### GKE clusters on

Description | Severity  
---|---  
A security issue was [discovered in Kubernetes](https://groups.google.com/g/kubernetes-announce/c/-e9OlTcED5E), CVE-2021-25741, where a user may be able to create a container with subpath volume mounts to access files & directories outside of the volume, including on the host filesystem.

#### Technical details:

In CVE-2021-25741, the attacker can create a symbolic link from a mounted emptyDir to the root filesystem of the node ( / ), the kubelet will follow the symlink and mount the host root into the container. 

####  What should I do?

**Updated 2021-09-24:** Patched versions 1.8.3 and 1.7.4 are now available. **Updated 2021-09-17:** Corrected the list of available versions that contain the patch.

* * *

The following versions of GKE on VMware have been updated with code to fix this vulnerability. Upgrade your admin clusters and user clusters to one of the following versions:

  * 1.8.3
  * 1.8.2
  * 1.7.4
  * 1.6.5

| High  
  
### GKE clusters on

Description | Severity  
---|---  
A security issue was [discovered in Kubernetes](https://groups.google.com/g/kubernetes-announce/c/-e9OlTcED5E), CVE-2021-25741, where a user may be able to create a container with subpath volume mounts to access files & directories outside of the volume, including on the host filesystem.

#### Technical details:

In CVE-2021-25741, the attacker can create a symbolic link from a mounted emptyDir to the root filesystem of the node ( / ), the kubelet will follow the symlink and mount the host root into the container. 

####  What should I do?

2021-9-16 Update: Added list of supported gke-versions for `AWSCluster` and `AWSNodePool` objects.

* * *

The following versions of GKE on AWS have been updated with code to fix this vulnerability. It is recommended that you: 

  * [Upgrade](https://cloud.google.com/anthos/clusters/docs/aws/how-to/upgrading) your `AWSManagementService`, `AWSCluster` and `AWSNodePool` objects to the following version: 
    * 1.8.2
  * Update the gke-version of your `AWSCluster` and `AWSNodePool` objects to one of the [supported Kubernetes versions](https://cloud.google.com/anthos/clusters/docs/aws/release-notes#September_01_2021): 
    * 1.17.17-gke.15800
    * 1.18.20-gke.4800
    * 1.19.14-gke.600
    * 1.20.10-gke.600

| High  
  
### GKE clusters on

Description | Severity  
---|---  
A security issue was [discovered in Kubernetes](https://groups.google.com/g/kubernetes-announce/c/-e9OlTcED5E), CVE-2021-25741, where a user may be able to create a container with subpath volume mounts to access files & directories outside of the volume, including on the host filesystem.

#### Technical details:

In CVE-2021-25741, the attacker can create a symbolic link from a mounted emptyDir to the root filesystem of the node ( / ), the kubelet will follow the symlink and mount the host root into the container. 

####  What should I do?

The following versions of GKE on Bare Metal have been updated with code to fix this vulnerability. Upgrade your admin clusters and user clusters to one of the following versions:

  * 1.8.3
  * 1.7.4

| High  
  
## GCP-2021-017

**Published:** 2021-09-01  
**Updated:** 2021-09-23  
**Reference:**[CVE-2021-33909](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33909)  
[CVE-2021-33910](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33910)  


### GKE

Description | Severity  
---|---  
  
##### 2021-09-23 update:

Containers running inside of [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) are unaffected by this vulnerability for attacks originating inside the container.

* * *

#####  2021-09-15 update: 

The following GKE versions address the vulnerabilities: 

  * 1.18.20-gke.4100
  * 1.19.13-gke.1900
  * 1.20.9-gke.1500
  * 1.21.3-gke.1400



* * *

Two security vulnerabilities, [CVE-2021-33909](https://nvd.nist.gov/vuln/detail/CVE-2021-33909) and [CVE-2021-33910](https://nvd.nist.gov/vuln/detail/CVE-2021-33910), have been discovered in the Linux kernel that can lead to an OS crash or an escalation to root by an unprivileged user. This vulnerability affects all GKE node operating systems (COS and Ubuntu).

#### Technical details:

In [CVE-2021-33909](https://nvd.nist.gov/vuln/detail/CVE-2021-33909), the Linux kernel's filesystem layer does not properly restrict seq buffer allocations, leading to an integer overflow, an Out-of-bounds Write, and escalation to root.  
With [CVE-2021-33910](https://nvd.nist.gov/vuln/detail/CVE-2021-33910), systemd has a memory allocation with an excessive size value (involving `strdupa` and `alloca` for a pathname controlled by a local attacker) that results in an operating system crash.

####  What should I do?

The versions of Linux node images for the following versions of GKE have been updated with code to fix this vulnerability. Upgrade your clusters to one of the following versions:

  * 1.18.20-gke.4100
  * 1.19.13-gke.1900
  * 1.20.9-gke.1500
  * 1.21.3-gke.1400

| High  
  
### GKE clusters on

Description | Severity  
---|---  
Two security vulnerabilities, [CVE-2021-33909](https://nvd.nist.gov/vuln/detail/CVE-2021-33909) and [CVE-2021-33910](https://nvd.nist.gov/vuln/detail/CVE-2021-33910), have been discovered in the Linux kernel that can lead to an OS crash or an escalation to root by an unprivileged user. This vulnerability affects all GKE node operating systems (COS and Ubuntu).

#### Technical details:

In [CVE-2021-33909](https://nvd.nist.gov/vuln/detail/CVE-2021-33909), the Linux kernel's filesystem layer does not properly restrict seq buffer allocations, leading to an integer overflow, an Out-of-bounds Write, and escalation to root.  
With [CVE-2021-33910](https://nvd.nist.gov/vuln/detail/CVE-2021-33910), systemd has a memory allocation with an excessive size value (involving `strdupa` and `alloca` for a pathname controlled by a local attacker) that results in an operating system crash.

####  What should I do?

The versions of Linux node images for GKE on AWS have been updated with code to fix this vulnerability. Upgrade your clusters to one of the following versions:  


  * 1.20.10-gke.600 
  * 1.19.14-gke.600
  * 1.18.20-gke.4800
  * 1.17.17-gke.15800

| High  
  
### GKE clusters on

Description | Severity  
---|---  
Two security vulnerabilities, [CVE-2021-33909](https://nvd.nist.gov/vuln/detail/CVE-2021-33909) and [CVE-2021-33910](https://nvd.nist.gov/vuln/detail/CVE-2021-33910), have been discovered in the Linux kernel that can lead to an OS crash or an escalation to root by an unprivileged user. This vulnerability affects all GKE node operating systems (COS and Ubuntu).

#### Technical details:

In [CVE-2021-33909](https://nvd.nist.gov/vuln/detail/CVE-2021-33909), the Linux kernel's filesystem layer does not properly restrict seq buffer allocations, leading to an integer overflow, an Out-of-bounds Write, and escalation to root.  
With [CVE-2021-33910](https://nvd.nist.gov/vuln/detail/CVE-2021-33910), systemd has a memory allocation with an excessive size value (involving `strdupa` and `alloca` for a pathname controlled by a local attacker) that results in an operating system crash.

####  What should I do?

The versions of Linux and COS node images for GKE on VMware have been updated with code to fix this vulnerability. Upgrade your clusters to one of the following versions:  


  * 1.9
  * 1.8.2
  * 1.7.3
  * 1.6.4 (Linux only)

See [Version history--Kubernetes and node kernel versions](https://cloud.google.com/anthos/clusters/docs/on-prem/1.9/version-history#kubernetes-and-node-kernel-versions). | High  
  
## GCP-2021-015

**Published:** 2021-07-13  
**Updated:** 2021-07-15  
**Reference:**[CVE-2021-22555](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22555)  


### GKE

Description | Severity  
---|---  
A new security vulnerability, [CVE-2021-22555](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22555), has been discovered where a malicious actor with `CAP_NET_ADMIN` privileges can potentially cause a container breakout to root on the host. This vulnerability affects all GKE clusters and GKE on VMware running Linux version 2.6.19 or later.

#### Technical details

In this attack, an out-of-bounds write in `setsockopt` in the `netfilter` subsystem in Linux can allow a heap corruption (and therefore denial of service) and escalation of privileges. 

#### What should I do?

The following versions of Linux on GKE have been updated with code to fix this vulnerability. Upgrade your clusters to one of the following versions:

  * 1.21.1-gke.2200
  * 1.20.7-gke.2200
  * 1.19.11-gke.2100
  * 1.18.20-gke.501



#### What vulnerability is addressed by this patch?

[CVE-2021-22555](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22555) | High  
  
### GKE clusters on

Description | Severity  
---|---  
A new security vulnerability, [CVE-2021-22555](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22555), has been discovered where a malicious actor with `CAP_NET_ADMIN` privileges can potentially cause a container breakout to root on the host. This vulnerability affects all GKE clusters and GKE on VMware running Linux version 2.6.19 or later.

#### Technical details

In this attack, an out-of-bounds write in `setsockopt` in the `netfilter` subsystem in Linux can allow a heap corruption (and therefore denial of service) and escalation of privileges. 

#### What should I do?

The following versions of Linux on GKE on VMware have been updated with code to fix this vulnerability. Upgrade your clusters to one of the following versions:

  * 1.8
  * 1.7.3
  * 1.6.4



#### What vulnerability is addressed by this patch?

[CVE-2021-22555](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22555) | High  
  
## GCP-2021-014

**Published:** 2021-07-05  
**Reference:**[CVE-2021-34527](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-34527)  


### GKE

Description | Severity  
---|---  
Microsoft published a security bulletin on a Remote code execution (RCE) vulnerability, CVE-2021-34527, that affects the print spooler in Windows servers. The CERT Coordination Center (CERT/CC) published an update note on a related vulnerability, dubbed "PrintNightmare" that also affects Windows print spoolers - [PrintNightmare, Critical Windows Print Spooler Vulnerability](https://us-cert.cisa.gov/ncas/current-activity/2021/06/30/printnightmare-critical-windows-print-spooler-vulnerability)

####  What should I do?

No action is required. GKE Windows nodes do not contain the affected Spooler service as part of the base image, so GKE Windows deployments are not vulnerable to this attack.

#### What vulnerabilities are addressed by this bulletin?

  * [PrintNightmare](https://us-cert.cisa.gov/ncas/current-activity/2021/06/30/printnightmare-critical-windows-print-spooler-vulnerability)
  * [CVE-2021-34527](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-34527)

| High  
  
## GCP-2021-012

**Published:** 2021-07-01  
**Updated:** 2021-07-09  
**Reference:**[CVE-2021-34824](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-34824)  


### GKE

Description | Severity  
---|---  
  
####  What should I do?

The Istio project recently [disclosed](https://istio.io/latest/news/security/istio-security-2021-007/) a new security vulnerability ([CVE-2021-34824](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-34824)) affecting [Istio](https://cloud.google.com/learn/what-is-istio). Istio contains a remotely exploitable vulnerability where credentials specified in the Gateway and DestinationRule credentialName field can be accessed from different namespaces.

##### Technical details:

The [Istio secure Gateway](https://istio.io/latest/docs/tasks/traffic-management/ingress/secure-ingress/) or [workloads using the DestinationRule](https://istio.io/latest/docs/reference/config/networking/destination-rule/) can load TLS private keys and certificates from Kubernetes secrets via the credentialName configuration. From Istio 1.8 and above, the secrets are read from istiod and conveyed to gateways and workloads via XDS. Normally, a gateway or workload deployment is only able to access TLS certificates and private keys stored in the secret within its namespace. However, a bug in istiod allows a client authorized to access the Istio XDS API to retrieve any TLS certificate and private keys cached in istiod. 

##### What should I do?

GKE clusters do not run Istio by default and, when enabled, use Istio version 1.6, which is not vulnerable to this attack. If you have installed or upgraded Istio on the cluster to Istio 1.8 or above, upgrade your Istio to the latest supported version. | High  
  
### GKE clusters on

Description | Severity  
---|---  
  
####  What should I do?

The Istio project recently [disclosed](https://istio.io/latest/news/security/istio-security-2021-007/) a new security vulnerability ([CVE-2021-34824](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-34824)) affecting [Istio](https://cloud.google.com/learn/what-is-istio). Istio contains a remotely exploitable vulnerability where credentials specified in the Gateway and DestinationRule credentialName field can be accessed from different namespaces.

##### Technical details:

The [Istio secure Gateway](https://istio.io/latest/docs/tasks/traffic-management/ingress/secure-ingress/) or [workloads using the DestinationRule](https://istio.io/latest/docs/reference/config/networking/destination-rule/) can load TLS private keys and certificates from Kubernetes secrets via the credentialName configuration. From Istio 1.8 and above, the secrets are read from istiod and conveyed to gateways and workloads via XDS. Normally, a gateway or workload deployment is only able to access TLS certificates and private keys stored in the secret within its namespace. However, a bug in istiod allows a client authorized to access the Istio XDS API to retrieve any TLS certificate and private keys cached in istiod. 

##### What should I do?

Anthos clusters on VMware v1.6 and v1.7 are not vulnerable to this attack. Anthos clusters on VMware v1.8 are vulnerable.  If you are using Anthos clusters on VMware v1.8, upgrade to the following patched version or later:

  * 1.8.0-gke.25

| High  
  
### GKE clusters on

Description | Severity  
---|---  
  
####  What should I do?

The Istio project recently [disclosed](https://istio.io/latest/news/security/istio-security-2021-007/) a new security vulnerability ([CVE-2021-34824](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-34824)) affecting [Istio](https://cloud.google.com/learn/what-is-istio). Istio contains a remotely exploitable vulnerability where credentials specified in the Gateway and DestinationRule credentialName field can be accessed from different namespaces.

##### Technical details:

The [Istio secure Gateway](https://istio.io/latest/docs/tasks/traffic-management/ingress/secure-ingress/) or [workloads using the DestinationRule](https://istio.io/latest/docs/reference/config/networking/destination-rule/) can load TLS private keys and certificates from Kubernetes secrets via the credentialName configuration. From Istio 1.8 and above, the secrets are read from istiod and conveyed to gateways and workloads via XDS. Normally, a gateway or workload deployment is only able to access TLS certificates and private keys stored in the secret within its namespace. However, a bug in istiod allows a client authorized to access the Istio XDS API to retrieve any TLS certificate and private keys cached in istiod. Clusters created or upgraded with Anthos clusters on bare metal v1.8.0 are impacted by this CVE.

##### What should I do?

Anthos v1.6 and 1.7 are not vulnerable to this attack. If you have v1.8.0 clusters, download and install the 1.8.1 version of bmctl and upgrade your clusters to the following patched version:

  * 1.8.1

| High  
  
## GCP-2021-011

**Published:** 2021-06-04  
**Updated:** 2021-10-19  
**Reference:**[CVE-2021-30465](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30465)  


2021-10-19 update: Added bulletins for GKE on VMware, GKE on AWS, and GKE on Bare Metal.

### GKE

Description | Severity  
---|---  
The security community recently disclosed a new security vulnerability ([CVE-2021-30465](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30465)) found in `runc` that has the potential to allow full access to a node filesystem. For GKE, because exploiting this vulnerability requires the ability to create pods, we have rated the severity of this vulnerability at MEDIUM.

#### Technical details

The `runc` package is vulnerable to a symlink exchange attack when mounting a volume.  For this specific attack, a user can potentially exploit a race condition by starting multiple pods on a single node simultaneously, all of which share the same volume mount with a symlink.  If the attack succeeds, one of the pods will mount the node's filesystem with root permissions. 

#### What should I do?

There is a newly released patch to `runc` (1.0.0-rc95) that fixes this vulnerability. Upgrade your GKE cluster to one of the following updated versions:

  * 1.18.19-gke.2100
  * 1.19.9-gke.1400
  * 1.20.6-gke.1400
  * 1.21.2-gke.600

|  Medium  
  
### GKE clusters on

Description | Severity  
---|---  
The security community recently disclosed a new security vulnerability ([CVE-2021-30465](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30465)) found in `runc` that has the potential to allow full access to a node filesystem. For GKE on VMware, because exploiting this vulnerability requires the ability to create pods, we have rated the severity of this vulnerability at MEDIUM.

#### Technical details

The `runc` package is vulnerable to a symlink exchange attack when mounting a volume.  For this specific attack, a user can potentially exploit a race condition by starting multiple pods on a single node simultaneously, all of which share the same volume mount with a symlink.  If the attack succeeds, one of the pods will mount the node's filesystem with root permissions. 

#### What should I do?

There is a newly released patch to `runc` that fixes this vulnerability. Upgrade your GKE on VMware to one of the following versions: 

  * 1.7.3-gke-2
  * 1.8.1-gke.7
  * 1.9.0-gke.8

|  Medium  
  
### GKE clusters on

Description | Severity  
---|---  
The security community recently disclosed a new security vulnerability ([CVE-2021-30465](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30465)) found in `runc` that has the potential to allow full access to a node filesystem. Because this is an OS-level vulnerability, GKE on AWS are not vulnerable.

#### Technical details

The `runc` package is vulnerable to a symlink exchange attack when mounting a volume.  For this specific attack, a user can potentially exploit a race condition by starting multiple pods on a single node simultaneously, all of which share the same volume mount with a symlink.  If the attack succeeds, one of the pods will mount the node's filesystem with root permissions. 

#### What should I do?

Ensure that the OS version on which you are running GKE on AWS is upgraded to the latest OS version that has an updated `runc` package.  |  None  
  
### GKE clusters on

Description | Severity  
---|---  
The security community recently disclosed a new security vulnerability ([CVE-2021-30465](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30465)) found in `runc` that has the potential to allow full access to a node filesystem. Because this is an OS-level vulnerability, GKE on Bare Metal are not vulnerable.

#### Technical details

The `runc` package is vulnerable to a symlink exchange attack when mounting a volume.  For this specific attack, a user can potentially exploit a race condition by starting multiple pods on a single node simultaneously, all of which share the same volume mount with a symlink.  If the attack succeeds, one of the pods will mount the node's filesystem with root permissions. 

#### What should I do?

Ensure that the OS version on which you are running Google Distributed Cloud Virtual for Bare Metal is upgraded to the latest OS version that has an updated `runc` package.  |  None  
  
## GCP-2021-006

**Published:** 2021-05-11  
**Reference:**[CVE-2021-31920](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-31920)  


### GKE

Description | Severity  
---|---  
The Istio project recently [disclosed](https://istio.io/latest/news/security/) a new security vulnerability ([CVE-2021-31920](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-31920)) affecting [Istio](https://cloud.google.com/learn/what-is-istio). Istio contains a remotely-exploitable vulnerability where an HTTP request with multiple slashes or escaped slash characters can bypass Istio authorization policy when path based authorization rules are used.

#### What should I do?

We strongly recommend that you update and reconfigure your GKE clusters. Please note it is important to complete both steps below to successfully resolve the vulnerability:

  1. **Update your clusters:** Please complete the following instructions to upgrade your clusters to the newest patch versions as soon as possible: 
     * **If you are using Istio on GKE 1.6:** The newest patch release version is 1.6.14-gke.3. Please follow the [upgrade instructions](https://docs.cloud.google.com/istio/docs/istio-on-gke/upgrading#operator) to upgrade your clusters to the newest version.
     * **If you are using Istio on GKE 1.4:**
Istio on GKE 1.4 releases are no longer supported by Istio and we **do not** backport CVE fixes to these versions. Please follow the [Istio upgrade instructions](https://docs.cloud.google.com/istio/docs/istio-on-gke/upgrade-with-operator) to upgrade your clusters to 1.6, then follow the above instructions to get the newest version of Istio on GKE 1.6.
  2. **Configure Istio:** Once your clusters are patched, you must reconfigure Istio on GKE. Please refer to the [security best practices guide](https://istio.io/latest/docs/ops/best-practices/security/#authorization-policies) to correctly configure your system. 

| High  
  
## GCP-2021-004

**Published:** 2021-05-06  
**Reference:**[CVE-2021-28683](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-28683), [CVE-2021-28682](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-28682), [CVE-2021-29258](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-29258)  


### GKE

Description | Severity  
---|---  
The Envoy and Istio projects recently [announced](https://istio.io/latest/news/security/istio-security-2021-003/) several new security vulnerabilities ([CVE-2021-28683](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-28683), [CVE-2021-28682](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-28682) and [CVE-2021-29258](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-29258)), that could allow an attacker to crash Envoy. GKE clusters do not run Istio by default and are not vulnerable. If Istio has been installed in a cluster and configured to expose services to the internet, those services may be vulnerable to denial of service.

#### What should I do?

To fix these vulnerabilities, [upgrade your GKE control plane](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrading_the_cluster) to one of the following patched versions: 

  * 1.16.15-gke.16200
  * 1.17.17-gke.6100
  * 1.18.17-gke.1300
  * 1.19.9-gke.1300
  * 1.20.5-gke.1400

| Medium  
  
### GKE clusters on

Description | Severity  
---|---  
The Envoy and Istio projects recently [announced](https://istio.io/latest/news/security/istio-security-2021-003/) several new security vulnerabilities ([CVE-2021-28683](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-28683), [CVE-2021-28682](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-28682) and [CVE-2021-29258](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-29258)), that could allow an attacker to crash Envoy. GKE on VMware use Envoy by default for Ingress, so Ingress services may be vulnerable to denial of service.

#### What should I do?

To fix these vulnerabilities, upgrade your GKE on VMware to one of the following patched versions when released: 

  * 1.5.4
  * 1.6.3
  * 1.7.1

| Medium  
  
### GKE clusters on

**Updated:** 2021-05-06

Description | Severity  
---|---  
The Envoy and Istio projects recently [announced](https://istio.io/latest/news/security/istio-security-2021-003/) several new security vulnerabilities ([CVE-2021-28683](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-28683), [CVE-2021-28682](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-28682) and [CVE-2021-29258](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-29258)), that could allow an attacker to crash Envoy. Google Distributed Cloud Virtual for Bare Metal uses Envoy by default for Ingress, so Ingress services may be vulnerable to denial of service.

#### What should I do?

To fix these vulnerabilities, upgrade your Google Distributed Cloud Virtual for Bare Metal cluster to one of the following patched versions when released:

  * 1.6.3
  * 1.7.1

| Medium  
  
## GCP-2021-003

**Published:** 2021-04-19  
**Reference:**[CVE-2021-25735](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25735)  


### GKE

Description | Severity  
---|---  
The Kubernetes project recently [ announced](https://groups.google.com/g/kubernetes-security-announce/c/FKAGqT4jx9Y) a new security vulnerability, [ CVE-2021-25735](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25735), that could allow node updates to bypass a Validating Admission Webhook. In a scenario where an attacker has sufficient privileges and where a Validating Admission Webhook is implemented that uses old `Node` object properties (for example fields in `Node.NodeSpec`), the attacker could update properties of a node that could lead to a cluster compromise. None of the policies enforced by GKE and Kubernetes built-in admission controllers are affected, but we recommend customers check any additional admission webhooks they have installed.

#### What should I do?

To fix this vulnerability, upgrade your GKE cluster to one of the following patched versions: 

  * 1.18.17-gke.900
  * 1.19.9-gke.900
  * 1.20.5-gke.900

| Medium  
  
### GKE clusters on

Description | Severity  
---|---  
The Kubernetes project recently [ announced](https://groups.google.com/g/kubernetes-security-announce/c/FKAGqT4jx9Y) a new security vulnerability, [ CVE-2021-25735](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25735), that could allow node updates to bypass a Validating Admission Webhook. In a scenario where an attacker has sufficient privileges and where a Validating Admission Webhook is implemented that uses old `Node` object properties (for example fields in `Node.NodeSpec`), the attacker could update properties of a node that could lead to a cluster compromise. None of the policies enforced by GKE and Kubernetes built-in admission controllers are affected, but we recommend customers check any additional admission webhooks they have installed.

#### What should I do?

An upcoming patch version will include a mitigation for this vulnerability. | Medium  
  
### GKE clusters on

Description | Severity  
---|---  
The Kubernetes project recently [ announced](https://groups.google.com/g/kubernetes-security-announce/c/FKAGqT4jx9Y) a new security vulnerability, [ CVE-2021-25735](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25735), that could allow node updates to bypass a Validating Admission Webhook. In a scenario where an attacker has sufficient privileges and where a Validating Admission Webhook is implemented that uses old `Node` object properties (for example fields in `Node.NodeSpec`), the attacker could update properties of a node that could lead to a cluster compromise. None of the policies enforced by GKE and Kubernetes built-in admission controllers are affected, but we recommend customers check any additional admission webhooks they have installed.

#### What should I do?

An upcoming patch version will include a mitigation for this vulnerability. | Medium  
  
### GKE clusters on

Description | Severity  
---|---  
The Kubernetes project recently [ announced](https://groups.google.com/g/kubernetes-security-announce/c/FKAGqT4jx9Y) a new security vulnerability, [ CVE-2021-25735](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25735), that could allow node updates to bypass a Validating Admission Webhook. In a scenario where an attacker has sufficient privileges and where a Validating Admission Webhook is implemented that uses old `Node` object properties (for example fields in `Node.NodeSpec`), the attacker could update properties of a node that could lead to a cluster compromise. None of the policies enforced by GKE and Kubernetes built-in admission controllers are affected, but we recommend customers check any additional admission webhooks they have installed.

#### What should I do?

An upcoming patch version will include a mitigation for this vulnerability. | Medium  
  
## GCP-2021-001

**Published:** 2021-01-28  
**Reference:**[CVE-2021-3156](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3156)  


### GKE

Description | Severity  
---|---  
A vulnerability was recently discovered in the Linux utility `sudo`, described in [CVE-2021-3156](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2021-3156), that may allow an attacker with unprivileged local shell access on a system with `sudo` installed to escalate their privileges to root on the system. Google Kubernetes Engine (GKE) clusters are not affected by this vulnerability:

  * Users who are authorized to SSH to GKE nodes are already considered highly privileged and can use `sudo` to obtain root privileges by design. The vulnerability does not yield any additional privilege escalation paths in this scenario.
  * Most GKE system containers are built from [distroless base images](https://github.com/GoogleContainerTools/distroless) which do not have a shell or `sudo` installed. Other images are built from a debian base image that doesn't contain `sudo`. Even if `sudo` was present, access to `sudo` inside the container does not give you access to the host due to the container boundary.



#### What should I do?

Because GKE clusters are not affected by this vulnerability, no further action is required. GKE will have the patch for this vulnerability applied in a coming release at regular cadence. | None  
  
### GKE clusters on

Description | Severity  
---|---  
A vulnerability was recently discovered in the Linux utility `sudo`, described in [CVE-2021-3156](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2021-3156), that may allow an attacker with unprivileged local shell access on a system with `sudo` installed to escalate their privileges to root on the system. GKE on VMware are not affected by this vulnerability:

  * Users who are authorized to SSH to GKE on VMware nodes are already considered highly privileged and can use `sudo` to obtain root privileges by design. The vulnerability does not yield any additional privilege escalation paths in this scenario.
  * Most GKE on VMware system containers are built from [distroless base images](https://github.com/GoogleContainerTools/distroless) which do not have a shell or `sudo` installed. Other images are built from a debian base image that doesn't contain `sudo`. Even if `sudo` was present, access to `sudo` inside the container does not give you access to the host due to the container boundary.



#### What should I do?

Because GKE on VMware clusters are not affected by this vulnerability, no further action is required. GKE on VMware will have the patch for this vulnerability applied in a coming release at regular cadence. | None  
  
### GKE clusters on

Description | Severity  
---|---  
A vulnerability was recently discovered in the Linux utility `sudo`, described in [CVE-2021-3156](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2021-3156), that may allow an attacker with unprivileged local shell access on a system with `sudo` installed to escalate their privileges to root on the system. GKE on AWS are not affected by this vulnerability:

  * Users who are authorized to SSH to GKE on AWS nodes are already considered highly privileged and can use `sudo` to obtain root privileges by design. The vulnerability does not yield any additional privilege escalation paths in this scenario.
  * Most GKE on AWS system containers are built from [distroless base images](https://github.com/GoogleContainerTools/distroless) which do not have a shell or `sudo` installed. Other images are built from a debian base image that doesn't contain `sudo`. Even if `sudo` was present, access to `sudo` inside the container does not give you access to the host due to the container boundary.



#### What should I do?

Because GKE on AWS clusters are not affected by this vulnerability, no further action is required. GKE on AWS will have the patch for this vulnerability applied in a coming release at regular cadence. | None  
  
### GKE clusters on

Description | Severity  
---|---  
A vulnerability was recently discovered in the Linux utility `sudo`, described in [CVE-2021-3156](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2021-3156), that may allow an attacker with unprivileged local shell access on a system with `sudo` installed to escalate their privileges to root on the system. Google Distributed Cloud Virtual for Bare Metal clusters are not affected by this vulnerability:

  * Users who are authorized to SSH to Google Distributed Cloud Virtual for Bare Metal nodes are already considered highly privileged and can use `sudo` to obtain root privileges by design. The vulnerability does not yield any additional privilege escalation paths in this scenario.
  * Most Google Distributed Cloud Virtual for Bare Metal system containers are built from [distroless base images](https://github.com/GoogleContainerTools/distroless) which do not have a shell or `sudo` installed. Other images are built from a debian base image that doesn't contain `sudo`. Even if `sudo` was present, access to `sudo` inside the container does not give you access to the host due to the container boundary.



#### What should I do?

Because Google Distributed Cloud Virtual for Bare Metal clusters are not affected by this vulnerability, no further action is required. Google Distributed Cloud Virtual for Bare Metal will have the patch for this vulnerability applied in a coming release at regular cadence. | None  
  
## GCP-2020-015

**Published:** 2020-12-07  
**Updated:** 2021-12-22  
**Reference:**[CVE-2020-8554](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8554)  


2021-12-22 update: Uses `gcloud beta` instead of the `gcloud` command. 

2021-12-15 update: Added additional mitigate for GKE. 

### GKE

Description | Severity  
---|---  
**Updated: 2021-12-22** The command for GKE in the following section should use `gcloud beta` instead of the `gcloud` command. 
    
    
    gcloud beta container clusters update –no-enable-service-externalips
    

* * *

**Updated: 2021-12-15** For GKE, the following mitigation is now available: 

  1. Starting in GKE version 1.21, services with ExternalIPs are blocked by a `DenyServiceExternalIPs` admission controller that is enabled by default for new clusters. 
  2. Customers who upgrade to GKE version 1.21 can block services with ExternalIPs using the following command: 
         
         gcloud container clusters update –no-enable-service-externalips
         


For more information, see [ Hardening your cluster's security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#deny_external_IPs). 

* * *

The Kubernetes project [recently discovered](https://groups.google.com/g/kubernetes-announce/c/GPpZzVtGwiI) a new security vulnerability, [CVE-2020-8554](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8554), that might allow an attacker who has obtained permissions to create a Kubernetes Service of type LoadBalancer or ClusterIP to intercept network traffic originating from other Pods in the cluster. This vulnerability by itself does not give an attacker permissions to create a Kubernetes Service.  All Google Kubernetes Engine (GKE) clusters are affected by this vulnerability.

#### What should I do?

Kubernetes might need to make backwards incompatible design changes in a future version to address the vulnerability. If many users share access to your cluster with permissions to create Services, such as in a multi-tenant cluster, consider applying a mitigation in the meantime. For now, the best approach for mitigation is to restrict the use of ExternalIPs in a cluster. ExternalIPs are not a commonly used feature. Restrict the use of ExternalIPs in a cluster with **one** of the following methods:

  1. Use GKE Enterprise Policy Controller or Gatekeeper with this [constraint template](https://github.com/open-policy-agent/gatekeeper-library/tree/master/library/general/externalip) and apply it. For example: 
         
         # Only allow the creation of Services with no
         # ExternalIP or an ExternalIP of 203.0.113.1:
         
         apiVersion: constraints.gatekeeper.sh/v1beta1
         kind: K8sExternalIPs
         metadata:
           name: external-ips
         spec:
           match:
             kinds:
               - apiGroups: [""]
                 kinds: ["Service"]
           parameters:
             allowedIPs:
               - "203.0.113.1"
         

  2. **Or** install an admission controller to prevent the use of ExternalIPs. The Kubernetes project has provided a [sample admission controller](https://github.com/kubernetes-sigs/externalip-webhook) for this task.

As mentioned in the [Kubernetes announcement](https://groups.google.com/g/kubernetes-announce/c/GPpZzVtGwiI), no mitigation is provided for Services of type LoadBalancer because, by default, only highly privileged users and system components are granted the `container.services.updateStatus` [permission](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.services.updateStatus) which is required to leverage this vulnerability. | Medium  
  
### GKE clusters on

Description | Severity  
---|---  
**Updated: 2021-12-22** The command for GKE in the following section should use `gcloud beta` instead of the `gcloud` command. 
    
    
    gcloud beta container clusters update –no-enable-service-externalips
    

* * *

**Updated: 2021-12-15** For GKE, the following mitigation is now available: 

  1. Starting in GKE version 1.21, services with ExternalIPs are blocked by a `DenyServiceExternalIPs` admission controller that is enabled by default for new clusters. 
  2. Customers who upgrade to GKE version 1.21 can block services with ExternalIPs using the following command: 
         
         gcloud container clusters update –no-enable-service-externalips
         


For more information, see [ Hardening your cluster's security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#deny_external_IPs). 

* * *

The Kubernetes project [recently discovered](https://groups.google.com/g/kubernetes-announce/c/GPpZzVtGwiI) a new security vulnerability, [CVE-2020-8554](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8554), that might allow an attacker who has obtained permissions to create a Kubernetes Service of type LoadBalancer or ClusterIP to intercept network traffic originating from other Pods in the cluster. This vulnerability by itself does not give an attacker permissions to create a Kubernetes Service.  All GKE on VMware are affected by this vulnerability.

#### What should I do?

Kubernetes might need to make backwards incompatible design changes in a future version to address the vulnerability. If many users share access to your cluster with permissions to create Services, such as in a multi-tenant cluster, consider applying a mitigation in the meantime. For now, the best approach for mitigation is to restrict the use of ExternalIPs in a cluster. ExternalIPs are not a commonly used feature. Restrict the use of ExternalIPs in a cluster with **one** of the following methods:

  1. Use GKE Enterprise Policy Controller or Gatekeeper with this [constraint template](https://github.com/open-policy-agent/gatekeeper-library/tree/master/library/general/externalip) and apply it. For example: 
         
         # Only allow the creation of Services with no
         # ExternalIP or an ExternalIP of 203.0.113.1:
         
         apiVersion: constraints.gatekeeper.sh/v1beta1
         kind: K8sExternalIPs
         metadata:
           name: external-ips
         spec:
           match:
             kinds:
               - apiGroups: [""]
                 kinds: ["Service"]
           parameters:
             allowedIPs:
               - "203.0.113.1"
         

  2. **Or** install an admission controller to prevent the use of ExternalIPs. The Kubernetes project has provided a [sample admission controller](https://github.com/kubernetes-sigs/externalip-webhook) for this task.

As mentioned in the [Kubernetes announcement](https://groups.google.com/g/kubernetes-announce/c/GPpZzVtGwiI), no mitigation is provided for Services of type LoadBalancer because, by default, only highly privileged users and system components are granted the `container.services.updateStatus` [permission](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.services.updateStatus) which is required to leverage this vulnerability. | Medium  
  
### GKE clusters on

Description | Severity  
---|---  
**Updated: 2021-12-22** The command for GKE in the following section should use `gcloud beta` instead of the `gcloud` command. 
    
    
    gcloud beta container clusters update –no-enable-service-externalips
    

* * *

**Updated: 2021-12-15** For GKE, the following mitigation is now available: 

  1. Starting in GKE version 1.21, services with ExternalIPs are blocked by a `DenyServiceExternalIPs` admission controller that is enabled by default for new clusters. 
  2. Customers who upgrade to GKE version 1.21 can block services with ExternalIPs using the following command: 
         
         gcloud container clusters update –no-enable-service-externalips
         


For more information, see [ Hardening your cluster's security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#deny_external_IPs). 

* * *

The Kubernetes project [recently discovered](https://groups.google.com/g/kubernetes-announce/c/GPpZzVtGwiI) a new security vulnerability, [CVE-2020-8554](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8554), that might allow an attacker who has obtained permissions to create a Kubernetes Service of type LoadBalancer or ClusterIP to intercept network traffic originating from other Pods in the cluster. This vulnerability by itself does not give an attacker permissions to create a Kubernetes Service.  All GKE on AWS are affected by this vulnerability.

#### What should I do?

Kubernetes might need to make backwards incompatible design changes in a future version to address the vulnerability. If many users share access to your cluster with permissions to create Services, such as in a multi-tenant cluster, consider applying a mitigation in the meantime. For now, the best approach for mitigation is to restrict the use of ExternalIPs in a cluster. ExternalIPs are not a commonly used feature. Restrict the use of ExternalIPs in a cluster with **one** of the following methods:

  1. Use GKE Enterprise Policy Controller or Gatekeeper with this [constraint template](https://github.com/open-policy-agent/gatekeeper-library/tree/master/library/general/externalip) and apply it. For example: 
         
         # Only allow the creation of Services with no
         # ExternalIP or an ExternalIP of 203.0.113.1:
         
         apiVersion: constraints.gatekeeper.sh/v1beta1
         kind: K8sExternalIPs
         metadata:
           name: external-ips
         spec:
           match:
             kinds:
               - apiGroups: [""]
                 kinds: ["Service"]
           parameters:
             allowedIPs:
               - "203.0.113.1"
         

  2. **Or** install an admission controller to prevent the use of ExternalIPs. The Kubernetes project has provided a [sample admission controller](https://github.com/kubernetes-sigs/externalip-webhook) for this task.

As mentioned in the [Kubernetes announcement](https://groups.google.com/g/kubernetes-announce/c/GPpZzVtGwiI), no mitigation is provided for Services of type LoadBalancer because, by default, only highly privileged users and system components are granted the `container.services.updateStatus` [permission](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.services.updateStatus) which is required to leverage this vulnerability. | Medium  
  
## GCP-2020-014

**Published:** 2020-10-20  
**Reference:** [CVE-2020-8563](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8563), [CVE-2020-8564](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8564), [CVE-2020-8565](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8565), [CVE-2020-8566](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8566)  


### GKE

**Updated:** 2020-10-20

Description | Severity  
---|---  
The Kubernetes project recently discovered [several issues](https://groups.google.com/forum/#!topic/kubernetes-announce/ScdmyORnPDk) that allow for the exposure of secret data when verbose logging options are enabled. The issues are:

  * CVE-2020-8563: Secret leaks in logs for vSphere Provider kube-controller-manager
  * CVE-2020-8564: Docker config secrets leaked when file is malformed and loglevel >= 4
  * CVE-2020-8565: Incomplete fix for CVE-2019-11250 in Kubernetes allows for token leak in logs when logLevel >= 9. Discovered by GKE Security.
  * CVE-2020-8566: Ceph RBD adminSecrets exposed in logs when loglevel >= 4

GKE is not affected.

#### What should I do?

No further action is required due to the default verbosity logging levels of GKE. | None  
  
### GKE clusters on

**Updated:** 2020-10-10

Description | Severity  
---|---  
The Kubernetes project recently discovered [several issues](https://groups.google.com/forum/#!topic/kubernetes-announce/ScdmyORnPDk) that allow for the exposure of secret data when verbose logging options are enabled. The issues are:

  * CVE-2020-8563: Secret leaks in logs for vSphere Provider kube-controller-manager
  * CVE-2020-8564: Docker config secrets leaked when file is malformed and loglevel >= 4
  * CVE-2020-8565: Incomplete fix for CVE-2019-11250 in Kubernetes allows for token leak in logs when logLevel >= 9. Discovered by GKE Security.
  * CVE-2020-8566: Ceph RBD adminSecrets exposed in logs when loglevel >= 4

GKE on VMware is not affected.

#### What should I do?

No further action is required due to the default verbosity logging levels of GKE. | None  
  
### GKE clusters on

**Updated:** 2020-10-20

Description | Severity  
---|---  
The Kubernetes project recently discovered [several issues](https://groups.google.com/forum/#!topic/kubernetes-announce/ScdmyORnPDk) that allow for the exposure of secret data when verbose logging options are enabled. The issues are:

  * CVE-2020-8563: Secret leaks in logs for vSphere Provider kube-controller-manager
  * CVE-2020-8564: Docker config secrets leaked when file is malformed and loglevel >= 4
  * CVE-2020-8565: Incomplete fix for CVE-2019-11250 in Kubernetes allows for token leak in logs when logLevel >= 9. Discovered by GKE Security.
  * CVE-2020-8566: Ceph RBD adminSecrets exposed in logs when loglevel >= 4

GKE on AWS is not affected.

#### What should I do?

No further action is required due to the default verbosity logging levels of GKE. | None  
  
## GCP-2020-012

**Published:** 2020-09-14  
**Reference:**[CVE-2020-14386](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14386)  


### GKE

Description | Severity  
---|---  
A vulnerability was recently discovered in the Linux kernel, described in [CVE-2020-14386](https://www.openwall.com/lists/oss-security/2020/09/03/3), that may allow container escape to obtain root privileges on the host node. All GKE nodes are affected. Pods running in [GKE Sandbox](https://cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) are not able to leverage this vulnerability.

#### What should I do?

To fix this vulnerability, [upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) your control plane, and then your nodes to one of the patched versions listed below:

  * 1.14.10-gke.50   
**Note:** 1.14 is at the end of its support lifecycle. We recommend upgrading to 1.15 if possible. 
  * 1.15.12-gke.20
  * 1.16.13-gke.401
  * 1.17.9-gke.1504
  * 1.18.6-gke.3504

Exploiting this vulnerability requires `CAP_NET_RAW`, but very few containers typically require `CAP_NET_RAW`. This and other powerful capabilities should be blocked by default through `PodSecurityPolicy` or Policy Controller: Drop the `CAP_NET_RAW` capability from containers with one of the following methods:

  * Enforce blocking these capabilities with [`PodSecurityPolicy`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies), for example: 
        
        # Require dropping CAP_NET_RAW with a PSP
            apiversion: extensions/v1beta1
            kind: PodSecurityPolicy
            metadata:
              name: no-cap-net-raw
            spec:
              requiredDropCapabilities:
                -NET_RAW
                 ...
                 # Unrelated fields omitted

  * Or by using Policy Controller or Gatekeeper with this [constraint template](https://github.com/open-policy-agent/gatekeeper-library/blob/master/library/pod-security-policy/capabilities/template.yaml) and applying it, for example: 
        
        # Dropping CAP_NET_RAW with Gatekeeper
            # (requires the K8sPSPCapabilities template)
            apiversion: constraints.gatekeeper.sh/v1beta1
            kind:  K8sPSPCapabilities
            metadata:
              name: forbid-cap-net-raw
            spec:
              match:
                kinds:
                  - apiGroups: [""]
                  kinds: ["Pod"]
                namespaces:
                  #List of namespaces to enforce this constraint on
                  - default
                # If running gatekeeper >= v3.1.0-beta.5,
                # you can exclude namespaces rather than including them above.
                excludedNamespaces:
                  - kube-system
              parameters:
                requiredDropCapabilities:
                  - "NET_RAW"

  * Or by updating your Pod specs: 
        
        # Dropping CAP_NET_RAW from a Pod:
            apiVersion: v1
            kind: Pod
            metadata:
              name: no-cap-net-raw
            spec:
              containers:
                -name: my-container
                 ...
                securityContext:
                  capabilities:
                    drop:
                      -NET_RAW


**Note:** GKE Sandbox pods already disable `CAP_NET_RAW` by default and do not require the changes above.

#### What vulnerability is addressed by this patch?

The patch mitigates the following vulnerability: The vulnerability [CVE-2020-14386](https://www.openwall.com/lists/oss-security/2020/09/03/3), which allows containers with `CAP_NET_RAW` to write 1 to 10 bytes of kernel memory, and possibly escape the container and obtain root privileges on the host node. This is rated as a High severity vulnerability. | High  
  
### GKE clusters on

**Updated:** 2020-09-17

Description | Severity  
---|---  
A vulnerability was recently discovered in the Linux kernel, described in [CVE-2020-14386](https://www.openwall.com/lists/oss-security/2020/09/03/3), that may allow container escape to obtain root privileges on the host node. All GKE on VMware nodes are affected.

#### What should I do?

To fix this vulnerability, [upgrade](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/how-to/upgrading) your cluster to a patched version. The following upcoming {gke_on_prem_name}} versions will contain the fix for this vulnerability, and this bulletin will be updated when they are available:

  * GKE on VMware 1.4.3, now available.
  * GKE on VMware 1.3.4, now available.

Exploiting this vulnerability requires `CAP_NET_RAW`, but very few containers typically require `CAP_NET_RAW`. This and other powerful capabilities should be blocked by default through `PodSecurityPolicy` or Policy Controller: Drop the `CAP_NET_RAW` capability from containers with one of the following methods:

  * Enforce blocking these capabilities with [`PodSecurityPolicy`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies), for example: 
        
        # Require dropping CAP_NET_RAW with a PSP
            apiversion: extensions/v1beta1
            kind: PodSecurityPolicy
            metadata:
              name: no-cap-net-raw
            spec:
              requiredDropCapabilities:
                -NET_RAW
                 ...
                 # Unrelated fields omitted

  * Or by using Policy Controller or Gatekeeper with this [constraint template](https://github.com/open-policy-agent/gatekeeper-library/blob/master/library/pod-security-policy/capabilities/template.yaml) and applying it, for example: 
        
        # Dropping CAP_NET_RAW with Gatekeeper
            # (requires the K8sPSPCapabilities template)
            apiversion: constraints.gatekeeper.sh/v1beta1
            kind:  K8sPSPCapabilities
            metadata:
              name: forbid-cap-net-raw
            spec:
              match:
                kinds:
                  - apiGroups: [""]
                  kinds: ["Pod"]
                namespaces:
                  #List of namespaces to enforce this constraint on
                  - default
                # If running gatekeeper >= v3.1.0-beta.5,
                # you can exclude namespaces rather than including them above.
                excludedNamespaces:
                  - kube-system
              parameters:
                requiredDropCapabilities:
                  - "NET_RAW"

  * Or by updating your Pod specs: 
        
        # Dropping CAP_NET_RAW from a Pod:
            apiVersion: v1
            kind: Pod
            metadata:
              name: no-cap-net-raw
            spec:
              containers:
                -name: my-container
                 ...
                securityContext:
                  capabilities:
                    drop:
                      -NET_RAW


**Note:** GKE Sandbox pods already disable `CAP_NET_RAW` by default and do not require the changes above.

#### What vulnerability is addressed by this patch?

The patch mitigates the following vulnerability: The vulnerability [CVE-2020-14386](https://www.openwall.com/lists/oss-security/2020/09/03/3), which allows containers with `CAP_NET_RAW` to write 1 to 10 bytes of kernel memory, and possibly escape the container and obtain root privileges on the host node. This is rated as a High severity vulnerability. | High  
  
### GKE clusters on

**Updated:** 2020-10-13

Description | Severity  
---|---  
A vulnerability was recently discovered in the Linux kernel, described in [CVE-2020-14386](https://www.openwall.com/lists/oss-security/2020/09/03/3), that may allow container escape to obtain root privileges on the host node. All GKE on AWS nodes are affected. 

#### What should I do?

To fix this vulnerability, upgrade your [management service](https://docs.cloud.google.com/anthos/clusters/docs/aws/how-to/upgrading-management) and your [user clusters](https://docs.cloud.google.com/anthos/clusters/docs/aws/how-to/upgrading-user-cluster) to a patched version. The following upcoming GKE on AWS versions or newer will include the fix for this vulnerability, and this bulletin will be updated when they are available:

  * 1.5.0-gke.6
  * 1.4.3-gke.7

Drop the `CAP_NET_RAW` capability from containers with one of the following methods:

  * Enforce blocking these capabilities with [`PodSecurityPolicy`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies), for example: 
        
        # Require dropping CAP_NET_RAW with a PSP
            apiversion: extensions/v1beta1
            kind: PodSecurityPolicy
            metadata:
              name: no-cap-net-raw
            spec:
              requiredDropCapabilities:
                -NET_RAW
                 ...
                 # Unrelated fields omitted

  * Or by using Policy Controller or Gatekeeper with this [constraint template](https://github.com/open-policy-agent/gatekeeper-library/blob/master/library/pod-security-policy/capabilities/template.yaml) and applying it, for example: 
        
        # Dropping CAP_NET_RAW with Gatekeeper
            # (requires the K8sPSPCapabilities template)
            apiversion: constraints.gatekeeper.sh/v1beta1
            kind:  K8sPSPCapabilities
            metadata:
              name: forbid-cap-net-raw
            spec:
              match:
                kinds:
                  - apiGroups: [""]
                  kinds: ["Pod"]
                namespaces:
                  #List of namespaces to enforce this constraint on
                  - default
                # If running gatekeeper >= v3.1.0-beta.5,
                # you can exclude namespaces rather than including them above.
                excludedNamespaces:
                  - kube-system
              parameters:
                requiredDropCapabilities:
                  - "NET_RAW"

  * Or by updating your Pod specs: 
        
        # Dropping CAP_NET_RAW from a Pod:
            apiVersion: v1
            kind: Pod
            metadata:
              name: no-cap-net-raw
            spec:
              containers:
                -name: my-container
                 ...
                securityContext:
                  capabilities:
                    drop:
                      -NET_RAW




#### What vulnerability is addressed by this patch?

The patch mitigates the following vulnerability: The vulnerability [CVE-2020-14386](https://www.openwall.com/lists/oss-security/2020/09/03/3), which allows containers with `CAP_NET_RAW` to write 1 to 10 bytes of kernel memory, and possibly escape the container and obtain root privileges on the host node. This is rated as a High severity vulnerability. | High  
  
## GCP-2020-011

**Published:** 2020-07-24  
**Reference:**[CVE-2020-8558](https://github.com/kubernetes/kubernetes/issues/92315)  


### GKE

Description | Severity  
---|---  
A networking vulnerability, [CVE-2020-8558](https://github.com/kubernetes/kubernetes/issues/92315), was recently discovered in Kubernetes. Services sometimes communicate with other applications running inside the same Pod using the local loopback interface (127.0.0.1). This vulnerability allows an attacker with access to the cluster's network to send traffic to the loopback interface of adjacent Pods and nodes. Services that rely on the loopback interface not being accessible outside their Pod could be exploited. Exploiting this vulnerability on GKE clusters requires an attacker to have network administrator privileges on the Google Cloud hosting the cluster's VPC. This vulnerability alone does not give an attacker network administrator privileges. For this reason, this vulnerability has been assigned a Low severity for GKE.

#### What should I do?

To fix this vulnerability, [upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades) your cluster's node pools to the following GKE versions (and later):

  * 1.17.7-gke.0
  * 1.16.11-gke.0
  * 1.16.10-gke.11
  * 1.16.9-gke.14



#### What vulnerability is addressed by this patch?

This patch fixes the following vulnerability: [CVE-2020-8558](https://github.com/kubernetes/kubernetes/issues/92315). |  Low  
  
### GKE clusters on

Description | Severity  
---|---  
A networking vulnerability, [CVE-2020-8558](https://github.com/kubernetes/kubernetes/issues/92315), was recently discovered in Kubernetes. Services sometimes communicate with other applications running inside the same Pod using the local loopback interface (127.0.0.1). This vulnerability allows an attacker with access to the cluster's network to send traffic to the loopback interface of adjacent Pods and nodes. Services that rely on the loopback interface not being accessible outside their Pod could be exploited.

#### What should I do?

To fix this vulnerability, [upgrade](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/how-to/upgrading) your cluster to a patched version. The following upcoming GKE on VMware versions or newer contain the fix for this vulnerability:

  * GKE on VMware 1.4.1



#### What vulnerability is addressed by this patch?

This patch fixes the following vulnerability: [CVE-2020-8558](https://github.com/kubernetes/kubernetes/issues/92315). |  Medium  
  
### GKE clusters on

Description | Severity  
---|---  
A networking vulnerability, [CVE-2020-8558](https://github.com/kubernetes/kubernetes/issues/92315), was recently discovered in Kubernetes. Services sometimes communicate with other applications running inside the same Pod using the local loopback interface (127.0.0.1). This vulnerability allows an attacker with access to the cluster's network to send traffic to the loopback interface of adjacent Pods and nodes. Services that rely on the loopback interface not being accessible outside their Pod could be exploited. Exploiting this vulnerability on user clusters requires an attacker to disable [source destination checks](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_NAT_Instance.html) on the EC2 instances in the cluster. This requires the attacker to have AWS IAM permissions for `ModifyInstanceAttribute` or `ModifyNetworkInterfaceAttribute` on the EC2 instances. For this reason, this vulnerability has been assigned a Low severity for GKE on AWS.

#### What should I do?

To fix this vulnerability, upgrade your cluster to a patched version. The following upcoming GKE on AWS versions or newer are expected to include the fix for this vulnerability:

  * GKE on AWS 1.4.1-gke.17



#### What vulnerability is addressed by this patch?

This patch fixes the following vulnerability: [CVE-2020-8558](https://github.com/kubernetes/kubernetes/issues/92315). |  Low  
  
## GCP-2020-009

**Published:** 2020-07-15  
**Reference:**[CVE-2020-8559](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8559)  


### GKE

Description | Severity  
---|---  
A privilege escalation vulnerability, [CVE-2020-8559](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8559), was recently discovered in Kubernetes. This vulnerability allows an attacker that has already compromised a node to execute a command in any Pod in the cluster. The attacker can thereby use the already compromised node to compromise other nodes and potentially read information, or cause destructive actions. Note that for an attacker to exploit this vulnerability, a node in your cluster must have already been compromised. This vulnerability, by itself, will not compromise any nodes in your cluster.

#### What should I do?

[Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades) your cluster to a patched version. Clusters will be auto-upgraded over the next weeks, and patched versions will be available by July 19, 2020 for an accelerated manual upgrade schedule. The following GKE control plane versions or newer contain the fix for this vulnerability:

  * v1.14.10-gke.46
  * v1.15.12-gke.8
  * v1.16.9-gke.11
  * v1.16.10-gke.9
  * v1.16.11-gke.3+
  * v1.17.7-gke.6+



#### What vulnerability is addressed by this patch?

These patches mitigate vulnerability CVE-2020-8559. This is rated as a Medium vulnerability for GKE, as it requires the attacker to have first hand information about the cluster, nodes, and workloads to effectively leverage this attack in addition to an existing compromised node. This vulnerability by itself will not provide an attacker with a compromised node. | Medium  
  
### GKE clusters on

Description | Severity  
---|---  
A privilege escalation vulnerability, [CVE-2020-8559](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8559), was recently discovered in Kubernetes. This vulnerability allows an attacker that has already compromised a node to execute a command in any Pod in the cluster. The attacker can thereby use the already compromised node to compromise other nodes and potentially read information, or cause destructive actions. Note that for an attacker to exploit this vulnerability, a node in your cluster must have already been compromised. This vulnerability, by itself, will not compromise any nodes in your cluster.

#### What should I do?

[Upgrade](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/how-to/upgrading) your cluster to a patched version. The following upcoming GKE on VMware versions or newer contain the fix for this vulnerability:

  * Anthos 1.3.3
  * Anthos 1.4.1



#### What vulnerability is addressed by this patch?

These patches mitigate vulnerability CVE-2020-8559. This is rated as a Medium vulnerability for GKE, as it requires the attacker to have first hand information about the cluster, nodes, and workloads to effectively leverage this attack in addition to an existing compromised node. This vulnerability by itself will not provide an attacker with a compromised node. | Medium  
  
### GKE clusters on

Description | Severity  
---|---  
A privilege escalation vulnerability, [CVE-2020-8559](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8559), was recently discovered in Kubernetes. This vulnerability allows an attacker that has already compromised a node to execute a command in any Pod in the cluster. The attacker can thereby use the already compromised node to compromise other nodes and potentially read information, or cause destructive actions. Note that for an attacker to exploit this vulnerability, a node in your cluster must have already been compromised. This vulnerability, by itself, will not compromise any nodes in your cluster.

#### What should I do?

GKE on AWS GA (1.4.1, available end of July, 2020) or newer includes the patch for this vulnerability. If you are using a previous version, [download a new version of the anthos-gke command line tool](https://docs.cloud.google.com/anthos/clusters/docs/aws/how-to/prerequisites) and recreate your management and user clusters.

#### What vulnerability is addressed by this patch?

These patches mitigate vulnerability CVE-2020-8559. This is rated as a Medium vulnerability for GKE, as it requires the attacker to have first hand information about the cluster, nodes, and workloads to effectively leverage this attack in addition to an existing compromised node. This vulnerability by itself will not provide an attacker with a compromised node. | Medium  
  
## GCP-2020-007

**Published:** 2020-06-01  
**Reference:**[CVE-2020-8555](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8555)  


### GKE

Description | Severity  
---|---  
Server Side Request Forgery (SSRF) vulnerability, [CVE-2020-8555](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8555), was recently discovered in Kubernetes, allowing certain authorized users to leak up to 500 bytes of sensitive information from the control plane host network. The Google Kubernetes Engine (GKE) control plane uses controllers from Kubernetes and is thus affected by this vulnerability. We recommend that you [upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) the control plane to the latest patch version, as we detail below. A node upgrade is not required. 

#### What should I do?

For most customers, no further action is required. The vast majority of clusters are already running a patched version. The following GKE versions or newer contain the fix for this vulnerability: 

  * 1.14.7-gke.39
  * 1.14.8-gke.32
  * 1.14.9-gke.17
  * 1.14.10-gke.12
  * 1.15.7-gke.17
  * 1.16.4-gke.21
  * 1.17.0-gke.0

Clusters using [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels) are already on control plane versions with the mitigation. 

#### What vulnerability is addressed by this patch? 

These patches mitigate vulnerability CVE-2020-8555. This is rated as a Medium vulnerability for GKE as it was difficult to exploit due to various control plane hardening measures. An attacker with permissions to create a Pod with certain built-in Volume types (GlusterFS, Quobyte, StorageFS, ScaleIO) or permissions to create a StorageClass can cause `kube-controller-manager` to make `GET` requests or `POST` requests _without_ an attacker controlled request body from the master's host network. These volume types are rarely used on GKE, so new use of these volume types may be a useful detection signal. Combined with a means to leak the results of the `GET/POST` back to the attacker, such as through logs, this can lead to disclosure of sensitive information. We have updated the storage drivers in question to remove the potential for such leaks.  | Medium  
  
### GKE clusters on

Description | Severity  
---|---  
Server Side Request Forgery (SSRF) vulnerability, [CVE-2020-8555](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8555), was recently discovered in Kubernetes, allowing certain authorized users to leak up to 500 bytes of sensitive information from the control plane host network. The Google Kubernetes Engine (GKE) control plane uses controllers from Kubernetes and is thus affected by this vulnerability. We recommend that you upgrade the control plane to the latest patch version, as we detail below. A node upgrade is not required.

#### What should I do?

The following GKE on VMware versions or newer contain the fix for this vulnerability: 

  * Anthos 1.3.0

If you are using a previous version, [upgrade your existing cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/how-to/upgrading) to a version containing the fix.

#### What vulnerability is addressed by this patch? 

These patches mitigate vulnerability CVE-2020-8555. This is rated as a Medium vulnerability for GKE as it was difficult to exploit due to various control plane hardening measures. An attacker with permissions to create a Pod with certain built-in Volume types (GlusterFS, Quobyte, StorageFS, ScaleIO) or permissions to create a StorageClass can cause `kube-controller-manager` to make `GET` requests or `POST` requests _without_ an attacker controlled request body from the master's host network. These volume types are rarely used on GKE, so new use of these volume types may be a useful detection signal. Combined with a means to leak the results of the `GET/POST` back to the attacker, such as through logs, this can lead to disclosure of sensitive information. We have updated the storage drivers in question to remove the potential for such leaks.  | Medium  
  
### GKE clusters on

Description | Severity  
---|---  
Server Side Request Forgery (SSRF) vulnerability, [CVE-2020-8555](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8555), was recently discovered in Kubernetes, allowing certain authorized users to leak up to 500 bytes of sensitive information from the control plane host network. The Google Kubernetes Engine (GKE) control plane uses controllers from Kubernetes and is thus affected by this vulnerability. We recommend that you upgrade the control plane to the latest patch version, as we detail below. A node upgrade is not required.

#### What should I do?

GKE on AWS v0.2.0 or newer already includes the patch for this vulnerability. If you are using a previous version, [download a new version of the anthos-gke command line tool](https://docs.cloud.google.com/anthos/clusters/docs/aws/how-to/prerequisites) and recreate your management and user clusters.

#### What vulnerability is addressed by this patch? 

These patches mitigate vulnerability CVE-2020-8555. This is rated as a Medium vulnerability for GKE as it was difficult to exploit due to various control plane hardening measures. An attacker with permissions to create a Pod with certain built-in Volume types (GlusterFS, Quobyte, StorageFS, ScaleIO) or permissions to create a StorageClass can cause `kube-controller-manager` to make `GET` requests or `POST` requests _without_ an attacker controlled request body from the master's host network. These volume types are rarely used on GKE, so new use of these volume types may be a useful detection signal. Combined with a means to leak the results of the `GET/POST` back to the attacker, such as through logs, this can lead to disclosure of sensitive information. We have updated the storage drivers in question to remove the potential for such leaks.  | Medium  
  
## GCP-2020-006

**Published:** 2020-06-01  
**Reference:**[Kubernetes issue 91507](https://github.com/kubernetes/kubernetes/issues/91507)  


### GKE

Description | Severity  
---|---  
Kubernetes has disclosed a [vulnerability](https://github.com/kubernetes/kubernetes/issues/91507) that allows a privileged container to redirect node traffic to another container. Mutual TLS/SSH traffic, such as between the kubelet and API server or traffic from applications using mTLS cannot be read or modified by this attack. All Google Kubernetes Engine (GKE) nodes are affected by this vulnerability, and we recommend that you [upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) to the latest patch version, as we detail below.

####  What should I do?

To mitigate this vulnerability, [upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) your control plane, and then your nodes to one of the patched versions listed below. Clusters on release channels are already running a patched version on both control plane and nodes: 

  * 1.14.10-gke.36
  * 1.15.11-gke.15
  * 1.16.8-gke.15

Very few containers typically require `CAP_NET_RAW`. This and other powerful capabilities should be blocked by default through [PodSecurityPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies) or [Anthos Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller): Drop the `CAP_NET_RAW` capability from containers with one of the following methods:

  * Enforce blocking these capabilities with [`PodSecurityPolicy`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies), for example: 
        
        # Require dropping CAP_NET_RAW with a PSP
            apiversion: extensions/v1beta1
            kind: PodSecurityPolicy
            metadata:
              name: no-cap-net-raw
            spec:
              requiredDropCapabilities:
                -NET_RAW
                 ...
                 # Unrelated fields omitted

  * Or by using Policy Controller or Gatekeeper with this [constraint template](https://github.com/open-policy-agent/gatekeeper-library/blob/master/library/pod-security-policy/capabilities/template.yaml) and applying it, for example: 
        
        # Dropping CAP_NET_RAW with Gatekeeper
            # (requires the K8sPSPCapabilities template)
            apiversion: constraints.gatekeeper.sh/v1beta1
            kind:  K8sPSPCapabilities
            metadata:
              name: forbid-cap-net-raw
            spec:
              match:
                kinds:
                  - apiGroups: [""]
                  kinds: ["Pod"]
                namespaces:
                  #List of namespaces to enforce this constraint on
                  - default
                # If running gatekeeper >= v3.1.0-beta.5,
                # you can exclude namespaces rather than including them above.
                excludedNamespaces:
                  - kube-system
              parameters:
                requiredDropCapabilities:
                  - "NET_RAW"

  * Or by updating your Pod specs: 
        
        # Dropping CAP_NET_RAW from a Pod:
            apiVersion: v1
            kind: Pod
            metadata:
              name: no-cap-net-raw
            spec:
              containers:
                -name: my-container
                 ...
                securityContext:
                  capabilities:
                    drop:
                      -NET_RAW




#### What vulnerability is addressed by this patch? 

The patch mitigate the following vulnerability: The vulnerability described in [Kubernetes issue 91507](https://github.com/kubernetes/kubernetes/issues/91507) `CAP_NET_RAW` capability (which is included in the default container capability set) to maliciously configure the IPv6 stack on the node and redirect node traffic to the attacker controlled container. This will allow the attacker to intercept/modify traffic originating from or destined for the node. Mutual TLS/SSH traffic, such as between the kubelet and API server or traffic from applications using mTLS cannot be read or modified by this attack. | Medium  
  
### GKE clusters on

Description | Severity  
---|---  
Kubernetes has disclosed a [vulnerability](https://github.com/kubernetes/kubernetes/issues/91507) that allows a privileged container to redirect node traffic to another container. Mutual TLS/SSH traffic, such as between the kubelet and API server or traffic from applications using mTLS cannot be read or modified by this attack. All Google Kubernetes Engine (GKE) nodes are affected by this vulnerability, and we recommend that you upgrade to the latest patch version, as we detail below.

####  What should I do?

To mitigate this vulnerability for GKE on VMware, [upgrade your clusters](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/how-to/upgrading) to the following version or newer: 

  * Anthos 1.3.2

Very few containers typically require `CAP_NET_RAW`. This and other powerful capabilities should be blocked by default through [Anthos Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller) or by updating your Pod specs: Drop the `CAP_NET_RAW` capability from containers with one of the following methods:

  * Enforce blocking these capabilities with [`PodSecurityPolicy`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies), for example: 
        
        # Require dropping CAP_NET_RAW with a PSP
            apiversion: extensions/v1beta1
            kind: PodSecurityPolicy
            metadata:
              name: no-cap-net-raw
            spec:
              requiredDropCapabilities:
                -NET_RAW
                 ...
                 # Unrelated fields omitted

  * Or by using Policy Controller or Gatekeeper with this [constraint template](https://github.com/open-policy-agent/gatekeeper-library/blob/master/library/pod-security-policy/capabilities/template.yaml) and applying it, for example: 
        
        # Dropping CAP_NET_RAW with Gatekeeper
            # (requires the K8sPSPCapabilities template)
            apiversion: constraints.gatekeeper.sh/v1beta1
            kind:  K8sPSPCapabilities
            metadata:
              name: forbid-cap-net-raw
            spec:
              match:
                kinds:
                  - apiGroups: [""]
                  kinds: ["Pod"]
                namespaces:
                  #List of namespaces to enforce this constraint on
                  - default
                # If running gatekeeper >= v3.1.0-beta.5,
                # you can exclude namespaces rather than including them above.
                excludedNamespaces:
                  - kube-system
              parameters:
                requiredDropCapabilities:
                  - "NET_RAW"

  * Or by updating your Pod specs: 
        
        # Dropping CAP_NET_RAW from a Pod:
            apiVersion: v1
            kind: Pod
            metadata:
              name: no-cap-net-raw
            spec:
              containers:
                -name: my-container
                 ...
                securityContext:
                  capabilities:
                    drop:
                      -NET_RAW




#### What vulnerability is addressed by this patch? 

The patch mitigate the following vulnerability: The vulnerability described in [Kubernetes issue 91507](https://github.com/kubernetes/kubernetes/issues/91507) `CAP_NET_RAW` capability (which is included in the default container capability set) to maliciously configure the IPv6 stack on the node and redirect node traffic to the attacker controlled container. This will allow the attacker to intercept/modify traffic originating from or destined for the node. Mutual TLS/SSH traffic, such as between the kubelet and API server or traffic from applications using mTLS cannot be read or modified by this attack. | Medium  
  
### GKE clusters on

Description | Severity  
---|---  
Kubernetes has disclosed a [vulnerability](https://github.com/kubernetes/kubernetes/issues/91507) that allows a privileged container to redirect node traffic to another container. Mutual TLS/SSH traffic, such as between the kubelet and API server or traffic from applications using mTLS cannot be read or modified by this attack. All Google Kubernetes Engine (GKE) nodes are affected by this vulnerability, and we recommend that you upgrade to the latest patch version, as we detail below.

####  What should I do?

[Download the anthos-gke command line tool](https://docs.cloud.google.com/anthos/clusters/docs/aws/how-to/prerequisites) with the following version or newer and recreate your management and user clusters: 

  * aws-0.2.1-gke.7

Very few containers typically require `CAP_NET_RAW`. This and other powerful capabilities should be blocked by default through [Anthos Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller) or by updating your Pod specs: Drop the `CAP_NET_RAW` capability from containers with one of the following methods:

  * Enforce blocking these capabilities with [`PodSecurityPolicy`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies), for example: 
        
        # Require dropping CAP_NET_RAW with a PSP
            apiversion: extensions/v1beta1
            kind: PodSecurityPolicy
            metadata:
              name: no-cap-net-raw
            spec:
              requiredDropCapabilities:
                -NET_RAW
                 ...
                 # Unrelated fields omitted

  * Or by using Policy Controller or Gatekeeper with this [constraint template](https://github.com/open-policy-agent/gatekeeper-library/blob/master/library/pod-security-policy/capabilities/template.yaml) and applying it, for example: 
        
        # Dropping CAP_NET_RAW with Gatekeeper
            # (requires the K8sPSPCapabilities template)
            apiversion: constraints.gatekeeper.sh/v1beta1
            kind:  K8sPSPCapabilities
            metadata:
              name: forbid-cap-net-raw
            spec:
              match:
                kinds:
                  - apiGroups: [""]
                  kinds: ["Pod"]
                namespaces:
                  #List of namespaces to enforce this constraint on
                  - default
                # If running gatekeeper >= v3.1.0-beta.5,
                # you can exclude namespaces rather than including them above.
                excludedNamespaces:
                  - kube-system
              parameters:
                requiredDropCapabilities:
                  - "NET_RAW"

  * Or by updating your Pod specs: 
        
        # Dropping CAP_NET_RAW from a Pod:
            apiVersion: v1
            kind: Pod
            metadata:
              name: no-cap-net-raw
            spec:
              containers:
                -name: my-container
                 ...
                securityContext:
                  capabilities:
                    drop:
                      -NET_RAW




#### What vulnerability is addressed by this patch? 

The patch mitigate the following vulnerability: The vulnerability described in [Kubernetes issue 91507](https://github.com/kubernetes/kubernetes/issues/91507) `CAP_NET_RAW` capability (which is included in the default container capability set) to maliciously configure the IPv6 stack on the node and redirect node traffic to the attacker controlled container. This will allow the attacker to intercept/modify traffic originating from or destined for the node. Mutual TLS/SSH traffic, such as between the kubelet and API server or traffic from applications using mTLS cannot be read or modified by this attack. | Medium  
  
## GCP-2020-005

**Published:** 2020-05-07  
**Updated:** 2020-05-07  
**Reference:**[CVE-2020-8835](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8835)  


### GKE

Description | Severity  
---|---  
A vulnerability was recently discovered in the Linux kernel, described in [CVE-2020-8835](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8835), allowing container escape to obtain root privileges on the host node.  Google Kubernetes Engine (GKE) Ubuntu nodes running GKE 1.16 or 1.17 are affected by this vulnerability, and we recommend that you upgrade to the latest patch version as soon as possible, as we detail below.  Nodes running Container-Optimized OS are not affected. Nodes running on GKE on VMware are not affected. 

#### What should I do?

**For most customers, no further action is required. Only nodes running Ubuntu in GKE version 1.16 or 1.17 are affected.** In order to upgrade your nodes, you must first upgrade your master to the newest version. This patch will be available in Kubernetes 1.16.8-gke.12, 1.17.4-gke.10, and newer releases. Track the availability of these patches in the [release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes). 

#### What vulnerability is addressed by this patch?

The patch mitigates the following vulnerability:  [CVE-2020-8835](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8835) describes a vulnerability in the Linux kernel version 5.5.0 and newer that allows a malicious container to (with minimal user interaction in the form of an exec) read and write kernel memory and thus gain root-level code execution on the host node. This is rated as a 'High' severity vulnerability.  | High  
  
## GCP-2020-004

**Published:** 2020-05-07  
**Updated:** 2020-05-07  
**Reference:**[CVE-2019-11254](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11254)  


### GKE clusters on

Description | Severity  
---|---  
A vulnerability was recently discovered in Kubernetes, described in [CVE-2019-11254](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11254), which allows any user authorized to make POST requests to execute a remote Denial-of-Service attack on a Kubernetes API server. The Kubernetes Product Security Committee (PSC) released additional information on this vulnerability which can be found [here](https://groups.google.com/g/kubernetes-security-announce/c/wuwEwZigXBc).  You can mitigate this vulnerability by limiting which clients have network access to your Kubernetes API servers. 

#### What should I do?

We recommend that you upgrade your clusters to patch versions containing the fix for this vulnerability as soon as they are available.  The patch versions which contain the fix are listed below: 

  * Anthos 1.3.0, which runs Kubernetes version 1.15.7-gke.32



#### What vulnerabilities are addressed by this patch?

The patch fixes the following Denial-of-Service (DoS) vulnerability:  [CVE-2019-11254](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11254).  | Medium  
  
## GCP-2020-003

**Published:** 2020-03-31  
**Updated:** 2020-03-31  
**Reference:**[CVE-2019-11254](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11254)  


### GKE

Description | Severity  
---|---  
A vulnerability was recently discovered in Kubernetes, described in [CVE-2019-11254](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11254), which allows any user authorized to make POST requests to execute a remote Denial-of-Service attack on a Kubernetes API server. The Kubernetes Product Security Committee (PSC) released additional information on this vulnerability which can be found [here](https://groups.google.com/forum/#!topic/kubernetes-security-announce/wuwEwZigXBc).  GKE Clusters that use [Master Authorized Networks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks) and [Private clusters with no public endpoint](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#private_master) mitigate this vulnerability. 

#### What should I do?

We recommend that you upgrade your cluster to a patch version containing the fix for this vulnerability.  The patch versions which contain the fix are listed below: 

  * 1.13.12-gke.29
  * 1.14.9-gke.27
  * 1.14.10-gke.24
  * 1.15.9-gke.20
  * 1.16.6-gke.1



#### What vulnerabilities are addressed by this patch?

The patch fixes the following Denial-of-Service (DoS) vulnerability:  [CVE-2019-11254](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11254).  | Medium  
  
## GCP-2020-002

**Published:** 2020-03-23  
**Updated:** 2020-03-23  
**Reference:**[CVE-2020-8551](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8551), [CVE-2020-8552](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8552)  


### GKE

Description | Severity  
---|---  
Kubernetes has disclosed [two denial of service vulnerabilities](https://groups.google.com/forum/#!topic/kubernetes-security-announce/2UOlsba2g0s), one impacting the API server, and the other impacting Kubelets. For more details, see the Kubernetes issues: [89377](https://github.com/kubernetes/kubernetes/issues/89377) and [89378](https://github.com/kubernetes/kubernetes/issues/89378). 

#### What should I do?

All GKE users are protected from CVE-2020-8551 unless untrusted users can send requests within the cluster's internal network. Use of [master authorized networks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks) additionally mitigates against CVE-2020-8552. 

#### When will these be patched?

Patches for CVE-2020-8551 require a node upgrade. The patch versions which will contain the mitigation are listed below: 

  * 1.15.10-gke.*
  * 1.16.7-gke.*

Note: Versions 1.14.x and earlier are unaffected by this vulnerability so no patches are required.  Patches for CVE-2020-8552 require a master upgrade. The patch versions which will contain the mitigation are listed below: 

  * 1.14.10-gke.32
  * 1.15.10-gke.*
  * 1.16.7-gke.*

| Medium  
  
## GCP-january_21_2020

**Published:** 2020-01-21  
**Updated:** 2020-01-24  
**Reference:**[CVE-2019-11254](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11254)  


### GKE

Description | Severity  
---|---  
**2020-01-24 Update:** The process of making patched versions available is already underway and will be completed by January 25, 2020.

* * *

Microsoft has disclosed a vulnerability in the Windows Crypto API and its validation of elliptic curve signatures. For more information please see [ Microsoft's disclosure.](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0601) **What should I do?** **For most customers, no further action is required. Only nodes running Windows Server are impacted.** For customers who are using Windows Server nodes, both the nodes and the containerized workloads that run on those nodes must be updated to patched versions to mitigate this vulnerability. **To update the containers:** Rebuild your containers using Microsoft's latest base container images, selecting a [servercore](https://hub.docker.com/_/microsoft-windows-servercore) or [nanoserver](https://hub.docker.com/_/microsoft-windows-nanoserver) tag with a LastUpdated Time of 1/14/2020 or later. **To update the nodes:** The process of making patched versions available is already underway and will be completed by January 24, 2020. You may either wait until that time and perform a node upgrade to a patched GKE version or you may use Windows Update to deploy the latest Windows patch manually at any time.  The patch versions which will contain the mitigation are listed below:

  * 1.14.7-gke.40
  * 1.14.8-gke.33
  * 1.14.9-gke.23
  * 1.14.10-gke.17
  * 1.15.7-gke.23
  * 1.16.4-gke.22

**What vulnerabilities are addressed by this patch?** The patch mitigates the following vulnerabilities: [CVE-2020-0601](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-0601) \- This vulnerability is also known as the [Windows Crypto API Spoofing Vulnerability](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0601) and could be exploited to make malicious executables appear trusted or allow the attacker to conduct man-in-the-middle attacks and decrypt confidential information on TLS connections to the affected software. | NVD Base Score: 8.1 (High)  
  
## Archived security bulletins

For security bulletins prior to 2020, see the [Security bulletins archive](https://docs.cloud.google.com/kubernetes-engine/security-bulletins-archive).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
