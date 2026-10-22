---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-controls/
title: Create serving controls \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:21.659125+00:00
---

# Create serving controls  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Create serving controls Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create serving controls.

Serving controls are rules that you define and apply to individual serving configs.

You can create a serving control in the AI Commerce Search in Gemini Enterprise for Customer Experience console consisting of a condition, which triggers the control, and an action that takes place when the condition triggers. You can then attach the new serving control to a serving configuration.

## Relationship between serving controls and configs

Serving configs have a multi-to-multi relationship with controls. You can add multiple controls to a serving config, and a single control can be associated with multiple serving configs.

When you create serving controls and serving configs, you select a product (recommendations or search) that the control can be used for.

Serving controls can be associated only with serving configs of the same product type. For example, a serving control created for recommendations can't be associated with a serving config that was created for search.

![Serving configurations](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/Serving-controls-and-configs.jpg)

Serving configs manage which controls are applied during a search or prediction request. Only the controls on the active serving config for a request are considered at serving time. For example, suppose you have created two controls: a control called **gShoe Sale** that boosts results for the brand gShoe when _shoes_ is searched for and a control called **More shoes** that expands queries using the term _running shoes_ to include _sport shoes._ If you attach only the **gShoe Sale** control to a serving config, then search requests using that serving config boosts gShoe results for queries using the term _shoes,_ but the **More shoes** control has no effect because it is not attached to the serving config you are using.

For more information, refer to [About serving configs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/configs).

## Quickstart videos and guides

  * **Introduction to serving controls** : Serving controls enable you to create rules that customize how your serving configurations return search results. 

  * **Boost/bury** : Affects result ranking and order in the returned result list. Available for search and recommendations. 

  * **Filter** : Removes results that do not pass the filter from the returned result list. Available for search only. 

  * **Redirect** : Redirects your users to a specific page depending on the search query. Available for search only. 




This tutorial shows you to how to use the redirect control.

* * *

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_redirect_control_select_language&show=ide&environment_deployment=ide)

* * *

  * **Linguistic** : Customizes search query linguistics. Available for search only. 

Several types of linguistic controls are available: 
    * **Synonym** : Expands considered synonyms for a search query.
    * **One-way synonym** : Expands considered synonyms unidirectionally for specific terms.
    * **Do not associate** : Prevent a group of terms from being used in search when specific terms appear.
    * **Ignore** : Prevent a term from being used in searches.
    * **Replacement** : Replaces terms in the search query.
  * **Pinning** : Affects result ordering, placing a result at a specific position — for example, at position 4. Available for search and browse.



For examples of these controls, see [About serving controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/serving-control-rules).

**Note:** Creating chaining or conflicting controls is not recommended. AI Commerce Search doesn't support running controls in a predetermined order.

## Serving control configuration options

You can create controls and then add or swap them into a live serving configuration.

