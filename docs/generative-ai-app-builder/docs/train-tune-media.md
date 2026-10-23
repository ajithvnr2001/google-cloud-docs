---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/train-tune-media/
title: Train and tune media apps \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:46.467229+00:00
---

# Train and tune media apps  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/train-tune-media/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Train and tune media apps Stay organized with collections  Save and categorize content based on your preferences. 

This page describes tuning and training media recommendations apps.

For information about tuning for search, see [Improve search results with search tuning](https://docs.cloud.google.com/generative-ai-app-builder/docs/tune-search).

Media recommendations apps are automatically tuned every three months, and automatically trained at least once a week and at most once a day. You can use these instructions to manually restart tuning for your app, or to pause and resume training.

## Before you begin

Before you can train or tune your app, you must meet the app's minimum data requirements.

For information about data requirements, see [Prepare data for ingesting](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data#structured-media).

## Manually tune a media recommendations app

Media recommendations apps use the data you upload to adjust hyperparameters for training underlying models. They are automatically tuned every three months.

Tuning keeps training optimal as data and end user behavior change throughout the year. In addition, some internal upgrades can only be applied after the app has been tuned.

For information about tuning costs, see [Pricing](https://docs.cloud.google.com/generative-ai-app-builder/pricing).

Manually restarting tuning triggers a one-time tune for your app. You might restart tuning for your app when there is a significant change in your data store (such as size increase or change in hierarchy) or events (such as backfilling historical events or a change in data distribution after promoting certain groups of content).

To restart tuning, follow these steps:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/start)

  2. Click the name of the app that you plan to tune.

  3. Go to the **Configurations** page and click the **Training** tab. This page shows the tuning status of your app.

  4. Click **Restart tuning**.

Tuning takes 2-4 days, during which the app continues to work as usual.




## Pause and resume training for a model

If your app is active (not paused), training occurs at least once a week, but no more often than once a day. For consistent retraining, make sure that you upload user event data no more than 24 hours after the event occurs.

You can pause your model to stop retraining. You might want to do this if you have imported bad data or to stay under the limit of 10 active recommendation apps per project. If you have fewer than 10 active models, you can restart a paused app at any time.

For training cost details, see [Pricing](https://docs.cloud.google.com/generative-ai-app-builder/pricing).

You can start up to five media app creation, deletion, pause training, and resume training operations per minute.

To pause or resume training:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/start)

  2. Click the name of the app you plan to tune.

  3. Go to the **Configurations** page and click the **Training** tab. This page shows the training status of your app.

  4. To pause training, click _pause_ **Pause training**.

  5. To resume a paused training, click _play_arrow_ **Resume training**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
