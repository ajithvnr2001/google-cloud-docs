---
url: https://docs.cloud.google.com/kms/docs/cmek-org-policy/
title: CMEK organization policies \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:42:49.636593+00:00
---

# CMEK organization policies  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/cmek-org-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  CMEK organization policies Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud offers two organization policy constraints to help ensure CMEK usage across an organization:

  * `constraints/gcp.restrictNonCmekServices` is used to require CMEK protection.
  * `constraints/gcp.restrictCmekCryptoKeyProjects` is used to limit which Cloud KMS keys are used for CMEK protection.



CMEK organization policies only apply to newly created resources within supported Google Cloud services.

## Required roles

To ensure that each user has the necessary permissions to check organization policies when creating resources, ask your administrator to grant the [Organization Policy Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyViewer) (`roles/orgpolicy.policyViewer`) IAM role to each user on your organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to check organization policies when creating resources. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to check organization policies when creating resources:

  * To view full organization policy details: `orgpolicy.policy.get`
  * To check organization policy when creating resources: `orgpolicy.policies.check`



Your administrator might also be able to give each user these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

When organization policies are active, the `orgpolicy.policies.check` permission is required for Google Cloud console users who create resources that are protected by CMEK keys. Users without this permission can create CMEK-protected resources using the Google Cloud console, but they can select a CMEK key that isn't allowed by the `restrictCmekCryptoKeyProjects` constraint. When a key that does not meet this constraint is selected, resource creation eventually fails.

