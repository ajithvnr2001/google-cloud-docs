---
url: https://docs.cloud.google.com/architecture/migrate-amazon-s3-to-cloud-storage/
title: Migrate from AWS to Google Cloud: Migrate from Amazon S3 to Cloud Storage \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:05.467790+00:00
---

# Migrate from AWS to Google Cloud: Migrate from Amazon S3 to Cloud Storage  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/migrate-amazon-s3-to-cloud-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Migrate from AWS to Google Cloud: Migrate from Amazon S3 to Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-04-14 UTC

Google Cloud provides tools, products, guidance, and professional services to help you migrate data from [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) to [Cloud Storage](https://docs.cloud.google.com/storage). This document discusses how to design, implement, and validate a plan to migrate from Amazon S3 to Cloud Storage. The document describes a portion of the overall migration process in which you create an inventory of Amazon S3 artifacts and create a plan for how to handle the migration process.

The discussion in this document is intended for cloud administrators who want details about how to plan and implement a migration process. It's also intended for decision-makers who are evaluating the opportunity to migrate and who want to explore what migration might look like.

This document is part of a multi-part series about migrating from AWS to Google Cloud that includes the following documents:

  * [Get started](https://docs.cloud.google.com/architecture/migration-from-aws-get-started)
  * [Migrate from Amazon EC2 to Compute Engine](https://docs.cloud.google.com/architecture/migrate-amazon-ec2-to-compute-engine)
  * Migrate from Amazon S3 to Cloud Storage (this document)
  * [Migrate from Amazon EKS to Google Kubernetes Engine](https://docs.cloud.google.com/architecture/migrate-amazon-eks-to-gke)
  * [Migrate from Amazon RDS and Amazon Aurora for MySQL to Cloud SQL for MySQL](https://docs.cloud.google.com/architecture/migrate-aws-rds-to-sql-mysql)
  * [Migrate from Amazon RDS and Amazon Aurora for PostgreSQL to Cloud SQL for PostgreSQL and AlloyDB for PostgreSQL](https://docs.cloud.google.com/architecture/migrate-aws-rds-aurora-to-postgresql)
  * [Migrate from Amazon RDS for SQL Server to Cloud SQL for SQL Server](https://docs.cloud.google.com/architecture/migrate-aws-rds-to-cloudsql-for-sqlserver)
  * [Migrate from AWS Lambda to Cloud Run](https://docs.cloud.google.com/architecture/migrate-aws-lambda-to-cloudrun)



For this migration to Google Cloud, we recommend that you follow the migration framework described in [Migrate to Google Cloud: Get started](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started#the_migration_path).

The following diagram illustrates the path of your migration journey.

![Migration path with four phases.](https://docs.cloud.google.com/static/architecture/images/migration-to-gcp-getting-started-migration-path.svg)

You might migrate from your source environment to Google Cloud in a series of iterations—for example, you might migrate some workloads first and others later. For each separate migration iteration, you follow the phases of the general migration framework:

  1. Assess and discover your workloads and data.
  2. Plan and build a foundation on Google Cloud.
  3. Migrate your workloads and data to Google Cloud.
  4. Optimize your Google Cloud environment.



For more information about the phases of this framework, see [Migrate to Google Cloud: Get started](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started).

To design an effective migration plan, we recommend that you validate each step of the plan, and ensure that you have a rollback strategy. To help you validate your migration plan, see [Migrate to Google Cloud: Best practices for validating a migration plan](https://docs.cloud.google.com/architecture/migration-to-google-cloud-best-practices).

## Assess the source environment

In the assessment phase, you determine the requirements and dependencies to migrate your source environment to Google Cloud.

The assessment phase is crucial for the success of your migration. You need to gain deep knowledge about the workloads you want to migrate, their requirements, their dependencies, and about your current environment. You need to understand your starting point to successfully plan and execute a Google Cloud migration.

The assessment phase consists of the following tasks:

  1. Build a comprehensive inventory of your workloads.
  2. Catalog your workloads according to their properties and dependencies.
  3. Train and educate your teams on Google Cloud.
  4. Build experiments and proofs of concept on Google Cloud.
  5. Calculate the total cost of ownership (TCO) of the target environment.
  6. Choose the migration strategy for your workloads.
  7. Choose your migration tools.
  8. Define the migration plan and timeline.
  9. Validate your migration plan.



For more information about the assessment phase and these tasks, see [Migrate to Google Cloud: Assess and discover your workloads](https://docs.cloud.google.com/architecture/migration-to-gcp-assessing-and-discovering-your-workloads). The following sections are based on information in that document.

### Build an inventory of your Amazon S3 buckets

To scope your migration, you create two inventories: an inventory of your Amazon S3 buckets, and an inventory of the objects that are stored in the buckets.

After you build the inventory of your Amazon S3 buckets, refine the inventory by considering the following data points about each Amazon S3 bucket:

  * How you've configured Amazon S3 bucket server-side encryption.
  * Your settings for Amazon S3 bucket identity and access management.
  * The configuration for S3 Block Public Access.
  * Any cost allocation tags for Amazon S3 buckets.
  * The configuration for S3 Object Lock.
  * How you're accessing the Amazon S3 bucket.
  * How you've configured Requester Pays.
  * The settings for Amazon S3 object versioning.
  * The configuration for AWS Backup policies for Amazon S3.
  * Whether you're using Amazon S3 Intelligent-Tiering.
  * How you've configured for Amazon S3 object replication.
  * The Amazon S3 object lifecycle.
  * Whether the bucket is a specialized type such as S3 Tables, S3 Metadata, or S3 Vectors.



We also recommend that you gather data about your Amazon S3 buckets that lets you compute aggregate statistics about the objects that each bucket contains. For example, if you gather the total object size, average object size, and object count, it can help you [estimate the time and cost that's needed](https://docs.cloud.google.com/architecture/migration-to-google-cloud-transferring-your-large-datasets#step_3_evaluating_your_transfer_options) to migrate from an Amazon S3 bucket to a Cloud Storage bucket.

To build the inventory of your Amazon S3 buckets and to gather data points about your Amazon S3 buckets, you can implement data-collection mechanisms and processes that rely on AWS tools, such as the following:

  * Amazon S3 monitoring tools
  * S3 Analytics
  * AWS Multi-Account Multi-Region Data Aggregation
  * AWS APIs
  * AWS developer tools
  * The AWS command-line interface



To help you avoid issues during the migration, and to help estimate the effort needed for the migration, we recommend that you evaluate how Amazon S3 bucket features map to similar Cloud Storage bucket features. The following table summarizes this mapping.

Amazon S3 feature | Cloud Storage feature  
---|---  
[Bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide//bucketnamingrules.html) | [Bucket name requirements](https://docs.cloud.google.com/storage/docs/buckets#naming)  
[Bucket location](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html) | [Bucket location](https://docs.cloud.google.com/storage/docs/locations)  
[Server-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide//bucket-encryption.html) | [Encryption options](https://docs.cloud.google.com/storage/docs/encryption)  
[Identity and access management](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html) | [Identity and Access Management (IAM)](https://docs.cloud.google.com/storage/docs/access-control/iam)  
[Public access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html) | [Public data access](https://docs.cloud.google.com/storage/docs/access-control/making-data-public)  
[Public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention)  
[Cost allocation S3 bucket tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/CostAllocTagging.html) | [Tags and labels](https://docs.cloud.google.com/storage/docs/tags-and-labels)  
[S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide//object-lock.html) | [Retention policies and retention policy lock](https://docs.cloud.google.com/storage/docs/bucket-lock)  
[Methods for accessing an Amazon S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide//access-bucket-intro.html) | [Object uploads](https://docs.cloud.google.com/storage/docs/uploads) and [downloads](https://docs.cloud.google.com/storage/docs/reads-and-downloads)  
[Requester Pays](https://docs.aws.amazon.com/AmazonS3/latest/userguide//RequesterPaysBuckets.html) | [Requester Pays](https://docs.cloud.google.com/storage/docs/requester-pays)  
[Object versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide//Versioning.html) | [Object versioning](https://docs.cloud.google.com/storage/docs/object-versioning)  
[AWS Backup policies for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide//backup-for-s3.html) | [Event-driven transfer jobs](https://docs.cloud.google.com/storage-transfer/docs/event-driven-transfers)  
[Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide//intelligent-tiering.html) | [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass)  
[Object replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide//replication.html) | [Redundancy across regions and turbo replication](https://docs.cloud.google.com/storage/docs/availability-durability#cross-region-redundancy)  
[Event-driven transfer jobs](https://docs.cloud.google.com/storage-transfer/docs/event-driven-transfers)  
[Object lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide//object-lifecycle-mgmt.html) | [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle)  
[S3 Express One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide//directory-bucket-high-performance.html) | [Rapid Bucket](https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket)  
[Mountpoint for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide//mountpoint.html) | [Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview)  
  
As noted earlier, the features listed in the preceding table might look similar when you compare them. However, differences in the design and implementation of the features in the two cloud providers can have significant effects on your migration from Amazon S3 to Cloud Storage.

### Specialized Amazon S3 Bucket Types

To help you avoid issues during the migration, and to help estimate the effort needed for specialized use cases, we recommend that you evaluate how these Amazon S3 bucket features map to Google Cloud services. The following table summarizes this mapping.

Amazon S3 feature | Cloud Storage feature  
---|---  
[S3 Tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables.html) | [BigLake](https://docs.cloud.google.com/bigquery/docs/biglake-intro) or [BigQuery](https://docs.cloud.google.com/bigquery/docs)  
[S3 Vectors](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors.html) | [Vector Search](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/overview)  
[S3 Metadata](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-overview.html) | [Storage Insights](https://docs.cloud.google.com/storage/docs/insights/datasets)  
  
### Build an inventory of the objects stored in your Amazon S3 objects

After you build the inventory of your Amazon S3 buckets, we recommend that you build an inventory of the objects stored in these buckets by using the [Amazon S3 inventory](https://docs.aws.amazon.com/AmazonS3/latest/userguide//storage-inventory.html) tool.

To build the inventory of your Amazon S3 objects, consider the following for each object:

  * Amazon S3 object name
  * Amazon S3 object size
  * Amazon S3 object metadata
  * Amazon S3 object subresources
  * Amazon S3 object versions, and if you need to migrate these versions
  * Amazon S3 object presigned URLs
  * Amazon S3 object transformations
  * Amazon S3 object tags
  * Amazon S3 object storage classes
  * Amazon S3 object archiving
  * Amazon S3 object checksums



We also recommend that you gather data about your Amazon S3 objects to understand how often you and your workloads create, update, and delete Amazon S3 objects.

To help you avoid issues during the migration, and to help estimate the effort needed for the migration, we recommend that you evaluate how Amazon S3 object features map to similar Cloud Storage object features. The following table summarizes this mapping.

Amazon S3 feature | Cloud Storage feature  
---|---  
[Object naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide//object-keys.html) | [Object name requirements](https://docs.cloud.google.com/storage/docs/objects#naming)  
[Object metadata](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingMetadata.html)  
[Object tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide//object-tagging.html) | [Object metadata](https://docs.cloud.google.com/storage/docs/metadata)  
[Object subresources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingObjects.html#ObjectAndSubResource) | [Object metadata](https://docs.cloud.google.com/storage/docs/metadata)  
[Object presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide//using-presigned-url.html) | [Signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls)  
[Object transformations](https://docs.aws.amazon.com/AmazonS3/latest/userguide//transforming-objects.html) | [Pub/Sub notifications for Cloud Storage](https://docs.cloud.google.com/storage/docs/pubsub-notifications)  
[Cloud Run functions](https://docs.cloud.google.com/functions)  
[Cloud Run](https://docs.cloud.google.com/run/docs)  
[Object storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide//storage-class-intro.html)  
[Object archiving](https://docs.aws.amazon.com/AmazonS3/latest/userguide//archived-objects.html) | [Cloud Storage storage classes](https://docs.cloud.google.com/storage/docs/storage-classes)  
[Object preconditional operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide//conditional-requests.html) | [Request preconditions](https://docs.cloud.google.com/storage/docs/request-preconditions)  
  
As noted earlier, the features listed in the preceding table might look similar when you compare them. However, differences in the design and implementation of the features in the two cloud providers can have significant effects on your migration from Amazon S3 to Cloud Storage.

### Complete the assessment

After you build the inventories from your Amazon S3 environment, complete the rest of the activities of the assessment phase as described in [Migrate to Google Cloud: Assess and discover your workloads](https://docs.cloud.google.com/solutions/migration-to-gcp-assessing-and-discovering-your-workloads).

## Plan and build your foundation

In the plan and build phase, you provision and configure the infrastructure to do the following:

  * Support your workloads in your Google Cloud environment.
  * Connect your source environment and your Google Cloud environment to complete the migration.



The plan and build phase is composed of the following tasks:

  1. Build a resource hierarchy.
  2. Configure Google Cloud's Identity and Access Management (IAM).
  3. Set up billing.
  4. Set up network connectivity.
  5. Harden your security.
  6. Set up logging, monitoring, and alerting.



For more information about each of these tasks, see the [Migrate to Google Cloud: Plan and build your foundation](https://docs.cloud.google.com/architecture/migration-to-google-cloud-building-your-foundation).

## Migrate data and workloads from Amazon S3 to Cloud Storage

To migrate data from Amazon S3 to Cloud Storage, we recommend that you design a data migration plan by following the guidance in [Migrate to Google Cloud: Transfer your large datasets](https://docs.cloud.google.com/architecture/migration-to-google-cloud-transferring-your-large-datasets). That document recommends using [Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/overview), a Google Cloud product that lets you migrate data from several sources to Cloud Storage, such as from on-premises environments or from other cloud storage providers. Storage Transfer Service supports several types of data transfer jobs, such as the following:

  * [Run-once transfer jobs](https://docs.cloud.google.com/storage-transfer/docs/create-transfers), which transfer data from Amazon S3 or other supported sources to Cloud Storage on demand.
  * [Scheduled transfer jobs](https://docs.cloud.google.com/storage-transfer/docs/schedule-transfer-jobs), which transfer data from Amazon S3 or other supported sources to Cloud Storage on a schedule.
  * [Event-driven transfer jobs](https://docs.cloud.google.com/storage-transfer/docs/event-driven-transfers), which automatically transfer data when Amazon S3 sends Amazon S3 Event Notifications to Amazon Simple Queue Service (SQS).



To implement a data migration plan, you can configure one or more data transfer jobs. For example, to reduce the length of cut-over windows during the migration, you can implement a [continuous replication](https://docs.cloud.google.com/architecture/migration-to-google-cloud-transferring-your-large-datasets#continuous_replication) data migration strategy as follows:

  1. Configure a run-once transfer job to copy the data from an Amazon S3 bucket to the Cloud Storage bucket.
  2. Perform data validation and consistency checks to compare data in the Amazon S3 bucket against the copied data in the Cloud Storage bucket.
  3. Set up event-driven transfer jobs to automatically transfer data from the Amazon S3 bucket to the Cloud Storage bucket when the content of the Amazon S3 bucket changes.
  4. Stop the workloads and services that have access to the data that's being migrated (that is, to the data that's involved in the previous step).
  5. Refactor workloads to use Cloud Storage instead of Amazon S3. You can refactor your workloads by using one of the following approaches, or by using the approaches in sequence:

     * [Simple migration from Amazon S3 to Cloud Storage](https://docs.cloud.google.com/storage/docs/aws-simple-migration). In a simple migration, you use your existing tools and libraries that generate authenticated REST requests to Amazon S3 to instead generate authenticated requests to Cloud Storage.

For example, Cloud Storage supports the deletion of up to 1,000 objects in a single request by using the [XML multi-object delete API](https://docs.cloud.google.com/storage/docs/xml-api/post-bucket). This capability is compatible with the [Amazon S3 DeleteObjects API](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjects.html).

     * [Fully migrate from Amazon S3 to Cloud Storage](https://docs.cloud.google.com/storage/docs/migrating). In a full migration, you can use all of the features of Cloud Storage, including multiple projects and OAuth 2.0 for authentication.

  6. Wait for the replication to fully synchronize Cloud Storage with Amazon S3.

  7. Start your workloads.

  8. When you no longer need your Amazon S3 environment as a fallback option, retire it.




Storage Transfer Service can preserve [certain metadata when you migrate objects from a supported source to Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/metadata-preservation). We recommend that you assess whether Storage Transfer Service can migrate [the Amazon S3 metadata](https://docs.cloud.google.com/storage-transfer/docs/metadata-preservation#s3-to-cloud) that you're interested in.

When you design your data migration plan, we recommend that you also assess AWS network egress costs and your Amazon S3 costs. For example, consider the following options to transfer data:

  * Across the public internet.
  * By using an interconnect link.
  * By using [Amazon CloudFront](https://docs.cloud.google.com/storage-transfer/docs/s3-cloudfront).



The option that you choose can have an impact on your AWS network egress costs and your Amazon S3 costs. The option can also affect the amount of effort and resources that you need in order to provision and configure the infrastructure. For more information about costs, see the following:

  * [Transfer from Amazon S3 to Cloud Storage: Egress options](https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agentless/s3#egress_options)
  * [Understanding data transfer charges](https://docs.aws.amazon.com/cur/latest/userguide/cur-data-transfers-charges.html) in the AWS documentation
  * [Amazon S3 pricing](https://aws.amazon.com/s3/pricing)



When you migrate data from Amazon S3 to Cloud Storage, we recommend that you [use VPC Service Controls to build a perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters) that explicitly denies communication between Google Cloud services unless the services are authorized.

## Optimize your Google Cloud environment

Optimization is the last phase of your migration. In this phase, you iterate on optimization tasks until your target environment meets your optimization requirements. The steps of each iteration are as follows:

  1. Assess your current environment, teams, and optimization loop.
  2. Establish your optimization requirements and goals.
  3. Optimize your environment and your teams.
  4. Tune the optimization loop.



You repeat this sequence until you've achieved your optimization goals.

For more information about optimizing your Google Cloud environment, see [Migrate to Google Cloud: Optimize your environment](https://docs.cloud.google.com/architecture/migration-to-google-cloud-optimizing-your-environment) and [Google Cloud Well-Architected Framework: Performance optimization](https://docs.cloud.google.com/architecture/framework/performance-optimization).

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

Last updated 2026-04-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-14 UTC."],[],[]] 
