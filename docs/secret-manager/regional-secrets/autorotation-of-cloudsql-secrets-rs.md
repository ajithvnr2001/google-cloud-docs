---
url: https://docs.cloud.google.com/secret-manager/regional-secrets/autorotation-of-cloudsql-secrets-rs/
title: Automatic rotation of Cloud SQL secrets \u00a0|\u00a0 Secret Manager Regional Service Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:38:58.740902+00:00
---

# Automatic rotation of Cloud SQL secrets  |  Secret Manager Regional Service Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/regional-secrets/autorotation-of-cloudsql-secrets-rs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Regional service ](https://docs.cloud.google.com/secret-manager/regional-secrets)
  * [ Guides ](https://docs.cloud.google.com/secret-manager/regional-secrets/regional-secrets-overview)



Send feedback 

#  Automatic rotation of Cloud SQL secrets Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes the automatic rotation of Cloud SQL secrets in Secret Manager. With automatic rotation, Secret Manager generates a secure password, updates the secret in the target Cloud SQL database instance, and stores the new secret as the latest secret version.

**Note:**

  * Automatic rotation for Cloud SQL credentials is available only for regional secrets in Secret Manager. Global secrets don't support this feature.
  * Ensure that your Cloud SQL instance uses a supported database engine flavor, such as [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/introduction) or [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/introduction).



## Benefits of automatic rotation

Automatic rotation provides the following advantages: 

  * Eliminates the need to maintain custom Cloud Run functions for rotating credentials.
  * Minimizes the impact of leaked credentials by rotating them frequently.
  * Lets you meet compliance requirements that mandate regular password rotation, for example, the [Payment Card Industry Data Security Standards (PCI-DSS)](https://cloud.google.com/security/compliance/pci-dss). For more information, see the [Compliance resource center](https://cloud.google.com/compliance).



## Key concepts

To use automatic rotation, you must understand the following concepts: 

### Secret types

You can use secret types to categorize your secrets. To enable automatic rotation, select `Cloud SQL DB credentials` secret type during creation. For more information, see [Create a regional secret](https://docs.cloud.google.com/secret-manager/regional-secrets/create-regional-secret).

Existing secrets don't support automatic rotation.

**Note:**

  * You can't manually add versions to secrets with type `Cloud SQL DB credentials`. Secret Manager automatically manages them during the rotation process. You can add versions to secrets with other secret types.
  * You can only select a secret type when you create a secret. You can't add or update the secret type of an existing secret.
  * You must create your regional secret in the same region as your Cloud SQL instance to minimize cross-region latency and align with regional data residency requirements.



### Built-in identities for secrets

Secrets are resource types with [built-in identities](https://docs.cloud.google.com/guides/product-specific/iam/iam-terms). Each secret has a unique identifier that distinguishes it from all other resources in your Google Cloud project. The system automatically generates this unique identifier when you create a secret and stores it in the `iamPolicyUidPrincipal` field of the secret resource. For more information, see [Built-in identities for resources](https://docs.cloud.google.com/iam/docs/built-in-resource-identities). 

You must grant the built-in identity the required permissions to update credentials on your Cloud SQL instance. This ensures that a secret only holds the privileges necessary to rotate its own credentials, adhering to the principle of least privilege. 

**Note:** Automatic rotation fails if the built-in identity doesn't have the required permissions.

### Rotation schedule and status

You can use rotation schedules to specify how often you want to rotate secrets. For example, every 30 or 90 days. 

The system tracks the health of the rotation schedule using the secret's rotation status: 

  * `Enabled`: The rotation schedule is enabled, and the most recent rotation was successful.
  * `Disabled`: The rotation schedule is paused. The status also changes to `Disabled` if a rotation attempt fails.



### Rotation strategy

Each `Cloud SQL DB credentials` secret manages one set of database credentials (Cloud SQL instance ID, username, and password). 

During rotation, Secret Manager generates a secure password for the Cloud SQL user and updates the secret in both Secret Manager and the target Cloud SQL instance. 

**Note:** Automatic rotation can cause temporary application downtime. After Secret Manager updates the database password, a short delay occurs before the `alias` points to the new version. During this window, applications using the old password experience connection failures. Ensure that you implement robust error handling (retries) to retrieve the latest version upon authentication failure.

### Rotation lifecycle

The automatic rotation process follows a specific lifecycle managed by Secret Manager, and the workflow includes the following steps: 

  1. **Initiate:** the process starts based on the configured rotation schedule or an on-demand manual rotation.
  2. **Generate:** Secret Manager generates a secure password that complies with [ Cloud SQL password policies](https://docs.cloud.google.com/sql/docs/mysql/built-in-authentication).
  3. **Synchronize:** Secret Manager updates the password in the target Cloud SQL instance and stores the new secret as the latest secret version. At this stage, the Cloud SQL instance has the new password, but the secret `alias` still points to the old version.
  4. **Update alias:** Secret Manager updates the secret alias to point to the new secret version.
  5. **Send notification:** if configured, Secret Manager sends a Pub/Sub notification to alert you of the rotation's success or failure.



If the rotation fails, the system automatically retries. If failure persists, Secret Manager sets the rotation status to `Disabled`. To resume rotation, you must resolve the underlying issue and enable the rotation again. 

## What's next

  * [Create rotation schedules](https://docs.cloud.google.com/secret-manager/regional-secrets/rotate-regional-secrets)
  * [Set expiration date for a regional secret](https://docs.cloud.google.com/secret-manager/regional-secrets/set-expiration-regional-secrets)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
