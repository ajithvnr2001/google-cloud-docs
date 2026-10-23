---
url: https://docs.cloud.google.com/migration-center/docs/migration-planning-overview/
title: About migration planning \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:38.980324+00:00
---

# About migration planning  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/migration-planning-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  About migration planning Stay organized with collections  Save and categorize content based on your preferences. 

After you complete the discovery and assessment phase, and set up your foundation design, you can start planning your migration by categorizing your workloads into _migration waves_.

This page describes how to plan a successful migration.

## Before you begin

Before you start your migration planning, complete a [workload discovery and assessment](https://docs.cloud.google.com/migration-center/docs/discovery-and-assessment-overview), and create an overall migration strategy with the following tasks:

  * Create a catalog of workloads, such as applications, services, and databases, that you want to migrate.
  * Map the workloads to infrastructure components.
  * Map the dependencies.
  * Identify high level migration and modernization paths (rehost, replatform, refactor, re-architect, replace, retire).



Then, use the [Cloud Foundation Toolkit](https://docs.cloud.google.com/docs/terraform/blueprints/terraform-blueprints) to build your foundation on Google Cloud.

The Cloud Foundation Toolkit includes resources to help you get started with the following aspects of your new cloud infrastructure:

  * Identity and Access Management
  * Resource management
  * Networking
  * Data management
  * Infrastructure as code
  * Logging, monitoring, and billing
  * Security foundations
  * GKE foundations

**Note:** [Foundations design and set up](https://docs.cloud.google.com/architecture/migration-to-google-cloud-building-your-foundation) is a preliminary step to migration planning and landing zone creation. You must tailor your migration landing zones to meet your specific use cases and application requirements. The details of the landing zone, such as IAM, networking constructs, logging, monitoring, billing, and security, are determined based on the fundamental design elements created during the foundations design phase.

## Migration concepts

A **cloud migration project** represents the entire process that your organization follows to migrate the applications to Google Cloud.

Each cloud migration project is divided into **waves**. A wave is a group of applications that share common characteristics or interdependencies, as identified by the workload discovery and assessment. Standalone applications and databases are typically good candidates for a first migration wave, given their low external dependencies. On the other hand, applications with many dependencies would constitute a complex migration wave that requires additional planning.

Applications within a migration wave are divided into **move groups** and migrated to Google Cloud in **sprints**. A move group is a group of infrastructure resources and workloads that you need to migrate together. These resources and workloads can be part of the same application, or a group of applications that are interdependent.

![A cloud migration project is divided into waves and move groups](https://docs.cloud.google.com/static/migration-center/images/cloud-migration-project.png)

Business capability is one of the most important aspects to determine the move groups. For example, supply chain management and inventory management in retail, fraud monitoring in banking, claim processing in insurance, represent business capability areas in the respective domains. Considering business capability is critical to ensure minimal or no disruption to business service performance and availability during and after migration.

Within a business capability area, you need to perform the migration according to your different environments. Research and development (R&D) environments are typically the first to be migrated. This helps you identify and mitigate any blockers that might prevent or slow down the migration. You can then follow the best practices and mitigation activities as you progress through the migration of R&D, pre-production and production environments.

You need to run **discovery and assessment** as an ongoing process, with data collection getting increasingly refined and more accurate over time. This lets you constantly improve the accuracy of workload-specific data, which helps you identify workload-specific risks associated with the cloud migration.

The first wave of discovery and assessment lets you create a high-level map of the dependencies between your infrastructure components and workloads. This helps you plan and optimize the elements of your target Google Cloud architecture during the first wave—for example, VM types, storage classes, landing zone design, high-level capacity sizing based on computational and I/O throughput requirements.

You also need to run a **migration risk assessment** in parallel with discovery and assessment. The aim is to identify and measure the workload-specific risks associated with the migration, and to start the appropriate mitigation actions.

The following diagram shows the whole migration process at a glance.

![Diagram of the migration planning and execution process.](https://docs.cloud.google.com/static/migration-center/images/migration-process-overview.png)

## What's next

  * Learn how to [evaluate and mitigate the migration risks](https://docs.cloud.google.com/migration-center/docs/migration-risks).
  * Learn how to [plan your migration waves](https://docs.cloud.google.com/migration-center/docs/plan-migration-waves).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
