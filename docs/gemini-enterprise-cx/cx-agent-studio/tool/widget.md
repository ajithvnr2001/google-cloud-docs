---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/widget/
title: Widget tools \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:22:24.283547+00:00
---

# Widget tools  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/widget/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Widget tools Stay organized with collections  Save and categorize content based on your preferences. 

You can use widget tools to create rich, interactive UI elements for your user interface in a flexible way. When configuring this tool, you provide a type (carousel, comparison, and so on) and information about the widget schema. When responding to queries, the agent may decide to use this tool and configuration to send widget data back to your client. Your client then processes this data and presents the widget in your user interface. When your user makes a selection, you send this information back to the agent.

## Configuration

The following configuration settings are available:

  * **Name:** A unique name for the tool (Required).
  * **Description:** A description of what the tool does (Optional). This helps the agent's language model understand when to use this tool and how to populate the data.
  * **Widget Type:** The specific type of rich content widget this tool represents. This determines the expected structure of the payload and how the client should render it. The types are as follows: 
    * **PRODUCT_CAROUSEL** : Displays a scrollable carousel of products.
    * **PRODUCT_DETAILS** : Shows detailed information about a single product.
    * **QUICK_ACTIONS** : Presents a list of suggested reply buttons or actions the user can take.
    * **PRODUCT_COMPARISON** : Displays a side-by-side comparison of multiple products.
    * **ORDER_SUMMARY** : Shows a summary of an order.
  * **Parameters:** The input schema for the widget data. The agent uses the schema when invoking the tool. This is defined using a schema object, specifying the expected fields and data types for the widget's content.



## Sample tool descriptions

Here are samples of effective tool descriptions:

Widget Type | Sample Tool Description  
---|---  
**Product Carousel** | Generates a UI carousel component. Required whenever the user asks to see options or a catalog. You must provide the list of products in `productDetails`, and the system will automatically render the visual card.  
**Product Detail** | This tool should be called after you have get one product info and try to show this product to user.  
**Quick Action** | This tool should be called whenever the user is prompted for whether they are a business, school, or nonprofit. Include exactly 3 quick actions that read as "I'm a business", "I'm a school", and "I'm a nonprofit".  
**Product Comparison** | This tool should be invoked when you are asked to compare 2 products.  
**Order Summary** | Use this tool when a user is ready to finalize a purchase. It generates a structured visual summary of the item, price breakdown (including tax and shipping), and the payment method on file. Call this tool only after the user has confirmed they want to proceed to the checkout phase.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
