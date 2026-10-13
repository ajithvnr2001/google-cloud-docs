---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/
title: Google.Cloud.NetworkSecurity.V1 \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:56.285879+00:00
---

# Google.Cloud.NetworkSecurity.V1  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google.Cloud.NetworkSecurity.V1 Stay organized with collections  Save and categorize content based on your preferences. 

`Google.Cloud.NetworkSecurity.V1` is a.NET client library for the [Network Security API](https://cloud.google.com/products/networking).

Note: This documentation is for version `1.0.0-beta01` of the library. Some samples may not work with other versions.

## Installation

Install the `Google.Cloud.NetworkSecurity.V1` package from NuGet. Add it to your project in the normal way (for example by right-clicking on the project in Visual Studio and choosing "Manage NuGet Packages..."). Please ensure you enable pre-release packages (for example, in the Visual Studio NuGet user interface, check the "Include prerelease" box). Some of the following samples might only work with the latest pre-release version (`1.0.0-beta01`) of `Google.Cloud.NetworkSecurity.V1`.

## Authentication

When running on Google Cloud, no action needs to be taken to authenticate.

Otherwise, the simplest way of authenticating your API calls is to set up Application Default Credentials. The credentials will automatically be used to authenticate. See [Set up Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc) for more details.

## Getting started

All operations are performed through the following client classes:

  * [AddressGroupServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.AddressGroupServiceClient)
  * [DnsThreatDetectorServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DnsThreatDetectorServiceClient)
  * [FirewallActivationClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallActivationClient)
  * [InterceptClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.InterceptClient)
  * [MirroringClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.MirroringClient)
  * [NetworkSecurityClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.NetworkSecurityClient)
  * [OrganizationAddressGroupServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OrganizationAddressGroupServiceClient)
  * [OrganizationSecurityProfileGroupServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OrganizationSecurityProfileGroupServiceClient)
  * [SecurityProfileGroupServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.SecurityProfileGroupServiceClient)
  * [SSERealmServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.SSERealmServiceClient)



Create a client instance by calling the static `Create` or `CreateAsync` methods. Alternatively, use the builder class associated with each client class (e.g. AddressGroupServiceClientBuilder for AddressGroupServiceClient) as an easy way of specifying custom credentials, settings, or a custom endpoint. Clients are thread-safe, and we recommend using a single instance across your entire application unless you have a particular need to configure multiple client objects separately.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-01 UTC."],[],[]] 
