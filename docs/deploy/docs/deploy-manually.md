---
url: https://docs.cloud.google.com/deploy/docs/deploy-manually/
title: Deploy manually \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:47.769336+00:00
---

# Deploy manually  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/deploy-manually/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Deploy manually Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manually deploy your application to a specific target.

During normal use, Cloud Deploy deploys your application into each target in the [progression](https://docs.cloud.google.com/deploy/docs/terminology#progression), in sequence. But you can also manually deploy your application to any defined target.

You can manually deploy a new or an existing release.

## Manually deploy an existing release

If a release is already created, you can simply promote it to the intended target:
    
    
    gcloud deploy releases promote --release=RELEASE_NAME \
                           --delivery-pipeline=PIPELINE_NAME \
                           --to-target=TARGET_NAME \
                           --region=REGION
    

Where:

  * RELEASE_NAME is the name of the release which you're manually promoting to the intended target.

  * PIPELINE_NAME is the name of the delivery pipeline that describes the automated deployment progression you're overriding.

  * TARGET_NAME is the name of the target you're manually deploying to.

  * REGION is the name of the region in which the release was created, for example `us-central1`. This is required.




## Manually deploy a new release

By default, when you create a release Cloud Deploy automatically deploys it to the first target in the promotion sequence. But you can specify a target other than the first one.

As with the default first target in the progression, Cloud Deploy automatically creates the `rollout` for the specified target and deploys the release there.

To manually deploy a new release, run the following command:
    
    
    gcloud deploy releases create \
                           --release=RELEASE_NAME \
                           --delivery-pipeline=PIPELINE_NAME \
                           --to-target=TARGET_NAME \
                           --region=REGION
    

Where:

  * RELEASE_NAME is the name of the release which you're manually promoting to the intended target.

  * PIPELINE_NAME is the name of the delivery pipeline that describes the automated deployment progression you're overriding.

  * TARGET_NAME is the name of the target you're manually deploying to.

  * REGION is the name of the region in which to create the release, for example `us-central1`. This is required.




## Effect of manual deployment on the progression

When you manually deploy to a specific target and then promote the release without specifying a target, Cloud Deploy promotes it to the correct next target in the progression. This is because the service tracks the furthest target to which a release has been deployed. If the release is already in the last target in the progression, Cloud Deploy returns a message indicating there is no further target to promote to.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
