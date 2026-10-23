---
url: https://docs.cloud.google.com/looker/docs/write-lookml-gemini/
title: Write LookML with Gemini assistance \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:20.908290+00:00
---

# Write LookML with Gemini assistance  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/write-lookml-gemini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Write LookML with Gemini assistance Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This documentation page describes how to use Gemini assistance to create dimensions, dimension groups, and measures, in a LookML project. Generating LookML code suggestions in response to written prompts is a Gemini in Looker feature that is available in Looker (original) and Looker (Google Cloud core) instances.

[Gemini in Looker](https://docs.cloud.google.com/looker/docs/gemini-overview-looker) provides generative AI-powered assistance to help you work with your data.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

This page is intended for Looker developers.

**Tip:** You can also use the [Looker extension for VS Code](https://marketplace.visualstudio.com/items?itemName=Google.vscode-looker-official) to develop LookML directly within your local desktop environment using the Visual Studio Code (VS Code) framework. See the [Getting started with the Looker extension for VS Code](https://docs.cloud.google.com/looker/docs/getting-started-vscode-extension) documentation page for more information.

## Before you begin

To use Gemini in the Looker IDE, note the following requirements:

  * Gemini in Looker must be enabled for your Looker instance: 
    * For Looker (original), the instance must be running Looker 25.2 or later, and the instance must have the **Gemini in Looker** and **LookML Assistant** settings enabled in the Admin settings. For detailed enablement instructions, see the [Admin settings — Gemini in Looker](https://docs.cloud.google.com/looker/docs/admin-panel-platform-gil) documentation page.
    * For [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/gemini-overview-looker) the instance must be enabled for Gemini in Looker in the Google Cloud console. The **LookML Assistant** must also be enabled for your instance. For detailed enablement instructions, see the [Administer Gemini on your Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-admin-gemini) documentation page.
  * You must be assigned a Looker role that contains the [`develop`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#develop) permission for at least one model in a LookML project.
  * You must be assigned a role that contains the [`gemini_in_looker`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#gemini_in_looker) permission for at least one model in the LookML project.



## Use Gemini in the Looker IDE

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

To use Gemini for creating LookML in your Looker project, follow these steps:

  1. On your Looker instance, enable [Development Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode#development_mode).
  2. [Open your project in the Looker IDE](https://docs.cloud.google.com/looker/docs/looker-ide#accessing-ide).
  3. Use the IDE [file browser](https://docs.cloud.google.com/looker/docs/ide-folders) to open a LookML view file in which you want to insert LookML.
  4. Select the **Help me code** icon from the side panel selector.

![Looker IDE with Help me code icon highlighted.](https://docs.cloud.google.com/static/looker/docs/images/ide-help-me-code-2416.png)

  5. With the the **Help me code** panel open, click to place your cursor on a line in your LookML view file. Based on the type of LookML file and where your cursor is placed in the file, Gemini provides appropriate options to guide you, such as **Create a dimension** or **Create a measure**.

  6. Select one of the following options from the **Help me code** panel:

**Note:** If you don't see all of these options, make sure that you are in a view file and that your cursor is placed at a location in the file where a dimension, dimension group, or measure is supported.
     * **Create a[dimension group](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group)**
     * **Create a[dimension](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension)**
     * **Create a[measure](https://docs.cloud.google.com/looker/docs/reference/param-field-measure)**
  7. In the **Help me code** panel text field, use conversational language to describe the dimension, dimension group, or measure that you want to create. See the Tips for using Gemini in the Looker IDE and Sample prompts sections on this page for guidance.

  8. Press **Enter** or click the **Submit** icon to send your request to Gemini. Gemini will respond with suggested code.

  9. With the suggested code, you can do the following:

     * Hold your pointer over the **Insert** button to preview the suggested LookML in your file. You can move your cursor to a different line in your file to preview it in a different location before inserting the LookML in the file.
     * Click the **Edit** button to manually change the suggested LookML.
     * Click the **Insert** button to insert the LookML into your file at the location of your cursor.
     * Provide feedback about the suggested code by selecting the thumbs up icon (**This response was helpful**) or thumbs down icon (**This response was not what I expected**).
     * Click the **New code suggestion** link to start over and enter a new prompt for Gemini.

![Gemini showing a preview of the code placement when the cursor is hovered over the Insert button.](https://docs.cloud.google.com/static/looker/docs/images/help-me-code-preview-2416.png)

  10. Click **Save Changes** in your LookML file.

  11. Verify the LookML by doing the following:

     * Use the [LookML Validator](https://docs.cloud.google.com/looker/docs/lookml-validation) to verify your LookML.
     * [Test your LookML in an Explore](https://docs.cloud.google.com/looker/docs/looker-ide#testing_the_fields_in_the_explore).



## Tips for using Gemini in the Looker IDE

Here are some tips for using Gemini in the Looker IDE:

  * For best results, write your prompts in American English. See the [Gemini for Google Cloud limitations](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai#gemini-limitations) documentation for more information.
  * The **Help me code** panel does not retain context from a previous prompt in the conversation and does not retain prompts across logins and refreshes.
  * When you use LookML that was suggested by Gemini, always validate your LookML with the [LookML Validator](https://docs.cloud.google.com/looker/docs/lookml-validation), and [test your new fields in an Explore](https://docs.cloud.google.com/looker/docs/looker-ide#testing_the_fields_in_the_explore).
  * Depending on your request, Gemini may suggest LookML that references fields in other view files. When you add suggested LookML to your file, save the file and run the LookML Validator. The LookML Validator will display errors if you need to add [`include`](https://docs.cloud.google.com/looker/docs/reference/param-model-include) statements to your model file.



## Sample prompts

To give you some ideas, here are some example prompts and their results:

  * Create a dimension using longitude and latitude
  * Create a measure for today's total sales



### Create a dimension using longitude and latitude

Here is a prompt using the **Create a dimension** option that asks Gemini to create a new dimension based on the `longitude` and `latitude` fields that are defined in the view file:

`show coordinates with longitude and latitude`

Gemini returns this suggested code:
    
    
       dimension: coordinates {
          type: location
          sql_latitude: ${TABLE}.latitude ;;
          sql_longitude: ${TABLE}.longitude ;;
       }
    

You can verify this LookML in an Explore by selecting the new `coordinates` field, along with the `longitude` and `latitude` fields it's based on. Because Gemini created the dimension using [`type:location`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#location), the Explore results include a hyperlink to view the coordinates on a map:

![Looker Explore showing the latitude and longitude fields, with the new coordinates field with values that match the latitude and longitude values.](https://docs.cloud.google.com/static/looker/docs/images/help-me-code-explore-test-2416.png)

### Create a measure for today's total sales

Here is a prompt using the **Create a measure** option that asks Gemini to create a new measure for the sum of all of today's orders:

`show the total sale price of today's orders`

Gemini returns this suggested code:
    
    
       measure: todays_orders {
          type: sum
          sql: ${basic_order_items.sale_price} ;;
          filters: [basic_order_items.created_at_date: "today"]
      }
    

## Provide feedback

You can provide feedback for the generated LookML in the **Help me code** panel. If the generated LookML looks correct, click the thumb_up thumbs-up icon. If the generated LookML looks incorrect or isn't what you expected, click the thumb_down thumbs-down icon.

**Note:** Gemini in Looker is in preview with limited support. We encourage you to share your feedback to help us improve. To report bugs or issues, reach out to [Looker Support](https://docs.cloud.google.com/looker/docs/best-practices/looker-support-details) and be sure to include the following details: 

  * A clear description of the problem and the expected behavior
  * Steps to reproduce the issue
  * Any additional relevant details



## Related resources

  * [Learn more about Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/overview)
  * [Learn more about Gemini in Looker](https://docs.cloud.google.com/looker/docs/gemini-overview-looker)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
