---
url: https://docs.cloud.google.com/functions/1stgendocs/writing/specifying-dependencies-dotnet/
title: Specify dependencies in .NET \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:30.437404+00:00
---

# Specify dependencies in .NET  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/writing/specifying-dependencies-dotnet/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Specify dependencies in .NET

.NET Cloud Run functions use [Microsoft Build Engine (MSBuild) project files](https://docs.microsoft.com/en-us/aspnet/web-forms/overview/deployment/web-deployment-in-the-enterprise/understanding-the-project-file). These files are central to the build and deployment process. For C# the file extension is `.csproj`, for F# it is `.fsproj`, and for Visual Basic it is `.vbproj`.

For example, here is the `.csproj` file for the C# Hello World sample:
    
    
      <Project Sdk="Microsoft.NET.Sdk">
      <PropertyGroup>
        <OutputType>Exe</OutputType>
        <TargetFramework>net6.0</TargetFramework>
      </PropertyGroup>
    
      <ItemGroup>
        <PackageReference Include="Google.Cloud.Functions.Hosting" Version="2.2.1" />
      </ItemGroup>
    </Project>
    

You can add libraries to your function's project file as follows:
    
    
    dotnet add package MY_LIBRARY

The [Functions Framework](https://docs.cloud.google.com/functions/1stgendocs/functions-framework) is a required dependency for all functions. Although Cloud Run functions installs it on your behalf when the function is created, we recommend that you include it as an explicit dependency for clarity.

If your function relies on private dependencies, we recommend that you mirror `functions-framework` to your private registry. Include the mirrored `functions-framework` as a dependency to your function to avoid installing the package from the public internet.

For more discussion of dependencies and other types of customization, see [Customization through Functions Startup classes](https://github.com/GoogleCloudPlatform/functions-framework-dotnet/blob/master/docs/customization.md#customization-through-functions-startup-classes).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
