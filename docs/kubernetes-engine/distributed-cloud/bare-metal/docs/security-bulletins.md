---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/security-bulletins/
title: Security bulletins \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:06.191456+00:00
---

# Security bulletins  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/security-bulletins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Security bulletins Stay organized with collections  Save and categorize content based on your preferences. 

This document describes security bulletins for Distributed Cloud (software only) for VMware and bare metal. The bulletins in this document start from June 1, 2026. To view bulletins for these products for dates prior to June 1, 2026, see [GKE security bulletins](https://docs.cloud.google.com/kubernetes-engine/security-bulletins).

## GCP-2026-051

**Published:** 2026-07-31

**Updated:** 2026-08-04

**Reference:** [CVE-2026-50195](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-50195), [CVE-2026-53488](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-53488), [CVE-2026-53492](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-53492), [CVE-2026-53489](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-53489), [CVE-2026-47262](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47262)

### VMware

Description | Severity  
---|---  
**2026-08-04 Update:** Changed the VMware patch version from 1.33.1100 to 1.33.1200. The following vulnerabilities have been discovered in containerd (the GDC container runtime). These vulnerabilities allow attackers with permissions to create Pods to bypass Kubernetes security boundaries and perform host compromise, cache poisoning, and denial of service. While these vulnerabilities are critical in the context of containerd, the requirement to have cluster privileges to create Pods to exploit them means they are considered High according to GDC (software only) vulnerability classification. 

  * **CVE-2026-50195 (Critical)** : containerd's CRI checkpoint import process fails to validate image references. An attacker with permissions to create Pods can use a crafted checkpoint image to poison the node's local image cache, causing other pods to use a malicious image.
  * **CVE-2026-53488 (Critical)** : CRI plugin propagates labels from an image config to a container without validation. This may result in executing an arbitrary command on the host.
  * **CVE-2026-53492 (Critical)** : CRI implementation improperly trusts Container Device Interface (CDI) annotations during container restoration. This allows an attacker to inject arbitrary CDI configurations (such as host mounts and device nodes) into restored containers, bypassing resource allocation and device plugin enforcement.
  * **CVE-2026-53489 (High)** : CRI plugin restores container.log without validating a symlinked path, allowing an attacker to read arbitrary host files via kubectl logs.
  * **CVE-2026-47262 (Moderate)** : A vulnerability in containerd allows a maliciously crafted image to cause memory exhaustion (DoS) of the containerd process.

These vulnerabilities affect all GDC (software only) configurations using Container-Optimized OS and Ubuntu node images. 

#### What should I do?

For GDC software only on VMware, the following patches will contain fixes for the vulnerabilities:

  * 1.34.800 
  * 1.33.1200

| High  
  
### Bare metal

**2026-08-04 Update:** Changed the VMware patch version from 1.33.1100 to 1.33.1200.

Description | Severity  
---|---  
The following vulnerabilities have been discovered in containerd (the GDC container runtime). These vulnerabilities allow attackers with permissions to create Pods to bypass Kubernetes security boundaries and perform host compromise, cache poisoning, and denial of service. While these vulnerabilities are critical in the context of containerd, the requirement to have cluster privileges to create Pods to exploit them means they are considered High according to GDC (software only) vulnerability classification. 

  * **CVE-2026-50195 (Critical)** : containerd's CRI checkpoint import process fails to validate image references. An attacker with permissions to create Pods can use a crafted checkpoint image to poison the node's local image cache, causing other pods to use a malicious image.
  * **CVE-2026-53488 (Critical)** : CRI plugin propagates labels from an image config to a container without validation. This may result in executing an arbitrary command on the host.
  * **CVE-2026-53492 (Critical)** : CRI implementation improperly trusts Container Device Interface (CDI) annotations during container restoration. This allows an attacker to inject arbitrary CDI configurations (such as host mounts and device nodes) into restored containers, bypassing resource allocation and device plugin enforcement.
  * **CVE-2026-53489 (High)** : CRI plugin restores container.log without validating a symlinked path, allowing an attacker to read arbitrary host files via kubectl logs.
  * **CVE-2026-47262 (Moderate)** : A vulnerability in containerd allows a maliciously crafted image to cause memory exhaustion (DoS) of the containerd process.

These vulnerabilities affect all GDC (software only) configurations using Ubuntu node images. 

#### What should I do?

For GDC software only on bare metal, the following patches will contain fixes for the vulnerabilities issue:

  * 1.34.800 
  * 1.33.1100

| High  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
