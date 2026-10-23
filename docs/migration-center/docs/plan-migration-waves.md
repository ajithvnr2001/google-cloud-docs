---
url: https://docs.cloud.google.com/migration-center/docs/plan-migration-waves/
title: Plan your migration waves \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:49.413395+00:00
---

# Plan your migration waves  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/plan-migration-waves/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Plan your migration waves Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to plan your migration waves.

You can group migration candidates into migration waves. Grouping can be done at a high-level (category-based) or detailed-level (applications, locations, components), based on the information you collect during the discovery and assessment phase.

## Create an application catalog

To start your planning, create an [application catalog](https://docs.cloud.google.com/architecture/migration-to-gcp-assessing-and-discovering-your-workloads#example_of_an_app_catalog). Organize your applications into categories based on application architecture, business considerations, and IT operations. This helps prioritize them according to business criticality, complexity and risks involved in moving to the cloud. The combination and prioritization of these factors vary across organizations, their business imperatives, and the mapping of these imperatives to workloads, both in their current architecture, and the future Google Cloud architecture.

The following list presents the three main categories and the factors that you need to consider within each category.

  * **Application architecture**

    * Technical constraints
    * Number of dependencies
    * Number of tiers
    * Stateful vs stateless
    * Performance requirements
    * Geographic dependencies
  * **Business considerations**

    * Compliance requirements
    * Business criticality
    * Business change capability
    * Number of users
    * Type of users (internal, external)
    * TCO
  * **IT operations**

    * Operating environment
    * Service level agreement
    * Availability
    * Backup



![Dimensions to be considered for application catalog.](https://docs.cloud.google.com/static/migration-center/images/migration-planning-application-catalog.png)

## Map and prioritize

From the application catalog, map out applications based on the complexity and target migration approach. Your migration approach should be based on the business outcomes you expect, the migration effort, and the associated risk factors, both during and after migration.

Then, rank migration candidates in order of priority, based on business value and the effort required to migrate. To prepare for your migration, identify apps with features that make them likely to be moved first. You can pick just one, or include many apps in your first wave. The apps in the first wave let your teams test the deployment in the cloud environment, while focusing on the migration instead of on the complexity of the apps.

Starting with a standalone app lowers your initial risk because later you can apply your team's new knowledge to applications that are more complex and have many dependencies.

Apps in the first wave typically are not business critical and have fewer system and network-to-network dependencies. They also require less refactoring, usually have less data gravity, don't have specific compliance challenges, and can afford a cutover window. For more details, see how to [choose the apps to migrate first](https://docs.cloud.google.com/architecture/migration-to-gcp-assessing-and-discovering-your-workloads#choosing_the_apps_to_migrate_first).

![Mapping applications by complexity.](https://docs.cloud.google.com/static/migration-center/images/migration-planning-map-prioritize.png)

## Group applications in waves

Group applications into multiple waves with timelines associated with each wave, along with the time to revise plans based on the feedback from each wave.

  * **Wave 1** : High business value, low effort to implement. 
    * _These applications are ideal candidates for early migrations or proof-of-concepts._
  * **Wave 2** : High business value, high effort to implement. 
    * _These applications may be prioritized next._
  * **Wave 3** : Low business value, low effort to implement. 
    * _These applications may be prioritized next._
  * **Wave 4** : Low business value, high effort to implement. 
    * _These applications should be prioritized last._



![Planning migration waves.](https://docs.cloud.google.com/static/migration-center/images/migration-planning-waves.png)

After you have defined your migration waves, you can organize them in a project plan.

![Migration timeline and project plan.](https://docs.cloud.google.com/static/migration-center/images/migration-planning-timeline.png)

## Follow the best practices

To improve your migration plan, follow the [best practices to validate a migration plan](https://docs.cloud.google.com/architecture/migration-to-google-cloud-best-practices). Following the concepts in that document does not give any guarantees for success. However, the document highlights some points that are often overlooked when planning migrations, such as:

  1. Ensuring that you have a rollback strategy for each step of the migration plan.
  2. Planning for gradual rollout and deployments, as discussed earlier in this document.
  3. Alerting all the development and operations teams that are responsible for the workloads to migrate.
  4. Removing proof-of-concept resources and experiments from the target production environment.
  5. Defining criteria to safely retire the source environment.
  6. Ensuring that you conduct a migration risk assessment for each migration wave and execute mitigations for the risks identified.



## What's next

  * Learn how to [execute a migration](https://docs.cloud.google.com/migration-center/docs/migration-execution).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