You can create up to 100 serving controls in AI Commerce Search. If you need more serving controls, request additional quota. To do so, follow the steps in [Increase your quotas](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/quotas#increase-your-quotas).

A serving config can have up to 100 serving controls of any type, with the exception of search redirect controls, whose limit can be up to 1,000 per serving config. Keep in mind that your quota for controls on one serving config may differ from the overall quota allowed for a control type in your AI Commerce Search API.

**Note:** There is a five-minute delay from when a control is attached to ready for use in serving. The preview page and search requests will reflect this delay.

You can create a serving control in these ways:

  * On the [Controls page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/controls/) in the Google Cloud console: Here, you can optionally create controls during the [serving config creation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-configs) process.

  * You can use the [Merchandising console](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/merchandising-controls#use-merchandising-console).

  * You can create a serving control inline, using the `Controls.create` method.




To use the Google Cloud console to create serving controls:

  1. Go to the **Controls** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Controls page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/controls/)

  2. Follow the Google Cloud console steps under each serving control section.




## Control types

Controls have different requirements depending on their type. Go to the creation procedure for the control type you plan to create:

  * Create a boost/bury control
  * Create a filter control
  * Create a redirect control
  * Create a pinning control
  * Create a two-way synonym control
  * Create a one-way synonym control
  * Create a do-not-associate control
  * Create an ignore control
  * Create a replacement control



### Create a boost/bury control

This control type is available for search and recommendations.

  * Create a search boost/bury control
  * Create a recommendations boost/bury control



See [Boost/bury controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/serving-control-rules#boost-bury) for more about this control type.

#### Create a search boost/bury control

To create a search boost/bury control:

###  Cloud console 

  1. Go to the **Controls** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Controls page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/controls/)

  2. Under the **Serving controls** tab, click _add_box_**Create control**.

The **Create control** pane opens.

  3. In the **Preferences** section, in the **Control name** field, enter a name for your new control.

  4. Optional: To change the automatically created control ID, click **Edit** and enter a new control ID.

  5. In the **Product selection** section, select **Search**.

  6. Choose **Boost/bury controls** as the control type. Click **Continue**

  7. In the **Triggers** section, select what type of user behavior triggers this control.

     * **Browse categories** : The rule is triggered when a user browses categories on your site ([`search.request.query`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.query) is empty).

     * **Search** : The rule is triggered when a user searches on your site ([`search.request.query`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.query) isn't empty). To set this control to trigger when any category is browsed, or any query is searched for, skip the following step.

  8. Optional: Set specific categories or queries that can trigger this control depending on whether a specific category is browsed or a specific query is searched for.

     * If you chose **Browse categories** : In the **Categories** field, enter which categories will trigger this control when browsed.

     * If you chose **Search** : Click the **Add query** button to add query terms (for example, `running shoes`) to be filtered. For each term, choose either **Partial match** or **Full match**.

**Note:** If you specify a category or query term condition in addition to a time range conditions, the control is applied only when both conditions are met.
  9. Optional: Click the **Add Time Range** button to add one or more time ranges during which this control can be applied.

**Note:** If you specify time range conditions in addition to this type of condition, the control is applied only if both conditions are met.
  10. Click **Continue** to proceed to the **Actions** section.

  11. Add filters for product attributes in the **Boost/bury product** field.

Use the filter expression syntax documented in [Filtering and ordering](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/filter-and-order#filter). For example, to specify red and blue versions of "product1" and "product2": `(id: ANY("product1","product2")) AND (colorFamily: ANY("Red","Blue"))`

  12. For **Boost/bury value** , use the slider to set the strength of the boost. Positive values boost the results, and negative values bury them. Click **Continue**.

  13. In the **Serving configs** section, select which serving configs to apply the control to.

  14. Submit your control settings.

It takes a few minutes for newly created or updated controls to be ready to serve live traffic. You can test if your changes have been applied on the console [**Evaluate** ](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/evaluate/) page. 




You can now find the new control listed on the **Serving controls** tab of the **Controls** page.

###  curl 

Make a `Control.create` request with a control ID and an instance of `Control` contained in the request body.

For field details, see the [`Controls` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls) and the [`Controls.create` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls/create).

A boost/bury control can be triggered when a user browses categories on your site ([`search.request.query`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.query) is empty), or when a user searches on your site ([`search.request.query`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.query) isn't empty).

The following example shows fields for a browse-triggered control, where `searchSolutionUseCase` is set to `SEARCH_SOLUTION_USE_CASE_BROWSE`.
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         --data '{
                  "displayName": "DISPLAY_NAME",
                  "solutionTypes": [ "SOLUTION_TYPE_SEARCH" ],
                  "searchSolutionUseCase": [
                    "SEARCH_SOLUTION_USE_CASE_BROWSE"
                  ],
                  "rule": {
                    "condition": {
                      "pageCategories": [
                          "CATEGORY_ABC",
                          "CATEGORY_XYZ"
                      ],
                      "activeTimeRange": [
                        {
                          "startTime": "START_TIMESTAMP_1",
                          "endTime": "END_TIMESTAMP_1"
                        },
                        {
                          "startTime": "START_TIMESTAMP_2",
                          "endTime": "END_TIMESTAMP_2"
                        }
                      ]
                    },
                    "boostAction": {
                      "boost": BOOST_NUMBER,
                      "productsFilter": "FILTER_EXPRESSION"
                    }
                  }
        }' \
        "https://retail.googleapis.com/v2beta/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/controls?controlId=CONTROL_ID"

The following example shows fields for a search-triggered control, where `searchSolutionUseCase` is set to `SEARCH_SOLUTION_USE_CASE_SEARCH`.
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         --data '{
                  "displayName": "DISPLAY_NAME",
                  "solutionTypes": [ "SOLUTION_TYPE_SEARCH" ],
                  "searchSolutionUseCase": [
                    "SEARCH_SOLUTION_USE_CASE_SEARCH"
                  ],
                  "rule": {
                    "condition": {
                      "queryTerms": [
                        {
                          "value": "VALUE_1",
                          "fullMatch": "FULLMATCH_BOOLEAN_1"
                        },
                        {
                          "value": "VALUE_2",
                          "fullMatch": "FULLMATCH_BOOLEAN_2"
                        }
                      ],
                      "activeTimeRange": [
                        {
                          "startTime": "START_TIMESTAMP_1",
                          "endTime": "END_TIMESTAMP_1"
                        },
                        {
                          "startTime": "START_TIMESTAMP_2",
                          "endTime": "END_TIMESTAMP_2"
                        }
                      ]
                    },
                    "boostAction": {
                      "boost": BOOST_NUMBER,
                      "productsFilter": "FILTER_EXPRESSION"
                    }
                  }
        }' \
        "https://retail.googleapis.com/v2beta/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/controls?controlId=CONTROL_ID"
      

It takes a few minutes for newly created or updated controls to be ready to serve live traffic. You can test if your changes have been applied on the console [**Evaluate** ](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/evaluate/) page. 

To add a control to a serving config, use the `ServingConfig.addControl` method:

  * For more about this method, see the [`ServingConfig.addControl` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/addControl).

  * For an example of this method, see [Manage serving configs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-configs). 




#### Create a recommendations boost/bury control

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To create a recommendations boost/bury control:

###  Cloud console 

  1. Go to the **Controls** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Controls page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/controls/)

  2. On the **Serving controls** tab, click _add_box_**Create control**.

The **Create control** pane opens.

  3. In the **Preferences** section, in the **Control name** field, enter a name for your new control.

  4. (Optional) To change the automatically created control ID, click **Edit** and enter a new control ID.

  5. In the **Product selection** section, select **Recommendation**.

  6. Choose **Boost/bury controls** as the control type.

  7. Click **Continue** to proceed to the **Actions** section.

  8. Add filters for product attributes in the **Boost/bury product** field.

Use the filter expression syntax documented in [Filter recommendations](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/filter-recs).

For example, to specify red and blue versions of "product1" and "product2": `(id: ANY("product1","product2")) AND (colorFamily: ANY("Red","Blue"))`

  9. For **Boost/bury value** , use the slider to set the strength of the boost. Positive values boost the results, and negative values bury them.

  10. Click **Continue** to proceed to the **Serving configs** section.

  11. Select which serving configs to apply the control to.

  12. Submit your control settings.

It takes a few minutes for newly created or updated controls to be ready to serve live traffic. You can test if your changes have been applied on the console [**Evaluate** ](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/evaluate/) page. 




You can find the new control listed on the **Serving controls** tab of the **Controls** page.

###  curl 

Make a `Control.create` request with a control ID and an instance of `Control` contained in the request body.

For field details, see the [`Controls` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls) and the [`Controls.create` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls/create).

To create a filter expression, use the filter expression syntax documented in [Filter recommendations](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/filter-recs).
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         --data '{
                  "displayName": "DISPLAY_NAME",
                  "solutionTypes": [ "SOLUTION_TYPE_RECOMMENDATION" ],
                    "boostAction": {
                      "boost": BOOST_NUMBER,
                      "productsFilter": "FILTER_EXPRESSION"
                    }
                  }
        }' \
        "https://retail.googleapis.com/v2beta/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/controls?controlId=CONTROL_ID"
       

