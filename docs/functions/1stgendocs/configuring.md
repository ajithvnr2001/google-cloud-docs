---
url: https://docs.cloud.google.com/functions/1stgendocs/configuring/
title: Configure Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:38.249167+00:00
---

# Configure Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/configuring/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure Cloud Run functions (1st gen)

Use this page to understand what configuration options are available in Cloud Run functions, how to control the behavior of your functions, and what the best practices are for each type of configuration.

## Guard against high request levels

You can control how many instances your function creates to serve requests. This can help to curb costs and guard against [abnormally high request levels](https://docs.cloud.google.com/functions/1stgendocs/configuring/max-instances#limits_best_practices). See [Using maximum instances](https://docs.cloud.google.com/functions/1stgendocs/configuring/max-instances) to learn more.

## Avoid cold starts and reduce latency

You can avoid cold starts for your application and reduce application latency by setting a minimum number of instances. Note that setting a minimum number of instances incurs cost. See [Using minimum instances](https://docs.cloud.google.com/functions/1stgendocs/configuring/min-instances) to learn more.

## Secrets

You can use [Secret Manager](https://docs.cloud.google.com/secret-manager/docs#docs) with your Cloud Run functions to securely store API keys, passwords, and other sensitive information. See [Using secrets](https://docs.cloud.google.com/functions/1stgendocs/configuring/secrets) to learn more.

## Environment variables

You can create key/value pairs for use with your function. See [Using environment variables](https://docs.cloud.google.com/functions/1stgendocs/configuring/env-var) to learn more.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
