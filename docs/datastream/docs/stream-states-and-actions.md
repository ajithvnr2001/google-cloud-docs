---
url: https://docs.cloud.google.com/datastream/docs/stream-states-and-actions/
title: Stream lifecycle \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:03:45.423753+00:00
---

# Stream lifecycle  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/stream-states-and-actions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Stream lifecycle Stay organized with collections  Save and categorize content based on your preferences. 

The following diagram shows the various states and transitions in the lifecycle of a stream.

![Datastream user flow diagram](https://docs.cloud.google.com/static/datastream/docs/images/stream-states-and-actions-final_02.png)

In this diagram, the upside-down trapezoid boxes represent actions that the user performs with the stream, and the rectangle boxes represent the resultant states of the stream based on the user's actions. 

First, you [create a stream](https://docs.cloud.google.com/datastream/docs/create-a-stream). Datastream uses this stream to transfer data from a source database into a destination. After the stream is created, the state of the stream is `Not started`.

After creating the stream, you [start it](https://docs.cloud.google.com/datastream/docs/run-a-stream#startastream). The status of the stream changes to `Starting`. This signifies that the stream is in the process of being started and validated.

  * If the stream is valid, then the status of the stream changes from `Starting` to `Running`.
  * If the stream isn't valid, then the status of the stream changes from `Starting` back to `Not started`. You can then [rectify the problems of the stream](https://docs.cloud.google.com/datastream/docs/troubleshoot-a-stream). For example, if errors are associated with the connectivity information of the stream, then modify the stream definition. After resolving all problems of the stream, start it again, and the status changes to `Starting`, and then to `Running`.



You can [pause a stream](https://docs.cloud.google.com/datastream/docs/run-a-stream#pauseastream). When a stream is paused, Datastream doesn't pull any new data from the source database into the destination. However, some data may continue to be written to the destination because _in flight_ data continues to flow.

Therefore, after you pause a stream, the status of the stream changes from `Running` to `Draining`. Draining a stream is the process of emptying the stream so that it doesn't contain any data. After the stream is drained of all data, then the status of the stream changes from `Draining` to `Paused`.

When you [resume a paused stream](https://docs.cloud.google.com/datastream/docs/run-a-stream#resumeastream), the status of the stream changes from `Paused` to `Running`.

There are two actions that you can perform at any time during the lifecycle of the stream:

  * [Modify the stream](https://docs.cloud.google.com/datastream/docs/modify-a-stream). Any changes that you make to it take effect immediately.
  * [Delete the stream](https://docs.cloud.google.com/datastream/docs/delete-a-stream) after you no longer need it.



## Stream errors

A running stream can encounter errors which might cause the stream to change its state to `Failed` or `Failed permanently`:

  * A `Failed` status means that the stream encountered a recoverable error. This means that the stream is either still active, or continuously attempting to run.
  * A `Failed permanently` stream is a stream that ran into an unrecoverable error which prevents it from continuing to run. Such errors might cause data loss.



You can address the issues for a `Failed` stream, and the stream automatically resumes. Its state changes from `Failed` back to `Running`. For more information, see [Troubleshoot a stream](https://docs.cloud.google.com/datastream/docs/troubleshoot-a-stream).

You can manually recover a `Failed permanently` stream. For more information, see [Recover a stream](https://docs.cloud.google.com/datastream/docs/troubleshoot-a-stream).

## What's next

  * For information about running a stream, see [Run a stream](https://docs.cloud.google.com/datastream/docs/run-a-stream).
  * For information about modifying your streams, see [Modify a stream](https://docs.cloud.google.com/datastream/docs/modify-a-stream).
  * For information about troubleshooting a stream, see [Troubleshoot a stream](https://docs.cloud.google.com/datastream/docs/troubleshoot-a-stream).
  * For information about recovering a stream, see [Recover a stream](https://docs.cloud.google.com/datastream/docs/recover-a-stream).
  * For information about deleting a stream, see [Delete a stream](https://docs.cloud.google.com/datastream/docs/delete-a-stream).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
