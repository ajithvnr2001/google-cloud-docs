---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/configurable-dashboards/
title: Configurable dashboards \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:45.201829+00:00
---

# Configurable dashboards  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/configurable-dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Configurable dashboards Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

View usage and feedback metrics from Customer Experience Insights over time with a configurable dashboard. Configurable dashboards offer flexibility in data representation and layout because you can build and maintain custom views with a variety of charts. The configurable dashboard gives you the ability to select a chart type, store the configuration, and retrieve it the next time you visit the page.

## Dashboard components

A dashboard contains the following components.

Component | Description  
---|---  
Dashboard | The top-level resource that stores the entire structure and chart definitions.  
Section | A section can have tiles or nested sections (these appears as tabs). Dashboard sections can have a display name and description. You can apply the date_range filter to all the charts in an entire tab. Sections define their physical dimensions using width and height in grid units.  
Tile | An element within the dashboard, defined as a nested section or a chart. The default date range is last week. You can further query the date_range as last 1 day, last 2 days, last 1 week, last 2 weeks, last 1 month, last 1 quarter, last 1 year or the customized start and end dates.  
  
## Dashboard field definitions

Each dashboard is made up of the following fields. Only `display_name` and `description` appear in the console.

Field | Description | Constraints/Notes  
---|---|---  
`name` | Dashboard name | Format: `projects/{project}/locations/{location}/dashboards/{dashboard}`  
`display_name` | User-provided name for the dashboard | Maximum of 100 characters  
`description` | Dashboard description | Optional  
`create_time` | Dashboard creation timestamp | Output-only  
`update_time` | Dashboard last update timestamp | Output-only  
`filter` | Filter for all charts in the dashboard | Supports optional string filter  
  
## Data and querying

The chart uses natural language (NL), which Customer Experience Insights translates in SQL queries. These queries generate the data and visual specifications to display the chart. Visual specifications are in a [VEGA-LITE](https://vega.github.io/vega-lite/docs) format. The chart API uses the `GenerativeInsights data` source, `session_id`, and `revision_id` to store the current SQL and visual specifications states of a chart.

## Dashboard operations

You can perform the following operations on configurable dashboards.

### Create dashboard

Follow these steps to create your dashboard.

### Console

  1. Navigate to the CX Insights console, sign in with your Google Account, and select your project.

[CX Insights console](https://ccai.cloud.google.com/insights)

  2. Click **Dashboard**. Here, you can see both prebuilt and custom dashboards.

  3. On the Dashboard studio, click **\+ Add dashboard** to create your own custom dashboard.

  4. Each dashboard appears in the form of a tile.

  5. When you click a dashboard, it gives an overview of all the charts.




### REST API

Submit a request like the following example.
    
    
    {
    "displayName": "My New Dashboard with Container",
    "root_container": {
      "displayName": "Overview tab",
      "widgets": [
       {
          "container": {
            "displayName": "Inner Chart Group 1",
            "widgets": [
              {
                "chart": {
                  "displayName": "Most Reported Issues"
                  "dataSource": {"generativeInsights": "What are top 5 issues?"}
                }
              },
              {
                "chart": {
                  "displayName": "Topic Distribution"
                  "dataSource": {"generativeInsights": "What are the topics?"}
                }
              }
            ]
          }
        }
      ]
    }
    }
    

### Curl

Run the following curl command. In this example, the payload is saved in `create_dashboard_nested.json`.
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth --impersonate-service-account=$SA_EMAIL print-access-token)" \
    -H "Content-Type: application/json; charset=utf-8" \
    -d @create_dashboard_nested.json
    "https://$ENDPOINT/v1/projects/$PROJECT/locations/$LOCATION/dashboards?dashboard_id=$DASHBOARD_ID"
    

### Edit dashboard

Follow these steps to edit your dashboard.

### Console

  1. Choose a dashboard and click **More** more_vert > **Edit** to edit the dashboard.

  2. Choose one of the following options:



  * **\+ Add tile**
  * **\+ Add section**
  * edit **Rename tab**
  * content_copy **Duplicate tab**
  * delete **Delete tab**
  * Choose a date range to view your results.
  * Choose a tile and click **More** more_vert. A side panel appears with the following options: Ask AI, Tile settings, and Query editor.



#### Additional options

**Ask AI** : Click Ask AI and enter a text description of your changes. The AI assistant can help you in building your dashboard. You also have an option to ask follow-up questions to the AI assistant. If you click **Save Chart** , you can rollback to the previous visualizations. Natural language (NL) lets you to generate visualizations by specifying descriptive queries like _What is the average conversation count each day for a virtual agent?_ These queries are converted into SQL for execution against BigQuery and visual specification (VEGA lite) for display purposes.

**Tile settings** : In this section, you can update the visual specification directly to control the chart attribute. For example: Change the display name of the chart. You can choose your preferred chart type in the drop-down menu. The chart API supports the following chart types and data representations:

  * BAR
  * LINE
  * AREA
  * PIE
  * SCATTER
  * TABLE
  * SCORE_CARD
  * SUNBURST
  * GAUGE
  * SANKEY



You can further specify the conversation filter or new time range upon reloading the dashboard.

**Query editor** : You can interact with the AI assistant and build a dashboard. If you are not satisfied with the AI-generated SQL response, you can update the SQL directly to regenerate a chart and the SQL response further repopulates the existing visual specification. The query editor displays the generated SQL, whose table name is masked to reference a predefined placeholder string, `INSIGHTS_DASHBOARD_VIEW`. Note: You can only do any `SELECT` operation.

### Curl

Run the following curl command. In this example, the payload is saved in `update_dashboard.json`.
    
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth --impersonate-service-account=$SA_EMAIL print-access-token)" \
    -H "Content-Type: application/json; charset=utf-8" \
    -d @update_dashboard.json \
    "https://$ENDPOINT/v1/projects/$PROJECT/locations/$LOCATION/dashboards/$DASHBOARD_ID?update_mask=root_container"
    

### Delete dashboard

Follow these steps to delete a dashboard and all related charts.

### Console

Choose a dashboard and click **More** more_vert > **Delete** to delete the dashboard.

### Curl

Run the following curl command.
    
    
    curl -X DELETE \
    -H "Authorization: Bearer $(gcloud auth --impersonate-service-account=$SA_EMAIL print-access-token)" \
    "https://$ENDPOINT/v1/projects/$PROJECT/locations/$LOCATION/dashboards/$DASHBOARD_ID"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
