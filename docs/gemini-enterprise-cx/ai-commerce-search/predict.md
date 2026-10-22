---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/predict/
title: Get recommendations \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:42.313267+00:00
---

# Get recommendations  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/predict/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Get recommendations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to request product recommendations for a specific user and user event.

After you have uploaded your products and recorded user events, you can request product recommendations for specific users based on the recorded user events for that user and their current activity. It can take up to 48 hours for new products and user events to be reflected in the recommendation model.

AI Commerce Search returns a list of ranked product identifiers. You are responsible for rendering the results on your website with images and text.

Never cache personalized results from an end user, and never return personalized results to a different end user.

## Before You Begin

You must create a Google Cloud project and set up authentication using the steps in [Before you begin](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/setting-up).

Before you can request predictions from recommendations, you need both:

  * A [trained and tuned recommendation (model)](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-models#new-model)
  * One or more active [serving configs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/configs)



## Evaluate recommendations

Before you update your website code to request recommendations, you can use preview prediction results to confirm that your model and serving config are working as you expect.

For more information about serving configs, see [About serving configs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/configs).

Preview serving config results from either the **Evaluate** page, or by going to a serving config's **Details** page in the console and clicking its **Evaluate** tab.

To preview recommendations returned by your serving config:

  1. Go to the **Evaluate** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Evaluate page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/evaluate/)

  2. Click the **Recommendations** tab, if it isn't already selected.

  3. Select the serving config you want to preview.

  4. Optional: Enter a visitor ID to preview recommendations for that user.

  5. If the **Associated items** section is shown, click **Add item** and enter a product ID to get associated recommendations for that item. You can add multiple associated items.

Adding items is available only if the selected serving config's model type requires products as input for recommendations. Recommended for You models don't require associated items to be entered.

  6. Click **Prediction preview** to see the prediction results.




To see the **Details** page for the serving config you're previewing, click **View serving config** under the **Select serving config** field.

## Get a recommendation

The Recommendations API has limits on the number of items returned. However, there are workarounds to increase the number of items returned.

### Maximize the value of browse listing

This section outlines how to get the most out of your browse listings in AI Commerce Search by effective category handling, ensuring the highest data tier model and unlocking personalization.

#### Effective category handling

  * Use unique and descriptive page category names to ensure accurate tracking of user behavior and model learning.
  * Structure categories from broad to specific, allowing users to progressively refine their browsing experience.
  * Avoid overly niche categories with limited user engagement.



#### Ensure highest-tier model

[Go to the Data quality page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/data_quality/)

Then, to configure the highest-tier model:

  1. Implement user event tracking to capture user interactions (clicks, purchases, add-to-cart) for both search and browse.

  2. Monitor data ingestion and model readiness using the AI Commerce Search [**Data quality**](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/data_quality/) dashboard.

**Note:** Ensure your browse model reaches at least "**Tier 2** ," preferably "**Tier 3** ," before [A/B testing](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/a-b-testing) or production deployment. A Tier 2 model quickly advances to Tier 3 with sufficient high-quality traffic, unlocking peak performance. Only conduct performance comparisons and A/B tests after the model achieves Tier 3, as this is its most optimized state.



