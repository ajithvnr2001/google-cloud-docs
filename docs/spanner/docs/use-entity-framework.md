---
url: https://docs.cloud.google.com/spanner/docs/use-entity-framework/
title: Using Entity Framework Core with Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:12.142978+00:00
---

# Using Entity Framework Core with Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/use-entity-framework/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Using Entity Framework Core with Spanner Stay organized with collections  Save and categorize content based on your preferences. 

**PostgreSQL interface note:** The Spanner Entity Framework Core provider isn't supported in PostgreSQL databases. 

The [Spanner Entity Framework Core provider](https://github.com/googleapis/dotnet-spanner-entity-framework) lets you create a Spanner database, run queries, and update data through an application using [Entity Framework Core](https://docs.microsoft.com/en-us/ef/core/). The provider is compatible with [Microsoft.EntityFrameworkCore 8](https://www.nuget.org/packages/Microsoft.EntityFrameworkCore/8.0).

## Set up the Spanner Entity Framework Core provider

To set up the Spanner Entity Framework Core provider in your application, add the following dependency.
    
    
    <Project Sdk="Microsoft.NET.Sdk">
    
      <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <OutputType>Exe</OutputType>
      </PropertyGroup>
    
      ...
    
      <ItemGroup>
        <PackageReference Include="Google.Cloud.EntityFrameworkCore.Spanner" Version="3.2.0" />
      </ItemGroup>
    
      ...
    
    </Project>
    

As authentication for the Spanner Entity Framework Core provider, the [service account JSON credentials](https://docs.cloud.google.com/docs/authentication/getting-started) file location should be provided in the `GOOGLE_APPLICATION_CREDENTIALS` environment variable. Otherwise, the provider can also use the default credentials set in the Google Cloud CLI `gcloud` application.

## Use the Spanner Entity Framework Core provider

For more information about the available features, limitations of the provider, recommendations on how to use the provider, and for code samples, consult the [reference documentation](https://github.com/googleapis/dotnet-spanner-entity-framework#readme) on GitHub.

## What's next

  * Checkout the [code examples](https://github.com/googleapis/dotnet-spanner-entity-framework/tree/master/Google.Cloud.EntityFrameworkCore.Spanner.Samples) on how to use the Spanner Entity Framework Core provider.
  * View the repository for the Spanner Entity Framework Core provider on [GitHub](https://github.com/googleapis/dotnet-spanner-entity-framework).
  * File a [GitHub issue](https://github.com/googleapis/dotnet-spanner-entity-framework/issues) to report a bug or ask a question about the Spanner Entity Framework provider.
  * Learn more about [Entity Framework Core](https://docs.microsoft.com/en-us/ef/core/).
  * Learn more about [NuGet](https://www.nuget.org/).
  * Learn about authorization and authentication credentials in [Getting started with authentication](https://docs.cloud.google.com/docs/authentication/getting-started).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