It takes a few minutes for newly created or updated controls to be ready to serve live traffic. You can test if your changes have been applied on the console [**Evaluate** ](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/evaluate/) page. 

To add a control to a serving config, use the `ServingConfig.addControl` method:

  * For more about this method, see the [`ServingConfig.addControl` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/addControl).

  * For an example of this method, see [Manage serving configs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-configs). 




### Create a filter control

See [Filter controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/serving-control-rules#filter) for more about this control type.

###  Cloud console 

  1. Go to the **Controls** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Controls page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/controls/)

  2. On the **Serving controls** tab, click _add_box_**Create control**.

The **Create control** pane opens.

  3. In the **Preferences** section, in the **Control name** field, enter a name for your new control.

  4. Optional: To change the automatically created control ID, click **Edit** and enter a new control ID.

  5. Choose **Filter controls** as the control type.

  6. Click continue to proceed to the **Triggers** section.

  7. Select what type of user behavior triggers this control:

     * **Browse categories** : The rule is triggered when a user browses categories on your site ([`search.request.query`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.query) is empty).

     * **Search** : The rule is triggered when a user searches on your site ([`search.request.query`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.query) isn't empty).

  8. Optional: Set a control condition that triggers the rule based on what category is browsed, or what query is searched for. The available option depends on if you chose **Browse categories** or **Search** :

     * If you chose **Browse categories** : In the **Categories** field, enter which categories will trigger this control when browsed.

     * If you chose **Search** : Click the **Add query** button to add query terms (for example, `running shoes`) to be filtered, and select one of the following for each term:

       * **Partial match** : This control applies when a query contains a partial match to this query term.
       * **Full match** : This control applies only when a query contains a full match to this query term.

When one of these terms is included in a query, the control is applied.

**Note:** If you specify a time range condition in addition to this condition, the control is applied only if both conditions are met.
  9. Optional: Click the **Add Time Range** button to add one or more time ranges during which this control can be applied.

**Note:** If you specify a category or query term condition in addition to this time range condition, the control is applied only when both conditions are met.
  10. Click **Continue** to proceed to the **Actions** section.

  11. Add filters for product attributes in the **Filter action** field.

Use the filter expression syntax documented in [Filtering and ordering](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/filter-and-order#filter).

For example, to specify red and blue versions of "product1" and "product2": `(id: ANY("product1","product2")) AND (colorFamily: ANY("Red","Blue"))`

  12. Click **Continue** to proceed to the **Serving configs** section.

  13. Select which serving configs to apply the control to.

  14. Submit your control settings.

It takes a few minutes for newly created or updated controls to be ready to serve live traffic. You can test if your changes have been applied on the console [**Evaluate** ](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/evaluate/) page. 




You can find the new control listed on the **Serving controls** tab of the **Controls** page.

###  curl 

Make a `Control.create` request with a control ID and an instance of `Control` contained in the request body.

For field details, see the [`Controls` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls) and the [`Controls.create` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls/create).

A filter control can be triggered when a user browses categories on your site ([`search.request.query`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.query) is empty), or when a user searches on your site ([`search.request.query`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.query) isn't empty).

The following example shows fields for a browse-triggered control, where `searchSolutionUseCase` is set to `SEARCH_SOLUTION_USE_CASE_BROWSE`.
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         --data '{
                  "displayName": "DISPLAY_NAME",
                  "solutionTypes": [ "SOLUTION_TYPE_SEARCH" ],
                  "searchSolutionUseCase": [
                    "SEARCH_SOLUTION_USE_CASE_BROWSE"
                  ],
                  "rule": {
                    "condition": {
                      "pageCategories": [
                          "CATEGORY_ABC",
                          "CATEGORY_XYZ"
                      ],
                      "activeTimeRange": [
                        {
                          "startTime": "START_TIMESTAMP_1",
                          "endTime": "END_TIMESTAMP_1"
                        },
                        {
                          "startTime": "START_TIMESTAMP_2",
                          "endTime": "END_TIMESTAMP_2"
                        }
                      ]
                    },
                    "filterAction": {
                      "filter": "FILTER_EXPRESSION"
                    }
                  }
        }' \
        "https://retail.googleapis.com/v2beta/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/controls?controlId=CONTROL_ID"

The following example shows fields for a search-triggered control, where `searchSolutionUseCase` is set to `SEARCH_SOLUTION_USE_CASE_SEARCH`.
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         --data '{
                  "displayName": "DISPLAY_NAME",
                  "solutionTypes": [ "SOLUTION_TYPE_SEARCH" ],
                  "searchSolutionUseCase": [
                    "SEARCH_SOLUTION_USE_CASE_SEARCH"
                  ],
                  "rule": {
                    "condition": {
                      "pageCategories": [
                          "CATEGORY_ABC",
                          "CATEGORY_XYZ"
                      ],
                      "activeTimeRange": [
                        {
                          "startTime": "START_TIMESTAMP_1",
                          "endTime": "END_TIMESTAMP_1"
                        },
                        {
                          "startTime": "START_TIMESTAMP_2",
                          "endTime": "END_TIMESTAMP_2"
                        }
                      ]
                    },
                    "filterAction": {
                      "filter": "FILTER_EXPRESSION"
                    }
                  }
        }' \
        "https://retail.googleapis.com/v2beta/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/controls?controlId=CONTROL_ID"
      

To add a control to a serving config, use the `ServingConfig.addControl` method:

  * For more about this method, see the [`ServingConfig.addControl` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/addControl).

  * For an example of this method, see [Manage serving configs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-configs). 




### Create a redirect control

See [Redirect controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/serving-control-rules#redirect) for more about this control type.

###  Cloud console 

  1. Go to the **Controls** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Controls page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/controls/)

  2. On the **Serving controls** tab, click _add_box_**Create control**.

The **Create control** pane opens.

  3. In the **Preferences** section, in the **Control name** field, enter a name for your new control.

  4. Optional: To change the automatically created control ID, click **Edit** and enter a new control ID.

  5. Choose **Redirect controls** as the control type.

  6. Click continue to proceed to the **Triggers** section.

  7. Create at least one query term or time range trigger. Redirect controls require at least one trigger:

  8. Select what type of user behavior triggers this control:

     * **Browse categories** : The rule is triggered when a user browses categories on your site ([`search.request.query`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.query) is empty).

     * **Search** : The rule is triggered when a user searches on your site ([`search.request.query`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.query) isn't empty).

  9. Set a control condition that triggers the rule based on what category is browsed, or what query is searched for. The available option depends on if you chose **Browse categories** or **Search** :

     * If you chose **Browse categories** : In the **Categories** field, enter which categories will trigger this control when browsed.

     * If you chose **Search** : Click the **Add query** button to add query terms (for example, `running shoes`) to be filtered, and select one of the following for each term:

       * **Partial match** : This control applies when a query contains a partial match to this query term.
       * **Full match** : This control applies only when a query contains a full match to this query term.

When one of these terms is included in a query, the control is applied.

**Note:** If you specify a time range condition in addition to this condition, the control is applied only if both conditions are met.
  10. Click the **Add Time Range** button to add one or more time ranges during which this control can be applied.

**Note:** If you specify a category or query term condition in addition to this time range condition, the control is applied only when both conditions are met.
  11. Click **Continue** to proceed to the **Actions** section.

  12. Enter the URI to redirect to when this control is triggered.

  13. Click **Continue** to proceed to the **Serving configs** section.

  14. Select which serving configs to apply the control to.

  15. Submit your control settings.

It takes a few minutes for newly created or updated controls to be ready to serve live traffic. You can test if your changes have been applied on the console [**Evaluate** ](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/evaluate/) page. 




You can find the new control listed on the **Serving controls** tab of the Controls page.

###  curl 

Make a `Control.create` request with a control ID and an instance of `Control` contained in the request body.

For field details, see the [`Controls` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls) and the [`Controls.create` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls/create).

A redirect control can be triggered when a user browses categories on your site ([`search.request.query`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.query) is empty), or when a user searches on your site ([`search.request.query`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.query) isn't empty).

The following example shows fields for a browse-triggered control, where `searchSolutionUseCase` is set to `SEARCH_SOLUTION_USE_CASE_BROWSE`.
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         --data '{
                  "displayName": "DISPLAY_NAME",
                  "solutionTypes": [ "SOLUTION_TYPE_SEARCH" ],
                  "searchSolutionUseCase": [
                    "SEARCH_SOLUTION_USE_CASE_BROWSE"
                  ],
                  "rule": {
                    "condition": {
                      "queryTerms": [
                        {
                          "value": "VALUE_1",
                          "fullMatch": "FULLMATCH_BOOLEAN_1"
                        },
                        {
                          "value": "VALUE_2",
                          "fullMatch": "FULLMATCH_BOOLEAN_2"
                        }
                      ],
                      "activeTimeRange": [
                        {
                          "startTime": "START_TIMESTAMP_1",
                          "endTime": "END_TIMESTAMP_1"
                        },
                        {
                          "startTime": "START_TIMESTAMP_2",
                          "endTime": "END_TIMESTAMP_2"
                        }
                      ]
                    },
                    "redirectAction": {
                      "redirectUri": "REDIRECT_URI",
                    }
                  }
        }' \
        "https://retail.googleapis.com/v2beta/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/controls?controlId=CONTROL_ID"

The following example shows fields for a search-triggered control, where `searchSolutionUseCase` is set to `SEARCH_SOLUTION_USE_CASE_SEARCH`.
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         --data '{
                  "displayName": "DISPLAY_NAME",
                  "solutionTypes": [ "SOLUTION_TYPE_SEARCH" ],
                  "searchSolutionUseCase": [
                    "SEARCH_SOLUTION_USE_CASE_SEARCH"
                  ],
                  "rule": {
                    "condition": {
                      "queryTerms": [
                        {
                          "value": "VALUE_1",
                          "fullMatch": "FULLMATCH_BOOLEAN_1"
                        },
                        {
                          "value": "VALUE_2",
                          "fullMatch": "FULLMATCH_BOOLEAN_2"
                        }
                      ],
                      "activeTimeRange": [
                        {
                          "startTime": "START_TIMESTAMP_1",
                          "endTime": "END_TIMESTAMP_1"
                        },
                        {
                          "startTime": "START_TIMESTAMP_2",
                          "endTime": "END_TIMESTAMP_2"
                        }
                      ]
                    },
                    "redirectAction": {
                      "redirectUri": "REDIRECT_URI",
                    }
                  }
        }' \
        "https://retail.googleapis.com/v2beta/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/controls?controlId=CONTROL_ID"
      

To add a control to a serving config, use the `ServingConfig.addControl` method:

  * For more about this method, see the [`ServingConfig.addControl` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/addControl).

  * For an example of this method, see [Manage serving configs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-configs). 




### Create a two-way synonym control

See [Two-way synonym controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/serving-control-rules#synonym) for more about this control type.

###  Cloud console 

  1. Go to the **Controls** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Controls page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/controls/)

  2. On the **Serving controls** tab, click _add_box_**Create control**.

  3. In the **Control name** field, enter a name for your new control.

The **Create control** pane opens.

  4. You will be in the **Preferences** section.

  5. Optional: To change the automatically created control ID, click **Edit** and enter a new control ID.

  6. Choose **Two-way synonym control** as the control type.

  7. Click continue to proceed to the **Triggers** section.

  8. Optional: Click the **Add Time Range** button to add one or more time ranges during which this control can be applied.

  9. Click **Continue** to proceed to the **Actions** section.

  10. In the **Synonyms** field, enter 2 to 100 query terms (for example, `shirt` and `top`) that should be synonyms of each other.

When any one of these terms is included in a query, search considers the other query terms as synonyms of the included term.

  11. Click **Continue** to proceed to the **Serving configs** section.

  12. Select which serving configs to apply the control to.

  13. Submit your control settings.

It takes a few minutes for newly created or updated controls to be ready to serve live traffic. You can test if your changes have been applied on the console [**Evaluate** ](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/evaluate/) page. 




You can find the new control listed on the **Serving controls** tab of the Controls page.

###  curl 

Make a `Control.create` request with a control ID and an instance of `Control` contained in the request body.

For field details, see the [`Controls` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls) and the [`Controls.create` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls/create).
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         --data '{
                  "displayName": "DISPLAY_NAME",
                  "solutionTypes": [ "SOLUTION_TYPE_SEARCH" ],
                  "rule": {
                    "condition": {
                      "activeTimeRange": [
                        {
                          "startTime": "START_TIMESTAMP_1",
                          "endTime": "END_TIMESTAMP_1"
                        },
                        {
                          "startTime": "START_TIMESTAMP_2",
                          "endTime": "END_TIMESTAMP_2"
                        }
                        ]
                    },
                    "twoWaySynonymAction": {
                      "synonyms": [
                        "SYNONYM_1",
                        "SYNONYM_2"
                      ]
                    }
                  }
        }' \
        "https://retail.googleapis.com/v2beta/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/controls?controlId=CONTROL_ID"
      

