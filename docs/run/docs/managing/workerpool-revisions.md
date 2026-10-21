---
url: https://docs.cloud.google.com/run/docs/managing/workerpool-revisions/
title: Manage worker pool revisions \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:54.979326+00:00
---

# Manage worker pool revisions  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/managing/workerpool-revisions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Manage worker pool revisions Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Run worker pool revisions let you track configuration history and roll back to previous deployment states. Each deployment or configuration update to a worker pool creates an immutable revision.

Inactive revisions don't consume resources or incur costs, so you don't need to manually delete revisions. Each worker pool retains up to 1000 revisions and automatically deletes older ones when you exceed that limit.

## Required roles

To get the permissions that you need to manage Cloud Run worker pools and worker pool revisions, ask your administrator to grant you the [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) IAM role on your Cloud Run worker pool. 

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run worker pool interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/workerpools/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## View the list of revisions for a worker pool

Each revision name includes an automatically assigned suffix, unless you specify a custom suffix when deploying with the Google Cloud CLI [`--revision-suffix`](https://docs.cloud.google.com/sdk/gcloud/reference/run/worker-pools/deploy#--revision-suffix) flag.

### console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run/worker-pools)

  2. Select **Worker pools** from the menu to display the list of worker pools.




###  gcloud 

To view the list of revisions for a given worker pool:

  1. Find your worker pool name from the list of worker pools available in your project:
         
         gcloud run worker-pools list

  2. Use the following command to get all the revisions for that worker pool:
         
         gcloud run worker-pools revisions list
            --worker-pool=WORKER_POOL
            --region=REGION

Replace:

     * WORKER_POOL with the name of your worker pool.
     * REGION with the Google Cloud region of the worker pool.



## View revision details

### console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run/worker-pools)

  2. Select **Worker pools** from the menu to display the available worker pools.

  3. Click the worker pool to display its details pane.




###  gcloud 

To view the details for a revision in your project:

  1. Find your worker pool name from the list of worker pools available in your project:
         
         gcloud run worker-pools list

  2. Use the following command to get all the revisions for the worker pool you just looked up: 
         
         gcloud run worker-pools revisions list
             --worker-pool=WORKER_POOL
             --region=REGION

Replace

     * WORKER_POOL with the name of your worker pool.
     * REGION with the Google Cloud region of the worker pool.
  3. Use the following command to see more details about a specific revision: 
         
         gcloud run worker-pools revisions describe REVISION --region=REGION --worker-pool=WORKER_POOL

Replace

     * REVISION with the name of the revision you want to learn more about.
     * REGION with the Google Cloud region of the worker pool.
     * WORKER_POOL with the name of the worker pool.

You can use the [`--format` flag](https://docs.cloud.google.com/sdk/gcloud/reference#--format) to format the output. For example, to format the output as YAML: 
    
    gcloud run worker-pools revisions describe REVISION
        --region=REGION
        --worker-pool=WORKER_POOL
        --format yaml




Note that a non-current revision may have the status of `RETIRED`, which means that Cloud Run has retired the infrastructure needed for that particular revision.

## Delete revisions

A common use case for deleting a revision is when you want to make sure a particular revision won't be accidentally used.

You cannot delete a revision if it is:

  * The only revision of the worker pool.
  * The latest revision of the worker pool.



When you delete a revision, the container image used by this revision is not deleted automatically from Artifact Registry. To delete a container image from Artifact Registry, see the deletion instructions for [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images#deleting_images).

You cannot undo a revision deletion.

Use the Google Cloud console or the Google Cloud CLI to delete a revision:

### console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run/worker-pools)

  2. Select **Worker pools** from the menu to display the available worker pools.

  3. Click the worker pool to display its details pane.

  4. Click **Revisions**.

  5. Select the revision to delete.

  6. Click the ellipsis under **Actions** , then click **Delete** to delete the revision.




###  gcloud 

To delete a revision, use the following command:
    
    
    gcloud run worker-pools revisions delete REVISION
        --region=REGION
        --worker-pool=WORKER_POOL

Replace

  * REVISION with the name of the revision you are deleting.
  * WORKER_POOL with the name of your worker pool.
  * REGION with the Google Cloud region of the worker pool.



## What's next

After you deploy a revision, you can do the following:

  * [Gradual rollouts, rollback revisions, instance splits](https://docs.cloud.google.com/run/docs/workerpools/rollouts-rollbacks-splits)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
