---
url: https://docs.cloud.google.com/data-fusion/docs/use-case/dataproc-in-different-project/
title: Use case: Access control for a Managed Service for Apache Spark cluster in another project \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:42.996667+00:00
---

# Use case: Access control for a Managed Service for Apache Spark cluster in another project  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/use-case/dataproc-in-different-project/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Use case: Access control for a Managed Service for Apache Spark cluster in another project Stay organized with collections  Save and categorize content based on your preferences. 

This page describes managing access control when you deploy and run a pipeline that uses Managed Service for Apache Spark clusters in another Google Cloud project.

## Scenario

By default, when a Cloud Data Fusion instance is launched in a Google Cloud project, it deploys and runs pipelines using Managed Service for Apache Spark clusters within the same project. However, your organization might require you to use clusters in another project. For this use case, you must manage access between the projects. The following page describes how you can change the _baseline_ (default) configurations and apply the appropriate access controls.

## Before you begin

To understand the solutions in this use case, you need the following context:

  * Familiarity with basic [Cloud Data Fusion concepts](https://docs.cloud.google.com/data-fusion/docs/concepts/overview#explore-concepts)
  * Familiarity with [Identity and Access Management (IAM) for Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/access-control)
  * Familiarity with [Cloud Data Fusion networking](https://docs.cloud.google.com/data-fusion/docs/concepts/networking)



## Assumptions and scope

This use case has the following requirements:

  * A [private Cloud Data Fusion instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip). For security reasons, an organization may require that you use this type of instance.
  * A BigQuery source and sink.
  * Access control with IAM, not role-based access control (RBAC).

**Note:** This use case doesn't show networking scenarios where sources and sinks are in other VPCs.

## Solution

This solution compares baseline and use case specific architecture and configuration.

### Architecture

The following diagrams compare the project architecture for creating a Cloud Data Fusion instance and running pipelines when you use clusters in the same project (baseline) and in a different project through the tenant project VPC.

#### Baseline architecture

This diagram shows the baseline architecture of the projects:

![Tenant, customer, and Dataproc project architecture in Cloud Data Fusion.](https://docs.cloud.google.com/static/data-fusion/docs/images/use-case/diagram-data-fusion-projects@1x.png)

For the baseline configuration, you create a private Cloud Data Fusion instance and run a pipeline with no additional customization:

  * You use one of the built-in compute profiles
  * The source and sink are in the same project as the instance
  * No additional roles have been granted to any of the service accounts



For more information about tenant and customer projects, see [Networking](https://docs.cloud.google.com/data-fusion/docs/concepts/networking).

#### Use case architecture

This diagram shows the project architecture when you use clusters in another project:

![Tenant, customer, and Dataproc project architecture in Cloud Data Fusion.](https://docs.cloud.google.com/static/data-fusion/docs/images/use-case/diagram-dataproc-data-fusion-projects@1x.png)

### Configurations

The following sections compare the baseline configurations to the use case specific configurations for using Managed Service for Apache Spark clusters in a different project through the default, tenant project VPC.

In the following use case descriptions, the _customer project_ is where the Cloud Data Fusion instance runs and the _Managed Service for Apache Spark project_ is where the Managed Service for Apache Spark cluster is launched.

**Note:** The use case configurations assume that you use the default Compute Engine service account in the Managed Service for Apache Spark project for running Managed Service for Apache Spark jobs.

#### Tenant project VPC and instance

Baseline | Use case  
---|---  
In the preceding baseline architecture diagram, the tenant project contains the following components: 

  * The default VPC, which is created automatically.
  * The physical deployment of the Cloud Data Fusion instance.

| No additional configuration is needed for this use case.  
  
#### Customer project

Baseline | Use case  
---|---  
Your Google Cloud project is where you deploy and run pipelines. By default, the Managed Service for Apache Spark clusters are launched in this project when you run your pipelines. | In this use case, you manage two projects. On this page, the _customer project_ refers to where the Cloud Data Fusion instance runs.  
The _Managed Service for Apache Spark project_ refers to where the Managed Service for Apache Spark clusters launch.  
  
#### Customer VPC

Baseline | Use case  
---|---  
From your (the customer's) perspective, the customer VPC is where Cloud Data Fusion is logically situated.  
**Key takeaway:**  
You can find the Customer VPC details in the VPC networks page of your project. [ Go to VPC networks](https://console.cloud.google.com/networking/networks/list) | No additional configuration is needed for this use case.  
  
#### Cloud Data Fusion subnet

Baseline | Use case  
---|---  
From your (the customer's) perspective, this subnet is where Cloud Data Fusion is logically situated.  
**Key takeaway:**  
The region of this subnet is the same as the location of the Cloud Data Fusion instance in the tenant project.  | No additional configuration is needed for this use case.  
  
#### Managed Service for Apache Spark subnet

Baseline | Use case  
---|---  
The subnet where Managed Service for Apache Spark clusters are launched when you run a pipeline.  
**Key takeaways:**  


  * For this baseline configuration, Managed Service for Apache Spark is run in the same subnet as the Cloud Data Fusion instance.
  * Cloud Data Fusion locates a subnet in the same region as both the instance and subnet of Cloud Data Fusion. If there's only one subnet in this region, the subnets are the same.
  * The Managed Service for Apache Spark subnet must have Private Google Access.

| This is a new subnet where Managed Service for Apache Spark clusters are launched when you run a pipeline.  
**Key takeaways:**  


  * For this new subnet, set Private Google Access to **On**.
  * The Managed Service for Apache Spark subnet doesn't need to be in the same location as the Cloud Data Fusion instance.

  
  
#### Sources and sinks

Baseline | Use case  
---|---  
The sources where data is extracted and sinks where data is loaded, such as BigQuery sources and sinks.  
**Key takeaway:**  


  * The jobs that fetch and load data must be processed in the same location as the dataset, or an error results.

| The use case specific access control configurations on this page are for BigQuery sources and sinks.  
  
#### Cloud Storage

Baseline | Use case  
---|---  
The storage bucket in the customer project that helps transfer files between Cloud Data Fusion and Managed Service for Apache Spark.  
**Key takeaways:**  


  * You can specify this bucket through the Cloud Data Fusion web interface in the **Compute Profile** settings for ephemeral clusters.
  * For batch and real-time pipelines, or replication jobs: if you don't specify a bucket in the compute profile, Cloud Data Fusion creates a bucket in the same project as the instance for this purpose.
  * Even for static Managed Service for Apache Spark clusters, in this baseline configuration, the bucket is created by Cloud Data Fusion and differs from the Managed Service for Apache Spark staging and temp buckets.
  * The Cloud Data Fusion API Service Agent has built-in permissions to create this bucket in the project containing the Cloud Data Fusion instance.

| No additional configuration is needed for this use case.  
  
#### Temporary buckets used by source and sink

Baseline | Use case  
---|---  
The temporary buckets created by plugins for your sources and sinks, such as the load jobs initiated by the BigQuery Sink plugin.   
**Key takeaways:**  


  * You can define these buckets when you configure the source and sink plugin properties.
  * If you don't define a bucket, one is created in the same project where Managed Service for Apache Spark runs.
  * If the dataset is multi-regional, the bucket is created in the same scope.
  * If you define a bucket in the plugin configuration, the region of the bucket must match the region of the dataset.
  * If you don't define a bucket in the plugin configurations, the one that's created for you is deleted when the pipeline finishes.

| For this use case, the bucket can be created in any project.  
  
#### Buckets that are sources or sinks of data for plugins

Baseline | Use case  
---|---  
Customer buckets, which you specify in the configurations for plugins, such as the Cloud Storage plugin and the FTP to Cloud Storage plugin. | No additional configuration is needed for this use case.  
  
#### IAM: Cloud Data Fusion API Service Agent

Baseline | Use case  
---|---  
When the Cloud Data Fusion API is enabled, the [Cloud Data Fusion API Service Agent role](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) is automatically granted to the [ Cloud Data Fusion service account](https://docs.cloud.google.com/iam/docs/service-agents#cloud-data-fusion-service-account), the primary service agent.   
**Key takeaways:**  


  * The role contains permissions for services in the same project as the instance, such as BigQuery and Managed Service for Apache Spark. For all supported services, see the [role details](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent).
  * The Cloud Data Fusion service account does the following: 
    * Data plane (pipeline design and execution) communication with other services (for example—communicating with Cloud Storage, BigQuery, and Datastream at design time).
    * Provisions Managed Service for Apache Spark clusters.
  * If you're replicating from an Oracle source, this service account must also be given the Datastream Admin and Storage Admin roles in the project where the job occurs. This page doesn't address a replication use case.

| For this use case, grant the Cloud Data Fusion API Service Agent role to the service account in the Managed Service for Apache Spark project. Then grant the following roles in that project:

  * Compute Network User role
  * Dataproc Editor role

  
  
#### IAM: Managed Service for Apache Spark service account

Baseline | Use case  
---|---  
The service account used to run the pipeline as a job within the Managed Service for Apache Spark cluster. By default, it's the Compute Engine service account.  
Optional: in the baseline configuration, you can change the default service account to another service account from the same project. Grant the following IAM roles to the new service account:

  * The Cloud Data Fusion Runner role. This role lets Managed Service for Apache Spark communicate with Cloud Data Fusion API.
  * The Dataproc Worker role. This role lets the jobs run on Managed Service for Apache Spark clusters.

**Key takeaways:**  


  * The API Agent service account for the new service must be granted the Service Account User role on the Managed Service for Apache Spark service account so that the Service API Agent can use it to launch Managed Service for Apache Spark clusters.

| This use case example assumes you use the default Compute Engine service account (`PROJECT_NUMBER-compute@developer.gserviceaccount.com`) of the Managed Service for Apache Spark project.  
Grant the following roles to the default Compute Engine service account in the Managed Service for Apache Spark project. **Note:** To use a different service account for running Cloud Data Fusion pipelines, grant the roles in that service account in the Managed Service for Apache Spark project. 

  * The Dataproc Worker role
  * The Storage Admin role (or, at minimum, the `storage.buckets.create` permission) to let Managed Service for Apache Spark create temporary buckets for BigQuery.
  * BigQuery Job User role. This role lets Managed Service for Apache Spark create load jobs. The jobs are created in the Managed Service for Apache Spark project by default.
  * BigQuery Dataset Editor role. This role lets Managed Service for Apache Spark create datasets while loading data.

Grant the Service Account User role to the Cloud Data Fusion Service Account on the default Compute Engine service account of the Managed Service for Apache Spark project. This action must be performed in the Managed Service for Apache Spark project. Add the default Compute Engine service account of the Managed Service for Apache Spark project to the Cloud Data Fusion project. Also grant the following roles:

  * The Storage Object Viewer role to retrieve pipeline job related artifacts from the Cloud Data Fusion Consumer bucket.
  * Cloud Data Fusion Runner role, so the Managed Service for Apache Spark cluster can communicate with Cloud Data Fusion while it's running.

  
  
#### APIs

Baseline | Use case  
---|---  
When you enable the Cloud Data Fusion API, the following APIs are also enabled. For more information about these APIs, go to the APIs & services page in your project.  
[Go to APIs & services](https://console.cloud.google.com/apis/dashboard)

  * Cloud Autoscaling API
  * Dataproc API
  * Cloud Dataproc Control API
  * Cloud DNS API
  * Cloud OS Login API
  * Pub/Sub API
  * Compute Engine API
  * Container Filesystem API
  * Container Registry API
  * Service Account Credentials API
  * Identity and Access Management API
  * Kubernetes Engine API

When you enable the Cloud Data Fusion API, the following service accounts are automatically added to your project:

  * Google APIs Service Agent
  * Compute Engine Service Agent
  * Kubernetes Engine Service Agent
  * Google Container Registry Service Agent
  * Google Cloud Dataproc Service Agent
  * Cloud KMS Service Agent
  * Cloud Pub/Sub Service Account

| For this use case, enable the following APIs in the project that contains the Managed Service for Apache Spark project, if they aren't already enabled:  


  * Compute Engine API
  * Dataproc API
  * Cloud Resource Manager API

  
  
#### Encryption keys

Baseline | Use case  
---|---  
In the baseline configuration, encryption keys can be Google-managed or [CMEK ](https://docs.cloud.google.com/data-fusion/docs/how-to/customer-managed-encryption-keys)   
**Key takeaways:**  
If you use CMEK, your baseline configuration requires the following:

  * The key must be regional, created in the same region as the Cloud Data Fusion instance.
  * Grant the Cloud KMS CryptoKey Encrypter/Decrypter role to the following service accounts at the key level (not in the IAM page of the Google Cloud console) in the project where it's created: 
    * Cloud Data Fusion API service account
    * Managed Service for Apache Spark service account, which is the Compute Engine Service Agent (`service-PROJECT_NUMBER@compute-system.iam.gserviceaccount.com`) by default
    * Google Cloud Dataproc Service Agent (`service-PROJECT_NUMBER@dataproc-accounts.iam.gserviceaccount.com`)
    * Cloud Storage Service Agent (`service-PROJECT_NUMBER@gs-project-accounts.iam.gserviceaccount.com`)

Depending on the services used in your pipeline, such as BigQuery or Cloud Storage, service accounts must also be granted the Cloud KMS CryptoKey Encrypter/Decrypter role:

  * The BigQuery service account (`bq-PROJECT_NUMBER@bigquery-encryption.iam.gserviceaccount.com`)
  * The Pub/Sub service account (`service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com`)
  * The Spanner service account (`service-PROJECT_NUMBER@gcp-sa-spanner.iam.gserviceaccount.com`)

|  If you don't use CMEK, no additional changes are needed for this use case. If you use CMEK, the Cloud KMS CryptoKey Encrypter/Decrypter role must be provided to the following service account at the key level in the project where it's created:

  * Cloud Storage Service Agent (`service-PROJECT_NUMBER@gs-project-accounts.iam.gserviceaccount.com`)

Depending on the services used in your pipeline, such as BigQuery or Cloud Storage, other service accounts must also be granted the Cloud KMS CryptoKey Encrypter/Decrypter role at the key level. For example:

  * The BigQuery service account (`bq-PROJECT_NUMBER@bigquery-encryption.iam.gserviceaccount.com`)
  * The Pub/Sub service account (`service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com`)
  * The Spanner service account (`service-PROJECT_NUMBER@gcp-sa-spanner.iam.gserviceaccount.com`)

  
  
After you make these use case specific configurations, your data pipeline can start running on clusters in another project.

## What's next

  * Learn more about [networking in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/networking).
  * Refer to the [IAM basic and predefined roles reference](https://docs.cloud.google.com/iam/docs/understanding-roles).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
