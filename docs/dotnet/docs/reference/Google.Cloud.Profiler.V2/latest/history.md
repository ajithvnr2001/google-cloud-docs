---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/latest/history/
title: .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:39:08.382110+00:00
---

# .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/latest/history/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.7.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/latest/history/)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/2.6.0/history/)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/2.5.0/history/)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/2.4.0/history/)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/2.3.0/history/)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/2.2.0/history/)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/2.1.0/history/)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/2.0.0/history/)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/1.2.0/history/)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/1.1.0/history/)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/1.0.0/history/)



# Version history

## Version 2.7.0, released 2025-11-06

### New features

  * Update dependencies



## Version 2.6.0, released 2024-05-14

### New features

  * Add IServiceCollection extension methods for client registration where an IServiceProvider is required. ([commit 022fab2](https://github.com/googleapis/google-cloud-dotnet/commit/022fab203f28fb9c608972af7f8b83f571ae5694))



## Version 2.5.0, released 2024-03-26

### New features

  * Change netstandard2.1 target to netstandard2.0 ([commit 82bea85](https://github.com/googleapis/google-cloud-dotnet/commit/82bea850661975b9750ac30753528cc9d2e05240))



## Version 2.4.0, released 2024-02-27

### New features

  * Add `start_time` to Profile proto ([commit 4e7680a](https://github.com/googleapis/google-cloud-dotnet/commit/4e7680a120658891eddb812e47e739e239eb524d))



### Documentation improvements

  * Update documentation to add guidance around use of ProfilerService API methods ([commit 4e7680a](https://github.com/googleapis/google-cloud-dotnet/commit/4e7680a120658891eddb812e47e739e239eb524d))



## Version 2.3.0, released 2024-01-08

### New features

  * Add `ListProfiles` RPC to `ExportService` ([commit 720d004](https://github.com/googleapis/google-cloud-dotnet/commit/720d004863acc47395697f6bfcb54063f4dd529f))



## Version 2.2.0, released 2023-03-20

### Bug fixes

  * Marked some fields as input only or output only ([commit 87965f1](https://github.com/googleapis/google-cloud-dotnet/commit/87965f1990e2eb027e01dfc9f1c7658794bc26b5))



### New features

  * Added new method signatures for `CreateOfflineProfile`, `UpdateProfile` ([commit 87965f1](https://github.com/googleapis/google-cloud-dotnet/commit/87965f1990e2eb027e01dfc9f1c7658794bc26b5))
  * Marked `Profile` as a resource ([commit 87965f1](https://github.com/googleapis/google-cloud-dotnet/commit/87965f1990e2eb027e01dfc9f1c7658794bc26b5))



### Documentation improvements

  * Updated comments ([commit 87965f1](https://github.com/googleapis/google-cloud-dotnet/commit/87965f1990e2eb027e01dfc9f1c7658794bc26b5))



## Version 2.1.0, released 2023-01-19

### New features

  * Enable REST transport in C# ([commit 31e55cd](https://github.com/googleapis/google-cloud-dotnet/commit/31e55cdbafe12bfae68e28a75a1b75ceb445684f))



## Version 2.0.0, released 2022-06-08

This is the first version of this package to depend on GAX v4.

There are some breaking changes, both in GAX v4 and in the generated code. The changes that aren't specific to any given API are [described in the Google Cloud documentation](https://cloud.google.com/dotnet/docs/reference/help/breaking-gax4). We don't anticipate any changes to most customer code, but please [file a GitHub issue](https://github.com/googleapis/google-cloud-dotnet/issues/new/choose) if you run into problems.

The most important change in this release is the use of the Grpc.Net.Client package for gRPC communication, instead of Grpc.Core. When using .NET Core 3.1 or .NET 5.0+ this should lead to a smaller installation footprint and greater compatibility (e.g. with Apple M1 chips). Any significant change in a core component comes with the risk of incompatibility, however - so again, please let us know if you encounter any issues.

## Version 1.2.0, released 2021-09-01

  * [Commit ac367e2](https://github.com/googleapis/google-cloud-dotnet/commit/ac367e2): feat: Regenerate all APIs to support self-signed JWTs



## Version 1.1.0, released 2021-05-26

No API surface changes; just dependency updates.

## Version 1.0.0, released 2021-03-02

No API surface change since 1.0.0-beta01

## Version 1.0.0-beta01, released 2021-02-03

Initial release.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
