---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-transcript-documentation/
title: Transcript \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:40.430104+00:00
---

# Transcript  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-transcript-documentation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Transcript Stay organized with collections  Save and categorize content based on your preferences. 

This page contains the API documentation for the Transcript UI module. This module is used to display a live transcript of a voice conversation.

## Usage

Import the module in your HTML page using the following code:
    
    
    <script src="https://www.gstatic.com/agent-assist-ui-modules/v1/transcript.js"></script>
    

Embed the module using the following tag:
    
    
    <agent-assist-transcript>
    

## Attributes

Property name | Type | Comment  
---|---|---  
show-message-time | BooleanString | Whether to show a timestamp offset next to each message.  
  
### Usage

Attributes are string-based component properties which can be set in the following ways:

From your HTML template directly:
    
    
    <element-selector property-name="value">
    

From your JavaScript code:
    
    
    var el = document.querySelector('element-selector');
    el.setAttribute('property-name', 'value');
    

## Inputs

No inputs.

## Types

See the following section for the custom types used by the component.

### BooleanString
    
    
    "true" | "false"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
