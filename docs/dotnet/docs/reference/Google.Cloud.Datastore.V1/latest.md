---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/
title: Google.Cloud.Datastore.V1 \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:57:47.410394+00:00
---

# Google.Cloud.Datastore.V1  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google.Cloud.Datastore.V1 Stay organized with collections  Save and categorize content based on your preferences. 

5.2.0 (latest)  5.1.0  5.0.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.5.0  3.4.0  3.3.0  3.2.0 

`Google.Cloud.Datastore.V1` is a.NET client library for the [Google Cloud Datastore API](https://cloud.google.com/datastore/docs/concepts/overview).

Note: This documentation is for version `5.2.0` of the library. Some samples may not work with other versions.

## Installation

Install the `Google.Cloud.Datastore.V1` package from NuGet. Add it to your project in the normal way (for example by right-clicking on the project in Visual Studio and choosing "Manage NuGet Packages...").

## Authentication

When running on Google Cloud, no action needs to be taken to authenticate.

Otherwise, the simplest way of authenticating your API calls is to set up Application Default Credentials. The credentials will automatically be used to authenticate. See [Set up Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc) for more details.

## Getting started

See the [Datastore Quickstart](https://cloud.google.com/datastore/docs/quickstart) for an introduction with runnable code samples.

The [DatastoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.DatastoreDb) class is provided as a wrapper for [DatastoreClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.DatastoreClient), simplifying operations considerably by assuming all operations act on the same partition, and providing page streaming operations on structured query results.

Several custom conversions, additional constructors, factory methods (particularly on [Filter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Filter) are provided to simplify working with the protobuf messages.

## Support for emulator detection

As of 2.2.0-beta02 and 2.2.0, the library has support for detecting the emulator via environment variables, if requested. This is configured via `DatastoreDbBuilder`, which can also be used to configure custom credentials easily.

The following code creates a `DatastoreDb` which will use the emulator when the environment variables are present, but will otherwise connect to the production environment.
    
    
    DatastoreDb db = new DatastoreDbBuilder
    {
        ProjectId = projectId,
        EmulatorDetection = EmulatorDetection.EmulatorOrProduction
    }.Build();
    // Use db as normal
    

See the [EmulatorDetection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.EmulatorDetection.yml) enum for details of the other possible values.

## Sample code

## Inserting data
    
    
    DatastoreDb db = DatastoreDb.Create(projectId, namespaceId);
    
    KeyFactory keyFactory = db.CreateKeyFactory("message");
    Entity entity = new Entity
    {
        Key = keyFactory.CreateIncompleteKey(),
        ["created"] = DateTime.UtcNow,
        ["text"] = "Text of the message",
        ["tags"] = new[] { "tag1", "tag2" }
    };
    using (DatastoreTransaction transaction = db.BeginTransaction())
    {
        transaction.Insert(entity);
        CommitResponse commitResponse = transaction.Commit();
        Key insertedKey = commitResponse.MutationResults[0].Key;
        Console.WriteLine($"Inserted key: {insertedKey}");
        // The key is also propagated to the entity
        Console.WriteLine($"Entity key: {entity.Key}");
    }
    

## Querying data
    
    
    DatastoreDb db = DatastoreDb.Create(projectId, namespaceId);
    
    // Print the messages created in the last 5 minutes, most recent first
    DateTime cutoff = DateTime.UtcNow.AddMinutes(-5);
    Query query = new Query("message")
    {
        Filter = Filter.GreaterThanOrEqual("created", cutoff),
        Order = { { "created", Direction.Descending } }
    };
    foreach (Entity entity in db.RunQueryLazily(query))
    {
        DateTime created = (DateTime)entity["created"];
        string text = (string)entity["text"];
        Console.WriteLine($"{created:yyyy-MM-dd'T'HH:mm:ss}: {text}");
    }
    

When a query contains a projection, any timestamp fields will be returned using integer values. Use the `Value.ToDateTimeFromProjection` and `Value.ToDateTimeOffsetFromProjection` methods to convert either integer or timestamp values to `DateTime` or `DateTimeOffset`.

Lots more samples: [github.com/googleapis/dotnet-docs-samples](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/tree/master/datastore/api)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
