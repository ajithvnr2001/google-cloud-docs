---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-configuration-scanning/
title: About Kubernetes security posture scanning \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:20.893351+00:00
---

# About Kubernetes security posture scanning  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-configuration-scanning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  About Kubernetes security posture scanning Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes how to use _Kubernetes security posture scanning_ to find and mitigate security risks in GKE. This document assumes that you know about the following:

  * [security posture dashboard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard)



Kubernetes security posture screening is a feature of security posture dashboard that helps you proactively identify and address security vulnerabilities in your Google Kubernetes Engine (GKE) clusters. Kubernetes security posture scanning provides the following features:

  * Workload configuration auditing
  * Actionable security bulletin surfacing



This document is for Security specialists who monitor clusters for security issues. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

To learn how to enable and use Kubernetes security posture scanning, see [Automatically audit workloads for configuration issues](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/protect-workload-configuration#overview).

## Pricing

Offered at no extra charge in GKE.

Entries added to Cloud Logging are subject to [Cloud Logging pricing](https://cloud.google.com/stackdriver/pricing#logging-costs).

## About workload configuration auditing

The workloads that you deploy on GKE should have a hardened configuration that limits their attack surface. Checking workloads across clusters for configuration issues can be difficult to do manually at scale. You can use the security posture dashboard to automatically audit the configuration of all your running workloads across multiple clusters and return actionable, scored results and opinionated recommendations to improve your security posture.

Workload configuration auditing checks each deployed workload against a subset of policies in the [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/). Workload configuration auditing happens on Google's infrastructure and doesn't use compute resources on your nodes.

### Benefits of workload configuration auditing

  * Automate detection of known configuration concerns across all workloads.
  * Get actionable recommendations to improve security posture.
  * Use the Google Cloud console to get a high-level view of configuration concerns.
  * Use Logging to get an auditable trail of concerns for better reporting and observability.



### How workload configuration auditing works

For each eligible deployed workload, GKE continuously scans the workload's specification and compares the fields and values to the controls defined in the underlying security policy. For example, a Pod with `spec.containers.securityContext.privileged=true` violates the Baseline Pod Security Standard, and a Pod with the `spec.securityContext.runAsNonRoot` field set to `false` violates the Restricted standard. For a list of the security policies that GKE checks, refer to What does workload configuration auditing check?.

After scanning and discovering concerns, GKE rates the severity of discovered configuration issues based on the built-in security hardening measures. GKE assigns a [severity rating](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard#severity-ratings) that can inform the speed with which you respond to the concern. The Google Cloud console displays the results and recommended actions you can take to fix the concerns. GKE also adds entries to Cloud Logging for tracing and auditing.

### What does workload configuration auditing check?

Concern | Fields | Allowed values | Severity  
---|---|---|---  
**Host namespaces** Pods that share host namespaces allow Pod processes to communicate with host processes and gather host information, which could lead to a container escape. | 

  * `spec.hostNetwork`
  * `spec.hostIPC`
  * `spec.hostPID`

| 

  * Undefined or nil
  * `false`

| High  
**Privileged containers** Privileged containers allow nearly unrestricted host access. They share namespaces with the host, and lack control group, seccomp, AppArmor, and capability restrictions. | 

  * `spec.containers[*].securityContext.privileged`
  * `spec.initContainers[*].securityContext.privileged`
  * `spec.ephemeralContainers[*].securityContext.privileged`

| 

  * Undefined or nil
  * `false`

| High  
**Host port access** Exposing a host port to a container potentially allows the container to intercept network traffic to a host service using that port or to bypass network access control rules, such as the rules in a NetworkPolicy. | 

  * `spec.containers[*].ports[*].hostPort`
  * `spec.initContainers[*].ports[*].hostPort`
  * `spec.ephemeralContainers[*].ports[*].hostPort`

| 

  * Undefined or nil
  * `0`

| High  
**Non-default capabilities** A container has assigned capabilities that could allow a container escape. | 

  * `spec.containers[*].securityContext.capabilities.add`
  * `spec.initContainers[*].securityContext.capabilities.add`
  * `spec.ephemeralContainers[*].securityContext.capabilities.add`

| 

  * Undefined or nil
  * `AUDIT_WRITE`
  * `CHOWN`
  * `DAC_OVERRIDE`
  * `FOWNER`
  * `FSETID`
  * `KILL`
  * `MKNOD`
  * `NET_BIND_SERVICE`
  * `SETFCAP`
  * `SETGID`
  * `SETPCAP`
  * `SETUID`
  * `SYS_CHROOT`

| Medium  
**Mounting host path volumes** `hostPath` volumes mount files or directories from the host. These volumes present security risks that could lead to container escape. | `spec.volumes[*].hostPath` | Undefined or nil | Medium  
**Non-default`/proc` mask** The default `/proc` mount type masks certain paths in `/proc` to avoid exposure of paths that could lead to information leakage or container escape. Using a non-default type increases these risks. | 

  * `spec.containers[*].securityContext.procMount`
  * `spec.initContainers[*].securityContext.procMount`
  * `spec.ephemeralContainers[*].securityContext.procMount`

| 

  * Undefined or nil
  * Default

| Medium  
**Unsafe sysctls mask** A Pod can be configured to allow modification of unsafe kernel parameters using the `/proc/sys` virtual file system. Unsafe parameters don't support namespacing, don't properly isolate their effect between Pods, could harm the node's health, or might allow the Pod to gain resources beyond its limits. | `spec.securityContext.sysctls[*].name` | 

  * Undefined or nil
  * `kernel.shm_rmid_forced`
  * `net.ipv4.ip_local_port_range`
  * `net.ipv4.ip_unprivileged_port_start`
  * `net.ipv4.tcp_syncookies`
  * `net.ipv4.ping_group_range`

| Medium  
**Running as non-root** You can explicitly allow a container to run as the root user if the `runAsUser` or the `USER` directive in the image specifies the root user. The lack of preventive security controls when running as the root user increases the risk of container escape. | 

  * `spec.securityContext.runAsNonRoot`
  * `spec.containers[*].securityContext.runAsNonRoot`
  * `spec.initContainers[*].securityContext.runAsNonRoot`
  * `spec.ephemeralContainers[*].securityContext.runAsNonRoot`

| `true` | Medium  
**Privilege escalation** A container can be explicitly configured to allow privilege escalation on execution. This permits a process created within the container by executing a set-user-id, set-group-id, or file capability executable to gain the privileges specified by the executable. The lack of preventive security control increases the risk of container escape. | 

  * `spec.containers[*].securityContext.allowPrivilegeEscalation`
  * `spec.initContainers[*].securityContext.allowPrivilegeEscalation`
  * `spec.ephemeralContainers[*].securityContext.allowPrivilegeEscalation`

| `false` | Medium  
**Unconfined AppArmor profile** A container can be explicitly configured to be unconfined by AppArmor. This configuration helps ensure that no AppArmor profile is applied to the container and is thus not constrained by them. The disabled preventive security control increases the risk of container escape. | `metadata.annotations["container.apparmor.security.beta.kubernetes.io/*"]` | `false` | Low  
  
Additionally, GKE checks for any RBAC RoleBindings or ClusterRoleBindings that reference one of the following users or groups:

  * `system:anonymous`
  * `system:authenticated`
  * `system:unauthenticated`



If any RBAC bindings that reference these users or groups exist, a finding named **Effectively Anonymous Users Granted GKE Cluster Access** with a severity of **Medium** appears in the security posture dashboard. These users and groups are effectively anonymous and shouldn't be used in RoleBindings or ClusterRoleBindings. For more information, see [Avoid default roles and groups](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/rbac#default-roles-groups).

## About security bulletin surfacing

When a vulnerability is discovered in GKE, we patch the vulnerability and publish a security bulletin for the vulnerability. For information about identification, patching, and timelines, refer to [GKE security patching](https://docs.cloud.google.com/kubernetes-engine/docs/resources/security-patching).

The security posture dashboard displays security bulletins that affect your clusters, workloads, and Standard mode node pools. This feature is a part of the _Kubernetes security posture_ capability of the security posture dashboard and is automatically enabled when you create an Autopilot or Standard cluster. To enable Kubernetes security posture scanning, use the instructions in [Automatically audit workloads for configuration issues](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/protect-workload-configuration).

The Google Cloud console displays details such as affected clusters, versions, and recommended patch versions for upgrades to mitigate the vulnerability. You only see bulletins for which a mitigation is available in your cluster's Google Cloud region or zone.

To view bulletins for clusters that you enrolled in Kubernetes security posture scanning, go to the security posture dashboard:

[Go to Security Posture](https://console.cloud.google.com/kubernetes/security)

Any available bulletins that affect your environment appear in the **Security bulletins** section.

## What's next

  * [Learn about the security posture dashboard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard).
  * [Learn how to implement workload configuration auditing](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/protect-workload-configuration).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