**Note:** The `orgpolicy.policies.check` permission is not visible in the Google Cloud console but has been added to all predefined roles that include the `orgpolicy.policy.get` permission. If your organization uses custom roles and CMEK organization policies, use gcloud CLI to add the `orgpolicy.policies.check` permission to each role that can create resources. For more information, see [Editing an existing custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#iam-custom-roles-edit-gcloud).

## Require CMEK protection

To require CMEK protection for your organization, configure the `constraints/gcp.restrictNonCmekServices` organization policy.

As a list constraint, the accepted values for this constraint are Google Cloud service names (for example, `bigquery.googleapis.com`). Use this constraint by providing a list of Google Cloud service names and setting the constraint to **Deny**. This configuration blocks the creation of resources in these services if the resource is not protected by CMEK. In other words, requests to create a resource in the service don't succeed without specifying a Cloud KMS key. Additionally, this constraint blocks the removal of CMEK protection from resources in these services. This constraint can only be applied to supported services.

**Caution:** The creation of some Google Cloud resource types can trigger the creation of a resource type from a different service. Use caution when configuring this constraint in an environment with services that don't support CMEK. Requiring CMEK protection for a service that is CMEK-aware may prevent a CMEK-unaware service from creating resources and disrupt normal functioning.

## Limit the use of Cloud KMS keys for CMEK

To limit which Cloud KMS keys are used for CMEK protection, configure the `constraints/gcp.restrictCmekCryptoKeyProjects` constraint.

As a list constraint, the accepted values are resource hierarchy indicators (for example, `projects/PROJECT_ID`, `under:folders/FOLDER_ID`, and `under:organizations/ORGANIZATION_ID`). Use this constraint by configuring a list of resource hierarchy indicators and setting the constraint to **Allow**. This configuration restricts supported services so that CMEK keys can be chosen only from the listed projects, folders, and organizations. Requests to create CMEK-protected resources in configured services don't succeed without a Cloud KMS key from one of the allowed resources. Where configured, this constraint applies to all supported services.

**Note:** This constraint by itself does not necessarily guarantee the use of customer-managed encryption keys from allowed projects within the specified services, because other methods of encryption might be available. To enforce the use of customer-managed encryption keys from allowed projects, you must apply both this constraint and the `constraints/gcp.restrictNonCmekServices` constraint.

## Supported services

Service | Constraint value when requiring CMEK  
---|---  
Agent Assist | `dialogflow.googleapis.com`  
Agent Search | `discoveryengine.googleapis.com`  
[AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/alloydb-predefined-constraints#cmek_organization_policy) | `alloydb.googleapis.com`  
[Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/using-org-policies) | `apigee.googleapis.com`  
Application Integration | `integrations.googleapis.com`  
[Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/cmek#org-policy) | `artifactregistry.googleapis.com`  
Backup and DR Service | `backupdr.googleapis.com`  
Backup for GKE | `gkebackup.googleapis.com`  
[BigQuery](https://docs.cloud.google.com/bigquery/docs/customer-managed-encryption#control_cmek_use_with_organization_policy) | `bigquery.googleapis.com`  
Bigtable | `bigtable.googleapis.com`  
Cloud Data Fusion | `datafusion.googleapis.com`  
[Cloud Logging](https://docs.cloud.google.com/logging/docs/routing/managed-encryption-storage#org-policy) | `logging.googleapis.com`  
Cloud Run | `run.googleapis.com`  
Cloud Run functions | `cloudfunctions.googleapis.com`  
[Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/org-policy/org-policy) | `sqladmin.googleapis.com`  
[Cloud Storage](https://docs.cloud.google.com/storage/docs/org-policy-constraints) | `storage.googleapis.com`  
[Cloud Tasks](https://docs.cloud.google.com/tasks/docs/use-cmek#org-policy) | `cloudtasks.googleapis.com`  
Cloud TPU | `tpu.googleapis.com`  
Cloud Workstations | `workstations.googleapis.com`  
Colab Enterprise | `aiplatform.googleapis.com`  
Compute Engine | `compute.googleapis.com`  
Customer Experience Insights | `contactcenterinsights.googleapis.com`  
[Data Studio](https://docs.cloud.google.com/data-studio/cmek#enforce_cmek_with_organization_policies) | `datastudio.googleapis.com`  
Database Migration Service | `datamigration.googleapis.com`  
Dataflow | `dataflow.googleapis.com`  
[Dataform](https://docs.cloud.google.com/dataform/docs/cmek#org-policy) | `dataform.googleapis.com`  
Datastream | `datastream.googleapis.com`  
Dialogflow CX | `dialogflow.googleapis.com`  
Document AI | `documentai.googleapis.com`  
[Eventarc Advanced](https://docs.cloud.google.com/eventarc/advanced/docs/use-cmek#org-policy) ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `eventarc.googleapis.com`  
[Eventarc Standard](https://docs.cloud.google.com/eventarc/docs/use-cmek#org-policy) | `eventarc.googleapis.com`  
[Filestore](https://docs.cloud.google.com/filestore/docs/cmek-organization-policy) | `file.googleapis.com`  
[Firestore](https://docs.cloud.google.com/firestore/docs/use-cmek#configure_a_cmek_organization_policy) | `firestore.googleapis.com`  
Gemini Enterprise | `discoveryengine.googleapis.com`  
Google Cloud Managed Lustre | `lustre.googleapis.com`  
Google Cloud Managed Service for Apache Kafka | `managedkafka.googleapis.com`  
[Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/cmek/apply-CMEK-organization-policy) | `netapp.googleapis.com`  
[Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs/observability/cmek#app-org-policies) ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `observability.googleapis.com`  
[Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-cmek#cmek-org-policy) ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `container.googleapis.com`  
[Google Security Operations](https://docs.cloud.google.com/chronicle/docs/secops/cmek_for_secops#org-policies) | `chronicleservicemanager.googleapis.com`  
[Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/cmek#org-policy) | `dataplex.googleapis.com`  
Looker (Google Cloud core) | `looker.googleapis.com`  
Managed Service for Apache Airflow | `composer.googleapis.com`  
Managed Service for Apache Spark | `dataproc.googleapis.com`  
[Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/about-cmek#org-policy) | `redis.googleapis.com`  
[Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster/about-cmek#org-policy) | `redis.googleapis.com`  
[Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey/about-cmek#org-policy) | `memorystore.googleapis.com`  
Pub/Sub | `pubsub.googleapis.com`  
Secret Manager | `secretmanager.googleapis.com`  
[Secure Source Manager](https://docs.cloud.google.com/secure-source-manager/docs/cmek#org-policy) | `securesourcemanager.googleapis.com`  
[Security Command Center](https://docs.cloud.google.com/security-command-center/docs/cmek#org-policies) | `securitycenter.googleapis.com`  
Spanner | `spanner.googleapis.com`  
Speech-to-Text | `speech.googleapis.com`  
Vector Search | `aiplatform.googleapis.com`  
Vertex AI | `aiplatform.googleapis.com`  
Vertex AI Workbench instances | `notebooks.googleapis.com`  
  
### CMEK organization policies and Storage Transfer Service

Storage Transfer Service doesn't have a CMEK integration but can be used with CMEK organization policies. If you use Storage Transfer Service and want to use CMEK to help protect the database credentials stored in Secret Manager, you must add both `storagetransfer.googleapis.com` and `secretmanager.googleapis.com` to the `constraints/gcp.restrictNonCmekServices` constraint. For more information, see the [Storage Transfer Service CMEK documentation](https://docs.cloud.google.com/storage-transfer/docs/cmek).

**Caution:** If you add `storagetransfer.googleapis.com` to this constraint but not `secretmanager.googleapis.com`, then the organization policy won't function as intended. 

### Enforcement exceptions by resource type

CMEK organization policy constraints are enforced when creating a new resource or when changing (where supported) the Cloud KMS key on an existing resource. Generally, they are enforced on all of a service's resource types that support CMEK and based solely on the resource's configuration. Some notable exceptions are summarized here:

Resource type | Enforcement exception  
---|---  
`bigquery.googleapis.com/Dataset` |  Partially enforced on dataset default Cloud KMS key (`gcp.restrictCmekCryptoKeyProjects` only)   
`bigquery.googleapis.com/Job` |  Query jobs only: enforced on Cloud KMS key provided with query or default from billing project; see also separate [configuration of project default Cloud KMS key](https://docs.cloud.google.com/bigquery/docs/default-configuration)  
`bigquerydatatransfer.googleapis.com/TransferConfig` |  Transfer configs use the service name of the Data Transfer Service (bigquerydatatransfer.googleapis.com) for CMEK organization policy constraints.   
`container.googleapis.com/Cluster` | ([Preview](https://cloud.google.com/products/#product-launch-stages)) Enforced on the Cloud KMS key for node boot disk only; not enforced on secrets at the application layer   
`logging.googleapis.com/LogBucket` |  Enforced on explicitly created log buckets; see also separate [configuration required to ensure compliance of built-in log buckets](https://docs.cloud.google.com/logging/docs/routing/managed-encryption#enable)  
`storage.googleapis.com/Bucket` |  Enforced on bucket default Cloud KMS key  
`storage.googleapis.com/Object` |  Enforced independently of bucket; see also separate [ configuration of bucket default Cloud KMS key](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys#use_default_encryption_keys)  
  
## Configuration examples

In the configuration examples, assume the sample organization has the following resource hierarchy:

![A diagram of an organization resource hierarchy](https://docs.cloud.google.com/static/kms/images/cmek_resource_hierarchy.png)

**Note:** CMEK organization policies only apply to newly created resources within supported services.

### Require CMEK and limit keys for a project

Suppose you want to require CMEK protection for all Cloud Storage resources under `projects/5` and ensure that only keys coming from `projects/4` can be used.

To require CMEK protection for all new Cloud Storage resources, use the following organization policy setting:

  * Organization policy: `constraints/gcp.restrictNonCmekServices`
  * Binding at: `projects/5`
  * Policy type: **Deny**
  * Policy value: `storage.googleapis.com`



To ensure only keys from `projects/4` are used, use the following configuration:

  * Organization policy: `constraints/gcp.restrictCmekCryptoKeyProjects`
  * Binding at: `projects/5`
  * Policy type: **Allow**
  * Policy value: `projects/4`



### Require CMEK and limit keys to within a folder

Alternatively, suppose you're expecting to add additional Cloud KMS projects under `folders/2` in the future and want to require CMEK more broadly within `folders/3`. For this scenario, you need slightly different configurations.

To require additional CMEK protection for new Cloud SQL and Cloud Storage resources anywhere under `folders/3`:

  * Organization policy: `constraints/gcp.restrictNonCmekServices`
  * Binding at: `folders/3`
  * Policy type: **Deny**
  * Policy values: `sqladmin.googleapis.com`, `storage.googleapis.com`



To ensure only keys from Cloud KMS projects under `folders/2` are used:

  * Organization policy: `constraints/gcp.restrictCmekCryptoKeyProjects`
  * Binding at: `folders/3`
  * Policy type: **Allow**
  * Policy value: `under:folders/2`



### Require CMEK for an organization

To require CMEK everywhere in the organization (in supported services), configure the `constraints/gcp.restrictNonCmekServices` constraint with the following setting:

  * Organization policy: `constraints/gcp.restrictNonCmekServices`
  * Binding at: `organizations/1`
  * Policy type: **Deny**
  * Policy values: (all supported services)



## Limitations

If you use Google Cloud console to create a resource, you might notice that you can't use any encryption options other than CMEK when `constraints/gcp.restrictNonCmekServices` is configured for a project and service. The CMEK organization policy restriction is only visible when the customer account has been granted the `orgpolicy.policy.get` IAM permission on the project.

## What's next

See [Introduction to the Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) to learn more about the benefits and common use cases for organization policies.

For more examples on creating an organization policy with particular constraints, see [Using constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
