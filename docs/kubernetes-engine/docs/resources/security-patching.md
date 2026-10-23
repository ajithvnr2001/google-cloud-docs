---
url: https://docs.cloud.google.com/kubernetes-engine/docs/resources/security-patching/
title: Security patching \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:14.344244+00:00
---

# Security patching  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/resources/security-patching/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Security patching Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes how Google manages security vulnerabilities and patches for Google Kubernetes Engine (GKE). This information might be useful for [Security specialists](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks#security) who support the resolution of security issues or vulnerabilities that need strategic assistance, such as incidents and issues escalated from support.

## Patching shared responsibility

Patching is a shared responsibility between Google and the customer, as described in [GKE shared responsibility](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/shared-responsibility).

## How we discover vulnerabilities

Google has made large investments in proactive security design and hardening, but even the best designed software systems can have vulnerabilities. To find those vulnerabilities and patch them before they can be exploited, Google has made significant investments on multiple fronts.

For patching purposes, GKE is an Operating System (OS) layer with containers running on top. The operating systems, Container-Optimized OS or Ubuntu, are hardened and contain the minimum amount of software required to run containers. GKE features run as containers on top of the base images. GKE consistently works to reduce the number of dependencies that system components have, which helps to reduce the attack surface and improve the efficiency of vulnerability management. For example, GKE system components might use minimal base images when possible.

Google identifies and fixes vulnerabilities and missing patches in the following ways:

  * Container-Optimized OS: Google scans images to identify potential vulnerabilities and missing patches. The Container-Optimized OS team reviews and resolves issues.

  * Ubuntu: Canonical provides Google with OS builds that have all available security patches applied.




