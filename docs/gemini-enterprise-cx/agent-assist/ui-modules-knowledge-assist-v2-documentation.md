---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-knowledge-assist-v2-documentation/
title: Knowledge assist \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:00.036612+00:00
---

# Knowledge assist  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-knowledge-assist-v2-documentation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Knowledge assist Stay organized with collections  Save and categorize content based on your preferences. 

This page contains the API documentation for the [Generative knowledge assist](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/generative-knowledge-assist) UI module, also called Knowledge Assist V2. This module is used by agents to query their company's knowledge bases and receive generative AI-powered answers.

## Usage

Import the module in your HTML page using the following code:
    
    
    <script src="https://www.gstatic.com/agent-assist-ui-modules/v2/knowledge_assist.js"></script>
    

Embed the module using the following tag:
    
    
    <agent-assist-knowledge-assist-v2>
    

## Attributes

Property name | Type | Comment  
---|---|---  
session-id | string | Optional session ID for non-conversation-based usage.  
parent | string | Parent project location name to use for non-conversation-based usage. Example: "projects/foo/locations/global"  
  
### Usage

Attributes are string-based component properties which can be set in the following ways:

From your HTML template directly:
    
    
    <element-selector property-name="value">
    

From your JavaScript code:
    
    
    var el = document.querySelector('element-selector');
    el.setAttribute('property-name', 'value');
    

## Inputs

Property name | Type | Comment  
---|---|---  
config | KnowledgeAssistV2Config | Optional configurations for Knowledge Assist V2 module.  
  
### Usage

Inputs are typically JavaScript objects or other complex property types which must be assigned on the element instance directly:
    
    
    const el = document.querySelector('element-selector');
    el.propertyName = value;
    

## Types

See the following section for the custom types used by the component.

### KnowledgeAssistV2Config
    
    
    interface KnowledgeAssistV2Config {
      articleLinkConfig: {
        /**
         * Whether to open the article in a new tab, or as a popup. Defaults to new
         * tab.
         */
        target?: "blank" | "popup";
        /**
         * Options to configure the popup's size and location. See
         * https://developer.mozilla.org/en-US/docs/Web/API/Window/open#window_features.
         */
        popupWindowOptions?: string;
        /**
         * The field name on the document metadata if a separate article link source
         * is provided.
         */
        linkMetadataKey?: string;
      };
      showCopyAnswer: boolean;
      showPasteAnswer: boolean;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
