---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/
title: .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:32.140592+00:00
---

# .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.8.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/)
  * [ 3.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.7.0/)
  * [ 3.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.6.0/)
  * [ 3.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.5.0/)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.4.0/)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.3.0/)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.2.0/)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.1.0/)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.0.0/)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/2.3.0/)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/2.2.0/)



# Google.Cloud.Language.V1

`Google.Cloud.Language.V1` is a.NET client library for the [Google Cloud Natural Language API](https://cloud.google.com/natural-language).

Note: This documentation is for version `3.8.0` of the library. Some samples may not work with other versions.

## Installation

Install the `Google.Cloud.Language.V1` package from NuGet. Add it to your project in the normal way (for example by right-clicking on the project in Visual Studio and choosing "Manage NuGet Packages...").

## Authentication

When running on Google Cloud, no action needs to be taken to authenticate.

Otherwise, the simplest way of authenticating your API calls is to set up Application Default Credentials. The credentials will automatically be used to authenticate. See [Set up Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc) for more details.

## Getting started

All operations are performed through [LanguageServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/Google.Cloud.Language.V1.LanguageServiceClient).

Create a client instance by calling the static `Create` or `CreateAsync` methods. Alternatively, use the builder class associated with each client class (e.g. LanguageServiceClientBuilder for LanguageServiceClient) as an easy way of specifying custom credentials, settings, or a custom endpoint. Clients are thread-safe, and we recommend using a single instance across your entire application unless you have a particular need to configure multiple client objects separately.

### Using the REST (HTTP/1.1) transport

This library defaults to performing RPCs using [gRPC](https://grpc.io/) using the binary [Protocol Buffer](https://protobuf.dev) wire format. However, it also supports HTTP/1.1 and JSON, for situations where gRPC doesn't work as desired. (This is typically due to an incompatible proxy or other network issue.) To create a client using HTTP/1.1, specify a `RestGrpcAdapter` reference for the `GrpcAdapter` property in the client builder. Sample code:
    
    
    var client = new LanguageServiceClientBuilder
    {
        GrpcAdapter = RestGrpcAdapter.Default
    }.Build();
    

For more details, see the [transport selection](https://cloud.google.com/dotnet/docs/reference/help/transports) page.

### Creating a Document

All the methods on the client require a [Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/Google.Cloud.Language.V1.Document) to analyze. The Document class provides convenient factory methods [Document.FromPlainText](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/Google.Cloud.Language.V1.Document#Google_Cloud_Language_V1_Document_FromPlainText_System_String_System_String_) and [Document.FromHtml](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/Google.Cloud.Language.V1.Document#Google_Cloud_Language_V1_Document_FromHtml_System_String_System_String_) to construct instances from text available in your application, or you can specify a Google Cloud Storage URI.

## Sample code

## Analyze sentiment in a document
    
    
    LanguageServiceClient client = LanguageServiceClient.Create();
    Document document = Document.FromPlainText("You're simply the best - better than all the rest.");
    AnalyzeSentimentResponse response = client.AnalyzeSentiment(document);
    Console.WriteLine($"Detected language: {response.Language}");
    Console.WriteLine($"Sentiment score: {response.DocumentSentiment.Score}");
    Console.WriteLine($"Sentiment magnitude: {response.DocumentSentiment.Magnitude}");
    

## Analyze entities in a document
    
    
    LanguageServiceClient client = LanguageServiceClient.Create();
    Document document = Document.FromPlainText("Richard of York gave battle in vain.");
    AnalyzeEntitiesResponse response = client.AnalyzeEntities(document);
    Console.WriteLine($"Detected language: {response.Language}");
    Console.WriteLine("Detected entities:");
    foreach (Entity entity in response.Entities)
    {
        Console.WriteLine($"  {entity.Name} ({(int) (entity.Salience * 100)}%)");
    }
    

## Analyze syntax in a document
    
    
    LanguageServiceClient client = LanguageServiceClient.Create();
    Document document = Document.FromPlainText(
        "This is a simple sentence. This sentence, while not very complicated, is still more complicated than the first.");
    AnalyzeSyntaxResponse response = client.AnalyzeSyntax(document);
    Console.WriteLine($"Detected language: {response.Language}");
    Console.WriteLine($"Number of sentences: {response.Sentences.Count}");
    Console.WriteLine($"Number of tokens: {response.Tokens.Count}");
    

## Multiple operations: analyze syntax and entities
    
    
    LanguageServiceClient client = LanguageServiceClient.Create();
    Document document = Document.FromPlainText("Richard of York gave battle in vain.");
    // "Features" selects which features you wish to enable. Here we want to extract syntax
    // and entities - you can also extract document sentiment.
    AnnotateTextResponse response = client.AnnotateText(document,
        new Features { ExtractSyntax = true, ExtractEntities = true });
    Console.WriteLine($"Detected language: {response.Language}");
    // The Sentences and Tokens properties provide all kinds of information
    // about the parsed text.
    Console.WriteLine($"Number of sentences: {response.Sentences.Count}");
    Console.WriteLine($"Number of tokens: {response.Tokens.Count}");
    Console.WriteLine("Detected entities:");
    foreach (Entity entity in response.Entities)
    {
        Console.WriteLine($"  {entity.Name} ({(int)(entity.Salience * 100)}%)");
    }
    

## Using an API key

The Cloud Language API supports [API keys](https://cloud.google.com/docs/authentication/api-keys) as an alternative to regular authentication. The Google.Cloud.Language.V1 library can be configured to use an API key instead of any other credentials, by setting the `ApiKey` property in the client builder, as shown below.
    
    
    // Create a LanguageServiceClient which uses the given API key
    // instead of regular credentials.
    LanguageServiceClient client = new LanguageServiceClientBuilder
    {
        ApiKey = apiKey
    }.Build();
    
    // After creating the client with an API key configured, we can use it
    // as normal.
    Document document = Document.FromPlainText("This is a simple sentence.");
    AnalyzeSyntaxResponse response = client.AnalyzeSyntax(document);
    
    Console.WriteLine($"Detected language: {response.Language}");
    Console.WriteLine($"Number of sentences: {response.Sentences.Count}");
    Console.WriteLine($"Number of tokens: {response.Tokens.Count}");
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
