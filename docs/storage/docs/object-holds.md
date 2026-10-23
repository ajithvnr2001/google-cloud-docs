---
url: https://docs.cloud.google.com/storage/docs/object-holds/
title: Object holds \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:34.800952+00:00
---

# Object holds  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/object-holds/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Object holds Stay organized with collections  Save and categorize content based on your preferences. 

[Usage](https://docs.cloud.google.com/storage/docs/holding-objects)

This page discusses object holds, which are metadata flags that you [place on individual objects](https://docs.cloud.google.com/storage/docs/holding-objects#set-object-hold). While an object has a hold placed on it, the object cannot be deleted or replaced. You can, however, [edit the metadata](https://docs.cloud.google.com/storage/docs/metadata#editable) of the object. To place or remove object holds on millions or billions of objects in bulk with a single job, use [Storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview).

## Types of holds

Cloud Storage offers the following types of holds:

  * **Event-based** holds
  * **Temporary** holds



An object can have one type of hold, both types, or neither hold placed on it. When an object does not have a [retention configuration](https://docs.cloud.google.com/storage/docs/object-lock) and is stored in a bucket without a [retention policy](https://docs.cloud.google.com/storage/docs/bucket-lock#overview), both hold types behave exactly the same. The following table describes how each hold type behaves if an object has a retention configuration or is stored in a bucket with a retention policy:

| Object has an event-based hold | Object has a temporary hold  
---|---|---  
Object has a retention configuration | Not applicable: Objects cannot simultaneously have an event-based hold and a retention configuration | Releasing a temporary hold does not affect the object's retain-until time  
Object is stored in a bucket with a retention policy | Releasing an event-based hold resets the object's time in the bucket for the purposes of the retention period | Releasing a temporary hold does not affect the object's time in the bucket for the purposes of the retention period  
  
#### Event-based hold example

Say you have two objects - Object A and Object B - in a bucket whose retention policy sets a 1-year retention period. When you added the objects to the bucket, you placed an event-based hold on Object A and a temporary hold on Object B. A year passes, and while you'd normally be able to delete them at this point, because both objects still have a hold on them, you can't delete either of them.

At this point, you release the hold from both objects. For Object A, which was using an event-based hold, its time in the bucket restarts for the purposes of the retention period. This means it must stay in the bucket for another year before it can be deleted or replaced. Object B, which was using a temporary hold, can immediately be deleted or replaced, because the temporary hold has no effect on when the object fulfilled its retention time.

This behavior lets you use event-based holds in conjunction with [retention policies](https://docs.cloud.google.com/storage/docs/bucket-lock#overview) to control retention based on the occurrence of some event, such as holding loan documents for a certain period after the loan was paid. Temporary holds can be used for regulatory or legal purposes, such as holding trading documents for legal investigation.

## The default event-based hold property

In addition to placing holds on individual objects, you can [enable the default event-based property](https://docs.cloud.google.com/storage/docs/holding-objects#set-default-hold) on your bucket. When you do this, each new object that subsequently gets added to the bucket automatically has an event-based hold placed on it.

This behavior is useful when you want an object to persist in your bucket for a certain length of time after a certain event occurs. For example, your bucket may be meant to store loans that you must retain for a certain number of years once they've been paid off. With a suitable retention policy and the default event-based hold property enabled for your bucket, when you upload a loan document to your bucket, it gets an event-based hold placed on it. When the loan is paid off, you can release the hold, at which point the retention policy ensures the loan remains stored and unchangeable until it fulfills the retention period set in your retention policy.

## Restrictions

  * Requests that attempt to place an event-based hold on an object that has an existing [retention configuration](https://docs.cloud.google.com/storage/docs/object-lock) fail.

    * Requests that would simultaneously place an event-based hold on an object and set a retention configuration for the object similarly fail.
  * Object holds cannot be managed with the [XML API](https://docs.cloud.google.com/storage/docs/xml-api/overview), and the hold status of an object is not included when using the XML API to [retrieve object metadata](https://docs.cloud.google.com/storage/docs/viewing-editing-metadata#view).

    * However, attempting to delete or replace an object with the XML API still fails if the object has a hold on it.

    * For [XML API multipart uploads](https://docs.cloud.google.com/storage/docs/multipart-uploads), you can initiate an upload and upload parts, but the request to complete the upload fails if it would overwrite an object that has a hold on it.

  * Object holds are not supported for buckets that use hierarchical namespace.




## What's next

  * Learn how to [enable event-based holds by default](https://docs.cloud.google.com/storage/docs/holding-objects#set-default-hold) and how to [set individual object holds](https://docs.cloud.google.com/storage/docs/holding-objects#use-object-holds).
  * Learn about [retention policies](https://docs.cloud.google.com/storage/docs/bucket-lock#overview), which protect data from deletion for a specified period of time.
  * Learn about [lifecycle configurations](https://docs.cloud.google.com/storage/docs/lifecycle) for your bucket, which can automatically delete objects after you remove their holds.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
