---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/rich-response-widget/
title: Rich response widgets \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:22:21.236810+00:00
---

# Rich response widgets  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/rich-response-widget/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Rich response widgets Stay organized with collections  Save and categorize content based on your preferences. 

You can use rich response widgets to create rich, interactive UI elements for your user interface that utilizes the [web widget deployment option](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/web-widget). When configuring this tool, you provide a type (carousel, comparison, and so on) and information about the widget schema. When responding to queries, the agent may decide to use this tool and configuration to send widget data back to your client. Your client then processes this data and presents the widget in your user interface. When your user makes a selection, you send this information back to the agent.

### Create a rich response

**Note:** The current implementation of rich response widgets is built on [widget tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/widget). A future implementation will be stand alone, and will not require referencing a tool in agent instructions.

To create a widget tool:

  1. Click the rich response widgets icon on the right side of the agent builder.
  2. Click the **Add a widget** or **+** button to open the widget gallery.
  3. Select a widget type template from the gallery, or click Custom widget in the header to create one from scratch.
  4. Provide the requested information for the widget tool in the configuration panel 
     * Name: A unique name for the widget tool.
     * Description: A description of what the tool does. This helps the agent's language model understand when to use this tool and how to populate the data.
     * Schema Preview / Parameters: For provided widget types, view the read-only JSON schema preview. If you selected a Custom widget, write your own JSON parameters to customize the widget's layout and elements.



### Use a widget in an agent

After creating a widget, you need to instruct a particular agent to use the widget.

  * Hover over an agent.
  * Click Add widget.
  * Select the widget.
  * Describe how the widget should be used in your agent instructions and reference the widget using the syntax: `{@Widget: widget_name}`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
