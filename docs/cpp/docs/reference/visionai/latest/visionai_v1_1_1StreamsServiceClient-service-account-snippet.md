---
url: https://docs.cloud.google.com/cpp/docs/reference/visionai/latest/visionai_v1_1_1StreamsServiceClient-service-account-snippet/
title: Override visionai_v1::StreamsServiceClient Authentication Defaults \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:44.526854+00:00
---

# Override visionai_v1::StreamsServiceClient Authentication Defaults  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/visionai/latest/visionai_v1_1_1StreamsServiceClient-service-account-snippet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Override visionai_v1::StreamsServiceClient Authentication Defaults Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0 
    
    
      [](std::string const& keyfile) {
        auto is = std::ifstream(keyfile);
        is.exceptions(std::ios::badbit);  // Minimal error handling in examples
        auto contents = std::string(std::istreambuf_iterator<char>(is.rdbuf()), {});
        auto options =
            google::cloud::Options{}.set<google::cloud::UnifiedCredentialsOption>(
                google::cloud::MakeServiceAccountCredentials(contents));
        return google::cloud::visionai_v1::StreamsServiceClient(
            google::cloud::visionai_v1::MakeStreamsServiceConnection(options));
      }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
