---
url: https://docs.cloud.google.com/security-command-center/docs/assess-software-vulnerabilities-overview/
title: Assess software vulnerabilities overview \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:57.060870+00:00
---

# Assess software vulnerabilities overview  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/assess-software-vulnerabilities-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Assess software vulnerabilities overview Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (some features require [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

Security Command Center offers multiple services that detect vulnerabilities in containers, the operating systems and software found in VMs, and web applications. Where vulnerabilities can be detected depends on the cloud service you're using. Each service is enabled and configured independently.

## AWS

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

[**Vulnerability Assessment for AWS**](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-aws-overview): Detects vulnerabilities in the following AWS resources:

  * Software packages installed on [Amazon EC2 instances](https://aws.amazon.com/ec2/).
  * Software packages and operating system misconfigurations in Elastic Container Registry (ECR) images.



The findings from this service have a category of `SOFTWARE_VULNERABILITY`.

## Google Cloud

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (some features require [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

  * [**Artifact Registry vulnerability assessment**](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#ar-vuln-assessment): Finds vulnerabilities in container images stored in Artifact Registry or deployed to one of the following assets:

    * App Engine
    * Cloud Run job
    * Cloud Run
    * Google Kubernetes Engine cluster

The findings from this service have a category of `CONTAINER_IMAGE_VULNERABILITY`. 

  * [**Kubernetes security posture dashboard**](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#gke-security-posture-dashboard): Provides opinionated, actionable findings about potential security issues in your Google Kubernetes Engine (GKE) clusters.

The findings from this service are issued in the `VULNERABILITY` and `MISCONFIGURATION` finding classes. 

  * [**VM Manager**](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#vm_manager): Identifies vulnerabilities in operating systems that are installed on VMs, including Common Vulnerabilities and Exposures (CVEs).

The findings from this service have a category of `OS_VULNERABILITY`. Available for Premium and Enterprise (Deprecated) service tiers.

  * [**Vulnerability Assessment for Google Cloud**](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-google-cloud): Helps to discover critical and high severity software vulnerabilities in your Compute Engine VM instances without installing agents.

The findings from this service have categories of `OS_VULNERABILITY` and `SOFTWARE_VULNERABILITY`. Available for Standard, Premium, and Enterprise (Deprecated) service tiers.

  * [**Web Security Scanner**](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview): Identifies security vulnerabilities in your App Engine, GKE, and Compute Engine web applications. Available for Standard-legacy, Premium, and Enterprise (Deprecated) service tiers.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
