---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/check-media-data-quality/
title: Check data quality for media recommendations \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:28:10.676272+00:00
---

# Check data quality for media recommendations  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/check-media-data-quality/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Check data quality for media recommendations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to find out whether various metrics for your media data meet their requirement thresholds.

## About checking media data quality

Because recent user events are so important for media recommendations, you must regularly check the quality of your ingested data and user events. You can do this by reviewing the **Optimization** tab for your media recommendations app to determine what improvements you can make to your data in order to optimize for better quality recommendations.

If a metric's threshold isn't met, then the metric has a warning status. Then, you need to review the metric and its description to determine what action you should take to improve your media quality.

All models and objectives need to pass the _General quality_ metric thresholds. Some model and objectives have additional _App-specific quality_ metrics and thresholds. The general quality metrics are the same for all apps using the same data store, but app-specific quality metrics vary according to the app's model and objectives.

For information about the recommendation models and objectives, see [About media app recommendations types](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-media-recommendations-types).

## Check data quality

### Console

To check the quality of your media recommendations data, follow these steps:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/start)

  2. Click the name of the media recommendations app that you want check data quality for.

  3. In the navigation menu, click **Data quality** and click the **Optimization** tab. This page shows the status of various metrics for the data associated with your app.

  4. Review the **General quality** and the **App-specific quality** statuses at the top of the page. The summary status at the top of the page shows as a warning if one or more metrics has exceeded its threshold.

The two metrics tables (**General quality** and the **App-specific quality**) list the individual metrics.