See [Data quality](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/data-quality#text_query_search) for more information on data tiers for search and browse.

#### Improve performance with personalization

As a ranking model learning from user behavior, a large portion of the browse model's performance comes from its personalization capabilities.

  * Enable personalization when evaluating the model's performance.
  * Disabling personalization impacts performance and minimizes the model's potential impact.
  * Personalization should be active before exposing browse results to live production traffic or A/B testing.



### Increase result size limits

  * The limit for AI Commerce Search results is 120.

  * The Recommendations API supports reranking up to 2,000 items.

  * Although latency increases, it's possible to increase page size up to 500 or 1,000.




### Workarounds for more recommended results

You can personalize and rerank category pages using personal recommendations using REST APIs. To work around the result limit of 120 items, make multiple simultaneous calls for the first given number of pages. Then, stitch the results together to look like one large page.

To manually restrict the set of recommendations returned to end users, you can add [filter criteria](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/filter-recs) in [`PredictRequest.params`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.servingConfigs/predict#body.request_body.FIELDS.params) queries. Mark your selected attributes as filterable using the API, then refer to them directly in their prediction requests.

Because `PredictRequest` does not support standard pagination (like `offset` or `pageToken`), you cannot request a specific page to stitch results. Instead, to work around the result size limit and manually restrict results for category pages using recommendations, use filtering to slice your catalog into distinct segments, such as by category, price range, or brand. Make simultaneous calls for those segments, then merge the results.

**Note:** When using filters to emulate category pages, ensure `strictFiltering` is set to `True` in the parameters so that the model does not backfill with generic popular items when it runs out of matching results.

For prediction cost details, see [Pricing](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/pricing).

There are two workarounds for increasing the recommended result size.

#### Workaround A: Increase the page size

Configure the predict request's `pageSize` to a larger number than the default 20. See the REST API call template.

#### Workaround B: Use attribute and category pagination

The result limit workaround for category pages is comprised of three steps:

  1. **Configure attributes**. Mark attributes (like category or price) as filterable using the `CatalogService` API so they can be used in recommendation filters. Before filtering recommendations by an attribute (such as categories), you must enable the `recommendationsFilteringOption` for that attribute in your catalog configuration.
  2. **Generate recommendations**. Make a `PredictRequest` [using filterable attributes in a predict request](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/filter-recs#predict) to request specific product subsets.
  3. **Fetch and stitch filtered recommendations**. To simulate a larger result set or category page, make parallel requests with specific filters by invoking the [sample predict call](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/filter-recs#predict) from step 2 with a different category value in the filter.



#### Enable filtering option in the REST call

### curl

To get a recommendation, make a `POST` request to the [`predict`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.servingConfigs/predict) REST method and provide the appropriate request body:

  * The service account you use needs to have role "Retail Viewer" or above.

  * Replace SERVING_CONFIG_ID with the serving config where you will use the predictions. [Learn more](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/configs).

  * If you imported Google Analytics 360 user events [using BigQuery](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-user-events#bq-ga), set `visitorId` to the Google Analytics client ID. See the [Google Analytics documentation](https://developers.google.com/analytics/devguides/collection/analyticsjs/cookies-user-id#getting_the_client_id_from_the_cookie) for how to get the client ID.

  * If you are running an A/B experiment, set `experimentIds` to the ID for this experiment group. [Learn more](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/a-b-testing).

  * Provide a user event object for the user action that initiated the recommendation request.

Note that this user event is not recorded; it is only used to provide context for this recommendation request. You should also record the user event the same way you record other user events.

  * Optionally, provide a filter to narrow the potential products returned. Learn more.


**Note:** If your recommendation is not yet active, or you want to test your method call, you can call this method with the `validateOnly` flag set to `true`. This call returns a placeholder result, and does not incur charges. You can see whether your recommendation is active on the **Dashboard** tab.
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data '{
                  "filter": "FILTER_STRING",
                  "validateOnly": false,
                  "userEvent": {
                      "eventType": "detail-page-view",
                      "visitorId": "VISITOR_ID",
                      "userInfo": {
                          "userId": "USER_ID",
                          "ipAddress": "IP_ADDRESS",
                          "userAgent": "USER_AGENT"
                      },
                      "experimentIds": "EXPERIMENT_GROUP",
                      "productDetails": [{
                          "product": {
                            "id": "PRODUCT_ID"
                         }
                      }]
                  }
                }' \
    https://retail.googleapis.com/v2/projects/PROJECT_ID/locations/global/catalogs/default_catalog/servingConfigs/SERVING_CONFIG_ID:predict

You should see results similar to the following:
    
    
    {
      "results": [{"id": "sample-id-1"}, {"id": "sample-id-2"}],
      "attribution_token": "sample-atr-token"
    }

### Java
    
    
    public static PredictResponse predictWithNextPageToken(UserEvent userEvent, int pageSize,
        String nextPageToken)
        throws IOException, InterruptedException {
      PredictionServiceClient predictionClient = getPredictionServiceClient();
    
      PredictRequest request = PredictRequest.newBuilder()
          .setPlacement(HOME_PAGE_PLACEMENT_NAME)
          .setUserEvent(userEvent)
          .setPageSize(pageSize)
          .setPageToken(nextPageToken)
          .setValidateOnly(true)
          .build();
    
      PredictResponse response = predictionClient.predict(request);
    
      predictionClient.shutdownNow();
      predictionClient.awaitTermination(2, TimeUnit.SECONDS);
    
      return response;
    }

### Price reranking

Price reranking causes recommended products with a similar recommendation probability to be ordered by price, with the highest-priced items first. Relevance is still also used to order items, so enabling price reranking is not the same as sorting by price.

Price reranking can be set on the serving config level, or per prediction request.

When you choose a price reranking setting when [creating a serving config](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-configs) in the AI Commerce Search in Gemini Enterprise for Customer Experience console, that setting applies to all recommendations served by that configuration, without you having to take further action.

If you need to control the price reranking of a particular recommendation, you can do so using the [`PredictRequest.params`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.servingConfigs/predict#body.request_body.FIELDS.params) field. This overrides any configuration-level reranking setting that would otherwise apply to this recommendation.

### Recommendation diversity

Recommendation diversification affects whether results returned from a single prediction request are from different categories of your product catalog.

Recommendation diversification can be set on the serving config level, or per prediction request.

When you choose a recommendation diversification setting when [creating a serving config](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-configs) in the AI Commerce Search in Gemini Enterprise for Customer Experience console, that setting applies by default to all predictions served by that configuration, without you having to take further action.

If you need to control the diversity of a particular recommendation, you can do so using the [`PredictRequest.params`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.servingConfigs/predict#body.request_body.FIELDS.params) field. This overrides any configuration-level diversification setting that would otherwise apply to this recommendation. See for accepted values.

### Use recommendation filters

You can filter the recommendations returned by recommendations by using the `filter` field in the `predict` method. For information, see [Filter recommendations](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/filter-recs).

### Prediction calls with Page-Level Optimization models

Providing recommendations using [Page-Level Optimization](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/models#plo) requires an extra prediction call step.

Make an initial prediction call using a serving config containing the Page-Level Optimization model. The prediction response returns a sorted list of serving config IDs representing the model to use for each panel.

Then make a prediction call for each panel using the serving config ID that the Page-Level Optimization model recommended for it. The prediction response contains the model name (such as Recommended for You) and list of recommended items to display in that panel.

Price reranking, recommendation diversity, and recommendation filters are not available for serving configs using the Page-Level Optimization model.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
