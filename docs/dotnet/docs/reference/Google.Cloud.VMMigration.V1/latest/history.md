---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/history/
title: .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:54:18.990221+00:00
---

# .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/history/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.9.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/history/)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.8.0/history/)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.7.0/history/)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.6.0/history/)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.5.0/history/)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.4.0/history/)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.3.0/history/)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.2.0/history/)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.1.0/history/)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.0.0/history/)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/1.0.0/history/)



# Version history

## Version 2.9.0, released 2025-11-17

### New features

  * Add adaptation modifiers and storage pools to MigratingVM target defaults
  * Add adaptation modifiers and guest OS features to ImageImport target details



### Documentation improvements

  * A comment for method `CancelImageImportJob` in service `VmMigration` is changed
  * A comment for message `DataDiskImageImport` is changed



## Version 2.8.0, released 2025-11-06

### New features

  * Update dependencies



## Version 2.7.0, released 2025-09-08

### New features

  * Azure as a source
  * CMEK support
  * VM disk migration
  * Image Import
  * Machine Image Import
  * Cutover forecast
  * OS capabilities detection
  * Multiple additional supported target details
  * Migration warnings in addition to errors
  * API for extending the time to live (TTL) of a Migrating VM



### Bug fixes

  * Changed field behavior for an existing field `key` in message `.google.cloud.vmmigration.v1.AwsSourceDetails` to `required` to protect from incorrect input
  * Changed field behavior for an existing field `value` in message `.google.cloud.vmmigration.v1.AwsSourceDetails` to `required` to protect from incorrect input
  * Changed field behavior for an existing field `project` in message `.google.cloud.vmmigration.v1.TargetProject` to `required` to protect from incorrect input



### Documentation improvements

  * Updated comments and descriptions to improve clarity



## Version 2.6.0, released 2024-05-14

### New features

  * Add IServiceCollection extension methods for client registration where an IServiceProvider is required. ([commit 022fab2](https://github.com/googleapis/google-cloud-dotnet/commit/022fab203f28fb9c608972af7f8b83f571ae5694))



## Version 2.5.0, released 2024-03-26

### New features

  * Change netstandard2.1 target to netstandard2.0 ([commit 82bea85](https://github.com/googleapis/google-cloud-dotnet/commit/82bea850661975b9750ac30753528cc9d2e05240))



## Version 2.4.0, released 2024-02-29

No API surface changes; just dependency updates.

## Version 2.3.0, released 2023-01-19

### New features

  * Enable REST transport in C# ([commit 6ce3faf](https://github.com/googleapis/google-cloud-dotnet/commit/6ce3faf6f74ea6c63e14ee4c77627a6774fb807f))



## Version 2.2.0, released 2023-01-16

### New features

  * AWS as a source ([commit 8c6bdf0](https://github.com/googleapis/google-cloud-dotnet/commit/8c6bdf05056adb2f6f87045c4209838c00630a76))
  * Cycles history ([commit 8c6bdf0](https://github.com/googleapis/google-cloud-dotnet/commit/8c6bdf05056adb2f6f87045c4209838c00630a76))
  * Cycle\Clone\Cutover steps ([commit 8c6bdf0](https://github.com/googleapis/google-cloud-dotnet/commit/8c6bdf05056adb2f6f87045c4209838c00630a76))



## Version 2.1.0, released 2022-07-25

### New features

  * Rename product ([commit f3b6e78](https://github.com/googleapis/google-cloud-dotnet/commit/f3b6e78f207771c908bdd9016c6be22e001566b9))
  * API updates ([commit f3b6e78](https://github.com/googleapis/google-cloud-dotnet/commit/f3b6e78f207771c908bdd9016c6be22e001566b9))



## Version 2.0.0, released 2022-06-08

This is the first version of this package to depend on GAX v4.

There are some breaking changes, both in GAX v4 and in the generated code. The changes that aren't specific to any given API are [described in the Google Cloud documentation](https://cloud.google.com/dotnet/docs/reference/help/breaking-gax4). We don't anticipate any changes to most customer code, but please [file a GitHub issue](https://github.com/googleapis/google-cloud-dotnet/issues/new/choose) if you run into problems.

The most important change in this release is the use of the Grpc.Net.Client package for gRPC communication, instead of Grpc.Core. When using .NET Core 3.1 or .NET 5.0+ this should lead to a smaller installation footprint and greater compatibility (e.g. with Apple M1 chips). Any significant change in a core component comes with the risk of incompatibility, however - so again, please let us know if you encounter any issues.

## Version 1.0.0, released 2022-01-25

No API surface changes; just dependency updates and promotion to 1.0.0.

## Version 1.0.0-beta01, released 2021-11-15

Initial release.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
