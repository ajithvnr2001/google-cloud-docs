---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/history/
title: .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:37:24.729227+00:00
---

# .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/history/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/history/)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/2.4.0/history/)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/2.3.0/history/)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/2.2.0/history/)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/2.1.0/history/)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/2.0.0/history/)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/1.4.0/history/)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/1.3.0/history/)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/1.2.0/history/)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/1.1.0/history/)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/1.0.0/history/)



# Version history

## Version 2.5.0, released 2025-11-03

### New features

  * Update dependencies



## Version 2.4.0, released 2024-05-13

### New features

  * Add IServiceCollection extension methods for client registration where an IServiceProvider is required. ([commit 022fab2](https://github.com/googleapis/google-cloud-dotnet/commit/022fab203f28fb9c608972af7f8b83f571ae5694))



## Version 2.3.0, released 2024-03-26

### New features

  * Change netstandard2.1 target to netstandard2.0 ([commit 82bea85](https://github.com/googleapis/google-cloud-dotnet/commit/82bea850661975b9750ac30753528cc9d2e05240))



## Version 2.2.0, released 2024-02-28

### Documentation improvements

  * Point to Search Console for domain ownership verification ([commit e79e82e](https://github.com/googleapis/google-cloud-dotnet/commit/e79e82e92a5cccdfa8f6bc7e16c1805e2632afb8))



## Version 2.1.0, released 2023-01-17

### New features

  * Enable REST transport in C# ([commit cdb518c](https://github.com/googleapis/google-cloud-dotnet/commit/cdb518c3524106ea73f0e546557a0180589ca3b0))



## Version 2.0.0, released 2022-06-08

This is the first version of this package to depend on GAX v4.

There are some breaking changes, both in GAX v4 and in the generated code. The changes that aren't specific to any given API are [described in the Google Cloud documentation](https://cloud.google.com/dotnet/docs/reference/help/breaking-gax4). We don't anticipate any changes to most customer code, but please [file a GitHub issue](https://github.com/googleapis/google-cloud-dotnet/issues/new/choose) if you run into problems.

The most important change in this release is the use of the Grpc.Net.Client package for gRPC communication, instead of Grpc.Core. When using .NET Core 3.1 or .NET 5.0+ this should lead to a smaller installation footprint and greater compatibility (e.g. with Apple M1 chips). Any significant change in a core component comes with the risk of incompatibility, however - so again, please let us know if you encounter any issues.

## Version 1.4.0, released 2022-05-05

### New features

  * Add Application.service_account ([commit 523e2d2](https://github.com/googleapis/google-cloud-dotnet/commit/523e2d23624e0ed8565027843f2e7e48c2e76f5c))
  * Add client library method signature to retrieve Application by name ([commit 523e2d2](https://github.com/googleapis/google-cloud-dotnet/commit/523e2d23624e0ed8565027843f2e7e48c2e76f5c))
  * Add Service.labels ([commit 523e2d2](https://github.com/googleapis/google-cloud-dotnet/commit/523e2d23624e0ed8565027843f2e7e48c2e76f5c))
  * Add Version.app_engine_apis ([commit 523e2d2](https://github.com/googleapis/google-cloud-dotnet/commit/523e2d23624e0ed8565027843f2e7e48c2e76f5c))
  * Add VpcAccessConnector.egress_setting ([commit 523e2d2](https://github.com/googleapis/google-cloud-dotnet/commit/523e2d23624e0ed8565027843f2e7e48c2e76f5c))



## Version 1.3.0, released 2022-04-26

No API surface changes; just dependency updates.

## Version 1.2.0, released 2021-08-19

  * [Commit ac367e2](https://github.com/googleapis/google-cloud-dotnet/commit/ac367e2): feat: Regenerate all APIs to support self-signed JWTs



## Version 1.1.0, released 2021-04-29

  * [Commit c78b2f8](https://github.com/googleapis/google-cloud-dotnet/commit/c78b2f8):
    * feat: added vm_liveness, search_api_available, network_settings, service_account, build_env_variables, kms_key_reference to v1 API



## Version 1.0.0, released 2021-02-24

No API changes from 1.0.0-beta01.

## Version 1.0.0-beta01, released 2021-01-05

Initial release.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