To add a control to a serving config, use the `ServingConfig.addControl` method. See [Add controls to serving configs inline](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-configs#addcontrol-inline).

### Create a one-way synonym control

See [One-way synonym controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/serving-control-rules#one-way) for more about this control type.

###  Cloud console 

  1. Go to the **Controls** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Controls page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/controls/)

  2. On the **Serving controls** tab, click _add_box_**Create control**.

The **Create control** pane opens.

  3. In the **Preferences** section, in the **Control name** field, enter a name for your new control.

  4. Optional: To change the automatically created control ID, click **Edit** and enter a new control ID.

  5. Choose **One-way synonym control** as the control type.

  6. Click continue to proceed to the **Triggers** section.

  7. Optional: Click the **Add Time Range** button to add one or more time ranges during which this control can be applied.

  8. Click **Continue** to proceed to the **Actions** section.

  9. In the **Query terms** field, enter terms (for example, `shoes`) that should have synonyms associated with them when any of them is included in a query.

  10. In the **Synonyms** field, enter terms that should be used as synonyms for the query terms you specified (for example, `sneakers` and `sandals` as one-way synonyms for the query term `shoes`).

  11. Click **Continue** to proceed to the **Serving configs** section.

  12. Select which serving configs to apply the control to.

  13. Submit your control settings.

It takes a few minutes for newly created or updated controls to be ready to serve live traffic. You can test if your changes have been applied on the console [**Evaluate** ](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/evaluate/) page. 




You can find the new control listed on the **Serving controls** tab of the Controls page.

###  curl 

Make a `Control.create` request with a control ID and an instance of `Control` contained in the request body.

For field details, see the [`Controls` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls) and the [`Controls.create` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls/create).
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         --data '{
                  "displayName": "DISPLAY_NAME",
                  "solutionTypes": [ "SOLUTION_TYPE_SEARCH" ],
                  "rule": {
                    "condition": {
                      "activeTimeRange": [
                        {
                          "startTime": "START_TIMESTAMP_1",
                          "endTime": "END_TIMESTAMP_1"
                        },
                        {
                          "startTime": "START_TIMESTAMP_2",
                          "endTime": "END_TIMESTAMP_2"
                        }
                      ]
                    },
                    "oneWaySynonymAction": {
                      "synonyms": [
                        "queryTerms": [
                          "QUERY_TERM_1",
                          "QUERY_TERM_2"
                        ],
                        "synonyms": [
                          "SYNONYM_1",
                          "SYNONYM_2"
                        ]
                      ]
                    }
                  }
        }' \
        "https://retail.googleapis.com/v2beta/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/controls?controlId=CONTROL_ID"
      

