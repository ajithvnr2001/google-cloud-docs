---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/seccomp-in-gke/
title: About seccomp in GKE \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:41.919227+00:00
---

# About seccomp in GKE  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/seccomp-in-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  About seccomp in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes the Linux _secure computing_ mode (seccomp) in Google Kubernetes Engine (GKE). This document assumes that you know about the following:

  * [Seccomp](https://en.wikipedia.org/wiki/Seccomp)
  * [Seccomp commands](https://man7.org/linux/man-pages/man2/seccomp.2.html)



Use the information in this document to understand which actions your containerized applications can perform on the host virtual machine (VM) that backs your nodes.

This document is for Security specialists who use seccomp as part of their organization's security strategy and want to understand how GKE interacts with seccomp profiles. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## What is seccomp?

Secure computing mode, or seccomp, is a security capability in Linux that lets you restrict the system calls (syscalls) that a process can make to the Linux kernel.

By default, GKE nodes use the [Container-Optimized OS operating system](https://docs.cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits) with the [containerd _container runtime_](https://containerd.io/). containerd protects the Linux kernel by limiting the allowed Linux _capabilities_ to a default list, and you can further limit allowed syscalls with a seccomp _profile_. containerd has a default seccomp profile available. Whether GKE applies the default seccomp profile for you depends on the cluster mode that you use, as follows:

  * [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) (recommended): GKE applies the containerd default seccomp profile to all workloads automatically.
  * [Standard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#modes): GKE **does not** apply the containerd default seccomp profile to all workloads automatically. We recommend that you apply either the default seccomp profile or a custom seccomp profile to your workloads.



The default containerd seccomp profile provides baseline hardening while maintaining compatibility with most workloads. The full seccomp profile definition for containerd is available on [GitHub](https://github.com/containerd/containerd/blob/main/contrib/seccomp/seccomp_default.go).

## Linux capabilities and syscalls

Non-root processes running on Linux systems might require specific privileges to perform actions as the root user. Linux uses _capabilities_ to divide the available privileges into groups, so that a non-root process can perform a specific action without being granted all privileges. For a process to successfully make a specific syscall, the process must have the corresponding privileges granted by a capability.

For a list of all Linux capabilities, refer to [capabilities](https://man7.org/linux/man-pages/man7/capabilities.7.html) .

## Denied syscalls in the default GKE seccomp profile

The containerd default seccomp profile blocks all syscalls and then selectively allows specific syscalls, some of which depend on the CPU architecture of the node's VM and the kernel version. The [`syscalls` variable in the `DefaultProfile` function](https://github.com/containerd/containerd/blob/main/contrib/seccomp/seccomp_default.go#L58) lists the allowed syscalls for all architectures.

The default seccomp profile blocks syscalls that can be used to bypass container isolation boundaries and allow privileged access to the node or to other containers. The following table describes some of the significant syscalls that the default seccomp profile denies:

Denied syscalls  
---  
`mount`, `umount`, `umount2`, `fsmount`, `mount_setattr` | Restrict processes from accessing or manipulating the node filesystem outside of the container boundaries. Also denied because the [`CAP_SYS_ADMIN` capability](https://github.com/containerd/containerd/blob/main/contrib/seccomp/seccomp_default.go#L572) is dropped.  
`bpf` | Restrict processes from creating eBPF programs in the kernel, which can lead to privilege escalation on the node. For example, [CVE-2021-3490](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3490) used the `bpf` syscall. Also denied because the [`CAP_SYS_ADMIN` capability](https://github.com/containerd/containerd/blob/main/contrib/seccomp/seccomp_default.go#L572) is dropped.  
`clone`, `clone3`, `unshare` | Restrict processes from creating new processes in new namespaces that might be outside the container's restricted namespace. These new processes might have elevated permissions and capabilities. For example, [CVE-2022-0185](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0185) used the `unshare` syscall. Also denied because the [`CAP_SYS_ADMIN` capability](https://github.com/containerd/containerd/blob/main/contrib/seccomp/seccomp_default.go#L572) is dropped.  
`reboot` | Restrict processes from rebooting the node. Denied because the [`CAP_SYS_BOOT` capability](https://github.com/containerd/containerd/blob/main/contrib/seccomp/seccomp_default.go#L604) is dropped.  
`open_by_handle_at`, `name_to_handle_at` | Restrict access to files outside of the container. These syscalls were used in one of the earliest [Docker container escape exploits](https://www.exploit-db.com/exploits/33808). Also denied because the [`CAP_DAC_READ_SEARCH` capability](https://github.com/containerd/containerd/blob/main/contrib/seccomp/seccomp_default.go#L566) and the [`CAP_SYS_ADMIN` capability](https://github.com/containerd/containerd/blob/main/contrib/seccomp/seccomp_default.go#L572) are dropped.  
**Note:** This table only describes a subset of the syscalls that the default seccomp profile blocks. For a full list, refer to the [profile definition on GitHub](https://github.com/containerd/containerd/blob/main/contrib/seccomp/seccomp_default.go).

## How to use seccomp in GKE

In Autopilot clusters, GKE automatically applies the containerd default seccomp profile to all your workloads. No further action is required. Attempts to make restricted syscalls fail. Autopilot disallows custom seccomp profiles because GKE manages the nodes.

In Standard clusters, you must manually apply a seccomp profile. GKE doesn't apply a profile for you.

### Enable seccomp in Standard clusters

Apply a seccomp profile manually by setting the Pod or container [Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) using the `spec.securityContext.seccompProfile` field in the Pod specification, such as in the following example. We strongly recommend that you use a seccomp profile for your workloads unless your use case requires using any restricted syscalls. The two supported `seccompProfile` types are as follows:

  * `RuntimeDefault`: the default profile specified by the containerd runtime.
  * `Localhost`: a custom profile definition.



The following example manifest sets the seccomp profile to the runtime default profile:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-deployment
      labels:
        app: default-pod
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: default-pod
      template:
        metadata:
          labels:
            app: default-pod
        spec:
          **securityContext :
            seccompProfile:
              type: RuntimeDefault**
          containers:
          - name: seccomp-test
            image: nginx
    

**Important:** You can't apply a seccomp profile to containers that run in [Privileged mode](https://kubernetes.io/docs/concepts/workloads/pods/#privileged-mode-for-containers).

When you deploy this manifest, if a container in the Pod tries to make a syscall that violates the runtime default seccomp profile, the Pod or the workload might experience unexpected behavior. For example, a Pod that makes a restricted syscall during startup would fail to start. If an application tries to make a restricted syscall while the Pod is running, you might notice errors in the container. The severity of a failed syscall depends on how the application handles errors.

### Use a custom seccomp profile in Standard clusters

If the runtime default seccomp profile is too restrictive for your application (or not restrictive enough), you can apply a custom seccomp profile to Pods in Standard clusters. This process requires access to the filesystem on the node. For a tutorial on how to load and use custom seccomp profiles, refer to [Restrict a Container's Syscalls with seccomp](https://kubernetes.io/docs/tutorials/security/seccomp/).

## What's next

  * [Use PodSecurityAdmission to enforce pre-defined Pod-level policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/podsecurityadmission)
  * [Use Organization Policy Service to set project or organization-level policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/custom-org-policies)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
