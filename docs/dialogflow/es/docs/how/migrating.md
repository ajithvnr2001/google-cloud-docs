---
url: https://docs.cloud.google.com/dialogflow/es/docs/how/migrating/
title: Migrating between Dialogflow versions \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:45:20.230103+00:00
---

# Migrating between Dialogflow versions  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/how/migrating/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Migrating between Dialogflow versions Stay organized with collections  Save and categorize content based on your preferences. 

## V2beta1 to V2

The V2beta1 API is used to share beta features with Dialogflow users. This section has advice for switching to the stable V2 API.

**Important:** The default behavior for enabling machine learning has changed. See details below.

  * If you are using REST or RPC, update the endpoint from `dialogflow.googleapis.com/v2beta1/...` to `dialogflow.googleapis.com/v2/...`
  * If you are using a [client library](https://docs.cloud.google.com/dialogflow/docs/reference/libraries), update it: 
    * **Dynamic languages** (Python, Node.js, Ruby): Upgrade the package, and your code will automatically use the latest stable version.
    * **Static languages** (Java, C#, PHP, Go): Install the new package and update all import statements to reference "v2" instead of "v2beta1".
  * The field that controls whether machine learning (ML) is enabled for an `Intent` has changed. The `mlEnabled` field has been removed and replaced by the `mlDisabled` field, and ML is enabled by default. Version | REST | RPC | Default value | Default behavior  
---|---|---|---|---  
V2beta1 | [mlEnabled](https://docs.cloud.google.com/dialogflow/docs/reference/rest/v2beta1/projects.agent.intents#Intent.FIELDS.ml_enabled) | [ml_enabled](https://docs.cloud.google.com/dialogflow/docs/reference/rpc/google.cloud.dialogflow.v2beta1#google.cloud.dialogflow.v2beta1.Intent.FIELDS.bool.google.cloud.dialogflow.v2beta1.Intent.ml_enabled) |  true  |  ML is enabled   
V2 | [mlDisabled](https://docs.cloud.google.com/dialogflow/docs/reference/rest/v2/projects.agent.intents#Intent.FIELDS.ml_disabled) | [ml_disabled](https://docs.cloud.google.com/dialogflow/docs/reference/rpc/google.cloud.dialogflow.v2#google.cloud.dialogflow.v2.Intent.FIELDS.bool.google.cloud.dialogflow.v2.Intent.ml_disabled) | false | ML is enabled  



[ Previous arrow_back  Regionalization and data residency  ](https://docs.cloud.google.com/dialogflow/es/docs/how/region)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
