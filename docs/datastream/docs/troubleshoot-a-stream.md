---
url: https://docs.cloud.google.com/datastream/docs/troubleshoot-a-stream/
title: Troubleshoot a stream \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:58.126837+00:00
---

# Troubleshoot a stream  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/troubleshoot-a-stream/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Troubleshoot a stream Stay organized with collections  Save and categorize content based on your preferences. 

If a problem occurs while a stream is transferring data from a source database into a destination, the stream can enter a `Failed` or `Failed permanently` state. In both cases, you can rectify the problem.

## Troubleshoot a stream

  1. Go to the **Streams** page in the Google Cloud Console.

[Go to the Streams page](https://console.cloud.google.com/datastream/streams)

  2. Click the **Column display options** icon in the upper-right corner of the page. The icon appears as three vertical columns.

  3. If it isn't selected, select the **Status** checkbox, and then click **OK**. Datastream displays the following statuses:

     * `Failed`: for an error that occurs on a `Running` stream. Such errors imply that the stream is still active or continuously attempting to run.
     * `Failed permanently`: for a stream that can't continue to run. Such errors might cause data loss.
  4. Click the stream that you want to troubleshoot. Any errors associated with the stream appear on the **Stream details** page.

For example, if Datastream can't connect to the source database, then the **We can't use the credentials that you provided to connect to the data source.** error message appears on this page.

  5. Address the errors. You can resolve errors for either the stream or the connection profile.

For example, if errors are associated with either the source data objects of the stream or its destination configuration information, then [modify the stream](https://docs.cloud.google.com/datastream/docs/modify-a-stream#modifyastream).

If errors are associated with the connectivity information of the stream, then update the configuration information about the [source database](https://docs.cloud.google.com/datastream/docs/modify-a-stream#modifystreamsourceinfo) or the [destination](https://docs.cloud.google.com/datastream/docs/modify-a-stream#modifystreamdestinfo) for any connection profiles being used by the stream. Any changes that you make to a single connection profile affect all streams using that connection profile. 

  6. Fix the `Failed` stream so that it can automatically resume, or [recover](https://docs.cloud.google.com/datastream/docs/recover-a-stream) the `Failed permanently` stream.




### Recover a stream

The first thing to try when recovering a stream is to recover it from the current position. For more information about stream recovery options, see [Stream recovery overview](https://docs.cloud.google.com/datastream/docs/recover-a-stream#recovery-overview).

If recovering a stream from the current position fails, then try the following:

  1. Drop or truncate the affected tables in the destination. You need to do this because while the stream was down, Datastream might have missed some `DELETE` events. `DELETE` events can't be recovered if you don't truncate the table before performing the backfill.
  2. Recover the stream from the most recent position. For PostgreSQL, recreate the replication slot or create a new replication slot.
  3. Once the stream is running, trigger backfills to restore all historical data. For information about how to trigger a backfill, see [Initiate backfill](https://docs.cloud.google.com/datastream/docs/manage-backfill-for-the-objects-of-a-stream#initiatebackfill).



## What's next

  * To learn more about streams, see [Stream lifecycle](https://docs.cloud.google.com/datastream/docs/stream-states-and-actions).
  * To learn how to modify a stream, see [Modify a stream](https://docs.cloud.google.com/datastream/docs/modify-a-stream).
  * To learn how to recover a failed stream, see [Recover a stream](https://docs.cloud.google.com/datastream/docs/recover-a-stream).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
