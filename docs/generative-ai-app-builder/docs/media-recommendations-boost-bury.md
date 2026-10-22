---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/media-recommendations-boost-bury/
title: Boost and bury media recommendations \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:23.548123+00:00
---

# Boost and bury media recommendations  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/media-recommendations-boost-bury/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Boost and bury media recommendations Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This feature is a Preview offering, subject to the "Pre-GA Offerings Terms" of the [GCP Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA products and features may have limited support, and changes to pre-GA products and features may not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). Further, by using this feature, you agree to the [Generative AI Preview terms and conditions](https://cloud.google.com/trustedtester/aitos) ("Preview Terms"). For this feature, you can process personal data as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to applicable restrictions and obligations in the Agreement (as defined in the Preview Terms). 

This page explains how to change the ranking position of media recommendations returned by the model by using boost serving controls (also called controls).

A boost control changes the order of the recommendations after those recommendations have been returned by the model. You apply a filter expression to the results to identify which recommendations you want to boost or bury, and then you apply a boost value between -1 and +1. A boost value of +1 gives the biggest _boost_ to a recommendation, placing it at the top of recommendations returned. A value of -1 _buries_ the recommendation towards the bottom of the list of recommendations returned.

Boost is a _serving-time_ control. First, the recommendations model returns a list of recommendations. Using a serving config, the boost control is then applied to that list to adjust the ranking of the recommendations. The boost control doesn't add or delete recommendations, but it does control the order in which the recommendations are presented to the user.

## Boost versus filtering recommendations

Boost is a _soft_ filter. Whereas, the regular filter for recommendations, described in [Filter recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-recommendations) is a _hard_ filter.

If you apply a hard filter to recommendations, you'll never see the documents that are filtered out. However, with a soft filter, you don't remove documents from the list of recommendations. Instead, the filter is used to determine which documents should be higher or lower in the list of recommendations returned.

## Avoid swamping your recommendations model

When applying a boost or bury filter, small values close to zero are recommended. Values close to +1 or -1 are likely to overwhelm the recommendations model, so that the recommendations ranking applied by the model is not reflected in the order that the user sees the recommendations.

For example, if you boost animated movies with +1, users would only see animated movies at the top of the recommendations list; these would push non-animated movies that were highly recommended by the model to the bottom of the list where the user might not see them.

## Demoting versus burying

Demoting and burying both move recommendations to lower positions in the list of returned recommendations that they'd appear otherwise.

However, _demotion_ is based on the age of the content or on whether the user has already watched some of the content. For more information about demotion, see [Demote media recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/demote-recommendations).

_Burying_ applies to content identified by a filter. The filter can be any data field marked as filterable in the schema. For general information about recommendation filters including how to mark a field as filterable, see [Filter recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-recommendations).

## About boost controls and serving configs

Each boost _serving control_ is made up of a filter and a boost value. For example, one boost control boosts movies with Christmas in the title with a value of `0.1` and another buries horror movies with a value of`-0.2`.

