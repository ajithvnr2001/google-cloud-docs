---
url: https://docs.cloud.google.com/docs/security/gcmvsp/organization/
title: Organization guidelines \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:11.645222+00:00
---

# Organization guidelines  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/gcmvsp/organization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Organization guidelines Stay organized with collections  Save and categorize content based on your preferences. 

The following guidelines for the minimum viable security platform align with the organization security pillar.

## Intermediate level guidelines

After you implemented the basic guidelines, implement the following organization guidelines.

Item | 

### Restrict authorized principals  
  
---|---  
Description | Ensure only identities from your organization are allowed in your Google Cloud environment. Use the **Domain restricted sharing** (`iam.allowedPolicyMemberDomains`) or the `iam.managed.allowedPolicyMembers` organization policy constraint to define one or more Cloud Identity or Google Workspace customer IDs whose principals can be added to Identity and Access Management (IAM) policies.These constraints help prevent employees from granting access to external accounts outside of your organization's control that don't follow your security policies for multifactor authentication (MFA) or password management. This control is critical for preventing unauthorized access, ensuring that only trusted, managed corporate identities can be used.  
Related information | 

  * [Restricting identities by domain](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains)

  
Item ID | MVSP-CO-1.21  
Mapping |  Related NIST-800-53 controls:

  * AC-3
  * AC-17
  * AC-20

Related CRI profile controls:

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.PT-3.1
  * PR.PT-4.1

Compliance Manager control:

  * [Enforce Domain Restricted Sharing](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enforce-domain-restricted-sharing)

  
  
## Advanced level guidelines

After you implemented the intermediate guidelines, implement the following organization guidelines.

Item | 

### Restrict resource locations  
  
---|---  
Description | The Resource Location Restriction (`gcp.resourceLocations`) constraint ensures that only your approved Google Cloud regions are used to store data. The value is specific to your systems and matches your organization's approved list of regions for data residency.This constraint lets your organization enforce that your resources and data are only created and saved in specific, approved geographic regions.  
Related information | 

  * [Restricting resource locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations)

  
Item ID | MVSP-CO-1.22  
Mapping |  Related NIST-800-53 controls:

  * AC-3
  * AC-17
  * AC-20

Related CRI profile controls:

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.PT-3.1
  * PR.PT-4.1

  
Item | 

### Restrict resource service usage  
  
---|---  
Description | The `gcp.restrictServiceUsage` constraint ensures that only your approved Google Cloud services are used in the right places. For example, a production or highly sensitive folder has a small list of Google Cloud services that are approved to store data. A sandbox folder might have a larger list of services and accompanying data security controls to help prevent data exfiltration. The value is specific to your systems and matches your approved list of services and dependencies for specific folders and projects.This constraint lets your organization create an allowlist of approved services, which helps prevent employees from using unvetted services.  
Related information | 

  * [Restricting resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources)

  
Item ID | MVSP-CO-1.23  
Mapping |  Related NIST-800-53 controls:

  * AC-3
  * AC-17
  * AC-20

Related CRI profile controls:

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.PT-3.1
  * PR.PT-4.1

Compliance Manager control:

  * [Restrict Resource Service Usage](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-resource-service-usage)

  
  
## What's next

  * [Infrastructure guidelines](https://docs.cloud.google.com/docs/security/gcmvsp/infrastructure)
  * [Overview of minimum viable secure platform](https://docs.cloud.google.com/docs/security/gcmvsp)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
