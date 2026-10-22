---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-summarization-documentation/
title: Summarization \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:37.232966+00:00
---

# Summarization  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-summarization-documentation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Summarization Stay organized with collections  Save and categorize content based on your preferences. 

This page contains the API documentation for the [Conversation Summarization](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-with-custom-sections) UI module. This module is used to generate a summary of a conversation.

## Usage

Import the module in your HTML page using the following code:
    
    
    <script src="https://www.gstatic.com/agent-assist-ui-modules/v1/summarization.js"></script>
    

Embed the module using the following tag:
    
    
    <agent-assist-summarization>
    

## Attributes

Property name | Type | Comment  
---|---|---  
show-generate-summary-button | BooleanString | Whether to show the **Generate Summary** button.  
  
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
onSaveSummary | OnSaveSummary | Callback to invoke when summary is saved. Used by customers to send summary details to CRM.  
  
### Usage

Inputs are typically JavaScript objects or other complex property types which must be assigned on the element instance directly:
    
    
    const el = document.querySelector('element-selector');
    el.propertyName = value;
    

## Types

See the following section for the custom types used by the component.

### BooleanString
    
    
    "true" | "false"
    

### OnSaveSummary
    
    
    type OnSaveSummary = (
      summary: {
        summary: string;
        conversationDetails: ConversationDetails;
      },
      saveCallbacks: {
        setLoading: () => void;
        setSuccess: (message: string) => void;
        setError: (message: string) => void;
      }
    ) => void;
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
