---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/responsible-ai/
title: Responsible AI \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:45.123428+00:00
---

# Responsible AI  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/responsible-ai/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Responsible AI Stay organized with collections  Save and categorize content based on your preferences. 

Agent Search lets developers tap into the power of Google's foundation models, search expertise, and conversational AI technologies to create enterprise-grade generative AI applications. As an early-stage technology, its evolving capabilities and uses create potential for misapplication, misuse, and unintended or unforeseen consequences. For example, Agent Search can generate output that you don't expect, including text that's offensive, insensitive, or factually incorrect.

Given these risks and complexities, Agent Search is designed with Google's [AI Principles](https://ai.google/principles/) in mind. However, it is important for developers to understand and test their models to deploy safely and responsibly. To aid developers, Agent Search has built-in safety filters to help customers block potentially harmful outputs within their use case. For more information, see Safety settings for Agent Search.

When Agent Search is integrated into a customer's unique use case and context, additional responsible AI considerations and model limitations might need to be considered. We encourage customers to exercise fairness, interpretability, privacy, and security [recommended practices](https://ai.google/responsibilities/responsible-ai-practices/).

## Safety settings for Agent Search

Agent Search offers SafeSearch filters to filter explicit website search results. Explicit results might include content like pornography, violence, and gore. SafeSearch filtering is not available for private content.

Summarization (both for website search and private content) filters out responses such as derogatory, sexually explicit, toxic, or violent information. Additionally, the summarization response contains safety attributes, which include "harmful categories" and topics that might be considered sensitive.

### Website search

SafeSearch can be applied to public content indexed by Agent Search, such as [websites](https://docs.cloud.google.com/generative-ai-app-builder/docs/enterprise-search-introduction#websites). When SafeSearch is on, Agent Search helps filter out explicit content in a customer's Agent Search results for all queries across images, videos, and websites. While those filters are not 100% accurate, we continuously evaluate and update filtering capabilities.

In certain contexts and use cases, customers might require access to a wide range of information, even if it includes explicit content, to gather comprehensive insights and results from Agent Search. Customers can enable and disable safety filters using the API by setting `safe_search` to "true" or "false".

To enable SafeSearch for Agent Search, use the following API call:
    
    
    curl -X POST\
     -H "Authorization: Bearer $(gcloud auth application-default print-access-token)"
     -H "Content-Type: application/json"\
    "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/servingConfigs/default_config:search"
         -d '{
          "query": { "input": "FREE_TEXT"},
      "serving_config": "SERVING_CONFIG_ID",
      "safe_search": "true",
    }'
    

To enable SafeSearch for Search with follow-ups in Agent Search, use the following API call:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/conversations/CONVERSATION_ID:converse" \
    -d '{
      "query": { "input": "FREE_TEXT"},
      "serving_config": "SERVING_CONFIG_ID",
      "safe_search": "true",
    }'
    

The `safe_search` setting applies to search results and also to Agent Search outputs like summarization (which is based on the search results).

Agent Search outputs, such as summarization, are assessed against a list of safety attributes which filter potentially harmful content even when `safe_search` is turned off.

### Summarization for private content and website search

Agent Search outputs, such as summarization, are assessed against a list of safety attributes, which filters potentially harmful content such as derogatory, sexually explicit, toxic, or violent information, even when `safe_search` for website search is turned off. Additionally, you can filter out responses which include "harmful categories" and topics that might be considered sensitive by using `safetyAttributes` in the Agent Search API response.

### Fallback responses

If the summarization model responds to a request with an empty string or a generic response, it means that either the input or the output is triggering a safety filter. In the Agent Search API response, `SummarySkippedReason` is set to `BLOCKED_DUE_TO_POTENTIAL_POLICY_VIOLATION` if a potential policy violation is detected.

If you think that a safety filter is being inappropriately triggered, [report this issue](https://docs.cloud.google.com/support/docs/issue-trackers) using the Google Cloud console.

## Additional resources

  * Learn more about Google's recommendations for [Responsible AI practices](https://ai.google/responsibility/responsible-ai-practices/)
  * Read our blog, [A shared agenda for responsible AI progress](https://blog.google/technology/ai/a-shared-agenda-for-responsible-ai-progress/)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
