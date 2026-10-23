---
url: https://docs.cloud.google.com/application-integration/docs/cancel-executions/
title: Cancel executions \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:27.642180+00:00
---

# Cancel executions  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/cancel-executions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cancel executions

If you have an execution that is suspended due to an approval task or a technical issue, you can choose to cancel the execution. You can cancel an integration execution if the integration is in one of the following [execution states](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.executions#state):

  * **Suspended**
  * **On hold**
  * **Retry on hold**



## Cancel an execution

To cancel an execution, select one of the following options:

### Console

  1. In **Application Integration** , go to the **Logs** page. 

[Go to Application Integration Logs](https://console.cloud.google.com/integrations/logs)

  2. In the navigation menu, click **Logs**. The **Execution Logs** page appears.
  3. For the execution that you want to cancel, click **more_vert** and then **cancel Cancel**. The **Cancel execution** pane appears.
  4. Add the reason to replay the execution.
  5. Click **Cancel Execution**.



### API

Call the [`projects.locations.integrations.executions.cancel` method](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.executions/cancel) and provide the ID of the execution that you want to cancel:
    
    
    curl -X POST https://integrations.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/integrations/INTEGRATION_NAME/executions/EXECUTION_ID:cancel -H "Authorization: Bearer $TOKEN"

## Limitations

Cancel execution is subject to the following limitations:

  * Canceling an execution that is triggered by a [Schedule trigger](https://docs.cloud.google.com/application-integration/docs/configure-schedule-trigger) isn't supported.
  * You can't cancel an integration execution if the integration is in one of the following states: 
    * **In process**
    * **Succeeded**
    * **Failed**
    * **Canceled**



## What's next

  * Learn about [logs in Application Integration](https://docs.cloud.google.com/application-integration/docs/introduction-logs).
  * Learn how to [test and publish integrations](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