To add a control to a serving config, use the `ServingConfig.addControl` method:

  * For more about this method, see the [`ServingConfig.addControl` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/addControl).

  * For an example of this method, see [Manage serving configs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-configs). 




### Create a do-not-associate control

See [Do-not-associate control rules](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/serving-control-rules#do-not-associate) for more about this control type.

###  Cloud console 

  1. Go to the **Controls** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Controls page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/controls/)

  2. On the **Serving controls** tab, click _add_box_**Create control**.

The **Create control** pane opens.

  3. In the **Preferences** section, in the **Control name** field, enter a name for your new control.

  4. Optional: To change the automatically created control ID, click **Edit** and enter a new control ID.

  5. Choose **Do not associate control** as the control type.

  6. Click continue to proceed to the **Triggers** section.

  7. Optional: Click the **Add Time Range** button to add one or more time ranges during which this control can be applied.

  8. Click **Continue** to proceed to the **Actions** section.

  9. In the **Query terms** field, enter terms (for example, `gShoe`) that you want to explicitly disambiguate from others.

  10. In the **Dissociated terms** field, enter terms that to be disassociated from search results with the query terms you have specified.

For example, you can dissociate the query term `gShoe` from the term `cheap`.

  11. Click **Continue** to proceed to the **Serving configs** section.

  12. Select which serving configs to apply the control to.

  13. Submit your control settings.

