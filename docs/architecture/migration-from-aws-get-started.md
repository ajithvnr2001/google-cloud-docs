---
url: https://docs.cloud.google.com/architecture/migration-from-aws-get-started/
title: Migrate from AWS to Google Cloud: Get started \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:21:59.662858+00:00
---

# Migrate from AWS to Google Cloud: Get started  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/migration-from-aws-get-started/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Migrate from AWS to Google Cloud: Get started Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-10-21 UTC

Google Cloud provides tools, products, guidance, and professional services to help you migrate workloads, data, and processes from Amazon Web Services (AWS) to Google Cloud. This document introduces a discussion about how to design, implement, and validate a plan to migrate from AWS to Google Cloud.

The discussion is intended for cloud administrators who want details about how to plan and implement a migration process. It's also intended for decision-makers who are evaluating the opportunity to migrate and who want to explore what migration looks like.

This document is part of a multi-part series about migrating from AWS to Google Cloud that includes the following documents:

  * Get started (this document)
  * [Migrate from Amazon EC2 to Compute Engine](https://docs.cloud.google.com/architecture/migrate-amazon-ec2-to-compute-engine)
  * [Migrate from Amazon S3 to Cloud Storage](https://docs.cloud.google.com/architecture/migrate-amazon-s3-to-cloud-storage)
  * [Migrate from Amazon EKS to Google Kubernetes Engine](https://docs.cloud.google.com/architecture/migrate-amazon-eks-to-gke)
  * [Migrate from Amazon RDS and Amazon Aurora for MySQL to Cloud SQL for MySQL](https://docs.cloud.google.com/architecture/migrate-aws-rds-to-sql-mysql)
  * [Migrate from Amazon RDS and Amazon Aurora for PostgreSQL to Cloud SQL for PostgreSQL and AlloyDB for PostgreSQL](https://docs.cloud.google.com/architecture/migrate-aws-rds-aurora-to-postgresql)
  * [Migrate from Amazon RDS for SQL Server to Cloud SQL for SQL Server](https://docs.cloud.google.com/architecture/migrate-aws-rds-to-cloudsql-for-sqlserver)
  * [Migrate from AWS Lambda to Cloud Run](https://docs.cloud.google.com/architecture/migrate-aws-lambda-to-cloudrun)



Migrating your workloads, data, and processes from AWS to Google Cloud can be a challenging task and can take days, weeks, or months to complete, depending on the scope and size of the migration. Therefore, we recommend that you plan and execute your migration carefully.

AWS and Google Cloud products that target similar use cases might seem similar in the way you provision, configure, and use the resources that they provide. However, despite similarities, these resources might differ significantly in the way they work and in their requirements. We therefore recommend that you assess the ways in which similar AWS and Google Cloud resources work before you plan your migration.

This series provides guidance about the following migration journeys:

  * **From AWS compute services to Google Cloud**
    * [Migrate from Amazon EC2 to Compute Engine](https://docs.cloud.google.com/architecture/migrate-amazon-ec2-to-compute-engine)
    * [Migrate VMware VMs to your Google Cloud VMware Engine private cloud](https://docs.cloud.google.com/vmware-engine/docs/workloads/howto-migrate-workloads)
    * [Migrate from Amazon Elastic Kubernetes Service (Amazon EKS) to Google Kubernetes Engine](https://docs.cloud.google.com/architecture/migrate-amazon-eks-to-gke)
    * [Migrate from AWS Lambda to Cloud Run](https://docs.cloud.google.com/architecture/migrate-aws-lambda-to-cloudrun)
  * **From AWS data storage services to Google Cloud**
    * [Migrate from Amazon S3 to Cloud Storage](https://docs.cloud.google.com/architecture/migrate-amazon-s3-to-cloud-storage)
  * **From AWS database services to Google Cloud**
    * [Migrate from Amazon RDS and Amazon Aurora for MySQL to Cloud SQL for MySQL](https://docs.cloud.google.com/architecture/migrate-aws-rds-to-sql-mysql)
    * [Migrate from Amazon RDS and Amazon Aurora for PostgreSQL to Cloud SQL for PostgreSQL and AlloyDB for PostgreSQL](https://docs.cloud.google.com/architecture/migrate-aws-rds-aurora-to-postgresql)
    * [Migrate from Amazon RDS for SQL Server to Cloud SQL for SQL Server](https://docs.cloud.google.com/architecture/migrate-aws-rds-to-cloudsql-for-sqlserver)
    * [Migrate from Amazon DynamoDB to Spanner](https://docs.cloud.google.com/spanner/docs/migrating-dynamodb-to-cloud-spanner)
    * [Migrate from Amazon DynamoDB to Bigtable](https://docs.cloud.google.com/bigtable/docs/dynamodb-users)
  * **From AWS data analytics services to Google Cloud**
    * [Amazon Redshift to BigQuery migration](https://docs.cloud.google.com/bigquery/docs/migration/redshift-overview)



## What's next

  * Read about [other AWS to Google Cloud migration journeys](https://docs.cloud.google.com/architecture/migration-from-aws-get-started).
  * Learn how to [compare AWS and Azure services to Google Cloud](https://docs.cloud.google.com/free/docs/aws-azure-gcp-service-comparison).
  * Learn where to [find help for your migrations](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started#finding_help).
  * Take the [Google Skills training course on migrating to Google Cloud](https://www.skills.google/course_templates/1561).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Marco Ferrari](https://www.linkedin.com/in/ferrarimark) | Cloud Solutions Architect

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-10-21 UTC."],[],[]] 
