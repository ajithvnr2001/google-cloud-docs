---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/operate/metadata-keys-warning/
title: Metadata keys quota warning \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:06.032304+00:00
---

# Metadata keys quota warning  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/operate/metadata-keys-warning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Metadata keys quota warning

As of v1.4.0, Manufacturing Data Engine (MDE) keeps track of the number of metadata instances per natural-key. When the size of the natural-key instances reaches 50% of the maximum limit (which is 200), MDE sends a warning to indicate that the natural-keys will be removed if no action is taken. This is pushed using the [Notification service](https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/operate/notification-api).

You will then be able to filter through the exact natural-keys that are growing and take action to fix the configuration and avoid automatic deletion.

There is a dedicated tab in the web interface to filter through the natural-keys, and if you are using the API, you can use the following filters to narrow down the search for the affected natural-keys:

  * Bucket name
  * Natural key
  * Sort by the detection time



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