It takes a few minutes for newly created or updated controls to be ready to serve live traffic. You can test if your changes have been applied on the console [**Evaluate** ](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/evaluate/) page. 




You can find the new control listed on the **Serving controls** tab of the Controls page.

###  curl 

Make a `Control.create` request with a control ID and an instance of `Control` contained in the request body.

For field details, see the [`Controls` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls) and the [`Controls.create` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls/create).
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         --data '{
                  "displayName": "DISPLAY_NAME",
                  "solutionTypes": [ "SOLUTION_TYPE_SEARCH" ],
                  "rule": {
                    "condition": {
                      "activeTimeRange": [
                        {
                          "startTime": "START_TIMESTAMP_1",
                          "endTime": "END_TIMESTAMP_1"
                        },
                        {
                          "startTime": "START_TIMESTAMP_2",
                          "endTime": "END_TIMESTAMP_2"
                        }
                      ]
                    },
                    "doNotAssociateAction": {
                        "queryTerms": [
                          "QUERY_TERM_1",
                          "QUERY_TERM_2"
                        ],
                        "doNotAssociateTerms": [
                          "DISSOCIATED_TERM_1",
                          "DISSOCIATED_TERM_2"
                        ]
                      ]
                    }
                  }
        }' \
        "https://retail.googleapis.com/v2beta/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/controls?controlId=CONTROL_ID"
      

To add a control to a serving config, use the `ServingConfig.addControl` method:

  * For more about this method, see the [`ServingConfig.addControl` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/addControl).

  * For an example of this method, see [Manage serving configs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-configs). 




### Create an ignore control

See [Ignore controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/serving-control-rules#ignore) for more about this control type.

###  Cloud console 

  1. Go to the **Controls** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Controls page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/controls/)

  2. On the **Serving controls** tab, click _add_box_**Create control**.

