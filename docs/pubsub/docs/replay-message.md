---
url: https://docs.cloud.google.com/pubsub/docs/replay-message/
title: Quickstart: Replay a message in Pub/Sub by seeking to a snapshot or timestamp \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:02.667414+00:00
---

# Quickstart: Replay a message in Pub/Sub by seeking to a snapshot or timestamp  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/replay-message/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Replay a message in Pub/Sub by seeking to a snapshot or timestamp

Pub/Sub cannot retrieve the messages after you have acknowledged them. However, sometimes you might find it necessary to replay the acknowledged messages, for example, if you performed an erroneous acknowledgment. Then you can use the [Seek](https://docs.cloud.google.com/pubsub/docs/replay-overview) feature to mark previously acknowledged messages as unacknowledged, and force Pub/Sub to redeliver those messages. You can also use seek to delete the unacknowledged messages by changing their state to acknowledged.

Seek to a [snapshot](https://docs.cloud.google.com/pubsub/docs/replay-message#create_and_seek_to_snapshots) or seek to a [timestamp](https://docs.cloud.google.com/pubsub/docs/replay-message#seek_to_a_timestamp) to replay the messages in a subscription. This guide shows examples of how to replay previously acknowledged Pub/Sub messages using seek.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/freetrial?redirectPath=/http://console.cloud.google.com/?walkthrough_id=pubsub--replay-from-snapshot)

* * *

## Before you begin

Complete the following steps before running your pipeline.

### Set up your project

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. Set up a Google Cloud console project.

Set up a project

Click to:

     * Create or select a project.
     * Enable the Pub/Sub API for that project, if it is not already enabled. 

You can view and manage these resources at any time in the [Google Cloud console](https://console.cloud.google.com/).

  3. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  4. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  5. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

**Note:** You can run the gcloud CLI in the Google Cloud console without installing the Google Cloud CLI. To run the gcloud CLI in the Google Cloud console, [use Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 

  6. Set up a Google Cloud console project.

Set up a project

Click to:

     * Create or select a project.
     * Enable the Pub/Sub API for that project, if it is not already enabled. 

You can view and manage these resources at any time in the [Google Cloud console](https://console.cloud.google.com/).

  7. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  8. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

**Note:** You can run the gcloud CLI in the Google Cloud console without installing the Google Cloud CLI. To run the gcloud CLI in the Google Cloud console, [use Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 




### Required roles

To complete this quickstart, you need the following Identity and Access Management (IAM) roles.

To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles on your project: 

  * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)
  * [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Using the `gcloud` Command-Line Interface

The easiest way to use gcloud is in the [Cloud Shell ](https://docs.cloud.google.com/shell). You can also use the command line tool that comes with the [Google Cloud CLI](https://docs.cloud.google.com/sdk). Setup prerequisites are met automatically for the gcloud CLI if you create a brand new [Compute Engine machine instance](https://console.cloud.google.com/compute/instances) with access scopes including all Cloud APIs and the default Debian image. The simplest way to create it is via the Compute Engine UI. For the rest of this document, we will assume that you are using one of these command line tools.

For more information about using gcloud, see the [gcloud quickstart](https://docs.cloud.google.com/pubsub/docs/create-topic-gcloud). Also see the [gcloud pubsub section](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub) in the [gcloud reference](https://docs.cloud.google.com/sdk/gcloud/reference) for a complete list of Pub/Sub `gcloud` commands.

### Create and Seek to Snapshots

Create a topic and a subscription. For better interactivity, use a short acknowledgment deadline:
    
    
    gcloud pubsub topics create seek-demo-topic
    gcloud pubsub subscriptions create seek-demo-sub --topic=seek-demo-topic --ack-deadline=10

So far, no messages in the subscription have been acknowledged. Capture this state by creating a snapshot:
    
    
    gcloud pubsub snapshots create my-snapshot --subscription=seek-demo-sub
    gcloud pubsub snapshots list

Now publish, pull, and acknowledge a message:
    
    
    gcloud pubsub topics publish seek-demo-topic --message 'hello, world'
    gcloud pubsub subscriptions pull --auto-ack seek-demo-sub

Note that subsequent pulls yield no new messages (some transient duplicates are possible):
    
    
    gcloud pubsub subscriptions pull --auto-ack seek-demo-sub

You can recover the message by seeking the subscription to the snapshot. Note that the message may not be delivered instantly: Pub/Sub does not guarantee message delivery latency. However, what is guaranteed is that the messages retained in the snapshot will be delivered at least once:
    
    
    gcloud pubsub subscriptions seek seek-demo-sub --snapshot=my-snapshot
    gcloud pubsub subscriptions pull seek-demo-sub --auto-ack

Note that you can seek other subscriptions to the same snapshot, as long as the subscription's topic is the same as the snapshot's topic:
    
    
    gcloud pubsub subscriptions create seek-demo-sub2 --topic=seek-demo-topic --ack-deadline=10
    gcloud pubsub subscriptions seek seek-demo-sub2 --snapshot=my-snapshot

Pulling from `seek-demo-sub2` will now yield messages which were published before `seek-demo-sub2` was created:
    
    
    gcloud pubsub subscriptions pull seek-demo-sub2 --auto-ack

When you are done with the snapshot, clean up:
    
    
    gcloud pubsub snapshots delete my-snapshot

### Seek to a timestamp

Another way to replay messages that have been acknowledged is to seek to a timestamp. To seek to a timestamp, you must first configure the subscription to retain acknowledged messages using `retain-acked-messages`. If `retain-acked-messages` is set, Pub/Sub retains acknowledged messages for 7 days.

You only need to do this step if you intend to seek to a timestamp, not to a snapshot.
    
    
    gcloud pubsub subscriptions update seek-demo-sub --retain-acked-messages

Now publish, pull, and acknowledge a message:
    
    
    gcloud pubsub topics publish seek-demo-topic --message 'hello, world'
    gcloud pubsub subscriptions pull --auto-ack seek-demo-sub

The next pull should return no messages:
    
    
    gcloud pubsub subscriptions pull seek-demo-sub

Now seek the subscription back in time to recover the message. Note that the date arithmetic flags differ between the GNU and BSD (MacOS) versions of the date command:
    
    
    export TS_FORMAT=%Y-%m-%dT%H:%M:%SZ
    gcloud pubsub subscriptions seek seek-demo-sub --time=$(date -u -d '-10 min' +$TS_FORMAT)

For more information about supported time formats, see [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes).

A subsequent pull should yield the message again:
    
    
    gcloud pubsub subscriptions pull --auto-ack seek-demo-sub

You can also use seek to skip delivery of all messages published before some point in time, such as the current time. To do this, seek the subscription to the current time to mark as acknowledged all past messages:
    
    
    gcloud pubsub topics publish seek-demo-topic --message 'hello, world'
    gcloud pubsub subscriptions seek seek-demo-sub --time=$(date -u +$TS_FORMAT)

After some propagation delay (~60 seconds), the message will no longer be delivered. You can check this by repeatedly executing the pull command without acknowledging the message:
    
    
    gcloud pubsub subscriptions pull seek-demo-sub

## Using the Cloud console

You can create snapshots, or seek to existing snapshots, in the subscription detail page of the [Cloud console](https://console.cloud.google.com/cloudpubsub/subscriptions/). For snapshot naming rules, see [Resource names](https://docs.cloud.google.com/pubsub/docs/pubsub-basics#resource_names).

### Creating a snapshot

  1. In the Google Cloud console, go to the **Pub/Sub subscriptions** page.

[Go to the subscriptions page](https://console.cloud.google.com/cloudpubsub/subscription)

  2. Select a subscription from the list.

  3. Click **Create snapshot**.

  4. Enter an ID for the snapshot, then click **Create** to save.




Snapshots can be viewed on the [snapshots page](https://console.cloud.google.com/cloudpubsub/snapshot) in the Google Cloud console. You can also manage snapshots in the [details page of an individual topic](https://console.cloud.google.com/cloudpubsub/topicList).

### Replaying a subscription

The **Replay messages** dialog lets you seek to a previous time point or a saved snapshot. To open the dialog:

  1. In the Google Cloud console, go to the **Pub/Sub subscriptions** page.

[Go to the subscriptions page](https://console.cloud.google.com/cloudpubsub/subscription)

  2. Select a subscription from the list.

  3. Click **Replay messages**.

  4. Under **Seek** , select either **To a previous time point** or **To a snapshot** , then select the time point or snapshot to seek to.

  5. Click **Seek** to replay messages.


**Note:** To seek to a previous time point, your subscription must be configured to retain acknowledged messages. You can change this setting by clicking **Edit** on the subscription details page, and checking the box for **Retain acknowledged messages**.

## How did it go?

It worked!  **Great!** What did you like about the quickstart? What could we have done better?  Let us know!.  I got stuck.  **We're sorry to hear that.** Let us know what went wrong. We'll want to fix it. 

Note that additional resources and links are available on the [Pub/Sub support page](https://docs.cloud.google.com/pubsub/docs/support).

## What's next

See [Replaying and discarding messages](https://docs.cloud.google.com/pubsub/docs/replay-overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
