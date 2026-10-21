---
url: https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller-bundles/
title: Policy Controller bundles \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:41:11.899791+00:00
---

# Policy Controller bundles  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller-bundles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Policy Controller ](https://docs.cloud.google.com/kubernetes-engine/policy-controller)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview)



Send feedback 

#  Policy Controller bundles Stay organized with collections  Save and categorize content based on your preferences. 

This page describes what Policy Controller bundles are and provides an overview of the available policy bundles.

This page is for IT administrators and Operators who want to ensure that all resources running within the cloud platform meet organizational compliance requirements by providing and maintaining automation to audit or enforce. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## About Policy Controller bundles

You can use Policy Controller to [apply individual constraints](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview#constraints) to your cluster or write your own custom policies. You can also use policy bundles, which let you audit your clusters without writing any constraints. Policy bundles are a group of constraints that can help apply best practices, meet industry standards, or solve regulatory problems across your cluster resources.

You can apply policy bundles to your existing clusters to check if your workloads are compliant. When you apply a policy bundle, it audits your cluster by applying constraints with the `dryrun` enforcement type. The `dryrun` enforcement type lets you see violations without blocking your workloads. It's also recommended that only the `warn` or `dryrun` enforcement actions are used on clusters with production workloads, when testing new constraints, or performing migrations such as upgrading platforms. For more information about enforcement actions, see [Auditing using constraints](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/auditing-constraints).

For example, one type of policy bundle is the CIS Kubernetes Benchmark bundle, which can help audit your cluster resources against the [CIS Kubernetes Benchmark](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cis-benchmarks#cis_kubernetes_benchmark). This benchmark is a set of recommendations for configuring Kubernetes resources to support a strong security posture.

## Available Policy Controller bundles

The following table lists the available policy bundles. Select the name of the policy bundle to read documentation on how to apply the bundle, audit resources, and enforce policies.

The _bundle alias_ column lists the single-token name of the bundle. This value is needed to apply a bundle with [Google Cloud CLI commands](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/apply-policy-bundles#gcloud).

The _earliest included version_ column lists the earliest version that the bundle is available with Policy Controller. If you want to install policy bundles directly, follow the instructions to [apply multiple policy bundles](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/apply-policy-bundles). If you want to install policy bundles manually, for example if you need to modify a policy bundle, follow the linked instructions for that specific bundle in the table.

**Note:** Some bundles require referential constraints, which are not enabled by default. [Learn more about referential constraints and how to enable them](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/creating-policy-controller-constraints#referential).

Kubernetes standardBest practicesIndustry standard

Bundle includes referential constraints

Name and description | Bundle alias | Earliest included version | Type | Includes referential constraints  
---|---|---|---|---  
[CIS GKE Benchmark](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-cis-gke-v1.5): Audit compliance of your clusters against the CIS GKE Benchmark v1.5, a set of recommended security controls for configuring Google Kubernetes Engine (GKE). | `cis-gke-v1.5.0` | 1.18.0 | Kubernetes standard |  Yes   
[CIS Kubernetes Benchmark](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-cis-k8s-benchmark): Audit compliance of your clusters against the CIS Kubernetes Benchmark v1.5, a set of recommendations for configuring Kubernetes to support a strong security posture. | `cis-k8s-v1.5.1` | 1.15.2 | Kubernetes standard |  Yes   
[CIS Kubernetes Benchmark](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-cis-k8s-v1.7) (Preview): Audit compliance of your clusters against the CIS Kubernetes Benchmark v1.7, a set of recommendations for configuring Kubernetes to support a strong security posture. | `cis-k8s-v1.7.1` | not available | Kubernetes standard |  Yes   
[Cost and Reliability](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-cost-reliability-v2023): The Cost and Reliability bundle helps adopt best practices for running cost-efficient GKE clusters without compromising the performance or reliability of workloads. | `cost-reliability-v2023` | 1.16.1 | Best practices |  Yes   
[MITRE](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-mitre-v2024) (Preview): The MITRE policy bundle helps evaluate the compliance of your cluster resources against some aspects of the MITRE knowledge base of adversary tactics and techniques based on real-world observations. | `mitre-v2024` | not available | Industry standard |  Yes   
[Pod Security Policy](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-constraints-to-enforce-pod-security): Apply protections based on the Kubernetes Pod Security Policy (PSP). | `psp-v2022` | 1.15.2 | Kubernetes standard | No  
[Pod Security Standards Baseline](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-pss-baseline): Apply protections based on the Kubernetes Pod Security Standards (PSS) Baseline policy.  | `pss-baseline-v2022` | 1.15.2 | Kubernetes standard | No  
[Pod Security Standards Restricted](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-pss-restricted): Apply protections based on the Kubernetes Pod Security Standards (PSS) Restricted policy.  | `pss-restricted-v2022` | 1.15.2 | Kubernetes standard | No  
[Cloud Service Mesh security](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-asm-security-policy): Audit the compliance of your Cloud Service Mesh security vulnerabilities and best practices. | `asm-policy-v0.0.1` | 1.15.2 | Best practices |  Yes   
[Policy Essentials](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-policy-essentials-v2022): Apply best practices to your cluster resources. | `policy-essentials-v2022` | 1.14.1 | Best practices | No  
[NIST SP 800-53 Rev. 5](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-nist-sp-800-53-r5): The NIST SP 800-53 Rev. 5 bundle implements controls listed in NIST Special Publication (SP) 800-53, Revision 5. The bundle may help organizations protect their systems and data from a variety of threats by implementing out-of-the-box security and privacy policies. | `nist-sp-800-53-r5` | 1.16.0 | Industry standard |  Yes   
[NIST SP 800-190](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-nist-sp-800-190): The NIST SP 800-190 bundle implements controls listed in NIST Special Publication (SP) 800-190, Application Container Security Guide. The bundle is intended to help organizations with application container security including image security, container runtime security, network security and host system security to name a few.  | `nist-sp-800-190` | 1.16.0 | Industry standard |  Yes   
[NSA CISA Kubernetes Hardening Guide v1.2](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-nsa-cisa-k8s-v1.2): Apply protections based on the NSA CISA Kubernetes Hardening Guide v1.2. | `nsa-cisa-k8s-v1.2` | 1.16.0 | Industry standard |  Yes   
[PCI-DSS v3.2.1](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-pci-dss-v3) (Deprecated): Apply protections based on the Payment Card Industry Data Security Standard (PCI-DSS) v3.2.1. | `pci-dss-v3.2.1` or `pci-dss-v3.2.1-extended` | 1.15.2 | Industry standard |  Yes   
[PCI-DSS v4.0](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-pci-dss-v4): Apply protections based on the Payment Card Industry Data Security Standard (PCI-DSS) v4.0. | `pci-dss-v4.0` | not available | Industry standard |  Yes   
  
## What's next

  * Learn more about [applying individual constraints](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/creating-policy-controller-constraints).
  * [Apply best practices to your clusters](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-policy-essentials-v2022).
  * Take a tutorial on [using policy bundles in your CI/CD pipeline to shift left](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/tutorials/app-policy-validation-ci-pipeline).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
