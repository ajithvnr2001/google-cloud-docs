---
url: https://docs.cloud.google.com/data-studio/create-calculated-fields-gemini/
title: Create calculated fields with Gemini assistance \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:17.625519+00:00
---

# Create calculated fields with Gemini assistance  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/create-calculated-fields-gemini/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Create calculated fields with Gemini assistance Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** While in preview, Gemini in Data Studio features are available at no additional cost. At the end of this Preview period, usage of Gemini in Data Studio features may require an additional fee.

This documentation describes how to use [Gemini in Data Studio](https://docs.cloud.google.com/data-studio/gemini-overview) to help you create calculated fields by letting you describe the kinds of fields that you want.

Data Studio prompts you to describe the fields that you'd like to create. Based on your input, Data Studio suggests a formula for a [calculated field](https://docs.cloud.google.com/data-studio/about-calculated-fields) by using fields from your data source along with Data Studio functions and operators.

Gemini in Data Studio is a product in the [Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/overview) portfolio that provides generative AI-powered assistance to help you analyze and gain valuable insights from your data.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

This page is intended for report editors in Data Studio.

## Before you begin

To use this Gemini in Data Studio feature, you need to fulfill the following requirements:

  * You must be a user under a [Data Studio Pro subscription](https://docs.cloud.google.com/data-studio/pro-subscription-overview). Data Studio Pro licenses are [available at no cost](https://docs.cloud.google.com/looker/docs/admin-panel-platform-lsp) to Looker users.
  * To be able to create chart-specific calculated fields, you must be an editor of the report.
  * [Field Editing in Reports](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports) must be enabled in the data source.
  * Gemini in Data Studio must be [enabled for your Data Studio Pro project](https://docs.cloud.google.com/data-studio/enable-and-disable-gemini-in-data-studio).



## Create a calculated field with Gemini assistance

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

To create a calculated field with Gemini assistance, follow these steps:

  1. When you're [writing a calculated field](https://docs.cloud.google.com/data-studio/about-calculated-fields), click the **Help me write a calculated field** icon in the bottom right of the field editor.
  2. If you have not begun writing a calculated field, Data Studio prompts you to select a suggested prompt or to describe the kind of calculated field that you want to create. 
     * To select one of the suggested prompts, click the prompt.
     * To describe the kind of calculated field that you want to create, write a description and then click **Create**. See the **Sample prompts** section for examples of descriptions that you can write.
  3. If you have already begun writing a calculated field, Data Studio will use that formula as context. Describe how you would like to change the calculated field, and then click **Create**. 
     * To edit your original prompt, hover over the prompt and click the **Edit** icon. Edit your prompt, and then click **Update.**
     * To remove the previous formula from Data Studio's context, hover over the formula and click the **Reset** icon.
     * To refine your formula, click **Refine**. Next, provide Data Studio with additional information about your formula, such as adding or removing a bucket, or adding another field to a concatenation. Finally, click **Create**.
  4. To add the generated formula to your calculated field definition, click **Apply**.
  5. To save your field definition, click **Save**.



To exit the formula generation dialog at any point without saving your changes, close the dialog by clicking the **X** in the top right corner or by clicking outside of the dialog.

### Limitations

Note the following limitations on calculated field creation:

  * Gemini in Data Studio can help you create only calculated fields that meet Data Studio criteria of [what you can do with calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields).
  * Data Studio won't suggest [parameters](https://docs.cloud.google.com/data-studio/parameters) or a [NATIVE_DIMENSION](https://docs.cloud.google.com/data-studio/nativedimension) when it suggests a calculated field.
  * The [Looker connector](https://docs.cloud.google.com/data-studio/limits-of-the-looker-connector#support-of-data-studio-features) supports only [some functions](https://docs.cloud.google.com/data-studio/limits-of-the-looker-connector#expandable-1) for calculated fields.



### Information used by Gemini in Data Studio

When you create a calculated field with Gemini assistance, Data Studio uses the following information to generate formulas:

  * The prompt that you write to instruct Data Studio to create or edit a field
  * The formula definition for any field that you change or refine
  * The schema of the underlying data source



## Sample prompts

To get you started, here are some sample prompts for different kinds of fields:

  * Try entering the following prompt:
        
        Merge city and state like City, State
        

Data Studio may return a field definition like the following:
        
        CONCAT(Users City, ", ", Users State)
        

  * Try entering the following prompt:
        
        bucket sale price in groups of 20
        

Data Studio may return a field definition like the following:
        
        CASE
            WHEN Order Items Sale Price < 20 THEN "0-20"
            WHEN Order Items Sale Price < 40 THEN "20-40"
            WHEN Order Items Sale Price < 60 THEN "40-60"
            WHEN Order Items Sale Price < 80 THEN "60-80"
            WHEN Order Items Sale Price < 100 THEN "80-100"
            WHEN Order Items Sale Price < 120 THEN "100-120"
            WHEN Order Items Sale Price < 140 THEN "120-140"
            WHEN Order Items Sale Price < 160 THEN "140-160"
            WHEN Order Items Sale Price < 180 THEN "160-180"
            WHEN Order Items Sale Price < 200 THEN "180-200"
            ELSE "200+"
        END
        




## Troubleshooting

If you get an error while creating a calculated field with Data Studio, make sure that you are asking for a [result that you can achieve with calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields), rather than the results of a query or a chart.

## Provide feedback

After generating a calculated field, Data Studio will prompt you to provide feedback on the field. If the generated field looks correct, click the thumb_up **Rate positive** thumbs-up icon. If the generated field looks incorrect, or if you'd like to provide other feedback on this feature, click the thumb_down **Rate negative** thumbs-down icon. Include the prompt that you entered as well as the formula that Data Studio created. This feedback is collected for our development team and is not used to train the Gemini in Data Studio model.

**Note:** Gemini in Data Studio features are in preview with limited support. We encourage you to share your feedback to help us improve. To report bugs or issues, reach out to [data-studio-ca AT google.com](mailto:data-studio-ca@google.com) and include the following details: 

  * A clear description of the problem and the expected behavior
  * Steps to reproduce the issue
  * Any additional relevant details



## Related resources

  * [Gemini for Google Cloud overview](https://docs.cloud.google.com/gemini/docs/overview)
  * [Gemini in Data Studio](https://docs.cloud.google.com/data-studio/gemini-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
