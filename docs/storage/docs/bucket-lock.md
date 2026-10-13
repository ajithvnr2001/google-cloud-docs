---
url: https://docs.cloud.google.com/storage/docs/bucket-lock/
title: Bucket Lock \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:27:53.167294+00:00
---

# Bucket Lock  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/bucket-lock/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Bucket Lock Stay organized with collections  Save and categorize content based on your preferences. 

[Setup](https://docs.cloud.google.com/storage/docs/using-bucket-lock)

This page discusses the Bucket Lock feature, which lets you configure a Cloud Storage bucket's retention policy. This policy governs how long objects in the bucket must be retained. The feature also lets you lock the bucket's retention policy, permanently preventing the policy from being reduced or removed.

This feature can provide immutable storage on Cloud Storage. In conjunction with [Detailed audit logging mode](https://docs.cloud.google.com/storage/docs/org-policy-constraints#audit-logging), which logs Cloud Storage request and response details, Bucket Lock [can help with regulatory and compliance requirements](https://docs.cloud.google.com/security/compliance/sec-us), such as those associated with FINRA, SEC, and CFTC. Bucket Lock can also help you address certain health care industry retention regulations.

## Overview

  * You can add a _retention policy_ to a bucket to specify a _retention period_.

    * When a bucket retention policy is set, objects in the bucket can only be deleted or replaced once their age is greater than the retention period.

    * The policy retroactively applies to existing objects in the bucket as well as new objects added to the bucket. This differs from the [Object Retention Lock](https://docs.cloud.google.com/storage/docs/object-lock) feature, which lets you define data retention requirements on a per-object basis.

  * You can _lock_ a bucket's retention policy to **permanently** set it on the bucket.

    * Once you lock a policy, you cannot remove it or reduce the retention period it has.

    * You cannot delete a bucket with a locked policy unless every object in the bucket has met the retention period.

    * You can increase the retention period of a locked policy.

**Caution:** Locking a bucket's retention policy is an irreversible action. For more information, see [Retention policy locks](https://docs.cloud.google.com/storage/docs/bucket-lock#policy-locks).



## Bucket retention policies

You can include a retention policy when creating a new bucket, or you can [add a retention policy to an existing bucket](https://docs.cloud.google.com/storage/docs/using-bucket-lock#set-policy). Placing a retention policy on a bucket ensures that all current and future objects in the bucket cannot be deleted or replaced until they reach the age you define in the policy. Attempts to delete or replace objects whose age is less than the retention period fail with a `403 - retentionPolicyNotMet` error.

For example, say you have a bucket with two objects in it: Object A you added a month ago, and Object B you added two years ago. If you apply a retention policy to your bucket that has a retention period of 1 year, you cannot delete or replace Object A for another 11 months: it is currently 1 month old, but must be a least 1 year old to delete or replace. Object B, on the other hand, can be deleted or replaced immediately, since its age is greater than the retention period. If you decided to replace Object B, this new version of Object B has an age that restarts at 0 years.

To help track when individual objects are eligible for deletion, objects in a bucket with a retention policy each have _retention expiration time_ metadata. This piece of metadata shows the date and time when an object fulfills the retention period.

### General considerations

When working with retention policies, keep in mind the following:

  * Unless a bucket's retention policy is locked, you can increase, decrease, or remove the policy.

  * An object's [editable metadata](https://docs.cloud.google.com/storage/docs/metadata#editable) is not subject to a bucket's retention policy and can be modified even when the object itself cannot be.

  * A bucket's retention policy contains an _effective time_ , the time after which all objects in the bucket are guaranteed to be in compliance with the retention period.

  * To see the earliest date when a given object is eligible for deletion in a bucket with a retention policy, view the _retention expiration date_ portion of the [object's metadata](https://docs.cloud.google.com/storage/docs/viewing-editing-metadata#view).




### Considerations with other features

The following are interactions that retention policies have with other Cloud Storage features:

  * In buckets that use [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning), a live object version that has a retention expiration date in the future can still be made noncurrent, and any versioned objects that exist in the bucket at the time you apply a retention policy are also protected by the policy.

  * An object that is subject to an [event-based hold](https://docs.cloud.google.com/storage/docs/object-holds) cannot be deleted while the hold applies to it. Once the event-based hold is removed from the object, [the object's retention period is reset](https://docs.cloud.google.com/storage/docs/object-holds#example).

  * An individual object can be subject to the bucket's retention policy and to its own, individual [retention configuration](https://docs.cloud.google.com/storage/docs/object-lock). If an object is subject to both, it is retained until both retentions have been satisfied.

  * You cannot destroy [Cloud Key Management Service key versions](https://docs.cloud.google.com/kms/docs/object-hierarchy#key_versions) that encrypt objects in locked buckets if the objects haven't met their retention expiration times. For more information, see [Key versions used to encrypt locked objects](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys#locked-objects).

  * You can use [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle) to automatically delete objects in a bucket, including in a bucket with a locked policy. A lifecycle rule won't delete an object until after the object fulfills the retention policy.

  * You should not perform [parallel composite uploads](https://docs.cloud.google.com/storage/docs/parallel-composite-uploads) if your bucket has a retention policy, because the component pieces cannot be deleted until each has met the bucket's minimum retention period.

  * Attempting to [complete an XML API multipart upload](https://docs.cloud.google.com/storage/docs/xml-api/post-object-complete) fails if the resulting object would overwrite an object that has not yet met its retention period.

  * You can use the [retention policy constraint](https://docs.cloud.google.com/storage/docs/org-policy-constraints#retention) in your [organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) to require that bucket retention policies with specific retention periods be included as part of creating a new bucket or as part of adding/updating the retention policy on an existing bucket.




### Retention periods

Retention periods are measured in seconds; however, some tools, like the [Google Cloud console](https://docs.cloud.google.com/storage/docs/cloud-console) and the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/storage) allow you to set and view retention periods with other units of time for convenience. The following conversions apply in such cases:

  * A day is considered to be 86,400 seconds.
  * A week is considered to be 7 days, which is 604,800 seconds.
  * A month is considered to be 31 days, which is 2,678,400 seconds.
  * A year is considered to be 365.25 days, which is 31,557,600 seconds.



You can set a maximum retention period of 3,155,760,000 seconds (100 years).

#### gcloud CLI

For the gcloud CLI, you should specify the retention period using the following format:
    
    
    P#Y#M#W#DT#H#M#S

In this format, each # represents an integer you specify, which should be followed by a unit of time. The units `Y`, `W`, `D`, `H`, and `S` signify years, weeks, days, hours, and seconds, respectively. `M` signifies months when it comes after `P`, while `M` signifies minutes when it comes after `T`.

You must include at least one integer-unit pair as part of your retention period, but you can omit any integer-unit pairs that you don't need.

For example, `P1DT720M` sets a retention period of 1 day and 720 minutes (one and a half days).

## Retention policy locks

When you [lock a bucket's retention policy](https://docs.cloud.google.com/storage/docs/using-bucket-lock#lock-bucket), you prevent the policy from ever being removed or the retention period from ever being reduced (although you can still increase the retention period). If you try to remove or reduce the policy duration of a locked bucket, you get a `400 BadRequestException` error. Once a retention policy is locked, you cannot delete the bucket until every object in the bucket has met the retention period.

**Locking a bucket's retention policy is irreversible** , and you should be familiar with the implications of doing so prior to using this feature. When you use an _unlocked_ policy, you have the ability to remove the policy, allowing you to still delete objects when desired. When you _lock_ a policy, you must delete the entire bucket in order to "remove" the policy. However, you can't delete the bucket if there are objects in it that haven't fulfilled their retention period. Thus, to "remove" a locked policy, you have to wait until every object in the bucket has fulfilled its retention period, at which point you can delete the bucket.

Additionally, when you lock a retention policy, Cloud Storage automatically applies a [lien](https://docs.cloud.google.com/resource-manager/docs/project-liens) on the project that contains the bucket. While in place, the lien prevents the project from being deleted by blocking the `resourcemanager.projects.delete` permission. To delete the project, your project owner or organization administrator must first [remove the lien](https://docs.cloud.google.com/resource-manager/docs/project-liens#remove-liens).

For information on how locking a retention policy can help your data comply with record retention regulations, [see the compliance page](https://docs.cloud.google.com/security/compliance/sec-us).

**Important:** To maintain your retention policies and [object holds](https://docs.cloud.google.com/storage/docs/object-holds), you must keep your current Google Cloud account active and in good standing. Before discontinuing your account, you must transfer your data to another compliant service to maintain compliance. Any individual tasked with removing a [project lien](https://docs.cloud.google.com/resource-manager/docs/project-liens) associated with a locked bucket should be someone with legal or compliance accountability and outside of your IT department's accountability chain. For more information, see the Cloud Storage section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms).

## What's next

  * Learn to [use and lock retention policies](https://docs.cloud.google.com/storage/docs/using-bucket-lock).
  * Learn about [Object Retention Lock](https://docs.cloud.google.com/storage/docs/object-lock) and [object holds](https://docs.cloud.google.com/storage/docs/object-holds), which provide ways to protect individual objects from deletion.
  * Learn about [Detailed audit logging mode](https://docs.cloud.google.com/storage/docs/org-policy-constraints#audit-logging), which can also help with regulatory and compliance requirements.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
