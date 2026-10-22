---
url: https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/agent-card/
title: Add your AI agent's Agent Card \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:44.983415+00:00
---

# Add your AI agent's Agent Card  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/agent-card/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Add your AI agent's Agent Card Stay organized with collections  Save and categorize content based on your preferences. 

AI agents from Cloud Marketplace use the [Agent2Agent (A2A) protocol](https://a2a-protocol.org/latest/topics/what-is-a2a/) to communicate and collaborate with other AI agents. For each AI agent that you offer through Cloud Marketplace, you must create an _Agent Card_ aligned to the [A2A Agent Card specification](https://a2a-protocol.org/dev/specification/). Your AI agent's Agent Card defines its presence on Cloud Marketplace, detailing its capabilities and facilitating its coordination with other AI agents. Agent Cards exist as JSON files stored in Cloud Storage.

After you've created an Agent Card for the AI agent that you're offering through Cloud Marketplace, use the **Agent Card** tab in Producer Portal to complete the following steps:

  * Add the Agent Card for your AI agent's Google Cloud Marketplace listing.
  * Submit your AI agent's Agent Card to Google for validation. To publish your AI agent, you must have successfully validated its Agent Card.



## Before you begin

  * To access Producer Portal, you must have completed the _Cloud Marketplace Project Info Form_ , provided by the Google Cloud Marketplace team. For more information about becoming a Cloud Marketplace vendor, see [Sign up as a Cloud Marketplace vendor](https://docs.cloud.google.com/marketplace/docs/partners/offer-products#initiate-onboarding).

If you can't access Producer Portal, verify that you've selected the correct project. If you still can't access it, use the [Google Cloud Support portal](https://g.co/cloud/psd-partner) to request assistance, and include the word "Marketplace" in your description. For more information about the Google Cloud Support portal, visit [Request assistance with Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/get-support).

  * Add your AI agent as a product in Producer Portal. For steps, see [Add your AI agent in Producer Portal](https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/add-product).




## Add an Agent Card

To add your AI agent's Agent Card to its Cloud Marketplace listing, use [Producer Portal](https://console.cloud.google.com/producer-portal). In Producer Portal, select your AI agent and complete the following steps:

  1. [Upload your Agent Card](https://docs.cloud.google.com/storage/docs/uploading-objects) as a JSON file to a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) with [Object Versioning enabled](https://docs.cloud.google.com/storage/docs/using-object-versioning) under the same project.

  2. On the **Overview** page of your AI agent product, go to the **Agent Card** section and click **Browse**. It will pop up a Cloud Storage file selector, select your agent card file.

  3. Click **Save and validate**. Cloud Marketplace validates your Agent Card to ensure that it meets the necessary thresholds for an acceptable and robust Agent Card, and displays its progress on this page. If your Agent Card doesn't meet the requirements, you are provided with a list of gaps to address. For details about the validation tests and thresholds, consult the Agent ScoreCard guide provided to you.

  4. When prompted, choose whether to populate your product's description and metadata fields using content from your Agent Card. You can override the populated content when you complete the rest of your Cloud Marketplace listing.

To help customers evaluate your product, we strongly recommend creating an Agent Card that's as complete as possible. Important features to include are skills, competence, models, and security.




## What's next

  * Add your AI agent's [product details](https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/product-details).
  * Complete your [integration of your AI agent with Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/technical-integration).



[ Previous arrow_back  Add pricing information  ](https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/choose-pricing)

[ Next Integrate your AI agent with Cloud Marketplace  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/technical-integration)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
