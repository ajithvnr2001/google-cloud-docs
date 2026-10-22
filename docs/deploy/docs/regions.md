---
url: https://docs.cloud.google.com/deploy/docs/regions/
title: About Cloud Deploy regions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:24:47.763443+00:00
---

# About Cloud Deploy regions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/regions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  About Cloud Deploy regions Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Deploy service runs as multiple independent, isolated instances in various Google Cloud locations. The location where you create a delivery pipeline determines which Cloud Deploy instance stores and processes requests for that pipeline.

The [Cloud Locations page](https://cloud.google.com/about/locations) lists supported regions for each Google Cloud product, including Cloud Deploy.

**Note:** you must create targets, releases, and rollouts in the same region in which you created the delivery pipeline. GKE clusters and Cloud Run services and jobs represented by those targets, however, can be in any region.

When Cloud Deploy uses other Google Cloud resources for a pipeline, it creates them in the same location if possible, including Cloud Storage buckets, for example, which Cloud Deploy uses to store rendered configuration manifests.

Cloud Deploy instances can deploy applications to locations other than the one where Cloud Deploy is running. This capability allows your delivery pipelines to deploy to multiple regions. However, a given delivery pipeline is only accessible by a single Cloud Deploy instance.

Cloud Deploy instances operate independently, so a failure in one region doesn't affect an instance in another. For this reason, if you are only deploying to a single region, we recommended (but don't require) that you create your pipeline in the same location as your target cluster.

**Note:** your choice of region can have an impact on performance and billing, because data transfers among Google Cloud locations can perform better or worse, depending on location.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
