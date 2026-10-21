---
url: https://docs.cloud.google.com/healthcare-api/docs/fhir-access-control/
title: Access control in FHIR \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:08:04.123830+00:00
---

# Access control in FHIR  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/fhir-access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Access control in FHIR Stay organized with collections  Save and categorize content based on your preferences. 

FHIR access control is a comprehensive solution for managing access to healthcare data in FHIR stores. It provides a granular level of control over which users can access which resources, and what actions they can take on those resources. FHIR access control helps to ensure that healthcare data is only accessed by authorized users, and that it is used in a way that is consistent with the intent of the data owner.

FHIR access control is built on the following principles:

  * **Granularity** : provides a fine-grained level of control over access to data. This allows organizations to define access policies that are tailored to their specific needs.
  * **Flexibility** : adapts to meet the changing needs of organizations. This allows organizations to keep their access control policies up-to-date as their data governance requirements evolve.
  * **Scalability** : provides an integrated and streamlined approach to managing end-user consents. This provides built-in access enforcement for each EHR operation with minimal overhead.
  * **Compliance** : conforms to the FHIR specification. This ensures that organizations can use FHIR access control with any FHIR-compliant system.



FHIR access control addresses a wide range of data governance challenges, such as the following:

  * **Patient consent** : enforces patient consent to use their healthcare data. This ensures that patients are in control of how their data is used.
  * **Data sharing** : facilitates healthcare data sharing between organizations. This improves the coordination of care and supports research.
  * **Regulatory compliance** : helps organizations comply with regulatory requirements for the protection of healthcare data.



FHIR access control offers a number of benefits, including the following:

  * **Improved data security** : improves the security of healthcare data by ensuring that only authorized users can access data.
  * **Reduced risk of data breaches** : reduces the risk of data breaches by providing a centralized mechanism for data access management.
  * **Improved compliance** : helps organizations to comply with regulatory requirements for the protection of healthcare data.
  * **Increased patient trust** : ensures patient trust by giving patients control over how their data is used.



## Authorities of consent

The following four main authorities are involved in consent:

  * **Administrator authority** : establishes the framework for consent authority. They determine who can grant consent, what information must be included in a consent agreement, and how consent agreements will be enforced.
  * **Grantor authority** : an individual or organization that grants consent to access data, such as a patient or an administrator. They can provide consent agreements to grantees or delegate consent authority to others.
  * **System authority** : the ability to make authoritative assertions about the identity, application use case, and environment of a grantee. This can be used in a [zero-trust architecture](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf) to verify that a grantee has the right to access data.
  * **Grantee authority** : an individual or organization that is granted consent to access data, such as the EHR's accessor. They can provide information about their role, purpose, and environment to help the system verify their identity and authority.



The distribution of authority, the rules that govern them, and the evaluation of data elements as part of matching policies with accessors are unique to consent when compared to other forms of access control.

## Comparison with other access control systems

FHIR access control allows fine grained resource level access control, whereas Identity and Access Management (IAM) focuses on project, dataset and fhir store level permissions. [SMART-on-FHIR](https://hl7.org/fhir/smart-app-launch/2021May/) focuses on the use case of single authority with basic policies and request attributes. While SMART-on-FHIR provides some level of granularity, it's limited by single request attributes and cannot allow same level of fine-grained control as FHIR access control. Full comparisons are listed in the following table.

Capabilities | FHIR access control | [IAM](https://docs.cloud.google.com/iam/docs/conditions-overview) | [Smart-on-FHIR](https://build.fhir.org/ig/HL7/smart-app-launch/scopes-and-launch-context.html) | [Other](https://healthcaresecprivacy.blogspot.com/2022/05/explaining-fhir-consent-examples.html) on-premises solutions  
---|---|---|---|---  
Multi-authority enablement | Supported | Not Supported | Not Supported | Supported  
Multi-request attributes | Supported | Limited due to fixed attributes | Not Supported | Supported  
Dynamic fine-grained resource attributes | Supported | Not Supported | Limited by single search query | Require continual sync with data  
Comprehensive overlapping policies | Up to 200 administrator policies + 200 consents per patient | Up to 100 | `O(10)` | Bounded by serving performance  
Performance & Scalability | Supported | Not Supported | Supported | Not Supported  
In-built EHR security | Supported | Not Supported | Supported | Not Supported  
Concurrent permission change | Possible | Possible | Not Supported | Possible  
Policy administration and audit | Supported | Not Supported | Not Supported | Supported  
  
  * **Multi-authority enablement** : enable both administrators and patients, within their boundary, to grant consents / enforce policies.
  * **Multi-request attributes** : represent grantee as a set of abstract actor, purpose, and environment attributes for evaluation against consent policies.
  * **Dynamic fine-grained resource attributes** : allow applying policy enforcement / granting consent to various data elements (e.g. resource type, data source, data tag). Access can change in real time with data mutation.
  * **Comprehensive overlapping policies** : multiple consents can be enforced on a single resource with comprehensive access determination rules.
  * **Performance & Scalability**: all EHR's operations (e.g. patient-$everything, search) are performant with minimal overhead.
  * **In-built EHR security** : all EHR's operations are supported without the need for additional configuration or customization.
  * **Concurrent permission change** : when there is a permission change, existing issued credentials (e.g. access tokens) are subjected to the new permission.
  * **Policy administration and audit** : allow administrators to draft and update policies with audit trail and audit data accesses (e.g. who attempted to access what data for which purpose in which environment).



## What's next

  * [Learn about access data models and determination rules](https://docs.cloud.google.com/healthcare-api/docs/fhir-access-control-technical).
  * [Get started with using FHIR access control](https://docs.cloud.google.com/healthcare-api/docs/fhir-consent).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