Google scans containers using [Container Registry Artifact Analysis](https://docs.cloud.google.com/artifact-registry/docs/analysis) to discover vulnerabilities and missing patches in Kubernetes and Google-managed containers. If fixes are available, the scanner automatically begins the patching and release process.

In addition to automated scanning, Google discovers and patches vulnerabilities _unknown to scanners_ in the following ways.

Google performs its own audits, penetration testing, and vulnerability discovery across all platforms. For a list of platforms, see the previous section [Patching shared responsibility](https://docs.cloud.google.com/kubernetes-engine/docs/resources/security-patching#patching_shared_responsibility).

Specialized teams inside Google and trusted third-party security vendors conduct their own attack research. Google has also worked with the [CNCF](https://www.cncf.io/) to provide much of the organization and technical consulting expertise for the [Kubernetes security audit](https://github.com/trailofbits/audit-kubernetes/blob/master/reports/Kubernetes%20Security%20Review.pdf).

Google actively engages with the security research community through [multiple vulnerability reward programs](https://www.google.com/about/appsecurity/programs-home/). A dedicated Google Cloud vulnerability rewards program provides significant bounties, [including $133,337 for the best cloud vulnerability](https://security.googleblog.com/2020/03/announcing-our-first-gcp-vrp-prize.html) found each year. For GKE, there is a program that rewards security researchers if they are able to [break our security controls](https://security.googleblog.com/2020/05/expanding-our-work-with-open-source.html). The program covers all GKE software dependencies.

Google collaborates with other industry and open source software partners who share vulnerabilities, security research, and patches before the public release of the vulnerability. The goal of this collaboration is to patch large pieces of Internet infrastructure before the vulnerability is announced to the public. In some cases, Google contributes vulnerabilities found to this community. For example, Google's Project Zero discovered and publicized the [Spectre and Meltdown](https://blog.google/topics/google-cloud/what-google-cloud-g-suite-and-chrome-customers-need-know-about-industry-wide-cpu-vulnerability/) vulnerabilities. The Google Cloud Security team also regularly finds and fixes [vulnerabilities in the Kernel-based Virtual Machine (KVM)](https://cloud.google.com/blog/products/gcp/7-ways-we-harden-our-kvm-hypervisor-at-google-cloud-security-in-plaintext).

Google's security collaboration happens on many levels. Sometimes it occurs formally through programs where organizations sign up to receive pre-release notifications about software vulnerabilities for products such as [Kubernetes](https://github.com/kubernetes/security/blob/master/private-distributors-list.md) and [Envoy](https://github.com/envoyproxy/envoy/security/policy#private-distributors-list). Collaboration also happens informally due to our engagement with many open source projects such as the Linux kernel, container runtimes, virtualization technology, and others.

For Kubernetes, Google is an active and founding member of the [Security Response Committee (SRC)](https://github.com/kubernetes/committee-security-response) and wrote much of the [Security Release Process](https://github.com/kubernetes/security/blob/master/security-release-process.md). Google is a member of the [Kubernetes Distributors List](https://github.com/kubernetes/security/blob/master/private-distributors-list.md) that receives prior notification of vulnerabilities and has been involved in the triage, patching, mitigation development, and communication of nearly every serious Kubernetes security vulnerability. Google also discovered multiple Kubernetes vulnerabilities, such as [CVE-2019-11254](https://github.com/kubernetes/kubernetes/issues/89535), [CVE-2019-11255](https://github.com/kubernetes/kubernetes/issues/85233), and [CVE-2021-25741](https://github.com/kubernetes/kubernetes/issues/104980).

While less severe vulnerabilities are discovered and patched outside of these processes, most critical security vulnerabilities are reported privately through one of the channels previously listed. Early reporting gives Google time before the vulnerability becomes public to research how it affects GKE, develop patches or mitigations, and prepare advice and communications for customers. When possible, Google patches all clusters before the public release of the vulnerability.

## How vulnerabilities are classified

GKE makes large investments in security hardening the entire stack, including the OS, container, Kubernetes, and network layers, in addition to setting good defaults, security-hardened configurations, and managed components. Combined, these efforts help to reduce the impact and likelihood of vulnerabilities.

The GKE security team classifies vulnerabilities according to the [Kubernetes vulnerability scoring](https://github.com/kubernetes/committee-security-response/blob/main/severity-ratings.md) system. Classifications consider many factors including GKE configuration and security hardening. Because of these factors and the investments GKE makes in security, GKE vulnerability classifications might differ from other classification sources.

The following table describes vulnerability severity categories:

**Severity** | **Description**  
---|---  
Critical | A vulnerability easily exploitable in _all_ clusters by an unauthenticated remote attacker that leads to full system compromise.   
High | A vulnerability easily exploitable for _many_ clusters that leads to loss of confidentiality, integrity, or availability.  
Medium | A vulnerability exploitable for _some_ clusters where loss of confidentiality, integrity, or availability is limited by common configurations, difficulty of the exploit itself, required access, or user interaction.  
Low | All other vulnerabilities. Exploitation is unlikely or consequences of exploitation are limited.  
  
See the [security bulletins](https://docs.cloud.google.com/kubernetes-engine/docs/security-bulletins) for example vulnerabilities, fixes and mitigations, and their ratings.

**Note:** Starting on May 7, 2026, GKE classifies most Linux kernel container breakout vulnerabilities as Medium severity. Information about these vulnerabilities and others will continue to be published in [the GKE release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes). The release notes link to detailed vulnerability patching information, such as the [Container-Optimized OS release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes). Prior to this date, GKE classified all Linux kernel container breakout vulnerabilities as High. The updated classification of Medium is more appropriate, because an application vulnerability must typically be exploited before an attacker can gain execution access in the container and exploit a breakout vulnerability. Untrusted code shouldn't rely on the container security boundary, and should use [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods). GKE continues to patch these vulnerabilities as a priority and continues to use our insights into the exploitation of several years worth of container breakouts [collected through our vulnerability rewards program](https://security.googleblog.com/2023/06/learnings-from-kctf-vrps-42-linux.html) to improve kernel security upstream.

## How vulnerabilities are patched for GKE clusters

Patching a vulnerability involves upgrading to a new GKE version number. GKE versions include versioned components for the operating system, Kubernetes components, and other containers that make up the GKE platform. Fixing some vulnerabilities requires only a control plane upgrade, performed automatically by Google on GKE, while others require both control plane and node upgrades.

To keep clusters hardened against vulnerabilities of all severities, we recommend following the [best practices for GKE cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/upgrading-clusters) to help ensure that your cluster receives security patches in a timely manner.

Google recommends upgrading Kubernetes clusters at least monthly. For a list of platforms, see the previous section [Patching shared responsibility](https://docs.cloud.google.com/kubernetes-engine/docs/resources/security-patching#patching_shared_responsibility).

Some security scanners or manual version checks might incorrectly assume that a component like runc or containerd is missing a specific upstream security patch. GKE regularly patches components and only performs package version upgrades when required, which means that GKE components are functionally similar to their upstream counterparts even if the version number of the GKE component doesn't match the upstream version number. For details about a specific CVE, see [GKE security bulletins](https://docs.cloud.google.com/kubernetes-engine/security-bulletins).

## Patching timelines

Google's goal is to mitigate detected vulnerabilities within a time period appropriate for the risks they represent. GKE is included within [Google Cloud's FedRAMP provisional ATO](https://cloud.google.com/security/compliance/fedramp) which requires that known vulnerabilities to be remediated within specific timeframes according to their severity level as specified in control RA-5(d) of the Risk Assessment (RA) record RA-5, "Vulnerability Scanning", in the [FedRAMP Security Controls Baseline](https://www.fedramp.gov/resources/documents/FedRAMP_Security_Controls_Baseline.xlsx) spreadsheet.

For every known vulnerability, GKE's goal is to release patch versions that remediate the vulnerability within the corresponding timeframe. After GKE makes patch versions available to remediate a known vulnerability, upgrade your clusters to those versions to meet patching timeframes for your organization.

## How vulnerabilities and patches are communicated

The best sources for current information about vulnerabilities and security patches for GKE are the [security bulletins](https://docs.cloud.google.com/kubernetes-engine/security-bulletins) and [release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes).

Starting on June 1, 2026, GKE doesn't publish security bulletins for Google Distributed Cloud (software only), GKE on AWS, or GKE on Azure. To view more recent security bulletins and vulnerability fixes for these products, see the following documents:

  * [Distributed Cloud (software only) security bulletins](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/security-bulletins)
  * [GKE on AWS release notes](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/release-notes)
  * [GKE on Azure release notes](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/release-notes)

**Caution:** GKE on AWS and GKE on Azure are in maintenance mode and will be shut down on March 17, 2027.



Vulnerabilities are sometimes kept private under embargoes for a limited time. Embargoes help prevent early publication of vulnerabilities that might lead to widespread exploitation attempts before steps can be taken to address them. In embargo situations, the release notes refer to "security updates" until the embargo has been lifted. After the embargo is lifted, Google updates release notes to include the specific vulnerabilities.

The GKE security team publishes security bulletins for High and Critical severity vulnerabilities. In addition, Google might also contact customers through [Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts) or through applicable Support channels.

## What's the fastest way to get a security patch installed?

All clusters will automatically stay patched with [GKE auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades). This section describes how to patch faster than auto-upgrades for specific security fixes, or on an ongoing basis. By combining test environments, cross-channel manual upgrades, accelerated patch settings, and event-driven notifications, you can reduce patching lead times.

GKE manages version rollouts across release channels to ensure new versions are qualified and soaked. To reduce your patching lead times, you need to understand how these rollouts work, and then tailor the default behavior to meet your specific needs.

Soaking a patched version involves running it on clusters over time to observe stability. This process helps catch bugs that only appear after prolonged use across diverse environments. To ensure sufficient soak time, GKE patch releases are introduced first to the [Rapid channel, followed by Regular and Stable](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#channels). Releases are also soaked in each channel before becoming the upgrade target for the channel.

### Qualify patches early and manage rollout with rollout sequencing

To qualify a security patch that you want to accelerate, [use rollout sequencing to roll out across environments](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/upgrading-clusters#use-rollout-sequencing), testing a patch in other GKE clusters before upgrading the production environment. This approach lets you verify workload compatibility, and catch any problems as soon as a security fix is released by Google. Then, you can apply the patched version to the rest of your fleet and control the remaining soak time.

### Reduce soak delays with accelerated patch auto-upgrades

Alternatively, you can choose to consume patches faster by enabling [accelerated patch auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#accelerated-patch) for your clusters. This feature tells GKE to bypass the in-channel soak time for patch updates, particularly security patches. If you use this approach, Google recommends running a test cluster on the Rapid channel (also with [accelerated patch auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#accelerated-patch)) to qualify patches.

**Note:** If you enable accelerated patch auto-upgrades for a cluster enrolled in a rollout sequence, the cluster bypasses the rollout sequence's staging and soak periods and upgrades immediately when the patch version is available.

### Manual upgrades to newer patch versions in Regular and Stable channels

If your production workloads are on clusters enrolled in the Regular or Stable channels, _you don't need to leave those channels_ or wait for the automatic, phased rollout of a patch to reach you if there is a specific security update you need to prioritize.

If you have qualified the patched version, [you can manually initiate](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions) upgrades on your clusters in Regular or Stable to that exact patch version to control the remaining soak time.

### Automate patching management with cluster notifications

It is not necessary to monitor the security bulletins web page for patch information. To get fast programmatic notifications of available patches and trigger patch qualification and upgrade actions, you can use [cluster notifications](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications).

To get notifications for security bulletins or scheduled upgrades, configure your notifications to specifically filter for the following event types:

  * [SecurityBulletinEvent](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications#securitybulletin)
  * [UpgradeEvent](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications#upgradeevent)



Cluster notifications let you receive real-time messages when these events occur. You can integrate these notifications into your security information and event management (SIEM) systems, chat operations, or trigger automated test pipelines.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
