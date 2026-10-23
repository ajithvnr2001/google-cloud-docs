---
url: https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access/
title: Uniform bucket-level access \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:19.426981+00:00
---

# Uniform bucket-level access  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Uniform bucket-level access Stay organized with collections  Save and categorize content based on your preferences. 

[Setup](https://docs.cloud.google.com/storage/docs/using-uniform-bucket-level-access)

This page discusses uniform bucket-level access, which allows you to uniformly control access to your Cloud Storage resources. When you enable uniform bucket-level access on a bucket, Access Control Lists (ACLs) are disabled, and only bucket-level Identity and Access Management (IAM) permissions grant access to that bucket and the objects it contains. You revoke all access granted by object ACLs and the ability to administrate permissions using bucket ACLs.

**Note:** Enabling uniform bucket-level access on a bucket is required for creating and managing managed folders in that bucket.

## Overview

Cloud Storage offers two systems for granting users permission to access your buckets and objects: [IAM](https://docs.cloud.google.com/storage/docs/access-control/iam) and [Access Control Lists (ACLs)](https://docs.cloud.google.com/storage/docs/access-control/lists). These systems act in parallel - in order for a user to access a Cloud Storage resource, only one of the systems needs to grant the user permission. IAM is used throughout Google Cloud and allows you to grant a variety of permissions at the bucket and project levels. ACLs are used only by Cloud Storage and have limited permission options, but they allow you to grant permissions on a per-object basis.

In order to support a uniform permissioning system, Cloud Storage has uniform bucket-level access. Using this feature on a bucket disables ACLs for all Cloud Storage resources in the bucket; access to Cloud Storage resources then is granted exclusively through IAM. Uniform bucket-level access cannot be disabled after it has been active on a bucket for 90 consecutive days.

**Caution:** If you enable uniform bucket-level access, you revoke access from users who gain their access solely through object ACLs and prevent users from administrating permissions using bucket ACLs. Be sure that you read considerations when migrating an existing bucket prior to enabling uniform bucket-level access.

### Should you use uniform bucket-level access?

Generally, using uniform bucket-level access is recommended:

  * Uniform bucket-level access unifies and simplifies how you grant access to your Cloud Storage resources.

  * Uniform bucket-level access prevents unintended data exposure from ACLs.

  * Uniform bucket-level access must be enabled to use the following features:

    * [Hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview)
    * [Managed folders](https://docs.cloud.google.com/storage/docs/managed-folders)
    * [IAM conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) set directly on the bucket
  * Uniform bucket-level access must be enabled to grant [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) or [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) entities access to Cloud Storage resources.

**Note:** Even when uniform bucket-level access is disabled, Workforce Identity Federation and Workload Identity Federation entities can be added to ACLs and IAM policies, but doing so does not grant the entities any access to Cloud Storage resources, unless you subsequently enable uniform bucket-level access.



You shouldn't use uniform bucket-level access if [you want to use the ACLs system](https://docs.cloud.google.com/storage/docs/access-control/lists#iam-vs-acl) for your bucket.

### Behavior when enabled

You can enable uniform bucket-level access either when you create a new bucket, or when you explicitly [enable uniform bucket-level access](https://docs.cloud.google.com/storage/docs/using-uniform-bucket-level-access#set) on an existing bucket.

Once enabled, a bucket has the following behavior:

  * Requests to set, read, or modify bucket and object ACLs fail with `400 Bad Request` errors.

    * This includes JSON API requests using any [`BucketAccessControls`](https://docs.cloud.google.com/storage/docs/json_api/v1/bucketAccessControls), [`DefaultObjectAccessControls`](https://docs.cloud.google.com/storage/docs/json_api/v1/defaultObjectAccessControls), or [`ObjectAccessControls`](https://docs.cloud.google.com/storage/docs/json_api/v1/objectAccessControls) methods.
  * JSON API requests for a full projection of bucket or object metadata include an empty ACL list as part of the response.

  * Individual [object ownership](https://docs.cloud.google.com/storage/docs/access-control/lists#ownership) no longer exists; access that is granted from such ownership is revoked, and requests for bucket and object metadata no longer contain an `owner` field.

  * At creation time, buckets receive specialized IAM roles. If you enable uniform bucket-level access as part of creating a new bucket, that bucket gets [additional IAM roles](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#basic-roles-modifiable).

    * This behavior maintains the permissioning that objects would have inherited from the standard [default object ACL](https://docs.cloud.google.com/storage/docs/access-control/lists#default) for a bucket.

    * If you enable uniform bucket-level access on an existing bucket, you must apply any such roles manually; if you have previously changed the bucket's default object ACL, you likely want to apply a different set of IAM roles.




### Behavior if reverted

To support the ability to disable uniform bucket-level access and revert to using ACLs, Cloud Storage saves existing ACLs. If you disable uniform bucket-level access:

  * Objects regain their saved ACLs.

  * Any objects added to the bucket after uniform bucket-level access was enabled gain ACLs according to the [default object ACLs](https://docs.cloud.google.com/storage/docs/access-control/lists#default) used by the bucket.




### Requirements for disabling uniform bucket-level access

In order to disable uniform bucket-level access, the following must be true:

  * The feature has been enabled for less than 90 consecutive days.

  * You have [removed any IAM conditions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#conditions-remove) from the bucket's IAM policy.

  * The bucket is not subject to the [Require uniform bucket-level access](https://docs.cloud.google.com/storage/docs/org-policy-constraints#uniform-access) organization policy constraint.

  * You have deleted any [managed folders](https://docs.cloud.google.com/storage/docs/managed-folders) from the bucket.




## Considerations when migrating an existing bucket

When you enable uniform bucket-level access on an existing bucket, you should ensure that users and services that previously relied on ACLs for access have their permissions migrated to IAM. This section outlines some steps you should take when migrating a bucket to uniform bucket-level access. Note that since ACLs and IAM are [synchronized for bucket permissions](https://docs.cloud.google.com/storage/docs/access-control/iam#acls), your considerations focus specifically on access to objects within your bucket and not on access to the bucket.

### Consider whether a bucket-level IAM permission overexposes data

Before assigning IAM equivalents to your ACLs, consider the following:

  * An IAM permission applied at the bucket level applies to **all** objects in the bucket, whereas object ACLs can vary from object to object.



If there is access that you want to apply to some objects but not others, you should group objects into separate buckets. Each grouping should contain those objects that have the same permissions.

### Check object ACL usage

When migrating to uniform bucket-level access, you should check to see if objects in the bucket are being accessed through the ACLs applied to them. To check this, [Cloud Monitoring](https://docs.cloud.google.com/monitoring) has a metric that tracks ACL usage. If this metric indicates users or services rely on ACLs for access to your objects, you should assign IAM equivalents to the bucket before enabling uniform bucket-level access. For a guide to checking ACL usage in Monitoring, see [Check for ACL usage](https://docs.cloud.google.com/storage/docs/using-uniform-bucket-level-access#acl-check).

Use this metric to determine if enabling uniform bucket-level access would break your workflow:

Metric | Description  
---|---  
`storage.googleapis.com/authz/acl_operations_count`[](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-storage) |  The number of ACL operations that will be disabled once uniform bucket-level access is enabled, broken down by ACL operation type and bucket. **Caution:** This metric provides data about ACL usage within the past [24 months only](https://docs.cloud.google.com/monitoring/quotas#data_retention_policy). It doesn't include earlier ACL usage.   
  
An important ACL operation to examine is `OBJECT_ACCESS_REQUIRED_OBJECT_ACL`:

  * If this number is zero, no object level ACLs were required to access objects within the past 24 months. IAM policies are covering the necessary permissions at the bucket or project level.

  * If this number is greater than zero, there were requests to access objects within the past 24 months that required object ACL permissions. You should assign equivalent IAM policies before enabling uniform bucket-level access.




For more information on Monitoring metrics, see [Metrics, Time Series, and Resources](https://docs.cloud.google.com/monitoring/api/v3/metrics).

### Check the bucket's default object ACL

Buckets without uniform bucket-level access have a [default object ACL](https://docs.cloud.google.com/storage/docs/access-control/lists#default) associated with them. New objects added to such buckets have this default object ACL applied to them unless an ACL is explicitly supplied at the time the object is added to the bucket.

For example, buckets commonly use the `projectPrivate` predefined ACL as their default object ACL. `projectPrivate` grants the object `READER` permission to the [project viewers](https://docs.cloud.google.com/storage/docs/access-control/iam#convenience-values) associated with the bucket, and it grants the object `OWNER` permission to the project editors and owners associated with the bucket.

Prior to enabling uniform bucket-level access, [check the default object ACL](https://docs.cloud.google.com/storage/docs/access-control/create-manage-lists#defaultobjects) that your bucket has. Consider whether you want to grant the permissions associated with the default object ACL after you've enabled uniform bucket-level access. If so, assign IAM equivalents to the bucket.

### Assign IAM equivalents to object ACLs

Object ACLs can grant access that IAM currently does not. To ensure existing users do not lose access to objects when you enable uniform bucket-level access, use the following table and [assign affected users](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#bucket-add) the appropriate IAM roles.

Object ACL permission | Equivalent IAM role  
---|---  
`READER` | Storage Legacy Object Reader (`roles/storage.legacyObjectReader`)  
`OWNER` | Storage Legacy Object Owner (`roles/storage.legacyObjectOwner`)  
  
## Considerations when using IAM Conditions

To prevent conflicts between a bucket's IAM policies and object ACLs, [IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) can only be used on buckets with uniform bucket-level access enabled. This means:

  * To set IAM Conditions on a bucket, you must first [enable uniform bucket-level access](https://docs.cloud.google.com/storage/docs/using-uniform-bucket-level-access#set) on that bucket.

  * Before you can [disable uniform bucket-level access on a bucket](https://docs.cloud.google.com/storage/docs/using-uniform-bucket-level-access#set), you must first remove all IAM Conditions from that bucket's policy. For information on how to view and remove conditions from a bucket's policy, see [Using IAM Conditions on bucket](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#conditions-iam).




## What's next

  * Learn how to [use uniform bucket-level access](https://docs.cloud.google.com/storage/docs/using-uniform-bucket-level-access).
  * Learn about the [enforce uniform bucket-level access constraint](https://docs.cloud.google.com/storage/docs/org-policy-constraints#uniform-access), which you can set within your Google Cloud organization, folder, or project.
  * [Set IAM permissions on buckets and projects](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#bucket-add).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
