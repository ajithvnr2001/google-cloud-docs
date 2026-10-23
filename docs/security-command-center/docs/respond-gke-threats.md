---
url: https://docs.cloud.google.com/security-command-center/docs/respond-gke-threats/
title: Respond to Google Kubernetes Engine threat findings \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:17:45.477928+00:00
---

# Respond to Google Kubernetes Engine threat findings  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/respond-gke-threats/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Respond to Google Kubernetes Engine threat findings Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This document offers informal guidance on how you can respond to findings of suspicious activities in your Google Kubernetes Engine resources. The recommended steps might not be appropriate for all findings and might impact your operations. Before you take any action, you should investigate the findings; assess the information that you gather; and decide how to respond.

**Note:** The techniques that Security Command Center provides aren't guaranteed to be effective against any previous, current, or future threats that you face. For information about why Security Command Center does not provide official remediation guidance for threats, see [Approach to threat finding remediation](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats#remediating_threats).

## Before you begin

  1. [Review the finding](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats#reviewing_findings). Review the affected Google Kubernetes Engine resource, the detected principal email, and the caller IP address (if present). Also review the finding for indicators of compromise (IP, domain, file hash, or signature).
  2. To learn more about the finding that you're investigating, search for the finding in the [Threat findings index](https://docs.cloud.google.com/security-command-center/docs/threat-findings-index).



## General recommendations

  * Contact the owner of the project that contains the potentially compromised resource.
  * Determine whether there are other signs of malicious activity related to the affected GKE resource in the audit logs in Cloud Logging.
  * Stop or delete the compromised GKE resource and replace it with a new one.
  * Determine whether there are other signs of malicious activity by the principal in the audit logs in Cloud Logging.
  * If the principal is a service account (IAM or Kubernetes), identify the source of the modification to determine its legitimacy.
  * If the principal that conducted the action isn't a service account, contact the owner of the account to confirm whether the legitimate owner conducted the action.
  * Review the [guidance on the principle of least privilege](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/rbac#least-privilege) for the RBAC roles and cluster roles.



In addition, consider the recommendations in the following sections.

## Added binary or library

If the added binary, script, or library was intended to be included in the container, rebuild the container image with the binary, script, or library included. For information about immutable container images, see [Container images](https://kubernetes.io/docs/concepts/containers#container-images) in the Kubernetes documentation.

## Threats related to Kubernetes certificate signing requests (CSR)

  * Review the audit logs in Cloud Logging and additional alerts for other CSR-related events. Determine whether the CSR was approved and issued and whether the CSR-related actions are expected from the principal.
  * If a CSR approval was unexpected or is determined to be malicious, the cluster requires a credential rotation to invalidate the certificate. Review the guidance for [rotating your cluster credentials](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/credential-rotation).



## Threat findings for Pods

  * Review the manifest file of the Pod and its purpose. Verify that the Pod is legitimate and necessary.
  * If the Pod is illegitimate, remove it along with any associated RBAC bindings and service accounts that the workload used.



## What's next

  * Learn [how to work with threat findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats).
  * Refer to the [Threat findings index](https://docs.cloud.google.com/security-command-center/docs/threat-findings-index).
  * Learn how to [review a finding](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats#reviewing_findings) through the Google Cloud console.
  * Learn about the [services that generate threat findings](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#threats).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
