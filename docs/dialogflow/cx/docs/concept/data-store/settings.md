---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/settings/
title: Data store tool settings \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:17.281339+00:00
---

# Data store tool settings  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/settings/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Data store tool settings Stay organized with collections  Save and categorize content based on your preferences. 

You can configure the following [data store tool](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/handler) settings.

## Tool settings (Conversational Agents console only)

Selecting an option from the **Tool settings** list automatically affects which other tool configurations are available.

The `Default` and `Optimized for voice` options are default settings that automatically configure all other parameters in the tool configuration menu.

The following options are available:

Tool Settings | Description  
---|---  
Default | Optimized for all agent types.  
Optimized for voice | This default tool type has been configured specifically for voice agents.  
Customize | Choosing the `Customize` option lets you specify your own [Grounding](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/settings#grounding), [Rewriter](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/settings#rewriter_bring-your-own-prompt), and [Summarization](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/settings#summarization_bring-your-own-prompt) parameters instead of using the `Default` and `Optimized for voice` assigned defaults.  
  
## Grounding

**Note:** We recommend reducing the size of context chunks passed to the model. You can minimize hallucinations and improve the accuracy and consistency of responses by keeping inputs concise.

Dialogflow CX calculates a confidence level for each response generated from the content of your connected data stores. This gauges the confidence that all information in the response is supported by information in the data stores. You can adjust which responses are allowed by selecting the lowest confidence level you're comfortable with, and the agent won't return responses lower than that level.

There are five confidence levels to choose from: `VERY_LOW`, `LOW`, `MEDIUM`, `HIGH`, and `VERY_HIGH`.

You can also apply a grounding heuristics filter. If you enable it, the agent suppresses responses containing content that is likely inaccurate based on common hallucinations.

## Select summarization model

You can select the generative model that a data store agent uses for summarization generative requests. The following table lists the available options:

Model Name | Launch Stage | Model Spec  
---|---|---  
Default  | GA  | This is the recommended configuration and is subject to change over time. If you use this option, you may experience changes in agent behavior (likely improvements). If you would like more consistency in agent behavior, select a specific model.  
Disabled  | GA  | Only supported under Customer Engagement AI. Disables the summarization component under Data Store Tool. Latency will improve, but quality will be degraded.  
Summarization by agent  | GA  | Only supported under Customer Engagement AI. This option delegates summarization to the agent. It is specifically optimized for voice interactions with optimized latency.  
gemini-2.5-flash | GA | [Gemini 2.5 flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/2-5-flash)  
gemini-2.5-flash-lite | GA | [Gemini 2.5 flash lite](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/2-5-flash-lite)  
gemini-3.1-flash-lite | GA | [Gemini 3.1 flash lite](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-1-flash-lite)  
gemini-3.5-flash-lite | GA | [Gemini 3.5 flash lite](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-5-flash-lite)  
  
All listed models are available in all [supported languages](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store#languages) and [supported regions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store#regions).

### Summarization custom prompt

**Note:** Providing a custom prompt might influence the quality of answers either positively or negatively. You're responsible for the quality of the answers.

You can either use a default summarization prompt with your selected summarization model or provide your own. The prompt is a text template that can contain predefined placeholders. The placeholders will be replaced with the appropriate values at runtime and the final text will be sent to the LLM.

The placeholders are as follows:

  * `$original-query`: The user's query text.
  * `$rewritten-query`: Dialogflow uses a rewriter module to rewrite the original user query into a more accurate format.
  * `$sources`: Dialogflow uses Enterprise Search to search for sources based on the user's query. The found sources are rendered in a specific format:
        
        [1] title of first source
        content of first source
        [2] title of second source
        content of second source
        

  * `$end-user-metadata`: Information about the user sending the query is rendered in the following format:
        
        The following additional information is available about the human: {
          "key1": "value1",
          "key2": "value2",
          ...
        }
        

  * `$conversation`: The conversation history is rendered in the following format:
        
        Human: user's first query
        AGENT: answer to user's first query
        Human: user's second query
        AGENT: answer to user's second query
        

  * `${conversation USER:"<user prefix>" AGENT:"<agent prefix>" TURNS:<turn count>}`: A parameterized version of the `$conversation` placeholder. You can customize the end-user prefix (`USER`), the agent prefix (`AGENT`), and the number of previous turns to include (`TURNS`). All placeholder parameter values must be specified.

For example, `${conversation USER:"Human says:" AGENT:"Agent says:" TURNS:1}`. The conversation history is rendered as:
        
        Human says: user's first query
        Agent says: answer to user's first query
        


**Important:** The placeholders `$original-query` (or `$rewritten-query`) and `$sources` are required in custom prompts. You can't save prompts missing these placeholders because the agent doesn't function correctly without them. The `$conversation` placeholder is **recommended** —without it, the agent can't use contextual information from the conversation to answer questions.

A custom prompt should instruct the LLM to return "NOT_ENOUGH_INFORMATION" when it cannot provide an answer. In this case, the agent invokes a [no-match event](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in).

For example:
    
    
    Given the conversation between a Human and a AI assistant and a list of sources,
    write a final answer for the AI assistant.
    Follow these guidelines:
    +   Answer the Human's query and make sure you mention all relevant details from
      the sources, using exactly the same words as the sources if possible.
    +   The answer must be based only on the sources and not introduce any additional
      information.
    +   All numbers, like price, date, time or phone numbers must appear exactly as
      they are in the sources.
    +   Give as comprehensive answer as possible given the sources. Include all
      important details, and any caveats and conditions that apply.
    +   The answer MUST be in English.
    +   Don't try to make up an answer: If the answer cannot be found in the sources,
      you admit that you don't know and you answer NOT_ENOUGH_INFORMATION.
    You will be given a few examples before you begin.
    
    Example 1:
    Sources:
    [1] <product or service> Info Page
    Yes, <company> offers <product or service> in various options or variations.
    
    Human: Do you sell <product or service>?
    AI: Yes, <company> sells <product or service>. Is there anything else I can
    help you with?
    
    Example 2:
    Sources:
    [1] Andrea - Wikipedia
    Andrea is a given name which is common worldwide for both males and females.
    
    Human: How is the weather?
    AI: NOT_ENOUGH_INFORMATION
    
    Begin! Let's work this out step by step to be sure we have the right answer.
    
    Sources:
    $sources
    
    $end-user-metadata
    $conversation
    Human: $original-query
    AI:
    

## Select rewriter model

**Note:** Providing a custom prompt might influence the quality of answers either positively or negatively. You're responsible for the quality of the answers.

When the agent processes a user query, it sends the user query and a prompt to the LLM to refactor the query using a **rewriter**.

You can select the generative model used by a data store agent for the rewriter generative request. The following table lists the available options:

Model Name | Launch Stage | Model Spec  
---|---|---  
Default  | GA  | This is the recommended configuration and is subject to change over time. If you use this option, you may experience changes in agent behavior (likely improvements). If you would like more consistency in agent behavior, select a specific model.  
Disabled Rewriter  | GA  | No query rewrite will occur. Latency will improve, but quality will be degraded. In particular, the data store tool may struggle to answer questions that require context from conversation history.  
rewrite-by-agent  | GA  | Only supported under Customer Engagement AI. This option delegates rewrite to the agent. It is optimized for both voice and text with optimized latency  
gemini-2.5-flash | GA | [Gemini 2.5 flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/2-5-flash)  
gemini-2.5-flash-lite | GA | [Gemini 2.5 flash lite](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/2-5-flash-lite)  
gemini-3.1-flash-lite | GA | [Gemini 3.1 flash lite](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-1-flash-lite)  
gemini-3.5-flash-lite | GA | [Gemini 3.5 flash lite](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-5-flash-lite)  
  
All listed models are available in all [supported languages](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store#languages) and [supported regions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store#regions).

### Rewriter custom prompt

You can use a default prompt or provide your own. The prompt is a text template that can contain predefined placeholders. Runtime values replace the placeholders, and the final text is sent to the LLM.

The placeholders and required text are as follows:

  * `$original-query`: The user's query text.
  * `$conversation`: The conversation history is rendered in the following format:
        
        Human: user's first query
        AGENT: answer to user's first query
        Human: user's second query
        AGENT: answer to user's second query
        

  * `${conversation USER:"<user prefix>" AGENT:"<agent prefix>" TURNS:<turn count>}`: A parameterized version of the `$conversation` placeholder. You can customize the end-user prefix (`USER`), the agent prefix (`AGENT`), and the number of previous turns to include (`TURNS`). All placeholder parameter values must be specified.

For example, `${conversation USER:"Human says:" AGENT:"Agent says:" TURNS:1}`. The conversation history is rendered as:
        
        Human says: user's first query
        Agent says: answer to user's first query
        

  * `$end-user-metadata`: Information about the user sending the query is rendered in the following format:
        
        The following additional information is available about the human: {
          "key1": "value1",
          "key2": "value2",
          ...
        }
        




For example:
    
    
    You observe conversations between a human and an AI assistant working at ${customer!}${business_description!}.
    Your goal is to perform a search query to help the AI assistant respond to the human's last statement.
    * Always output the best search query you can, even if you suspect it's not needed.
    * Never generate a query that is the same as the user's last statement.
    * Include as much context as necessary from the conversation history.
    * Output a concise search query, and nothing else.
    * Don't use quotes or search operators.
    * The query must be in ${language!}.
    
    Conversation History: $conversation
    Human: $original-query
    Search Query:
    

## Payload settings

Payload settings let you add the data store snippets as rich content in the response payload, which is rendered in the [messenger](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger). You can turn this feature on or off.

## Data store tool search configuration

You can configure dynamic search parameters to fine-tune your results based on context from an ongoing conversation. For more information, see the [Search configuration documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/search-configure).

[ Previous arrow_back  Data store tools  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/handler)

[ Next Data store performance improvements  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/performance)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
