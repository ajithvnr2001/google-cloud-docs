---
url: https://docs.cloud.google.com/cpp/docs/reference/discoveryengine/latest/discoveryengine-env/
title: Environment Variables \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:44:06.223084+00:00
---

# Environment Variables  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/discoveryengine/latest/discoveryengine-env/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Environment Variables Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1 

A number of environment variables can be used to configure the behavior of the library. There are also functions to configure this behavior in code. The environment variables are convenient when troubleshooting problems.

## Endpoint Overrides

  * `GOOGLE_CLOUD_CPP_COMPLETION_SERVICE_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "discoveryengine.googleapis.com") used by `MakeCompletionServiceConnection()`.
  * `GOOGLE_CLOUD_CPP_CONTROL_SERVICE_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "discoveryengine.googleapis.com") used by `MakeControlServiceConnection()`.
  * `GOOGLE_CLOUD_CPP_CONVERSATIONAL_SEARCH_SERVICE_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "discoveryengine.googleapis.com") used by `MakeConversationalSearchServiceConnection()`.
  * `GOOGLE_CLOUD_CPP_DATA_STORE_SERVICE_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "discoveryengine.googleapis.com") used by `MakeDataStoreServiceConnection()`.
  * `GOOGLE_CLOUD_CPP_DOCUMENT_SERVICE_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "discoveryengine.googleapis.com") used by `MakeDocumentServiceConnection()`.
  * `GOOGLE_CLOUD_CPP_ENGINE_SERVICE_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "discoveryengine.googleapis.com") used by `MakeEngineServiceConnection()`.
  * `GOOGLE_CLOUD_CPP_GROUNDED_GENERATION_SERVICE_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "discoveryengine.googleapis.com") used by `MakeGroundedGenerationServiceConnection()`.
  * `GOOGLE_CLOUD_CPP_PROJECT_SERVICE_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "discoveryengine.googleapis.com") used by `MakeProjectServiceConnection()`.
  * `GOOGLE_CLOUD_CPP_RANK_SERVICE_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "discoveryengine.googleapis.com") used by `MakeRankServiceConnection()`.
  * `GOOGLE_CLOUD_CPP_RECOMMENDATION_SERVICE_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "discoveryengine.googleapis.com") used by `MakeRecommendationServiceConnection()`.
  * `GOOGLE_CLOUD_CPP_SCHEMA_SERVICE_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "discoveryengine.googleapis.com") used by `MakeSchemaServiceConnection()`.
  * `GOOGLE_CLOUD_CPP_SEARCH_SERVICE_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "discoveryengine.googleapis.com") used by `MakeSearchServiceConnection()`.
  * `GOOGLE_CLOUD_CPP_SITE_SEARCH_ENGINE_SERVICE_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "discoveryengine.googleapis.com") used by `MakeSiteSearchEngineServiceConnection()`.
  * `GOOGLE_CLOUD_CPP_USER_EVENT_SERVICE_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "discoveryengine.googleapis.com") used by `MakeUserEventServiceConnection()`.



###### See Also

[`google::cloud::EndpointOption`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1EndpointOption.html)

## Logging

`GOOGLE_CLOUD_CPP_ENABLE_TRACING=rpc`: turns on tracing for most gRPC calls. The library injects an additional Stub decorator that prints each gRPC request and response. Unless you have configured your own logging backend, you should also set `GOOGLE_CLOUD_CPP_ENABLE_CLOG` to produce any output on the program's console.

###### See Also

[`google::cloud::LoggingComponentsOption`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1LoggingComponentsOption.html)`GOOGLE_CLOUD_CPP_TRACING_OPTIONS=...`: modifies the behavior of gRPC tracing, including whether messages will be output on multiple lines, or whether string/bytes fields will be truncated.

###### See Also

[`google::cloud::GrpcTracingOptionsOption`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1GrpcTracingOptionsOption.html)`GOOGLE_CLOUD_CPP_ENABLE_CLOG=yes`: turns on logging in the library, basically the library always "logs" but the logging infrastructure has no backend to actually print anything until the application sets a backend or they set this environment variable.

###### See Also

[`google::cloud::LogBackend`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1LogBackend.html)

###### See Also

[`google::cloud::LogSink`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1LogSink.html)

## Setting the Default Project

`GOOGLE_CLOUD_PROJECT=...`: is used in examples and integration tests to configure the GCP project. This has no effect in the library. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
