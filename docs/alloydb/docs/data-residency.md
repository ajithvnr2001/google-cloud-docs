---
url: https://docs.cloud.google.com/alloydb/docs/data-residency/
title: Enforce data residency requirements \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:54.962067+00:00
---

# Enforce data residency requirements  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/data-residency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Enforce data residency requirements Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to configure AlloyDB for PostgreSQL to enforce data residency requirements.

## Overview of data residency

_Data residency_ refers to the physical location of data, and the local regulations that govern how you store, encrypt, and access that data. As countries' data protections and privacy regulations evolve, it's increasingly important that you understand how to follow local data residency requirements and protect your users' data.

In a traditional on-premises environment, you configure various components to handle data residency. For example, a company can host a tokenization gateway as a cloud access security broker (CASB) to secure application data before it's transmitted overseas.

Because a cloud computing service stores your data off-premises, cloud computing introduces its own data residency issues and questions. These include the following:

  * If a company's cloud administrators don't know the physical location of the data, then they don't know the local regulations. To research the data residency policies for each location, administrators need to know where the data centers are.
  * A company's cloud administrators and providers might use service-level agreements (SLAs) that establish allowed locations, requiring restrictions on the range of regions that the cloud service can use for data storage.
  * Users must ensure that their data, and all of the services and resources that they use in their cloud projects, follow the data residency regulations of the host country.



## Data residency for AlloyDB

Data residency involves storing personally identifiable information (PII) or other sensitive information within a particular region, in a way that meets that region's laws and regulations.

To store data, you must meet a country's legal and regulatory demands, such as data locality laws. For example, a country might mandate that any government-related data be stored in that country. Or, a company might be contractually obligated to store data for some of their customers in a different country. Therefore, a company has to meet the data residency requirements of the country where the data is stored.

You can use the [Cloud Asset Inventory (CAI)](https://docs.cloud.google.com/asset-inventory) service to view and monitor the locations of resources across [services supported by it](https://docs.cloud.google.com/asset-inventory/docs/supported-asset-types), which includes AlloyDB.

AlloyDB helps you with your data residency requirements by letting you specify the location of your data, and constrain which locations that AlloyDB makes available.

### Location selection

With Google Cloud, you choose where your data is stored. This includes letting you choose the [regions](https://docs.cloud.google.com/alloydb/docs/locations) where you store your data. When you configure AlloyDB resources in these regions, Google stores your data at rest only in these regions, according to our [Service Specific Terms](https://cloud.google.com/terms/service-terms). You can select the region when you create your cluster. Any instances and backups created against a cluster is stored in the same region as the cluster.

### Resource locations constraint

You can use organizational policy constraints to enforce data residency requirements at the organization, project, or folder level. These constraints let you define the Google Cloud locations where users can create resources for supported services. For data residency, you can use the [resource locations constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) to limit the physical location of new [supported AlloyDB resources](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services#AlloyDB). You can also fine-tune policies for a constraint to specify regions, such as `us-east1` or `europe-west1`, as allowed or denied locations. Existing location violations can be [discovered using Security Health Analytics](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations#vulnerability_findings_and_remediation) and then remediated.

## What's next

  * For more information about Google Cloud data location commitments, see the Google Cloud [Service Specific Terms](https://cloud.google.com/terms/service-terms).

  * To learn more about data residency in Google Cloud, see [Understanding your options for data residency, operational transparency, and privacy controls on Google Cloud](https://cloud.google.com/blog/products/identity-security/meet-data-residency-requirements-with-google-cloud).

  * To learn more about how Google Cloud protects customer data throughout its lifecycle, and how Google Cloud provides customers with transparency and control over their data, see [Trusting your data with Google Cloud](https://services.google.com/fh/files/misc/072022_google_cloud_trust_whitepaper.pdf).

  * Learn about best practices for [data residency](https://docs.cloud.google.com/architecture/framework/security/meet-regulatory-compliance-and-privacy-needs#control_data_residency) and [data sovereignty](https://docs.cloud.google.com/architecture/framework/security/meet-regulatory-compliance-and-privacy-needs#recommendations_to_manage_your_data_sovereignty).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
