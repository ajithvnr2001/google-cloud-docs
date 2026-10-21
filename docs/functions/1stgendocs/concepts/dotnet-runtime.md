---
url: https://docs.cloud.google.com/functions/1stgendocs/concepts/dotnet-runtime/
title: The .NET Runtime \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:30.493482+00:00
---

# The .NET Runtime  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/concepts/dotnet-runtime/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# The .NET Runtime

## Overview

Your Cloud Run function runs in an environment consisting of an operating system version plus add-on packages, language support, and the Functions Framework library that supports and invokes your function. This environment is identified by the language version, and is known as the runtime.

For information about runtimes in general, and to learn which Ubuntu version each .NET runtime uses, see the [Cloud Run functions execution environment](https://docs.cloud.google.com/functions/1stgendocs/concepts/execution-environment#.net-core).

## Template package

The template package helps you to create new functions. To use it:

  1. Install the [.NET SDK](https://dotnet.microsoft.com/download).

  2. Install the template package:
         
         dotnet new install Google.Cloud.Functions.Templates
         


**Note:** versions of the .NET SDK earlier than .NET 7 use `dotnet new -i` instead of `dotnet new install`.

Templates are provided for the three kinds of functions in C# (the default), F#, and Visual Basic. When creating a new project from a template, specify `-lang f#` to create an F# project, or `-lang vb` to create a Visual Basic project. For more information, see:

  * [.NET Languages](https://docs.cloud.google.com/functions/1stgendocs/concepts/dotnet-langs) (for F# and Visual Basic)



## Select a .NET Functions Framework version

Different versions of the .NET Functions Framework support different runtimes. Version 1 supports .NET Core 3.1 and later, with templates defaulting to .NET Core 3.1. Version 2 supports .NET 6 and later, with templates defaulting to .NET 6.

To upgrade an existing project using .NET Functions Framework version 1, edit the project file (or use Visual Studio) to update all dependencies that begin with `Google.Cloud.Functions` to the latest version, and set the target framework to .NET 6.

## Select your runtime

Cloud Run functions supports several versions of .NET, listed on the [Runtime support](https://docs.cloud.google.com/functions/1stgendocs/runtime-support#.net-core) page. When you deploy your function, you must specify a .NET runtime corresponding to the target framework in your project file (`MyFunction.csproj` or similar). To specify your .NET runtime:

If you're using the Google Cloud CLI, specify the runtime by using the `--runtime` parameter. The `--entry-point` flag specifies the fully qualified class name (FQN). For example:
    
    
    gcloud functions deploy NAME --no-gen2 --entry-point FQN --no-gen2 --runtime dotnet6 --trigger-http

For more deployment parameters, see [Deploy a Cloud Run function](https://docs.cloud.google.com/functions/1stgendocs/deploy#basics).

## Function preparation

You can write a function on your local machine and upload it. To prepare your local machine for .NET development, see [Setting up a .NET development environment](https://docs.cloud.google.com/dotnet/docs/setup).

The library that invokes your function is the [.NET Functions Framework](https://docs.cloud.google.com/functions/1stgendocs/functions-framework).

**Note:** The only type of [event-driven functions](https://docs.cloud.google.com/functions/1stgendocs/writing#types_of_cloud_functions) .NET supports are [CloudEvent functions](https://docs.cloud.google.com/functions/1stgendocs/writing#cloudevent_functions).

## Source code structure

In order for Cloud Run functions to find your function's definition, each runtime has certain structuring requirements for your source code. See [Write Cloud Run functions](https://docs.cloud.google.com/functions/1stgendocs/writing#functions-writing-file-structuring-csharp) for more information.

## Specifying dependencies

You can specify dependencies for your function by adding them to a project file. For more information, see [Specifying dependencies in .NET](https://docs.cloud.google.com/functions/1stgendocs/writing/specifying-dependencies-dotnet).

## What's next

  * [Learn about the other .NET languages](https://docs.cloud.google.com/functions/1stgendocs/concepts/dotnet-langs) you can use to write Cloud Run functions: F# and Visual Basic.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
