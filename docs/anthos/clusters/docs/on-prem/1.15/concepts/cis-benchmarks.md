---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/concepts/cis-benchmarks/
title: CIS Kubernetes Benchmark \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:33.732788+00:00
---

# CIS Kubernetes Benchmark  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/concepts/cis-benchmarks/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  CIS Kubernetes Benchmark Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/concepts/cis-benchmarks)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/concepts/cis-benchmarks)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This document introduces the CIS Kubernetes Benchmark, explains how to audit your compliance with the benchmark, and explains what Google Distributed Cloud configures when you cannot implement a recommendation yourself.

## About the CIS Benchmarks

The Center for Internet Security (CIS) releases benchmarks for best practice security recommendations. The [CIS Kubernetes Benchmark](https://www.cisecurity.org/benchmark/kubernetes/) provides a set of recommendations for configuring Kubernetes to support a strong security posture. The Benchmark is tied to a specific Kubernetes release. The CIS Kubernetes Benchmark is written for the open source Kubernetes distribution and intended to be as universally applicable across distributions as possible.

### Versions

The version numbers for different Benchmarks might not be the same. This document refers to the following versions:

Anthos version | Kubernetes version | CIS Kubernetes Benchmark version  
---|---|---  
1.15.3 | 1.26.2 | 1.7  
  
## Use the CIS Kubernetes Benchmark

### Access the benchmark

The CIS Kubernetes Benchmark is available on the [CIS website](https://www.cisecurity.org/benchmark/kubernetes/).

### Recommendation levels

The following table describes the recommendation levels in the CIS Kubernetes Benchmark.

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
  
### Assessment status

An assessment status is included for every recommendation. The assessment status indicates whether the given recommendation can be automated or requires manual steps to implement. Both statuses are equally important and are determined and supported as defined in the following table.

Scoring | Description  
---|---  
Automated | Represents recommendations for which assessment of a technical control can be fully automated and validated to a pass/fail state. Recommendations include the necessary information to implement automation.   
Manual | Represents recommendations for which assessment of a technical control cannot be fully automated and requires all or some manual steps to validate that the configured state is set as expected. The expected state can vary depending on the environment.   
  
### Evaluation on Google Distributed Cloud

We use the following values to specify the status of Kubernetes Recommendations in Google Distributed Cloud.

Status | Description  
---|---  
Pass | Complies with a Benchmark Recommendation.  
Fail | Does not comply with a Benchmark Recommendation.  
Equivalent Control | Does not comply with the exact terms in the Benchmark Recommendation, but other mechanisms in Google Distributed Cloud exist to provide equivalent security controls.  
Depends on Environment | Google Distributed Cloud does not configure items related to this Recommendation. The user's configuration determines whether their environment complies with a Benchmark Recommendation.  
  
### Google Distributed Cloud architecture

Google Distributed Cloud uses an _admin cluster_ to manage one or more _user clusters_ , which run actual Kubernetes workloads. More information about this architecture can be found in the [Google Distributed Cloud overview](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview#architecture). The configuration of both admin and user clusters is evaluated against the following benchmarks.

### Status on Google Distributed Cloud

When creating a new cluster on Google Distributed Cloud with the specified version, here's how it performs against the CIS Kubernetes Benchmark. CIS benchmark reports are automatically generated by scripts. The scripts are run on new clusters that aren't running any user workloads. If you install your own workloads and run the scripts, the report may be different.

#### Status of Google Distributed Cloud admin cluster

# | Recommendation | Level | Status  
---|---|---|---  
**_1_** | **_Control Plane Security Configuration_** |  |   
**1.1** | **Control Plane Node Configuration Files** |  |   
1.1.1 | Ensure that the API server pod specification file permissions are set to `600` or more restrictive (Automated) | L1 | Equivalent Control  
1.1.2 | Ensure that the API server pod specification file ownership is set to `root:root` (Automated) | L1 | Pass  
1.1.3 | Ensure that the controller manager pod specification file permissions are set to `600` or more restrictive (Automated) | L1 | Equivalent Control  
1.1.4 | Ensure that the controller manager pod specification file ownership is set to `root:root` (Automated) | L1 | Pass  
1.1.5 | Ensure that the scheduler pod specification file permissions are set to `600` or more restrictive (Automated) | L1 | Equivalent Control  
1.1.6 | Ensure that the scheduler pod specification file ownership is set to `root:root` (Automated) | L1 | Pass  
1.1.7 | Ensure that the etcd pod specification file permissions are set to `600` or more restrictive (Automated) | L1 | Equivalent Control  
1.1.8 | Ensure that the etcd pod specification file ownership is set to `root:root` (Automated) | L1 | Pass  
1.1.9 | Ensure that the Container Network Interface file permissions are set to `600` or more restrictive (Manual) | L1 | Pass  
1.1.10 | Ensure that the Container Network Interface file ownership is set to `root:root` (Manual) | L1 | Pass  
1.1.11 | Ensure that the etcd data directory permissions are set to `700` or more restrictive (Automated) | L1 | Pass  
1.1.12 | Ensure that the etcd data directory ownership is set to `etcd:etcd` (Automated) | L1 | Equivalent Control  
1.1.13 | Ensure that the admin.conf file permissions are set to `600` or more restrictive (Automated) | L1 | Pass  
1.1.14 | Ensure that the admin.conf file ownership is set to `root:root` (Automated) | L1 | Pass  
1.1.15 | Ensure that the scheduler.conf file permissions are set to `600` or more restrictive (Automated) | L1 | Pass  
1.1.16 | Ensure that the scheduler.conf file ownership is set to `root:root` (Automated) | L1 | Equivalent Control  
1.1.17 | Ensure that the controller-manager.conf file permissions are set to `600` or more restrictive (Automated) | L1 | Pass  
1.1.18 | Ensure that the controller-manager.conf file ownership is set to `root:root` (Automated) | L1 | Equivalent Control  
1.1.19 | Ensure that the Kubernetes PKI directory and file ownership is set to `root:root` (Automated) | L1 | Pass  
1.1.20 | Ensure that the Kubernetes PKI certificate file permissions are set to `600` or more restrictive (Manual) | L1 | Pass  
1.1.21 | Ensure that the Kubernetes PKI key file permissions are set to `600` (Manual) | L1 | Pass  
**1.2** | **API Server** |  |   
1.2.1 | Ensure that the `--anonymous-auth` argument is set to false (Manual) | L1 | Pass  
1.2.2 | Ensure that the `--token-auth-file` parameter is not set (Automated) | L1 | Pass  
1.2.3 | Ensure that the `--DenyServiceExternalIPs` is set (Manual) | L1 | Warn  
1.2.4 | Ensure that the `--kubelet-client-certificate` and `--kubelet-client-key` arguments are set as appropriate (Automated) | L1 | Pass  
1.2.5 | Ensure that the `--kubelet-certificate-authority` argument is set as appropriate (Automated) | L1 | Pass  
1.2.6 | Ensure that the `--authorization-mode` argument is not set to AlwaysAllow (Automated) | L1 | Pass  
1.2.7 | Ensure that the `--authorization-mode` argument includes Node (Automated) | L1 | Pass  
1.2.8 | Ensure that the `--authorization-mode` argument includes RBAC (Automated) | L1 | Pass  
1.2.9 | Ensure that the admission control plugin EventRateLimit is set (Manual) | L1 | Warn  
1.2.10 | Ensure that the admission control plugin AlwaysAdmit is not set (Automated) | L1 | Pass  
1.2.11 | Ensure that the admission control plugin AlwaysPullImages is set (Manual) | L1 | Depends On Environment  
1.2.12 | Ensure that the admission control plugin SecurityContextDeny is set if PodSecurityPolicy is not used (Manual) | L1 | Equivalent Control  
1.2.13 | Ensure that the admission control plugin ServiceAccount is set (Automated) | L1 | Pass  
1.2.14 | Ensure that the admission control plugin NamespaceLifecycle is set (Automated) | L1 | Pass  
1.2.15 | Ensure that the admission control plugin NodeRestriction is set (Automated) | L1 | Pass  
1.2.16 | Ensure that the `--secure-port` argument is not set to `0` \- NoteThis recommendation is obsolete and will be deleted per the consensus process (Manual) | L1 | Pass  
1.2.17 | Ensure that the `--profiling` argument is set to false (Automated) | L1 | Pass  
1.2.18 | Ensure that the `--audit-log-path` argument is set (Automated) | L1 | Pass  
1.2.19 | Ensure that the `--audit-log-maxage` argument is set to `30` or as appropriate (Automated) | L1 | Equivalent Control  
1.2.20 | Ensure that the `--audit-log-maxbackup` argument is set to `10` or as appropriate (Automated) | L1 | Pass  
1.2.21 | Ensure that the `--audit-log-maxsize` argument is set to `100` or as appropriate (Automated) | L1 | Pass  
1.2.22 | Ensure that the `--request-timeout` argument is set as appropriate (Manual) | L1 | Pass  
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
**_2_** | **_Etcd Node Configuration_** |  |   
**2** | **Etcd Node Configuration** |  |   
2.1 | Ensure that the `--cert-file` and `--key-file` arguments are set as appropriate (Automated) | L1 | Pass  
2.2 | Ensure that the `--client-cert-auth` argument is set to true (Automated) | L1 | Pass  
2.3 | Ensure that the `--auto-tls` argument is not set to true (Automated) | L1 | Pass  
2.4 | Ensure that the `--peer-cert-file` and `--peer-key-file` arguments are set as appropriate (Automated) | L1 | Pass  
2.5 | Ensure that the `--peer-client-cert-auth` argument is set to true (Automated) | L1 | Pass  
2.6 | Ensure that the `--peer-auto-tls` argument is not set to true (Automated) | L1 | Pass  
2.7 | Ensure that a unique Certificate Authority is used for etcd (Manual) | L2 | Pass  
**_3_** | **_Control Plane Configuration_** |  |   
**3.1** | **Authentication and Authorization** |  |   
3.1.1 | Client certificate authentication should not be used for users (Manual) | L2 | Pass  
3.1.2 | Service account token authentication should not be used for users (Manual) | L1 | Warn  
3.1.3 | Bootstrap token authentication should not be used for users (Manual) | L1 | Warn  
**3.2** | **Logging** |  |   
3.2.1 | Ensure that a minimal audit policy is created (Manual) | L1 | Pass  
3.2.2 | Ensure that the audit policy covers key security concerns (Manual) | L2 | Equivalent Control  
**_4_** | **_Worker Node Security Configuration_** |  |   
**4.1** | **Worker Node Configuration Files** |  |   
4.1.1 | Ensure that the kubelet service file permissions are set to `600` or more restrictive (Automated) | L1 | Fail  
4.1.2 | Ensure that the kubelet service file ownership is set to `root:root` (Automated) | L1 | Pass  
4.1.3 | If proxy kubeconfig file exists ensure permissions are set to `600` or more restrictive (Manual) | L1 | Pass  
4.1.4 | If proxy kubeconfig file exists ensure ownership is set to `root:root` (Manual) | L1 | Pass  
4.1.5 | Ensure that the `--kubeconfig` kubelet.conf file permissions are set to `600` or more restrictive (Automated) | L1 | Pass  
4.1.6 | Ensure that the `--kubeconfig` kubelet.conf file ownership is set to `root:root` (Automated) | L1 | Pass  
4.1.7 | Ensure that the certificate authorities file permissions are set to `600` or more restrictive (Manual) | L1 | Pass  
4.1.8 | Ensure that the client certificate authorities file ownership is set to `root:root` (Manual) | L1 | Pass  
4.1.9 | If the kubelet config`.`yaml configuration file is being used validate permissions set to `600` or more restrictive (Manual) | L1 | Warn  
4.1.10 | If the kubelet config`.`yaml configuration file is being used validate file ownership is set to `root:root` (Manual) | L1 | Pass  
**4.2** | **Kubelet** |  |   
4.2.1 | Ensure that the `--anonymous-auth` argument is set to false (Automated) | L1 | Pass  
4.2.2 | Ensure that the `--authorization-mode` argument is not set to AlwaysAllow (Automated) | L1 | Pass  
4.2.3 | Ensure that the `--client-ca-file` argument is set as appropriate (Automated) | L1 | Pass  
4.2.4 | Verify that the `--read-only-port` argument is set to `0` (Manual) | L1 | Fail  
4.2.5 | Ensure that the `--streaming-connection-idle-timeout` argument is not set to `0` (Manual) | L1 | Pass  
4.2.6 | Ensure that the `--make-iptables-util-chains` argument is set to true (Automated) | L1 | Pass  
4.2.7 | Ensure that the `--hostname-override` argument is not set (Manual) | L1 | Pass  
4.2.8 | Ensure that the eventRecordQPS argument is set to a level which ensures appropriate event capture (Manual) | L1 | Pass  
4.2.9 | Ensure that the `--tls-cert-file` and `--tls-private-key-file` arguments are set as appropriate (Manual) | L2 | Equivalent Control  
4.2.10 | Ensure that the `--rotate-certificates` argument is not set to false (Automated) | L1 | Pass  
4.2.11 | Verify that the RotateKubeletServerCertificate argument is set to true (Manual) | L1 | Pass  
4.2.12 | Ensure that the Kubelet only makes use of Strong Cryptographic Ciphers (Manual) | L1 | Pass  
4.2.13 | Ensure that a limit is set on pod PIDs (Manual) | L1 | Warn  
  
#### Descriptions of Failures and Equivalent Controls for Google Distributed Cloud admin cluster

# | Recommendation | Level | Status | Value | Justification  
---|---|---|---|---|---  
1.1.1 | Ensure that the API server pod specification file permissions are set to `600` or more restrictive (Automated) | L1 | Equivalent Control | N/A | In kubeception mode, user cluster's API server pod specification is stored in etcd.  
1.1.3 | Ensure that the controller manager pod specification file permissions are set to `600` or more restrictive (Automated) | L1 | Equivalent Control | N/A | In kubeception mode, user cluster's controller manager pod specification is stored in etcd.  
1.1.5 | Ensure that the scheduler pod specification file permissions are set to `600` or more restrictive (Automated) | L1 | Equivalent Control | N/A | In kubeception mode, user cluster's scheduler pod specification is stored in etcd.  
1.1.7 | Ensure that the etcd pod specification file permissions are set to `600` or more restrictive (Automated) | L1 | Equivalent Control | N/A | In kubeception mode, user cluster's etcd specification is stored in admin cluster's etcd.  
1.1.12 | Ensure that the etcd data directory ownership is set to `etcd:etcd` (Automated) | L1 | Equivalent Control | `2001:2001` | The etcd container runs as `2001` and the etcd data directory is owned by `2001:2001`.  
1.1.16 | Ensure that the scheduler.conf file ownership is set to `root:root` (Automated) | L1 | Equivalent Control | `2000:2000` | The kube-scheduler container runs as `2000` and this file is owned by `2000:2000`.  
1.1.18 | Ensure that the controller-manager.conf file ownership is set to `root:root` (Automated) | L1 | Equivalent Control | `2002:2002` | The controller-manager container runs as 2002 and this file is owned by 2002:2002.  
1.2.3 | Ensure that the `--`DenyServiceExternalIPs is set (Manual) | L1 | Warn | not set | Anthos clusters on VMware does not support the Event Rate Limit admission controller as it is a Kubernetes Alpha feature.  
1.2.9 | Ensure that the admission control plugin EventRateLimit is set (Manual) | L1 | Warn | not set | Anthos clusters on VMware does not support the Event Rate Limit admission controller as it is a Kubernetes Alpha feature.  
1.2.11 | Ensure that the admission control plugin AlwaysPullImages is set (Manual) | L1 | Depends On Environment | not set | The AlwaysPullImages admission controller provides some protection for private registry images in noncooperative multitenant clusters, at the cost of making container registries a single-point-of-failure for creating new Pods across the entire cluster. Google Distributed Cloud does not enable the AlwaysPullImages admission controller, which leaves it up to cluster admins to implement admission policy to make this tradeoff for themselves.  
1.2.12 | Ensure that the admission control plugin SecurityContextDeny is set if PodSecurityPolicy is not used (Manual) | L1 | Equivalent Control | not set | PodSecurityPolicy will be removed from Kubernetes in [1.25](https://kubernetes.io/docs/concepts/security/pod-security-policy/). As a replacement, [Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/) is enabled by default as of 1.23.  
1.2.19 | Ensure that the `--audit-log-maxage` argument is set to `30` or as appropriate (Automated) | L1 | Equivalent Control | not set | Google Distributed Cloud captures audit logs but does not use these flags for auditing. See Google Distributed Cloud [Audit policy](https://cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/audit-logging) for more details.  
3.1.2 | Service account token authentication should not be used for users (Manual) | L1 | Warn | not set | Anthos clusters on VMware does not support the Event Rate Limit admission controller as it is a Kubernetes Alpha feature.  
3.1.3 | Bootstrap token authentication should not be used for users (Manual) | L1 | Warn | not set | Anthos clusters on VMware does not support the Event Rate Limit admission controller as it is a Kubernetes Alpha feature.  
3.2.2 | Ensure that the audit policy covers key security concerns (Manual) | L2 | Equivalent Control | not set | Google Distributed Cloud captures audit logs but does not use these flags for auditing. See Google Distributed Cloud [Audit policy](https://cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/audit-logging) for more details.  
4.1.1 | Ensure that the kubelet service file permissions are set to `600` or more restrictive (Automated) | L1 | Fail | not set | Anthos clusters on VMware does not support the Event Rate Limit admission controller as it is a Kubernetes Alpha feature.  
4.1.9 | If the kubelet config`.`yaml configuration file is being used validate permissions set to `600` or more restrictive (Manual) | L1 | Warn | not set | Anthos clusters on VMware does not support the Event Rate Limit admission controller as it is a Kubernetes Alpha feature.  
4.2.4 | Verify that the `--read-only-port` argument is set to `0` (Manual) | L1 | Fail | `10255` | Some Google Distributed Cloud monitoring components use the kubelet read-only port to obtain metrics.  
4.2.9 | Ensure that the `--tls-cert-file` and `--tls-private-key-file` arguments are set as appropriate (Manual) | L2 | Equivalent Control | not set | Google Distributed Cloud manages kubelet server TLS using the `--rotate-server-certificates` flag.  
4.2.13 | Ensure that a limit is set on pod PIDs (Manual) | L1 | Warn | not set | Anthos clusters on VMware does not support the Event Rate Limit admission controller as it is a Kubernetes Alpha feature.  
  
#### Status of Google Distributed Cloud user cluster

# | Recommendation | Level | Status  
---|---|---|---  
**_1_** | **_Control Plane Security Configuration_** |  |   
**1.1** | **Control Plane Node Configuration Files** |  |   
1.1.1 | Ensure that the API server pod specification file permissions are set to `600` or more restrictive (Automated) | L1 | Equivalent Control  
1.1.2 | Ensure that the API server pod specification file ownership is set to `root:root` (Automated) | L1 | Equivalent Control  
1.1.3 | Ensure that the controller manager pod specification file permissions are set to `600` or more restrictive (Automated) | L1 | Equivalent Control  
1.1.4 | Ensure that the controller manager pod specification file ownership is set to `root:root` (Automated) | L1 | Equivalent Control  
1.1.5 | Ensure that the scheduler pod specification file permissions are set to `600` or more restrictive (Automated) | L1 | Equivalent Control  
1.1.6 | Ensure that the scheduler pod specification file ownership is set to `root:root` (Automated) | L1 | Equivalent Control  
1.1.7 | Ensure that the etcd pod specification file permissions are set to `600` or more restrictive (Automated) | L1 | Equivalent Control  
1.1.8 | Ensure that the etcd pod specification file ownership is set to `root:root` (Automated) | L1 | Equivalent Control  
1.1.9 | Ensure that the Container Network Interface file permissions are set to `600` or more restrictive (Manual) | L1 | Pass  
1.1.10 | Ensure that the Container Network Interface file ownership is set to `root:root` (Manual) | L1 | Pass  
1.1.11 | Ensure that the etcd data directory permissions are set to `700` or more restrictive (Automated) | L1 | Equivalent Control  
1.1.12 | Ensure that the etcd data directory ownership is set to `etcd:etcd` (Automated) | L1 | Equivalent Control  
1.1.13 | Ensure that the admin.conf file permissions are set to `600` or more restrictive (Automated) | L1 | Pass  
1.1.14 | Ensure that the admin.conf file ownership is set to `root:root` (Automated) | L1 | Pass  
1.1.15 | Ensure that the scheduler.conf file permissions are set to `600` or more restrictive (Automated) | L1 | Pass  
1.1.16 | Ensure that the scheduler.conf file ownership is set to `root:root` (Automated) | L1 | Equivalent Control  
1.1.17 | Ensure that the controller-manager.conf file permissions are set to `600` or more restrictive (Automated) | L1 | Pass  
1.1.18 | Ensure that the controller-manager.conf file ownership is set to `root:root` (Automated) | L1 | Equivalent Control  
1.1.19 | Ensure that the Kubernetes PKI directory and file ownership is set to `root:root` (Automated) | L1 | Pass  
1.1.20 | Ensure that the Kubernetes PKI certificate file permissions are set to `600` or more restrictive (Manual) | L1 | Pass  
1.1.21 | Ensure that the Kubernetes PKI key file permissions are set to `600` (Manual) | L1 | Pass  
**1.2** | **API Server** |  |   
1.2.1 | Ensure that the `--anonymous-auth` argument is set to false (Manual) | L1 | Pass  
1.2.2 | Ensure that the `--token-auth-file` parameter is not set (Automated) | L1 | Pass  
1.2.3 | Ensure that the `--DenyServiceExternalIPs` is set (Manual) | L1 | Warn  
1.2.4 | Ensure that the `--kubelet-client-certificate` and `--kubelet-client-key` arguments are set as appropriate (Automated) | L1 | Pass  
1.2.5 | Ensure that the `--kubelet-certificate-authority` argument is set as appropriate (Automated) | L1 | Pass  
1.2.6 | Ensure that the `--authorization-mode` argument is not set to AlwaysAllow (Automated) | L1 | Pass  
1.2.7 | Ensure that the `--authorization-mode` argument includes Node (Automated) | L1 | Pass  
1.2.8 | Ensure that the `--authorization-mode` argument includes RBAC (Automated) | L1 | Pass  
1.2.9 | Ensure that the admission control plugin EventRateLimit is set (Manual) | L1 | Warn  
1.2.10 | Ensure that the admission control plugin AlwaysAdmit is not set (Automated) | L1 | Pass  
1.2.11 | Ensure that the admission control plugin AlwaysPullImages is set (Manual) | L1 | Depends On Environment  
1.2.12 | Ensure that the admission control plugin SecurityContextDeny is set if PodSecurityPolicy is not used (Manual) | L1 | Equivalent Control  
1.2.13 | Ensure that the admission control plugin ServiceAccount is set (Automated) | L1 | Pass  
1.2.14 | Ensure that the admission control plugin NamespaceLifecycle is set (Automated) | L1 | Pass  
1.2.15 | Ensure that the admission control plugin NodeRestriction is set (Automated) | L1 | Pass  
1.2.16 | Ensure that the `--secure-port` argument is not set to `0` \- NoteThis recommendation is obsolete and will be deleted per the consensus process (Manual) | L1 | Pass  
1.2.17 | Ensure that the `--profiling` argument is set to false (Automated) | L1 | Pass  
1.2.18 | Ensure that the `--audit-log-path` argument is set (Automated) | L1 | Pass  
1.2.19 | Ensure that the `--audit-log-maxage` argument is set to `30` or as appropriate (Automated) | L1 | Equivalent Control  
1.2.20 | Ensure that the `--audit-log-maxbackup` argument is set to `10` or as appropriate (Automated) | L1 | Pass  
1.2.21 | Ensure that the `--audit-log-maxsize` argument is set to `100` or as appropriate (Automated) | L1 | Pass  
1.2.22 | Ensure that the `--request-timeout` argument is set as appropriate (Manual) | L1 | Pass  
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
**_2_** | **_Etcd Node Configuration_** |  |   
**2** | **Etcd Node Configuration** |  |   
2.1 | Ensure that the `--cert-file` and `--key-file` arguments are set as appropriate (Automated) | L1 | Pass  
2.2 | Ensure that the `--client-cert-auth` argument is set to true (Automated) | L1 | Pass  
2.3 | Ensure that the `--auto-tls` argument is not set to true (Automated) | L1 | Pass  
2.4 | Ensure that the `--peer-cert-file` and `--peer-key-file` arguments are set as appropriate (Automated) | L1 | Pass  
2.5 | Ensure that the `--peer-client-cert-auth` argument is set to true (Automated) | L1 | Pass  
2.6 | Ensure that the `--peer-auto-tls` argument is not set to true (Automated) | L1 | Pass  
2.7 | Ensure that a unique Certificate Authority is used for etcd (Manual) | L2 | Pass  
**_3_** | **_Control Plane Configuration_** |  |   
**3.1** | **Authentication and Authorization** |  |   
3.1.1 | Client certificate authentication should not be used for users (Manual) | L2 | Pass  
3.1.2 | Service account token authentication should not be used for users (Manual) | L1 | Warn  
3.1.3 | Bootstrap token authentication should not be used for users (Manual) | L1 | Warn  
**3.2** | **Logging** |  |   
3.2.1 | Ensure that a minimal audit policy is created (Manual) | L1 | Pass  
3.2.2 | Ensure that the audit policy covers key security concerns (Manual) | L2 | Equivalent Control  
**_4_** | **_Worker Node Security Configuration_** |  |   
**4.1** | **Worker Node Configuration Files** |  |   
4.1.1 | Ensure that the kubelet service file permissions are set to `600` or more restrictive (Automated) | L1 | Fail  
4.1.2 | Ensure that the kubelet service file ownership is set to `root:root` (Automated) | L1 | Pass  
4.1.3 | If proxy kubeconfig file exists ensure permissions are set to `600` or more restrictive (Manual) | L1 | Pass  
4.1.4 | If proxy kubeconfig file exists ensure ownership is set to `root:root` (Manual) | L1 | Pass  
4.1.5 | Ensure that the `--kubeconfig` kubelet.conf file permissions are set to `600` or more restrictive (Automated) | L1 | Pass  
4.1.6 | Ensure that the `--kubeconfig` kubelet.conf file ownership is set to `root:root` (Automated) | L1 | Pass  
4.1.7 | Ensure that the certificate authorities file permissions are set to `600` or more restrictive (Manual) | L1 | Pass  
4.1.8 | Ensure that the client certificate authorities file ownership is set to `root:root` (Manual) | L1 | Pass  
4.1.9 | If the kubelet config`.`yaml configuration file is being used validate permissions set to `600` or more restrictive (Manual) | L1 | Warn  
4.1.10 | If the kubelet config`.`yaml configuration file is being used validate file ownership is set to `root:root` (Manual) | L1 | Pass  
**4.2** | **Kubelet** |  |   
4.2.1 | Ensure that the `--anonymous-auth` argument is set to false (Automated) | L1 | Pass  
4.2.2 | Ensure that the `--authorization-mode` argument is not set to AlwaysAllow (Automated) | L1 | Pass  
4.2.3 | Ensure that the `--client-ca-file` argument is set as appropriate (Automated) | L1 | Pass  
4.2.4 | Verify that the `--read-only-port` argument is set to `0` (Manual) | L1 | Fail  
4.2.5 | Ensure that the `--streaming-connection-idle-timeout` argument is not set to `0` (Manual) | L1 | Pass  
4.2.6 | Ensure that the `--make-iptables-util-chains` argument is set to true (Automated) | L1 | Pass  
4.2.7 | Ensure that the `--hostname-override` argument is not set (Manual) | L1 | Pass  
4.2.8 | Ensure that the eventRecordQPS argument is set to a level which ensures appropriate event capture (Manual) | L1 | Pass  
4.2.9 | Ensure that the `--tls-cert-file` and `--tls-private-key-file` arguments are set as appropriate (Manual) | L2 | Equivalent Control  
4.2.10 | Ensure that the `--rotate-certificates` argument is not set to false (Automated) | L1 | Pass  
4.2.11 | Verify that the RotateKubeletServerCertificate argument is set to true (Manual) | L1 | Pass  
4.2.12 | Ensure that the Kubelet only makes use of Strong Cryptographic Ciphers (Manual) | L1 | Pass  
4.2.13 | Ensure that a limit is set on pod PIDs (Manual) | L1 | Warn  
  
#### Descriptions of Failures and Equivalent Controls for Google Distributed Cloud user cluster

# | Recommendation | Level | Status | Value | Justification  
---|---|---|---|---|---  
1.1.1 | Ensure that the API server pod specification file permissions are set to `600` or more restrictive (Automated) | L1 | Equivalent Control | N/A | In kubeception mode, user cluster's API server pod specification is stored in etcd.  
1.1.2 | Ensure that the API server pod specification file ownership is set to `root:root` (Automated) | L1 | Equivalent Control | N/A | In kubeception mode, user cluster's API server pod specification is stored in etcd.  
1.1.3 | Ensure that the controller manager pod specification file permissions are set to `600` or more restrictive (Automated) | L1 | Equivalent Control | N/A | In kubeception mode, user cluster's controller manager pod specification is stored in etcd.  
1.1.4 | Ensure that the controller manager pod specification file ownership is set to `root:root` (Automated) | L1 | Equivalent Control | N/A | In kubeception mode, user cluster's controller manager pod specification is stored in etcd.  
1.1.5 | Ensure that the scheduler pod specification file permissions are set to `600` or more restrictive (Automated) | L1 | Equivalent Control | N/A | In kubeception mode, user cluster's scheduler pod specification is stored in etcd.  
1.1.6 | Ensure that the scheduler pod specification file ownership is set to `root:root` (Automated) | L1 | Equivalent Control | N/A | In kubeception mode, user cluster's scheduler pod specification is stored in etcd.  
1.1.7 | Ensure that the etcd pod specification file permissions are set to `600` or more restrictive (Automated) | L1 | Equivalent Control | N/A | In kubeception mode, user cluster's etcd specification is stored in admin cluster's etcd.  
1.1.8 | Ensure that the etcd pod specification file ownership is set to `root:root` (Automated) | L1 | Equivalent Control | N/A | In kubeception mode, user cluster's etcd specification is stored in admin cluster's etcd.  
1.1.11 | Ensure that the etcd data directory permissions are set to `700` or more restrictive (Automated) | L1 | Equivalent Control | `777` | The etcd data directory is mounted through vshpere external storage.  
1.1.12 | Ensure that the etcd data directory ownership is set to `etcd:etcd` (Automated) | L1 | Equivalent Control | `2001:2001` | The etcd container runs as `2001` and the etcd data directory is owned by `2001:2001`.  
1.1.16 | Ensure that the scheduler.conf file ownership is set to `root:root` (Automated) | L1 | Equivalent Control | `2000:2000` | The kube-scheduler container runs as `2000` and this file is owned by `2000:2000`.  
1.1.18 | Ensure that the controller-manager.conf file ownership is set to `root:root` (Automated) | L1 | Equivalent Control | `2002:2002` | The controller-manager container runs as 2002 and this file is owned by 2002:2002.  
1.2.3 | Ensure that the `--`DenyServiceExternalIPs is set (Manual) | L1 | Warn | not set | Anthos clusters on VMware does not support the Event Rate Limit admission controller as it is a Kubernetes Alpha feature.  
1.2.9 | Ensure that the admission control plugin EventRateLimit is set (Manual) | L1 | Warn | not set | Anthos clusters on VMware does not support the Event Rate Limit admission controller as it is a Kubernetes Alpha feature.  
1.2.11 | Ensure that the admission control plugin AlwaysPullImages is set (Manual) | L1 | Depends On Environment | not set | The AlwaysPullImages admission controller provides some protection for private registry images in noncooperative multitenant clusters, at the cost of making container registries a single-point-of-failure for creating new Pods across the entire cluster. Google Distributed Cloud does not enable the AlwaysPullImages admission controller, which leaves it up to cluster admins to implement admission policy to make this tradeoff for themselves.  
1.2.12 | Ensure that the admission control plugin SecurityContextDeny is set if PodSecurityPolicy is not used (Manual) | L1 | Equivalent Control | not set | PodSecurityPolicy will be removed from Kubernetes in [1.25](https://kubernetes.io/docs/concepts/security/pod-security-policy/). As a replacement, [Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/) is enabled by default as of 1.23.  
1.2.19 | Ensure that the `--audit-log-maxage` argument is set to `30` or as appropriate (Automated) | L1 | Equivalent Control | not set | Google Distributed Cloud captures audit logs but does not use these flags for auditing. See Google Distributed Cloud [Audit policy](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/audit-logging) for more details.  
3.1.2 | Service account token authentication should not be used for users (Manual) | L1 | Warn | not set | Anthos clusters on VMware does not support the Event Rate Limit admission controller as it is a Kubernetes Alpha feature.  
3.1.3 | Bootstrap token authentication should not be used for users (Manual) | L1 | Warn | not set | Anthos clusters on VMware does not support the Event Rate Limit admission controller as it is a Kubernetes Alpha feature.  
3.2.2 | Ensure that the audit policy covers key security concerns (Manual) | L2 | Equivalent Control | not set | Google Distributed Cloud captures audit logs but does not use these flags for auditing. See Google Distributed Cloud [Audit policy](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/audit-logging) for more details.  
4.1.1 | Ensure that the kubelet service file permissions are set to `600` or more restrictive (Automated) | L1 | Fail | not set | Anthos clusters on VMware does not support the Event Rate Limit admission controller as it is a Kubernetes Alpha feature.  
4.1.9 | If the kubelet config`.`yaml configuration file is being used validate permissions set to `600` or more restrictive (Manual) | L1 | Warn | not set | Anthos clusters on VMware does not support the Event Rate Limit admission controller as it is a Kubernetes Alpha feature.  
4.2.4 | Verify that the `--read-only-port` argument is set to `0` (Manual) | L1 | Fail | `10255` | Some Google Distributed Cloud monitoring components use the kubelet read-only port to obtain metrics.  
4.2.9 | Ensure that the `--tls-cert-file` and `--tls-private-key-file` arguments are set as appropriate (Manual) | L2 | Equivalent Control | not set | Google Distributed Cloud manages kubelet server TLS using the `--rotate-server-certificates` flag.  
4.2.13 | Ensure that a limit is set on pod PIDs (Manual) | L1 | Warn | not set | Anthos clusters on VMware does not support the Event Rate Limit admission controller as it is a Kubernetes Alpha feature.  
  
## Audit benchmarks

Specific instructions for auditing each Recommendation is available as part of the relevant CIS Benchmark. However, you may wish to automate some of these checks to simplify the verification of these controls in your environment. The following tool can help with this.

### Automated auditing of the CIS Kubernetes Benchmark

You can use an open-source tool `[kube-bench](https://github.com/aquasecurity/kube-bench)` to test your cluster configuration against the CIS Kubernetes Benchmark.

Make sure to specify the [appropriate version](https://github.com/aquasecurity/kube-bench/blob/main/docs/platforms.md#cis-kubernetes-benchmark-support). For example:
    
    
    kube-bench node --benchmark cis-1.7
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
