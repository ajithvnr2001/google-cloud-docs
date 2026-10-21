---
url: https://docs.cloud.google.com/certificate-manager/docs/v2/roles/
title: Roles and permissions \u00a0|\u00a0 Certificate Manager (2nd gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:57:17.267894+00:00
---

# Roles and permissions  |  Certificate Manager (2nd gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/v2/roles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager)
  * [ Certificate Manager (2nd gen) ](https://docs.cloud.google.com/certificate-manager/docs/v2/overview)



Send feedback 

#  Roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

****

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Understand the Identity and Access Management (IAM) predefined roles and permissions required to securely manage and control access to your Certificate Manager (2nd gen) resources. These resources include observed certificates, issuance configurations, and trust configurations. IAM permissions let you control who can create, view, update, or delete these resources at the project level or higher. For permissions related to load balancer resources, see [IAM roles and permissions for load balancing](https://docs.cloud.google.com/certificate-manager/docs/permissions).

## Predefined roles

IAM provides predefined roles that let you grant granular access to specific Google Cloud resources and prevent unauthorized access to other resources.

The following table describes predefined roles that include permissions for Certificate Manager (2nd gen) resources.

Role | Description  
---|---  
Certificate Manager Editor role  
(`roles/certificatemanager.editor`) | Grants read and write access to Certificate Manager resources, including Certificate Manager (2nd gen) resources like issuance configurations, trust configurations, and observed certificates.  
Certificate Manager Viewer role  
(`roles/certificatemanager.viewer`) | Grants read-only access to Certificate Manager resources, including Certificate Manager (2nd gen) resources like issuance configurations, trust configurations, and observed certificates.  
  
## Permissions

The following table lists permissions for Certificate Manager (2nd gen) resources. These permissions are included in the Certificate Manager Editor role (`roles/certificatemanager.editor`) and the Certificate Manager Viewer role (`roles/certificatemanager.viewer`).

Permission | Description  
---|---  
`certificatemanager.observedcerts.get` | View details of an observed certificate in the inventory.  
`certificatemanager.observedcerts.list` | List observed certificates in the inventory.  
`certificatemanager.certs.create` | Create a certificate.  
`certificatemanager.certs.list` | List certificates.  
`certificatemanager.certs.get` | View details of a certificate.  
`certificatemanager.certs.update` | Update a certificate.  
`certificatemanager.certs.use` | Associate a certificate with a resource.  
`certificatemanager.certs.delete` | Delete a certificate.  
`certificatemanager.certmaps.create` | Create a certificate map.  
`certificatemanager.certmaps.list` | List certificate maps.  
`certificatemanager.certmaps.get` | View details of a certificate map.  
`certificatemanager.certmaps.update` | Update a certificate map.  
`certificatemanager.certmaps.use` | Attach a certificate map to a resource.  
`certificatemanager.certmaps.delete` | Delete a certificate map.  
`certificatemanager.certmapentries.create` | Create a certificate map entry.  
`certificatemanager.certmapentries.list` | List certificate map entries.  
`certificatemanager.certmapentries.get` | View details of a certificate map entry.  
`certificatemanager.certmapentries.update` | Update a certificate map entry.  
`certificatemanager.certmapentries.delete` | Delete a certificate map entry.  
`certificatemanager.dnsauthorizations.create` | Create a DNS authorization.  
`certificatemanager.dnsauthorizations.list` | List DNS authorizations.  
`certificatemanager.dnsauthorizations.get` | View details of a DNS authorization.  
`certificatemanager.dnsauthorizations.update` | Update a DNS authorization.  
`certificatemanager.dnsauthorizations.delete` | Delete a DNS authorization.  
`certificatemanager.certissuanceconfigs.create` | Create a certificate issuance config.  
`certificatemanager.certissuanceconfigs.list` | List certificate issuance configs.  
`certificatemanager.certissuanceconfigs.get` | View a certificate issuance config.  
`certificatemanager.certissuanceconfigs.delete` | Delete a certificate issuance config.  
`certificatemanager.trustconfigs.create` | Create a trust config.  
`certificatemanager.trustconfigs.list` | List trust configs.  
`certificatemanager.trustconfigs.update` | Update a trust config.  
`certificatemanager.trustconfigs.get` | View details of a trust config.  
`certificatemanager.trustconfigs.use` | Associate a trust config with a resource.  
`certificatemanager.trustconfigs.delete` | Delete a trust config.  
  
## What's next

  * [Issue a certificate using CA Service and verify in Certificate Manager (2nd gen)](https://docs.cloud.google.com/certificate-manager/docs/v2/quickstart-ca-service)
  * [Automate certificate lifecycle for load balancers](https://docs.cloud.google.com/certificate-manager/docs/v2/quickstart-lb-certificates)
  * [Configure lifecycle management for managed workloads](https://docs.cloud.google.com/certificate-manager/docs/v2/configure-managed-workloads)
  * [Configure lifecycle management for load balancers](https://docs.cloud.google.com/certificate-manager/docs/v2/configure-load-balancers)
  * [View certificate inventory](https://docs.cloud.google.com/certificate-manager/docs/v2/inventory)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
