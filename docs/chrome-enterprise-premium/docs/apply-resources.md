---
url: https://docs.cloud.google.com/chrome-enterprise-premium/docs/apply-resources/
title: Quickstart: Apply Chrome Enterprise Premium to cloud resources \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:21.657459+00:00
---

# Quickstart: Apply Chrome Enterprise Premium to cloud resources  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chrome-enterprise-premium/docs/apply-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Chrome Enterprise Premium ](https://docs.cloud.google.com/chrome-enterprise-premium/docs)
  * [ Guides ](https://docs.cloud.google.com/chrome-enterprise-premium/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Apply Chrome Enterprise Premium to cloud resources

This page walks through the high level steps of applying Chrome Enterprise Premium to your Google Cloud and on-premises resources.

For information about how Chrome Enterprise Premium leverages other Google Cloud offerings, see the [Chrome Enterprise Premium access protection overview](https://docs.cloud.google.com/chrome-enterprise-premium/docs/overview).

## Before you begin

Before you make your apps and resources context-aware, you'll need to:

  1. If you don't already have [Cloud Identity](https://docs.cloud.google.com/identity) user accounts in your organization, [create a few Cloud Identity accounts](https://support.google.com/cloudidentity/answer/7332836?hl=en).

  2. Determine a resource you want to protect. Configure one of the following if you don't have a resource.

     * A web app running behind an [HTTPS load balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https) on Google Cloud. This includes web apps like App Engine apps, apps running on-premises, and apps running in another cloud.
     * A virtual machine on Google Cloud.
  3. Determine principals that you want to grant and limit access to.




If you're interested in securing Google Workspace apps, see the [Google Workspace Chrome Enterprise Premium overview](https://support.google.com/a/answer/9275380?hl=en).

## Securing your apps and resources with IAP

Identity-Aware Proxy (IAP) establishes a central identity awareness layer for apps and resources accessed by HTTPS and TCP. This means you can control access on each individual app and resource instead of using network-level firewalls.

Secure your Google Cloud app and all its resources by selecting one of the following guides:

  * [App Engine standard and flexible environment](https://docs.cloud.google.com/chrome-enterprise-premium/docs/securing-app-engine)
  * [Compute Engine](https://docs.cloud.google.com/chrome-enterprise-premium/docs/securing-compute-engine)
  * [Google Kubernetes Engine](https://docs.cloud.google.com/chrome-enterprise-premium/docs/securing-kubernetes-engine)



You can also extend IAP to non-Google Cloud environments like on-premises as well as other clouds. To learn more, see the [Securing on-premises apps](https://docs.cloud.google.com/chrome-enterprise-premium/docs/securing-on-premises) guide.

For more information, see the [IAP documentation](https://docs.cloud.google.com/iap/docs).

### Virtual machine resources

You can control access to administrative services like SSH and RDP on your backends by setting tunnel resource permissions and creating tunnels that route TCP traffic through IAP to virtual machine instances.

To secure a virtual machine, see the [Securing virtual machines](https://docs.cloud.google.com/chrome-enterprise-premium/docs/securing-virtual-machines) guide.

## Creating an access level with Access Context Manager

Once you've secured your apps and resources with IAP, it's time to set richer access policies with [access levels](https://docs.cloud.google.com/access-context-manager/docs/overview#access-levels).

[Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs/overview) creates access levels. Access levels can limit access based on the following attributes:

  * [IP subnetworks](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes#ip-subnetworks)
  * [Regions](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes#regions)
  * [Access level dependency](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes#access-level-dependency)
  * [Principals](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes#members)
  * [Device policy](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes#device-policy) (Note that [Endpoint Verification](https://docs.cloud.google.com/chrome-enterprise-premium/docs/apply-resources#enable-endpoint-verification) must be set up.)



Create an access level by following the [Creating an access levels](https://docs.cloud.google.com/chrome-enterprise-premium/docs/access-levels#creating-an-access-level) guide.

## Applying access levels

An access level doesn't take effect until you apply it on a IAP-secured resources' Identity and Access Management (IAM) policy. This step is done by adding an [IAM Condition](https://docs.cloud.google.com/chrome-enterprise-premium/docs/access-protection#applying-cloud-iam-conditions) on the IAP role used to grant access to your resource.

To apply your access level, see [applying access levels](https://docs.cloud.google.com/chrome-enterprise-premium/docs/access-levels#applying_an_access_level).

Once you've applied your access level, your resources are now secured with Chrome Enterprise Premium.

## Enabling device trust and security with Endpoint Verification

To further strengthen the security of your Chrome Enterprise Premium secured resources, you can apply device-based trust and security access control attributes with access levels. [Endpoint Verification](https://docs.cloud.google.com/chrome-enterprise-premium/docs/access-protection#Gathering-device-information) enables this control.

Endpoint Verification is a Chrome extension for Windows, Mac, and Chrome OS devices. [Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs/overview) references the device attributes gathered by Endpoint Verification to enforce fine grained access control with [access levels](https://docs.cloud.google.com/access-context-manager/docs/overview#access-levels).

Follow the [Endpoint Verification quickstart](https://docs.cloud.google.com/endpoint-verification/docs/quickstart) to set up Endpoint Verification for your organization.

## What's next

  * Learn how to view [Context-Aware Access logs in Cloud Audit Logs](https://docs.cloud.google.com/access-context-manager/docs/audit-logs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
