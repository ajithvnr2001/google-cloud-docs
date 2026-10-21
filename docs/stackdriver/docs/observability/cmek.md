---
url: https://docs.cloud.google.com/stackdriver/docs/observability/cmek/
title: Support for CMEKs \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:46.007105+00:00
---

# Support for CMEKs  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/observability/cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Support for CMEKs Stay organized with collections  Save and categorize content based on your preferences. 

By default, Google Cloud Observability encrypts customer content at rest. Google Cloud Observability handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Google Cloud Observability. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you view audit logs and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Google Cloud Observability resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

Google Cloud Observability can use customer-managed encryption keys (CMEKs) to encrypt data stored in observability datasets. These datasets store your trace data. This document lists the supported organization policies, introduces default settings for observability buckets, and describes how organization policies and default settings interact.

This document doesn't apply to Cloud Logging, which can encrypt data stored in log buckets with CMEKs. For more information, see [Configure CMEKs for Cloud Logging](https://docs.cloud.google.com/logging/docs/routing/managed-encryption).

## Supported organization policy constraints

To control where your observability buckets are created and who manages the encryption keys for those buckets, you might want to configure the following organization policies:

  * A policy with a constraint ID `constraints/gcp.resourceLocations`. This policy [defines the set of locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) where new resources can be created. To use observability buckets, this set of locations must include at least one [supported observability buckets location](https://docs.cloud.google.com/stackdriver/docs/observability/observability-bucket-locations).

  * A `Deny` policy with the constraint ID `constraints/gcp.restrictNonCmekServices`. This policy requires that [new resources are encrypted with CMEKs](https://docs.cloud.google.com/kms/docs/cmek-org-policy).

  * A policy with the constraint ID `constraints/gcp.restrictCmekCryptoKeyProjects`. This policy limits which Cloud Key Management Service keys are used for encryption.




You can create organization policies that apply at the organization, folder, or project level. For more information, see [Creating and editing policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#creating_and_editing_policies).

**Note:** If you configure organization policies that require use of CMEKs, then you must configure default settings for observability buckets. For example, if you create an organization policy that requires CMEK for a specific folder, then for that folder or for one of its hierarchical ancestors, you must configure default settings. If you don't configure default settings, then provisioning for system-created observability buckets fails.

## About default settings for observability buckets

Google Cloud Observability provides default settings for observability buckets, which are applied to a project, folder, or organization. These default settings work together with your organization policies to make sure that new observability buckets are in the location you prefer and use the encryption model you specify.

For organizations, folders, and projects, default settings for observability buckets let you configure the following:

  * A default storage location.
  * For each location, a default Cloud Key Management Service key.



There are two different ways the system uses default settings:

  * When the system automatically creates an observability bucket, it uses the default settings to determine the bucket's location and encryption key. If you haven't defined default settings, then the system selects the location and the bucket uses Google-default encryption.

  * When you initiate creation of an observability bucket by issuing an API request, you provide the location. However, the system automatically uses the Cloud KMS key defined by the default settings to encrypt the data, unless the arguments to the API request specify the key.




Because the parent of an observability bucket is always a project, when you create a bucket, the system first searches for project-level default settings. If those don't exist, then the system searches the parent's ancestors for default settings. For example, if you define default settings for a folder, then those settings apply to descendants of the folder, except those descendants that have default settings configured.

For more information, see [Set defaults for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets). 

## How organization policies and default settings interact

The parent of an observability bucket must be a project. That is, the system can't create an observability bucket in a folder or in an organization. However, if you configure default settings for observability buckets for an organization or a folder, then those default settings apply to all projects that are descendants of that organization or folder.

The following table lists the rules the system uses to determine the location of a new observability bucket:

Use organization policy  
to restrict location | Project (or ancestor) has a  
default storage location | How the system determines the location for a new observability bucket | No | No | The system selects the location from the supported locations for observability buckets.  
---|---|---  
Yes | No | The system selects the location from the intersection of those locations the organization policies allow and those observability buckets support. **If the intersection is empty, then the system doesn't create the observability bucket.**  
No | Yes | The system sets the location to the default storage location defined in the project's default settings. If the project doesn't define a default storage location, then the system uses the default storage location defined for an ancestor.  
Yes | Yes | The system sets the location to the default storage location defined in the project's default settings. If the project doesn't define a default storage location, then the system uses the ancestor's default storage location. **If the default storage location isn't allowed by the organization policies, then the system doesn't create the observability bucket.**  
**Note:** If you set a default Cloud KMS key for a location, then you must also set that location as the default storage location. If you don't set a default storage location, then your observability buckets aren't encrypted with your default Cloud KMS key even if those buckets are in the location where the key is defined.

The following table lists the rules the system uses to determine whether a new observability bucket uses CMEKs, and if so, the value of the Cloud KMS key. To encrypt an observability bucket, a Cloud KMS key must be in the location of the bucket and be allowed by organization policies. If you don't specify an organization policy with the `gcp.restrictCmekCryptoKeyProjects` constraint, then all keys are allowed:

Use organization policy  
to require CMEKs | Project (or ancestor) has a  
default Cloud KMS key | How the system determines which Cloud KMS key to use. | No | No | The observability bucket doesn't use CMEKs.  
---|---|---  
Yes | No | **The system doesn't create new observability buckets** because the organization policy requires CMEKs but a default Cloud KMS key isn't defined.  
No | Yes | To identify a key for encryption, the system first determines whether a default storage location is set for the project or for one of its ancestors. If not, the system selects a location and creates the observability bucket. The bucket doesn't use a CMEK. If a default storage location is found, then the system searches the project's default settings for a default Cloud KMS key. If the project's default settings don't specify an appropriate key, then the system searches the ancestor's default settings for a default key that is in the location of the new bucket. One of the following occurs:

  * A key isn't found: The new observability bucket doesn't use a CMEK.
  * A key is found and is allowed: The system creates the observability bucket.
  * A key is found but isn't allowed: **The system doesn't create the new observability bucket**.

  
Yes | Yes | To identify a key for encryption, the system first determines whether a default storage location is set for the project or for one of its ancestors. If a default storage location isn't set, then **the system doesn't create the new observability bucket**. If a default storage location is found, then the system searches the project's default settings for a default Cloud KMS key. If the project's default settings don't specify an appropriate key, then the system searches the ancestor's default settings for a default key that is in the location of the new bucket. One of the following occurs:

  * A key isn't found: **The new observability bucket isn't created.**
  * A key is found and is allowed: The system creates the observability bucket.
  * A key is found but isn't allowed: **The system doesn't create the new observability bucket**.

  
  
## Limitations

When the system creates an observability bucket, it either uses Google-default encryption or encrypts the data with a CMEK. After the bucket exists, you can update the CMEK. For more information, see [Update observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/update-observability-buckets).

## What's next

  * [Set defaults for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets) describes how to set a default storage location and a default Cloud KMS key for your observability buckets.

  * [Configure default resource settings for Cloud Logging](https://docs.cloud.google.com/logging/docs/default-settings) and [Configure CMEKs for Cloud Logging](https://docs.cloud.google.com/logging/docs/routing/managed-encryption) describe how to set a default storage location and a default Cloud KMS key for your log buckets.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