![optimization tab shows one warning metric for the general quality
doc_with_same_title_percentage](https://docs.cloud.google.com/generative-ai-app-builder/images/optimization_tab_media_recommendations_app.png)

  5. In the metrics tables, click **View details** for more information about any metrics in the warning state.

  6. Optional: If you want to see the threshold for a compliant metric, click **View Details**. Thresholds for compliant metrics are not shown in the metrics table. 




### REST

**Note:** This feature is a Preview offering, subject to the "Pre-GA Offerings Terms" of the [GCP Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA products and features may have limited support, and changes to pre-GA products and features may not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). Further, by using this feature, you agree to the [Generative AI Preview terms and conditions](https://cloud.google.com/trustedtester/aitos) ("Preview Terms"). For this feature, you can process personal data as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to applicable restrictions and obligations in the Agreement (as defined in the Preview Terms). 

Use the [`requirements:checkRequirement`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.requirements/checkRequirement) method to check the quality of your media recommendations data, as shown.

To check the quality from the command line, follow these steps:

  1. Find your data store ID. If you already have your data store ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page and in the navigation menu, click **Data Stores**.

[Go to the Data Stores page](https://console.cloud.google.com/gen-app-builder/data-stores)

     2. Click the name of your data store.

     3. On the **Data** page for your data store, get the data store ID.

  2. Run the following curl command to learn if your media recommendations meets the thresholds for the general metrics:
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-GFE-SSL: yes" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global/requirements:checkRequirement" \
         -d '{
               "location": "projects/PROJECT_ID/locations/global",
               "requirementType": "discoveryengine.googleapis.com/media_recs/general/all/warning",
               "resources": [
                 {
                   "labels": {
                     "branch_id": "0",
                     "collection_id": "default_collection",
                     "datastore_id": "DATA_STORE_ID",
                     "location_id": "global",
                     "project_number": "PROJECT_ID"
                   },
                   "type": "discoveryengine.googleapis.com/Branch"
                 },
                 {
                   "labels": {
                     "collection_id": "default_collection",
                     "datastore_id": "DATA_STORE_ID",
                     "location_id": "global",
                     "project_number": "PROJECT_ID"
                   },
                   "type": "discoveryengine.googleapis.com/DataStore"
                 }
               ]
             }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `DATA_STORE_ID`: the ID of the Agent Search data store.

#### Example command and result
    
    curl -X POST
    -H "Authorization: Bearer $(gcloud auth print-access-token)"
    -H "Content-Type: application/json"
    -H "X-GFE-SSL: yes"
    -H "X-Goog-User-Project: my-project-123"
    "https://discoveryengine.googleapis.com/v1alpha/projects/my-project-123/locations/global/requirements:checkRequirement"
    -d '{
      "location": "projects/123456/locations/global",
      "requirementType": "discoveryengine.googleapis.com/media_recs/general/all/warning",
      "resources": [
        {
          "labels": {
            "branch_id": "0",
            "collection_id": "default_collection",
            "datastore_id": "my-data-store",
            "location_id": "global",
            "project_number": "123456"
          },
          "type": "discoveryengine.googleapis.com/Branch"
        },
        {
          "labels": {
            "collection_id": "default_collection",
            "datastore_id": "my-data-store",
            "location_id": "global",
            "project_number": "123456"
          },
          "type": "discoveryengine.googleapis.com/DataStore"
        }
      ]
    }'
        
    
    * * *
    
    
    {
    "requirement": {
    "type": "discoveryengine.googleapis.com/media_recs/general/all/warning",
    "displayName": "Warning level requirements for all models and all business objectives.",
    "description": "Requirements for the media recommendations model that will result in performance issue if not met for all media recommendations models and all business objectives.",
    "condition": {
      "expression": "doc_with_same_title_percentage \u003c doc_with_same_title_percentage_threshold && most_common_visitor_id_percentage \u003c most_common_visitor_id_percentage_threshold && short_term_unjoined_events_percentage \u003c short_term_unjoined_events_percentage_threshold && long_term_unjoined_events_percentage \u003c long_term_unjoined_events_percentage_threshold"
    },
    "metricBindings": [
      {
        "variableId": "doc_with_same_title_percentage",
        "resourceType": "discoveryengine.googleapis.com/Branch",
        "metricFilter": "metric.type = 'discoveryengine.googleapis.com/branch/documents/items_with_same_title' AND metric.labels.is_percentage = 'True' AND resource.labels.project_number = '123456' AND resource.labels.branch_id = '0' AND resource.labels.datastore_id = 'my-data-store' AND resource.labels.location_id = 'global' AND resource.labels.collection_id = 'default_collection'",
        "description": "The percentage of the documents with the same title in a branch.",
        "category": "Document"
      },
      {
        "variableId": "most_common_visitor_id_percentage",
        "resourceType": "discoveryengine.googleapis.com/DataStore",
        "metricFilter": "metric.type = 'discoveryengine.googleapis.com/branch/datastore/user_events/most_used_visitor_id_events' AND metric.labels.is_percentage = 'True' AND resource.labels.datastore_id = 'my-data-store' AND resource.labels.project_number = '123456' AND resource.labels.location_id = 'global' AND resource.labels.collection_id = 'default_collection'",
        "description": "The percentage of the events with the same visitor id.",
        "category": "DataStore"
      },
      {
        "variableId": "short_term_unjoined_events_percentage",
        "resourceType": "discoveryengine.googleapis.com/DataStore",
        "metricFilter": "metric.type = 'discoveryengine.googleapis.com/datastore/user_events/unjoined_events_for_document_ids' AND metric.labels.is_percentage = 'True' AND metric.conditions.time_range = 'WEEK' AND resource.labels.datastore_id = 'my-data-store' AND resource.labels.project_number = '123456' AND resource.labels.location_id = 'global' AND resource.labels.collection_id = 'default_collection'",
        "description": "The percentage of events refers to a document id that is not in the catalog in the last 7 days.",
        "category": "DataStore"
      },
      {
        "variableId": "long_term_unjoined_events_percentage",
        "resourceType": "discoveryengine.googleapis.com/DataStore",
        "metricFilter": "metric.type = 'discoveryengine.googleapis.com/datastore/user_events/unjoined_events_for_document_ids' AND metric.labels.is_percentage = 'True' AND metric.conditions.time_range = 'NINETY_DAYS' AND resource.labels.datastore_id = 'my-data-store' AND resource.labels.project_number = '123456' AND resource.labels.location_id = 'global' AND resource.labels.collection_id = 'default_collection'",
        "description": "The percentage of events refers to a document id that is not in the catalog in the last 90 days.",
        "category": "DataStore"
      }
    ],
    "thresholdBindings": [
      {
        "variableId": "doc_with_same_title_percentage_threshold",
        "threshold_values": {
          "severity": "WARNING",
          "value": 1.0
        }
        "description": "The threshold for the percentage of the documents with the same title in a branch."
      },
      {
        "variableId": "most_common_visitor_id_percentage_threshold",
        "threshold_values": {
          "severity": "WARNING",
          "value": 5.0
        }
        "description": "The threshold for the percentage of the events with the same visitor id."
      },
      {
        "variableId": "short_term_unjoined_events_percentage_threshold",
        "threshold_values": {
          "severity": "WARNING",
          "value": 5.0
        }
        "description": "The threshold for the percentage of the events refers to a document id that is not in the catalog in the last 7 days."
      },
      {
        "variableId": "long_term_unjoined_events_percentage_threshold",
        "threshold_values": {
          "severity": "WARNING",
          "value": 2.0
        }
        "description": "The threshold for the percentage of the events refers to a document id that is not in the catalog in the last 90 days"
      }
    ]
    },
    "result": "WARNING",
    "requirementCondition": {
    "expression": "doc_with_same_title_percentage \u003c doc_with_same_title_percentage_threshold && most_common_visitor_id_percentage \u003c most_common_visitor_id_percentage_threshold && short_term_unjoined_events_percentage \u003c short_term_unjoined_events_percentage_threshold && long_term_unjoined_events_percentage \u003c long_term_unjoined_events_percentage_threshold"
    },
    "metricResults": [
    {
      "name": "short_term_unjoined_events_percentage",
      "value": {
        "doubleValue": 0
      },
      "timestamp": "2024-06-06T03:03:13.416900898Z",
      "unit": "%",
      "metricType": "discoveryengine.googleapis.com/datastore/user_events/unjoined_events_for_document_ids"
    },
    {
      "name": "long_term_unjoined_events_percentage",
      "value": {
        "doubleValue": 0
      },
      "timestamp": "2024-06-06T03:03:13.417962744Z",
      "unit": "%",
      "metricType": "discoveryengine.googleapis.com/datastore/user_events/unjoined_events_for_document_ids"
    },
    {
      "name": "most_common_visitor_id_percentage",
      "value": {
        "doubleValue": 0.8
      },
      "timestamp": "2024-06-06T03:03:16.090037135Z",
      "unit": "%",
      "metricType": "discoveryengine.googleapis.com/datastore/user_events/most_used_visitor_id_events"
    },
    {
      "name": "doc_with_same_title_percentage",
      "value": {
        "doubleValue": 30.47
      },
      "timestamp": "2024-06-06T03:03:17.599458357Z",
      "unit": "%",
      "metricType": "discoveryengine.googleapis.com/documents/items_with_same_title"
    }
    ],
    "oldestMetricTimestamp": "2024-06-06T03:03:13.416900898Z"
    }
    

  3. Review the output:

     1. Look for the value of `result`:

        * If the value is `SUCCESS`, then your data passes the general requirements; continue to step 4.

        * If the value is `WARNING`, continue to step b.

        * If you don't see `result` in the output, there are a couple possible reasons:

          * The `PROJECT_ID` or `DATA_STORE_ID` in the request is incorrect.

          * Some metric values are unavailable. Try again in 6 hours or reach out to a customer engineer for help.

     2. Look for the expression (`requirement.Condition.Expression`): If this expression evaluates to false, then there is a problem with your data.

**Note:** The less-than sign in the expression appears in unicode, `\u003c`, instead of as "<".

The value of the metrics are in the `requirementCondition.metricResults.value` field. The warning threshold values are in the `thresholdBindings.thresholdValues` fields. The `description` fields can help you understand the purpose of the metric.

For example, the value of `doc_with_same_title_percentage` is `30.47` and the warning threshold for `doc_with_same_title_percentage_threshold` is `1`. There is a data problem that so many of the titles in the data store are the same, and this needs to be investigated.

  4. If the model and objective combination used for your recommendations app appears in this table, then you also need to call the check requirement method, updated with the values for your model and objective:

Model | Objective | `MODEL_OBJ`  
---|---|---  
Others You May Like | Conversion rate | `oyml/cvr`  
Recommended for You | Conversion rate | `rfy/cvr`  
More Like This | Conversion rate | `mlt/cvr`  
Most Popular | Conversion rate | `mp/cvr`  
Others You May Like | Watch duration per session | `oyml/wdps`  
Recommended for You | Watch duration per session | `rfy/wdps`  
More Like This | Watch duration per session | `mlt/wdps`  
           
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-GFE-SSL: yes" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global/requirements:checkRequirement" \
         -d '{
               "location": "projects/PROJECT_ID/locations/global",
               "requirementType": "discoveryengine.googleapis.com/media_recs/MODEL_OBJ/warning",
               "resources": [
                 {
                   "labels": {
                     "branch_id": "0",
                     "collection_id": "default_collection",
                     "datastore_id": "DATA_STORE_ID",
                     "location_id": "global",
                     "project_number": "PROJECT_ID"
                   },
                   "type": "discoveryengine.googleapis.com/Branch"
                 },
                 {
                   "labels": {
                     "collection_id": "default_collection",
                     "datastore_id": "DATA_STORE_ID",
                     "location_id": "global",
                     "project_number": "PROJECT_ID"
                   },
                   "type": "discoveryengine.googleapis.com/DataStore"
                 }
               ]
             }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `DATA_STORE_ID`: the ID of the Agent Search data store.
     * `MODEL_OBJ`: see the preceding table to choose the correct value for your recommendations app.

