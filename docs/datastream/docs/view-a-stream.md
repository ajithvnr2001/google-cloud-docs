---
url: https://docs.cloud.google.com/datastream/docs/view-a-stream/
title: View a stream \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:29:15.406520+00:00
---

# View a stream  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/view-a-stream/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  View a stream Stay organized with collections  Save and categorize content based on your preferences. 

In this page, you learn how to get information about your streams.

To view high-level and detailed information about a stream, do the following:

  1. Go to the **Streams** page in the Google Cloud Console.

[Go to the Streams page](https://console.cloud.google.com/datastream/streams)

  2. Click the stream for which you want to see detailed information. This information appears on the **Stream details** page.




## View high-level information

High-level information about a stream includes:

  * The name and status of the stream.
  * The source and destination connection profiles that the stream uses to transfer data from a source database into a destination.
  * The profile types of the connection profiles.



## View detailed information

In addition to viewing high-level information about a stream, you can click a stream to see additional information, including:

  * The region where the stream is stored. Streams, like all resources, are saved in a region. Streams can only use connection profiles and private connectivity configurations that are in the same region.
  * When the stream was created, last updated, or recovered.
  * Any labels added to the stream. These labels are used to organize the stream.
  * Depending on the source database, the CDC method that you selected for the stream.
  * The tables and schemas in the source database which Datastream should include when processing the stream.
  * The tables and schemas in the source database that Datastream should exclude when processing the stream.
  * For all sources apart from PostgreSQL, the CDC method set for the stream.
  * For Oracle sources: the log file access method.
  * Whether [historical backfill](https://docs.cloud.google.com/datastream/docs/create-a-stream#backfillhistoricaldata) is enabled or disabled for the stream. 
    * If it's enabled, how many schemas and tables in the source database are excluded from backfilling.
  * For BigQuery destinations:

    * Whether the destination dataset is a dynamic or default dataset.
    * Whether the write mode for the stream is set to **Merge** or **Append-only**.
    * If you selected **Merge mode** , the staleness limit configuration applied to the new BigQuery tables created by Datastream.

Additionally, for Apache Iceberg tables destinations:

    * The identifier of the BigQuery connection that you use for your stream.
    * The uniform resource identifier (URI) of the Cloud Storage bucket where you store your data.
  * For Cloud Storage destinations:

    * The location of the destination into which the stream transfers schemas, tables, and data from a source database.
    * The format of files written to the destination. Datastream supports two output formats: Avro and JSON.
  * Whether your data is encrypted with a key that's managed by Google (Google-managed) or by you (Customer-managed).

  * A link and the path to the customer-managed encryption key (if you're managing the encryption).

  * A link to create an alerting policy for the stream.

  * A status of how many backfills are in progress, pending, or failed.

  * The number of events that are processed and loaded to the destination by Datastream in the last 7 days.

  * The number of events that Datastream couldn't process in the last 7 days.

    * The Data freshness graph. This graph displays the time gap between data residing in the source and the data being transferred into the destination by the stream. This is calculated as the time elapsed since Datastream last checked for new data in the source.

For more information about this graph, see [Monitor a stream](https://docs.cloud.google.com/datastream/docs/monitor-a-stream).




## What's next

  * To learn more about streams, see [Stream lifecycle](https://docs.cloud.google.com/datastream/docs/stream-states-and-actions).
  * To learn how to modify your streams, see [Modify a stream](https://docs.cloud.google.com/datastream/docs/modify-a-stream).
  * To learn how to monitor a stream, see [Monitor a stream](https://docs.cloud.google.com/datastream/docs/monitor-a-stream).
  * To learn how to delete an existing stream, see [Delete a stream](https://docs.cloud.google.com/datastream/docs/delete-a-stream).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
