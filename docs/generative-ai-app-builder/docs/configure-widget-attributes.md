---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-widget-attributes/
title: Configure results for the search widget \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:14.732958+00:00
---

# Configure results for the search widget  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-widget-attributes/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Configure results for the search widget Stay organized with collections  Save and categorize content based on your preferences. 

This section describes how to configure results for the search widget, depending on the type of search app you have.

If you use third-party access control for your data sources, these configuration settings also apply to the web app.

## Search widget concepts

Here are some concepts to help you understand how to use the controls on the **UI** tab.

  * **Snippet** : A short section of text, typically a sentence, under the document title. By default, a snippet is displayed for each search result for website and unstructured data.

  * **Search with an answer** : This feature provides a paragraph of information (the answer) synthesized from the top results of website or unstructured data. You can customize the number of top results that the answer is based on. By default, the top five results are summarized to create the answer. Search with an answer cannot be combined with Search with follow-ups.

  * **Search with follow-ups** : This feature for website and unstructured data allows for follow-up questions that keep the context of the initial search query.

  * **Autocomplete** : Suggests search queries based on the first letters that users enter into the search bar. For more information, see [Configure autocomplete](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-autocomplete).

  * **Feedback** : Provides buttons thumb_up and thumb_down so that users can rate the quality of the search results. This information is sent only to Google. For more information, see [Configure widget feedback](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-feedback).

  * **Metadata** : If the data is structured or contains metadata, you can configure which metadata fields to include in the search results. You can also map fields to display names for facets. For more information, see [Configure facets for the search widget](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-widget-facets).

  * **Select an LLM** : The stable LLM version is chosen by default for your application. To change the LLM version, see [Search summarization differs by model](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-search-results#search_summarization_differs_by_model).

  * **Turning off generative responses** : If you turn off generative responses for a search widget, the [advanced LLM feature](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#generative-response-features), such as search with follow-ups and search with an answer, stop working for all users of the project. See [Turn generative responses on or off](https://docs.cloud.google.com/generative-ai-app-builder/docs/advanced-llm).

  * **Image in answers** : This feature returns the following kinds of images with the answers:

    * Charts generated from information in the answer
    * Images selected from an unstructured data store that a layout parser parses

Use this feature with **Search with an answer** or **Search with follow-ups** and the stable large language model or any Gemini model 2.0 or later. To return images from the corpus in the answer, enable snippets or extractive content. For more information, see [Generate charts for answer](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer#get-charts) and [Retrieve existing images from the data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer#get-images).

  * **Search-as-you-type** : Available only for media apps. This feature performs a search after each keystroke. You don't need to press `Enter` to get a search result. For more information, see [Get search-as-you-type results for a media app](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-search-results#media-search).




## Configure search results for unstructured or website data

The search widget for unstructured and website data offers the following search customizations:

  * Search (single-turn)
  * Search with an answer (single-turn search with summarization)
  * Search with follow-ups (multi-turn search)



For search with an answer and search with follow-ups, you need turn on some advanced settings:

  * For search apps with unstructured data: [Generative responses](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#generative-response-features)

  * For website search apps: [Generative responses](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#generative-response-features) and [Advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#advanced-website-indexing)




To configure how the widget displays search results for unstructured data:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/start)

  2. Click the name of the app that you want to edit.

  3. In the navigation menu, click **Configurations**.

  4. Click the **UI** tab.

  5. Edit the fields on the tab.

  6. Use the **Preview** pane to make sure your changes are displayed as expected.

  7. Click **Save and publish** to apply your changes.




## Configure search results for healthcare data

**Deprecated:** Agent Search for healthcare is deprecated and won't be available after May 15, 2027. 

The search widget for healthcare data offers the following search customizations:

  * Search
  * Search with an answer



For search with an answer, turn on the [Generative responses](https://docs.cloud.google.com/generative-ai-app-builder/docs/advanced-llm) option.

To configure how the widget displays search results for healthcare data:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/start)

  2. Click the name of the app that you want to edit.

  3. In the navigation menu, click **Configurations**.

  4. Click the **UI** tab.

  5. In the **Search type** list, select one of the following:

     * **Search** : to perform a single-turn search
     * **Search with an answer** : to perform a single-turn search with a generative AI generated answer
  6. If you selected **Search with an answer** , in the **Large language models for summarization** section, select one of the models that is supported for healthcare. See [Generally available (GA) models](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer-generation-models#generally_available_ga_models).

  7. Click **Save and publish** to apply your changes.




## Configure search results for structured data

**Note:** This feature is a Preview offering, subject to the "Pre-GA Offerings Terms" of the [GCP Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA products and features may have limited support, and changes to pre-GA products and features may not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). Further, by using this feature, you agree to the [Generative AI Preview terms and conditions](https://cloud.google.com/trustedtester/aitos) ("Preview Terms"). For this feature, you can process personal data as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to applicable restrictions and obligations in the Agreement (as defined in the Preview Terms). 

For structured data, by default, the widget displays all of the name-value pairs for each item in the search results. You can use the **Configurations** page in the Google Cloud console to customize how the widget displays search results.

The following list shows the primary fields for displaying search results:

  * **Title.** An item title that a user can click to select that item in a search result.
  * **Thumbnail.** The URL of an image to be shown next to the item title in a search result.
  * **URL.** A URL that the user is taken to when they click the item's title.



You can display up to three additional fields in your search results and configure how they appear.

In addition, you can select facets to filter search results on and set display names for them. For more about configuring widget facets, see [Configure facets for the search widget](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-widget-facets).

To configure how the widget displays search results for structured data:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/start)

  2. Click the name of the search app that you want to edit.

  3. Click **Configurations**.

  4. Click the **UI** tab.

  5. If you have multiple data stores connected to your app, select the data store to configure results for.

  6. Expand the **Configure fields in results** section.

  7. In the **Preview** pane, type a query and press **Enter** to view how search results are displayed with your current settings. The preview updates automatically when you enter new settings.

  8. Optional: Click a device icon to see the preview in desktop or mobile format.

  9. To configure the primary fields (**Title** , **Thumbnail** , and **URL**) in your search results:

     1. Click the **Title** box and select a field to map to the titles of your search results. Or, select **None** if you don't want titles to appear in search results.

     2. Click the **Thumbnail** box and select a field to map to the thumbnail images in your search results. Or, select **None** if you don't want thumbnail images to appear in search results.

     3. Click the **URL** box and select a field that maps to the items that open when users click item titles in search results. Or, select **None** if you don't want item titles in your search results to link to items.

  10. To add additional fields to your search results:

     1. Click the **Text 1** box and select a field that you want to display in your search results. By default, only the field value is displayed in search results.

     2. Click the arrow next to the **Text 1** box to display the **Template** box. The **{value}** field in **Template** box represents the field value to display in the search result. Add text before or after the **{value}** field (or both) to give context to the value in the search results. For example, suppose you selected `price` in the **Text 1** box, and the price value for a particular item is 42. If you update the **Template** field to `"Total Price: {value} USD"`, then "Total Price: 42 USD" is displayed in the search results for that item.

     3. To add additional fields, repeat these steps for the **Text 2** and **Text 3** boxes.

  11. To configure facet settings:

     1. Expand the **Facet settings** section.

     2. Click **Add facet**.

     3. Select a field to set as a facet and enter a display name.

     4. To add more facets, click **Add facet**.

  12. Check the **Preview** pane to make sure your changes display correctly.

  13. Click **Save and publish** to apply your changes.


**Note:** For information about enabling autocomplete, see [Configure autocomplete](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-autocomplete).  
For information about enabling feedback, see [Configure widget feedback](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-feedback).

## Next steps

  * [Get search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-search-results)
  * [Add the search widget to a web page](https://docs.cloud.google.com/generative-ai-app-builder/docs/add-widget)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
