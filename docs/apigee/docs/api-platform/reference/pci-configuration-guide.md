---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/pci-configuration-guide/
title: PCI Configuration Guide for Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:39:14.907607+00:00
---

# PCI Configuration Guide for Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/pci-configuration-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Resources ](https://docs.cloud.google.com/apigee/docs/release-notes)



Send feedback 

#  PCI Configuration Guide for Apigee Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

For a customer to be Payment Card Industry (PCI) compliant on Apigee, there are some actions and processes the customer owns under the "Shared Responsibility Model." The following items should be reviewed by customers who are seeking to be PCI compliant. These items are self-service within Apigee and need to be addressed for the customer organization (org) to meet PCI requirements. The overarching concept is "Google secures the platform, the customer secures their data." 

## PCI Requirements Mapping

The following table maps PCI requirements to related Apigee documentation. For more information about the requirements, see [ PCI DSS v4.0.1 Quick Reference Guide](https://docs-prv.pcisecuritystandards.org/PCI%20DSS/Standard/PCI-DSS-v4_0_1.pdf). 

**PCI Requirement** | **Section**  
---|---  
Requirement 3: Protect stored account data  | Data masking  
Requirement 3: Protect stored account data  | Data storage  
Requirement 4: Protect cardholder data with strong cryptography during transmission over open, public networks  | TLS configuration  
Requirement 4: Protect cardholder data with strong cryptography during transmission over open, public networks  | Data encryption  
Requirement 7: Restrict access to system components and cardholder data by business need to know  | Use/Authorizations  
Requirement 8: Identify users and authenticate access to system components  | Complex password requirements or SAML  
Requirement 10: Log and monitor all access to system components and cardholder data  | Audit trail  
Requirement 11: Test security of systems and networks regularly  | Endpoint scanning  
  
To obtain a PCI Data Security Standard Attestation of Compliance (AOC), please visit [Google Compliance Report Manager](https://cloud.google.com/security/compliance/compliance-reports-manager#/ProductArea=Apigee) or contact your Apigee sales team. 

## Debug Sessions

Debug Sessions is a troubleshooting tool that allows the user to view the status and contents of an API call as it is processed through the Apigee platform. 

During a Debug session, Data masking is enforced. Data Masking can block data from being displayed during a Debug session. See the Data Masking section below. 

Detailed instructions on the use of Debug are available at [Using Debug](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace). 

## Use/Authorizations

Access to Debug Session is managed through the Cloud IAM (Identity Access Management) RBAC (Role-Based Access Control) system. Detailed instructions on using the RBAC system to give and revoke Debug Session privileges are available at [Apigee roles](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/apigee-roles) and [Manage users in the Apigee UI](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/manage-users). Debug Session permissions allow the user to launch a Debug Session, access the output from a debug session. 

Since Debug Session has access to the payload of API calls (formally called the "Message Body"), it's important to consider who has access to run a Debug Session. Because user management is a customer responsibility, the granting of Debug Session permissions is also a customer responsibility. 

## Data masking

Data masking prevents the display of sensitive data during a Debug session only, both in the Debug tool (Apigee UI) and in the backend by Debug (Apigee API). Details of how to set up masking are available at [Data masking and hiding](https://docs.cloud.google.com/apigee/docs/api-platform/security/data-masking). Masking sensitive data is part of [PCI Requirement 3 - Protect stored account data](https://docs-prv.pcisecuritystandards.org/PCI%20DSS/Standard/PCI-DSS-v4_0_1.pdf). 

Data masking does NOT prevent the data from being visible in places such as log files, the cache, and analytics. Sensitive data should typically not be written to cache or analytics without a strong business justification and review by customer security and legal teams. 

## Caching

Caching is available to all customers. For more information, see [Cache internals](https://docs.cloud.google.com/apigee/docs/api-platform/cache/cache-internals). 

## Audit trail

Customers have the ability to review the audit trail of all administrative activities performed within the customer's org, including the use of Debug. For detailed instructions, see [Audit logging](https://docs.cloud.google.com/apigee/docs/api-platform/debug/audit-logs) and [Using Debug](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace). ([PCI Requirement 10: Log and monitor all access to system components and cardholder data](https://docs-prv.pcisecuritystandards.org/PCI%20DSS/Standard/PCI-DSS-v4_0_1.pdf)). 

## Complex password requirements or SAML

For PCI customers, user passwords are configured to meet most requirements as mandated by PCI DSS. Cloud Identity also offers multi-factor authentication ([PCI Requirement 8: Identify users and authenticate access to system components](https://docs-prv.pcisecuritystandards.org/PCI%20DSS/Standard/PCI-DSS-v4_0_1.pdf)). SAML as described at [SAML Overview](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/saml-overview), can be used as an alternative for authentication controls. 

**Note:** Customers with specific password requirements are recommended to use SAML to meet their individual requirements. 

## Endpoint security

### Endpoint scanning

Scanning and testing of hosts is required for PCI compliance ([Requirement 11: Test security of systems and networks regularly](https://docs-prv.pcisecuritystandards.org/PCI%20DSS/Standard/PCI-DSS-v4_0_1.pdf)). For Apigee, customers are responsible for the scanning and testing of their API endpoints (sometimes called the "runtime components") in Apigee. Customer testing should cover the actual API proxy services hosted on Apigee where API traffic is sent into Apigee prior to being processed and then delivered to the customer datacenter. Testing of shared resources, such as the management portal UI, is not approved for individual customers (a third party report covering testing of the shared services is available to customers under a non-disclosure agreement and upon request). 

Customers should, and are encouraged to, test their API endpoints. Your agreement with Apigee does not prohibit testing of your API endpoints, but we don't permit you to test the shared management UI. Notification to Apigee in advance is appreciated so that we can be aware of the testing traffic. 

Customers testing their endpoints should look for any API-specific issues, any issues related to Apigee services, and also check on the TLS and other configurable items. Any items that are found related to Apigee services should be communicated to Apigee through a support request. 

Most items related to the endpoint are customer self-service items and can be fixed by reviewing the Apigeee documentation. If there are items where it is unclear how to fix them, please open a support request. 

### TLS configuration

As per [PCI standards](https://blog.pcisecuritystandards.org/migrating-from-ssl-and-early-tls), SSL and early TLS need to be migrated to secured versions. Customers are responsible for defining and configuring their own TLS endpoints for API proxies. This is a self-service feature in Apigee. Customer requirements around encryption, protocol, and algorithm selections are widely variable and specific to individual use cases. Because Apigee does not know the details of every customer's API design and data payloads, customers have the responsibility to determine appropriate encryption for data in transit. Detailed instructions on TLS configuration are available at [TLS/SSL](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/options-configuring-tls). 

## Data storage

Storage of data within Apigee is not required for Apigee to function properly. However, there are services available for data storage in Apigee. Customers may choose to use cache, key value maps, or analytics for data storage. Analytics is not authorized for storage of Card Holder Data (CHD) per the Apigee PCI audit. Per [PCI Requirement 3 (Protect stored account data)](https://docs-prv.pcisecuritystandards.org/PCI%20DSS/Standard/PCI-DSS-v4_0_1.pdf), PCI data should be stored only in PCI compliant locations. Use of these services is available to customers for storing non-PCI data or other unrestricted data subject to the customer's security and legal requirements. These services are customer self-service items, so it is the customer's responsibility to configure them not to capture or store CHD. Reviews of configuration, policies, and deployments by customer administrators is recommended to avoid accidental or malicious use of data storage services in Apigee in a non-compliant manner . 

## Data encryption

Data encryption tools are not offered to customers for their use inside of Apigee. However, customers are free to encrypt their PCI data prior to sending to Apigee. [PCI Requirement 4: (Protect cardholder data with strong cryptography during transmission over open, public networks)](https://docs-prv.pcisecuritystandards.org/PCI%20DSS/Standard/PCI-DSS-v4_0_1.pdf) recommends to encrypt cardholder data across open, public networks. Encrypted data in the payload (or Message Body) does not prevent Apigee from functioning. Some Apigee policies may be unable to interact with the data if it is received encrypted by the customer. For example, a transformation is not possible if the data itself is not available to Apigee to change. But other policies and customer-built policies and bundles will work even if the data payload is encrypted. 

## Data Capture

Customers can use the [Data Capture policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/data-capture-policy) to send custom attributes to the Apigee analytics platform. Apigee recommends not using Data Capture for storing card holder information. 

## Information exposure through query strings in URL

Apigee recommends API designs that avoid sensitive data (including, but not restricted to cardholder information) through query strings in URLs. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
