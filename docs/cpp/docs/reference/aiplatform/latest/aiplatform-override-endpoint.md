---
url: https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/aiplatform-override-endpoint/
title: How to Override the Default Endpoint \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:05:22.899234+00:00
---

# How to Override the Default Endpoint  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/aiplatform-override-endpoint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  How to Override the Default Endpoint Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0 

In some cases, you may need to override the default endpoint used by the client library. Use the [EndpointOption](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1EndpointOption.html) when initializing the client library to change this default.

For example, this will override the default endpoint for `aiplatform_v1::DatasetServiceClient`:
    
    
      // This configuration is common with Private Google Access:
      //     https://cloud.google.com/vpc/docs/private-google-access
      auto options = google::cloud::Options{}.set<google::cloud::EndpointOption>(
          "private.googleapis.com");
      auto vpc_client = google::cloud::aiplatform_v1::DatasetServiceClient(
          google::cloud::aiplatform_v1::MakeDatasetServiceConnection("unused",
                                                                     options));
    

Follow these links to find examples for other `*Client` classes:

  * [`aiplatform_v1::DatasetServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/aiplatform_v1_1_1DatasetServiceClient-endpoint-snippet)
  * [`aiplatform_v1::DeploymentResourcePoolServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/aiplatform_v1_1_1DeploymentResourcePoolServiceClient-endpoint-snippet)
  * [`aiplatform_v1::EndpointServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/aiplatform_v1_1_1EndpointServiceClient-endpoint-snippet)
  * [`aiplatform_v1::EvaluationServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/aiplatform_v1_1_1EvaluationServiceClient-endpoint-snippet)
  * [`aiplatform_v1::FeatureOnlineStoreAdminServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/aiplatform_v1_1_1FeatureOnlineStoreAdminServiceClient-endpoint-snippet)
  * [`aiplatform_v1::FeatureOnlineStoreServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/aiplatform_v1_1_1FeatureOnlineStoreServiceClient-endpoint-snippet)
  * [`aiplatform_v1::FeatureRegistryServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/aiplatform_v1_1_1FeatureRegistryServiceClient-endpoint-snippet)
  * [`aiplatform_v1::FeaturestoreServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/aiplatform_v1_1_1FeaturestoreServiceClient-endpoint-snippet)
  * [`aiplatform_v1::FeaturestoreOnlineServingServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/aiplatform_v1_1_1FeaturestoreOnlineServingServiceClient-endpoint-snippet)
  * [`aiplatform_v1::GenAiTuningServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/aiplatform_v1_1_1GenAiTuningServiceClient-endpoint-snippet)
  * [`aiplatform_v1::IndexServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/aiplatform_v1_1_1IndexServiceClient-endpoint-snippet)
  * [`aiplatform_v1::IndexEndpointServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/aiplatform_v1_1_1IndexEndpointServiceClient-endpoint-snippet)
  * [`aiplatform_v1::JobServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/aiplatform_v1_1_1JobServiceClient-endpoint-snippet)
  * [`aiplatform_v1::LlmUtilityServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/aiplatform_v1_1_1LlmUtilityServiceClient-endpoint-snippet)
  * [`aiplatform_v1::MatchServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/aiplatform_v1_1_1MatchServiceClient-endpoint-snippet)
  * [`aiplatform_v1::MetadataServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/aiplatform_v1_1_1MetadataServiceClient-endpoint-snippet)
  * [`aiplatform_v1::MigrationServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/aiplatform_v1_1_1MigrationServiceClient-endpoint-snippet)
  * [`aiplatform_v1::ModelServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/aiplatform_v1_1_1ModelServiceClient-endpoint-snippet)
  * [`aiplatform_v1::ModelGardenServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/aiplatform_v1_1_1ModelGardenServiceClient-endpoint-snippet)
  * [`aiplatform_v1::NotebookServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/aiplatform_v1_1_1NotebookServiceClient-endpoint-snippet)
  * [`aiplatform_v1::PersistentResourceServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/aiplatform_v1_1_1PersistentResourceServiceClient-endpoint-snippet)
  * [`aiplatform_v1::PipelineServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/aiplatform_v1_1_1PipelineServiceClient-endpoint-snippet)
  * [`aiplatform_v1::PredictionServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/aiplatform_v1_1_1PredictionServiceClient-endpoint-snippet)
  * [`aiplatform_v1::ScheduleServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/aiplatform_v1_1_1ScheduleServiceClient-endpoint-snippet)
  * [`aiplatform_v1::SpecialistPoolServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/aiplatform_v1_1_1SpecialistPoolServiceClient-endpoint-snippet)
  * [`aiplatform_v1::TensorboardServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/aiplatform_v1_1_1TensorboardServiceClient-endpoint-snippet)
  * [`aiplatform_v1::VizierServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/aiplatform_v1_1_1VizierServiceClient-endpoint-snippet)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
