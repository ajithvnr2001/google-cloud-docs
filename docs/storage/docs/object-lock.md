---
url: https://docs.cloud.google.com/storage/docs/object-lock/
title: Object Retention Lock \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:16.617987+00:00
---

# Object Retention Lock  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/object-lock/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Object Retention Lock Stay organized with collections  Save and categorize content based on your preferences. 

[Setup](https://docs.cloud.google.com/storage/docs/using-object-lock)

This page discusses the Object Retention Lock feature, which lets you set a retention configuration on objects within Cloud Storage buckets that have enabled the feature. A retention configuration governs how long the object must be retained and has the option to permanently prevent the retention time from being reduced or removed.

In conjunction with [Detailed audit logging mode](https://docs.cloud.google.com/storage/docs/org-policy-constraints#audit-logging), which logs Cloud Storage request and response details, Object Retention Lock [can help with regulatory and compliance requirements](https://docs.cloud.google.com/security/compliance/sec-us), such as those associated with FINRA, SEC, and CFTC. It can also help you address regulations in other industries such as health care.

## Overview

Object Retention Lock lets you define data retention requirements on a per-object basis. This differs from [Bucket Lock](https://docs.cloud.google.com/storage/docs/bucket-lock), which defines data retention requirements uniformly for all objects in a bucket. To set or update retention configurations for millions or billions of objects with a single job, use [storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview).

With Object Retention Lock, the _retention configuration_ that you place on an object contains the following properties:

  * A _retain-until time_ that specifies a date and time until which the object must be retained. Prior to this time, the object cannot be deleted or replaced. Note that an object that hasn't reached this retain-until time can still be [made noncurrent](https://docs.cloud.google.com/storage/docs/object-versioning).

    * The retain-until time has a maximum value of 3,155,760,000 seconds (100 years) from the current date and time.
  * A _retention mode_ that controls what changes you can make to the retention configuration.

    * `Unlocked` allows authorized users to modify or remove an object's retention configuration without any limitations. In the XML API, this mode is named `GOVERNANCE`.

    * `Locked` permanently prevents the retention date from being reduced or removed. Once set to `Locked`, the mode cannot be changed, and the retention period can only be increased. In the XML API, this mode is named `COMPLIANCE`.

    * Locking a retention configuration can help your data [comply with record retention regulations](https://docs.cloud.google.com/security/compliance/sec-us).




You can only set retention configurations on objects that reside in buckets that have enabled the feature.

  * Existing buckets can only enable the feature using the Google Cloud console.

  * Once enabled, the feature cannot be disabled on a bucket.

  * After you enable the feature on a bucket, Cloud Storage applies a [lien](https://docs.cloud.google.com/resource-manager/docs/project-liens) to the `projects.delete` permission for the project that contains the bucket, at best effort. To find out whether a lien has been applied, [list all project liens](https://docs.cloud.google.com/resource-manager/docs/project-liens#listing_liens_on_a_project).

While in place, the lien prevents the project from being deleted. To delete the project, you must first [remove the lien](https://docs.cloud.google.com/resource-manager/docs/project-liens#removing_liens_from_a_project).




## Considerations

  * A bucket containing retained objects cannot be deleted until the retain-until time on all objects in the bucket has passed and all objects inside the bucket have been deleted.

  * An object can be subject to both its own retention configuration and an overall [bucket retention policy](https://docs.cloud.google.com/storage/docs/bucket-lock). If it is, the object is retained until both retentions that apply to it have been satisfied.

  * If you configure object-level retention policies on a large number of objects in a bucket, be aware that you must remove each object's retention configuration individually or wait until the retain-until time on all objects in the bucket has passed before the bucket can be deleted. To remove object-level retention policies in bulk, you might require long-running [ storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview) jobs.

  * Requests that attempt to set a retention configuration on a object that is subject to an [event-based hold](https://docs.cloud.google.com/storage/docs/object-holds) fail.

    * Requests that would simultaneously set a retention configuration for an object and place an event-based hold on the object similarly fail.

    * An object can simultaneously have a retention configuration and a [temporary hold](https://docs.cloud.google.com/storage/docs/object-holds).

  * You cannot destroy [Cloud Key Management Service key versions](https://docs.cloud.google.com/kms/docs/object-hierarchy#key_versions) that encrypt locked objects if the objects haven't met their retention expiration times. For more information, see [Key versions used to encrypt locked objects](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys#locked-objects).

  * You can use [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle) to automatically delete objects, but a lifecycle rule won't delete an object until after the object has reached its retention expiration date, even if the conditions of the lifecycle rule have been met.

  * In buckets that use [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning), a live object version that has a retain-until time in the future can still be made noncurrent.

  * You shouldn't set retention configurations on objects that are meant to be temporary, such as component pieces of a [parallel composite upload](https://docs.cloud.google.com/storage/docs/parallel-composite-uploads).

  * An object's [editable metadata](https://docs.cloud.google.com/storage/docs/metadata#editable) is not subject to the retention configuration and can be modified even when the object itself cannot be.




## What's next

  * [Use object retentions](https://docs.cloud.google.com/storage/docs/using-object-lock).
  * Learn about other Cloud Storage features that [protect objects and control their lifecycles](https://docs.cloud.google.com/storage/docs/control-data-lifecycles).
  * Learn about [Detailed audit logging mode](https://docs.cloud.google.com/storage/docs/org-policy-constraints#audit-logging), which can also help with regulatory and compliance requirements.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
