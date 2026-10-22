---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-companion-agent/
title: Companion agent UI module \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:18.933195+00:00
---

# Companion agent UI module  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-companion-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Companion agent UI module Stay organized with collections  Save and categorize content based on your preferences. 

The companion agent UI module embeds an interactive [companion agent](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/companion-agent-overview) directly within your agent desktop. The companion agent feature supersedes most other Agent Assist features, and replaces the need to use the [Container V2](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-container-v2). The companion agent UI module also includes some complementary features, such as [conversation summarization](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-with-custom-sections).

## Usage

Import the module in your HTML page with the following code:
    
    
    <script src="https://www.gstatic.com/agent-assist-ui-modules/v1/companion_agent.js"></script>
    

Embed the module with the following tag:
    
    
    <agent-assist-companion-agent></agent-assist-companion-agent>
    

### UI module connector

You must initialize the UI module connector separately when using the companion agent UI module. Deploy the latest version of the [integration backend](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/backend-basics) that includes streaming support.

For complete configuration options and supported agent desktop configurations, see [Implement the UI module connector](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules#implement_the_ui_module_connector).

### Localization

The companion agent UI module supports localized languages. To load the module in a specific language, prepend the locale code to the script path:

Example for Japanese:
    
    
    <script src="https://www.gstatic.com/agent-assist-ui-modules/ja/v1/companion_agent.js"></script>
    

If you don't specify a locale, the module defaults to English (`en`), loaded from the root path:
    
    
    <script src="https://www.gstatic.com/agent-assist-ui-modules/v1/companion_agent.js"></script>
    

Supported locales:

  * Arabic (`ar`)
  * Chinese (Simplified) (`zh_cn`)
  * Croatian (`hr`)
  * English (Australia) (`en_au`)
  * English (Canada) (`en_ca`)
  * English (United Kingdom) (`en_gb`)
  * Filipino (`fil`)
  * French (`fr`)
  * French (Canada) (`fr_ca`)
  * German (`de`)
  * Hindi (`hi`)
  * Hungarian (`hu`)
  * Italian (`it`)
  * Japanese (`ja`)
  * Korean (`ko`)
  * Malay (`ms`)
  * Norwegian (`no`)
  * Polish (`pl`)
  * Portuguese (Brazil) (`pt_br`)
  * Romanian (`ro`)
  * Russian (`ru`)
  * Spanish (`es`)
  * Swedish (`sv`)
  * Thai (`th`)
  * Turkish (`tr`)
  * Vietnamese (`vi`)



## Attributes

Attributes are string-based component properties which you can set in HTML or using `setAttribute()` in JavaScript.

Property name | Type | Comment  
---|---|---  
channel | string | Communication type the agent is using. Controls some minor UI elements. Options include `chat` or `voice`, defaults to `chat`.  
disabled-features | string | Comma-separated list of Agent Assist suggestion features to exclude from rendering. Example: `CONVERSATION_SUMMARIZATION`.  
disable-auto-conversation-summarization | BooleanString | Whether to disable automatic generation of conversation summarization when a conversation completes. Defaults to `false`.  
handoff-summarization-enabled | BooleanString | Whether to automatically trigger conversation summarization when an existing conversation is initialized. Defaults to `false`.  
namespace | string | Optional namespace limit. Only needed if implementing multiple UI module instances on a single page.  
  
## Type

`BooleanString`:
    
    
    "true" | "false"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
