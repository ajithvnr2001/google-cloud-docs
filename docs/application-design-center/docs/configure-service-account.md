---
url: https://docs.cloud.google.com/application-design-center/docs/configure-service-account/
title: Configure a service account \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:09.422451+00:00
---

# Configure a service account  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/configure-service-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)



Send feedback 

#  Configure a service account Stay organized with collections  Save and categorize content based on your preferences. 

A service account is a special kind of account used by an application or compute workload, such as a Compute Engine instance, rather than a person. A service account is identified by its email address, which is unique to the account. For more information, see [Service accounts overview](https://docs.cloud.google.com/iam/docs/service-account-overview).

This document describes the connections and parameters you can configure when using App Design Center to create a service account. The configuration parameters are based on the [terraform-google-service-accounts](https://github.com/terraform-google-modules/terraform-google-service-accounts/tree/main/modules/simple-sa) Terraform module.

## Component connections

The following table includes the components that you can connect to a service account, and the resulting updates to your application and its generated Terraform code.

Connected component | Application updates | Background information  
---|---|---  
[Compute Engine instance template](https://docs.cloud.google.com/application-design-center/docs/configure-compute-engine-instance) | 

  * The Compute Engine instance template uses the connected service account instead of creating a new service account. The connected service account is used for authentication and authorization to other Google Cloud services.
  * The service account email and IAM information are added to the Compute Engine instance template.

| [Create a VM that uses a user-managed service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances)  
[Secret Manager](https://docs.cloud.google.com/application-design-center/docs/configure-secret-manager) | 

  * The service account can access the secret data.
  * The `roles/secretmanager.secretAccessor` role is assigned to the service account.

| [Manage access to secrets](https://docs.cloud.google.com/secret-manager/docs/manage-access-to-secrets)  
[BigQuery](https://docs.cloud.google.com/application-design-center/docs/configure-bigquery) | 

  * The service account can be used by services, such as Cloud Run, to read and modify data in the BigQuery dataset.
  * The BigQuery `roles/bigquery.dataEditor` role is added to the service account.

| [BigQuery IAM roles and permissions](https://docs.cloud.google.com/bigquery/docs/access-control)  
[Cloud Run](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-run) | 

  * The Cloud Run service uses the service account as a [service identity](https://docs.cloud.google.com/run/docs/securing/service-identity).
  * The `roles/run.invoker` role is added to the service account.
  * The service account email and IAM information are added to the Cloud Run instance.

| [Authenticating service-to-service](https://docs.cloud.google.com/run/docs/authenticating/service-to-service)  
[Cloud SQL (MySQL)](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-sql-mysql) | 

  * The service account can connect to the Cloud SQL (MySQL) instance.
  * The `roles/cloudsql.instanceUser` and `roles/cloudsql.client` roles are added to the service account.
  * The service account IAM information is added to the Cloud SQL instance.

| [Roles and permissions](https://docs.cloud.google.com/sql/docs/mysql/roles-and-permissions)  
[Cloud SQL (PostgreSQL)](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-sql-postgresql) | 

  * The service account can connect to the Cloud SQL (PostgreSQL) instance.
  * The `roles/cloudsql.instanceUser` and `roles/cloudsql.client` roles are added to the service account.
  * The service account IAM information is added to the Cloud SQL instance.

| [Roles and permissions](https://docs.cloud.google.com/sql/docs/postgres/roles-and-permissions)  
[Cloud Storage](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-storage) | 

  * The service account can manage objects in the Cloud Storage bucket.
  * The service account IAM information is added to the Cloud Storage bucket.
  * The `roles/storage.objectAdmin` role is assigned to the service account.

| [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions)  
[Memorystore for Redis](https://docs.cloud.google.com/application-design-center/docs/configure-memorystore-for-redis) | 

  * The service account can manage the Memorystore for Redis instance.
  * The `roles/redis.editor` role is added to the service account.

| [The Memorystore for Redis service account](https://docs.cloud.google.com/memorystore/docs/redis/access-control#the_service_account)  
[Memorystore for Redis Cluster](https://docs.cloud.google.com/application-design-center/docs/configure-memorystore-for-redis-cluster) | 

  * The service account can manage the Memorystore for Redis Cluster.
  * App Design Center adds the `roles/redis.editor` role to the service account.

| [Access control with IAM](https://docs.cloud.google.com/memorystore/docs/cluster/access-control)  
[Memorystore for Valkey](https://docs.cloud.google.com/application-design-center/docs/configure-memorystore-for-valkey) | 

  * The service account can manage the Memorystore for Valkey instance.
  * App Design Center adds the `roles/memorystore.editor` role to the service account.

| [Access control with IAM](https://docs.cloud.google.com/memorystore/docs/valkey/access-control)  
[Pub/Sub](https://docs.cloud.google.com/application-design-center/docs/configure-pubsub) | 

  * The service account can manage Pub/Sub topics, and pull messages from subscriptions.
  * The `roles/pubsub.editor` role is added to the service account.
  * The service account name and email information are added to the Pub/Sub pull subscription.

| [Access control with IAM](https://docs.cloud.google.com/pubsub/docs/access-control)  
[Spanner](https://docs.cloud.google.com/application-design-center/docs/configure-spanner) | 

  * The service account has access to the Spanner instance.
  * The service account is added as an IAM user to the Spanner instance.

| [Configure an instance with a service account](https://docs.cloud.google.com/spanner/docs/configure-virtual-machine-instance#service-account)  
[Vertex AI](https://docs.cloud.google.com/application-design-center/docs/configure-vertex-ai) | 

  * The service account can interact with Vertex AI services.
  * The `roles/aiplatform.user` role is added to the service account.

| [Vertex AI access control with IAM](https://docs.cloud.google.com/vertex-ai/docs/general/access-control)  
  
## Required configuration parameters

If your template includes a service account component, you must configure the following parameters before you deploy.

Parameter name | Description and constraints | Background information  
---|---|---  
**Project ID** | The project where you want to create the service account resource. | [Configure components](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#configure_components)  
**Name** | An identifier that must be between 6 and 30 characters. Can contain lowercase alphanumeric characters and dashes. For example, `my-service-account`. | [Create service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-create)  
  
## Optional configuration parameters

The following parameters are optional. To display advanced parameters, in the **Configuration** area, select **Show advanced fields**.

Parameter name | Description and constraint information | Background information  
---|---|---  
**Display Name** | A user-readable name for the service account. | [Create service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-create)  
**Description** | A user-readable description. | [Create service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-create)  
**Project roles** | [project_roles](https://github.com/terraform-google-modules/terraform-google-service-accounts/tree/main/modules/simple-sa#inputs) | [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
