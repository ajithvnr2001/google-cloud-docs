---
url: https://docs.cloud.google.com/functions/1stgendocs/concepts/dotnet-langs/
title: .NET Languages \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:30.827576+00:00
---

# .NET Languages  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/concepts/dotnet-langs/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# .NET Languages

It's possible to write your function in using different .NET languages (C#, Visual Basic, or F#). The core task is the same in all languages—you create a class implementing one of the Functions Framework interfaces:

  * `[IHttpFunction](https://github.com/GoogleCloudPlatform/functions-framework-dotnet/blob/master/src/Google.Cloud.Functions.Framework/IHttpFunction.cs)`
  * The generic `[ICloudEvent<T>](https://github.com/GoogleCloudPlatform/functions-framework-dotnet/blob/master/src/Google.Cloud.Functions.Framework/ICloudEventFunction.cs)`
  * The non-generic `[ICloudEvent](https://github.com/GoogleCloudPlatform/functions-framework-dotnet/blob/master/src/Google.Cloud.Functions.Framework/ICloudEventFunction.cs)`



This document provides examples for F# and Visual Basic.

## Templates

Note that to run the examples in this document, you will use the [templates](https://github.com/GoogleCloudPlatform/functions-framework-dotnet#functions-framework-for-net):

  1. Install the [.NET SDK](https://dotnet.microsoft.com/download).

  2. Install the template package:
         
         dotnet new install Google.Cloud.Functions.Templates
         


**Note:** versions of the .NET SDK earlier than .NET 7 use `dotnet new -i` instead of `dotnet new install`.

Templates are provided for the three kinds of functions in C# (the default), F#, and Visual Basic. When creating a new project from a template, specify `-lang f#` to create an F# project, or `-lang vb` to create a Visual Basic project. For example, to create a new untyped CloudEvent function for Visual Basic, you would run:
    
    
    dotnet new gcf-untyped-event -lang vb
    

**Note:** `Function` is a keyword in Visual Basic, so for Visual Basic, the templates create a class with the name `CloudFunction`.

## HTTP function examples

You use [HTTP functions](https://docs.cloud.google.com/functions/1stgendocs/writing/write-http-functions) when you want to invoke your function via an HTTP(S) request. The following examples output the message `"Hello World!"`

### F#
    
    
    namespace HelloWorldFSharp
    
    open Google.Cloud.Functions.Framework
    open Microsoft.AspNetCore.Http
    
    type Function() =
        interface IHttpFunction with
            member this.HandleAsync context =
                async {
                    do! context.Response.WriteAsync "Hello World!" |> Async.AwaitTask
                } |> Async.StartAsTask :> _

### Visual Basic
    
    
    Imports Google.Cloud.Functions.Framework
    Imports Microsoft.AspNetCore.Http
    
    Public Class CloudFunction
        Implements IHttpFunction
    
        Public Async Function HandleAsync(context As HttpContext) As Task Implements IHttpFunction.HandleAsync
            Await context.Response.WriteAsync("Hello World!")
        End Function
    End Class

### Project files for HTTP examples

Here are the project files for the above samples:

### F#
    
    
    <Project Sdk="Microsoft.NET.Sdk">
      <PropertyGroup>
        <OutputType>Exe</OutputType>
        <TargetFramework>net6.0</TargetFramework>
      </PropertyGroup>
    
      <ItemGroup>
        <Compile Include="Function.fs" />
      </ItemGroup>
    
      <ItemGroup>
        <PackageReference Include="Google.Cloud.Functions.Hosting" Version="2.2.1" />
      </ItemGroup>
    </Project>

### Visual Basic
    
    
    <Project Sdk="Microsoft.NET.Sdk">
      <PropertyGroup>
        <OutputType>Exe</OutputType>
        <RootNamespace>HelloWorldVb</RootNamespace>
        <TargetFramework>net6.0</TargetFramework>
      </PropertyGroup>
    
      <ItemGroup>
        <PackageReference Include="Google.Cloud.Functions.Hosting" Version="2.2.1" />
      </ItemGroup>
    </Project>

### Deploying the HTTP functions

### F#
    
    
     gcloud functions deploy fsharp-helloworld --no-gen2 --entry-point HelloWorldFSharp.Function --runtime dotnet6 --trigger-http --allow-unauthenticated
    

### Visual Basic
    
    
     gcloud functions deploy vb-helloworld --no-gen2 --entry-point HelloWorldVb.CloudFunction --runtime dotnet6 --trigger-http --allow-unauthenticated
    

## CloudEvent examples

You use [CloudEvent functions](https://github.com/GoogleCloudPlatform/functions-framework-dotnet#cloud-event-functions) when you want to have your Cloud Run function invoked indirectly in response to an asynchronous event, such as a message on a Pub/Sub topic, a change in a Cloud Storage bucket, or a Firebase event.

### F#
    
    
    namespace HelloPubSubFSharp
    
    open Google.Cloud.Functions.Framework
    open Google.Events.Protobuf.Cloud.PubSub.V1
    open Microsoft.Extensions.Logging
    open System
    open System.Threading.Tasks
    
    type Function(logger: ILogger<Function>) =
        interface ICloudEventFunction<MessagePublishedData> with
            member this.HandleAsync(cloudEvent, data, cancellationToken) =
                let nameFromMessage = data.Message.TextData
                let name = if String.IsNullOrEmpty(nameFromMessage) then "world" else nameFromMessage
                logger.LogInformation("Hello {name}", name)
                Task.CompletedTask

### Visual Basic
    
    
    Imports System.Threading
    Imports CloudNative.CloudEvents
    Imports Google.Cloud.Functions.Framework
    Imports Google.Events.Protobuf.Cloud.PubSub.V1
    Imports Microsoft.Extensions.Logging
    
    Public Class CloudFunction
        Implements ICloudEventFunction(Of MessagePublishedData)
    
        Private _logger As ILogger
    
        Public Sub New(ByVal logger As ILogger(Of CloudFunction))
            _logger = logger
        End Sub
    
    
        Public Function HandleAsync(cloudEvent As CloudEvent, data As MessagePublishedData, cancellationToken As CancellationToken) As Task _
            Implements ICloudEventFunction(Of MessagePublishedData).HandleAsync
    
            Dim nameFromMessage = data.Message?.TextData
            Dim name = If(String.IsNullOrEmpty(nameFromMessage), "world", nameFromMessage)
            _logger.LogInformation("Hello {name}", name)
    
            Return Task.CompletedTask
        End Function
    End Class

### Deploying the CloudEvent functions

### F#
    
    
     gcloud functions deploy fsharp-hello-pubsub --no-gen2 --entry-point HelloPubSubFSharp.Function --runtime dotnet6 --trigger-topic my-topic --allow-unauthenticated
    

### Visual Basic
    
    
     gcloud functions deploy vb-hello-pubsub --no-gen2 --entry-point HelloPubSubVb.CloudFunction --runtime dotnet6 --trigger-topic my-topic --allow-unauthenticated
    

### Test the CloudEvent examples

You can test the CloudEvent examples as follows:

  1. Publish a message to your Pub/Sub topic to trigger your function:
         
         gcloud pubsub topics publish my-topic --message Flurry

  2. Look at the logs:
         
         gcloud functions logs read --limit 10




You should see something like this, with a message that includes the name you published to the Pub/Sub topic:
    
    
    D      my-function  ...  Function execution started
    I      my-function  ...  Hello Flurry!
    D      my-function  ...  Function execution took 39 ms, finished with status: 'ok'
    

**Note:** log messages may be delayed by a few minutes.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
