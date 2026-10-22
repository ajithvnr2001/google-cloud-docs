---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-container-v2/
title: Container V2 \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:38.341497+00:00
---

# Container V2  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-container-v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Container V2 Stay organized with collections  Save and categorize content based on your preferences. 

The container V2 offers significant improvements from the initial container. To ensure the most impactful suggestions and key tools are always accessible to the agent, version 2 uses a reactive display with dynamic panels and a unified feed of suggestions.

**Note:** If you use the [companion agent](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/companion-agent-overview), use the [companion agent UI module](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-companion-agent) instead of the container.

## Usage

Import the module in your HTML page with the following code:
    
    
    <script src="https://www.gstatic.com/agent-assist-ui-modules/v2/container.js"></script>
    

Embed the module with the following tag:
    
    
    <agent-assist-ui-modules-v2>
    

### UI module connector

Unlike V1, you must initialize the UI module connector separately in V2. Decoupling the connector from the container allows for greater integration flexibility. For the setup, refer to [UI modules connector](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules#implement_the_ui_module_connector). Many of the properties on the V1 container apply only to the UI module connector.

### Localization

The V2 Container supports localized languages. To load the container in a specific language, prepend the locale code to the script path:

Example for Japanese:
    
    
    <script src="https://www.gstatic.com/agent-assist-ui-modules/ja/v2/container.js"></script>
    

If no locale is specified, the container defaults to English (`en`), loaded from the root path: `html <script src="https://www.gstatic.com/agent-assist-ui-modules/v2/container.js"></script>`

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

Attributes are string-based component properties which can be set in HTML or using `setAttribute()` in JavaScript.

Property name | Type | Comment  
---|---|---  
features | string | Comma-separated list of Agent Assist suggestion feature keys to render. Supported list: `AGENT_COACHING`, `CONVERSATION_SUMMARIZATION`, `SMART_REPLY`, `KNOWLEDGE_SEARCH`, `PROACTIVE_GENERATIVE_KNOWLEDGE_ASSIST`. Ignored if `use-configured-features` is set to `true`.  
use-configured-features | BooleanString | Whether to dynamically load the suggestion features configured on the conversation profile instead of hardcoding them in `features`. Defaults to `"false"`.  
disabled-features | string | Comma-separated list of suggestion features to exclude when `use-configured-features` is `"true"`. Example: `"SMART_REPLY,CONVERSATION_SUMMARIZATION"`.  
session-id | string | Optional session ID for non-conversation-based usage, such as with Generative knowledge assist.  
show-header | BooleanString | Whether to show the Agent Assist branding header. Defaults to `"false"`.  
show-dark-mode-toggle | BooleanString | Whether to show the toggle for dark mode versus light mode. Defaults to `"true"`.  
namespace | string | Optional namespace limit. Only needed if implementing multiple UI module instances on a single page.  
handoff-summarization-enabled | BooleanString | Whether to automatically trigger conversation summarization for when an existing conversation is initialized. Defaults to `"false"`.  
  
## Inputs

Inputs are JavaScript objects or other complex property types which must be assigned on the element instance directly:
    
    
    const el = document.querySelector('agent-assist-ui-modules-v2');
    el.propertyName = value;
    

Property name | Type | Comment  
---|---|---  
knowledgeAssistCardConfig | KnowledgeAssistV2Config | Optional configurations for Generative Knowledge Assist cards, including copying/pasting answers and customizing article link targets.  
  
## Types

See the following section for the custom types used by the component.

### BooleanString
    
    
    "true" | "false"
    

### KnowledgeAssistV2Config
    
    
    interface KnowledgeAssistV2Config {
      /** Configuration for how suggested article links are opened. */
      articleLinkConfig?: {
        /** Whether to open the article in a new tab or in a popup window. Defaults to 'blank' (new tab). */
        target?: "blank" | "popup";
        /** Options to configure the popup's size and location. */
        popupWindowOptions?: string;
        /** The field name on the document metadata if a separate article link source is provided. */
        linkMetadataKey?: string;
      };
      /** Whether to show the Copy Answer button on suggestions. */
      showCopyAnswer: boolean;
      /** Whether to show the Paste Answer button on suggestions. */
      showPasteAnswer: boolean;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
