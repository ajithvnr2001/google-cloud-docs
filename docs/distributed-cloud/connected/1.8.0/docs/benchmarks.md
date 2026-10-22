---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/benchmarks/
title: CIS Benchmarks \u00a0|\u00a0 Google Distributed Cloud connected, version 1.8.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:08.660571+00:00
---

# CIS Benchmarks  |  Google Distributed Cloud connected, version 1.8.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/benchmarks/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/apis)



Send feedback 

#  CIS Benchmarks Stay organized with collections  Save and categorize content based on your preferences. 

This page introduces the CIS Kubernetes Benchmark, provides an assessment, and explains what Google Distributed Cloud connected does to address the recommendations.

## The CIS Benchmark

The Center for Internet Security (CIS) releases benchmarks for best practice security recommendations. The [CIS Kubernetes Benchmark](https://www.cisecurity.org/benchmark/kubernetes/) provides a set of recommendations for configuring Kubernetes to support a strong security posture. The Benchmark is tied to a specific Kubernetes release. The CIS Kubernetes Benchmark is written for the open source Kubernetes distribution and intended to be as universally applicable across distributions as possible.

### Versions

The following table lists the versions of Distributed Cloud connected, Kubernetes, and the CIS Kubernetes Benchmark that were used to perform the assessment described in this document:

Distributed Cloud connected version | Kubernetes version | CIS Kubernetes Benchmark version  
---|---|---  
1.4.0 - Local Control Plane | 1.25 | 1.70  
  
### Accessing the Benchmark

The CIS Kubernetes Benchmark is available on the [CIS website](https://www.cisecurity.org/benchmark/kubernetes/).

## Recommendation levels

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
  
## Assessment status

An assessment status is included for every recommendation. The assessment status indicates whether the given recommendation can be automated or requires manual steps to implement. Both statuses are equally important and are determined and supported as defined below:

Scoring | Description  
---|---  
Automated | Represents recommendations for which assessment of a technical control can be fully automated and validated to a pass/fail state. Recommendations will include the necessary information to implement automation.   
Manual | Represents recommendations for which assessment of a technical control cannot be fully automated and requires all or some manual steps to validate that the configured state is set as expected. The expected state can vary depending on the environment.   
  
### Status on Distributed Cloud connected local control plane clusters

# | Recommendation | Level | Status  
---|---|---|---  
**1** | **Control Plane Security Configuration** |  |   
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
1.1.13 | Ensure that the `admin.conf` file permissions are set to `600` or more restrictive (Automated) | L1 | Pass  
1.1.14 | Ensure that the `admin.conf` file ownership is set to `root:root` (Automated) | L1 | Pass  
1.1.15 | Ensure that the `scheduler.conf` file permissions are set to `644` or more restrictive (Automated) | L1 | Pass  
1.1.16 | Ensure that the `scheduler.conf` file ownership is set to `root:root` (Automated) | L1 | Equivalent Control  
1.1.17 | Ensure that the `controller-manager.conf` file permissions are set to `644` or more restrictive (Automated) | L1 | Pass  
1.1.18 | Ensure that the `controller-manager.conf` file ownership is set to `root:root` (Automated) | L1 | Equivalent Control  
1.1.19 | Ensure that the Kubernetes PKI directory and file ownership is set to `root:root` (Automated) | L1 | Equivalent Control  
1.1.20 | Ensure that the Kubernetes PKI certificate file permissions are set to `644` or more restrictive (Manual) | L1 | Equivalent Control  
1.1.21 | Ensure that the Kubernetes PKI key file permissions are set to `600` (Manual) | L1 | Pass  
**1.2** | **API Server** |  |   
1.2.1 | Ensure that the `--anonymous-auth` argument is set to false (Manual) | L1 | Pass  
1.2.2 | Ensure that the `--token-auth-file` parameter is not set (Automated) | L1 | Pass  
1.2.3 | Ensure that the `--DenyServiceExternalIPs` is not set (Automated) | L1 | Fail  
1.2.4 | Ensure that the `--kubelet-client-certificate` and `--kubelet-client-key` arguments are set as appropriate (Automated) | L1 | Pass  
1.2.5 | Ensure that the `--kubelet-certificate-authority` argument is set as appropriate (Automated) | L1 | Pass  
1.2.6 | Ensure that the `--authorization-mode` argument is not set to AlwaysAllow (Automated) | L1 | Pass  
1.2.7 | Ensure that the `--authorization-mode` argument includes Node (Automated) | L1 | Pass  
1.2.8 | Ensure that the `--authorization-mode` argument includes RBAC (Automated) | L1 | Fail  
1.2.9 | Ensure that the admission control plugin EventRateLimit is set (Manual) | L1 | Pass  
1.2.10 | Ensure that the admission control plugin AlwaysAdmit is not set (Automated) | L1 | Pass  
1.2.11 | Ensure that the admission control plugin AlwaysPullImages is set (Manual) | L1 | Fail  
1.2.12 | Ensure that the admission control plugin SecurityContextDeny is set if PodSecurityPolicy is not used (Manual) | L1 | Warn  
1.2.13 | Ensure that the admission control plugin ServiceAccount is set (Automated) | L1 | Pass  
1.2.14 | Ensure that the admission control plugin NamespaceLifecycle is set (Automated) | L1 | Pass  
1.2.15 | Ensure that the admission control plugin NodeRestriction is set (Automated) | L1 | Pass  
1.2.16 | Ensure that the `--secure-port` argument is not set to `0` (Automated) | L1 | Pass  
1.2.17 | Ensure that the `--profiling` argument is set to false (Automated) | L1 | Pass  
1.2.18 | Ensure that the `--audit-log-path` argument is set (Automated) | L1 | Fail  
1.2.19 | Ensure that the `--audit-log-maxage` argument is set to `30` or as appropriate (Automated) | L1 | Fail  
1.2.20 | Ensure that the `--audit-log-maxbackup` argument is set to `10` or as appropriate (Automated) | L1 | Fail  
1.2.21 | Ensure that the `--audit-log-maxsize` argument is set to `100` or as appropriate (Automated) | L1 | Fail  
1.2.22 | Ensure that the `--request-timeout` argument is set as appropriate (Manual) | L1 | Fail  
1.2.23 | Ensure that the `--service-account-lookup` argument is set to true (Automated) | L1 | Pass  
1.2.24 | Ensure that the `--service-account-key-file` argument is set as appropriate (Automated) | L1 | Pass  
1.2.25 | Ensure that the `--etcd-certfile` and `--etcd-keyfile` arguments are set as appropriate (Automated) | L1 | Pass  
1.2.26 | Ensure that the `--tls-cert-file` and `--tls-private-key-file` arguments are set as appropriate (Automated) | L1 | Pass  
1.2.27 | Ensure that the `--client-ca-file` argument is set as appropriate (Automated) | L1 | Pass  
1.2.28 | Ensure that the `--etcd-cafile` argument is set as appropriate (Automated) | L1 | Pass  
1.2.29 | Ensure that the `--encryption-provider-config` argument is set as appropriate (Manual) | L1 | Pass  
1.2.30 | Ensure that encryption providers are appropriately configured (Manual) | L1 | Pass  
1.2.31 | Ensure that the API Server only makes use of Strong Cryptographic Ciphers (Manual) | L1 | Pass  
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
**2** | ** `etcd` Node Configuration** |  |   
2.1 | Ensure that the `--cert-file` and `--key-file` arguments are set as appropriate (Automated) | L1 | Pass  
2.2 | Ensure that the `--client-cert-auth` argument is set to true (Automated) | L1 | Pass  
2.3 | Ensure that the `--auto-tls` argument is not set to true (Automated) | L1 | Pass  
2.4 | Ensure that the `--peer-cert-file` and `--peer-key-file` arguments are set as appropriate (Automated) | L1 | Pass  
2.5 | Ensure that the `--peer-client-cert-auth` argument is set to true (Automated) | L1 | Pass  
2.6 | Ensure that the `--peer-auto-tls` argument is not set to true (Automated) | L1 | Pass  
2.7 | Ensure that a unique Certificate Authority is used for etcd (Manual) | L2 | Pass  
**3** | **Control Plane Configuration** |  |   
**3.1** | **Authentication and Authorization** |  |   
3.1.1 | Client certificate authentication should not be used for users (Manual) | L2 | Pass  
**3.2** | **Logging** |  |   
3.2.1 | Ensure that a minimal audit policy is created (Manual) | L1 | Pass  
3.2.2 | Ensure that the audit policy covers key security concerns (Manual) | L2 | Fail  
**4** | **Worker Node Security Configuration** |  |   
**4.1** | **Worker Node Configuration Files** |  |   
4.1.1 | Ensure that the kubelet service file permissions are set to `644` or more restrictive (Automated) | L1 | Fail  
4.1.2 | Ensure that the kubelet service file ownership is set to `root:root` (Automated) | L1 | Pass  
4.1.3 | If proxy kubeconfig file exists ensure permissions are set to `644` or more restrictive (Manual) | L1 | Pass  
4.1.4 | If proxy kubeconfig file exists ensure ownership is set to `root:root` (Manual) | L1 | Pass  
4.1.5 | Ensure that the `--kubeconfig` `kubelet.conf` file permissions are set to `644` or more restrictive (Automated) | L1 | Pass  
4.1.6 | Ensure that the `--kubeconfig` `kubelet.conf` file ownership is set to `root:root` (Automated) | L1 | Pass  
4.1.7 | Ensure that the certificate authorities file permissions are set to `644` or more restrictive (Manual) | L1 | Fail  
4.1.8 | Ensure that the client certificate authorities file ownership is set to `root:root` (Manual) | L1 | Pass  
4.1.9 | Ensure that the kubelet `--config` configuration file has permissions set to `644` or more restrictive (Automated) | L1 | Fail  
4.1.10 | Ensure that the kubelet `--config` configuration file ownership is set to `root:root` (Automated) | L1 | Pass  
**4.2** | **Kubelet** |  |   
4.2.1 | Ensure that the `--anonymous-auth` argument is set to false (Automated) | L1 | Pass  
4.2.2 | Ensure that the `--authorization-mode` argument is not set to AlwaysAllow (Automated) | L1 | Pass  
4.2.3 | Ensure that the `--client-ca-file` argument is set as appropriate (Automated) | L1 | Pass  
4.2.4 | Ensure that the `--read-only-port` argument is set to `0` (Manual) | L1 | Fail  
4.2.5 | Ensure that the `--streaming-connection-idle-timeout` argument is not set to `0` (Manual) | L1 | Pass  
4.2.6 | Ensure that the `--protect-kernel-defaults` argument is set to true (Automated) | L1 | Pass  
4.2.7 | Ensure that the `--make-iptables-util-chains` argument is set to true (Automated) | L1 | Pass  
4.2.8 | Ensure that the `--hostname-override` argument is not set (Manual) | L2 | Pass  
4.2.9 | Ensure that the `--event-qps` argument is set to `0` or a level which ensures appropriate event capture (Manual) | L1 | Equivalent Control  
4.2.10 | Ensure that the `--tls-cert-file` and `--tls-private-key-file` arguments are set as appropriate (Manual) | L1 | Pass  
4.2.11 | Ensure that the `--rotate-certificates` argument is not set to false (Automated) | L1 | Pass  
4.2.12 | Verify that the RotateKubeletServerCertificate argument is set to true (Manual) | L1 | Pass  
4.2.13 | Ensure that the Kubelet only makes use of Strong Cryptographic Ciphers (Manual) | L1 | Fail  
  
## Failures and equivalent controls for Distributed Cloud connected local control plane clusters

# | Recommendation | Level | Status | Value | Justification  
---|---|---|---|---|---  
**1** | **Control Plane Security Configuration** |  |  |  |   
1.1.9 | Ensure that the Container Network Interface file permissions are set to `644` or more restrictive (Manual) | L1 | Equivalent Control | `755` | None.  
1.1.11 | Ensure that the `etcd` data directory permissions are set to `700` or more restrictive (Automated) | L1 | Equivalent Control | `755` | The `etcd` data directory has the default `755` permissions but its subdirectories use `700`.  
1.1.12 | Ensure that the `etcd` data directory ownership is set to `etcd:etcd` (Automated) | L1 | Equivalent Control | `2003:2003` | The `etcd` data directory, `/var/lib/etcd`, is owned by `2003:2003` due to [rootless control-plane](https://github.com/kubernetes/enhancements/tree/master/keps/sig-cluster-lifecycle/kubeadm/2568-kubeadm-non-root-control-plane) for enhanced security.  
1.1.16 | Ensure that the `scheduler.conf` file ownership is set to `root:root` (Automated) | L1 | Equivalent Control | `2002:2002` | `scheduler.conf` is owned by `2002:2002` due to [rootless control-plane](https://github.com/kubernetes/enhancements/tree/master/keps/sig-cluster-lifecycle/kubeadm/2568-kubeadm-non-root-control-plane) for enhanced security.  
1.1.18 | Ensure that the `controller-manager.conf` file ownership is set to `root:root` (Automated) | L1 | Equivalent Control | `2001:2001` | `controller-manager.conf` is owned by `2001:2001` due to [rootless control-plane](https://github.com/kubernetes/enhancements/tree/master/keps/sig-cluster-lifecycle/kubeadm/2568-kubeadm-non-root-control-plane) for enhanced security.  
1.1.19 | Ensure that the Kubernetes PKI directory and file ownership is set to `root:root` (Automated) | L1 | Equivalent Control | Varies | The PKI directory, `/etc/kubernetes/pki`, is owned by `root:root`; the files inside the directory have various owners. This is due to [rootless control-plane](https://github.com/kubernetes/enhancements/tree/master/keps/sig-cluster-lifecycle/kubeadm/2568-kubeadm-non-root-control-plane) for enhanced security.  
1.1.20 | Ensure that the Kubernetes PKI certificate file permissions are set to `644` or more restrictive (Manual) | L1 | Equivalent Control | `644` | This is due to [rootless control-plane](https://github.com/kubernetes/enhancements/tree/master/keps/sig-cluster-lifecycle/kubeadm/2568-kubeadm-non-root-control-plane) for enhanced security.  
**1.2** | **API Server** |  |  |  |   
1.2.3 | Ensure that the `--DenyServiceExternalIPs` is not set (Automated) | L1 | Fail |  |   
1.2.9 | Ensure that the `--authorization-mode` argument includes RBAC (Automated) | L1 | Fail |  | Event Rate Limit admission controller is a Kubernetes alpha feature. Google Distributed Cloud does not support non-GA features.  
1.2.11 | Ensure that the admission control plugin `AlwaysAdmit` is not set (Automated) | L1 | Fail |  |   
1.2.12 | Ensure that the admission control plugin `AlwaysPullImages` is set (Manual) | L1 | Fail | The `AlwaysPullImages` admission controller provides some protection for private registry images in non-cooperative multitenant clusters at the cost of making container registries single points of failure for creating new pods across the entire cluster. Distributed Cloud clusters do not enable the `AlwaysPullImages` admission controller, which leaves it up to cluster administrators to implement admission policy to make this tradeoff for themselves. |   
1.2.18 | Ensure that the `--audit-log-path` argument is set (Automated) | L1 | Fail |  | Distributed Cloud captures audit logs but does not use this flag for auditing. See [Audit Logging](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/audit-logging) for more information.  
1.2.19 | Ensure that the `--audit-log-maxage` argument is set to `30` or as appropriate (Automated) | L1 | Fail |  | Distributed Cloud captures audit logs but does not use this flag for auditing. See [Audit Logging](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/audit-logging) for more information.  
1.2.20 | Ensure that the `--audit-log-maxbackup` argument is set to `10` or as appropriate (Automated) | L1 | Fail |  | Distributed Cloud connected captures audit logs but does not use this flag for auditing. See [Audit Logging](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/audit-logging) for more information.  
1.2.21 | Ensure that the `--audit-log-maxsize` argument is set to `100` or as appropriate (Automated) | L1 | Fail |  | Distributed Cloud connected captures audit logs but does not use this flag for auditing. See [Audit Logging](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/audit-logging) for more information.  
1.2.22 | Ensure that the `--request-timeout` argument is set as appropriate (Manual) | L1 | Fail |  | Distributed Cloud connected captures audit logs but does not use this flag for auditing. See [Audit Logging](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/audit-logging) for more information.  
**3** | **Control Plane Configuration** |  |  |  |   
3.2.2 | Ensure that the audit policy covers key security concerns (Manual) | L2 | Fail |  |   
**4** | **Worker Node Security Configuration** |  |  |  |   
4.1.1 | Ensure that the kubelet service file permissions are set to `644` or more restrictive (Automated) | L1 | Fail | `755` |   
4.1.7 | Ensure that the certificate authorities file permissions are set to `644` or more restrictive (Manual) | L1 | Fail |  |   
4.1.9 | Ensure that the kubelet `--config` configuration file has permissions set to `644` or more restrictive (Automated) | L1 | Fail | `644` |   
4.2.4 | Ensure that the `--read-only-port` argument is set to `0` (Manual) | L1 | Fail |  | Distributed Cloud connected clusters set the `--read-only-port` argument to `10255` for collecting kubelet metrics.  
4.2.9 | Ensure that the `--event-qps` argument is set to `0` or a level which ensures appropriate event capture (Manual) | L1 | Equivalent Control |  | Distributed Cloud clusters manage kubelet server TLS using the `–rotate-server-certificates` flag.  
4.2.13 | Ensure that the Kubelet only makes use of Strong Cryptographic Ciphers (Manual) | L1 | Fail |  |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
