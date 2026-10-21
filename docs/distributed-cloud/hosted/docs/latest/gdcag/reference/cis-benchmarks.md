---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/cis-benchmarks/
title: CIS Kubernetes Benchmark \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:13:19.313461+00:00
---

# CIS Kubernetes Benchmark  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/cis-benchmarks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  CIS Kubernetes Benchmark Stay organized with collections  Save and categorize content based on your preferences. 

This document introduces the CIS Kubernetes Benchmark, explains how to audit your compliance with the benchmark, and explains what Google Distributed Cloud (GDC) air-gapped configures when you cannot implement a recommendation yourself.

**Important:** To access the URLs listed on this page, you must connect to the internet. The URLs are provided to access outside of your air-gapped environment.

## About the CIS benchmarks

The Center for Internet Security (CIS) releases benchmarks for best practice security recommendations. The CIS Kubernetes Benchmark provides a set of recommendations for configuring Kubernetes to support a strong security posture. The Benchmark is tied to a specific Kubernetes release. The CIS Kubernetes Benchmark is written for the open source Kubernetes distribution and intended to be as universally applicable across distributions as possible.

### Access the benchmark

The CIS Kubernetes Benchmark is available on the [CIS website](https://www.cisecurity.org/benchmark/kubernetes).

### Recommendation levels

The following table describes the recommendation levels in the CIS Kubernetes Benchmark.

Level | Description  
---|---  
Level 1 | Recommendations exhibit one or more of the following characteristics: 
* Be practical and prudent.
* Provide a clear security benefit.
* Don't inhibit the utility of the technology beyond acceptable means.  
Level 2 |  Extends the Level 1 profile. Recommendations exhibit one or more of the following characteristics: 
* Apply to environments or use cases where security is paramount.
* Acts as defense in depth measure.
* Might negatively inhibit the utility or performance of the technology.  
  
### Assessment status

An assessment status is included for every recommendation. The assessment status indicates whether the given recommendation can be automated or requires manual steps to implement. Both statuses are equally important and are determined and supported as defined in the following tables.

#### Versions

The assessment refers to the following versions:

GDC on bare metal version | Kubernetes version | CIS Kubernetes Benchmark version  
---|---|---  
1.30 | 1.30.9 | v0.10.4  
  
#### Status of GDC air-gapped Kubernetes cluster

# | Recommendation | Level | Status  
---|---|---|---  
**_1_** | **_Control Plane Security Configuration_** |  |   
**1.1** | **Control Plane Node Configuration Files** |  |   
1.1.1 | Ensure that the API server pod specification file permissions are set to `600` or more restrictive (Automated) | L1 | Pass  
1.1.2 | Ensure that the API server pod specification file ownership is set to `root:root` (Automated) | L1 | Pass  
1.1.3 | Ensure that the controller manager pod specification file permissions are set to `600` or more restrictive (Automated) | L1 | Pass  
1.1.4 | Ensure that the controller manager pod specification file ownership is set to `root:root` (Automated) | L1 | Pass  
1.1.5 | Ensure that the scheduler pod specification file permissions are set to `600` or more restrictive (Automated) | L1 | Pass  
1.1.6 | Ensure that the scheduler pod specification file ownership is set to `root:root` (Automated) | L1 | Pass  
1.1.7 | Ensure that the etcd pod specification file permissions are set to `600` or more restrictive (Automated) | L1 | Pass  
1.1.8 | Ensure that the etcd pod specification file ownership is set to `root:root` (Automated) | L1 | Pass  
1.1.9 | Ensure that the Container Network Interface file permissions are set to `600` or more restrictive (Manual) | L1 | Warn  
1.1.10 | Ensure that the Container Network Interface file ownership is set to `root:root` (Manual) | L1 | Warn  
1.1.11 | Ensure that the etcd data directory permissions are set to `700` or more restrictive (Automated) | L1 | Pass  
1.1.12 | Ensure that the etcd data directory ownership is set to `etcd:etcd` (Automated) | L1 | Fail  
1.1.13 | Ensure that the default administrative credential file permissions are set to `600` (Automated) | L1 | Pass  
1.1.14 | Ensure that the default administrative credential file ownership is set to `root:root` (Automated) | L1 | Pass  
1.1.15 | Ensure that the `scheduler.conf` file permissions are set to `600` or more restrictive (Automated) | L1 | Pass  
1.1.16 | Ensure that the `scheduler.conf` file ownership is set to `root:root` (Automated) | L1 | Fail  
1.1.17 | Ensure that the `controller-manager.conf` file permissions are set to `600` or more restrictive (Automated) | L1 | Pass  
1.1.18 | Ensure that the `controller-manager.conf` file ownership is set to `root:root` (Automated) | L1 | Fail  
1.1.19 | Ensure that the Kubernetes PKI directory and file ownership is set to `root:root` (Automated) | L1 | Fail  
1.1.20 | Ensure that the Kubernetes PKI certificate file permissions are set to `600` or more restrictive (Manual) | L1 | Warn  
1.1.21 | Ensure that the Kubernetes PKI key file permissions are set to `600` (Manual) | L1 | Warn  
**1.2** | **API Server** |  |   
1.2.1 | Ensure that the `--anonymous-auth` argument is set to `false` (Manual) | L1 | Warn  
1.2.2 | Ensure that the `--token-auth-file` parameter is not set (Automated) | L1 | Pass  
1.2.3 | Ensure that the `--DenyServiceExternalIPs` is set (Manual) | L1 | Warn  
1.2.4 | Ensure that the `--kubelet-client-certificate` and `--kubelet-client-key` arguments are set as appropriate (Automated) | L1 | Pass  
1.2.5 | Ensure that the `--kubelet-certificate-authority` argument is set as appropriate (Automated) | L1 | Pass  
1.2.6 | Ensure that the `--authorization-mode` argument is not set to AlwaysAllow (Automated) | L1 | Pass  
1.2.7 | Ensure that the `--authorization-mode` argument includes Node (Automated) | L1 | Pass  
1.2.8 | Ensure that the `--authorization-mode` argument includes RBAC (Automated) | L1 | Pass  
1.2.9 | Ensure that the admission control plugin `EventRateLimit` is set (Manual) | L1 | Warn  
1.2.10 | Ensure that the admission control plugin `AlwaysAdmit` is not set (Automated) | L1 | Pass  
1.2.11 | Ensure that the admission control plugin `AlwaysPullImages` is set (Manual) | L1 | Warn  
1.2.12 | Ensure that the admission control plugin `ServiceAccount` is set (Automated) | L1 | Pass  
1.2.13 | Ensure that the admission control plugin `NamespaceLifecycle` is set (Automated) | L1 | Pass  
1.2.14 | Ensure that the admission control plugin `NodeRestriction` is set (Automated) | L1 | Pass  
1.2.15 | Ensure that the `--profiling` argument is set to `false` (Automated) | L1 | Pass  
1.2.16 | Ensure that the `--audit-log-path` argument is set (Automated) | L1 | Pass  
1.2.17 | Ensure that the `--audit-log-maxage` argument is set to `30` or as appropriate (Automated) | L1 | Pass  
1.2.18 | Ensure that the `--audit-log-maxbackup` argument is set to `10` or as appropriate (Automated) | L1 | Pass  
1.2.19 | Ensure that the `--audit-log-maxsize` argument is set to `100` or as appropriate (Automated) | L1 | Pass  
1.2.20 | Ensure that the `--request-timeout` argument is set as appropriate (Manual) | L1 | Warn  
1.2.21 | Ensure that the `--service-account-lookup` argument is set to `true` (Automated) | L1 | Pass  
1.2.22 | Ensure that the `--service-account-key-file` argument is set as appropriate (Automated) | L1 | Pass  
1.2.23 | Ensure that the `--etcd-certfile` and `--etcd-keyfile` arguments are set as appropriate (Automated) | L1 | Pass  
1.2.24 | Ensure that the `--tls-cert-file` and `--tls-private-key-file` arguments are set as appropriate (Automated) | L1 | Pass  
1.2.25 | Ensure that the `--client-ca-file` argument is set as appropriate (Automated) | L1 | Pass  
1.2.26 | Ensure that the `--etcd-cafile` argument is set as appropriate (Automated) | L1 | Pass  
1.2.27 | Ensure that the `--encryption-provider-config` argument is set as appropriate (Manual) | L1 | Pass  
1.2.28 | Ensure that encryption providers are appropriately configured (Manual) | L1 | Pass  
1.2.29 | Ensure that the API Server only makes use of Strong Cryptographic Ciphers (Manual) | L1 | Pass  
**1.3** | **Controller Manager** |  |   
1.3.1 | Ensure that the `--terminated-pod-gc-threshold` argument is set as appropriate (Manual) | L1 | Pass  
1.3.2 | Ensure that the `--profiling argument` is set to `false` (Automated) | L1 | Pass  
1.3.3 | Ensure that the `--use-service-account-credentials` argument is set to `true` (Automated) | L1 | Pass  
1.3.4 | Ensure that the `--service-account-private-key-file` argument is set as appropriate (Automated) | L1 | Pass  
1.3.5 | Ensure that the `--root-ca-file` argument is set as appropriate (Automated) | L1 | Pass  
1.3.6 | Ensure that the `RotateKubeletServerCertificate` argument is set to `true` (Automated) | L2 | Pass  
1.3.7 | Ensure that the `--bind-address` argument is set to `127.0.0.1` (Automated) | L1 | Fail  
**1.4** | **Scheduler** |  |   
1.4.1 | Ensure that the `--profiling` argument is set to `false` (Automated) | L1 | Pass  
1.4.2 | Ensure that the `--bind-address` argument is set to `127.0.0.1` (Automated) | L1 | Fail  
  
## Audit benchmarks

Specific instructions for auditing each recommendation is available as part of the relevant CIS Benchmark. However, you might want to automate some of these checks to simplify the verification of these controls in your environment. The following tool can help with this.

### Automated auditing of the CIS Kubernetes Benchmark

You can use an open-source tool [kube-bench](https://github.com/aquasecurity/kube-bench) to test your cluster configuration against the CIS Kubernetes Benchmark.

Make sure to specify the [appropriate version](https://github.com/aquasecurity/kube-bench/blob/main/docs/platforms.md#cis-kubernetes-benchmark-support). For example:
    
    
    kube-bench --benchmark BENCHMARK_VERSION
    

Replace `BENCHMARK_VERSION` with the CIS Kubernetes Benchmark version you're using to assess your cluster.

To run specific CIS Benchmark sections, such as master, node, or etcd, use the `run --targets` command. For example:
    
    
    kube-bench run --targets master,node
    

For more information, see kube-bench documentation on [running kube-bench](https://github.com/aquasecurity/kube-bench/blob/main/docs/running.md) and [commands and flags](https://github.com/aquasecurity/kube-bench/blob/main/docs/flags-and-commands.md).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
