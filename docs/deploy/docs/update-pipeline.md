---
url: https://docs.cloud.google.com/deploy/docs/update-pipeline/
title: Update a delivery pipeline that's already in use \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:15:48.359878+00:00
---

# Update a delivery pipeline that's already in use  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/update-pipeline/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Update a delivery pipeline that's already in use Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to update a delivery pipeline that's already in use.

## Change a delivery pipeline

To change your delivery pipeline consists of the following steps:

  1. Edit the [delivery-pipeline definition](https://docs.cloud.google.com/deploy/docs/config-files).

  2. Re-register the delivery pipeline:
         
         gcloud deploy apply --file=PIPELINE_CONFIG
         

Where PIPELINE_CONFIG is the delivery pipeline configuration file that you just edited.




## Results

You might not see the results you expect, because of how Cloud Deploy treats the relationship between pipelines and targets and the releases they manage.

Each `release` and `rollout` resource is permanently associated with the pipeline as it was defined when the `release` was created. If you change a delivery pipeline configuration (including target definitions) after a release is created, that release is now mismatched from the definitions.

Preserving resources in this way ensures they function consistently across the targets and they're not disrupted by configuration changes. However this behavior might not be what you intend, in which case you can create a new release to deploy using the updated pipeline.

Cloud Deploy returns warnings if there's such a mismatch and you try to perform certain actions, such as promote the release.

For more information, see [Pipeline instances per release](https://docs.cloud.google.com/deploy/docs/pipeline-instances).

## What's next

  * Find out how to [view delivery pipelines](https://docs.cloud.google.com/deploy/docs/view-pipeline) that are already in use.

  * Learn how to [suspend a delivery pipeline](https://docs.cloud.google.com/deploy/docs/suspend-pipeline).

  * Find out how to [delete a delivery pipeline](https://docs.cloud.google.com/deploy/docs/delete-pipeline).

  * Learn how to [use service notifications](https://docs.cloud.google.com/deploy/docs/subscribe-deploy-notifications)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