After creating one or more boost controls, you attach the controls to a _serving config_. When any Agent Search app is created, a default serving config is also automatically created. The serving config is referenced at serving time to determine what results the app generates. In addition to boost controls, the serving config can contain other types of controls, such as [diversify](https://docs.cloud.google.com/generative-ai-app-builder/docs/diversify-recommendations) and [demote](https://docs.cloud.google.com/generative-ai-app-builder/docs/demote-recommendations) controls.

The serving config can be applied when you call the recommend method. All the controls in the serving config are then applied to recommendations returned by the method call.

Furthermore, you can have multiple serving configs associated with your app. This lets you apply different sets of controls in different circumstances. For example, if the recommendation request comes from a child's account, boost movies in categories suitable for children and bury unsuitable movies. Similarly, if the request comes from an account marked adult, boost titles or categories popular with adults. Alternatively, you might choose to have different serving configs for different geographic locations and boost content according to what is regionally popular. For more information about serving configs, see [Create and manage media serving configs](https://docs.cloud.google.com/generative-ai-app-builder/docs/serving-configs).

## Boost values are additive

If you have attached multiple serving controls to a serving config, boosts and buries become additive.

For example, if you boost animated children's movies by 0.3 and animated adventure movies by 0.4, then a movie that is categorized as a children's animated adventure is boosted by 0.7.

Similarly, if a horror movie was boosted by 0.2 by one control and buried by -0.3 by another control in the same serving config, the net result would be to bury the movie by -0.1.

The sum of the boosts can exceed +1. For example, if the controls boosted animated children's movies by 0.6 and animated adventure movies by 0.5, then a children's animated adventure movie would be boosted by +1.1.

## Examples of filters

The following are some examples of filters for media recommendations.

### Filters on common key properties

Examples of filters on common key string properties (`category`, `image_name`, `image_uri`, `language`, `title`, and `uri`).

  * Animations for kids:  
`"filter": "categories: ANY(\"animation\") AND categories: ANY(\"children\")"`

  * Scary media:  
`"filter": "categories: ANY(\"horror\", \"thriller\", \"crime\")`

  * Media where the title is "Christmas":  
`"filter": "title: ANY(\"Christmas\")"`

  * Media where the first item in the `images` array has the `name` "beach ball":  
`"filter": "images[0].name: ANY(\"beach ball\")"`




### Filters on media key properties

Examples of filters on media key properties. Media key properties begin with `media_`, and, in the filter syntax, the field name is prefaced with `media_key_properties.`. For a list of media key properties, see [Google predefined schema versus custom schema](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-documents#predefined-vs-custom).

  * Media where the type is `audio`:  
`"filter": "media_key_properties.media_type: ANY(\"audio\")"`

  * Media where the hash_tags array contains a string `#winter`:  
`"filter": "media_key_properties.hash_tags: ANY(\"#winter\")"`

  * Media where the first element of the hash_tags array is the string `#winter`:  
`"filter": "media_key_properties.hash_tags[0]: ANY(\"#winter\")"`




### Custom fields

Examples of filters on custom fields. For custom attributes, preface the field name with `attributes.`.

  * You have a custom string field, `festival`, in your schema to represent what film festival a movie premiered at. To filter on only those movies that premiered at Cannes:  
`"filter": "attributes.festival: ANY(\"Cannes\")`

  * You have a custom boolean field, `audio_desc`, that is true when the media includes an audio description for visually impaired viewers. To filter on media with an audio descripton:  
`"filter": "attributes.audio_desc: ANY(true)"`




## Limitations on filterable fields

The following limitations apply to boost serving controls:

  * Only property fields of types string and boolean can be used in filter expressions for boost.

  * You can't filter on fields nested more than one level. For example, you can filter on `persons.name` but you couldn't filter on a field `persons.name.stage` (even if such a field existed).

  * Filters must be exact matches. This means that in examples, a movie called "`Christmas Story`" or "`CHRISTMAS`" wouldn't be boosted.




## Before you begin

  * Make sure that you have created a media recommendations app and data store. For more information, see [Create a media recommendations app and data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-app-media).

  * Optional: If you don't want to use the default serving config, create a new serving config by following steps 1-5 and 7 in [Create a serving config](https://docs.cloud.google.com/generative-ai-app-builder/docs/serving-configs#create-serving-config). If your app is in production, Google recommends that you create a separate serving config for testing boost controls before applying the controls to your production serving config.

  * Make sure that any fields that you want to use in your boost control are marked as **Filterable** in the schema. For more information, see [Configure field settings](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-field-settings). See also [Filtering limits](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-recommendations#filter-limits).




## Boost or bury recommendations

This procedure describes how to create boost controls and attach the controls to a serving config.

After the controls have been attached to the serving config, you can specify the serving config when calling the [`servingConfigs.recommend`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.dataStores.servingConfigs/recommend) method and the boost control will be used to influence the order of the recommendations returned.

### REST

To create boost serving controls and attach them to a serving config, follow these steps:

  1. Find your app ID. If you already have your app ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page.

[Go to Apps](https://console.cloud.google.com/gen-app-builder/engines)

     2. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column.

  2. Find your data store ID. If you already have your data store ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page and in the navigation menu, click **Data Stores**.

[Go to the Data Stores page](https://console.cloud.google.com/gen-app-builder/data-stores)

     2. Click the name of your data store.

     3. On the **Data** page for your data store, get the data store ID.

  3. Create a boost control:
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -H "X-Goog-User-Project: PROJECT_NUMBER" \
         "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_NUMBER/locations/global/collections/default_collection/engines/APP_ID/controls?controlId=CONTROL_ID" \
         -d '{
               "displayName": "CONTROL_DISPLAY_NAME",
                   "solutionType": "SOLUTION_TYPE_RECOMMENDATION",
                   "boostAction": {
                        "dataStore": "projects/PROJECT_NUMBER/locations/global/collections/default_collection/dataStores/DATA_STORE_ID",
                        "boost" :  BOOST_VALUE,
                        "filter": "FILTER"
                   }
             }'
         

Replace the following:

     * `PROJECT_NUMBER`: the number of your Google Cloud project.

     * `CONTROL_DISPLAY_NAME`: a human-readable name to identify the control. Must be a UTF-8 string with a maximum length of 128 characters.

     * `CONTROL_ID`: a unique identifier (within a data store) for the control. The ID can contain lowercase letters, digits, hyphens, and underscores.

     * `APP_ID`: the ID of the Agent Search app.

     * `DATA_STORE_ID`: the ID of the Agent Search data store.

     * `BOOST_VALUE`: a floating point number in the range [-1,1]. When the value is negative, recommendations appear lower down in the results. When the value is positive, recommendations are promoted (they appear higher up in the results). 

     * `FILTER`: the filter expression that describes what documents will be boosted or buried. For detailed information about how to formulate the filter expression, see [Filter expressions](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-recommendations#filter-expressions). 

#### Example command and response
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json; charset=utf-8" \
    -H "X-Goog-User-Project: 123456" \
    "https://discoveryengine.googleapis.com/v1beta/projects/123456/locations/global/collections/default_collection/engines/my-app/controls?controlId=boost-kids" \
    -d '{
          "displayName": "Boost childrens category",
              "solutionType": "SOLUTION_TYPE_RECOMMENDATION",
              "boostAction": {
                   "dataStore": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store",
                   "boost" :  0.3,
                   "filter": "categories: ANY(\"Children\")"
              }
        }'
    
    
    {
      "name": "projects/123456/locations/global/collections/default_collection/engines/my-app/controls/boost-kids",
      "displayName": "Boost childrens category",
      "solutionType": "SOLUTION_TYPE_RECOMMENDATION",
      "boostAction": {
        "boost": 0.3,
        "filter": "categories: ANY(\"Children\")",
        "dataStore": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store"
      }
    }
    

This command boost documents that are categorized for children. 

  4. Repeat step 3 for each boost control that you want to apply to your recommendations. For example, you might want one boost control that boosts movies for children, `boost-kids` and a second control that buries horror films, `bury-horror`.

  5. Find the ID of the serving config. If you already have your serving config ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page.

[Go to Apps](https://console.cloud.google.com/gen-app-builder/engines)

     2. On the **Apps** page, click the name of your app.

     3. Go to the **Configurations** page and click the **Control** tab.

     4. Get the serving config ID from the **ID** column.

  6. Attach the new boost serving control to the serving config with an update request using the [`engines.servingConfigs.patch`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.engines.servingConfigs/patch) method.

**Important:** If there are already any boost controls attached to this serving config, those controls are deleted by this patch command. The patch command replaces the value of `boostControlIds` with the new value that you provide.
         
         curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/CONFIG_ID?update_mask=boost_control_ids" \
         -d '{
           "boostControlIds": ["CONTROL_ID"]
         }'
         

Replace the following:

     * `CONFIG_ID`: the ID of the serving config that you want to attach the boost controls to—for example, `my_app-1234567_id`. See the previous step.

     * `CONTROL_ID`: contains the IDs one or more of the boost serving control that you want to attach to the serving config—for example, `"boost-kids", "bury-horror"`. This is an array of strings, if you have more than one ID, don't forget to use separating quotes and commas.

#### Example command and response
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -H "X-Goog-User-Project: my-project-123" \
    "https://discoveryengine.googleapis.com/v1beta/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/servingConfigs/my_app-1234567_id?update_mask=boost_control_ids" \
    -d '{
      "boostControlIds": ["boost-kids", "bury-horror"]
    }'
    
    
    {
      "name": "projects/123456/locations/global/collections/default_collection/engines/my-app/servingConfigs/my_app-1234567_id",
      "displayName": "jane-day-test-serving-config-for-boost-bury",
      "solutionType": "SOLUTION_TYPE_RECOMMENDATION",
      "modelId": "my-app",
      "diversityLevel": "no-diversity",
      "diversityType": "RULE_BASED_DIVERSITY",
      "mediaConfig": {},
      "boostControlIds": [
        "boost-kids",
        "bury-horror"
      ]
    }
    

This command attaches two boost controls to the default serving config of the `my-app` app. 

  7. Wait a few minutes for the results to take effect.

  8. Preview the effects of your boost control. See [Get media recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-recommendations#get-media-recommendations). 




## Update the boost control

This procedure describes how to update an existing boost control to change the value of the boost or the filter.

After you have tested the boost control, you might discover that you want to make the boost stronger or weaker. Alternatively, you might want to change the filter string.

When updating a boost value or filter, you call the [`engines.controls.patch`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.engines.controls/patch) method.

The patch method replaces the values of `boost` and `filter` with the new values that you provide. This procedure shows how to edit the `boost` value (step 3) and the `filter` value (step 4) separately. However, you want to edit both, you can do that in a single curl command.

### REST

To modify the boost value for filter for an existing control, follow these steps:

  1. Find your app ID. If you already have your app ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page.

[Go to Apps](https://console.cloud.google.com/gen-app-builder/engines)

     2. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column.

  2. Find the ID of the boost control that you want to update using the [`engines.servingConfigs.get`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.servingConfigs/get) method. If you already have the ID, skip to the next step.
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/controls"
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.

     * `APP_ID`: the ID of the Agent Search app.

#### Example command and result
    
    curl -X GET \
     -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
     -H "Content-Type: application/json" \
     -H "X-Goog-User-Project: my-project-123" \
     "https://discoveryengine.googleapis.com/v1beta/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/controls"
    
    
    {
      "controls": [
        {
          "name": "projects/123456/locations/global/collections/default_collection/engines/my-app/controls/boost-kids",
          "displayName": "Boost childrens category",
          "associatedServingConfigIds": [
            "my_app-1234567_id"
          ],
          "solutionType": "SOLUTION_TYPE_RECOMMENDATION",
          "boostAction": {
            "boost": 0.3,
            "filter": "categories: ANY(\"Children\")",
            "dataStore": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store"
          }
        },
        {
          "name": "projects/123456/locations/global/collections/default_collection/engines/my-app/controls/bury-horror",
          "displayName": "Bury horror category",
          "associatedServingConfigIds": [
            "my_app-1234567_id"
          ],
          "solutionType": "SOLUTION_TYPE_RECOMMENDATION",
          "boostAction": {
            "boost": -0.4,
            "filter": "categories: ANY(\"Horror\")",
            "dataStore": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store"
          }
        }
      ]
    }

This command lists the all the controls associated with an app. Make note of the name of the boost control that you want to update. 

  3. Edit the boost value for the control:
         
         curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/controls/CONTROL_ID?update_mask=boost_action.boost" \
         -d '{
             "name": "projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/controls/CONTROL_ID",
             "boostAction": {
               "boost": BOOST_VALUE
             }
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.

     * `APP_ID`: the ID of the Agent Search app.

     * `CONTROL_ID`: the unique identifier for the boost control that you want to edit, the final part of the `name` field output by the `GET` command in the step 2. For example, `boost-kids`.

     * `BOOST_VALUE`: a floating point number in the range [-1,1]. When the value is negative, recommendations appear lower down in the results. When the value is positive, recommendations are promoted (they appear higher up in the results). 

#### Example command and result
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -H "X-Goog-User-Project: my-project-123" \
    "https://discoveryengine.googleapis.com/v1beta/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/controls/boost-kids?update_mask=boost_action.boost" \
    -d '{
        "name": "projects/my-project-123/locations/global/collections/default_collection/engines/my-app/controls/boost-kids",
        "boostAction": {
          "boost": 0.2
        }
    }'
    
    
    {
      "name": "projects/123456/locations/global/collections/default_collection/engines/my-app/controls/boost-kids",
      "displayName": "Boost childrens category",
      "solutionType": "SOLUTION_TYPE_RECOMMENDATION",
      "boostAction": {
        "boost": 0.2,
        "filter": "categories: ANY(\"Children\")",
        "dataStore": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store"
      }
    }
    

This command boost sets the boost value of the boost-kids control to `0.2`. 

  4. Edit the filter for the boost control:
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/controls/CONTROL_ID?update_mask=boost_action.filter" \
         -d '{
             "name": "projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/controls/CONTROL_ID",
             "boostAction": {
               "filter": "FILTER"
             }
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.

     * `APP_ID`: the ID of the Agent Search app.

     * `CONTROL_ID`: the unique identifier for the boost control that you want to edit, the final part of the `name` field output by the `GET` command in the step 2.

     * `FILTER`: the filter expression that describes what documents will be boosted or buried. For detailed information about how to formulate the filter expression, see [Filter expressions](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-recommendations#filter-expressions). 

#### Example command and result
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -H "X-Goog-User-Project: my-project-123" \
    "https://discoveryengine.googleapis.com/v1beta/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/controls/boost-kids?update_mask=boost_action.filter" \
    -d '{
    "name": "projects/my-project-123/locations/global/collections/default_collection/engines/my-app/controls/boost-kids",
    "boostAction": {
      "filter": "categories: ANY(\"animation\") AND categories: ANY(\"children\")"
    }
    }'
    
    
    {
      "name": "projects/123456/locations/global/collections/default_collection/engines/my-app/controls/boost-kids",
      "displayName": "Boost childrens category",
      "solutionType": "SOLUTION_TYPE_RECOMMENDATION",
      "boostAction": {
        "boost": 0.2,
        "filter": "categories: ANY(\"animation\") AND categories: ANY(\"children\")",
        "dataStore": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store"
      }
    }
    

This command adds the filter for the category `animation` so that animated media for children is boosted. The filter replaces the existing filter. 




## Delete a boost control

This procedure describes how to delete a boost control. If you're not using a boost control, best practice is to delete it so that you don't reach or exceed the [quota](https://docs.cloud.google.com/generative-ai-app-builder/quotas#allocation-quotas) for the number of controls allowed.

When deleting a boost control, you call the [`engines.controls.delete`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.engines.controls/delete) method.

Boost controls that are attached to a serving config can't be deleted. If you try to delete a boost control, an error message gives you the name of the serving config. You then need to [delete](https://docs.cloud.google.com/generative-ai-app-builder/docs/serving-configs#delete-serving-config) that serving config or detach that control from the serving config.

### REST

To delete a boost control, follow these steps:

  1. Find your app ID. If you already have your app ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page.

[Go to Apps](https://console.cloud.google.com/gen-app-builder/engines)

     2. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column.

  2. Find the ID of the boost control that you want to delete using the [`engines.servingConfigs.get`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.servingConfigs/get) method. If you already have the ID, skip to the next step.
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/controls"
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.

     * `APP_ID`: the ID of the Agent Search app.

#### Example command and result
    
    curl -X GET \
     -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
     -H "Content-Type: application/json" \
     -H "X-Goog-User-Project: my-project-123" \
     "https://discoveryengine.googleapis.com/v1beta/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/controls"
    
    
    {
      "controls": [
        {
          "name": "projects/123456/locations/global/collections/default_collection/engines/my-app/controls/boost-kids",
          "displayName": "Boost childrens category",
          "associatedServingConfigIds": [
            "my_app-1234567_id"
          ],
          "solutionType": "SOLUTION_TYPE_RECOMMENDATION",
          "boostAction": {
            "boost": 0.2,
            "filter": "categories: ANY(\"animation\") AND categories: ANY(\"children\")",
            "dataStore": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store"
          }
        },
        {
          "name": "projects/123456/locations/global/collections/default_collection/engines/my-app/controls/bury-horror",
          "displayName": "Bury horror category",
          "associatedServingConfigIds": [
            "my_app-1234567_id"
          ],
          "solutionType": "SOLUTION_TYPE_RECOMMENDATION",
          "boostAction": {
            "boost": -0.4,
            "filter": "categories: ANY(\"Horror\")",
            "dataStore": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store"
          }
        }
      ]
    }

This command lists the all the controls associated with an app. 

  3. Review the output. If the boost control attached to a serving config, then update the serving config to remove the control that you want to delete. See Update a serving config to remove a boost control.

  4. Run the following curl command to delete a boost control:
         
         curl -X DELETE \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/controls/CONTROL_ID"
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.

     * `APP_ID`: the ID of the Agent Search app.

     * `CONTROL_ID`: the unique identifier for the boost control that you want to delete, the final part of the `name` field output by the `GET` command in the step 2.

#### Example command
    
    curl -X DELETE \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -H "X-Goog-User-Project: my-project-123" \
    "https://discoveryengine.googleapis.com/v1beta/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/controls/boost-kids"
    
    
    {}
    

This command deletes the `boost-kids` control. 

If you get an error message, that says the control is actively referenced by at least one serving config, see Update a serving config to remove a boost control. 




## Update a serving config to remove a boost control

Before you can delete a boost control, you have to detach it from all serving controls. Do this by patching the serving controls to remove the ID of the boost control.

To detach boost controls from a serving config, follow these steps:

  1. Find out which boost controls are attached to the serving config by making a [`engines.servingConfigs.get`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.engines.servingConfigs/get) request and looking at the `boostControlIds` field in the response.
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/CONFIG_ID"
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.

     * `APP_ID`: the ID of the Agent Search app.

     * `CONFIG_ID`: the ID of the serving config that you want to know more about.

#### Example command and result
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -H "X-Goog-User-Project: my-project-123" \
    "https://discoveryengine.googleapis.com/v1beta/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/servingConfigs/my_app-1234567_id"
    
    
    {
      "name": "projects/123456/locations/global/collections/default_collection/engines/my-app/servingConfigs/my_app-1234567_id",
      "displayName": "jane-day-test-serving-config-for-boost-bury",
      "solutionType": "SOLUTION_TYPE_RECOMMENDATION",
      "modelId": "my-app",
      "diversityLevel": "no-diversity",
      "diversityType": "RULE_BASED_DIVERSITY",
      "mediaConfig": {},
      "createTime": "2024-11-22T23:54:45.613178Z",
      "updateTime": "2024-11-26T20:28:11.967439Z",
      "boostControlIds": [
        "boost-kids",
        "bury-horror"
      ]
    }
    

This command lists information about the serving config `my_app-1234567_id`, in particular, it shows that the serving config has two boost controls attached to it: `boost-kids` and `bury-horror`. 

  2. To update the serving config to remove one boost control, use the [`engines.servingConfigs.patch`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.engines.servingConfigs/patch) method.
         
         curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/CONFIG_ID?update_mask=boost_control_ids" \
         -d '{
           "boostControlIds": ["CONTROL_ID"]
         }'
         

Replace the following:

     * `CONFIG_ID`: the ID of the serving config that you want to attach the boost controls to—for example, `my_app-1234567_id`. See the previous step.

     * `CONTROL_ID`: contains the IDs one or more of the boost control that you want the serving config to have. Make sure to omit any boost controls that you want to delete. This is an array of strings. If you have more than one ID, don't forget to use separating quotes and commas—for example, `boost-1", "boost-2`.

#### Example command and result: leaves one control
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -H "X-Goog-User-Project: my-project-123" \
    "https://discoveryengine.googleapis.com/v1beta/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/servingConfigs/my_app-1234567_id?update_mask=boost_control_ids" \
    -d '{
      "boostControlIds": ["bury-horror"]
    }'
    
    
    {
      "name": "projects/123456/locations/global/collections/default_collection/engines/my-app/servingConfigs/my_app-1234567_id",
      "displayName": "jane-day-test-serving-config-for-boost-bury",
      "solutionType": "SOLUTION_TYPE_RECOMMENDATION",
      "modelId": "my-app",
      "diversityLevel": "no-diversity",
      "diversityType": "RULE_BASED_DIVERSITY",
      "mediaConfig": {},
      "boostControlIds": [
        "bury-horror"
      ]
    }
    

This command keeps the `bury-horror` boost control attached to the serving config and removes the `boost-kids` control. Assuming that `boost-kids` isn't attached to any other serving config, it can now be deleted. See Delete a boost control. 

#### Example command and result: removes all controls
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -H "X-Goog-User-Project: my-project-123" \
    "https://discoveryengine.googleapis.com/v1beta/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/servingConfigs/my_app-1234567_id?update_mask=boost_control_ids" \
    -d '{
    "boostControlIds": []
    }'
    
    
    {
    "name": "projects/123456/locations/global/collections/default_collection/engines/my-app/servingConfigs/my_app-1234567_id",
    "displayName": "jane-day-test-serving-config-for-boost-bury",
    "solutionType": "SOLUTION_TYPE_RECOMMENDATION",
    "modelId": "my-app",
    "diversityLevel": "no-diversity",
    "diversityType": "RULE_BASED_DIVERSITY",
    "mediaConfig": {}
    }
    

This command removes all boost controls from the serving config, `my_app-1234567_id`




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
