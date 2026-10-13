---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/
title: Google.Cloud.Firestore \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:28.221809+00:00
---

# Google.Cloud.Firestore  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google.Cloud.Firestore Stay organized with collections  Save and categorize content based on your preferences. 

4.5.0 (latest)  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.1  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.5.0  2.4.0  2.3.1 

`Google.Cloud.Firestore` is a.NET client library for the [Firestore API](https://firebase.google.com/docs/firestore/).

Note: This documentation is for version `4.5.0` of the library. Some samples may not work with other versions.

## Installation

Install the `Google.Cloud.Firestore` package from NuGet. Add it to your project in the normal way (for example by right-clicking on the project in Visual Studio and choosing "Manage NuGet Packages...").

## Authentication

When running on Google Cloud, no action needs to be taken to authenticate.

Otherwise, the simplest way of authenticating your API calls is to set up Application Default Credentials. The credentials will automatically be used to authenticate. See [Set up Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc) for more details.

## Getting started

Everything starts with [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb). Create an instance using the `Create` or `CreateAsync` methods, passing in your Google Cloud project ID. The default credentials will be used to authenticate with the server. `FirestoreDb` is thread-safe, and we recommend using a single instance across your application where possible.

From there, you can create, fetch and modify documents, and run queries.

For customization of credentials and other settings, create a `FirestoreDbBuilder`, set the appropriate properties, and call `Build` to create a `FirestoreDb`.

## Sample code
    
    
    FirestoreDb db = new FirestoreDbBuilder { ProjectId = projectId, DatabaseId = databaseId }.Build();
    
    // Create a document with a random ID in the "users" collection.
    CollectionReference collection = db.Collection("users");
    DocumentReference document = await collection.AddAsync(new { Name = new { First = "Ada", Last = "Lovelace" }, Born = 1815 });
    
    // A DocumentReference doesn't contain the data - it's just a path.
    // Let's fetch the current document.
    DocumentSnapshot snapshot = await document.GetSnapshotAsync();
    
    // We can access individual fields by dot-separated path
    Console.WriteLine(snapshot.GetValue<string>("Name.First"));
    Console.WriteLine(snapshot.GetValue<string>("Name.Last"));
    Console.WriteLine(snapshot.GetValue<int>("Born"));
    
    // Or deserialize the whole document into a dictionary
    Dictionary<string, object> data = snapshot.ToDictionary();
    Dictionary<string, object> name = (Dictionary<string, object>) data["Name"];
    Console.WriteLine(name["First"]);
    Console.WriteLine(name["Last"]);
    
    // See the "data model" guide for more options for data handling.
    
    // Query the collection for all documents where doc.Born < 1900.
    Query query = collection.WhereLessThan("Born", 1900);
    QuerySnapshot querySnapshot = await query.GetSnapshotAsync();
    foreach (DocumentSnapshot queryResult in querySnapshot.Documents)
    {
        string firstName = queryResult.GetValue<string>("Name.First");
        string lastName = queryResult.GetValue<string>("Name.Last");
        int born = queryResult.GetValue<int>("Born");
        Console.WriteLine($"{firstName} {lastName}; born {born}");
    }
    

See the [user guide](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/userguide) for more samples.

## Connecting to the emulator

To connect to the [Firestore Emulator](https://cloud.google.com/sdk/gcloud/reference/beta/emulators/firestore/), you need to:

  * Connect to the emulator endpoint
  * Use `ChannelCredentials.Insecure` as the channel credentials
  * Specify an "Authorization: Bearer owner" header on each request



As of version 1.1.0-beta02, the library has support for detecting the emulator via the environment variable and connecting to it automatically, if requested. This is configured via `FirestoreDbBuilder`, which can also be used to configure custom credentials easily.

The following code creates a `FirestoreDb` which will use the emulator when the environment variables are present, but will otherwise connect to the production environment.
    
    
    FirestoreDb db = new FirestoreDbBuilder
    {
        ProjectId = projectId,
        EmulatorDetection = EmulatorDetection.EmulatorOrProduction
    }.Build();
    // Use db as normal
    

See the [EmulatorDetection property](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDbBuilder#Google_Cloud_Firestore_FirestoreDbBuilder_EmulatorDetection) for more details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
