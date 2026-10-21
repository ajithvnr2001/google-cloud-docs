---
url: https://docs.cloud.google.com/spanner/docs/samples/spanner-dataflow-write/
title: Dataflow write with mutations \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:26.850406+00:00
---

# Dataflow write with mutations  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/samples/spanner-dataflow-write/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Samples ](https://docs.cloud.google.com/spanner/docs/samples)



#  Dataflow write with mutations Stay organized with collections  Save and categorize content based on your preferences. 

Use the Dataflow connector to write data by using mutations.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Import, export, and modify data using Dataflow](https://docs.cloud.google.com/spanner/docs/dataflow-connector)



## Code sample

### Java

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    albums
        // Spanner expects a Mutation object, so create it using the Album's data
        .apply("CreateAlbumMutation", ParDo.of(new DoFn<Album, Mutation>() {
          @ProcessElement
          public void processElement(ProcessContext c) {
            Album album = c.element();
            c.output(Mutation.newInsertOrUpdateBuilder("albums")
                .set("singerId").to(album.singerId)
                .set("albumId").to(album.albumId)
                .set("albumTitle").to(album.albumTitle)
                .build());
          }
        }))
        // Write mutations to Spanner
        .apply("WriteAlbums", SpannerIO.write()
            .withInstanceId(instanceId)
            .withDatabaseId(databaseId));

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudspanner). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
