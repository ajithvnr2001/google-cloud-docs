---
url: https://docs.cloud.google.com/deploy/docs/abandon-release/
title: Abandon a release \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:50.515635+00:00
---

# Abandon a release  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/abandon-release/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Abandon a release Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to permanently abandon a Cloud Deploy release.

You can permanently [abandon](https://docs.cloud.google.com/deploy/docs/terminology#abandon) a release. An abandoned release has the following characteristics:

  * You can't promote an abandoned release.

  * You can't roll back to an abandoned release.

  * You can't unabandon a release. After you abandon a release, it's permanently deactivated.




Reasons for abandoning a release include the following, for example:

  * There's a bug in the release

  * There's a security issue in the release

  * A feature included in the release has been deprecated




To abandon a release, run the following command:
    
    
    gcloud deploy releases abandon RELEASE_NAME --delivery-pipeline=PIPELINE_NAME --region=REGION
    

Where:

  * RELEASE_NAME

Is the name of the release to abandon. This is required.

  * PIPELINE_NAME

Is the name of the delivery pipeline that created the release. This is required.

  * REGION

Is the name of the region in which the release was created, for example `us-central1`. This is required.




## IAM permissions

The IAM permissions required for abandoning a release are included in the following roles:

  * roles/clouddeploy.admin

  * roles/clouddeploy.operator

  * roles/clouddeploy.developer




## Rollouts from abandoned releases

When you abandon a release, any rollouts created from that release that are in progress or queued continue to completion—they are not cancelled. However, you can't create new rollouts from an abandoned release.

## View abandoned releases

In Google Cloud console, you can see if a release has been abandoned. The **Releases** tab, on the Delivery pipeline details page, labels the release as "abandoned":

![List of releases in Google Cloud console showing an abandoned release](https://docs.cloud.google.com/static/deploy/images/abandoned_release.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
