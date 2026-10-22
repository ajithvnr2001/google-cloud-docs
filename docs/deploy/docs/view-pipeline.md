---
url: https://docs.cloud.google.com/deploy/docs/view-pipeline/
title: View delivery pipelines \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:26.282177+00:00
---

# View delivery pipelines  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/view-pipeline/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  View delivery pipelines Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view all your delivery pipelines in a project.

You can see a list of all your Cloud Deploy delivery pipelines for all your projects. You can list them from the command line, and you can view the list in Google Cloud console.

## View a list of delivery pipelines

###  Console 

In the Google Cloud console, navigate to the Cloud Deploy **Delivery pipelines** page to view a list of your available delivery pipelines.

[Open the Delivery pipelines page](https://console.cloud.google.com/deploy/delivery-pipelines)

The list of delivery pipelines is shown in Google Cloud console.

![Delivery pipelines page in Google Cloud console, showing list of pipelines](https://docs.cloud.google.com/static/deploy/images/pipelines-page-1.png)

Delivery pipelines that have been configured but not [registered with the Cloud Deploy service](https://docs.cloud.google.com/deploy/docs/create-pipeline-targets#register_the_delivery_pipeline_and_targets) are not shown.

###  gcloud 

The following command returns a list of all delivery pipelines in the current project.
    
    
    gcloud deploy delivery-pipelines list
    

You should see an output similar to the following:
    
    
    $ gcloud deploy delivery-pipelines list --region=$REGION
    ---
    createTime: '2021-05-03T16:03:11.687046682Z'
    description: main application pipeline
    etag: a9721c6cf665fcc7
    name: projects/try-cd-dev6/locations/us-central1/deliveryPipelines/my-demo-app-1
    serialPipeline:
      stages:
      - targetId: qsdev
      - targetId: qsprod
    uid: f0b8148d5ddf4071964803e278acb1da
    updateTime: '2021-05-03T16:03:12.780948171Z'
    

As shown in this output, the command returns only one pipeline, with two targets.

## View delivery-pipeline details

For an existing delivery pipeline, you can view pipeline details, including pipeline metadata and the progression of targets.

###  Console 

  1. In the Google Cloud console, navigate to the Cloud Deploy **Delivery pipelines** page to view of list of your available delivery pipelines.

[Open the Delivery pipelines page](https://console.cloud.google.com/deploy/delivery-pipelines)

The list of delivery pipelines is shown in Google Cloud console.

![List of delivery
pipelines](https://docs.cloud.google.com/static/deploy/images/pipelines-page-1.png)

Delivery pipelines that have been configured but not [registered with the Cloud Deploy service](https://docs.cloud.google.com/deploy/docs/create-pipeline-targets#register_the_delivery_pipeline_and_targets) are not shown.

  2. Click the **Name** of the delivery pipeline whose details you want to view.




Google Cloud console shows a visualization of the delivery pipeline, as well as pipeline metadata and status:

![Delivery pipeline
details page, with visualization of the pipeline](https://docs.cloud.google.com/static/deploy/images/pipeline_details1.png)

You can click the **Targets** tab to see details of the targets that this delivery pipeline uses:

![Delivery pipeline
details page, with visualization of the pipeline](https://docs.cloud.google.com/static/deploy/images/target_details1.png)

###  gcloud 

The following command returns details of the specified delivery pipelines:
    
    
    gcloud deploy delivery-pipelines describe <pipeline-name> --region=<region>
    

You should see an output similar to the following:
    
    
    $ gcloud deploy delivery-pipelines describe my-demo-app-1 --region=us-central1
    Delivery Pipeline:
      createTime: '2021-05-03T16:03:11.687046682Z'
      description: main application pipeline
      etag: a9721c6cf665fcc7
      name: projects/try-cd-dev6/locations/us-central1/deliveryPipelines/my-demo-app-1
      serialPipeline:
        stages:
        - targetId: qsdev
        - targetId: qsprod
      uid: f0b8148d5ddf4071964803e278acb1da
      updateTime: '2021-05-03T16:03:12.780948171Z'
    Targets:
    - Target: qsdev
    - Target: qsprod
    

As shown in this output, the command returns the details for the one pipeline. Note the two `stages` and the two corresponding `Target`s.

You can also [view release details](https://docs.cloud.google.com/deploy/docs/view-release), including rollout details and rendering source. And you can diff rendered artifacts, including manifests and Skaffold config.

## What's next

  * Find out how to [update a delivery pipeline](https://docs.cloud.google.com/deploy/docs/update-pipeline) that's already in use.

  * Learn how to [suspend a delivery pipeline](https://docs.cloud.google.com/deploy/docs/suspend-pipeline).

  * Find out how to [delete a delivery pipeline](https://docs.cloud.google.com/deploy/docs/delete-pipeline).

  * Learn how to [use service notifications](https://docs.cloud.google.com/deploy/docs/subscribe-deploy-notifications)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
