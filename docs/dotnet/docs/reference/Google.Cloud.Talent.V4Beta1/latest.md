---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/
title: .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:37.584753+00:00
---

# .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta07 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/)
  * [ 3.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/3.0.0-beta06/)
  * [ 2.0.0-beta07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/2.0.0-beta07/)



# Google.Cloud.Talent.V4Beta1

`Google.Cloud.Talent.V4Beta1` is a.NET client library for the [Google Cloud Talent Solution API](https://cloud.google.com/talent-solution/).

Note: This documentation is for version `3.0.0-beta07` of the library. Some samples may not work with other versions.

## Installation

Install the `Google.Cloud.Talent.V4Beta1` package from NuGet. Add it to your project in the normal way (for example by right-clicking on the project in Visual Studio and choosing "Manage NuGet Packages..."). Please ensure you enable pre-release packages (for example, in the Visual Studio NuGet user interface, check the "Include prerelease" box). Some of the following samples might only work with the latest pre-release version (`3.0.0-beta07`) of `Google.Cloud.Talent.V4Beta1`.

## Authentication

When running on Google Cloud, no action needs to be taken to authenticate.

Otherwise, the simplest way of authenticating your API calls is to set up Application Default Credentials. The credentials will automatically be used to authenticate. See [Set up Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc) for more details.

## Getting started

All operations are performed through the following client classes:

  * [CompanyServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.CompanyServiceClient)
  * [CompletionClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.CompletionClient)
  * [EventServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.EventServiceClient)
  * [JobServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.JobServiceClient)
  * [TenantServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.TenantServiceClient)



Create a client instance by calling the static `Create` or `CreateAsync` methods. Alternatively, use the builder class associated with each client class (e.g. CompanyServiceClientBuilder for CompanyServiceClient) as an easy way of specifying custom credentials, settings, or a custom endpoint. Clients are thread-safe, and we recommend using a single instance across your entire application unless you have a particular need to configure multiple client objects separately.

### Using the REST (HTTP/1.1) transport

This library defaults to performing RPCs using [gRPC](https://grpc.io/) using the binary [Protocol Buffer](https://protobuf.dev) wire format. However, it also supports HTTP/1.1 and JSON, for situations where gRPC doesn't work as desired. (This is typically due to an incompatible proxy or other network issue.) To create a client using HTTP/1.1, specify a `RestGrpcAdapter` reference for the `GrpcAdapter` property in the client builder. Sample code:
    
    
    var client = new CompanyServiceClientBuilder
    {
        GrpcAdapter = RestGrpcAdapter.Default
    }.Build();
    

For more details, see the [transport selection](https://cloud.google.com/dotnet/docs/reference/help/transports) page.

## Sample code

## Creating a company
    
    
    CompanyServiceClient client = CompanyServiceClient.Create();
    Company company = new Company
    {
        DisplayName = "Sample company",
        ExternalId = externalId,
        Size = CompanySize.Medium
    };
    ProjectName parent = ProjectName.FromProject(projectId);
    Company created = client.CreateCompany(parent, company);
    Console.WriteLine($"Created company with resource name {created.Name}");
    

## Creating a job
    
    
    JobServiceClient client = JobServiceClient.Create();
    Job job = new Job
    {
        ApplicationInfo = new ApplicationInfo
        {
            Instruction = "See company web site"
        },
        CompanyAsCompanyName = companyName,
        Description = "Company CEO, responsible for everything in the company.",
        RequisitionId = requisitionId,
        Title = "CEO"
    };
    ProjectName parent = ProjectName.FromProject(projectId);
    Job created = client.CreateJob(parent, job);
    Console.WriteLine($"Created job with resource name {created.Name}");
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
