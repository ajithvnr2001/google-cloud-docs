---
url: https://docs.cloud.google.com/bigtable/docs/change-streams-read-java/
title: Read a change stream with Java \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:39.533553+00:00
---

# Read a change stream with Java  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/change-streams-read-java/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Read a change stream with Java

The [Cloud Bigtable client library for Java](https://github.com/googleapis/google-cloud-java/tree/main/java-bigtable) provides low-level methods for processing data change records. However, in most cases, we recommend that you [stream changes with Dataflow](https://docs.cloud.google.com/bigtable/docs/change-streams-use-dataflow) instead of using the methods described on this page, because Dataflow handles [partition](https://docs.cloud.google.com/bigtable/docs/change-streams-overview#understand-partitions) splits and merges for you.

## Before you begin

Before you read a change stream with Java, make sure you are familiar with the [Change streams overview](https://docs.cloud.google.com/bigtable/docs/change-streams-overview). Then complete the following prerequisites.

### Set up authentication

To use the Java samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/bigtable/docs/authentication#local-development). 

For information about setting up authentication for a production environment, see [ Set up Application Default Credentials for code running on Google Cloud ](https://docs.cloud.google.com/bigtable/docs/authentication#on-gcp). 

### Enable a change stream

You must [enable a change stream](https://docs.cloud.google.com/bigtable/docs/change-streams-configure) on a table before you can read it. You can also [create a new table](https://docs.cloud.google.com/bigtable/docs/managing-tables#create-table) with a change stream enabled.

### Required roles

To get the permissions that you need to read a Bigtable change stream, ask your administrator to grant you the following IAM role.

  * Bigtable Administrator ([`roles/bigtable.admin`](https://docs.cloud.google.com/bigtable/docs/access-control#bigtable.admin)) on the Bigtable instance that contains the table you plan to stream changes from



## Add the Java client library as a dependency

Add code similar to the following to your Maven `pom.xml` file. Replace `VERSION` with the version of the client library that you are using. The version must be 2.21.0 or later.
    
    
    <dependencies>
      <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-bigtable</artifactId>
        <version>VERSION</version>
      </dependency>
    </dependencies>
    

## Determine the table's partitions

To start making `ReadChangeStream` requests, you need to know the partitions of your table. This can be determined using the `GenerateInitialChangeStreamPartitions` method. The following example shows how to use this method to get a stream of [`ByteStringRanges`](https://javadoc.io/doc/com.google.cloud/google-cloud-bigtable/latest/index.html) representing each partition in the table. Each `ByteStringRange` contains the start and end key for a partition.
    
    
    ServerStream<ByteStringRange> partitionStream =
        client.generateInitialChangeStreamPartitions("MyTable");
    

## Process changes for each partition

You can then process changes for each partition using the `ReadChangeStream` method. This is an example of how to open a stream for a partition, starting from the current time.
    
    
    ReadChangeStreamQuery query =
        ReadChangeStreamQuery.create("MyTable")
            .streamPartition(partition)
            .startTime(Instant.now());
    ServerStream<ChangeStreamRecord> changeStream = client.readChangeStream(query);
    

`ReadChangeStreamQuery` accepts the following arguments:

  * Stream partition (Required) - the partition to stream changes from
  * One of the following: 
    * Start time - Commit timestamp to start processing changes from
    * Continuation tokens - Tokens representing a position to resume streaming from
  * End Time (Optional) - Commit timestamp to stop processing changes when reached. If you don't provide a value, the stream continues reading.
  * Heartbeat duration (Optional) - Frequency of heartbeat messages when there are no new changes (defaults to five seconds)



## Change stream record format

A returned change stream record is one of three response types:

  * `ChangeStreamMutation` \- A message representing a data change record.

  * `CloseStream` \- A message indicating that the client should stop reading from the stream.

    * Status - Indicates the reason for closing the stream. One of: 
      * `OK` \- end time has been reached for the given partition
      * `OUT_OF_RANGE` \- the given partition no longer exists, meaning splits or merges have happened on this partition. A new `ReadChangeStream` request will need to be created for each new partition.
    * `NewPartitions` \- Gives the updated partitioning information on `OUT_OF_RANGE` responses.
    * `ChangeStreamContinuationTokens` \- List of tokens used to resume new `ReadChangeStream` requests from the same position. One per `NewPartition`.
  * `Heartbeat` \- A periodic message with information that can be used to checkpoint the state of the stream.

    * `EstimatedLowWatermark` \- Estimation of the low watermark for the given partition
    * `ContinuationToken` \- Token to resume streaming the given partition from the current position.



### Data change record contents

For information about change stream records, see [What's in a data change record](https://docs.cloud.google.com/bigtable/docs/change-streams-overview#data-change-record).

## Handle changes in partitions

When the partitions of a table changes, `ReadChangeStream` requests return a `CloseStream` message with the information required to resume streaming from the new partition(s).

For a _split_ , this will contain multiple new partitions and a corresponding `ContinuationToken` for each partition. To resume streaming the new partitions from the same position, you make a new `ReadChangeStream` request for each new partition with its corresponding token.

For example, if you are streaming partition `[A,C)` and it splits into two partitions, `[A,B)` and `[B,C)`, you can expect the following sequence of events:
    
    
    ReadChangeStream(streamPartition = ByteStringRange(A, C)) receives:
    CloseStream(
        Status = OUT_OF_RANGE,
        NewPartitions = List(ByteStringRange(A, B), ByteStringRange(B, C))
        ChangeStreamContinuationTokens = List(foo, bar)
    )
    

To resume streaming each partition from the same position you send the following `ReadChangeStreamQuery` requests:
    
    
    ReadChangeStreamQuery queryAB =
        ReadChangeStreamQuery.create("myTable")
            .streamPartition(ByteStringRange(A, B))
            .continuationTokens(List.of(foo));
    
    ReadChangeStreamQuery queryBC =
        ReadChangeStreamQuery.create("myTable")
            .streamPartition(ByteStringRange(B, C))
            .continuationTokens(List.of(bar));
    

For a merge, to resume from the same partition, you need to send a new `ReadChangeStream` request containing each token from the merged partitions.

For example, if you are streaming two partitions, `[A,B)` and `[B,C)`, and they merge into partition `[A,C)`, you can expect the following sequence of events:
    
    
    ReadChangeStream(streamPartition = ByteStringRange(A, B)) receives:
    CloseStream(
        Status = OUT_OF_RANGE,
        NewPartitions = List(ByteStringRange(A, C)),
        ChangeStreamContinuationTokens = List(foo)
    )
    
    ReadChangeStream(streamPartition = ByteStringRange(B, C)) receives:
    CloseStream(
        Status = OUT_OF_RANGE,
        NewPartitions = List(ByteStringRange(A, C)),
        ChangeStreamContinuationTokens = List(bar)
    )
    

To resume streaming partition `[A, C)` from the same position, you send a `ReadChangeStreamQuery` like the following:
    
    
    ReadChangeStreamQuery query =
        ReadChangeStreamQuery.create("myTable")
            .streamPartition(ByteStringRange(A, C))
            .continuationTokens(List.of(foo, bar));
    

## What's next

  * [Configure change streams.](https://docs.cloud.google.com/bigtable/docs/change-streams-configure)
  * [Stream changes with Dataflow.](https://docs.cloud.google.com/bigtable/docs/change-streams-use-dataflow)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