#### Example command and result

This example is for the More Like This model and the watch duration objective:
    
    curl -X POST
    -H "Authorization: Bearer $(gcloud auth print-access-token)"
    -H "Content-Type: application/json"
    -H "X-GFE-SSL: yes"
    -H "X-Goog-User-Project: my-project-123"
    "https://discoveryengine.googleapis.com/v1alpha/projects/my-project-123/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/requirements:checkRequirement"
    -d '{
      "location": "projects/my-project-123/locations/global",
      "requirementType": "discoveryengine.googleapis.com/media_recs/mlt/wdps/warning",
      "resources": [
        {
          "labels": {
            "branch_id": "0",
            "collection_id": "default_collection",
            "datastore_id": "my-data-store",
            "location_id": "global",
            "project_number": "my-project-123"
          },
          "type": "discoveryengine.googleapis.com/Branch"
        },
        {
          "labels": {
            "collection_id": "default_collection",
            "datastore_id": "my-data-store",
            "location_id": "global",
            "project_number": "my-project-123"
          },
          "type": "discoveryengine.googleapis.com/DataStore"
        }
      ]
    }'
        
    
    * * *
    
    
    {
    "requirement": {
    "type": "discoveryengine.googleapis.com/media_recs/mlt/wdps/warning",
    "displayName": "Warning level requirements for 'More Like This' models and 'Watch duration per session' business objectives.",
    "description": "Requirements for the media recommendations model that will result in performance issue if not met for the 'More Like This' model and the 'Watch duration per session' business objective.",
    "condition": {
      "expression": "invalid_sequence_percentage \u003c= invalid_sequence_percentage_threshold"
    },
    "metricBindings": [
      {
        "variableId": "invalid_sequence_percentage",
        "resourceType": "discoveryengine.googleapis.com/DataStore",
        "metricFilter": "metric.type = 'discoveryengine.googleapis.com/datastore/user_events/invalid_sequences_media_play_media_complete' AND metric.labels.is_percentage = 'True'  AND resource.labels.location_id = 'global' AND resource.labels.collection_id = 'default_collection' AND resource.labels.project_number = '123456' AND resource.labels.datastore_id = 'my-data-store'",
        "description": "The percentage of invalid sequences for media play and media complete events sampled by randomly selected visitor ids.",
        "category": "DataStore"
      }
    ],
    "thresholdBindings": [
      {
        "variableId": "invalid_sequence_percentage_threshold",
        "thresholdValues": [
          {
            "severity": "WARNING",
            "value": 50
          }
        ],
        "description": "The threshold for the percentage of invalid sequences sampled among all media play and media complete events."
      }
    ]
    },
    "result": "SUCCESS",
    "requirementCondition": {
    "expression": "invalid_sequence_percentage \u003c= invalid_sequence_percentage_threshold"
    },
    "metricResults": [
    {
      "name": "invalid_sequence_percentage",
      "value": {
        "doubleValue": 0
      },
      "timestamp": "2024-06-06T02:32:00.460056386Z",
      "unit": "%",
      "metricType": "discoveryengine.googleapis.com/datastore/user_events/invalid_sequences_media_play_media_complete"
    }
    ],
    "oldestMetricTimestamp": "2024-06-06T02:32:00.460056386Z"
    }
    

  5. Review the output:

     1. Look for the value of `result`:

        * If the value is `SUCCESS`, then your data is good enough.

        * If the value is `WARNING`, continue to step b.

        * If you don't see `result` in the output, there are a couple possible reasons:

          * The `PROJECT_ID` or `DATA_STORE_ID` in the request is incorrect.

          * Some metric values are unavailable. Try again in 6 hours or reach out to a customer engineer for help.

     2. Look the expression (`requirement.Condition.Expression`). If this expression evaluates to false, then there is a problem with your data.

**Note:** The less-than sign in the expression appears in unicode, `\u003c`, instead of as <.

The value of the metrics can be found in the `requirementCondition.metricResults.value` field, and the warning threshold values, in the `thresholdBindings.thresholdValues` fields. The `description` fields can help you understand the purpose of the metric.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
