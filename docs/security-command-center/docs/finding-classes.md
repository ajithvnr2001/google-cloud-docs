---
url: https://docs.cloud.google.com/security-command-center/docs/finding-classes/
title: Finding classes \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:10.393708+00:00
---

# Finding classes  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/finding-classes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Finding classes Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page explains the finding classes that the Security Command Center services use to report security issues in your environment.

In finding definitions, the finding class is stored in the `findingClass` field. For more information about the `findingClass` field, see [`FindingClass`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources.findings#findingclass).

Some findings don't include a finding class definition. Security Command Center classifies these findings as `Finding class unspecified`.

The classes include the following:

  * `Chokepoint`
  * `External exposure` ([Preview](https://cloud.google.com/products/#product-launch-stages))
  * `Misconfiguration`
  * `Observation`
  * `Posture violation`
  * `SCC Error`
  * `Secret` ([Preview](https://cloud.google.com/products/#product-launch-stages))
  * `Threat`
  * `Toxic combination`
  * `Vulnerability`
  * `Finding class unspecified`



## `Chokepoint` class

Findings in the `Chokepoint` class identify a resource or resource group where high-risk attack paths converge, based on attack path simulations.

Remediating a chokepoint finding might remediate multiple toxic combinations.

For more information about `Chokepoint` class findings, see [Toxic combinations and chokepoints overview](https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-overview).

## `External exposure` class

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Findings in the `External exposure` class identify external-facing IP addresses, hostnames, domain names, URLs, and exposed services on your resources that are confirmed to be reachable from the public internet.

For more information about `External exposure` class findings, see [Detect exposed resources](https://docs.cloud.google.com/security-command-center/docs/detect-external-exposure).

## `Misconfiguration` class

Findings in the `Misconfiguration` class identify security weaknesses that are caused by the incorrect or suboptimal configuration of cloud resources, assets, or policies. In most cases, you can fix the problem by updating the configuration that is indicated in the finding.

Findings in the `Misconfiguration` class are distinct from findings in the `Vulnerability` class, which describe software program flaws or Common Vulnerabilities and Exposures (CVEs). Misconfiguration findings from built-in Security Command Center services, such as Security Health Analytics, are documented in [Security Health Analytics findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#security-health-analytics-detectors).

## `Observation` class

Findings in the `Observation` class describe an event, configuration detail, or other issue in your environment that might not be a problem in itself, but could be if your environment were to be compromised. 

Security Command Center services that commonly generate observations include the following:

  * [Sensitive Data Protection](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#dlp)

  * [Sensitive Actions Service](https://docs.cloud.google.com/security-command-center/docs/concepts-sensitive-actions-overview)

  * [AI Protection](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#ma-observations)




## `Posture violation` class

Findings in the `Posture violation` class describe resource configurations that don't align with your organization's [security posture](https://docs.cloud.google.com/security-command-center/docs/security-posture-overview) or a [Compliance Manager cloud control](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview).

## `SCC error` class

Findings in the `SCC error` class identify a problem in the configuration of Security Command Center or one of its services that prevents Security Command Center from detecting security issues in your Google Cloud environment.

For more information about findings in the `SCC error` class, see [Overview of Security Command Center errors](https://docs.cloud.google.com/security-command-center/docs/concepts-scc-errors).

## `Secret` class

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Findings in the `Secret` class identify potential security risks caused by plaintext credentials, keys, access tokens, or certificates in container images that run on Gemini Enterprise Agent Platform.

For more information about these findings, see [Agent Platform Vulnerability Assessment](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#aevs).

## `Threat` class

Findings in the `Threat` class identify a potential active attack or other unwanted or malicious activity.

Findings in the `Threat` class should be investigated immediately.

For more information about findings in the `Threat` class, see [Approach to threat finding remediation](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats#remediating_threats).

## `Toxic combination` class

Findings in the `Toxic combination` class identify a group of security issues that, when they occur together, create a path to one or more of your high-value resources that a determined attacker could potentially use to reach and compromise those resources.

For more information about `Toxic combination` class findings, see [Toxic combinations and chokepoints overview](https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-overview).

## `Vulnerability` class

Findings in the `Vulnerability` class identify a flaw or weakness in software programs that an attacker could use to gain access to or otherwise compromise your Google Cloud environment.

For more information about findings in the `Vulnerability` class, see [Vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings).

## `Finding class unspecified` class

Findings in the `Finding class unspecified` class either don't have a value specified on the `findingClass` property or don't include the property at all.

To determine whether the finding identifies a threat, vulnerability, or other class of security issue, you need to review the finding and investigate the issue that it identifies.

Typically, the service that generates the finding determines the finding class and sets the `findingClass` property. We recommend that integrated and third-party service providers set the `findingClass` property, but doing so is not required.

## What's next

  * Learn how to view toxic combinations and chokepoints on the [Issues page](https://docs.cloud.google.com/security-command-center/docs/issues-overview).

  * Learn how to [assess risk using Risk overview dashboards](https://docs.cloud.google.com/security-command-center/docs/assess-risk).

  * Learn how to [investigate and respond to threats](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats).

  * Learn how to [monitor your frameworks for compliance](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-monitor-framework) in Compliance Manager.

  * Learn how to manage a security posture using [Security posture service](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
