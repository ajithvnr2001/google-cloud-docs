---
url: https://docs.cloud.google.com/docs/security/security-best-practices-catalog/data-management/
title: Data management controls \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:44.770808+00:00
---

# Data management controls  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/security-best-practices-catalog/data-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Data management controls Stay organized with collections  Save and categorize content based on your preferences. 

This document includes the best practices and guidelines for data management systems when running workloads on Google Cloud.

Data management systems such as [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction) and [Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction) let you store the data that you require for your workflows, including training data, model artifacts, and production data.

## Common controls

These controls apply to all data management systems.

### Enable Sensitive Data Protection for data inspection

Google control ID | COM-CO-5.1  
---|---  
Implementation | Recommended  
Description | Google Cloud recommends using Sensitive Data Protection. The infoTypes or job templates that you select depend on your particular systems.  
Applicable products |  Sensitive Data Protection  
Related NIST-800-53 controls | 

  * SI-4
  * IA-7
  * SC-7
  * SC-8

  
Related CRI profile controls | 

  * PR.AC-1.1
  * PR.AC-1.2
  * PR.AC-1.3
  * PR.DS-5.1
  * PR.DS-8.1
  * ID.RA-1.1
  * DE.CM-1.1
  * DE.CM-1.2
  * DE.CM-1.3
  * DE.CM-1.4
  * DE.CM-5.1
  * DE.CM-6.1
  * DE.CM-6.2
  * DE.CM-6.3
  * DE.CM-7.1
  * DE.CM-7.2
  * DE.CM-7.3
  * DE.CM-7.4
  * DE.DP-2.1
  * DE.DP-3.1
  * DE.DP-4.1
  * DE.DP-4.2
  * DE.DP-5.1
  * DE.AE-2.1
  * DE.AE-3.1
  * DE.AE-3.2
  * DE.AE-4.1

  
Related information | 

  * [Templates](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-templates)
  * [InfoTypes and infoType detectors](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes)

  
  
## Data warehouse controls

These controls apply to BigQuery.

### Ensure BigQuery datasets aren't publicly readable or set to allAuthenticatedUsers

Google control ID | BQ-CO-6.1  
---|---  
Implementation | Required  
Description | Ensure that BigQuery doesn't have datasets that are open to public access unless the datasets are intended to be public. Datasets in BigQuery often contain sensitive data.Restrict access to the information in a BigQuery dataset to specific users only. To configure this protection, you must set up detailed roles.Reviewing dataset access helps you ensure that you don't unintentionally expose data to the internet.  
Applicable products | 

  * Organization Policy Service
  * BigQuery
  * Identity and Access Management (IAM)

  
Path | `cloudasset.assets/assetType`  
Operator | ==  
Value |  `bigquery.googleapis.com/Dataset`  
Type | String  
Related NIST-800-53 controls | 

  * AC-3
  * AC-12
  * AC-17
  * AC-20

  
Related CRI profile controls | 

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.AC-7.1
  * PR.AC-7.2
  * PR.PT-3.1
  * PR-PT-4.1

  
