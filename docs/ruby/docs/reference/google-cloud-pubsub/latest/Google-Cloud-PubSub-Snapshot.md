---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Snapshot/
title: Cloud Pub/Sub API - Class Google::Cloud::PubSub::Snapshot (v2.23.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:48.977636+00:00
---

# Cloud Pub/Sub API - Class Google::Cloud::PubSub::Snapshot (v2.23.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Snapshot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Pub/Sub API - Class Google::Cloud::PubSub::Snapshot (v2.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.5.0 (latest)  3.4.1  3.3.0  3.2.1  3.1.1  3.0.3  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.1  2.17.0  2.16.0  2.15.5  2.14.0  2.12.1  2.11.0  2.10.0  2.9.2 

Reference documentation and code samples for the Cloud Pub/Sub API class Google::Cloud::PubSub::Snapshot.

## Snapshot

A named resource created from a subscription to retain a stream of messages from a topic. A snapshot is guaranteed to retain:

  * The existing backlog on the subscription. More precisely, this is defined as the messages in the subscription's backlog that are unacknowledged upon the successful completion of the `create_snapshot` operation; as well as:
  * Any messages published to the subscription's topic following the successful completion of the `create_snapshot` operation.



## Inherits

  * Object 



## Example
    
    
    require "google/cloud/pubsub"
    
    pubsub = Google::Cloud::PubSub.new
    sub = pubsub.subscription "my-sub"
    
    snapshot = sub.create_snapshot "my-snapshot"
    snapshot.name #=> "projects/my-project/snapshots/my-snapshot"

## Methods 

### #delete
    
    
    def delete() -> Boolean

Removes an existing snapshot. All messages retained in the snapshot are immediately dropped. After a snapshot is deleted, a new one may be created with the same name, but the new one has no association with the old snapshot or its subscription, unless the same subscription is specified.

**Returns**

  * (Boolean) — Returns `true` if the snapshot was deleted. 



**Example**
    
    
    require "google/cloud/pubsub"
    
    pubsub = Google::Cloud::PubSub.new
    
    pubsub.snapshots.each do |snapshot|
      snapshot.delete
    end

### #expiration_time
    
    
    def expiration_time() -> Time

The snapshot is guaranteed to exist up until this time. A newly-created snapshot expires no later than 7 days from the time of its creation. Its exact lifetime is determined at creation by the existing backlog in the source subscription. Specifically, the lifetime of the snapshot is 7 days - (age of oldest unacked message in the subscription). For example, consider a subscription whose oldest unacked message is 3 days old. If a snapshot is created from this subscription, the snapshot -- which will always capture this 3-day-old backlog as long as the snapshot exists -- will expire in 4 days.

**Returns**

  * (Time) — The time until which the snapshot is guaranteed to exist. 



**Example**
    
    
    require "google/cloud/pubsub"
    
    pubsub = Google::Cloud::PubSub.new
    sub = pubsub.subscription "my-sub"
    
    snapshot = sub.create_snapshot "my-snapshot"
    snapshot.topic.name #=> "projects/my-project/topics/my-topic"
    snapshot.expiration_time

### #labels
    
    
    def labels() -> Hash

A hash of user-provided labels associated with this snapshot. Labels can be used to organize and group snapshots.See [Creating and Managing Labels](https://cloud.google.com/pubsub/docs/labels).

The returned hash is frozen and changes are not allowed. Use [#labels=](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Snapshot#Google__Cloud__PubSub__Snapshot_labels__instance_ "Google::Cloud::PubSub::Snapshot#labels= \(method\)") to update the labels for this snapshot.

**Returns**

  * (Hash) — The frozen labels hash. 



### #labels=
    
    
    def labels=(new_labels)

Sets the hash of user-provided labels associated with this snapshot. Labels can be used to organize and group snapshots. Label keys and values can be no longer than 63 characters, can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter and each label in the list must have a different key. See [Creating and Managing Labels](https://cloud.google.com/pubsub/docs/labels).

**Parameter**

  * **new_labels** (Hash) — The new labels hash. 



**Raises**

  * (ArgumentError) 



### #name
    
    
    def name() -> String

The name of the snapshot.

**Returns**

  * (String) — A fully-qualified snapshot name in the form `projects/{project_id}/snapshots/{snapshot_id}`. 



### #topic
    
    
    def topic() -> Topic

The [Topic](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Topic "Google::Cloud::PubSub::Topic \(class\)") from which this snapshot is retaining messages.

**Returns**

  * ([Topic](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Topic)) 



**Example**
    
    
    require "google/cloud/pubsub"
    
    pubsub = Google::Cloud::PubSub.new
    sub = pubsub.subscription "my-sub"
    
    snapshot = sub.create_snapshot "my-snapshot"
    snapshot.topic.name #=> "projects/my-project/topics/my-topic"

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
