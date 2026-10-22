---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/smart-compose-best-practices/
title: Best practices: Smart compose \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:11.779032+00:00
---

# Best practices: Smart compose  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/smart-compose-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Best practices: Smart compose Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** This feature is no longer supported. For an alternative, use [smart reply](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/smart-reply).

This page outlines best practices for using the Agent Assist smart compose feature. See the smart compose [How-to guide](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/smart-compose) for more information on implementing this feature by calling the API directly, or the [console tutorial](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/smart-compose-console) for instructions about implementing this feature using the [Agent Assist console](https://agentassist.cloud.google.com).

## Terminology

Smart compose uses the following terms.

### Suggestion base text

This section defines the terminology used for Agent Assist.

A suggestion's **base text** is the partially-typed text that Smart Compose uses to generate the suggestion for completed text. This is the text in the `current_text_input.text` of [`SuggestSmartComposeAnswersRequest`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversations.participants.suggestions).

**Example:** If the human agent types "Ho", one possible suggestion could be "how are you". In this case, "Ho" is the **base text** and "how are you" is the suggestion.

### Suggestion extended text

A suggestion's **extended text** is constructed by merging the suggestion with its base text. If the base text contains a suffix that matches a prefix of the suggestion, the matched part will be merged. Smart Compose matches suffixes and prefixes in a case-insensitive way. To avoid false negatives, we recommend that you only show a suggestion when it has a non-empty prefix that matches a suffix in the base text.

**Example:** If the base text is "Ho" and the suggestion is "how are you", the suggestion **extended text** would be "How are you".

### Available Suggestion

A suggestion is an **available** suggestion if:

  1. The suggestion's base text is a prefix of the already-typed text.
  2. The typed text is a prefix of, but is not equal to, the suggestion's extended text.



**Example:** The suggestion "how are you" with base text "Ho" is an **available suggestion** when the already-typed text is "how a", but it's not an available suggestion when the already-typed text is "h" or "how are you".

## Requesting a suggestion

We suggest that you have your server send a [`suggestSmartComposeAnswers`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversations.participants.suggestions) request on every new character unless that character is already covered by an available suggestion. This increases the probability of generating Smart Compose suggestions. Be aware that this might generate a high qps: If you see that the requests are being throttled because of quota limits, please contact Google to discuss a solution. When constructing a request, consider setting `max_results`=3 to increase the number of suggestions retrieved.

## Selecting a suggestion

Selecting a suggestion is a critical functionality that must be implemented before you can implement Smart Compose on an agent UI. Typing can be rapid and there is some latency to any Smart Compose suggestion. Therefore, the suggestions might not be valid by the time they reach the agent UI. To minimize this issue, we recommend rendering only a subset of available suggestions to the UI. For a given typed text, a suggestion should be selected if:

  1. It's an available suggestion for the typed text.
  2. Its base text has the largest number of characters among all available suggestions.
  3. If there are multiple suggestions that have the same longest base text, choose the option with the highest suggestion rank.



**Example workflow:**

  1. An agent types "Ho".
  2. A request is sent with the current message "Ho".
  3. The agent continued typing "How".
  4. The suggestion {"Hope you", "how are you", "How are you doing today?"} (based on the original entry "Ho") reaches the agent UI.
  5. In this case "Hope you" is not a valid suggestion anymore, because the agent has typed a different word. Instead, "how are you" should be suggested.



## Caching

We recommend that you implement caching as a key-value map, with the prefix as the key and the suggestions returned by the API as the value. The map should be checked for a key that matches the agent input. If the map does not contain a matching key, characters should be removed from the end of the agent input one at a time, with the map being checked at every iteration. This should continue until either a matching suggestion is found, there are no more characters left to remove from the agent input, or an iteration limit is reached (50 iterations is a reasonable number). When the matching key is found, the suggestions should be iterated over. To determine if a suggestion is valid, the key (substring of prefix) and suggestion are merged, then checked against the agent input. The merged suggestion and agent input should overlap completely starting from the first characters. If they don't, the next suggestion should be checked.

**An example using caching:**

  1. "Agent" types "H".
  2. The key-value map is checked for suggestions for the prefix "H". There are none, and there are no more characters to remove from the end of the input, so a request for suggestions for "H" is made.
  3. "Agent" continues to type "Ho".
  4. The key-value map is checked for suggestions for the prefix "Ho". There are none, the key-value map is checked for suggestions for the prefix "H". There are none, and there are no more characters to remove from the end of the input, so a request for suggestions for "Ho" is made.
  5. A response with no suggestions is received from the request sent in Step 2, and the response is added to the cache for the key "H".
  6. A response with the suggestions {"Hope you", "how are you", "How are you doing today?"} is received from the request sent in Step 4, and the suggestions are added to the cache for the key "Ho".
  7. The key-value map is checked for suggestions for the prefix "Ho", there are suggestions. The suggestions are looped, with the key and suggestion being merged and checked against the "Agent" input. The "Agent" input "Ho" overlaps the first suggestion "Hope you", so the suggestion "pe you" is shown to the agent.
  8. "Agent" continues to type "How".
  9. The key-value map is checked for suggestions for the prefix "How". There are no suggestions, the key-value map is checked for suggestions for the prefix "Ho", there are suggestions. The suggestions are looped, with the key and suggestion being merged and checked against the "Agent" input. The "Agent" input "How" overlaps the first suggestion "how are you", so the suggestion " are you" is shown to the agent.

**Note:** Caching trades some quality for suggestion experience. In practice, we find that the caching mechanism can improve the overall experience of this feature.

## Conversation history

Smart Compose relies on conversation history to work correctly. If you are using Smart Reply or any other Agent Assist features through the [`analyzeContent` API](https://docs.cloud.google.com/dialogflow/priv/docs/reference/rest/v2beta1/projects.conversations.participants/analyzeContent), you should already be covered. Otherwise, you need to call the `analyzeContent` API on every completed message before using `suggestSmartComposeAnswers` to get smart compose suggestions. See the [Smart Compose How-to guide](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/priv/smart-compose) for more details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
