---
url: https://docs.cloud.google.com/spanner/docs/samples/spanner-dataflow-readall/
title: Dataflow read all \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:50:03.740855+00:00
---

# Dataflow read all  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/samples/spanner-dataflow-readall/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Samples ](https://docs.cloud.google.com/spanner/docs/samples)



#  Dataflow read all Stay organized with collections  Save and categorize content based on your preferences. 

Use SQL queries with the Dataflow connector to read data from all available tables in a database.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Import, export, and modify data using Dataflow](https://docs.cloud.google.com/spanner/docs/dataflow-connector)



## Code sample

### Java

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    PCollection<Struct> allRecords =
        pipeline
            .apply(
                SpannerIO.read()
                    .withSpannerConfig(spannerConfig)
                    .withBatching(false)
                    .withQuery(
                        "SELECT t.table_name FROM information_schema.tables AS t WHERE t"
                            + ".table_catalog = '' AND t.table_schema = ''"))
            .apply(
                MapElements.into(TypeDescriptor.of(ReadOperation.class))
                    .via(
                        (SerializableFunction<Struct, ReadOperation>)
                            input -> {
                              String tableName = input.getString(0);
                              return ReadOperation.create().withQuery("SELECT * FROM " + tableName);
                            }))
            .apply(SpannerIO.readAll().withSpannerConfig(spannerConfig));

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudspanner). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
