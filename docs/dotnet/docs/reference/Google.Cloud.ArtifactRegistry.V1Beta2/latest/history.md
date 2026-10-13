---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/history/
title: .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:18:17.125384+00:00
---

# .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/history/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/history/)
  * [ 2.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/2.0.0-beta05/history/)
  * [ 1.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/1.0.0-beta06/history/)



# Version history

## Version 2.0.0-beta06, released 2025-11-03

### New features

  * Update dependencies



## Version 2.0.0-beta05, released 2024-05-13

### New features

  * Add IServiceCollection extension methods for client registration where an IServiceProvider is required. ([commit 022fab2](https://github.com/googleapis/google-cloud-dotnet/commit/022fab203f28fb9c608972af7f8b83f571ae5694))



## Version 2.0.0-beta04, released 2024-03-26

### New features

  * Change netstandard2.1 target to netstandard2.0 ([commit 82bea85](https://github.com/googleapis/google-cloud-dotnet/commit/82bea850661975b9750ac30753528cc9d2e05240))



## Version 2.0.0-beta03, released 2024-02-28

No API surface changes; just dependency updates.

## Version 2.0.0-beta02, released 2023-01-16

### New features

  * Enable REST transport in C# ([commit a6c4606](https://github.com/googleapis/google-cloud-dotnet/commit/a6c46063bd961a9dadc728a780d66de772f28e71))
  * Add location methods ([commit 4c5f1de](https://github.com/googleapis/google-cloud-dotnet/commit/4c5f1deedbab60585fb109ab6ec0fafc86f0bcff))



## Version 2.0.0-beta01, released 2022-06-08

This is the first version of this package to depend on GAX v4.

There are some breaking changes, both in GAX v4 and in the generated code. The changes that aren't specific to any given API are [described in the Google Cloud documentation](https://cloud.google.com/dotnet/docs/reference/help/breaking-gax4). We don't anticipate any changes to most customer code, but please [file a GitHub issue](https://github.com/googleapis/google-cloud-dotnet/issues/new/choose) if you run into problems.

The most important change in this release is the use of the Grpc.Net.Client package for gRPC communication, instead of Grpc.Core. When using .NET Core 3.1 or .NET 5.0+ this should lead to a smaller installation footprint and greater compatibility (e.g. with Apple M1 chips). Any significant change in a core component comes with the risk of incompatibility, however - so again, please let us know if you encounter any issues.

## Version 1.0.0-beta06, released 2022-04-26

### Documentation improvements

  * More details for ListFilesRequest parent field ([commit 3602d26](https://github.com/googleapis/google-cloud-dotnet/commit/3602d266918515ebfc533a44a77986b2e9b10673))



## Version 1.0.0-beta05, released 2022-02-07

### New features

  * Add APIs for importing and uploading Apt and Yum artifacts ([commit 14bc6ed](https://github.com/googleapis/google-cloud-dotnet/commit/14bc6edc0e67a2a0809486c66ce901e63b07a42f))
  * Add version policy support for Maven repositories ([commit 14bc6ed](https://github.com/googleapis/google-cloud-dotnet/commit/14bc6edc0e67a2a0809486c66ce901e63b07a42f))
  * Add order_by support for listing versions ([commit 14bc6ed](https://github.com/googleapis/google-cloud-dotnet/commit/14bc6edc0e67a2a0809486c66ce901e63b07a42f))



## Version 1.0.0-beta04, released 2022-01-17

### Bug fixes

  * Fix resource pattern ID segment name ([commit dcc9a2a](https://github.com/googleapis/google-cloud-dotnet/commit/dcc9a2adf614a03250898a04642c4da5a30030eb))



## Version 1.0.0-beta03, released 2021-08-19

  * [Commit ac367e2](https://github.com/googleapis/google-cloud-dotnet/commit/ac367e2): feat: Regenerate all APIs to support self-signed JWTs



## Version 1.0.0-beta02, released 2021-05-25

No API surface changes; just dependency updates.

## Version 1.0.0-beta01, released 2020-11-16

Initial release.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
