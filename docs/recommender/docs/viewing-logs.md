---
url: https://docs.cloud.google.com/recommender/docs/viewing-logs/
title: View logs \u00a0|\u00a0 Recommender \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:44:05.429423+00:00
---

# View logs  |  Recommender  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recommender/docs/viewing-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Recommender ](https://docs.cloud.google.com/recommender/docs)
  * [ Guides ](https://docs.cloud.google.com/recommender/docs/whatis-activeassist)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View logs

Recommender logs record changes to recommendation and insight state.

## Permissions

Identity and Access Management permissions and roles determine which logs you can view and export.

To view Recommender logs, you must have one of the following IAM roles in the project that contains your logs:

  * One of the basic roles: **Project Owner** , **Project Editor** , or **Project Viewer**.
  * The Cloud Logging [**Logs Viewer**](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles) role.
  * A [custom IAM role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) with the `logging.logEntries.list` IAM permission.



## View recommendation logs

To view recommendation action logs:

  1. Go to the **Google Cloud Observability Logging > Logs** (Logs Explorer) page in the Google Cloud console:

[Go to the Logs Explorer page](https://console.cloud.google.com/logs/query)

  2. Select an existing Google Cloud project at the top of the page or create a new project.

  3. In the drop-down menu for resource type, select **Recommender**.

If the **Show query** toggle is **On** , your query becomes `resource.type="recommender"`.

  4. Expand a log entry to view the entry details. The following example shows a claimed recommendation.
         
         {
          insertId:  "t51fxaa1"
          jsonPayload: {
           @type:  "type.googleapis.com/google.cloud.recommender.logging.v1.ActionLog"
           actor:  "user@gmail.com"
           recommendationName:   "projects/my-recommender-project/locations/global/recommenders/google.iam.policy.Recommender/recommendations/r1"
           state:  "CLAIMED"
           stateMetadata: {
             my_metadata: "Some metadata."
           }
          }
          logName:  "projects/my-recommender-project/logs/recommender.googleapis.com%2Factions"
          receiveTimestamp:  "2019-07-01T21:55:06.950795284Z"
          resource: {
           labels: {
            location:  "global"
            project_id:  "my-recommender-project"
            recommender_id:  "google.iam.policy.Recommender"
           }
           type:  "recommender"
          }
          severity:  "INFO"
          timestamp:  "2019-07-01T21:55:06.529Z"
         }
         




## View insight logs

To view insight action logs:

  1. Go to the **Google Cloud Observability Logging > Logs** (Logs Explorer) page in the Google Cloud console:

[Go to the Logs Explorer page](https://console.cloud.google.com/logs/query)

  2. Select an existing Google Cloud project at the top of the page or create a new project.

  3. In the drop-down menu for resource type, select **InsightType**.

If the **Show query** toggle is **On** , your query becomes `resource.type="recommender_insight_type"`.

  4. Expand a log entry to view the entry details. The following example shows an accepted insight.
         
         {
          insertId:  "t51fxaa1"
          jsonPayload: {
           @type:  "type.googleapis.com/google.cloud.recommender.logging.v1.InsightActionLog"
           actor:  "user@gmail.com"
           insight:   "projects/my-recommender-project/locations/global/insightTypes/google.iam.policy.Insight/insights/i1"
           state:  "ACCEPTED"
           stateMetadata: {
             my_metadata: "Some metadata."
           }
          }
          logName:  "projects/my-recommender-project/logs/recommender.googleapis.com%2Factions"
          receiveTimestamp:  "2019-07-01T21:55:06.950795284Z"
          resource: {
           labels: {
            location:  "global"
            project_id:  "my-recommender-project"
            insight_type_id:  "google.iam.policy.Recommender"
           }
           type:  "recommender_insight_type"
          }
          severity:  "INFO"
          timestamp:  "2019-07-01T21:55:06.529Z"
         }
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
