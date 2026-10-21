---
url: https://docs.cloud.google.com/run/docs/runtimes/dotnet/
title: The .NET runtime \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:50.027890+00:00
---

# The .NET runtime  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/runtimes/dotnet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  The .NET runtime Stay organized with collections  Save and categorize content based on your preferences. 

Your Cloud Run function runs in an environment consisting of an operating system version with add-on packages, language support, and the [.NET Functions Framework](https://github.com/GoogleCloudPlatform/functions-framework-dotnet) library that supports and invokes your function. This environment is identified by the language version, and is known as the runtime ID.

## Function preparation

You can prepare a function directly from the Google Cloud console or write it on your local machine and upload it. To prepare your local machine for .NET development, see [Set up a .NET development environment](https://docs.cloud.google.com/dotnet/docs/setup).

## Supported .NET runtimes and base images

Runtime | Runtime ID | Stacks | Runtime base image | Deprecation | Decommission  
---|---|---|---|---|---  
.NET 10 | dotnet10 | 
* google-24 (default)
* google-24-full
| 
* [google-24/dotnet10](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24/runtimes/dotnet10)
* [google-24-full/dotnet10](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/dotnet10)
| 2028-11-14 | 2029-05-14  
.NET 8 | dotnet8 | 
* google-22 (default)
* google-22-full
| 
* [google-22/dotnet8](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/dotnet8)
* [google-22-full/dotnet8](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/dotnet8)
| 2026-11-10 | 2027-05-10  
.NET 6 | dotnet6 | 
* google-22 (default)
* google-22-full
| 
* [google-22/dotnet6](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/dotnet6)
* [google-22-full/dotnet6](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/dotnet6)
| 2024-11-12 | 2025-11-12  
.NET Core 3 | dotnet3 |  google-18-full  |  [google-18-full/dotnet3](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/dotnet3) | 2024-01-30 | 2025-01-30  
  
## Template package

The template package helps you to create new functions. To use it:

  1. Install the [.NET SDK](https://dotnet.microsoft.com/download).

  2. Install the template package:
         
         dotnet new install Google.Cloud.Functions.Templates
         


**Note:** versions of the .NET SDK earlier than .NET 7 use `dotnet new -i` instead of `dotnet new install`.

Templates are provided for the three kinds of functions in C# (the default), F#, and Visual Basic. When creating a new project from a template, specify `-lang f#` to create an F# project, or `-lang vb` to create a Visual Basic project.

## Select your runtime

When you deploy your function, you must specify a .NET runtime corresponding to the target framework in your project file (`MyFunction.csproj` or similar). You can select one of the supported .NET runtimes for your function during deployment.

You can select a runtime version using the Google Cloud console, or the gcloud CLI. Click the tab for instructions on using the tool of your choice:

###  gcloud 

Specify the [.NET base image](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images#how_to_obtain_base_images) for your function using the `--base-image` flag, while deploying your function. For example:
    
    
    gcloud run deploy FUNCTION \
        --source . \
        --function FUNCTION_ENTRYPOINT \
        --base-image dotnet10
    

Replace:

  * FUNCTION with the name of the function you are deploying. You can omit this parameter entirely, but you will be prompted for the name if you omit it.

  * FUNCTION_ENTRYPOINT with the entry point to your function in your source code. This is the code Cloud Run executes when your function runs. The value of this flag must be a function name or fully-qualified class name that exists in your source code.




For detailed instructions on deploying a function using the gcloud CLI, see [Deploy functions in Cloud Run](https://docs.cloud.google.com/run/docs/deploy-functions#gcloud).

###  Console 

You can select a runtime version when you create or update a Cloud Run function in the Google Cloud console. For detailed instructions on deploying a function, see [Deploy functions in Cloud Run](https://docs.cloud.google.com/run/docs/deploy-functions#deploy-functions).

To select a runtime in the Google Cloud console when you create a function, follow these steps:

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Click **Write a function**.

  3. In the **Runtime** list, select a .NET runtime version.

  4. Click **Create** , and wait for Cloud Run to create the service using a placeholder revision.

  5. The console will redirect you to the **Source** tab where you can see the source code of your function. Click **Save and redeploy**.




For detailed instructions on updating the runtime version after your function is deployed, see [Re-deploy new source code](https://docs.cloud.google.com/run/docs/deploy-functions#update-code-functions).

## Source code structure

For Cloud Run functions to find your function's definition, your source code must follow a specific structure. See [Write Cloud Run functions](https://docs.cloud.google.com/run/docs/write-functions#.net) for more information.

## Specifying dependencies

.NET Cloud Run functions uses [Microsoft Build Engine (MSBuild) project files](https://docs.microsoft.com/en-us/aspnet/web-forms/overview/deployment/web-deployment-in-the-enterprise/understanding-the-project-file) which are central to the build and deployment process. You can specify dependencies for your function in a project file. For C# the file extension is `.csproj`, for F# it is `.fsproj`, and for Visual Basic it is `.vbproj`.

For more discussion of dependencies and other types of customization, see [Customization through Functions Startup classes](https://github.com/GoogleCloudPlatform/functions-framework-dotnet/blob/master/docs/customization.md#customization-through-functions-startup-classes).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
