---
url: https://docs.cloud.google.com/apigee/docs/hybrid/security-patching/
title: Apigee hybrid security patching \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:06.287912+00:00
---

# Apigee hybrid security patching  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/security-patching/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Apigee hybrid security patching Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how Google manages security vulnerabilities and patches for Apigee hybrid. Except where otherwise noted, Apigee includes both the management plane and the data plane. 

## Shared patching responsibility

Patching is a shared responsibility between Google and the customer. Apigee X and Apigee hybrid have different shared responsibilities given the data plane for Apigee hybrid is entirely managed by the customer. For information on the Apigee hybrid shared responsibilities, see [Apigee hybrid shared responsibility model](https://docs.cloud.google.com/apigee/docs/hybrid/shared-responsibility-model). 

**Note:** If you are operating Apigee hybrid on Anthos, please refer to [Security Patching for Anthos](https://cloud.google.com/anthos/docs/concepts/security-patching) and the shared responsibilities for the corresponding Anthos platform. 

## How vulnerabilities are discovered

Google takes a proactive approach to the security of software systems, using Secure by Default design principles and implementing various security hardening practices. 

For example, containerized applications power the various Apigee API Management Platform features. The containerized applications are deployed on Kubernetes. The container images are built on top of minimal base images (for example, [distroless base images](https://github.com/GoogleContainerTools/distroless#readme)) for maximum security and improved performance. 

However, even the best designed software systems can have vulnerabilities. To find those vulnerabilities and patch them before they can be exploited, Google has made significant investments on multiple fronts. 

### Security scanners

Google proactively identifies and fixes vulnerabilities on different types of container images: 

  * **First party containers** : Container images built and distributed by Google as part of the Apigee platform. These are Google proprietary applications that power the Apigee API Management platform including core functionality such as traffic routing, quota management, and key management.
  * **Third party containers** : Container images built by the open source community but distributed by Google as part of the Apigee platform. These are mostly open source components that are used by the platform for common operational tasks such as logging, monitoring, and certificate management.



Google scans containers using [Container Registry Container Analysis](https://cloud.google.com/container-registry/docs/vulnerability-scanning) to discover vulnerabilities and missing patches in first party and third party containers. If fixes are available, Google begins the patching and release process. Such scans are run on a regular basis (when new images are published) as well as on-demand (before a release) to maximize the chances of detecting new vulnerabilities and early remediation or mitigation planning. 

### Security research 

In addition to automated scanning, Google discovers and patches vulnerabilities _unknown to scanners_ in these ways: 

  * **Google performs its own security and compliance audits, application and network penetration testing, segmentation testing, and security vulnerability discovery across all Apigee components.**  
  
Specialized teams inside Google and trusted third-party security vendors conduct their own attack research.
  * **Google collaborates with other industry and open source software partners who share vulnerabilities, security research, and patches before the public release of the vulnerability.**  
  
The goal of this collaboration is to patch large pieces of Internet infrastructure before the vulnerability is announced to the public. In some cases, Google contributes vulnerabilities found to this community. For example, Google's Project Zero discovered and publicized the [Spectre and Meltdown](https://blog.google/topics/google-cloud/what-google-cloud-g-suite-and-chrome-customers-need-know-about-industry-wide-cpu-vulnerability/) vulnerabilities. The Google Cloud Security team also regularly finds and fixes [vulnerabilities in the Kernel-based Virtual Machine (KVM)](https://cloud.google.com/blog/products/gcp/7-ways-we-harden-our-kvm-hypervisor-at-google-cloud-security-in-plaintext?m=0).



### Vulnerability Reward Programs

Google actively engages with the security research community through [multiple vulnerability reward programs](https://www.google.com/about/appsecurity/programs-home/). A dedicated Google Cloud vulnerability rewards program provides significant bounties, [including $133,337 for the best cloud vulnerability](https://security.googleblog.com/2020/03/announcing-our-first-gcp-vrp-prize.html) found each year. The program covers all Apigee software dependencies. 

### OSS

Google's security collaboration happens on many levels. Sometimes it occurs formally through programs where organizations sign up to receive pre-release notifications about software vulnerabilities for products such as [Kubernetes](https://github.com/kubernetes/security/blob/master/private-distributors-list.md) and [Envoy](https://github.com/envoyproxy/envoy/security/policy#private-distributors-list). Collaboration also happens informally due to our engagement with many open source projects such as the Linux kernel, container runtimes, virtualization technology, and others. 

While less severe vulnerabilities are discovered and patched outside of these processes, most critical security vulnerabilities are reported privately through one of the channels previously listed. Early reporting gives Google time before the vulnerability becomes public to research how it affects Apigee, develop patches or mitigations, and prepare advice and communications for customers. When possible, Google patches all clusters (for Apigee X) before the public release of the vulnerability. For Apigee hybrid, patch releases are made available on a regular basis for addressing security vulnerabilities in the container images and customers are encouraged to stay up-to-date with the latest patch versions. 

## How vulnerabilities are classified

Apigee makes large investments in security hardening on the entire stack, including the base image, the third party libraries and the first party application software, in addition to setting good defaults, security-hardened configurations, and managed components. Combined, these efforts help to reduce the impact and likelihood of vulnerabilities. 

The Apigee security team classifies vulnerabilities according to the [Common Vulnerability Scoring System (CVSS)](https://en.wikipedia.org/wiki/Common_Vulnerability_Scoring_System). 

The following table describes vulnerability severity categories: 

**Severity** | **Description**  
---|---  
Critical  | A vulnerability easily exploitable in _all_ clusters by an unauthenticated remote attacker that leads to full system compromise.   
High  | A vulnerability easily exploitable for _many_ clusters that leads to loss of confidentiality, integrity, or availability.   
Medium  | A vulnerability exploitable for _some_ clusters where loss of confidentiality, integrity, or availability is limited by common configurations, difficulty of the exploit itself, required access, or user interaction.   
Low  | All other vulnerabilities. Exploitation is unlikely or consequences of exploitation are limited.   
  
## How vulnerabilities and patches are communicated

Google's goal is to mitigate detected vulnerabilities within a time period appropriate for the risks they represent. Apigee is included within [Google Cloud's FedRAMP provisional ATO](https://cloud.google.com/security/compliance/fedramp) which requires that known vulnerabilities be remediated within specific timeframes according to their severity level as shown in the [ FedRAMP Continuous Monitoring Performance Management Guide](https://www.fedramp.gov/resources/documents/CSP_Continuous_Monitoring_Performance_Management_Guide.pdf). Google Cloud's FedRAMP provisional ATO doesn't include Apigee hybrid data plane components (customer-managed) but we aim for the same remediation timeframes on those products. 

### Vulnerabilities detected by proactive scanning

Google detects security vulnerabilities through proactive scanning of the binaries and the underlying infrastructure that hosts the Apigee platform. Apigee releases regular patch updates to address these vulnerabilities in a timely manner depending on the severity of underlying [CVE](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures)(s). Patching a vulnerability involves upgrading to a new Apigee hybrid version-‐either a minor version upgrade or a patch version upgrade, depending on the nature of the vulnerability. Such vulnerabilities are mostly addressed as part of monthly patch releases for Apigee hybrid and included in the regular software updates to our managed fleet in the case of Apigee X. Security patches are communicated through release notes for both Apigee X and Apigee hybrid. 

Fixing some vulnerabilities requires only a control plane upgrade, performed automatically by Google on Apigee, while others require new binaries to be rolled out to the data plane. In case of Apigee X, Google takes care of rolling out the new binaries to the entire fleet. Customers running Apigee Apigee hybrid must apply the patch release to their Apigee hybrid clusters in order to roll out the updated binaries. 

To keep clusters patched and hardened against vulnerabilities of all severities, we recommend applying the latest patch release for any given minor version of Apigee hybrid. For those running Apigee hybrid on Anthos, Google recommends upgrading your Anthos components at least monthly. 

### Customer-reported vulnerabilities

With Apigee hybrid, customers are given Apigee binaries to run in their data centers or their preferred cloud platforms. As part of a customer's security standards for launching software into production in their own data centers, they may run a series of security tests. These tests could include penetration testing, container scanning, static code scanning, etc. These tests might report possible vulnerabilities in the Apigee software. Prior to enabling these packages in their data centers, customers need to determine if these reported items are exploitable and therefore a security risk. 

#### Vulnerability with an exploit Proof of Concept

If the customer identifies an exploitable vulnerability and has a proof of concept (POC) on how to exploit the vulnerability, they should report this issue through the Google Vulnerabilities Reward Program found at [goo.gle/vulnz](https://goo.gle/vulnz). This reports the issue to the Google security team who will validate the proof of concept and determine its severity and potential impact. The issue will then be escalated to Apigee. The customer may be eligible for a reward through the VRP program. 

#### Vulnerability identified by an automated tool

If the customer has generated a report of possible vulnerabilities in the Apigee product based on static scanning or another tool or technique, but does not have any proof of concepts on how to exploit the issue(s), these items can be reported to support through [Google Cloud support portal](https://cloud.google.com/support). By reporting the issue to support, the customer has a ticket number for tracking and can see updates and responses to the report. The support team will then escalate the reported issue(s) internally as appropriate. 

#### CVE identifiers

Customers should include as much information about the vulnerability as possible, and specifically include the [CVE identifier](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures#CVE_identifiers), library/package name, name of the container image etc. for each item. CVEs allow us to know we are looking at the same vulnerability. Providing only a description of the issue or other proprietary tracking number does not allow correlation of the issue across detection tools or reporting processes. Without a CVE, Google may be unable to respond to the specific item. 

#### Response

For items reported to support which have a severity score of critical or high, customers can expect a response through the support ticketing system. For items reported to the VRP, please see [the rules and documentation provided](https://www.google.com/about/appsecurity/reward-program/index.html) by the program. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
