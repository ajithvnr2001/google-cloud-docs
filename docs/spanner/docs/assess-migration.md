---
url: https://docs.cloud.google.com/spanner/docs/assess-migration/
title: Assess your migration \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:32:35.529922+00:00
---

# Assess your migration  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/assess-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Assess your migration Stay organized with collections  Save and categorize content based on your preferences. 

Assessing your source database and how its usage maps to Spanner requires evaluating your business, technical, operational, and financial needs. We recommend covering the following key areas for your assessment:

  * **Business goals** : Define the specific business problems Spanner solves, such as scalability, availability, and consistency. Establish measurable success criteria, such as reduced latency, increased transaction volume, and cost reduction.


  * **Cost analysis** : Calculate the potential total cost of using Spanner (compute, storage, and network) and compare it to your current database costs. Factor in one-time migration costs and ongoing operational expenses. For more information, see [Spanner pricing](https://cloud.google.com/spanner/pricing).


  * **Schema compatibility** : Analyze the existing source database schema for possible incompatibilities with Spanner such as data types, constraints, indexes, or stored procedures. Plan for schema modifications and data transformations to appropriately map your source database schema to Spanner. For more information, see [Schema design best practices](https://docs.cloud.google.com/spanner/docs/schema-design).

  * **Data consistency and transactions** : Understand Spanner's external consistency model and its differences from your source database transaction model. Evaluate the impact on your application logic. For more information, see [Spanner: TrueTime and external consistency](https://docs.cloud.google.com/spanner/docs/true-time-external-consistency).

  * **Data locality and regional configurations** : Determine optimal Spanner deployment topology such as regional, dual-region, or multi-region deployments based on user locations, latency requirements, and cost considerations. For more information, see [Instances configurations](https://docs.cloud.google.com/spanner/docs/instance-configurations#configuration).

  * **Application code compatibility** : Inventory all database interactions with your application code. Identify areas that require modification because of differences in SQL dialect, client libraries, and transaction management.

  * **Performance and scalability requirements** : Define current and projected workloads such as read and write ratios, transaction rates, and data volume. Determine acceptable latency and throughput. For more information on Spanner's performance, see [Performance overview](https://docs.cloud.google.com/spanner/docs/performance#typical-workloads).

  * **Migration strategy and downtime** : Develop a detailed migration plan, including data extraction, transformation, loading, and validation. If downtime isn't a concern, you can perform a one-time bulk load and cutover. Otherwise, consider minimizing downtime. Define a rollback plan.

  * **Operational consideration** : Plan for changes in database administration, monitoring, and disaster recovery. Assess the learning curve for the team. Integrate Spanner with existing operational tools and processes For more information, see [Disaster recovery overview](https://docs.cloud.google.com/spanner/docs/backup/disaster-recovery-overview).

  * **Security** : Review Spanner's security features such as [authentication](https://docs.cloud.google.com/spanner/docs/authentication), [authorization](https://docs.cloud.google.com/spanner/docs/iam), and [encryption](https://docs.cloud.google.com/spanner/docs/encryption-in-transit). Ensure compliance with relevant regulations.




## Source specific guides

  * MySQL: [Migrate from MySQL to Spanner](https://docs.cloud.google.com/spanner/docs/migrating-mysql-to-spanner).



[ Previous arrow_back  Migration overview  ](https://docs.cloud.google.com/spanner/docs/migration-overview)

[ Next Migrate your schema  arrow_forward  ](https://docs.cloud.google.com/spanner/docs/schema-migration)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
