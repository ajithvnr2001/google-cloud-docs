---
url: https://docs.cloud.google.com/architecture/migrate-across-regions/
title: Migrate across Google Cloud regions: Get started \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:06.369776+00:00
---

# Migrate across Google Cloud regions: Get started  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/migrate-across-regions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Migrate across Google Cloud regions: Get started Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-12-08 UTC

This document series helps you prepare for migrating your workloads and data across Google Cloud [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). In this series, you learn how to design reliable, single-region environments, and how to set up security and compliance controls to help ensure that your workloads and data stay inside specific Google Cloud regions. This series also provides guidance on how to expand your environment to multiple regions. This series is useful if you're planning to do any of these actions, or if you're evaluating the opportunity to do so in the future and want to explore what it might look like.

This document is part of the following series:

  * Get started (this document)
  * [Design resilient single-region environments on Google Cloud](https://docs.cloud.google.com/architecture/migrate-across-regions/design-resilient-single-region-environments)
  * [Architect your workloads](https://docs.cloud.google.com/architecture/migrate-across-regions/architect-workloads)
  * [Prepare data and batch workloads for the migration](https://docs.cloud.google.com/architecture/migrate-across-regions/prepare-data-and-batch-workloads)



This series assumes that you have read and are familiar with [Migrate to Google Cloud: Get started](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started), which describes the general migration framework used in this series. This series is also part of a larger set of migration content. For an overview of all related migration content, see [Migration resources](https://docs.cloud.google.com/architecture/migrations).

Use the following list to help you get started with the documents in this series and with related migration content:

  * **Architecting your environments for reliability.** When designing your Google Cloud environments, there are several architectural choices to make, including how to distribute resources across Google Cloud regions and zones. For more information about how to design your Google Cloud environments, and about how to design reliable single-region environments, refer to [Design resilient single-region environments on Google Cloud](https://docs.cloud.google.com/architecture/migrate-across-regions/design-resilient-single-region-environments).
  * **Preparing for and migrating across Google Cloud regions**. Preparing for a migration across Google Cloud regions helps you avoid potential issues during such a migration, and also reduces the time and effort required to complete the migration. For example, you might want to prepare for a future migration to another region because you don't yet know if a particular region would be the best fit for your environment. Or you might prepare for a migration because you anticipate that your requirements about the preferred region might change in the future. You might even prepare for a migration because you're considering a migration to a soon-to-be-opened region.

The guidance in this series is also useful if you didn't plan in advance for a migration across regions or for an expansion to multiple regions. In this case, you might need to spend additional effort to prepare your infrastructure, workloads, and data for the migration across regions and for the expansion to multiple regions.

For more information about preparing for a migration across Google Cloud regions, see the following documents:

    * [Design resilient single-region environments](https://docs.cloud.google.com/architecture/migrate-across-regions/design-resilient-single-region-environments)
    * [Prepare data and batch workloads for migration across regions](https://docs.cloud.google.com/architecture/migrate-across-regions/prepare-data-and-batch-workloads)
  * **Setting up boundaries, and security and compliance controls to ensure that your workloads and data stay inside certain Google Cloud regions**. You might have to comply with security and regulatory requirements so that your workloads and data can only reside in specific Google Cloud regions. If you have this compliance requirement, you might need to implement boundaries, controls, and auditing to ensure locality, sovereignty, privacy, and confidentiality on top of the [guarantees that Google Cloud offers](https://docs.cloud.google.com/security). For example, you might need to make your environment compliant with regulations and security requirements that mandate certain workloads and data never leave a specific region residing in a particular political, administrative, or state entity.

  * **Minimizing the costs of your single- and multi-region environments, and of migrations across Google Cloud regions**. As your environments and your Google Cloud footprint grow, you might consider implementing mechanisms and processes to control and reduce the costs that are associated with your environments and your migrations across regions. For example, you can provision resources in specific regions, optimize network traffic patterns, streamline and automate processes, and automatically scale resources with demand. For more information about reducing costs, refer to [Migrate to Google Cloud: Minimize costs](https://docs.cloud.google.com/architecture/migration-to-google-cloud-minimize-costs).




## What's next

  * Learn how to [design resilient single-region environments on Google Cloud](https://docs.cloud.google.com/architecture/migrate-across-regions/design-resilient-single-region-environments).
  * Learn how to [prepare data and batch workloads for the migration](https://docs.cloud.google.com/architecture/migrate-across-regions/prepare-data-and-batch-workloads).
  * Learn how to [minimize costs](https://docs.cloud.google.com/architecture/migration-to-google-cloud-minimize-costs) of your Google Cloud environment and your migration across regions.
  * Read [an in-depth analysis of deployment archetypes for cloud applications](https://docs.cloud.google.com/architecture/deployment-archetypes).
  * Learn about the migration framework by reading [Migrate to Google Cloud: Get started](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started).
  * Learn where to [find help for your migrations](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started#finding_help).
  * Take the [Google Skills training course on migrating to Google Cloud](https://www.skills.google/course_templates/1561).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Marco Ferrari](https://www.linkedin.com/in/ferrarimark) | Cloud Solutions Architect

Other contributor: [Lee Gates](https://www.linkedin.com/in/gatesl) | Group Product Manager

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-12-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-12-08 UTC."],[],[]] 