The **Create control** pane opens.

  3. In the **Preferences** section, in the **Control name** field, enter a name for your new control.

  4. Optional: To change the automatically created control ID, click **Edit** and enter a new control ID.

  5. Choose **Do not associate control** as the control type.

  6. Click continue to proceed to the **Triggers** section.

  7. Optional: Click the **Add Time Range** button to add one or more time ranges during which this control can be applied.

  8. Click **Continue** to proceed to the **Actions** section.

  9. In the **Ignore terms** field, enter terms (for example, `shoddy`) that you want a search to ignore when they are entered as query terms.

  10. Click **Continue** to proceed to the **Serving configs** section.

  11. Select which serving configs to apply the control to.

  12. Submit your control settings.

It takes a few minutes for newly created or updated controls to be ready to serve live traffic. You can test if your changes have been applied on the console [**Evaluate** ](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/evaluate/) page. 




You can find the new control listed on the **Serving controls** tab of the Controls page.

###  curl 

Make a `Control.create` request with a control ID and an instance of `Control` contained in the request body.

For field details, see the [`Controls` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls) and the [`Controls.create` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls/create).
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         --data '{
                  "displayName": "DISPLAY_NAME",
                  "solutionTypes": [ "SOLUTION_TYPE_SEARCH" ],
                  "rule": {
                    "condition": {
                      "activeTimeRange": [
                        {
                          "startTime": "START_TIMESTAMP_1",
                          "endTime": "END_TIMESTAMP_1"
                        },
                        {
                          "startTime": "START_TIMESTAMP_2",
                          "endTime": "END_TIMESTAMP_2"
                        }
                      ]
                    },
                    "ignoreAction": {
                      "ignoreTerms": [
                          "IGNORE_TERM_1",
                          "IGNORE_TERM_2"
                        ]
                      ]
                    }
                  }
        }' \
        "https://retail.googleapis.com/v2beta/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/controls?controlId=CONTROL_ID"
      

To add a control to a serving config, use the `ServingConfig.addControl` method:

  * For more about this method, see the [`ServingConfig.addControl` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/addControl).

  * For an example of this method, see [Manage serving configs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-configs). 




### Create a replacement control

See [Replacement controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/serving-control-rules#replacement) for more about this control type.

###  Cloud console 

  1. Go to the **Controls** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Controls page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/controls/)

  2. On the **Serving controls** tab, click _add_box_**Create control**.

The **Create control** pane opens.

  3. In the **Preferences** section, in the **Control name** field, enter a name for your new control.

  4. Optional: To change the automatically created control ID, click **Edit** and enter a new control ID.

  5. Choose **Replacement control** as the control type.

  6. Click continue to proceed to the **Triggers** section.

  7. Optional: Click the **Add Time Range** button to add one or more time ranges during which this control can be applied.

  8. Click **Continue** to proceed to the **Actions** section.

  9. In the **Query terms** field, enter query terms (for example, `gShoe`) that you want to have replaced by the replacement term.

  10. In the **Replacement term** field, enter the term that should replace the query terms you specified.

For example, you can replace the query term `gShoe` with the replacement term `Google Shoe`.

  11. Click **Continue** to proceed to the **Serving configs** section.

  12. Select which serving configs to apply the control to.

  13. Submit your control settings.

It takes a few minutes for newly created or updated controls to be ready to serve live traffic. You can test if your changes have been applied on the console [**Evaluate** ](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/evaluate/) page. 




You can find the new control listed on the **Serving controls** tab of the Controls page.

###  curl 

Make a `Control.create` request with a control ID and an instance of `Control` contained in the request body.

For field details, see the [`Controls` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls) and the [`Controls.create` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls/create).
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         --data '{
                  "displayName": "DISPLAY_NAME",
                  "solutionTypes": [ "SOLUTION_TYPE_SEARCH" ],
                  "rule": {
                    "condition": {
                      "activeTimeRange": [
                        {
                          "startTime": "START_TIMESTAMP_1",
                          "endTime": "END_TIMESTAMP_1"
                        },
                        {
                          "startTime": "START_TIMESTAMP_2",
                          "endTime": "END_TIMESTAMP_2"
                        }
                      ]
                    },
                    "replacementAction": {
                        "queryTerms": [
                          "QUERY_TERM_1",
                          "QUERY_TERM_2"
                        ],
                        "replacementTerm": "REPLACEMENT_TERM"
                      }
                    }
                  }
        }' \
        "https://retail.googleapis.com/v2beta/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/controls?controlId=CONTROL_ID"
      

To add a control to a serving config, use the `ServingConfig.addControl` method:

  * For more about this method, see the [`ServingConfig.addControl` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/addControl).

  * For an example of this method, see [Manage serving configs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-configs). 




### Create a pinning control

To create a pinning control:

###  Cloud console 

  1. Go to the **Controls** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Controls page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/controls/)

  2. On the **Serving controls** tab, click _add_box_**Create control**.

The **Create control** pane opens.

  3. In the **Control name** field of the **Preferences** section, enter a name for your new control.

  4. Optional: To change the automatically created control ID, click **Edit** and enter a new control ID.

  5. In the **Product selection** section, select **Search or Browse**.

  6. Choose **Pinning control** as the control type. Click **Continue**.

  7. In the **Triggers** section, choose the user behavior that triggers this control:

     * **Browse categories** : Browse requests are required to have the `page_categories` field populated in addition to the [`search.request.query`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.query) being empty.

     * **Search** : Search requests require only the [`search.request.query`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.query) to be populated.

