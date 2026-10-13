---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/
title: Google.Cloud.GkeMultiCloud.V1 \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:30.499698+00:00
---

# Google.Cloud.GkeMultiCloud.V1  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google.Cloud.GkeMultiCloud.V1 Stay organized with collections  Save and categorize content based on your preferences. 

2.11.0 (latest)  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.0.0-beta01 

`Google.Cloud.GkeMultiCloud.V1` is a.NET client library for the [Anthos Multi-Cloud API](https://cloud.google.com/anthos/clusters/docs/multi-cloud).

Note: This documentation is for version `2.11.0` of the library. Some samples may not work with other versions.

## Installation

Install the `Google.Cloud.GkeMultiCloud.V1` package from NuGet. Add it to your project in the normal way (for example by right-clicking on the project in Visual Studio and choosing "Manage NuGet Packages...").

## Authentication

When running on Google Cloud, no action needs to be taken to authenticate.

Otherwise, the simplest way of authenticating your API calls is to set up Application Default Credentials. The credentials will automatically be used to authenticate. See [Set up Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc) for more details.

## Getting started

All operations are performed through the following client classes:

  * [AttachedClustersClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.AttachedClustersClient)
  * [AwsClustersClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.AwsClustersClient)
  * [AzureClustersClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.AzureClustersClient)



Clients in this API must be constructed with a regional endpoint. This can be done easily using the builder for a specific client (`AzureClustersClientBuilder` for `AzureClustersClient` for example). The following example shows how to list the Azure clusters for a given project in the `us-west1` region.
    
    
    string region = "us-west1";
    AttachedClustersClient client = new AttachedClustersClientBuilder
    {
        Endpoint = $"{region}-gkemulticloud.googleapis.com"
    }.Build();
    
    LocationName location = new LocationName(projectId, region);
    PagedEnumerable<ListAttachedClustersResponse, AttachedCluster> clusters = client.ListAttachedClusters(location);
    foreach (AttachedCluster cluster in clusters)
    {
        Console.WriteLine(cluster.Name);
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-26 UTC."],[],[]] 
