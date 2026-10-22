---
url: https://docs.cloud.google.com/deploy/docs/pipeline-instances/
title: Pipeline instances per release \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:45.231036+00:00
---

# Pipeline instances per release  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/pipeline-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Pipeline instances per release Stay organized with collections  Save and categorize content based on your preferences. 

When you invoke Cloud Deploy to create a new release to be managed by your delivery pipeline, the pipeline and targets are preserved in their current state for that release. You can still edit your delivery pipeline and target definition files, but the changes that you make affect future releases only.

**Note:** In addition to storing the pipeline instance with the release, Cloud Deploy also stores the execution environment, as [defined with the target](https://docs.cloud.google.com/deploy/docs/config-files#target_definitions).

## Why does Cloud Deploy do this?

To keep your releases reliable and durable, the delivery pipeline and its associated resources are preserved at the time the release is created. This preservation prevents recent changes to the delivery pipeline definition from affecting the release in ways the generated manifests might not be able to accommodate.

## Why does this matter?

When a delivery pipeline is changed after your release is created, Cloud Deploy delivers the release according to the previous pipeline definition (as it was when the release was created) not the new definition. This behavior isn't a problem unless you, or someone else in your organization, expects the release to follow the updated pipeline behavior.

## When does this matter?

  * When you promote a `release`

When the release was first created, Cloud Deploy took a snapshot of the pipeline. That snapshot—the _pipeline instance_ —is the version of the pipeline that controls the deployment cycle of that `release`.

If anyone _does_ edit the pipeline, and then you promote the release to the next target, Cloud Deploy displays a warning informing you that the deployment might not behave as you expect. You can respond by confirming the promotion or canceling it.



    
    
      gcloud deploy releases promote 
          …
    The pipeline or targets were cached when the release was created, but the source
    has changed since then. You should review the differences before proceeding.
    
    Promoting release xxxx-release-00n to target xxx.
    
    Do you want to continue (Y/n)?
    
    

If you confirm that you want to continue, then the release is promoted to the intended target cluster, with that target configured as defined when you created the `release`. That is, changes to the target do not affect that `release`.

  * When you approve a `rollout`

As with promotion, if you approve a `rollout` and there's a mismatch between the pipeline instance associated with the release, and the current pipeline definition, Cloud Deploy displays a message telling you about the mismatch. You can confirm or cancel the approval.

  * When you roll back a `release`.

If a delivery pipeline or target is changed after a `rollout`, and you try to roll back, there will be a pipeline mismatch. Cloud Deploy will prompt you to confirm you really want to roll back. In this case, we strongly recommend you examine the change to the delivery pipeline or target before rolling back. 




## What you can do

If you change a delivery pipeline, or any of its targets, after a release is created, you can do the following:

  * Let the original pipeline continue executing, without any of the changes from the edited pipeline.

The changes in the pipeline don't affect the rest of the release.

  * Create a new release.

The new release uses the new, edited delivery pipeline, and starts again with the first target in your delivery pipeline progression.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
