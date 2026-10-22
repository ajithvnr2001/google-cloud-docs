---
url: https://docs.cloud.google.com/firewall/docs/about-app-layer-inspection/
title: Application layer inspection overview \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:34.766865+00:00
---

# Application layer inspection overview  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/about-app-layer-inspection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Application layer inspection overview Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Next Generation Firewall (Cloud NGFW) application layer inspection provides advanced protection for your Google Cloud resources. Application layer inspection, also known as deep packet inspection or Layer 7 inspection, is a security process that examines the content of network packets as they pass through the firewall.

This document describes the services and components used for application layer inspection in Cloud NGFW.

## Application layer inspection services

Cloud NGFW offers the following application layer inspection services: Intrusion detection and prevention service, Advanced malware sandbox (WildFire) ([Preview](https://cloud.google.com/products#product-launch-stages)), and URL filtering service. Application layer inspection features are available in the Cloud NGFW Enterprise tier. For more information, see [Cloud NGFW Enterprise](https://docs.cloud.google.com/firewall/docs/ngfw_tiers#ngfw-tiers-enterprise).

### Intrusion detection and prevention service

The Intrusion detection and prevention service continuously monitors your Google Cloud workload traffic for malicious activity and takes preemptive actions to prevent it. Malicious activity includes threats such as intrusions, malware, spyware, and command-and-control attacks on your network. For more information, see [Intrusion detection and prevention service overview](https://docs.cloud.google.com/firewall/docs/about-intrusion-prevention).

### Advanced malware sandbox

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Advanced malware sandbox service for Cloud NGFW provides malware protection using inline machine learning (ML) and cloud-based behavioral sandboxing. Powered by Palo Alto Networks Advanced WildFire, the service extends standard signature-based intrusion detection and prevention service by evaluating suspicious files in real time to prevent zero-day threats from reaching your workloads. For more information, see [Advanced malware sandbox overview](https://docs.cloud.google.com/firewall/docs/about-wildfire).

### URL filtering service

URL filtering service lets you control access to websites by blocking or allowing specific URLs. This service can use Server Name Indication (SNI) to filter by domain. For more information, see [URL filtering service overview](https://docs.cloud.google.com/firewall/docs/about-url-filtering).

## Core components

Application layer inspection services use the following components:

  * **Firewall endpoints** and **firewall endpoint associations** : A firewall endpoint is a Google-managed zonal resource that performs deep packet inspection in your network. A firewall endpoint association links a firewall endpoint to a zone of a Virtual Private Cloud (VPC) network. You create one endpoint per zone in the region where you want to inspect traffic. For more information, see [Firewall endpoint overview](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints).

To inspect the contents of encrypted traffic, create a TLS inspection policy and add the policy to the firewall endpoint association. For more information, see [TLS inspection overview](https://docs.cloud.google.com/firewall/docs/about-tls-inspection).

  * **Security profiles** : an object that contains the configuration for a specific security service. Firewall endpoints use security profiles to scan intercepted traffic. For more information, see [Security profiles overview](https://docs.cloud.google.com/firewall/docs/about-security-profiles).

Cloud NGFW supports the following types of security profiles:

    * `THREAT_PREVENTION`: configures the intrusion detection and prevention service.
    * `WILDFIRE_ANALYSIS`: configures the Advanced malware sandbox.
    * `URL_FILTERING`: defines rules for the URL filtering service.
  * **Security profile group** : a container for security profiles. A security profile group can only contain one security profile of each type. For more information, see [Security profile group overview](https://docs.cloud.google.com/firewall/docs/about-security-profile-groups).

  * **`apply_security_profile_group` action**: a firewall rule action that redirects the intercepted traffic to a firewall endpoint for inspection. For more information, see [Action on match](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#action_on_match).




To understand how the core components work together, see [How intrusion detection and prevention service works](https://docs.cloud.google.com/firewall/docs/about-intrusion-prevention#how-ips-works), [How Advanced malware sandbox works](https://docs.cloud.google.com/firewall/docs/about-wildfire#how-it-works), and [How URL filtering service works](https://docs.cloud.google.com/firewall/docs/about-url-filtering#how-url-filtering-works).

## Organization-level and project-level resources

You can create and configure application layer inspection components at the organization level or at the project level. Organization-level resources apply across the organization through hierarchical firewall policies. Project-level resources apply only between projects with global network firewall policies.

  * To enforce mandatory, organization-wide security policies, use organization-level resources.
  * To manage rules for a specific application, use project-level resources.



The following table compares the characteristics of organization-level and project-level resources:

Feature | Organization-level resources | Project-level resources  
---|---|---  
Permissions | Require organization-level Identity and Access Management (IAM) roles to configure. | Require project-level IAM roles to configure.  
Hierarchical policies | Can be referenced by hierarchical firewall policies. | Can't be referenced by hierarchical firewall policies.  
Scope | Organization-level security profile groups apply automatically to all firewall endpoints in the organization. | Project-level security profile groups apply only to firewall endpoints within their specific project. You can't apply them across projects.  
Billing | Firewall endpoint uptime bills to a designated billing project that you provide. | Firewall endpoint uptime bills directly to the project that owns the resource.  
  
## Limitations

  * Project-level security profile groups apply only to firewall endpoints in the same project. You can't apply them across projects.

  * You can't migrate a project that contains project-level resources to a different organization.

  * You can associate a VPC network with only one firewall endpoint per zone. For each zone, you must use either a project-level or an organization-level endpoint.

  * If you associate a VPC network with a project-level firewall endpoint in a different project, both projects must be in the same organization.




## What's next

  * [Intrusion detection and prevention service overview](https://docs.cloud.google.com/firewall/docs/about-intrusion-prevention)
  * [Advanced malware sandbox overview](https://docs.cloud.google.com/firewall/docs/about-wildfire)
  * [URL filtering service overview](https://docs.cloud.google.com/firewall/docs/about-url-filtering)
  * [TLS inspection overview](https://docs.cloud.google.com/firewall/docs/about-tls-inspection)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
