---
url: https://docs.cloud.google.com/storage/docs/org-policy-constraints/
title: Organization policy constraints for Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:12.115562+00:00
---

# Organization policy constraints for Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/org-policy-constraints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Organization policy constraints for Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

This page provides supplemental information about [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) constraints that apply to Cloud Storage. Use constraints to enforce bucket and object behaviors across an entire project or organization. Organization policy constraints can either be [boolean constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#boolean-constraint) or [list constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#list-constraint).

Note that enforcing or disabling any constraints might take up to 10 minutes to go into effect.

## Cloud Storage constraints

The following constraints can be applied to an organization policy and relate to Cloud Storage:

### Enforce public access prevention

**Constraint Name** : `constraints/storage.publicAccessPrevention` **Constraint Type** : `boolean`

When you apply the `publicAccessPrevention` constraint on a resource, [public access is restricted](https://docs.cloud.google.com/storage/docs/public-access-prevention#enforced) for all buckets and objects, both new and existing, under that resource.

### Soft delete retention duration

**Constraint Name** : `constraints/storage.softDeletePolicySeconds` **Constraint Type** : `list`

When you apply the `softDeletePolicySeconds` constraint, you specify one or more [soft delete](https://docs.cloud.google.com/storage/docs/soft-delete) retention durations (`softDeletePolicy.retentionDuration`) as part of the constraint. The constraint validates that any request to create a new bucket or update the soft delete retention duration of an existing bucket must explicitly include one of the specified allowed retention durations. For example, if you set the retention duration to 864000 seconds (10 days) as part of this constraint, any request to create or update a bucket within the organization must include a soft delete retention duration of `864000` in the request payload. Requests that omit this configuration will fail.

This constraint only validates requests to create a new bucket or update an existing bucket in the organization. It doesn't otherwise affect pre-existing buckets.

If you set multiple `softDeletePolicySeconds` constraints at different resource levels, they are [enforced hierarchically](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy#hierarchy_evaluation_rules). For this reason, it's recommended that you set the `inheritFromParent` field to `true`, which ensures that policies at higher layers are also considered.

### Bucket retention policy duration in seconds

**Constraint Name** : `constraints/storage.retentionPolicySeconds` **Constraint Type** : `list`

When you apply the `retentionPolicySeconds` constraint, you specify one or more durations as part of the constraint. Once set, bucket [retention policies](https://docs.cloud.google.com/storage/docs/bucket-lock) must include one of the specified durations. `retentionPolicySeconds` is required when creating a new bucket and when adding or updating the retention period of a pre-existing bucket; however, it's not otherwise required on pre-existing buckets.

If you set multiple `retentionPolicySeconds` constraints at different resource levels, they are [enforced hierarchically](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy#hierarchy_evaluation_rules). For this reason, it's recommended that you set the `inheritFromParent` field to `true`, which ensures that policies at higher layers are also considered.

### Require uniform bucket-level access

**Constraint Name** : `constraints/storage.uniformBucketLevelAccess` **Constraint Type** : `boolean`

When you apply the `uniformBucketLevelAccess` constraint, [new buckets](https://docs.cloud.google.com/storage/docs/creating-buckets) must enable the [uniform bucket-level access feature](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access), and pre-existing buckets with this feature enabled cannot disable it. Pre-existing buckets with uniform bucket-level access disabled are not required to enable it.

**Note:** Some organizations have the `uniformBucketLevelAccess` constraint enabled by default. To find out whether your organization has the `uniformBucketLevelAccess` constraint enabled or disabled, contact your organization administrator.

### Detailed audit logging mode

**Constraint Name** : `constraints/gcp.detailedAuditLoggingMode` **Constraint Type** : `boolean`

When you apply the `detailedAuditLoggingMode` constraint, Cloud Audit Logs logs associated with [Cloud Storage operations](https://docs.cloud.google.com/storage/docs/audit-logging) contain detailed request and response information. This constraint is recommended to be used in conjunction with [Bucket Lock](https://docs.cloud.google.com/storage/docs/bucket-lock) and [Object Retention Lock](https://docs.cloud.google.com/storage/docs/object-lock) when [seeking various compliances](https://docs.cloud.google.com/security/compliance/sec-us) such as SEC Rule 17a-4(f), CFTC Rule 1.31(c)-(d), and FINRA Rule 4511(c).

Logged information includes query parameters, path parameters, and request body parameters. Logs exclude certain parts of requests and responses that are associated with sensitive information. For example, logs exclude:

  * Credentials, such as `Authorization`, `X-Goog-Signature`, or `upload-id`.
  * Encryption key information, such as `x-goog-encryption-key`.
  * Raw object data.



When using this constraint, note the following:

  * Detailed request and response information is not guaranteed; in rare cases, empty logs might be returned.
  * Enabling `detailedAuditLoggingMode` increases the amount of data stored in audit logs, which could affect your [Cloud Logging charges](https://docs.cloud.google.com/stackdriver/pricing#logging-costs) for Data Access logs.
  * Logged requests and responses are recorded in a generic format that matches the field names of the JSON API.



### Restrict authentication types

**Constraint Name** : `constraints/storage.restrictAuthTypes` **Constraint Type** : `list`

When you apply the `restrictAuthTypes` constraint, requests to access Cloud Storage resources using the restricted authentication type fail, regardless of the validity of the request. You can use the `restrictAuthTypes` constraint to restrict [HMAC keys](https://docs.cloud.google.com/storage/docs/authentication/hmackeys) to meet regulatory requirements or increase the security of your data.

The [list constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#list-constraint) explicitly denies specific authentication types while permitting all others. To do so, you must list the restricted authentication types in the `deniedValues` key within the `rules` of the `restrictAuthTypes` constraint. An error occurs if you try to list the restricted authentication types in the `allowedValues` key.

You can restrict the following authentication types:

  * `SERVICE_ACCOUNT_HMAC_SIGNED_REQUESTS`: Restricts requests signed by service account HMAC keys.

  * `USER_ACCOUNT_HMAC_SIGNED_REQUESTS`: Restricts requests [signed](https://docs.cloud.google.com/storage/docs/authentication/signatures#signing-process) by user account HMAC keys.

  * `RSA_SIGNED_REQUESTS`: Restricts requests [signed](https://docs.cloud.google.com/storage/docs/authentication/signatures#signing-process) by RSA keys.

  * `in:ALL_HMAC_SIGNED_REQUESTS`: Restrict requests signed by any HMAC key. If you need to meet data sovereignty requirements, it's recommended that you restrict all HMAC signed requests.

  * `in:ALL_SIGNED_REQUESTS`: Restrict requests signed by any HMAC or RSA key.




When you enable this constraint, the following occurs:

  * Cloud Storage restricts access for requests that are authenticated with the restricted authentication type. Requests fail with the error `403 Forbidden`.

  * Entities that were previously authorized to perform the request receive an error message explaining that the authentication type is disabled.

  * If HMAC keys are restricted:

    * HMAC keys of the restricted type can no longer be created or activated in the resource that the constraint is enforced upon. Requests to create or activate HMAC keys fail with the error `403 Forbidden`.

    * Existing HMAC keys remain but are no longer usable. They can be deactivated or deleted, but cannot be reactivated.




When using the `restrictAuthTypes` constraint, be aware of existing resources that depend on HMAC authentication. For example, if you migrated from Amazon Simple Storage Service (Amazon S3), your application likely uses HMAC keys to authenticate requests to Cloud Storage. You can use the Cloud Monitoring metric `storage.googleapis.com/authn/authentication_count` to track the number of times HMAC keys have been used to authenticate requests.

### Restrict unencrypted HTTP requests

**Constraint Name** : `constraints/storage.secureHttpTransport` **Constraint Type** : `boolean`

When you apply the `secureHttpTransport` constraint, all unencrypted HTTP access to Cloud Storage resources is denied.

  * By default, the [Cloud Storage XML API](https://docs.cloud.google.com/storage/docs/xml-api/overview) allows unencrypted HTTP access.
  * [`CNAME` redirects](https://docs.cloud.google.com/storage/docs/request-endpoints#custom-domains) only support unencrypted HTTP access. 



### Additional constraints

The following organization policy constraints apply more generally throughout Google Cloud, but are often applied to the Cloud Storage service:

  * [**`constraints/gcp.restrictNonCmekServices`**](https://docs.cloud.google.com/kms/docs/cmek-org-policy#require-cmek): Require new and rewritten objects to be encrypted using [customer-managed encryption keys](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys), and require new buckets to set a Cloud KMS key as the default encryption key.

  * [**`constraints/gcp.restrictCmekCryptoKeyProjects`**](https://docs.cloud.google.com/kms/docs/cmek-org-policy#project-constraint): Reject requests to Cloud Storage if the request includes a [customer-managed encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) and the key does not belong to a project specified by the constraint. Similarly, reject requests that create or rewrite an object if the object would be encrypted by the bucket's default encryption key and that key does not belong to a project specified by the constraint.

  * [**`constraints/gcp.restrictTLSVersion`**](https://docs.cloud.google.com/docs/security/compliance/restrict-tls-versions): Prevent access to Cloud Storage by requests made using Transport Layer Security (TLS) 1.0 or 1.1.




## Conditionally allow or deny organization policy constraints

Tags provides a way to conditionally allow or deny organization policies based on whether a Cloud Storage bucket has a specific tag. See [setting an organization policy with tags](https://docs.cloud.google.com/resource-manager/docs/organization-policy/tags-organization-policy) for detailed instructions.

## What's next

  * Learn about the [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#resource-hierarchy-detail) that applies to organization policies.
  * See [Creating and managing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies) for instructions on working with constraints and organization policies in the Google Cloud console.
  * See [Using constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints) for instructions on working with constraints and organization policies in the gcloud CLI.
  * Learn about [custom constraints for Cloud Storage](https://docs.cloud.google.com/storage/docs/custom-constraints).
  * See the Resource Manager API [reference documentation](https://docs.cloud.google.com/resource-manager/reference/rest) for relevant API methods, such as [`projects.setOrgPolicy`](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setOrgPolicy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
