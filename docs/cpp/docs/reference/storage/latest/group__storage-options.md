---
url: https://docs.cloud.google.com/cpp/docs/reference/storage/latest/group__storage-options/
title: GCS Client Library Configuration Options (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:54:38.210460+00:00
---

# GCS Client Library Configuration Options (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/storage/latest/group__storage-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  GCS Client Library Configuration Options (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

# GCS Client Library Configuration Options

The GCS client library uses the same mechanism as all other C++ client libraries for configuration. As usual for the C++ client libraries, it adds a number of unique options only applicable for the GCS library.

###### See Also

[Client Library Configuration](https://docs.cloud.google.com/cpp/docs/reference/common/latest/group__options.html) \- for an overview of client library configuration. 

### Classes

  * [`google::cloud::storage::PrecomputedChecksums`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage_1_1PrecomputedChecksums)
  * [`google::cloud::storage_experimental::EnableReadHedgingOption`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage__experimental_1_1EnableReadHedgingOption)
  * [`google::cloud::storage_experimental::ReadHedgeRateLimitOption`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage__experimental_1_1ReadHedgeRateLimitOption)
  * [`google::cloud::storage_experimental::MaxConcurrentHedgesOption`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage__experimental_1_1MaxConcurrentHedgesOption)
  * [`google::cloud::storage_experimental::MaxTotalHedgesOption`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage__experimental_1_1MaxTotalHedgesOption)
  * [`google::cloud::storage_experimental::MaximumHedgeBufferOption`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage__experimental_1_1MaximumHedgeBufferOption)
  * [`google::cloud::storage_experimental::ReadHedgeDelayOption`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage__experimental_1_1ReadHedgeDelayOption)
  * [`google::cloud::storage_experimental::MaxReadHedgesOption`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage__experimental_1_1MaxReadHedgesOption)
  * [`google::cloud::storage_experimental::ReadThreadPoolSizeOption`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage__experimental_1_1ReadThreadPoolSizeOption)
  * [`google::cloud::storage_experimental::HedgingThreadPoolSizeOption`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage__experimental_1_1HedgingThreadPoolSizeOption)
  * [`google::cloud::storage_experimental::HttpVersionOption`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage__experimental_1_1HttpVersionOption)
  * [`google::cloud::storage_experimental::OTelSpanEnrichmentOption`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage__experimental_1_1OTelSpanEnrichmentOption)
  * [`google::cloud::storage_experimental::HttpConnectTimeoutOption`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage__experimental_1_1HttpConnectTimeoutOption)
  * [`google::cloud::storage::UploadChecksumValidationOption`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage_1_1UploadChecksumValidationOption)
  * [`google::cloud::storage::DownloadChecksumValidationOption`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage_1_1DownloadChecksumValidationOption)
  * [`google::cloud::storage::PrecomputedChecksumsOption`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage_1_1PrecomputedChecksumsOption)
  * [`google::cloud::storage::RestEndpointOption`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage_1_1RestEndpointOption)
  * [`google::cloud::storage::IamEndpointOption`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage_1_1IamEndpointOption)
  * [`google::cloud::storage::ProjectIdOption`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage_1_1ProjectIdOption)
  * [`google::cloud::storage::ConnectionPoolSizeOption`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage_1_1ConnectionPoolSizeOption)
  * [`google::cloud::storage::DownloadBufferSizeOption`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage_1_1DownloadBufferSizeOption)
  * [`google::cloud::storage::UploadBufferSizeOption`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage_1_1UploadBufferSizeOption)
  * [`google::cloud::storage::MaximumSimpleUploadSizeOption`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage_1_1MaximumSimpleUploadSizeOption)
  * [`google::cloud::storage::TransferStallTimeoutOption`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage_1_1TransferStallTimeoutOption)
  * [`google::cloud::storage::TransferStallMinimumRateOption`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage_1_1TransferStallMinimumRateOption)
  * [`google::cloud::storage::DownloadStallTimeoutOption`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage_1_1DownloadStallTimeoutOption)
  * [`google::cloud::storage::DownloadStallMinimumRateOption`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage_1_1DownloadStallMinimumRateOption)
  * [`google::cloud::storage::RetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage_1_1RetryPolicyOption)
  * [`google::cloud::storage::BackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage_1_1BackoffPolicyOption)
  * [`google::cloud::storage::IdempotencyPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage_1_1IdempotencyPolicyOption)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
