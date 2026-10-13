---
url: https://docs.cloud.google.com/cpp/docs/reference/apiregistry/latest/apiregistry_v1_1_1CloudApiRegistryClient-universe-domain-snippet/
title: Override apiregistry_v1::CloudApiRegistryClient Universe Domain \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:50:47.941860+00:00
---

# Override apiregistry_v1::CloudApiRegistryClient Universe Domain  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/apiregistry/latest/apiregistry_v1_1_1CloudApiRegistryClient-universe-domain-snippet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Override apiregistry_v1::CloudApiRegistryClient Universe Domain Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1 
    
    
      google::cloud::Options options;
    
      // AddUniverseDomainOption interrogates the UnifiedCredentialsOption, if set,
      // in the provided Options for the Universe Domain associated with the
      // credentials and adds it to the set of Options.
      // If no UnifiedCredentialsOption is set, GoogleDefaultCredentials are used.
      auto ud_options = google::cloud::AddUniverseDomainOption(std::move(options));
    
      if (!ud_options.ok()) throw std::move(ud_options).status();
      auto ud_client = google::cloud::apiregistry_v1::CloudApiRegistryClient(
          google::cloud::apiregistry_v1::MakeCloudApiRegistryConnection(
              *ud_options));
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
