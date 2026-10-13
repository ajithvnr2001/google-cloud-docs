---
url: https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/group__google-cloud-aiplatform-options/
title: Vertex AI API Configuration Options (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:06:06.722168+00:00
---

# Vertex AI API Configuration Options (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/group__google-cloud-aiplatform-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Vertex AI API Configuration Options (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0 

# Vertex AI API Configuration Options

This library uses the same mechanism ([`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html)) and the common [options](https://docs.cloud.google.com/cpp/docs/reference/common/latest/group__options.html) as all other C++ client libraries for its configuration. Some `*Option` classes, which are only used in this library, are documented in this page.

###### See Also

[Client Library Configuration](https://docs.cloud.google.com/cpp/docs/reference/common/latest/group__options.html) \- for an overview of client library configuration. 

### Classes

  * [`google::cloud::aiplatform_v1::DatasetServiceRetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1DatasetServiceRetryPolicyOption)
  * [`google::cloud::aiplatform_v1::DatasetServiceBackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1DatasetServiceBackoffPolicyOption)
  * [`google::cloud::aiplatform_v1::DatasetServiceConnectionIdempotencyPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1DatasetServiceConnectionIdempotencyPolicyOption)
  * [`google::cloud::aiplatform_v1::DatasetServicePollingPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1DatasetServicePollingPolicyOption)
  * [`google::cloud::aiplatform_v1::DeploymentResourcePoolServiceRetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1DeploymentResourcePoolServiceRetryPolicyOption)
  * [`google::cloud::aiplatform_v1::DeploymentResourcePoolServiceBackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1DeploymentResourcePoolServiceBackoffPolicyOption)
  * [`google::cloud::aiplatform_v1::DeploymentResourcePoolServiceConnectionIdempotencyPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1DeploymentResourcePoolServiceConnectionIdempotencyPolicyOption)
  * [`google::cloud::aiplatform_v1::DeploymentResourcePoolServicePollingPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1DeploymentResourcePoolServicePollingPolicyOption)
  * [`google::cloud::aiplatform_v1::EndpointServiceRetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1EndpointServiceRetryPolicyOption)
  * [`google::cloud::aiplatform_v1::EndpointServiceBackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1EndpointServiceBackoffPolicyOption)
  * [`google::cloud::aiplatform_v1::EndpointServiceConnectionIdempotencyPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1EndpointServiceConnectionIdempotencyPolicyOption)
  * [`google::cloud::aiplatform_v1::EndpointServicePollingPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1EndpointServicePollingPolicyOption)
  * [`google::cloud::aiplatform_v1::EvaluationServiceRetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1EvaluationServiceRetryPolicyOption)
  * [`google::cloud::aiplatform_v1::EvaluationServiceBackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1EvaluationServiceBackoffPolicyOption)
  * [`google::cloud::aiplatform_v1::EvaluationServiceConnectionIdempotencyPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1EvaluationServiceConnectionIdempotencyPolicyOption)
  * [`google::cloud::aiplatform_v1::FeatureOnlineStoreAdminServiceRetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1FeatureOnlineStoreAdminServiceRetryPolicyOption)
  * [`google::cloud::aiplatform_v1::FeatureOnlineStoreAdminServiceBackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1FeatureOnlineStoreAdminServiceBackoffPolicyOption)
  * [`google::cloud::aiplatform_v1::FeatureOnlineStoreAdminServiceConnectionIdempotencyPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1FeatureOnlineStoreAdminServiceConnectionIdempotencyPolicyOption)
  * [`google::cloud::aiplatform_v1::FeatureOnlineStoreAdminServicePollingPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1FeatureOnlineStoreAdminServicePollingPolicyOption)
  * [`google::cloud::aiplatform_v1::FeatureOnlineStoreServiceRetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1FeatureOnlineStoreServiceRetryPolicyOption)
  * [`google::cloud::aiplatform_v1::FeatureOnlineStoreServiceBackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1FeatureOnlineStoreServiceBackoffPolicyOption)
  * [`google::cloud::aiplatform_v1::FeatureOnlineStoreServiceConnectionIdempotencyPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1FeatureOnlineStoreServiceConnectionIdempotencyPolicyOption)
  * [`google::cloud::aiplatform_v1::FeatureRegistryServiceRetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1FeatureRegistryServiceRetryPolicyOption)
  * [`google::cloud::aiplatform_v1::FeatureRegistryServiceBackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1FeatureRegistryServiceBackoffPolicyOption)
  * [`google::cloud::aiplatform_v1::FeatureRegistryServiceConnectionIdempotencyPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1FeatureRegistryServiceConnectionIdempotencyPolicyOption)
  * [`google::cloud::aiplatform_v1::FeatureRegistryServicePollingPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1FeatureRegistryServicePollingPolicyOption)
  * [`google::cloud::aiplatform_v1::FeaturestoreOnlineServingServiceRetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1FeaturestoreOnlineServingServiceRetryPolicyOption)
  * [`google::cloud::aiplatform_v1::FeaturestoreOnlineServingServiceBackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1FeaturestoreOnlineServingServiceBackoffPolicyOption)
  * [`google::cloud::aiplatform_v1::FeaturestoreOnlineServingServiceConnectionIdempotencyPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1FeaturestoreOnlineServingServiceConnectionIdempotencyPolicyOption)
  * [`google::cloud::aiplatform_v1::FeaturestoreServiceRetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1FeaturestoreServiceRetryPolicyOption)
  * [`google::cloud::aiplatform_v1::FeaturestoreServiceBackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1FeaturestoreServiceBackoffPolicyOption)
  * [`google::cloud::aiplatform_v1::FeaturestoreServiceConnectionIdempotencyPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1FeaturestoreServiceConnectionIdempotencyPolicyOption)
  * [`google::cloud::aiplatform_v1::FeaturestoreServicePollingPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1FeaturestoreServicePollingPolicyOption)
  * [`google::cloud::aiplatform_v1::GenAiTuningServiceRetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1GenAiTuningServiceRetryPolicyOption)
  * [`google::cloud::aiplatform_v1::GenAiTuningServiceBackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1GenAiTuningServiceBackoffPolicyOption)
  * [`google::cloud::aiplatform_v1::GenAiTuningServiceConnectionIdempotencyPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1GenAiTuningServiceConnectionIdempotencyPolicyOption)
  * [`google::cloud::aiplatform_v1::GenAiTuningServicePollingPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1GenAiTuningServicePollingPolicyOption)
  * [`google::cloud::aiplatform_v1::IndexEndpointServiceRetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1IndexEndpointServiceRetryPolicyOption)
  * [`google::cloud::aiplatform_v1::IndexEndpointServiceBackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1IndexEndpointServiceBackoffPolicyOption)
  * [`google::cloud::aiplatform_v1::IndexEndpointServiceConnectionIdempotencyPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1IndexEndpointServiceConnectionIdempotencyPolicyOption)
  * [`google::cloud::aiplatform_v1::IndexEndpointServicePollingPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1IndexEndpointServicePollingPolicyOption)
  * [`google::cloud::aiplatform_v1::IndexServiceRetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1IndexServiceRetryPolicyOption)
  * [`google::cloud::aiplatform_v1::IndexServiceBackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1IndexServiceBackoffPolicyOption)
  * [`google::cloud::aiplatform_v1::IndexServiceConnectionIdempotencyPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1IndexServiceConnectionIdempotencyPolicyOption)
  * [`google::cloud::aiplatform_v1::IndexServicePollingPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1IndexServicePollingPolicyOption)
  * [`google::cloud::aiplatform_v1::JobServiceRetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1JobServiceRetryPolicyOption)
  * [`google::cloud::aiplatform_v1::JobServiceBackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1JobServiceBackoffPolicyOption)
  * [`google::cloud::aiplatform_v1::JobServiceConnectionIdempotencyPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1JobServiceConnectionIdempotencyPolicyOption)
  * [`google::cloud::aiplatform_v1::JobServicePollingPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1JobServicePollingPolicyOption)
  * [`google::cloud::aiplatform_v1::LlmUtilityServiceRetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1LlmUtilityServiceRetryPolicyOption)
  * [`google::cloud::aiplatform_v1::LlmUtilityServiceBackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1LlmUtilityServiceBackoffPolicyOption)
  * [`google::cloud::aiplatform_v1::LlmUtilityServiceConnectionIdempotencyPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1LlmUtilityServiceConnectionIdempotencyPolicyOption)
  * [`google::cloud::aiplatform_v1::MatchServiceRetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1MatchServiceRetryPolicyOption)
  * [`google::cloud::aiplatform_v1::MatchServiceBackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1MatchServiceBackoffPolicyOption)
  * [`google::cloud::aiplatform_v1::MatchServiceConnectionIdempotencyPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1MatchServiceConnectionIdempotencyPolicyOption)
  * [`google::cloud::aiplatform_v1::MetadataServiceRetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1MetadataServiceRetryPolicyOption)
  * [`google::cloud::aiplatform_v1::MetadataServiceBackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1MetadataServiceBackoffPolicyOption)
  * [`google::cloud::aiplatform_v1::MetadataServiceConnectionIdempotencyPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1MetadataServiceConnectionIdempotencyPolicyOption)
  * [`google::cloud::aiplatform_v1::MetadataServicePollingPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1MetadataServicePollingPolicyOption)
  * [`google::cloud::aiplatform_v1::MigrationServiceRetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1MigrationServiceRetryPolicyOption)
  * [`google::cloud::aiplatform_v1::MigrationServiceBackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1MigrationServiceBackoffPolicyOption)
  * [`google::cloud::aiplatform_v1::MigrationServiceConnectionIdempotencyPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1MigrationServiceConnectionIdempotencyPolicyOption)
  * [`google::cloud::aiplatform_v1::MigrationServicePollingPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1MigrationServicePollingPolicyOption)
  * [`google::cloud::aiplatform_v1::ModelGardenServiceRetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1ModelGardenServiceRetryPolicyOption)
  * [`google::cloud::aiplatform_v1::ModelGardenServiceBackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1ModelGardenServiceBackoffPolicyOption)
  * [`google::cloud::aiplatform_v1::ModelGardenServiceConnectionIdempotencyPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1ModelGardenServiceConnectionIdempotencyPolicyOption)
  * [`google::cloud::aiplatform_v1::ModelGardenServicePollingPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1ModelGardenServicePollingPolicyOption)
  * [`google::cloud::aiplatform_v1::ModelServiceRetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1ModelServiceRetryPolicyOption)
  * [`google::cloud::aiplatform_v1::ModelServiceBackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1ModelServiceBackoffPolicyOption)
  * [`google::cloud::aiplatform_v1::ModelServiceConnectionIdempotencyPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1ModelServiceConnectionIdempotencyPolicyOption)
  * [`google::cloud::aiplatform_v1::ModelServicePollingPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1ModelServicePollingPolicyOption)
  * [`google::cloud::aiplatform_v1::NotebookServiceRetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1NotebookServiceRetryPolicyOption)
  * [`google::cloud::aiplatform_v1::NotebookServiceBackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1NotebookServiceBackoffPolicyOption)
  * [`google::cloud::aiplatform_v1::NotebookServiceConnectionIdempotencyPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1NotebookServiceConnectionIdempotencyPolicyOption)
  * [`google::cloud::aiplatform_v1::NotebookServicePollingPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1NotebookServicePollingPolicyOption)
  * [`google::cloud::aiplatform_v1::PersistentResourceServiceRetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1PersistentResourceServiceRetryPolicyOption)
  * [`google::cloud::aiplatform_v1::PersistentResourceServiceBackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1PersistentResourceServiceBackoffPolicyOption)
  * [`google::cloud::aiplatform_v1::PersistentResourceServiceConnectionIdempotencyPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1PersistentResourceServiceConnectionIdempotencyPolicyOption)
  * [`google::cloud::aiplatform_v1::PersistentResourceServicePollingPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1PersistentResourceServicePollingPolicyOption)
  * [`google::cloud::aiplatform_v1::PipelineServiceRetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1PipelineServiceRetryPolicyOption)
  * [`google::cloud::aiplatform_v1::PipelineServiceBackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1PipelineServiceBackoffPolicyOption)
  * [`google::cloud::aiplatform_v1::PipelineServiceConnectionIdempotencyPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1PipelineServiceConnectionIdempotencyPolicyOption)
  * [`google::cloud::aiplatform_v1::PipelineServicePollingPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1PipelineServicePollingPolicyOption)
  * [`google::cloud::aiplatform_v1::PredictionServiceRetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1PredictionServiceRetryPolicyOption)
  * [`google::cloud::aiplatform_v1::PredictionServiceBackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1PredictionServiceBackoffPolicyOption)
  * [`google::cloud::aiplatform_v1::PredictionServiceConnectionIdempotencyPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1PredictionServiceConnectionIdempotencyPolicyOption)
  * [`google::cloud::aiplatform_v1::ScheduleServiceRetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1ScheduleServiceRetryPolicyOption)
  * [`google::cloud::aiplatform_v1::ScheduleServiceBackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1ScheduleServiceBackoffPolicyOption)
  * [`google::cloud::aiplatform_v1::ScheduleServiceConnectionIdempotencyPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1ScheduleServiceConnectionIdempotencyPolicyOption)
  * [`google::cloud::aiplatform_v1::ScheduleServicePollingPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1ScheduleServicePollingPolicyOption)
  * [`google::cloud::aiplatform_v1::SpecialistPoolServiceRetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1SpecialistPoolServiceRetryPolicyOption)
  * [`google::cloud::aiplatform_v1::SpecialistPoolServiceBackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1SpecialistPoolServiceBackoffPolicyOption)
  * [`google::cloud::aiplatform_v1::SpecialistPoolServiceConnectionIdempotencyPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1SpecialistPoolServiceConnectionIdempotencyPolicyOption)
  * [`google::cloud::aiplatform_v1::SpecialistPoolServicePollingPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1SpecialistPoolServicePollingPolicyOption)
  * [`google::cloud::aiplatform_v1::TensorboardServiceRetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1TensorboardServiceRetryPolicyOption)
  * [`google::cloud::aiplatform_v1::TensorboardServiceBackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1TensorboardServiceBackoffPolicyOption)
  * [`google::cloud::aiplatform_v1::TensorboardServiceConnectionIdempotencyPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1TensorboardServiceConnectionIdempotencyPolicyOption)
  * [`google::cloud::aiplatform_v1::TensorboardServicePollingPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1TensorboardServicePollingPolicyOption)
  * [`google::cloud::aiplatform_v1::VizierServiceRetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1VizierServiceRetryPolicyOption)
  * [`google::cloud::aiplatform_v1::VizierServiceBackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1VizierServiceBackoffPolicyOption)
  * [`google::cloud::aiplatform_v1::VizierServiceConnectionIdempotencyPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1VizierServiceConnectionIdempotencyPolicyOption)
  * [`google::cloud::aiplatform_v1::VizierServicePollingPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/structgoogle_1_1cloud_1_1aiplatform__v1_1_1VizierServicePollingPolicyOption)



### Types

  * [`DatasetServicePolicyOptionList`](about:invalid#zCSafez)
  * [`DeploymentResourcePoolServicePolicyOptionList`](about:invalid#zCSafez)
  * [`EndpointServicePolicyOptionList`](about:invalid#zCSafez)
  * [`EvaluationServicePolicyOptionList`](about:invalid#zCSafez)
  * [`FeatureOnlineStoreAdminServicePolicyOptionList`](about:invalid#zCSafez)
  * [`FeatureOnlineStoreServicePolicyOptionList`](about:invalid#zCSafez)
  * [`FeatureRegistryServicePolicyOptionList`](about:invalid#zCSafez)
  * [`FeaturestoreOnlineServingServicePolicyOptionList`](about:invalid#zCSafez)
  * [`FeaturestoreServicePolicyOptionList`](about:invalid#zCSafez)
  * [`GenAiTuningServicePolicyOptionList`](about:invalid#zCSafez)
  * [`IndexEndpointServicePolicyOptionList`](about:invalid#zCSafez)
  * [`IndexServicePolicyOptionList`](about:invalid#zCSafez)
  * [`JobServicePolicyOptionList`](about:invalid#zCSafez)
  * [`LlmUtilityServicePolicyOptionList`](about:invalid#zCSafez)
  * [`MatchServicePolicyOptionList`](about:invalid#zCSafez)
  * [`MetadataServicePolicyOptionList`](about:invalid#zCSafez)
  * [`MigrationServicePolicyOptionList`](about:invalid#zCSafez)
  * [`ModelGardenServicePolicyOptionList`](about:invalid#zCSafez)
  * [`ModelServicePolicyOptionList`](about:invalid#zCSafez)
  * [`NotebookServicePolicyOptionList`](about:invalid#zCSafez)
  * [`PersistentResourceServicePolicyOptionList`](about:invalid#zCSafez)
  * [`PipelineServicePolicyOptionList`](about:invalid#zCSafez)
  * [`PredictionServicePolicyOptionList`](about:invalid#zCSafez)
  * [`ScheduleServicePolicyOptionList`](about:invalid#zCSafez)
  * [`SpecialistPoolServicePolicyOptionList`](about:invalid#zCSafez)
  * [`TensorboardServicePolicyOptionList`](about:invalid#zCSafez)
  * [`VizierServicePolicyOptionList`](about:invalid#zCSafez)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
