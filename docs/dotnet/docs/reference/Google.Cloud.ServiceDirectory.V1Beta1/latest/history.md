---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/history/
title: .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:17:43.622201+00:00
---

# .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/history/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta07 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/history/)
  * [ 2.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/2.0.0-beta06/history/)
  * [ 1.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/1.0.0-beta06/history/)



# Version history

## Version 2.0.0-beta07, released 2025-11-06

### New features

  * Update dependencies



### Documentation improvements

  * Add maximum page_size to ListNamespace API documentation
  * Add maximum page_size to ListService API documentation
  * Add maximum page_size to ListEndpoint API documentation



## Version 2.0.0-beta06, released 2024-05-08

### New features

  * Add IServiceCollection extension methods for client registration where an IServiceProvider is required. ([commit 022fab2](https://github.com/googleapis/google-cloud-dotnet/commit/022fab203f28fb9c608972af7f8b83f571ae5694))



## Version 2.0.0-beta05, released 2024-03-26

### New features

  * Change netstandard2.1 target to netstandard2.0 ([commit 82bea85](https://github.com/googleapis/google-cloud-dotnet/commit/82bea850661975b9750ac30753528cc9d2e05240))



## Version 2.0.0-beta04, released 2024-02-29

No API surface changes; just dependency updates.

## Version 2.0.0-beta03, released 2023-08-04

### New features

  * Added network and uid fields in Endpoint message ([commit 832f388](https://github.com/googleapis/google-cloud-dotnet/commit/832f388e29a18c4d7e0e39d74d1dc45536ada722))
  * Added uid field to Namespace message ([commit 832f388](https://github.com/googleapis/google-cloud-dotnet/commit/832f388e29a18c4d7e0e39d74d1dc45536ada722))
  * Added uid field to Service message ([commit 832f388](https://github.com/googleapis/google-cloud-dotnet/commit/832f388e29a18c4d7e0e39d74d1dc45536ada722))
  * Enable Location methods ([commit 832f388](https://github.com/googleapis/google-cloud-dotnet/commit/832f388e29a18c4d7e0e39d74d1dc45536ada722))



### Documentation improvements

  * Updated docs for ResolveServiceRequest message ([commit 832f388](https://github.com/googleapis/google-cloud-dotnet/commit/832f388e29a18c4d7e0e39d74d1dc45536ada722))
  * Updated docs for ListServicesRequest and ListEndpointsRequest message ([commit 832f388](https://github.com/googleapis/google-cloud-dotnet/commit/832f388e29a18c4d7e0e39d74d1dc45536ada722))



## Version 2.0.0-beta02, released 2023-01-19

### New features

  * Enable REST transport in C# ([commit e04406f](https://github.com/googleapis/google-cloud-dotnet/commit/e04406fbc8700134ab6955e5244a5f2924a16a0a))



## Version 2.0.0-beta01, released 2022-06-08

This is the first version of this package to depend on GAX v4.

There are some breaking changes, both in GAX v4 and in the generated code. The changes that aren't specific to any given API are [described in the Google Cloud documentation](https://cloud.google.com/dotnet/docs/reference/help/breaking-gax4). We don't anticipate any changes to most customer code, but please [file a GitHub issue](https://github.com/googleapis/google-cloud-dotnet/issues/new/choose) if you run into problems.

The most important change in this release is the use of the Grpc.Net.Client package for gRPC communication, instead of Grpc.Core. When using .NET Core 3.1 or .NET 5.0+ this should lead to a smaller installation footprint and greater compatibility (e.g. with Apple M1 chips). Any significant change in a core component comes with the risk of incompatibility, however - so again, please let us know if you encounter any issues.

## Version 1.0.0-beta06, released 2021-09-01

  * [Commit ac367e2](https://github.com/googleapis/google-cloud-dotnet/commit/ac367e2): feat: Regenerate all APIs to support self-signed JWTs



## Version 1.0.0-beta05, released 2021-07-27

  * [Commit 14795e6](https://github.com/googleapis/google-cloud-dotnet/commit/14795e6): feat: Update Service Directory v1beta1 protos to include VPC Network field, and create/modify timestamp fields.



## Version 1.0.0-beta04, released 2021-05-26

No API surface changes; just dependency updates.

## Version 1.0.0-beta03, released 2020-11-18

  * [Commit 0ca05f5](https://github.com/googleapis/google-cloud-dotnet/commit/0ca05f5): chore: Regenerate all APIs using protoc 3.13 and Grpc.Tools 2.31
  * [Commit 6bde7a3](https://github.com/googleapis/google-cloud-dotnet/commit/6bde7a3): docs: Regenerate all APIs with service comments in client documentation
  * [Commit 947a573](https://github.com/googleapis/google-cloud-dotnet/commit/947a573): docs: Regenerate all clients with more explicit documentation



## Version 1.0.0-beta02, released 2020-03-19

No API surface changes compared with 1.0.0-beta01, just dependency and implementation changes.

## Version 1.0.0-beta01, released 2020-03-11

Initial beta release.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
