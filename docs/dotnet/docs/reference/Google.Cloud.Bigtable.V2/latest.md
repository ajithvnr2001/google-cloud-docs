---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/
title: Google.Cloud.Bigtable.V2 \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:57:38.936832+00:00
---

# Google.Cloud.Bigtable.V2  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google.Cloud.Bigtable.V2 Stay organized with collections  Save and categorize content based on your preferences. 

3.33.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 

`Google.Cloud.Bigtable.V2` is a.NET client library for the [Google Bigtable API](https://cloud.google.com/bigtable/).

Note: This documentation is for version `3.33.0` of the library. Some samples may not work with other versions.

## Installation

Install the `Google.Cloud.Bigtable.V2` package from NuGet. Add it to your project in the normal way (for example by right-clicking on the project in Visual Studio and choosing "Manage NuGet Packages...").

## Authentication

When running on Google Cloud, no action needs to be taken to authenticate.

Otherwise, the simplest way of authenticating your API calls is to set up Application Default Credentials. The credentials will automatically be used to authenticate. See [Set up Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc) for more details.

## Getting started

Common operations are exposed via the [BigtableClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient) class.

## Sample code
    
    
    BigtableClient client = BigtableClient.Create();
    TableName tableName = new TableName(projectId, instanceId, tableId);
    
    // Insert a row with some cells into the table
    await client.MutateRowAsync(
        tableName,
        "user12345",
        Mutations.SetCell(
            familyName: "Score",
            columnQualifier: "Level 1",
            value: 456),
        Mutations.SetCell(
            familyName: "metrics",
            columnQualifier: "Level 1 - total time",
            value: 12000));
    
    // Read the row back from the table, but only the latest cell values
    // from the 'Score' column family
    Row row = await client.ReadRowAsync(
        tableName,
        "user12345",
        filter: RowFilters.Chain(
            RowFilters.FamilyNameExact("Score"),
            RowFilters.CellsPerColumnLimit(1)));
    
    foreach (Family family in row.Families)
    {
        string familyName = family.Name;
        Console.WriteLine($"Family: {familyName}");
    
        foreach (Column column in family.Columns)
        {
            BigtableByteString columnQualifier = column.Qualifier;
            BigtableByteString cellValue = column.Cells[0].Value;
            Console.WriteLine(
                $"\tColumn: {(string)columnQualifier}, Value: {(long)cellValue}");
        }
    }
    

## Client life-cycle management

By default, clients share an internally managed Grpc.Gcp.GcpCallInvoker to establish gRPC channels with the Bigtable service using default credentials. This class allows for multiple channels to be used concurrently and load-balances requests and streams among them. BigtableClient instances are intended to be ephermal and will reuse an existing GcpCallInvoker instance behind the scenes where possible.

Note that this reuse is dependent upon the settings which control the usage of the GcpCallInvoker instance being identical. Accidentally using different settings when creating different clients could result in unintended performance degredation as setting up a new GcpCallInvoker is expensive compared to creating a new BigtableClient.
    
    
    // client1 and client3 will share the same GcpCallInvoker, since they both
    // use the same default settings. This means they will use the same shared
    // set of gRPC channels to the Bigtable service.
    // client2 and client4 will share a different GcpCallInvoker, since they both
    // use the same custom MaxChannels/PreferredMaxStreamsPerChannel settings.
    BigtableServiceApiSettings settings1 = BigtableServiceApiSettings.GetDefault();
    BigtableClient client1 = new BigtableClientBuilder { Settings = settings1 }.Build();
    
    BigtableServiceApiSettings settings2 = new BigtableServiceApiSettings
    {
        MaxChannels = 10,
        PreferredMaxStreamsPerChannel = 4
    };
    BigtableClient client2 = new BigtableClientBuilder { Settings = settings2 }.Build();
    
    BigtableServiceApiSettings settings3 = BigtableServiceApiSettings.GetDefault();
    BigtableClient client3 = new BigtableClientBuilder { Settings = settings3 }.Build();
    
    BigtableServiceApiSettings settings4 = new BigtableServiceApiSettings
    {
        MaxChannels = 10,
        PreferredMaxStreamsPerChannel = 4
    };
    BigtableClient client4 = new BigtableClientBuilder { Settings = settings4 }.Build();
    
    // client5 will not share a GcpCallInvoker with any of the other clients, since
    // its MaxChannels/PreferredMaxStreamsPerChannel settings differ from the others.
    BigtableServiceApiSettings settings5 = new BigtableServiceApiSettings
    {
        MaxChannels = 15,
        PreferredMaxStreamsPerChannel = 4
    };
    BigtableClient client5 = new BigtableClientBuilder { Settings = settings5 }.Build();
    

## Non-default credentials

If you would like to create clients which share a GcpCallInvoker but do not use the default credentials, this can easily be done by manually creating a GcpCallInvoker and using Bigtable's default endpoint and settings.
    
    
    // Create a client from a custom credentials and a GcpCallInvoker that has
    // non-default gRPC stream/channel options.
    // The easiest way of creating a GcpCallInvoker is to use a new
    // BigtableServiceApiClientBuilder just to create the call invoker,
    // then remember the call invoker to set it in other builders.
    // Note: the GcpCallInvoker should be long-lived while the BigtableClient
    // instances can be ephemeral and each use the same call invoker.
    BigtableServiceApiSettings settings = new BigtableServiceApiSettings
    {
        MaxChannels = 10,
        PreferredMaxStreamsPerChannel = 4
    };
    GcpCallInvoker callInvoker = new BigtableServiceApiClientBuilder
    {
        Settings = settings,
        ChannelCredentials = credentials,
    }.CreateGcpCallInvoker();
    
    // These will share the same set of channels to the Bigtable service.
    BigtableClient client1 = new BigtableClientBuilder
    {
        CallInvoker = callInvoker,
        Settings = settings
    }.Build();
    // ...
    BigtableClient client2 = new BigtableClientBuilder
    {
        CallInvoker = callInvoker,
        Settings = settings
    }.Build();
    // ...
    
    await callInvoker.ShutdownAsync();
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
