---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/traffic-split/
title: Traffic splitting (A/B testing) \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:03.809873+00:00
---

# Traffic splitting (A/B testing)  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/traffic-split/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Traffic splitting (A/B testing) Stay organized with collections  Save and categorize content based on your preferences. 

Traffic splitting lets you divide user conversations across different [versions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/version) of your CX Agent Studio agent application within a single deployment channel. You can use traffic splitting to conduct A/B testing or safely deploy updates in stages by routing a specified percentage of traffic to each version.

This guide describes how to configure traffic splitting using the **[CX Agent Studio console](https://ces.cloud.google.com)** or the **CX Agent Studio REST API** , and analyze version performance using BigQuery logs once your experiment receives live customer traffic.

## Workflow overview

  1. **Create application versions** : Create immutable snapshots ([versions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/version)) of your agent application to compare.
  2. **Configure traffic splitting on a deployment channel** : Assign traffic percentages across multiple application versions using the console or REST API.
  3. **Analyze performance in BigQuery** : Once your experiment is running and has processed sufficient customer traffic, query exported conversation logs in BigQuery to evaluate metrics across versions.



## Configure traffic splitting

You can configure traffic allocations across different application versions using either the console or the REST API. Each allocation must point to an existing [agent application version](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/version), and the sum of all traffic percentages in the deployment must equal 100.

### Using the console

To configure traffic splitting in the agent builder console:

  1. Open the [CX Agent Studio console](https://ces.cloud.google.com) and select your agent application.
  2. Click **Deploy** tab at the top of the page.
  3. Select an existing deployment channel or click **New channel** to create one (for example, [API access](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/api-access)).
  4. Under **Agent version** , click **Add version** and select the agent application versions you want to include in the experiment.
  5. Enter the **Traffic percentage** for each version (for example, `90`% for Version A and `10`% for Version B). Ensure the percentages total 100%.
  6. Click **Create channel** to apply the configuration.



### Using the REST API

You can programmatically set up traffic splitting by calling the [`patch`](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.deployments/patch) method on your deployment resource and defining `experimentConfig.versionRelease.trafficAllocations`.

Before calling the API, ensure you have the following identifiers:

  * `PROJECT_ID`: Your Google Cloud project ID.
  * `LOCATION_ID`: The region of your agent application (for example, `us-east1`).
  * `APP_ID`: The ID of your agent application.
  * `DEPLOYMENT_ID`: The ID of the deployment channel.
  * `VERSION_A_UUID` / `VERSION_B_UUID`: The unique identifiers of your application versions.



Send a `PATCH` request to update the deployment configuration:
    
    
    curl -X PATCH \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      "https://ces.googleapis.com/v1beta/projects/PROJECT_ID/locations/LOCATION_ID/apps/APP_ID/deployments/DEPLOYMENT_ID?updateMask=experimentConfig" \
      -d '{
        "experimentConfig": {
          "versionRelease": {
            "trafficAllocations": [
              {
                "appVersion": "projects/PROJECT_ID/locations/LOCATION_ID/apps/APP_ID/versions/VERSION_A_UUID",
                "trafficPercentage": 90
              },
              {
                "appVersion": "projects/PROJECT_ID/locations/LOCATION_ID/apps/APP_ID/versions/VERSION_B_UUID",
                "trafficPercentage": 10
              }
            ]
          }
        }
      }'
    

## Verify deployment configuration

To verify that your traffic allocations are active:

### Using the console

  1. Open the **Deploy** page in the [CX Agent Studio console](https://ces.cloud.google.com).
  2. Locate your channel in the deployments list.
  3. Verify that the **Version** column displays the configured split (for example, `Version A (90%), Version B (10%)`).



### Using the REST API

Send a `GET` request to retrieve the deployment resource details:
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://ces.googleapis.com/v1beta/projects/PROJECT_ID/locations/LOCATION_ID/apps/APP_ID/deployments/DEPLOYMENT_ID"
    

The response JSON includes the active `experimentConfig` confirming the traffic percentages assigned to each version and displaying `"state": "RUNNING"` inside `versionRelease`.

## Analyze version performance in BigQuery

Once your traffic split experiment is running and has processed sufficient live customer conversation volume, you can analyze version performance using BigQuery logs.

Before analyzing logs, ensure you have enabled BigQuery export for your application by navigating in the [CX Agent Studio console](https://ces.cloud.google.com) to **Build** > **Settings** > **Advanced** and turning on **Export logs to BigQuery**. When export is enabled, interaction records—including the specific `app_version_id` handled by each turn—are recorded in your BigQuery dataset.

You can run SQL queries to evaluate and compare the responses generated by each version during your traffic split window.

  1. In the Google Cloud console, go to **BigQuery**.
  2. Run the example query against your interaction logs table, substituting your project details and evaluation window (`START_TIME` and `END_TIME`):
         
         SELECT
           app_version_id,
           tool_call.name AS tool_name,
           tool_call.output AS tool_result_message,
           COUNT(1) AS count
         FROM
           `PROJECT_ID.conversational_agents_logs.v1beta_logs`,
           UNNEST(json_payload.query_result.generations) AS generation,
           UNNEST(generation.tool_calls) AS tool_call
         WHERE
           json_payload.resource = 'projects/PROJECT_ID/locations/LOCATION_ID/apps/APP_ID'
           AND timestamp >= TIMESTAMP('START_TIME_YYYY-MM-DD HH:MM:SS', 'TIMEZONE')
           AND timestamp <= TIMESTAMP('END_TIME_YYYY-MM-DD HH:MM:SS', 'TIMEZONE')
         GROUP BY
           app_version_id, tool_name, tool_result_message
         ORDER BY
           app_version_id, count DESC
         

  3. **Evaluate metrics** :

     * **Identify versions** : Map the output rows to your specific version UUIDs or tool executions (for example, comparing responses from Version A versus Version B).
     * **Calculate success rate** : Compare the ratio of outcomes against errors or outdated responses across the two versions to decide whether to promote the candidate version to 100% of traffic.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
