---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/cis-benchmarks/
title: CIS Benchmarks \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:47:03.188844+00:00
---

# CIS Benchmarks  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/cis-benchmarks/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  CIS Benchmarks Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/concepts/cis-benchmarks)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/cis-benchmarks)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



This document introduces the CIS Kubernetes Benchmark, explains how to audit your compliance with the benchmark. For recommendations that you can't implement yourself, the document explains what Distributed Cloud does to address the recommendation.

## Using the CIS Benchmarks

The Center for Internet Security (CIS) releases benchmarks for best practice security recommendations. The [CIS Kubernetes Benchmark](https://www.cisecurity.org/benchmark/kubernetes/) provides a set of recommendations for configuring Kubernetes to support a strong security posture. The Benchmark is tied to a specific Kubernetes release. The CIS Kubernetes Benchmark is written for the open source Kubernetes distribution and intended to be as universally applicable across distributions as possible.

### Versions

The following table lists the versions of Google Distributed Cloud, Kubernetes, and the CIS Kubernetes Benchmark that were used to perform the assessment described in this document:

Anthos version | Kubernetes version | CIS Kubernetes Benchmark version  
---|---|---  
1.16.0 | 1.27.4 | V1.23 (1.0.1)  
  
Note that the version numbers for different Benchmarks may not be the same.

## CIS Kubernetes Benchmark

### Accessing the Benchmark

The CIS Kubernetes Benchmark is available on the [CIS website](https://www.cisecurity.org/benchmark/kubernetes/).

### Recommendation Levels

In the CIS Kubernetes Benchmark,

Level | Description  
---|---  
Level 1 | Recommendations intend to: 
* be practical and prudent;
* provide a clear security benefit; and
* not inhibit the utility of the technology beyond acceptable means.  
Level 2 |  Extends the Level 1 profile. Recommendations exhibit one or more of the following characteristics: 
* are intended for environments or use cases where security is paramount;
* acts as defense in depth measure; or
* may negatively inhibit the utility or performance of the technology.  
  
### Assessment Status

An assessment status is included for every recommendation. The assessment status indicates whether the given recommendation can be automated or requires manual steps to implement. Both statuses are equally important and are determined and supported as defined below:

Scoring | Description  
---|---  
Automated | Represents recommendations for which assessment of a technical control can be fully automated and validated to a pass/fail state. Recommendations will include the necessary information to implement automation.   
Manual | Represents recommendations for which assessment of a technical control cannot be fully automated and requires all or some manual steps to validate that the configured state is set as expected. The expected state can vary depending on the environment.   
  
### Evaluation on Google Distributed Cloud

We use the following values to specify the status of Kubernetes Recommendations in Google Distributed Cloud:

Status | Description  
---|---  
Pass | Complies with a Benchmark Recommendation.  
Fail | Does not comply with a Benchmark Recommendation.  
Equivalent Control | Does not comply with the exact terms in the Benchmark Recommendation, but other mechanisms in Google Distributed Cloud exist to provide equivalent security controls.  
Depends on Environment | Google Distributed Cloud does not configure items related to this Recommendation. The user's configuration determines whether their environment complies with a Benchmark Recommendation.  
  
### Google Distributed Cloud Architecture

Google Distributed Cloud supports multiple cluster configurations and cluster types. Every supported cluster type, admin, user, hybrid, and standalone, is evaluated against the CIS benchmark. The following assessments and justifications apply to all supported cluster types. More information on the cluster configurations supported by Google Distributed Cloud can be found in [Choosing deployment models](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/install-prep).

### Status on Google Distributed Cloud

The following sections contain the assessments for new clusters created with the specified version of Google Distributed Cloud. These assessments are an indicator for how new clusters without user workloads perform against the CIS Kubernetes Benchmark. If you deploy your own workloads before auditing Benchmarks yourself, your results may be different.

#### Status of Google Distributed Cloud clusters:

# | Recommendation | Level | Status  
---|---|---|---  
**_1_** | **_cis-1.23_** |  |   
**1.1** | **Control Plane Node Configuration Files** |  |   
1.1.1 | Ensure that the API server pod specification file permissions are set to `644` or more restrictive (Automated) | L1 | Pass  
1.1.2 | Ensure that the API server pod specification file ownership is set to `root:root` (Automated) | L1 | Pass  
1.1.3 | Ensure that the controller manager pod specification file permissions are set to `644` or more restrictive (Automated) | L1 | Pass  
1.1.4 | Ensure that the controller manager pod specification file ownership is set to `root:root` (Automated) | L1 | Pass  
1.1.5 | Ensure that the scheduler pod specification file permissions are set to `644` or more restrictive (Automated) | L1 | Pass  
1.1.6 | Ensure that the scheduler pod specification file ownership is set to `root:root` (Automated) | L1 | Pass  
1.1.7 | Ensure that the etcd pod specification file permissions are set to `644` or more restrictive (Automated) | L1 | Pass  
1.1.8 | Ensure that the etcd pod specification file ownership is set to `root:root` (Automated) | L1 | Pass  
1.1.9 | Ensure that the Container Network Interface file permissions are set to `644` or more restrictive (Manual) | L1 | Equivalent Control  
1.1.10 | Ensure that the Container Network Interface file ownership is set to `root:root` (Manual) | L1 | Pass  
1.1.11 | Ensure that the etcd data directory permissions are set to `700` or more restrictive (Automated) | L1 | Equivalent Control  
1.1.12 | Ensure that the etcd data directory ownership is set to `etcd:etcd` (Automated) | L1 | Equivalent Control  
1.1.13 | Ensure that the admin`.`conf file permissions are set to `600` or more restrictive (Automated) | L1 | Pass  
1.1.14 | Ensure that the admin`.`conf file ownership is set to `root:root` (Automated) | L1 | Pass  
1.1.15 | Ensure that the scheduler`.`conf file permissions are set to `644` or more restrictive (Automated) | L1 | Pass  
1.1.16 | Ensure that the scheduler`.`conf file ownership is set to `root:root` (Automated) | L1 | Equivalent Control  
1.1.17 | Ensure that the controller-manager`.`conf file permissions are set to `644` or more restrictive (Automated) | L1 | Pass  
1.1.18 | Ensure that the controller-manager`.`conf file ownership is set to `root:root` (Automated) | L1 | Equivalent Control  
1.1.19 | Ensure that the Kubernetes PKI directory and file ownership is set to `root:root` (Automated) | L1 | Equivalent Control  
1.1.20 | Ensure that the Kubernetes PKI certificate file permissions are set to `644` or more restrictive (Manual) | L1 | Pass  
1.1.21 | Ensure that the Kubernetes PKI key file permissions are set to `600` (Manual) | L1 | Equivalent Control  
**1.2** | **API Server** |  |   
1.2.1 | Ensure that the `--anonymous-auth` argument is set to false (Manual) | L1 | Warn  
1.2.2 | Ensure that the `--token-auth-file` parameter is not set (Automated) | L1 | Pass  
1.2.3 | Ensure that the `--`DenyServiceExternalIPs is not set (Automated) | L1 | Pass  
1.2.4 | Ensure that the `--kubelet-https` argument is set to true (Automated) | L1 | Pass  
1.2.5 | Ensure that the `--kubelet-client-certificate` and `--kubelet-client-key` arguments are set as appropriate (Automated) | L1 | Pass  
1.2.6 | Ensure that the `--kubelet-certificate-authority` argument is set as appropriate (Automated) | L1 | Pass  
1.2.7 | Ensure that the `--authorization-mode` argument is not set to AlwaysAllow (Automated) | L1 | Pass  
1.2.8 | Ensure that the `--authorization-mode` argument includes Node (Automated) | L1 | Pass  
1.2.9 | Ensure that the `--authorization-mode` argument includes RBAC (Automated) | L1 | Pass  
1.2.10 | Ensure that the admission control plugin EventRateLimit is set (Manual) | L1 | Warn  
1.2.11 | Ensure that the admission control plugin AlwaysAdmit is not set (Automated) | L1 | Pass  
1.2.12 | Ensure that the admission control plugin AlwaysPullImages is set (Manual) | L1 | Warn  
1.2.13 | Ensure that the admission control plugin SecurityContextDeny is set if PodSecurityPolicy is not used (Manual) | L1 | Warn  
1.2.14 | Ensure that the admission control plugin ServiceAccount is set (Automated) | L1 | Pass  
1.2.15 | Ensure that the admission control plugin NamespaceLifecycle is set (Automated) | L1 | Pass  
1.2.16 | Ensure that the admission control plugin NodeRestriction is set (Automated) | L1 | Pass  
1.2.17 | Ensure that the `--secure-port` argument is not set to `0` (Automated) | L1 | Pass  
1.2.18 | Ensure that the `--profiling` argument is set to false (Automated) | L1 | Pass  
1.2.19 | Ensure that the `--audit-log-path` argument is set (Automated) | L1 | Fail  
1.2.20 | Ensure that the `--audit-log-maxage` argument is set to `30` or as appropriate (Automated) | L1 | Fail  
1.2.21 | Ensure that the `--audit-log-maxbackup` argument is set to `10` or as appropriate (Automated) | L1 | Fail  
1.2.22 | Ensure that the `--audit-log-maxsize` argument is set to `100` or as appropriate (Automated) | L1 | Fail  
1.2.23 | Ensure that the `--request-timeout` argument is set as appropriate (Manual) | L1 | Pass  
1.2.24 | Ensure that the `--service-account-lookup` argument is set to true (Automated) | L1 | Pass  
1.2.25 | Ensure that the `--service-account-key-file` argument is set as appropriate (Automated) | L1 | Pass  
1.2.26 | Ensure that the `--etcd-certfile` and `--etcd-keyfile` arguments are set as appropriate (Automated) | L1 | Pass  
1.2.27 | Ensure that the `--tls-cert-file` and `--tls-private-key-file` arguments are set as appropriate (Automated) | L1 | Pass  
1.2.28 | Ensure that the `--client-ca-file` argument is set as appropriate (Automated) | L1 | Pass  
1.2.29 | Ensure that the `--etcd-cafile` argument is set as appropriate (Automated) | L1 | Pass  
1.2.30 | Ensure that the `--encryption-provider-config` argument is set as appropriate (Manual) | L1 | Pass  
1.2.31 | Ensure that encryption providers are appropriately configured (Manual) | L1 | Pass  
1.2.32 | Ensure that the API Server only makes use of Strong Cryptographic Ciphers (Manual) | L1 | Pass  
**1.3** | **Controller Manager** |  |   
1.3.1 | Ensure that the `--terminated-pod-gc-threshold` argument is set as appropriate (Manual) | L1 | Pass  
1.3.2 | Ensure that the `--profiling` argument is set to false (Automated) | L1 | Pass  
1.3.3 | Ensure that the `--use-service-account-credentials` argument is set to true (Automated) | L1 | Pass  
1.3.4 | Ensure that the `--service-account-private-key-file` argument is set as appropriate (Automated) | L1 | Pass  
1.3.5 | Ensure that the `--root-ca-file` argument is set as appropriate (Automated) | L1 | Pass  
1.3.6 | Ensure that the RotateKubeletServerCertificate argument is set to true (Automated) | L2 | Pass  
1.3.7 | Ensure that the `--bind-address` argument is set to `127.0.0.1` (Automated) | L1 | Pass  
**1.4** | **Scheduler** |  |   
1.4.1 | Ensure that the `--profiling` argument is set to false (Automated) | L1 | Pass  
1.4.2 | Ensure that the `--bind-address` argument is set to `127.0.0.1` (Automated) | L1 | Pass  
**_2_** | **_cis-1.23_** |  |   
**2** | **Etcd Node Configuration** |  |   
2.1 | Ensure that the `--cert-file` and `--key-file` arguments are set as appropriate (Automated) | L1 | Pass  
2.2 | Ensure that the `--client-cert-auth` argument is set to true (Automated) | L1 | Pass  
2.3 | Ensure that the `--auto-tls` argument is not set to true (Automated) | L1 | Pass  
2.4 | Ensure that the `--peer-cert-file` and `--peer-key-file` arguments are set as appropriate (Automated) | L1 | Pass  
2.5 | Ensure that the `--peer-client-cert-auth` argument is set to true (Automated) | L1 | Pass  
2.6 | Ensure that the `--peer-auto-tls` argument is not set to true (Automated) | L1 | Pass  
2.7 | Ensure that a unique Certificate Authority is used for etcd (Manual) | L2 | Pass  
**_3_** | **_cis-1.23_** |  |   
**3.1** | **Authentication and Authorization** |  |   
3.1.1 | Client certificate authentication should not be used for users (Manual) | L2 | Pass  
**3.2** | **Logging** |  |   
3.2.1 | Ensure that a minimal audit policy is created (Manual) | L1 | Pass  
3.2.2 | Ensure that the audit policy covers key security concerns (Manual) | L2 | Equivalent Control  
**_4_** | **_cis-1.23_** |  |   
**4.1** | **Worker Node Configuration Files** |  |   
4.1.1 | Ensure that the kubelet service file permissions are set to `644` or more restrictive (Automated) | L1 | Pass  
4.1.2 | Ensure that the kubelet service file ownership is set to `root:root` (Automated) | L1 | Pass  
4.1.3 | If proxy kubeconfig file exists ensure permissions are set to `644` or more restrictive (Manual) | L1 | Pass  
4.1.4 | If proxy kubeconfig file exists ensure ownership is set to `root:root` (Manual) | L1 | Pass  
4.1.5 | Ensure that the `--kubeconfig` kubelet`.`conf file permissions are set to `644` or more restrictive (Automated) | L1 | Pass  
4.1.6 | Ensure that the `--kubeconfig` kubelet`.`conf file ownership is set to `root:root` (Automated) | L1 | Pass  
4.1.7 | Ensure that the certificate authorities file permissions are set to `644` or more restrictive (Manual) | L1 | Pass  
4.1.8 | Ensure that the client certificate authorities file ownership is set to `root:root` (Manual) | L1 | Pass  
4.1.9 | Ensure that the kubelet `--config` configuration file has permissions set to `644` or more restrictive (Automated) | L1 | Pass  
4.1.10 | Ensure that the kubelet `--config` configuration file ownership is set to `root:root` (Automated) | L1 | Pass  
**4.2** | **Kubelet** |  |   
4.2.1 | Ensure that the `--anonymous-auth` argument is set to false (Automated) | L1 | Pass  
4.2.2 | Ensure that the `--authorization-mode` argument is not set to AlwaysAllow (Automated) | L1 | Pass  
4.2.3 | Ensure that the `--client-ca-file` argument is set as appropriate (Automated) | L1 | Pass  
4.2.4 | Ensure that the `--read-only-port` argument is set to `0` (Manual) | L1 | Fail  
4.2.5 | Ensure that the `--streaming-connection-idle-timeout` argument is not set to `0` (Manual) | L1 | Pass  
4.2.6 | Ensure that the `--protect-kernel-defaults` argument is set to true (Automated) | L1 | Fail  
4.2.7 | Ensure that the `--make-iptables-util-chains` argument is set to true (Automated) | L1 | Pass  
4.2.8 | Ensure that the `--hostname-override` argument is not set (Manual) | L1 | Pass  
4.2.9 | Ensure that the `--event-qps` argument is set to `0` or a level which ensures appropriate event capture (Manual) | L2 | Warn  
4.2.10 | Ensure that the `--tls-cert-file` and `--tls-private-key-file` arguments are set as appropriate (Manual) | L1 | Equivalent Control  
4.2.11 | Ensure that the `--rotate-certificates` argument is not set to false (Automated) | L1 | Pass  
4.2.12 | Verify that the RotateKubeletServerCertificate argument is set to true (Manual) | L1 | Pass  
4.2.13 | Ensure that the Kubelet only makes use of Strong Cryptographic Ciphers (Manual) | L1 | Equivalent Control  
  
##### Descriptions of Failures and Equivalent Controls for Google Distributed Cloud admin cluster:

# | Recommendation | Level | Status | Value | Justification  
---|---|---|---|---|---  
1.1.9 | Ensure that the Container Network Interface file permissions are set to `644` or more restrictive (Manual) | L1 | Equivalent Control | `755` | Anthos clusters on bare metal Container Network Interface path is `/opt/cni/bin`, and its permission is set to `755` for the normal cluster operation.  
1.1.11 | Ensure that the etcd data directory permissions are set to `700` or more restrictive (Automated) | L1 | Equivalent Control | `755` | The etcd data directory has the default `755` permissions but its subdirectories are `700`.  
1.1.12 | Ensure that the etcd data directory ownership is set to `etcd:etcd` (Automated) | L1 | Equivalent Control | `2003:2003` | The etcd data directory, /var/lib/etcd, is owned by `2003:2003` as the result of [rootless control-plane](https://github.com/kubernetes/enhancements/tree/master/keps/sig-cluster-lifecycle/kubeadm/2568-kubeadm-non-root-control-plane) for enhanced security.  
1.1.16 | Ensure that the scheduler`.`conf file ownership is set to `root:root` (Automated) | L1 | Equivalent Control | `2002:2002` | Anthos clusters on bare metal, starting release 1.9.0, implements [rootless control-plane](https://github.com/kubernetes/enhancements/tree/master/keps/sig-cluster-lifecycle/kubeadm/2568-kubeadm-non-root-control-plane) for enhanced security.  
1.1.18 | Ensure that the controller-manager`.`conf file ownership is set to `root:root` (Automated) | L1 | Equivalent Control | `2001:2001` | Anthos clusters on bare metal, starting release 1.9.0, implements [rootless control-plane](https://github.com/kubernetes/enhancements/tree/master/keps/sig-cluster-lifecycle/kubeadm/2568-kubeadm-non-root-control-plane) for enhanced security.  
1.1.19 | Ensure that the Kubernetes PKI directory and file ownership is set to `root:root` (Automated) | L1 | Equivalent Control | `variable:variable` | Anthos clusters on bare metal, starting release 1.9.0, implements [rootless control-plane](https://github.com/kubernetes/enhancements/tree/master/keps/sig-cluster-lifecycle/kubeadm/2568-kubeadm-non-root-control-plane) for enhanced security.  
1.1.21 | Ensure that the Kubernetes PKI key file permissions are set to `600` (Manual) | L1 | Equivalent Control | `600~640` | Anthos clusters on bare metal, starting release 1.9.0, implements [rootless control-plane](https://github.com/kubernetes/enhancements/tree/master/keps/sig-cluster-lifecycle/kubeadm/2568-kubeadm-non-root-control-plane) for enhanced security.  
1.2.1 | Ensure that the `--anonymous-auth` argument is set to false (Manual) | L1 | Warn | not set | Some Anthos clusters on bare metal operations, such as HA, require anonymous-auth be enabled.  
1.2.10 | Ensure that the admission control plugin EventRateLimit is set (Manual) | L1 | Warn |  |   
1.2.12 | Ensure that the admission control plugin AlwaysPullImages is set (Manual) | L1 | Warn | not set | The AlwaysPullImages admission controller provides some protection for private registry images in noncooperative multitenant clusters, at the cost of making container registries a single-point-of-failure for creating new Pods across the entire cluster. Anthos clusters on bare metal does not enable the AlwaysPullImages admission controller, which leaves it up to cluster admins to implement admission policy to make this tradeoff for themselves.  
1.2.13 | Ensure that the admission control plugin SecurityContextDeny is set if PodSecurityPolicy is not used (Manual) | L1 | Warn | not set | Anthos clusters on bare metal does not enable Pod Security Policy. Pod Security Admission is enabled in Kubernetes 1.23 clusters by default, see <https://kubernetes.io/docs/concepts/security/pod-security-admission/>  
1.2.19 | Ensure that the `--audit-log-path` argument is set (Automated) | L1 | Fail | not set by default; set `/var/log/apiserver/audit.log` only if Cloud Audit Logging is disabled | Anthos clusters on bare metal clusters, by default, send Kubernetes API server audit logs to Google Cloud.  
1.2.20 | Ensure that the `--audit-log-maxage` argument is set to `30` or as appropriate (Automated) | L1 | Fail | not set by default; set `30` only if Cloud Audit Logging is disabled | Anthos clusters on bare metal clusters, by default, send Kubernetes API server audit logs to Google Cloud.  
1.2.21 | Ensure that the `--audit-log-maxbackup` argument is set to `10` or as appropriate (Automated) | L1 | Fail | not set by default, set `10` only if Cloud Audit Logging is disabled | Anthos clusters on bare metal clusters, by default, send Kubernetes API server audit logs to Google Cloud.  
1.2.22 | Ensure that the `--audit-log-maxsize` argument is set to `100` or as appropriate (Automated) | L1 | Fail | not set by default, set `100` only if Cloud Audit Logging is disabled | Anthos clusters on bare metal clusters, by default, send Kubernetes API server audit logs to Google Cloud.  
3.2.2 | Ensure that the audit policy covers key security concerns (Manual) | L2 | Equivalent Control | not set | Anthos clusters on bare metal captures audit logs but does not use these flags for auditing, more on [logging and monitoring](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/log-monitoring).  
4.2.4 | Ensure that the `--read-only-port` argument is set to `0` (Manual) | L1 | Fail | 10255 | Anthos clusters on bare metal currently sets the --read-only-port argument to 10255 for collecting metrics from kubelet.  
4.2.6 | Ensure that the `--protect-kernel-defaults` argument is set to true (Automated) | L1 | Fail | `false` | Anthos on Bare Metal cluster machines do not protect kernel defaults from Kubernetes, as customer workloads may want to modify these.  
4.2.9 | Ensure that the `--event-qps` argument is set to `0` or a level which ensures appropriate event capture (Manual) | L2 | Warn | not set | Events are Kubernetes objects stored in etcd. To avoid overwhelming etcd they are only kept for one hour, and are not an appropriate security auditing mechanism. Allowing unlimited events as suggested in this control exposes the cluster to unnecessary DoS risk and contradicts the recommendation to use admission EventRateLimits. Security relevant events that need permanent storage should be sent to logs.  
4.2.10 | Ensure that the `--tls-cert-file` and `--tls-private-key-file` arguments are set as appropriate (Manual) | L1 | Equivalent Control | not set | Anthos clusters on bare metal manages kubelet server TLS using the --rotate-server-certificates flag.  
4.2.13 | Ensure that the Kubelet only makes use of Strong Cryptographic Ciphers (Manual) | L1 | Equivalent Control |  | In Anthos clusters on bare metal nodes, kubelet uses the default Go cipher suites. Anthos clusters on bare metal does not provide config options for user to customize cipher suites selection. Note that modern clients negotiate cipher suites and will not use the weak ciphers if strong ciphers are mutually available.  
  
## How to audit Benchmarks

Specific instructions for auditing each Recommendation is available as part of the relevant CIS Benchmark. However, you may wish to automate some of these checks to simplify the verification of these controls in your environment. The tools listed below can help with this.

### Automated auditing of the CIS Kubernetes Benchmark

You can use an open-source tool `[kube-bench](https://github.com/aquasecurity/kube-bench)` to test your cluster configuration against the CIS Kubernetes Benchmark.

Make sure to specify the appropriate version, for example,
    
    
    kube-bench node --benchmark cis-1.23
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v9ce9cb5b22b62a465ff52c45061a0a6a2d86a80b685e9aa8a182b203fdfbf420/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体
  * 日本語
  * 한국어


