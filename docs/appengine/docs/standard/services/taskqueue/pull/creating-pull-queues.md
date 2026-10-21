---
url: https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/pull/creating-pull-queues/
title: Creating Pull Queues \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:47:57.990402+00:00
---

# Creating Pull Queues  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/pull/creating-pull-queues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Creating Pull Queues Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

This page describes how to create a pull queue. You must create the queue before you can add tasks to it. The page also describes how to pause or delete a queue.

## Defining queues with `queue.yaml`

You can define pull queues using the `queue.yaml` file for your application. The process is the same as [creating named push queues](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/creating-push-queues), with a specialized directive, [`mode: pull`](https://docs.cloud.google.com/appengine/docs/standard/reference/queueref#mode), added to the file.
    
    
    queue:
    - name: my-queue-name
      mode: pull
    

You use the gcloud CLI `gcloud` command to upload the file.
    
    
    gcloud app deploy queue.yaml
    

**Note:** If you are using a service account to manage authentication for deploying your queue configuration file, it needs to have the `serviceusage.services.list` permission. This permission can be added either using the [`serviceusage.serviceUsageViewer`](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage) role or by creating a [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) with that permission.**Caution:** Queue creation for the Task Queue service can also be managed using Queue Management methods available directly through the Cloud Tasks API, but mixing the ``queue.yaml`` upload method with Queue Management methods can produce unexpected results and is not recommended. For more information, see [Overview of Queue Management and queue.yaml](https://docs.cloud.google.com/tasks/docs/queue-yaml). Also note that uploading a `queue.yaml` file via the gcloud CLI below version `332.0.0` uses a deprecated interface to the service. Starting on `2022-09-20`, attempts to use the upload method can fail with server errors. To resolve this, make sure the Cloud Tasks API is enabled in your project and your gcloud CLI is updated to at least version `332.0.0`.

## Disabling queues

You can disable, or pause, a queue by removing its definition from your queue configuration file and then uploading the updated file.

Once the updated file is uploaded, the queue is set to "disabled" and its rate is set to 0. Any tasks that are in the queue or new tasks that are added to the queue will not be processed. You can re-enable the disabled queue by uploading a new queue file with the queue defined.

You can also pause a queue from within the [Cloud Tasks page in the Google Cloud console](https://console.cloud.google.com/cloudtasks).

## Deleting queues

To delete a queue you must first disable it:

  1. Remove the queue definition from your queue configuration file.

  2. Upload the changed file.
         
         gcloud app deploy queue.yaml
         




Once the queue is disabled, use the Google Cloud console to delete it.

  1. In the Google Cloud console, select the queue.

[Go to Cloud Tasks](https://console.cloud.google.com/cloudtasks)

  2. Click **Delete queue**.




If you delete a queue from the Google Cloud console, you must wait 7 days before recreating with the same name.

**Important:** The local development server (`dev_appserver`) does not support pull queues. To test your pull queues and make sure you have the details of your configuration correct, you'll need to push your queue configuration file to an App Engine staging environment.

## What's next

Learn how to [create tasks](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/pull/creating-tasks).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
