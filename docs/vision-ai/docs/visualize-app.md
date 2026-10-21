---
url: https://docs.cloud.google.com/vision-ai/docs/visualize-app/
title: Enable and view Visualization output \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:00.175022+00:00
---

# Enable and view Visualization output  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/visualize-app/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Enable and view Visualization output Stay organized with collections  Save and categorize content based on your preferences. 

After you [create an app](https://docs.cloud.google.com/vision-ai/docs/build-app), you can enable visualization output during the deployment step. Then, view the output stream.

## Deploy an app with visualization output enabled

After you have built an end-to-end application with all the necessary components you must deploy the app to start using it. When you deploy, you have the option to enable visualization.

### Console

  1. Open the **Applications** tab of the Gemini Enterprise Agent Platform Vision dashboard.

[Go to the Applications tab](https://console.cloud.google.com/ai/vision-ai/applications)

  2. Find your application from the list and, next to it, select **View app**.

  3. From the application graph builder page, click **Deploy**.

  4. In the **Deploy application** menu that opens, select any other options that apply and check_box **Enable visualization**.

  5. Choose the input you want to visualize from the drop-down menu below the checkbox option.

  6. Click **Deploy**.

After deployment, green check marks appear next to the nodes.




## View output visualization

After an app has been deployed for some minutes, you can access a visualization of the selected input.

### Console

  1. Open the **Applications** tab of the Gemini Enterprise Agent Platform Vision dashboard.

[Go to the Applications tab](https://console.cloud.google.com/ai/vision-ai/applications)

  2. Find your application from the list and, next to it, select **View app**.

  3. From the application graph builder page, click insert_chart_outlined**View Output Visualization**.

You're then prompted to select the input and processor to visualize.

  4. Select **View** to be directed to a stream page and view the visualization stream.

![View Visualization option](https://docs.cloud.google.com/static/vision-ai/docs/images/visualization-stream-view.png)




## What's next

  * Read instructions about how to begin data ingestion from an app's input stream in [Create and manage streams](https://docs.cloud.google.com/vision-ai/docs/create-manage-streams#ingest-videos).
  * Learn how to list apps and view a deployed app's instances in [Managing applications](https://docs.cloud.google.com/vision-ai/docs/manage-app).
  * Learn how to read app input data from an ingestion stream or analyzed model output data in [Read stream data](https://docs.cloud.google.com/vision-ai/docs/read-stream).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
