---
url: https://docs.cloud.google.com/vision-ai/docs/search-streaming-warehouse/
title: Search streaming video warehouse data in the console \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:33.570141+00:00
---

# Search streaming video warehouse data in the console  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/search-streaming-warehouse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Search streaming video warehouse data in the console Stay organized with collections  Save and categorize content based on your preferences. 

After you have created a Vision Warehouse, added it to an app, and deployed the app, you can search for clips (assets) stored in the streaming video warehouse.

## Search streaming video clip assets

### Console

  1. Open the **Warehouses** tab of the Gemini Enterprise Agent Platform Vision dashboard.

[Go to the Warehouses tab](https://console.cloud.google.com/ai/vision-ai/media-warehouse)

  2. Find your desired warehouse, and click **View assets**.

  3. You will see a list of clips (each corresponding to a stream), as well as two search bars: **Date range** and **Stream name**. You can either select a clip to view it, or begin to search for clips.

**Note:** For assets not ingesting data, a placeholder image appears in Google Cloud console
  4. To begin searching, identify and enter search criteria. On the search result page you can see these video clips, each clip corresponding to a continuous video clip matching the search criteria. Use the following criteria:

     * **Date search** : To view all clips within some time frame (for example, _This month_), click the **Date range** drop down and select your desired range.

     * **Stream name search** : If you would like to search for a particular stream clip, type its stream name into the **Search stream name** bar.

     * **Date & stream name search**: To view one particular clip at some specified date range, populate both search options.

     * **Generic search** : Select the key-value pair of any searchable type in your warehouse using the **Add criteria (AND)** button.

  5. After specifying search criteria, click the **Search** button to execute the search.

All clips that matches the initial search criteria will appear on the side of the page. On the other side, you will see groups of facetable schema fields, and a list of criteria to select.

You can modify faceted filtering and selectively enable or disable facet criteria from the details page. Initially, all of these checkboxes will be disabled. To facet by some criteria you need to go to the details page, enable that facet, and then search again. See [create and update data schema](https://docs.cloud.google.com/vision-ai/docs/create-update-dataschema#modify-facetable-fields) for more details.

![search a warehouse image](https://docs.cloud.google.com/static/vision-ai/docs/images/search-ui.png)

To further filter the clips, select one or more of the facet criteria checkboxes on the side, then click **Search**. You will see an updated list of matching clips, as well as updated facets.

You can also click on a video image to view the clip. Downloading a clip has a 100MB restriction.

  6. After search results are populated, you can order the search results by the available data schema by clicking **Sort By** in the top right. Selecting a data schema automatically reorders the results.

     1. Optional: After search results populate, sort the search results by the available data schema by clicking the arrow at the top right.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
