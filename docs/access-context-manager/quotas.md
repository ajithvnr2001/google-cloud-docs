---
url: https://docs.cloud.google.com/access-context-manager/quotas/
title: Quotas and limits \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:46:18.397919+00:00
---

# Quotas and limits  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Resources ](https://docs.cloud.google.com/access-context-manager/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document contains the content limits for the Access Context Manager API. The content limits specified in this document are subject to change.

For quotas and limits for service perimeters, a component of VPC Service Controls, see the [VPC Service Controls documentation](https://docs.cloud.google.com/vpc-service-controls/quotas).

Access Context Manager enforces the following limits:

  * Read requests per minute: A read request is an operation that reads an Access Context Manager resource, such as an access level. The limit is 500 requests per minute per organization.

  * Write requests per minute: A write request is an operation that creates or modifies an Access Context Manager resource, such as an access level. The limit is 50 requests per minute per organization.

  * Access policies per organization: One organization-level policy and a maximum of 50 scoped policies can exist for an organization.

  * Access levels per access policy: 500

  * Conditions per access level: 40

  * List items per access level attribute (for example, the number of CIDR ranges you can include for the IP Subnetworks attribute): 200

  * VPC networks across all access levels per access policy: 500




The following limits apply specifically to custom access levels:

  * Maximum CEL list length: 200

**Note:** The limits specified in this document are system constraints and cannot be increased.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
