---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/
title: .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:59:45.475717+00:00
---

# .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.16.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/)
  * [ 3.15.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.15.0/)
  * [ 3.14.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.14.0/)
  * [ 3.13.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.13.0/)
  * [ 3.12.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.12.0/)
  * [ 3.11.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.11.0/)
  * [ 3.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.10.0/)
  * [ 3.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.9.0/)
  * [ 3.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.8.0/)
  * [ 3.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.7.0/)
  * [ 3.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.6.0/)
  * [ 3.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.5.0/)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.4.0/)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.3.0/)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.2.0/)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.1.0/)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.0.0/)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/2.6.0/)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/2.5.0/)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/2.4.0/)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/2.3.0/)



# Google.Cloud.Monitoring.V3

`Google.Cloud.Monitoring.V3` is a.NET client library for the [Google Cloud Monitoring API](https://cloud.google.com/monitoring/api/v3/).

Note: This documentation is for version `3.16.0` of the library. Some samples may not work with other versions.

## Installation

Install the `Google.Cloud.Monitoring.V3` package from NuGet. Add it to your project in the normal way (for example by right-clicking on the project in Visual Studio and choosing "Manage NuGet Packages...").

## Authentication

When running on Google Cloud, no action needs to be taken to authenticate.

Otherwise, the simplest way of authenticating your API calls is to set up Application Default Credentials. The credentials will automatically be used to authenticate. See [Set up Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc) for more details.

## Getting started

All operations are performed through the following client classes:

  * [AlertPolicyServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.AlertPolicyServiceClient)
  * [GroupServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.GroupServiceClient)
  * [MetricServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.MetricServiceClient)
  * [NotificationChannelServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.NotificationChannelServiceClient)
  * [QueryServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.QueryServiceClient)
  * [ServiceMonitoringServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.ServiceMonitoringServiceClient)
  * [SnoozeServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.SnoozeServiceClient)
  * [UptimeCheckServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.UptimeCheckServiceClient)



Create a client instance by calling the static `Create` or `CreateAsync` methods. Alternatively, use the builder class associated with each client class (e.g. AlertPolicyServiceClientBuilder for AlertPolicyServiceClient) as an easy way of specifying custom credentials, settings, or a custom endpoint. Clients are thread-safe, and we recommend using a single instance across your entire application unless you have a particular need to configure multiple client objects separately.

## Sample code

## List metric descriptors
    
    
    MetricServiceClient client = MetricServiceClient.Create();
    ProjectName projectName = ProjectName.FromProject(projectId);
    PagedEnumerable<ListMetricDescriptorsResponse, MetricDescriptor> metrics = client.ListMetricDescriptors(projectName);
    foreach (MetricDescriptor metric in metrics.Take(10))
    {
        Console.WriteLine($"{metric.Name}: {metric.DisplayName}");
    }
    

## List groups
    
    
    GroupServiceClient client = GroupServiceClient.Create();
    ProjectName projectName = ProjectName.FromProject(projectId);
    PagedEnumerable<ListGroupsResponse, Group> groups = client.ListGroups(projectName);
    foreach (Group group in groups.Take(10))
    {
        Console.WriteLine($"{group.Name}: {group.DisplayName}");
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
