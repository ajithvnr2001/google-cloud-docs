---
url: https://docs.cloud.google.com/security-command-center/docs/troubleshooting/
title: Troubleshooting steps \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:44:18.294526+00:00
---

# Troubleshooting steps  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Troubleshooting steps Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

Learn about troubleshooting steps that might be helpful if you experience the following problems while using Security Command Center.

**Note:** For more troubleshooting information, see [Error messages](https://docs.cloud.google.com/security-command-center/docs/error-messages). In addition, Security Command Center provides error detectors, which report configuration errors that prevent Security Command Center and its services from working properly. Each error finding includes suggested remediation steps. For more information, see [Security Command Center errors](https://docs.cloud.google.com/security-command-center/docs/concepts-scc-errors).

## Enabling Security Command Center fails

Enabling Security Command Center most commonly fails if your organization policies [restrict identities by domain](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains). You and your service account must be part of an allowed domain:

  * Make sure you sign in to an account that's in an allowed domain before you try to enable Security Command Center.
  * If you're using an `@*.gserviceaccount.com` service account, add the service account as an identity in a group within an allowed domain.



## Assets in Security Command Center aren't updating

If you're using VPC Service Controls, assets in Security Command Center can only be discovered and updated when you grant access to the Security Command Center service account.

To enable asset discovery, [grant access](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-health-analytics#service-perimeter) to the Security Command Center service account. This allows the service account to complete asset discovery and display assets in the Google Cloud console. The service account name is in the form of `service-org-organization-id@security-center-api.iam.gserviceaccount.com`.

## Viewing, editing, creating, and updating findings and assets

The IAM roles for Security Command Center can be granted at the organization, folder, or project level. Your ability to view, edit, create, or update findings, assets, and security sources depends on the level that you're granted access for. To learn more about Security Command Center roles, see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control). 

## Missing or delayed notifications

In some situations, notifications might be missing, dropped, or delayed:

  * There might not be any findings that match the filters in your `NotificationConfig`. To test notifications, use the Security Command Center API to [create a finding](https://docs.cloud.google.com/security-command-center/docs/how-to-api-create-manage-findings#creating_a_finding).
  * The Security Command Center service account must have the `securitycenter.notificationServiceAgent` role on the Pub/Sub topic. The service account name is in the form of `service-organization-id@gcp-sa-scc-notification.iam.gserviceaccount.com`. 
    * If you remove the role, notification publishing is disabled.
    * If you remove the role and then grant the role again, notifications are delayed.
  * If you delete and recreate the Pub/Sub topic, notifications will be dropped.



## External Exposure

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The following sections describe troubleshooting steps that you might find helpful if you experience issues or unexpected traffic that is related to External Exposure.

### Spikes in `403 Forbidden` request logs from `TsunamiSecurityScanner`

You observe unexpected spikes in HTTP `403 Forbidden` or HTTP `401 Unauthorized` request logs on your public-facing endpoints, such as Cloud Run, Google Kubernetes Engine (GKE), or Cloud Load Balancing, with the user agent `TsunamiSecurityScanner`.

#### Cause

When External Exposure scans your public IP addresses and endpoints to detect exposed interfaces and vulnerabilities, the service sends probe requests using the user agent string `TsunamiSecurityScanner`.

If your endpoints or services enforce access controls, such as Identity and Access Management (IAM) authentication, Identity-Aware Proxy (IAP), or Google Cloud Armor security policies, the endpoints reject unauthenticated scanner requests. These rejections generate an HTTP `403 Forbidden` or HTTP `401 Unauthorized` log response. This behavior is expected and indicates that your security controls are blocking unauthenticated access.

#### Diagnose and resolve

To diagnose and resolve spikes in HTTP `403 Forbidden` or HTTP `401 Unauthorized` request logs from `TsunamiSecurityScanner`, follow these steps:

  1. To verify whether the HTTP `403` request logs originate from the scanner, on the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/building-queries) page, run the following query:
         
         httpRequest.userAgent="TsunamiSecurityScanner" AND httpRequest.status=403
         

  2. Confirm that the scanned services reside in projects where External Exposure is active. For more information about how scanner traffic appears in your logs, see [Identify scanner traffic in your logs](https://docs.cloud.google.com/security-command-center/docs/detect-external-exposure#identify-scanner-traffic).

  3. Optional: If you have log-based alerts configured that trigger on HTTP `403` status codes, update the alert query to exclude scanner traffic:
         
         NOT httpRequest.userAgent="TsunamiSecurityScanner"
         




## Web Security Scanner

This section contains troubleshooting steps that you might find helpful if you have problems using Web Security Scanner

### Scan errors for Compute Engine and GKE

If the URL for a scan is misconfigured, Web Security Scanner rejects it. Possible reasons for rejection include:

#### URL has an IP address that is ephemeral

Mark this IP address as static:

  * For an application on a single VM, reserve the IP address on the VM
  * For an application behind a load balancer, reserve the IP address on the load balancer.



#### URL is mapped to a wrong IP address

To fix this finding, refer to the instructions from your DNS registrar service.

#### URL is mapped to an ephemeral IP address of the same VM

Mark this IP address as static.

#### URL is mapped to a reserved IP address

This error happens when the URL is mapped to an IP address that's reserved in a different project of the same organization. To resolve this, define security scans for the VM or HTTP load balancer in the project for which it is defined.

#### URL is mapped to more than one IP address

Make sure that all IP addresses that are mapped to this URL are reserved for the same project. If there is at least one IP address that isn't reserved for the same project, the Scan Create or Edit or Update operation fails.

## What's next

Learn about [Security Command Center errors](https://docs.cloud.google.com/security-command-center/docs/concepts-scc-errors).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
