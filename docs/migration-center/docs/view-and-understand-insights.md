---
url: https://docs.cloud.google.com/migration-center/docs/view-and-understand-insights/
title: View and understand insights \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:43.105170+00:00
---

# View and understand insights  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/view-and-understand-insights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  View and understand insights Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the insights that Migration Center generates about your infrastructure.

Migration Center collects information from your assets with the discovery client, or from the data that you collect and upload using the database scripts. Then, it analyzes the information collected using predefined rules and automatically generates various insights based on the preferences that you define.

## View insights for server and database assets

To view insights about a specific server or database, follow these steps:

  1. Go to the **Assets** page.

[Go to Assets](https://console.cloud.google.com/migration/discovery/assets)

  2. On the assets details page, click the **Servers** or **Database deployments** tab.

  3. From the list of assets, click the asset for which you want to view insights.

  4. On the asset details page, in the **Insights** tab, review the available insights for the asset.




### Understand server migration insights

Server migration insights provide you with a technical assessment of your server workloads fit for specific transformation objectives. These insights help you determine the potential fit with a feasible Google Cloud product. These insights also inform you if there are any technical blockers that prevent you from modernizing your server assets such as virtual machine (VM) instances to a feasible Google Cloud product such as Compute Engine or Google Kubernetes Engine.

The assessment uses technical fit conditions that are evaluated against the data collected from the source workloads. The fit conditions catalog is a knowledge repository based on Google Cloud technical specifications and known technical limitations of the transformation tools to be used for performing the migration.

The **fit type** column shows you how well an asset matches a Google Cloud product for migration using the following fit scores:

  * **Fit unspecified:** there is not enough information to perform an assessment.
  * **Good fit:** no issues found, your workload is fit for transformation to the suggested Google Cloud product.
  * **No fit:** technical blockers found that prevent the migration to a Google Cloud product.
  * **Fit with effort:** some technical issues found which can be resolved with some effort to enable the migration to a Google Cloud product.



The fit level per server is performed by reviewing several fit conditions, called _fit rules_ , and their aggregated result is presented as the server level technical fit score.

Along with the feasible Google Cloud product and fit type, the insights also provide you with information such as suggested Compute Engine machine type, cores, memory, and recommendation for simultaneous multithreading (SMT).

#### Detected software

Migration Center collects information about software products installed on a specific server asset. This information helps you define the scope of your migration assessment and determine which server asset can be migrated to a product such as Compute Engine, or transformed to be deployed on a fully-managed service such as GKE.

**Important:** The detected software list might include AI-powered suggestions. Rate the suggestions with the **thumbs up** thumb_up or **thumbs down** thumb_down buttons. Migration Center uses your feedback to improve the accuracy of the suggestions.

### Understand database migration insights

Database migration insights provide you with a detailed technical assessment with the potential fit with a feasible Google Cloud database product. The **fit type** column shows you how well an asset matches a Google Cloud database product for migration using the following fit scores:

  * **Fit unspecified:** there is not enough information to perform an assessment.
  * **Good fit:** no issues found, your database is fit for migration to the suggested Google Cloud database product.
  * **No fit:** technical blockers found that prevent the migration to a Google Cloud database product.
  * **Fit with effort:** some technical issues found which can be resolved with some effort to enable the migration to a Google Cloud database product.



You can also see a list of compatibility issues between the source and target databases, along with the recommended resource allocation for the Google Cloud database product.

## What's next

  * Learn how to [create groups of assets](https://docs.cloud.google.com/migration-center/docs/create-groups).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
