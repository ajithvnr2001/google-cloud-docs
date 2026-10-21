---
url: https://docs.cloud.google.com/appengine/migration-center/standard/go/migrating-push-queues-upgrade-sdk/
title: Migrating push queues to Cloud Tasks (Go) \u00a0|\u00a0 App Engine migration center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:38.532193+00:00
---

# Migrating push queues to Cloud Tasks (Go)  |  App Engine migration center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/migration-center/standard/go/migrating-push-queues-upgrade-sdk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Migration center ](https://docs.cloud.google.com/appengine/migration-center)
  * [ Guides ](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services)



Send feedback 

#  Migrating push queues to Cloud Tasks (Go) Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Migrate Task Queue to Cloud Tasks by upgrading the App Engine services SDK version**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Before you upgrade to the latest App Engine services SDK version, review the [migration overview](https://docs.cloud.google.com/appengine/migration-center/standard/go/migrating-push-queues-overview).

You can migrate to Cloud Tasks automatically by updating your App Engine services SDK to the latest version. After you upgrade, the SDK automatically redirects `PushQueue` calls to the Cloud Tasks frontend APIs for you. Cloud Tasks retains your existing task queues and tasks, so no additional migration is required.

Behind the scenes, the updated SDK uses the Cloud Tasks APIs to maintain feature parity with Task Queues features, the SDK supports the following:

  * **Batch task creation** : The SDK uses batch APIs to support adding up to 100 tasks in a single call.
  * **Task-level retries** : The SDK supports task-specific retry configurations.
  * **Transactional tasks** : The SDK enqueues tasks within Datastore transactions. To maintain reliability, either create or modify the `cron.yaml` file.



## Pricing and quotas

Migrating your push queues to Cloud Tasks might affect the pricing and quotas for your app.

### Pricing

Review the [Cloud Tasks pricing](https://cloud.google.com/tasks/pricing) to estimate your monthly cost before migrating.

Similar to Task Queues, sending requests to your App Engine app with a Cloud Tasks push target is free. However, unlike Task Queues, Cloud Tasks charges for operation performed, such as creating, deleting, or managing tasks. This might lead to higher overall monthly cost compared to the complimentary App Engine Task Queue.

### Quotas

Cloud Tasks requests also count towards your App Engine requests quotas.

Like Task Queues, Cloud Tasks has service-specific [quotas](https://cloud.google.com/tasks/docs/quotas). Migrating to Cloud Tasks will likely change your quotas.

## Before you begin

The following sections discuss the cost and quota considerations before migrating push queues to Cloud Tasks.

  1. Make sure that you have access to the App Engine source code.

  2. Enable the Cloud Tasks and Cloud Scheduler APIs:

[Enable APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudtasks.googleapis.com,cloudscheduler.googleapis.com)

  3. To ensure that the App Engine service account has the necessary permissions to let the SDK dispatch tasks to the Cloud Tasks API, ask your administrator to grant the [Cloud Tasks Enqueuer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.enqueuer) (`roles/cloudtasks.enqueuer`) IAM role on project.




## Update the App Engine services SDK

  1. Ensure your application uses the latest version of the App Engine services SDK.

In your `go.mod` file, update the `google.golang.org/appengine/v2` module to version `v2.1.0-preview` or higher.
         
         module my-app
         
         go 1.27
         
         require (
             google.golang.org/appengineppengine/v2.1.0-preview
         )

  2. Enable Cloud Tasks routing
         
         runtime: 1.27
         service: my-service-b
         
         env_variables:
           APPENGINE_USE_CLOUDTASK_PUSH_QUEUE: "true"
         

  3. Deploy your app:
         
         gcloud app deploy
         

  4. [Verify push queues in Cloud Tasks](https://console.cloud.google.com/cloudtasks) to verify that you app is using Cloud Tasks.




### Configure transactional tasks (optional)

If your app enqueues tasks within Datastore transactions, the SDK relies on an internal cron job to ensure that any tasks that fail to enqueue during the datastore commit are eventually processed.

To handle push queue transactional tasks, create or update your `cron.yaml` file to periodically call the internal processor. For example:
    
    
    cron:
    - description: "Process push queue transactional tasks"
      url: /_ah/cloudtask/sweep
      schedule: every 30 minutes # Change this based on the usage pattern
    

## What's next

  * [Cloud Tasks documentation](https://docs.cloud.google.com/tasks/docs)
  * [Cloud Tasks client library](https://docs.cloud.google.com/tasks/docs/reference/libraries)
  * [Cloud Tasks REST reference](https://docs.cloud.google.com/tasks/docs/reference/rest) overview
  * [Cloud Tasks RPC reference](https://docs.cloud.google.com/tasks/docs/reference/rpc) overview 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
