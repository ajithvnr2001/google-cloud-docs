---
url: https://docs.cloud.google.com/cpp/docs/reference/dialogflow_es/latest/dialogflow_es-override-universe-domain/
title: How to Override the Default Universe Domain \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:34:09.334811+00:00
---

# How to Override the Default Universe Domain  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/dialogflow_es/latest/dialogflow_es-override-universe-domain/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  How to Override the Default Universe Domain Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

In some cases, you may need to override the default universe domain used by the client library. Use `AddUniverseDomainOption` when initializing the client library to change this default.

For example, this will override the default universe domain for `dialogflow_es::AgentsClient`:
    
    
      google::cloud::Options options;
    
      // AddUniverseDomainOption interrogates the UnifiedCredentialsOption, if set,
      // in the provided Options for the Universe Domain associated with the
      // credentials and adds it to the set of Options.
      // If no UnifiedCredentialsOption is set, GoogleDefaultCredentials are used.
      auto ud_options = google::cloud::AddUniverseDomainOption(std::move(options));
    
      if (!ud_options.ok()) throw std::move(ud_options).status();
      auto ud_client = google::cloud::dialogflow_es::AgentsClient(
          google::cloud::dialogflow_es::MakeAgentsConnection(*ud_options));
    

Follow these links to find examples for other `*Client` classes:

  * [`dialogflow_es::AgentsClient`](https://docs.cloud.google.com/cpp/docs/reference/dialogflow_es/latest/dialogflow_es_1_1AgentsClient-universe-domain-snippet)
  * [`dialogflow_es::AnswerRecordsClient`](https://docs.cloud.google.com/cpp/docs/reference/dialogflow_es/latest/dialogflow_es_1_1AnswerRecordsClient-universe-domain-snippet)
  * [`dialogflow_es::ContextsClient`](https://docs.cloud.google.com/cpp/docs/reference/dialogflow_es/latest/dialogflow_es_1_1ContextsClient-universe-domain-snippet)
  * [`dialogflow_es::ConversationDatasetsClient`](https://docs.cloud.google.com/cpp/docs/reference/dialogflow_es/latest/dialogflow_es_1_1ConversationDatasetsClient-universe-domain-snippet)
  * [`dialogflow_es::ConversationModelsClient`](https://docs.cloud.google.com/cpp/docs/reference/dialogflow_es/latest/dialogflow_es_1_1ConversationModelsClient-universe-domain-snippet)
  * [`dialogflow_es::ConversationProfilesClient`](https://docs.cloud.google.com/cpp/docs/reference/dialogflow_es/latest/dialogflow_es_1_1ConversationProfilesClient-universe-domain-snippet)
  * [`dialogflow_es::ConversationsClient`](https://docs.cloud.google.com/cpp/docs/reference/dialogflow_es/latest/dialogflow_es_1_1ConversationsClient-universe-domain-snippet)
  * [`dialogflow_es::DocumentsClient`](https://docs.cloud.google.com/cpp/docs/reference/dialogflow_es/latest/dialogflow_es_1_1DocumentsClient-universe-domain-snippet)
  * [`dialogflow_es::EncryptionSpecServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/dialogflow_es/latest/dialogflow_es_1_1EncryptionSpecServiceClient-universe-domain-snippet)
  * [`dialogflow_es::EntityTypesClient`](https://docs.cloud.google.com/cpp/docs/reference/dialogflow_es/latest/dialogflow_es_1_1EntityTypesClient-universe-domain-snippet)
  * [`dialogflow_es::EnvironmentsClient`](https://docs.cloud.google.com/cpp/docs/reference/dialogflow_es/latest/dialogflow_es_1_1EnvironmentsClient-universe-domain-snippet)
  * [`dialogflow_es::FulfillmentsClient`](https://docs.cloud.google.com/cpp/docs/reference/dialogflow_es/latest/dialogflow_es_1_1FulfillmentsClient-universe-domain-snippet)
  * [`dialogflow_es::GeneratorsClient`](https://docs.cloud.google.com/cpp/docs/reference/dialogflow_es/latest/dialogflow_es_1_1GeneratorsClient-universe-domain-snippet)
  * [`dialogflow_es::IntentsClient`](https://docs.cloud.google.com/cpp/docs/reference/dialogflow_es/latest/dialogflow_es_1_1IntentsClient-universe-domain-snippet)
  * [`dialogflow_es::KnowledgeBasesClient`](https://docs.cloud.google.com/cpp/docs/reference/dialogflow_es/latest/dialogflow_es_1_1KnowledgeBasesClient-universe-domain-snippet)
  * [`dialogflow_es::ParticipantsClient`](https://docs.cloud.google.com/cpp/docs/reference/dialogflow_es/latest/dialogflow_es_1_1ParticipantsClient-universe-domain-snippet)
  * [`dialogflow_es::SessionEntityTypesClient`](https://docs.cloud.google.com/cpp/docs/reference/dialogflow_es/latest/dialogflow_es_1_1SessionEntityTypesClient-universe-domain-snippet)
  * [`dialogflow_es::SessionsClient`](https://docs.cloud.google.com/cpp/docs/reference/dialogflow_es/latest/dialogflow_es_1_1SessionsClient-universe-domain-snippet)
  * [`dialogflow_es::VersionsClient`](https://docs.cloud.google.com/cpp/docs/reference/dialogflow_es/latest/dialogflow_es_1_1VersionsClient-universe-domain-snippet)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
