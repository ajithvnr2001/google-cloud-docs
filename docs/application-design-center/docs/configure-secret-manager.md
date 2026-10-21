---
url: https://docs.cloud.google.com/application-design-center/docs/configure-secret-manager/
title: Configure a Secret Manager secret \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:10:58.187543+00:00
---

# Configure a Secret Manager secret  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/configure-secret-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)



Send feedback 

#  Configure a Secret Manager secret Stay organized with collections  Save and categorize content based on your preferences. 

Secret Manager is a secure and convenient storage system for API keys, passwords, certificates, and other sensitive data. For more information, see [Secret Manager overview](https://docs.cloud.google.com/secret-manager/docs/overview).

This document describes the connections and parameters you can configure when using App Design Center to create a Secret Manager secret. The configuration parameters are based on the [terraform-google-secret-manager](https://github.com/GoogleCloudPlatform/terraform-google-secret-manager/tree/main/modules/simple-secret) Terraform module.

## Component connections

The following table includes the components that you can connect to Secret Manager, and the resulting updates to your application and its generated Terraform code.

Connected component | Application updates | Background information  
---|---|---  
[Service account](https://docs.cloud.google.com/application-design-center/docs/configure-service-account) | 

  * The service account can access the secret data.
  * The `roles/secretmanager.secretAccessor` role is assigned to the Compute Engine instance template service account.

| [Manage access to secrets](https://docs.cloud.google.com/secret-manager/docs/manage-access-to-secrets)  
[Cloud Run](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-run) | 

  * The Cloud Run instance can reference the secret data.
  * The Secret Manager **Secret Data** field is referenced by the Cloud Run `env_secret_vars` field.
  * The `roles/secretmanager.secretAccessor` role is added to the Cloud Run service account.

| [Configure secrets for services](https://docs.cloud.google.com/run/docs/configuring/services/secrets)  
[Cloud SQL (MySQL)](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-sql-mysql) | 

  * Secret Manager stores user information.
  * The Secret Manager **Secret Data** field contains the password for the default user.

| [Use Secret Manager to handle secrets in Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/use-secret-manager)  
[Cloud SQL (PostgreSQL)](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-sql-postgresql) | 

  * Secret Manager stores user information.
  * The Secret Manager **Secret Data** field contains the password for the default user.

| [Use Secret Manager to handle secrets in Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/use-secret-manager)  
  
## Required configuration parameters

If your template includes a Secret Manager component, you must configure the following parameters before you deploy.

Parameter name | Description and constraints | Background information  
---|---|---  
**Project ID** | The project where you want to deploy the Secret Manager resource. | [Configure components](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#configure_components)  
**Name** | The name of the secret to create. | [Create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets)  
**Secret Data** | The secret data. Must be no larger than 64 KiB. This property is sensitive and is not displayed in the plan. | [Create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets)  
  
## Optional configuration parameters

The following parameters are optional. To display advanced parameters, in the **Configuration** area, select **Show optional fields**.

Feature | Parameter name | Description and constraint information | Background information  
---|---|---|---  
Rotation | **Rotation period** | [rotationPeriod](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.locations.secrets#Secret.Rotation.FIELDS.rotation_period) | [About rotation schedules](https://docs.cloud.google.com/secret-manager/docs/secret-rotation)  
**Next rotation time** | [nextRotationTime](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.locations.secrets#Secret.Rotation.FIELDS.next_rotation_time) | [Create and manage rotation schedules](https://docs.cloud.google.com/secret-manager/docs/rotation-recommendations)  
User managed replication | **Region** | [location](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.locations.secrets#Secret.Replica.FIELDS.location) | [User managed replication](https://docs.cloud.google.com/secret-manager/docs/choosing-replication#user-managed)  
**KMS key name** | [kmsKeyName](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.locations.secrets#Secret.CustomerManagedEncryption.FIELDS.kms_key_name) | [User managed replication](https://docs.cloud.google.com/secret-manager/docs/choosing-replication#user-managed)  
Automatic replication | **KMS key name** | [kmsKeyName](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.locations.secrets#Secret.CustomerManagedEncryption.FIELDS.kms_key_name) | [Automatic replication](https://docs.cloud.google.com/secret-manager/docs/choosing-replication#automatic)  
| **Topics** | [topics](https://github.com/GoogleCloudPlatform/terraform-google-secret-manager/tree/main/modules/simple-secret#inputs) | [Set up notifications on a secret](https://docs.cloud.google.com/secret-manager/docs/event-notifications)  
Labels | **Key** | [labels](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets#Secret.FIELDS.labels) | [Add labels to secrets](https://docs.cloud.google.com/secret-manager/docs/add-labels-to-secrets)  
**Value** | [labels](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets#Secret.FIELDS.labels) | [Add labels to secrets](https://docs.cloud.google.com/secret-manager/docs/add-labels-to-secrets)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
