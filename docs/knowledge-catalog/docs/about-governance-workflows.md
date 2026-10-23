---
url: https://docs.cloud.google.com/knowledge-catalog/docs/about-governance-workflows/
title: About governance workflows \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:50:49.224427+00:00
---

# About governance workflows  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/about-governance-workflows/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  About governance workflows Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Governance workflows in Knowledge Catalog let you set up automated controls and approval mechanisms for organizational data resources. You can then route requests to authorized individuals or teams to manage access to your data products.

## Benefits

Using governance workflows for managing access requests has the following benefits:

  * Data consumers can find relevant data products and request access directly within Knowledge Catalog, replacing manual support ticketing processes.
  * Upon request approval, the system automatically grants the required IAM roles and group memberships, eliminating manual administrative overhead and reducing time-to-access.
  * System logs capture complete audit trails of all requests, justifications, approver decisions, and timestamps to simplify regulatory compliance auditing.
  * Centralized approval mechanisms for sensitive data assets ensure access is restricted to authorized users and teams.



## Use cases

Governance workflows support automated access management across various industry scenarios:

  * **Retail and e-commerce:** A marketing manager requests access to a regional sales data product (for example, a curated `theLook eCommerce` dataset) to analyze customer behavior and build a targeted ad campaign. Upon approval, the required IAM roles are automatically provisioned.
  * **Healthcare:** A clinical research analyst requests access to a de-identified patient outcomes data product (for example, a curated anonymized patient records dataset) to evaluate treatment efficacy across patient demographics. Upon approval, the required IAM roles are automatically provisioned.
  * **Finance:** A risk analyst requests access to a transaction history data product (for example, an aggregated credit activity and fraud monitoring dataset) to build predictive risk models and ensure compliance auditing. Upon approval, the required IAM roles are automatically provisioned.



In each use case, the system provides the required IAM roles when the approver accepts the request.

## Use governance workflows in Knowledge Catalog

You can use governance workflows to request access to data products and suggest changes to business glossaries and Knowledge Catalog entries.

For more information on how to request access to data products, see [request access to data products](https://docs.cloud.google.com/knowledge-catalog/docs/use-data-products#request-access).

**Note:** Requesting metadata changes to business glossaries and Knowledge Catalog entries with governance workflows is available in **private preview**. To request access to the feature, fill in the following [access form](https://forms.gle/eFMGqsaKTUJ62mrR7).

## Governance workflows processing path

Knowledge Catalog tracks requests throughout their lifecycle using workflow status values (`NEW`, `APPROVED`, `REJECTED`, `DELETED`).

The following table lists the steps in the request processing path, their corresponding status values, and descriptions:

Step | Status | Description  
---|---|---  
**Request creation** | `NEW` | A requester submits a new request (for example, to access a data product). The system logs the request and assigns it the `NEW` status.  
**Review** | `NEW` | The request remains in `NEW` status while awaiting evaluation by an authorized approver.  
**Approver decision** | `APPROVED` or `REJECTED` | The approver evaluates the request and decides to approve or reject it: 

  * **Request approved** : The system automatically provisions the requested access or applies the metadata changes, and notifies the requester by email.
  * **Request rejected** : The status updates to `REJECTED`. The requester receives an email with the decision justification.

  
**Expiration or deletion** | `DELETED` | A request transitions to `DELETED` in the following scenarios: 

  * The request remains unaddressed in `NEW` status for the 90-day time to live (TTL) period.
  * The target resource associated with a pending request is deleted.
  * A requester or workflow administrator manually deletes the request.

  
  
## Governance workflows roles

Governance workflows roles include requesters, approvers, and workflow administrators. The following table describes the roles in detail:

Role | Description  
---|---  
**Requester** | A requester creates and submits requests.  
**Approver** | An approver approves or rejects requests.  
**Workflow administrator** | Ensures compliance, configures workflow policies, and maintains the request backlog. Administrators can view audit trails across all request states and have administrative deletion permissions to remove requests in any state.  
  
## Limitations

  * Governance workflows aren't supported for [Assured Workload](https://docs.cloud.google.com/assured-workloads/docs/overview) projects.
  * Governance workflows don't support [customer-managed encryption keys](https://docs.cloud.google.com/knowledge-catalog/docs/cmek).



## What's next

  * Learn how to [manage requests](https://docs.cloud.google.com/knowledge-catalog/docs/manage-requests).
  * Learn how to [request access to data products](https://docs.cloud.google.com/knowledge-catalog/docs/use-data-products#request-access).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
