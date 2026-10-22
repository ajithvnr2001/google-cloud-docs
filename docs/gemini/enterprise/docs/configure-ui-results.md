---
url: https://docs.cloud.google.com/gemini/enterprise/docs/configure-ui-results/
title: Configure results for the UI \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:13.082546+00:00
---

# Configure results for the UI  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/configure-ui-results/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Configure results for the UI Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure results for the web app UI, which is the interface that your users use to access your app.

## Search widget concepts

Here are some concepts to help you understand how to use the controls on the **UI** tab.

  * **Snippet.** A short section of text, typically a sentence, under the document title. By default, a snippet is displayed for each search result for website and unstructured data.

  * **Search with an answer.** This feature provides a paragraph of information (the answer) synthesized from the top results of website or unstructured data. You can customize the number of top results that the answer is based on. By default, the top five results are summarized to create the answer. Search with an answer cannot be combined with Search with follow-ups.

  * **Search with follow-ups.** This feature for website and unstructured data allows for follow-up questions that keep the context of the initial search query.

  * **Autocomplete.** Suggests search queries based on the first letters that users enter into the search bar. For more information, see [Configure autocomplete](https://docs.cloud.google.com/gemini/enterprise/docs/configure-autocomplete).

  * **Feedback.** Provides buttons thumb_up and thumb_down so that users can rate the quality of the search results. This information is sent only to Google. For more information, see [Configure feedback](https://docs.cloud.google.com/gemini/enterprise/docs/configure-feedback).

  * **Metadata.** If the data is structured or contains metadata, you can configure which metadata fields to include in the search results. You can also map fields to display names for facets. For more information, see [Configure facets for the UI](https://docs.cloud.google.com/gemini/enterprise/docs/configure-ui-facets).

  * **Admin-configured display name for sources.** Displays the administrator-configured display name for data sources in the web app instead of the connector type. For more information, see Show administrator-configured display names for data sources.




## Configure search results for unstructured or website data

The UI for unstructured and website data offers the following search customizations:

  * Search (single-turn)
  * Search with an answer (single-turn search with summarization)
  * Search with follow-ups (multi-turn search)



To configure how the UI displays search results for unstructured data:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/start)

  2. Click the name of the app that you want to edit.

  3. In the navigation menu, click **Configurations**.

  4. Click the **UI** tab.

  5. Edit the fields on the tab.

  6. Use the **Preview** pane to make sure your changes are displayed as expected.

  7. Click **Save and publish** to apply your changes.




## Configure search results for structured data

For structured data, by default, the UI displays all of the name-value pairs for each item in the search results. You can use the **Configurations** page in the Google Cloud console to customize how the UI displays search results.

The following list shows the primary fields for displaying search results:

  * **Title.** An item title that a user can click to select that item in a search result.
  * **Thumbnail.** The URL of an image to be shown next to the item title in a search result.
  * **URL.** A URL that the user is taken to when they click the item's title.



You can display up to three additional fields in your search results and configure how they appear.

In addition, you can select facets to filter search results on and set display names for them. For more about configuring facets, see [Configure facets for the UI](https://docs.cloud.google.com/gemini/enterprise/docs/configure-ui-facets).

To configure how the UI displays search results for structured data:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/start)

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

     2. Select a field to set as a facet and enter a display name.

     3. To add more facets, click **Add facet**.

  12. Check the **Preview** pane to make sure your changes display correctly.

  13. Click **Save and publish** to apply your changes.


**Note:** For information about enabling autocomplete, see [Configure autocomplete](https://docs.cloud.google.com/gemini/enterprise/docs/configure-autocomplete).  
For information about enabling feedback, see [Configure feedback](https://docs.cloud.google.com/gemini/enterprise/docs/configure-feedback).

## Show administrator-configured display names for data sources

By default, the web app displays the connector type as the label for single-instance data sources. You can turn on the **Use admin-configured display name for sources** setting so that the web app instead displays the custom display name that you configured for each data source.

To turn administrator-configured display names for data sources on or off:

### Console

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Go to Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/start)

  2. Click the name of the app that you want to edit.

  3. In the navigation menu, click **Configurations**.

  4. Click the **Search UI** tab.

  5. In the **General configurations** section, turn the **Use admin-configured display name for sources** toggle on or off.

  6. Click **Save and publish** to apply your changes.




### REST

Update the `uiSettings.sourceAdminDisplayNameEnabled` field on the app's `WidgetConfig` resource by calling the [`engines.widgetConfigs.patch`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.widgetConfigs/patch) method:
    
    
    curl -X PATCH \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -H "X-Goog-User-Project: PROJECT_ID" \
      "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/collections/default_collection/engines/APP_ID/widgetConfigs/default_search_widget_config?updateMask=uiSettings.sourceAdminDisplayNameEnabled" \
      -d '{
        "uiSettings": {
          "sourceAdminDisplayNameEnabled": SOURCE_ADMIN_DISPLAY_NAME_ENABLED
        }
      }'
    

Replace the following:

  * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * `PROJECT_ID`: the number or ID of your Google Cloud project.
  * `LOCATION_ID`: the geographic location of your data store, such as `global`. For more information, see [Locations](https://docs.cloud.google.com/gemini/enterprise/docs/locations). 
  * `APP_ID`: the ID of the app.
  * `SOURCE_ADMIN_DISPLAY_NAME_ENABLED`: a boolean value. Specify `true` to show the administrator-configured display name for data sources, or `false` to show the connector type.



## Next steps

  * [Preview search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
