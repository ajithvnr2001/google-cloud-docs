---
url: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/release-notes/
title: Enterprise Knowledge Graph release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:11:36.044617+00:00
---

# Enterprise Knowledge Graph release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Enterprise Knowledge Graph ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs)
  * [ Resources ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/quotas)



Send feedback 

#  Enterprise Knowledge Graph release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Enterprise Knowledge Graph. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

## October 10, 2022

Announcement

[Enterprise Knowledge Graph](https://docs.cloud.google.com/enterprise-knowledge-graph/docs) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

Feature

Enterprise Knowledge Graph API has been updated with the following features:

  * Support to [cancel](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/reference/rest/v1/projects.locations.entityReconciliationJobs/cancel) and [delete](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/reference/rest/v1/projects.locations.entityReconciliationJobs/delete) an entity reconciliation job
  * Support for [three entity types](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/schema): `Organization`, `LocalBusiness`, and `Person`.
  * Entity linking to Google Knowledge Graph is available for `Organization` and `LocalBusiness` entity types.



## May 24, 2022

Feature

Enterprise Knowledge Graph API has been updated with the following features:

  * Added a [model](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/entity-reconciliation-console#configure_a_reconciliation_job) that is fine tuned for the `Organization` type.
  * For entity reconciliation jobs, you can [select different models by name and version tag](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/reference/rest/v1/projects.locations.entityReconciliationJobs#modelconfig).
  * Increased [geocoding](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/reference/rest/v1/projects.locations.entityReconciliationJobs#options) efficiency, reducing time to process results.



## May 02, 2022

Feature

Enterprise Knowledge Graph has been updated with the following features:

  * You can [list](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/reference/rest/v1/projects.locations.entityReconciliationJobs/list) all entity reconciliation jobs.
  * Added [additional jobs states](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/reference/rest/v1/projects.locations.entityReconciliationJobs#jobstate) to help you understand which stage the job is currently in.



## March 10, 2022

Feature

Enterprise Knowledge Graph has been updated with the following [advanced options](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/entity-reconciliation-console#advanced_ptions):

  * The entity reconciliation API supports outputting stable cluster IDs across different runs.
  * You can select the clustering algorithm for reconciliation.
  * You can enable geo enrichment and separation for better location-related clustering.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
