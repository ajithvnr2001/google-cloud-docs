---
url: https://docs.cloud.google.com/developer-connect/docs/data-residency/
title: About data residency \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:53.187596+00:00
---

# About data residency  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/data-residency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Guides ](https://docs.cloud.google.com/developer-connect/docs/overview)



Send feedback 

#  About data residency Stay organized with collections  Save and categorize content based on your preferences. 

Developer Connect complies with [data residency requirements](https://cloud.google.com/terms/data-residency). Data residency describes where your data is stored _at rest_. To ensure compliance, Developer Connect does the following:

  * stores resource data in regional Spanner instances
  * replicates data only within designated cloud regions
  * queues webhook data within regional Spanner queues



However, this isn't true for all connections. By default, [GitHub connections](https://docs.cloud.google.com/developer-connect/docs/connect-github-repo) use a global Pub/Sub topic for event delivery. The topic is then replicated to regional subscriptions. Although the Pub/Sub messages aren't stored permanently by Pub/Sub, this global routing doesn't meet data residency requirements because Pub/Sub stores each message in a global topic temporarily.

When you create a GitHub connection using Google Cloud CLI, that connection is regional, but the Developer Connect GitHub app that the connection uses is global, and therefore doesn't comply with data residency requirements.

When you create a GitHub connection using Google Cloud console, data residency is disabled by default for that connection. You can enable it by activating the **Enable data residency** checkbox. Doing so makes this GitHub connection data-residency compliant. Developer Connect creates a GitHub app for your connection, owned by your GitHub user account or organization. The app uses a per-connection, regionalized webhook endpoint that avoids sending data to a global Pub/Sub topic.

To create a data-residency compliant GitHub connection, see [Connect to GitHub](https://docs.cloud.google.com/developer-connect/docs/connect-github-repo#connection). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
