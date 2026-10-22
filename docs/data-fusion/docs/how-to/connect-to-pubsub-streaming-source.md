---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/connect-to-pubsub-streaming-source/
title: Read from a Pub/Sub streaming source \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:15.419942+00:00
---

# Read from a Pub/Sub streaming source  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/connect-to-pubsub-streaming-source/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Read from a Pub/Sub streaming source Stay organized with collections  Save and categorize content based on your preferences. 

Pub/Sub sources in Cloud Data Fusion let you ingest real-time message streams into your streaming data pipelines. You can then transform, enrich, and write event data to downstream storage and analytics destinations with minimal latency.

## Before you begin

  * [Create a Cloud Data Fusion instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-instance).



### Required roles

To get the permissions that you need to read from a Pub/Sub streaming source, ask your administrator to grant you the [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`) IAM role on the service account used to access the Pub/Sub subscription. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to read from a Pub/Sub streaming source. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to read from a Pub/Sub streaming source:

  * `pubsub.snapshots.create`
  * `pubsub.snapshots.delete`
  * `pubsub.snapshots.seek`
  * `pubsub.subscriptions.consume`
  * `pubsub.topics.attachSubscription`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

You grant the role on the service account you specified in the plugin properties for accessing Pub/Sub. If none is specified, grant the role on the Managed Service for Apache Spark service account.

**Note:** In versions 6.9.1 and later, the predefined Pub/Sub Subscriber role isn't enough, as `pubsub.snapshots.create` and `pubsub.snapshots.delete` permission are required.

For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Add a Pub/Sub source to your streaming data pipeline

  1. Go to your instance: 

     1. In the Google Cloud console, go to the Cloud Data Fusion page.

     2. To open the instance in the Cloud Data Fusion Studio, click **Instances** , and then click **View instance**.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. In the Cloud Data Fusion web interface, click **Studio**.

  3. Select **Data Pipeline - Realtime**.

  4. In the **Source** menu, select **Pub/Sub**. A Pub/Sub streaming source node appears in the pipeline.

  5. On the Pub/Sub node, click **Properties** to configure the source. For more information, see [Pub/Sub Streaming Source](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/464912525/Google+Cloud+Pub+Sub+Streaming+Source).


**Note:** Cloud Data Fusion supports Pub/Sub pull subscriptions.

## Support for a single Pub/Sub source with no Windower plugins

Cloud Data Fusion version 6.9.1 supports real time pipelines with a single Pub/Sub streaming source and no Windower plugins.

  * The Pub/Sub streaming source has built-in support and data is processed at least once. Enabling Spark checkpointing isn't required.
  * The Pub/Sub streaming source creates a [Pub/Sub snapshot](https://docs.cloud.google.com/pubsub/docs/replay-overview#seek_to_a_snapshot) at the beginning of each batch and removes it at the end of each batch.
  * Creating Pub/Sub snapshots has a cost associated with it. For more information, see [Pub/Sub pricing](https://cloud.google.com/pubsub/pricing#storage_costs).
  * You can monitor snapshot creation in [Cloud Audit Logs](https://docs.cloud.google.com/pubsub/docs/audit-logging).



## Upgrade a pipeline with a Pub/Sub streaming source

Cloud Data Fusion supports [direct application upgrades](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477560983/Lifecycle+Microservices#Upgrade-an-Application) for streaming pipelines with a Pub/Sub streaming source created in 6.9.1 or later.

Cloud Data Fusion doesn't support upgrades for data pipelines with a Pub/Sub streaming source in version 6.9.0 or earlier. Instead, upgrade those pipelines to 6.9.1:

  1. Stop publishing the data to the topic when the instance upgrade is planned.
  2. Wait for the pipeline to finish processing the published data.
  3. After the data is processed completely, stop the pipeline.
  4. [Upgrade the instance](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrading).
  5. Duplicate the existing pipeline and update to the newest plugins.
  6. Deploy the pipeline.
  7. Run the new pipeline to read data.

The new version automatically uses snapshot instead of Spark checkpointing.

  8. Delete the old pipeline.




## What's next

  * Refer to the CDAP [Pub/Sub Streaming Source](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/464912525/Google+Cloud+Pub+Sub+Streaming+Source).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
