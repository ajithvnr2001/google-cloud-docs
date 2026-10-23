---
url: https://docs.cloud.google.com/apis/design/directory_structure/
title: Directory structure \u00a0|\u00a0 Cloud API Design Guide \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:00.851619+00:00
---

# Directory structure  |  Cloud API Design Guide  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apis/design/directory_structure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud APIs ](https://docs.cloud.google.com/apis/docs/overview)
  * [ Cloud API Design Guide ](https://docs.cloud.google.com/apis/design)



Send feedback 

#  Directory structure Stay organized with collections  Save and categorize content based on your preferences. 

A typical API directory contains `.proto` files, which define the API surface, and `.yaml` files, which configure the API service. Using this layout helps you maintain consistent service configurations and versioned interfaces across environments. Each API service **must** have an API directory inside an API repository, and the API directory **should** contain all API definition files and build scripts.

Each API directory **should** have the following standard layout:

  * API directory

    * Repository prerequisites

      * `BUILD` \- The build file.
      * `METADATA` \- The build metadata file.
      * `OWNERS` \- The API directory owners.
      * `README.md` \- The general information about the API service.
    * Configuration files

      * `{service}.yaml` \- The baseline service config file, which is the YAML representation of the `google.api.Service` proto message.
      * `prod.yaml` \- The prod delta service config file.
      * `staging.yaml` \- The staging delta service config file.
      * `test.yaml` \- The test delta service config file.
      * `local.yaml` \- The local delta service config file.
    * Documentation files

      * `doc/*` \- The technical documentation files. They should be in Markdown format.
    * Interface definitions

      * `v[0-9]*/*` \- Each such directory contains a major version of the API, mainly the proto files and build scripts.
      * `{subapi}/v[0-9]*/*` \- Each `{subapi}` directory contains interface definition of a sub-API. Each sub-API may have its own independent major version.
      * `type/*` \- proto files containing types that are shared between different APIs, different versions of the same API, or between the API and service implementation. Type definitions under `type/*` **should** not have breaking changes once they are released.



Public Google API definitions are published on GitHub, see [Google APIs](https://github.com/googleapis/googleapis) repository.

**Note:** If you are a [Cloud Endpoints](https://docs.cloud.google.com/endpoints) developer, you can follow [Configuring a gRPC service](https://docs.cloud.google.com/endpoints/docs/grpc/grpc-service-config) to configure your API service.

[ Previous arrow_back  Introduction  ](https://docs.cloud.google.com/apis/design)

[ Next Changelog  arrow_forward  ](https://docs.cloud.google.com/apis/design/changelog)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
