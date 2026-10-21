---
url: https://docs.cloud.google.com/compute/docs/instances/viewing-compute-operations/
title: View Compute Engine operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:39:02.613818+00:00
---

# View Compute Engine operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/viewing-compute-operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  View Compute Engine operations Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

When you call a Compute Engine API that mutates a resource, Compute Engine adds an entry to the list of operations. For example, when you make an update to a VM that mutates (alters) data, or when a [host event](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview) occurs that changes the state of a VM, operations are created. This page describes how you can view a list of Compute Engine operations by using the [Google Cloud console](https://console.cloud.google.com/), the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute), or [REST](https://docs.cloud.google.com/compute/docs/reference/rest/v1).

Remember that operations can take some time to complete, so you may find incomplete operations while viewing. When you want to see the final status of incomplete operations, repeatedly viewing operations is not recommended; instead, you should [wait for operations to be done](https://docs.cloud.google.com/compute/docs/api/best-practices#wait-for-operations).

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Operation Retention Period

While querying operations, keep in mind that completed operations are automatically removed from the database after a certain period.

Compute Engine retains completed operations for at least the minimum retention period of 1 hour, and up to the maximum retention period of 14 days. Although projects often observe a retention period for completed operations that is longer than the minimum of 1 hour, depending on the additional retention period is not recommended.

Note that the retention periods don't apply to operations deleted by the users through `Operations.delete` method.

## Viewing operations

To view a list of operations for your project, perform the following steps:

###  Console 

  1. In the Google Cloud console, go to the **Operations** page.

[Go to Operations](https://console.cloud.google.com/compute/operations)

  2. For more details on an operation, click the operation summary. For example, to view the migration details for the `my-instance` VM, click the **Automatically migrate an instance** operation.




![The operations page showing a live migration.](https://docs.cloud.google.com/static/compute/images/operations_console.png)![Live migration details.](https://docs.cloud.google.com/static/compute/images/migration_operation_console.png)

###  gcloud 

To view a list of operations for your project using `gcloud compute`, use the [`operations list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/operations/list) sub-command.

To view the list of operations in a specified zone, add the `--filter` flag.
    
    
    gcloud compute operations list --filter="zone:(ZONE)"

Replace `ZONE` with the zone where you want to view a list of operations. For example, to view the list of operations in `us-cental1-c`, run the following command:
    
    
    gcloud compute operations list --filter="zone:(us-central1-c)"
    

The output is similar to the following: 
    
    
    NAME                            TYPE                                        TARGET                                HTTP_STATUS  STATUS  TIMESTAMP
    systemevent-1543845145000...    compute.instances.migrateOnHostMaintenance  us-central1-c/instances/my-instance   200          DONE    2018-12-03T05:52:25.000-08:00
    

###  REST 

API requests for operations must be specified at either the [global](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalOperations/list), [region](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionOperations/list), or [zone](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zoneOperations/list) level. Live migration, VM stopping, and automatic restarts are all zone-level operations.

For zone operations, make a `GET` request to the [`zoneOperations.list`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zoneOperations/list) method.
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/operations

Replace the following:

  * `PROJECT_ID`: the project ID for this request
  * `ZONE`: the zone for this request



Leave the request body empty.

The following is a sample output for a zone operation request. In this output, details for a host migration displays.
    
    
    {
     "kind": "compute#operation",
     "id": "3216798767364213712",
     "name": "systemevent-1543845145000-57c1e7574b840-a195b637-5ff74d9b",
     "zone": "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-c",
     "operationType": "compute.instances.migrateOnHostMaintenance",
     "targetLink": "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-c/instances/my-instance",
     "targetId": "3070988523247098025",
     "status": "DONE",
     "statusMessage": "Instance migrated during Compute Engine maintenance.",
     "user": "system",
     "progress": 100,
     "insertTime": "2018-12-03T05:52:25.000-08:00",
     "startTime": "2018-12-03T05:52:25.000-08:00",
     "endTime": "2018-12-03T05:52:25.000-08:00",
     "selfLink": "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-c/operations/systemevent-1543845145000-57c1e7574b840-a195b637-5ff74d9b"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v9ce9cb5b22b62a465ff52c45061a0a6a2d86a80b685e9aa8a182b203fdfbf420/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


