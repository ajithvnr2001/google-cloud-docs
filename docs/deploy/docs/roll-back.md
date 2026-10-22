---
url: https://docs.cloud.google.com/deploy/docs/roll-back/
title: Roll back a target \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:44.409595+00:00
---

# Roll back a target  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/roll-back/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Roll back a target Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to roll back a Cloud Deploy target to an earlier release.

When you roll back a target, Cloud Deploy creates a new `rollout` resource based on a previous release.

## Roll back a target to an earlier release

###  gcloud CLI 

By default, the rollback uses the last release with a successful rollout to the indicated target, but you can choose a different one, using `--release`.

To roll back, run the following command from the directory containing your delivery pipeline:
    
    
    gcloud deploy targets rollback TARGET_NAME \
       --delivery-pipeline=PIPELINE_NAME \
       --release=RELEASE_NAME \
       --rollout-id=ROLLOUT_ID
    

In this command, `--release` and `--rollout-id` are optional. Use `--release` to identify a specific release to roll back to. If you omit this option, then Cloud Deploy uses the last known good release to the specified target.

Use `--rollout-id` to assign an identifier to the generated `rollout`. If you omit this, Cloud Deploy generates an ID for the generated `rollout`.

###  Console 

  1. [Open the Delivery pipelines page](https://console.cloud.google.com/deploy/delivery-pipelines).

  2. Click your pipeline shown in the list of delivery pipelines.

The Delivery pipeline details page shows a graphical representation of the progress of your delivery pipeline.

  3. Click the more menu ![The more menu](https://docs.cloud.google.com/static/deploy/images/more_menu.png) and select **Roll back release**.

![Select Rollback release from the menu. ](https://docs.cloud.google.com/static/deploy/images/pipeline-for-rollback.png)

The rollback form is displayed:

![Rollback form](https://docs.cloud.google.com/static/deploy/images/rollback_form.png)

  4. Select the release from the **Release** field.

This release is the one which you're rolling back to. The **Rollout name** is populated based on the selected release.

  5. If you want, you can change the rollout name and rollout description from the default.

  6. Click **Roll back**.

A new rollout is created from the chosen release, and deployed into the same target.




### Roll back even further

You can roll back _manually_ to an earlier release than the last successfully deployed one.

Simply run `gcloud deploy releases promote` with the earlier release and include the`--to-target` option set to the target in which you want to roll back your release.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