By default, all categories browsed and queries searched trigger this control.

  8. Optional: Set a condition that triggers the rule based on a particular category browsed or query searched for:

     * **Browse categories** : In the **Categories** field, enter which categories trigger the control.

     * **Search** : To add query terms to be filtered (for example, `running shoes`), click **Add query**. For each term, choose **Partial match** or **Full match**.

  9. Optional: Click **Add Time Range** or **Add Date Range** to add one or more time ranges during which this control can be applied.

**Note:** If you specify a category or query term plus time- or date-range conditions, the control is applied only if both types of conditions are met.
  10. Click **Continue** to proceed to the **Actions** section. For **Pin location** , use the slider to specify which position the products are to be pinned to. The pin value slider won't accept values of 0, negative numbers, or non-integers.

AI Commerce Search allows 10 pins in the pin map of any single control. The position can be any value between 1 and 120 (the maximum request page size).

**Note:** Pins to the second page are not honored if the position is greater than the request page size. For example, if a search query requests a page size of 50 but you have set a pin to page 75, the search item will be ignored in the results.
  11. Click **Continue** to proceed to the **Serving configs** section. Select which serving configs to apply the control to, and submit your control settings.

It takes a few minutes for newly created or updated controls to be ready to serve live traffic. You can test if your changes have been applied on the console [**Evaluate** ](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/evaluate/) page. 




You can find the new control listed on the **Serving controls** tab of the **Controls** page.

###  curl 

Make a [`Control.create`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls/create) request with a control ID and an instance of `Control` contained in the request body.

For field details, see the [`Controls` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls) and the [`Controls.create` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls/create).
    
    
    curl -X POST \
     -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
     -H "Content-Type: application/json; charset=utf-8" \
     -H "X-Goog-User-Project: PROJECT_NUMBER" \
     --data '{
              "displayName": "DisplayName",
              "solutionTypes": "SOLUTION_TYPE_SEARCH",
              "searchSolutionUseCase": ["SEARCH_SOLUTION_USE_CASE_SEARCH"],
         "rule": {
                "condition": {
     "queryTerms": [
                    {
                      "value": "Term1",
                      "fullMatch": "boolean: true / false"
                    },
                    {
                      "value": "Term2",
                      "fullMatch": "boolean: true / false"
                    },
                 ],
                 "activeTimeRange": [
                   {
                     "startTime": timestamp1,
                     "endTime": timestamp2
                   },
                   {
                     "startTime": timestamp3,
                     "endTime": timestamp4
                   }
                 ]
                },
                "pinAction": {
                   "pinMap" :  {
                            "pin_position1": "product_id",
                          "pin_position2": "product_id>"
                        }
                }
                  }
    }' \
    "https://retail.googleapis.com/v2alpha/projects/PROJECT_NUMBER/locations/LOCATION/catalogs/default_catalog/controls?controlId=CONTROL_ID"

The `pin_position` should be an integer between [1,10] inclusive and `product_id` must exist in your catalog. The maximum number of allowed elements in the pin map is 10 for each control.

Next, attach the pinning control to your serving config:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
    -H "Content-Type: application/json; charset=utf-8" \
    -H "X-Goog-User-Project: PROJECT_NUMBER" \
    -d '{
          "controlId": "CONTROL_ID"
      }' \
    'https://retail.googleapis.com/v2alpha/projects/PROJECT_NUMBER/locations/LOCATION/catalogs/default_catalog/servingConfigs/SERVING_CONFIG_ID:addControl'

In this case, `CONTROL_ID` should be the pinning control `id` you created previously.

To add a control to a serving config, use the `ServingConfig.addControl` method:

  * For more about this method, see the [`ServingConfig.addControl` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/addControl).

  * For an example of this method, see [Manage serving configs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-configs). 




Finally, to test your setup, make a search request. To make sure that a request will have the pinning control applied successfully, use query terms (in search) or page categories (in browse) that match the terms/categories provided in the control you created in the preceding steps.

###  Cloud console 

  1. Go to the **Evaluate** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Evaluate page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/evaluate/)

  2. Go to the **Search** tab.

  3. Enter a test query in the search query field.

  4. Click **Search preview**.

  5. View the results to ensure that your chosen products are pinned.




###  curl 
    
    
    curl -s -X POST -H "Authorization: Bearer " -H "Content-Type: application/json"
    --data "{'query': '','visitorId': ''}" \ "https://retail.googleapis.com/v2/projects/PROJECT/locations/global/catalogs/CATALOG/placements/default_search:search"

#### Constraints for error checking

For error checking, keep these constraints in mind:

  * Two products cannot be pinned to the same position, that is, products "a" and "b" cannot both occupy position #2.
  * Conversely, one product cannot be pinned to more than one location, that is, product "a" cannot be pinned to positions #2 and #3 at the same time for the same query.
  * The `product_id` must exist as a product in the catalog, assuming that no filters or sorting are applied.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