Related information | 

  * [Revoke access to a dataset](https://docs.cloud.google.com/bigquery/docs/control-access-to-resources-iam#revoke_access_to_a_dataset)
  * [allAuthenticatedUsers](https://docs.cloud.google.com/iam/docs/principals-overview#all-authenticated-users)
  * [Control access to resources with IAM](https://docs.cloud.google.com/bigquery/docs/control-access-to-resources-iam)

  
  
### Ensure BigQuery tables aren't publicly readable or set to allAuthenticatedUsers

Google control ID | BQ-CO-6.2  
---|---  
Implementation | Required  
Description | Restrict access to the information in a BigQuery table to specific users only. To configure this protection, you must set up detailed roles.  
Applicable products | 

  * Identity and Access Management (IAM)
  * BigQuery

  
Path | `cloudasset.assets/iamPolicy.bindings.members`  
Operator | anyof  
Value | 

  * `allUsers`
  * `allAuthenticatedUsers`

  
Type | String  
Related NIST-800-53 controls | 

  * AC-3
  * AC-12
  * AC-17
  * AC-20

  
Related CRI profile controls | 

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.AC-7.1
  * PR.AC-7.2
  * PR.PT-3.1
  * PR-PT-4.1

  
Related information | 

  * [Revoke access to a table or view](https://docs.cloud.google.com/bigquery/docs/control-access-to-resources-iam#revoke_access_to_a_table_or_view)
  * [allAuthenticatedUsers](https://docs.cloud.google.com/iam/docs/principals-overview#all-authenticated-users)
  * [Control access to resources with IAM](https://docs.cloud.google.com/bigquery/docs/control-access-to-resources-iam)

  
  
### Encrypt individual values in a BigQuery table

Google control ID | BQ-CO-6.3  
---|---  
Implementation | Optional  
Description | If your organization requires that you encrypt individual values within a BigQuery table, use the Authenticated Encryption with Associated Data (AEAD) encryption functions.  
Applicable products |  BigQuery  
Related NIST-800-53 controls | 

  * SC-13

  
Related CRI profile controls | 

  * PR.DS-5.1

  
Related information | 

  * [AEAD encryption functions](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/aead_encryption_functions)

  
  
### Use authorized views for BigQuery datasets

Google control ID | BQ-CO-6.4  
---|---  
Implementation | Optional  
Description | Authorized views let you share a subset of data in a dataset to specific users. For example, an authorized view lets you share query results with particular users and groups without giving them access to the underlying source data.  
Applicable products |  BigQuery  
Related NIST-800-53 controls | 

  * AC-3
  * AC-12
  * AC-17
  * AC-20

  
Related CRI profile controls | 

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.AC-7.1
  * PR.AC-7.2
  * PR.PT-3.1
  * PR-PT-4.1

  
Related information | 

  * [Authorized views](https://docs.cloud.google.com/bigquery/docs/authorized-views)

  
  
### Use BigQuery column-level security

Google control ID | BQ-CO-6.5  
---|---  
Implementation | Optional  
Description | Use BigQuery column-level security to create policies that check at query time whether a user has proper access. BigQuery provides fine-grained access to sensitive columns using policy tags or type-based classification of data.  
Applicable products |  BigQuery  
Related NIST-800-53 controls | 

  * AC-3
  * AC-12
  * AC-17
  * AC-20

  
Related CRI profile controls | 

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.AC-7.1
  * PR.AC-7.2
  * PR.PT-3.1
  * PR-PT-4.1

  
Related information | 

  * [Introduction to column-level access control](https://docs.cloud.google.com/bigquery/docs/column-level-security-intro)

  
  
### Use BigQuery row-level security

Google control ID | BQ-CO-6.6  
---|---  
Implementation | Optional  
Description | Use row-level security and access policies to enable fine-grained access control to a subset of data in a BigQuery table.  
Applicable products |  BigQuery  
Related NIST-800-53 controls | 

  * AC-3
  * AC-12
  * AC-17
  * AC-20

  
Related CRI profile controls | 

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.AC-7.1
  * PR.AC-7.2
  * PR.PT-3.1
  * PR-PT-4.1

  
Related information | 

  * [Introduction to row-level access control](https://docs.cloud.google.com/bigquery/docs/row-level-security-intro)

  
  
### Use BigQuery resource charts

Google control ID | BQ-CO-7.1  
---|---  
Implementation | Optional  
Description | BigQuery resource charts let BigQuery administrators observe how their organization, folder, or reservation uses BigQuery slots and how their queries perform.  
Applicable products |  BigQuery  
Related NIST-800-53 controls | 

  * AC-3
  * AC-12
  * AC-17
  * AC-20

  
Related CRI profile controls | 

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.AC-7.1
  * PR.AC-7.2
  * PR.PT-3.1
  * PR-PT-4.1

  
Related information | 

  * [Monitor health, resource utilization, and jobs](https://docs.cloud.google.com/bigquery/docs/admin-resource-charts)

  
  
## Storage controls

These controls apply to Cloud Storage.

### Block public access to Cloud Storage buckets

Google control ID | GCS-CO-4.1  
---|---  
Implementation | Required  
Description | The `storage.publicAccessPrevention` boolean constraint prevents storage buckets from being accessed from public sources without authentication. It disables and blocks access control lists (ACLs) and Identity and Access Management (IAM) permissions that grant access to `allUsers` and `allAuthenticatedUsers`. This constraint acts as an organization-wide safety net that actively blocks any setting that would make a bucket publicly accessible.  
Applicable products | 

  * Organization Policy Service
  * Cloud Storage

  
Path | `constraints/storage.publicAccessPrevention`  
Operator | ==  
Value |  `True`  
Type | Boolean  
Related NIST-800-53 controls | 

  * AC-3
  * AC-17
  * AC-20

  
Related CRI profile controls | 

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.PT-3.1
  * PR.PT-4.1

  
Related information | 

  * [Public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention)

  
  
### Use uniform bucket-level access

Google control ID | GCS-CO-4.2  
---|---  
Implementation | Required  
Description | The `storage.uniformBucketLevelAccess` boolean constraint requires buckets to use uniform bucket-level access. Uniform bucket-level access lets you only use bucket-level Identity and Access Management (IAM) permissions to grant access to your Cloud Storage resources.Using two different and conflicting systems to manage permissions on storage buckets is complex and a common cause of accidental data leaks. This setting turns off the legacy system (access control lists, or ACLs) and makes the modern, centralized system (IAM) the single source of truth for all permissions.  
Applicable products | 

  * Organization Policy Service
  * Cloud Storage

  
Path | `constraints/storage.uniformBucketLevelAccess`  
Operator | ==  
Value |  `True`  
Type | Boolean  
Related NIST-800-53 controls | 

  * AC-3
  * AC-17
  * AC-20

  
Related CRI profile controls | 

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.PT-3.1
  * PR.PT-4.1

  
Related information | 

  * [Require uniform bucket-level access](https://docs.cloud.google.com/storage/docs/org-policy-constraints#uniform-access)

  
  
### Protect HMAC keys for service accounts

Google control ID | GCS-CO-6.9  
---|---  
Implementation | Required  
Description | An HMAC key is a long-lived type of credential that is associated with a service account or a user account in Cloud Storage. Use an HMAC key to create signatures that are included in requests to Cloud Storage. A signature proves a user or service account has authorized a request.Unlike short-lived credentials (such as. OAuth 2.0 tokens), HMAC keys don't expire automatically and remain valid until manually revoked. HMAC keys are high-risk credentials: if compromised, they provide persistent access to your resources. You must ensure appropriate mechanisms are in place to help protect them.  
Applicable products |  Cloud Storage  
Path | `storage.projects.hmacKeys/id`  
Operator | Exists  
Value |  `[]`  
Type | String  
Related NIST-800-53 controls | 

  * SC-12
  * SC-13

  
Related CRI profile controls | 

  * PR.DS-1.1
  * PR.DS-1.2
  * PR.DS-2.1
  * PR.DS-2.2
  * PR.DS-5.1

  
Related information | 

  * [Manage HMAC keys for service accounts](https://cloud.google.com/storage/docs/authentication/managing-hmackeys)

  
  
### Detect enumeration of Cloud Storage buckets by service accounts

Google control ID | GCS-CO-7.2  
---|---  
Implementation | Required  
Description | Service accounts are non-human identities that are designed for applications, and their behavior is predictable and automated. Normally, service accounts don't need to itemize buckets, as they're already mapped. Therefore, if you detect a service account attempting to retrieve a list of all Cloud Storage buckets, investigate it immediately. Reconnaissance enumeration is often used as a recon technique by a malicious actor that has gained access to the service account.  
Applicable products | 

  * Cloud Storage
  * Cloud Audit Logs

  
Operator | ==  
Value |  `storage.bucket.list`  
Type | String  
Related NIST-800-53 controls | 

  * AU-2
  * AU-3
  * AU-8
  * AU-9

  
Related CRI profile controls | 

  * DM.ED-7.1
  * DM.ED-7.2
  * DM.ED-7.3
  * DM.ED-7.4
  * PR.IP-1.4

  
Related information | 

  * [Cloud Audit Logs with Cloud Storage](https://cloud.google.com/storage/docs/audit-logging)

  
  
### Detect IAM policy modifications of Cloud Storage buckets by service accounts

Google control ID | GCS-CO-7.3  
---|---  
Implementation | Required  
Description | Configure an alert that detects when the Identity and Access Management (IAM) policy of a Cloud Storage bucket is modified to grant public access. This alert fires when the `allUsers` or `allAuthenticatedUsers` principals are added to a bucket's IAM policy. This alert is a critical, high-severity event because it can expose all data in the bucket. Investigate this alert immediately to confirm if the change was authorized or is a sign of a misconfiguration or malicious actor.In the alert, set the `data.protoPayload.serviceData.policyData.bindingDeltas.member` JSON attribute to `allUsers` or `allAuthenticatedUsers` and the action to `ADD`.  
Applicable products | 

  * Cloud Storage
  * Cloud Audit Logs

  
Related NIST-800-53 controls | 

  * AU-2
  * AU-3
  * AU-8
  * AU-9

  
Related CRI profile controls | 

  * DM.ED-7.1
  * DM.ED-7.2
  * DM.ED-7.3
  * DM.ED-7.4
  * PR.IP-1.4

  
Related information | 

  * [Cloud Audit Logs with Cloud Storage](https://cloud.google.com/storage/docs/audit-logging)

  
  
### Ensure Cloud Storage bucket retention policy uses Bucket Lock

Google control ID | GCS-CO-6.1  
---|---  
Implementation | Recommended  
Description | Depending on your regulatory requirements, ensure that each Cloud Storage bucket retention policy is locked. Set the retention period to a timeframe that meets your requirements.  
Applicable products |  Cloud Storage  
Path | `storage.buckets/retentionPolicy.isLocked`  
Operator | !=  
Value |  `True`  
Type | Boolean  
Related NIST-800-53 controls | 

  * SI-12

  
Related CRI profile controls | 

  * PR.IP-2.1
  * PR.IP-2.2
  * PR.IP-2.3

  
Related information | 

  * [Use and lock retention policies](https://docs.cloud.google.com/storage/docs/bucket-lock)

  
  
### Set lifecycle rules for the SetStorageClass action

Google control ID | GCS-CO-6.11  
---|---  
Implementation | Recommended  
Description | Apply lifecycle rules to each Cloud Storage bucket that has a `SetStorageClass` action type.  
Applicable products |  Cloud Storage  
Path | `storage.buckets/lifecycle.rule.action.type`  
Operator | ==  
Value |  `SetStorageClass`  
Type | String  
Related NIST-800-53 controls | 

  * SI-12

  
Related CRI profile controls | 

  * PR.IP-2.1
  * PR.IP-2.2
  * PR.IP-2.3

  
Related information | 

  * [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle)

  
  
### Set permitted regions for storage classes

Google control ID | GCS-CO-6.12  
---|---  
Implementation | Recommended  
Description | Ensure that storage classes for the lifecycle configuration aren't within permitted regional classifications.  
Applicable products |  Cloud Storage  
Path | `storage.buckets/lifecycle.rule.action.storageClass`  
Operator | nin  
Value | 

  * `MULTI_REGIONAL`
  * `REGIONAL`

  
Type | String  
Related NIST-800-53 controls | 

  * SI-12

  
Related CRI profile controls | 

  * PR.IP-2.1
  * PR.IP-2.2
  * PR.IP-2.3

  
Related information | 

  * [Bucket locations](https://docs.cloud.google.com/storage/docs/locations)
  * [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle)

  
  
### Enable lifecycle management for Cloud Storage buckets

Google control ID | GCS-CO-6.13  
---|---  
Implementation | Recommended  
Description | Ensure that lifecycle management of Cloud Storage is enabled and configured. The lifecycle control contains the configuration for the storage lifecycle. Verify that the policies in this setting match your requirements.  
Applicable products |  Cloud Storage  
Path | `storage.buckets/lifecycle`  
Operator | Exists  
Value |  `[]`  
Type | Object  
Related NIST-800-53 controls | 

  * SI-12

  
Related CRI profile controls | 

  * PR.IP-2.1
  * PR.IP-2.2
  * PR.IP-2.3

  
Related information | 

  * [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle)

  
  
### Enable lifecycle management rules for Cloud Storage buckets

Google control ID | GCS-CO-6.14  
---|---  
Implementation | Recommended  
Description | Ensure that lifecycle management rules for Cloud Storage are enabled and configured. The rule control contains the configuration for the storage lifecycle. Verify that the policies in this setting match your requirements.  
Applicable products |  Cloud Storage  
Path | `storage.buckets/lifecycle.rule`  
Operator | Empty  
Value |  `[]`  
Type | Array  
Related NIST-800-53 controls | 

  * SI-12

  
Related CRI profile controls | 

  * PR.IP-2.1
  * PR.IP-2.2
  * PR.IP-2.3

  
Related information | 

  * [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle)

  
  
### Review and evaluate temporary holds on active objects

Google control ID | GCS-CO-6.16  
---|---  
Implementation | Recommended  
Description | Identify all objects where temporaryHold is set to TRUE and start an investigation and validation process. This evaluation is appropriate for the following use cases:

  * **Legal hold:** To comply with legal requirements for storing data, temporary hold can be used to prevent the deletion of sensitive data that may be relevant to ongoing investigations or litigation.
  * **Data loss prevention:** To prevent accidental deletion of important data, temporary hold can be used as a safety measure to protect critical business information.
  * **Content moderation:** To review potentially sensitive or inappropriate content before it becomes publicly accessible, apply a temporary hold to content uploaded to Cloud Storage for further inspection and moderation decisions.

  
Applicable products |  Cloud Storage  
Path | `storage.objects/temporaryHold`  
Operator | ==  
Value |  `TRUE`  
Type | Boolean  
Related NIST-800-53 controls | 

  * SI-12

  
Related CRI profile controls | 

  * PR.IP-2.1
  * PR.IP-2.2
  * PR.IP-2.3

  
Related information | 

  * [Object holds](https://cloud.google.com/storage/docs/object-holds)

  
  
### Enforce retention policies on Cloud Storage buckets

Google control ID | GCS-CO-6.17  
---|---  
Implementation | Recommended  
Description | Ensure that all the Cloud Storage buckets have a retention policy.  
Applicable products |  Cloud Storage  
Path | `storage.buckets/retentionPolicy.retentionPeriod`  
Operator | agesmaller  
Value |  `[90,"DAY","AFTER","yyyy-MM-dd'T'HH:mm:ss'Z'"]`  
Type | int64  
Related NIST-800-53 controls | 

  * SI-12

  
Related CRI profile controls | 

  * PR.IP-2.1
  * PR.IP-2.2
  * PR.IP-2.3

  
Related information | 

  * [Bucket Lock](https://docs.cloud.google.com/storage/docs/bucket-lock)

  
  
### Enforce classification tags for Cloud Storage buckets

Google control ID | GCS-CO-6.18  
---|---  
Implementation | Recommended  
Description | Data classification is a foundational component of any data governance and security program. Applying a classification label with values like public, internal, confidential, or restricted to each bucket is essential.Confirm that `google_storage_bucket.labels` has an expression for classification and create a violation if it doesn't.  
Applicable products |  Cloud Storage  
Path | `storage.buckets/labels.classification`  
Operator | notexists  
Value |  `[]`  
Type | Extended  
Related NIST-800-53 controls | 

  * SI-12

  
Related CRI profile controls | 

  * PR.IP-2.1
  * PR.IP-2.2
  * PR.IP-2.3

  
Related information | 

  * [Tags and labels](https://cloud.google.com/storage/docs/tags-and-labels)

  
  
### Enforce log buckets for Cloud Storage buckets

Google control ID | GCS-CO-6.3  
---|---  
Implementation | Recommended  
Description | Ensure that every Cloud Storage bucket includes a log bucket.  
Applicable products |  Cloud Storage  
Path | `storage.buckets/logging.logBucket`  
Operator | notexists  
Value |  `[]`  
Type | String  
Related NIST-800-53 controls | 

  * AU-2
  * AU-3
  * AU-8
  * AU-9

  
Related CRI profile controls | 

  * DM.ED-7.1
  * DM.ED-7.2
  * DM.ED-7.3
  * DM.ED-7.4
  * PR.IP-1.4

  
Related information | 

  * [Configure log buckets](https://docs.cloud.google.com/logging/docs/buckets)

  
  
### Configure deletion rules for Cloud Storage buckets

Google control ID | GCS-CO-6.5  
---|---  
Implementation | Recommended  
Description | In Cloud Storage, `storage.buckets/lifecycle.rule.action.type` refers to the type of action to be taken on a specific object based on a lifecycle rule within a bucket. This configuration helps automate the management and lifecycle of your data stored in the cloud.Configure the `storage.buckets/lifecycle.rule.action.type` to ensure that objects are permanently deleted from the bucket.  
Applicable products |  Cloud Storage  
Path | `storage.buckets/lifecycle.rule.action.type`  
Operator | ==  
Value |  `Delete`  
Type | String  
Related NIST-800-53 controls | 

  * SI-12

  
Related CRI profile controls | 

  * PR.IP-2.1
  * PR.IP-2.2
  * PR.IP-2.3

  
Related information | 

  * [Manage object lifecycles](https://docs.cloud.google.com/storage/docs/managing-lifecycles)

  
  
### Ensure isLive condition is False for deletion rules

Google control ID | GCS-CO-6.6  
---|---  
Implementation | Recommended  
Description | For deletion rules, ensure that the `isLive` condition of the rule is set to `false`. In Cloud Storage, `storage.buckets/lifecycle.rule.condition.isLive` is a boolean condition that is used in lifecycle rules to determine whether an object is considered live. This filter helps ensure that actions within a lifecycle rule are applied only to desired objects based on their live status. Use cases:

  * **Archive historical versions:** Archive only non-current versions of objects to save storage costs while keeping the latest version readily accessible.
  * **Clean up deleted objects:** Automate permanent deletion of objects that have been deleted by users, freeing up space in the bucket.
  * **Protect live data:** Ensure that actions like setting temporary holds are applied only to live objects, preventing accidental modification of archived or deleted versions

  
Applicable products |  Cloud Storage  
Path | `storage.buckets/lifecycle.rule.condition.isLive`  
Operator | ==  
Value |  `False`  
Type | Boolean  
Related NIST-800-53 controls | 

  * SI-12

  
Related CRI profile controls | 

  * PR.IP-2.1
  * PR.IP-2.2
  * PR.IP-2.3

  
Related information | 

  * [isLive](https://cloud.google.com/storage/docs/lifecycle#islive)

  
  
### Enforce versioning for Cloud Storage buckets

Google control ID | GCS-CO-6.7  
---|---  
Implementation | Recommended  
Description | Ensure that all Cloud Storage buckets have versioning enabled. Use cases include the following:

  * **Data protection and recovery:** Protect against accidental data loss by preventing overwrites and enabling recovery of deleted or modified data.
  * **Compliance and auditing:** Maintain a history of all object edits for regulatory compliance or internal auditing purposes.
  * **Version control:** Track changes to files and data sets, enabling collaboration and rollback to previous versions if necessary.

  
Applicable products |  Cloud Storage  
Path | `storage.buckets/versioning.enabled`  
Operator | !=  
Value |  `True`  
Type | Boolean  
Related NIST-800-53 controls | 

  * SI-12

  
Related CRI profile controls | 

  * PR.IP-2.1
  * PR.IP-2.2
  * PR.IP-2.3

  
Related information | 

  * [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning)

  
  
### Enforce owners for Cloud Storage buckets

Google control ID | GCS-CO-6.8  
---|---  
Implementation | Recommended  
Description | Ensure that `google_storage_bucket.labels` has an expression for an owner.  
Applicable products |  Cloud Storage  
Path | `storage.buckets/labels.owner`  
Operator | notexists  
Value |  `[]`  
Type | Extended  
Related NIST-800-53 controls | 

  * SI-12

  
Related CRI profile controls | 

  * PR.IP-2.1
  * PR.IP-2.2
  * PR.IP-2.3

  
Related information | 

  * [Using bucket labels](https://docs.cloud.google.com/storage/docs/using-bucket-labels)

  
  
### Enable logging of key Cloud Storage activities

Google control ID | GCS-CO-7.4  
---|---  
Implementation | Recommended  
Description | Enable additional logging around particular storage objects based on their use case. For example, log access to sensitive data buckets so that you can trace who gained access and when. When enabling additional logging, consider the volume of logs that you might generate.  
Applicable products |  Cloud Storage  
Related NIST-800-53 controls | 

  * AU-2
  * AU-3
  * AU-8
  * AU-9

  
Related CRI profile controls | 

  * DM.ED-7.1
  * DM.ED-7.2
  * DM.ED-7.3
  * DM.ED-7.4
  * PR.IP-1.4

  
Related information | 

  * [Cloud Audit Logs with Cloud Storage](https://docs.cloud.google.com/storage/docs/audit-logging)

  
  
## Database controls

### Restrict Cloud SQL public IP addresses

Implementation | Required  
---|---  
Description | Prevent Cloud SQL from having a public IP address and being directly exposed to the internet by setting the `constraints/sql.restrictPublicIp` organization policy constraint. Typically, databases aren't directly exposed to the internet.Preventing public IP addresses helps prevent your databases from getting public IP addresses, ensuring that they are private and only accessible from trusted, internal applications.  
Applicable products |  Cloud SQL  
Path | `constraints/sql.restrictPublicIp`  
Operator | =  
Value |  `True`  
Related NIST-800-53 controls | 

  * SC-7

  
Related CRI profile controls | 

  * PR.AC-3.1

  
Related information | 

  * [Improve instance security by disabling public IP](https://docs.cloud.google.com/sql/docs/mysql/recommender-disable-public-ip)
  * [Connection organization policies](https://docs.cloud.google.com/sql/docs/mysql/org-policy/org-policy#connection_organization_policies)

  
  
### Implement and test database backups

Implementation | Required  
---|---  
Description | Configure backups for your databases (for example, Cloud SQL and Filestore), storing copies in isolated or alternate locations. Regularly test your backup and restore procedures.  
Applicable products | 

  * Cloud SQL
  * Filestore
  * AlloyDB for PostgreSQL

  
Related NIST-800-53 controls | 

  * CP-2
  * CP-6
  * CP-9
  * CP-9(1)
  * CP-10

  
Related CRI profile controls | 

  * PR.IP-4.1
  * PR.IP-4.2

  
Related information | 

  * [Cloud SQL backups overview](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backups)
  * [About Filestore backups](https://docs.cloud.google.com/filestore/docs/backups)
  * [Configure AlloyDB for PostgreSQL backup plans](https://docs.cloud.google.com/alloydb/docs/backup/configure)

  
  
## What's next

  * Review [tools and inference controls](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/tools-inference).

  * See more [Google Cloud security best practices and guidelines](https://docs.cloud.google.com/docs/security/security-best-practices-catalog).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
