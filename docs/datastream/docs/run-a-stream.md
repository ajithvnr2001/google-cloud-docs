---
url: https://docs.cloud.google.com/datastream/docs/run-a-stream/
title: Run a stream \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:54.736367+00:00
---

# Run a stream  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/run-a-stream/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Run a stream Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the actions that you can take when you run a stream. The actions include:

  * Starting a stream
  * Pausing a stream
  * Resuming a stream



## Start the stream

When you [created a stream](https://docs.cloud.google.com/datastream/docs/create-a-stream#createthestream), you either created the stream and started it immediately, or created the stream without starting it.

If you created the stream, but you didn't start it, then you can do so now. By starting the stream, Datastream can transfer data, schemas, and tables from the source database to the destination.

  1. Go to the **Streams** page in the Google Cloud Console.

[Go to the Streams page](https://console.cloud.google.com/datastream/streams)

  2. Select the checkbox to the left of the stream that you want to start.

  3. Click **START**.

  4. In the dialog, click **START**. The status of the stream changes from `Not started` to `Starting` to `Running`.

It takes about 30 seconds for the stream to start running. Background resources need to start so that the stream can start.

For more information about the states and transitions of a stream, see [Stream lifecycle](https://docs.cloud.google.com/datastream/docs/stream-states-and-actions).




After starting a stream, you can [monitor it](https://docs.cloud.google.com/datastream/docs/monitor-a-stream) to verify that Datastream transferred data from the source database to the destination.

## Pause the stream

After starting a stream, you can pause it. When a stream is paused, Datastream doesn't pull any new data from the source database into the destination. However, some data may continue to be written to the destination as data "in flight" continues to flow.

In some cases, if you pause a stream, then the source database must retain the data until you resume the stream. The retention period for the source database may be limited. If the stream is paused for longer than the source retention period, and then the stream is resumed, this can cause the stream to fail. If this occurs, [delete the stream](https://docs.cloud.google.com/datastream/docs/delete-a-stream), [create a new one](https://docs.cloud.google.com/datastream/docs/create-a-stream), and then start it so that Datastream can transfer data, schemas, and tables from the source database to the destination.

  1. Go to the **Streams** page in the Google Cloud Console.

[Go to the Streams page](https://console.cloud.google.com/datastream/streams)

  2. Select the checkbox to the left of the stream that you want to pause.

  3. Click **PAUSE**.

  4. In the dialog, click **PAUSE**. The status of the stream changes from `Running` to `Draining`. Draining a stream is the process of emptying the stream so that it doesn't contain any data. 

After the stream is drained of all data, then the status of the stream changes from `Draining` to `Paused`.

For more information about the states and transitions of a stream, see [Stream lifecycle](https://docs.cloud.google.com/datastream/docs/stream-states-and-actions).




After pausing a stream, you can resume it so that Datastream can transfer new data from the source database to the destination.

## Resume the stream

You can resume a stream that you paused. By resuming the stream, Datastream can transfer new data from the source database to the destination.

  1. Go to the **Streams** page in the Google Cloud Console.

[Go to the Streams page](https://console.cloud.google.com/datastream/streams)

  2. Select the checkbox to the left of the stream that you want to resume.

  3. Click **RESUME**. The status of the stream changes from `Paused` to `Running`.

For more information about the states and transitions of a stream, see [Stream lifecycle](https://docs.cloud.google.com/datastream/docs/stream-states-and-actions).




After resuming a stream, you can [monitor it](https://docs.cloud.google.com/datastream/docs/monitor-a-stream) to verify that Datastream transferred new data from the source database to the destination.

## What's next

  * To learn more about streams, see [Stream lifecycle](https://docs.cloud.google.com/datastream/docs/stream-states-and-actions).
  * To learn how to modify your streams, see [Modify a stream](https://docs.cloud.google.com/datastream/docs/modify-a-stream).
  * To learn how to recover a stream, see [Recover a stream](https://docs.cloud.google.com/datastream/docs/recover-a-stream).
  * To learn how to delete an existing stream, see [Delete a stream](https://docs.cloud.google.com/datastream/docs/delete-a-stream).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
