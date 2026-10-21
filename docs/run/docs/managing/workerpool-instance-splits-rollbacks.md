---
url: https://docs.cloud.google.com/run/docs/managing/workerpool-instance-splits-rollbacks/
title: Instance splits and rollbacks for Cloud Run worker pools \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:45.962107+00:00
---

# Instance splits and rollbacks for Cloud Run worker pools  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/managing/workerpool-instance-splits-rollbacks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Instance splits and rollbacks for Cloud Run worker pools Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Run worker pools let you divide non-request workloads across multiple revisions by using instance splitting. You can assign specific instance percentages to each revision, roll back to a previous revision, or shift all instances to the latest revision when deploying updates.

## Lifecycle of instance splits

If you split instances between multiple revisions or assign instances to a previous revision, all subsequent deployments use that instance split pattern going forward. To return to just using the latest revision without instance splitting, send all instances to the latest revision.

Instance allocation adjustments aren't instantaneous. When you change instance allocation for revisions, in-process tasks continue to completion, and Cloud Run transitions workloads between the previous and new revisions according to the updated split.

### Required roles

To get the permissions that you need to manage Cloud Run worker pools and worker pool revisions, ask your administrator to grant you the [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) IAM role on your Cloud Run worker pool. 

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run worker pool interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/workerpools/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Roll back to a previous revision

To roll back to a previous revision, use the Google Cloud console, or the Google Cloud CLI:

### Console

  1. In the Google Cloud console, go to Cloud Run worker pools:

[Go to Cloud Run](https://console.cloud.google.com/run/worker-pools)

  2. Locate the worker pool in the list, and click it.

  3. Click the **Revisions** tab to show the list of current revisions for that worker pool.

  4. Click **Manage instance splits** to display the manage instances form. Cloud Run lists the latest serving revision. In the form, configure the following details:

     1. **Add revision** and use the drop-down list to select a previous revision.
     2. Set that previous revision's instance percentage to 100.
     3. Set the latest serving revision's percentage to 0.
     4. Click **Save**.



###  gcloud 

Specify the revisions to rollback to by running the following command.
    
    
       gcloud run worker-pools update-instance-split WORKER_POOL --to-revisions=REVISION=100
    

Replace the following:

  * WORKER_POOL: the name of the worker pool.
  * REVISION: the name of the revision you are rolling back to.



### YAML

  1. If you are creating a new worker pool, skip this step. If you are updating an existing worker pool, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run worker-pools describe WORKER_POOL --format export > worker-pool.yaml

  2. The following example contains the YAML configuration:
         
         apiVersion: run.googleapis.com/v1
         kind: WorkerPool
         metadata:
           name: WORKER_POOL
           labels:
             cloud.googleapis.com/location: REGION
         spec:
           template:
             spec:
               containers:
               - image: IMAGE_URL
           instanceSplits:
           - revisionName: REVISION
             percent: 100
         

Replace the following:

     * WORKER_POOL: the name of the worker pool.
     * REGION: the Google Cloud region—for example, `us-central1`.
     * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`
     * REVISION: the name of the revision you are rolling back to.
  3. Create or update the worker pool using the following command:
         
         gcloud run worker-pools replace worker-pool.yaml

The `gcloud run worker-pools replace` command defaults to using `worker-pool.yaml` file if present.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).
    
    
    import {
      id = "projects/PROJECT_ID/locations/REGION/workerPools/WORKER_POOL"
      to = google_cloud_run_v2_worker_pool.default
    }
    
    resource "google_cloud_run_v2_worker_pool" "default" {
      name     = "WORKER_POOL"
      location = "REGION"
    
      template {
        containers {
          image = "IMAGE_URL"
        }
      }
    
      instance_splits {
        type     = "INSTANCE_SPLIT_ALLOCATION_TYPE_REVISION"
        revision = "REVISION"
        percent  = 100
      }
    }
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the Google Cloud region—for example, `us-central1`.
  * WORKER_POOL: the name of the worker pool.
  * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`
  * REVISION: the name of the revision you are rolling back to.



## Split instances between multiple revisions

To split instances between two or more revisions, use the Google Cloud console, or the Google Cloud CLI:

When you split instances between multiple revisions, make sure that the total percentage across all revisions equals 100%, and the number of [manual instances](https://docs.cloud.google.com/run/docs/configuring/workerpools/manual-scaling) must be greater than the number of instance splits serving the workload.

### Console

  1. In the Google Cloud console, go to Cloud Run worker pools:

[Go to Cloud Run](https://console.cloud.google.com/run/worker-pools)

  2. Locate the worker pool in the list, and click it.

  3. Click the **Revisions** tab to show the list of current revisions for that worker pool.

  4. Click **Manage instance splits** to display the manage instances form. Cloud Run lists the latest serving revision. In the form, configure the following details:

     1. Set the latest serving revision's percentage to the required split, for example, reduce it from 100%.

     2. Click **Add revision** and use the drop-down list to select a previous revision and set its corresponding percentage split.

     3. To split instances with additional revisions, click **Add Revision** , and select another revision, and set its percentage.

     4. Click **Save**.




###  gcloud 

Specify the revisions and the percentage of instances by running the following command. [Allocate instances for each revision](https://docs.cloud.google.com/sdk/gcloud/reference/run/worker-pools/update-instance-split#--to-revisions) in a comma delimited list:
    
    
       gcloud run worker-pools update-instance-split WORKER_POOL --to-revisions=LIST
    

Replace the following:

  * WORKER_POOL: the name of the worker pool.

  * LIST: comma delimited list of revisions and percentages:

REVISION1=PERCENTAGE1,REVISION2=PERCENTAGE2,REVISIONn=PERCENTAGEx.

For example, `my-worker-pool-s5sxn=10,my-worker-pool-cp9kw=90`.




### YAML

  1. If you are creating a new worker pool, skip this step. If you are updating an existing worker pool, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run worker-pools describe WORKER_POOL --format export > worker-pool.yaml

  2. The following example contains the YAML configuration:
         
         apiVersion: run.googleapis.com/v1
         kind: WorkerPool
         metadata:
           name: WORKER_POOL
           labels:
             cloud.googleapis.com/location: REGION
           annotations:
             run.googleapis.com/scalingMode: manual
         spec:
           template:
             spec:
               containers:
               - image: IMAGE_URL
           instanceSplits:
           - revisionName: REVISION1
             percent: PERCENTAGE1
           - revisionName: REVISION2
             percent: PERCENTAGE2
         

Replace the following:

     * WORKER_POOL: the name of the worker pool.
     * REGION: the Google Cloud region—for example, `us-central1`.
     * INSTANCE_COUNT: the number of instances.
     * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`
     * REVISION1 and REVISION2: the name of the revisions.
     * PERCENTAGE1 and PERCENTAGE2: the percentage of instances to allocate to each of these revisions. These need to add up to 100.
  3. Create or update the worker pool using the following command:
         
         gcloud run worker-pools replace worker-pool.yaml

The `gcloud run worker-pools replace` command defaults to using `worker-pool.yaml` file if present.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).
    
    
    import {
      id = "projects/PROJECT_ID/locations/REGION/workerPools/WORKER_POOL"
      to = google_cloud_run_v2_worker_pool.default
    }
    
    resource "google_cloud_run_v2_worker_pool" "default" {
      name     = "WORKER_POOL"
      location = "REGION"
    
      template {
        containers {
          image = "IMAGE_URL"
        }
      }
    
      instance_splits {
        type     = "INSTANCE_SPLIT_ALLOCATION_TYPE_REVISION"
        revision = "REVISION1"
        percent  = PERCENTAGE1
      }
      instance_splits {
        type     = "INSTANCE_SPLIT_ALLOCATION_TYPE_REVISION"
        revision = "REVISION2"
        percent  = PERCENTAGE2
      }
    }
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the Google Cloud region—for example, `us-central1`.
  * WORKER_POOL: the name of the worker pool.
  * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`
  * REVISION1 and REVISION2: the name of the revisions.
  * PERCENTAGE1 and PERCENTAGE2: the percentage of instances to allocate to each of these revisions. These need to add up to 100.



## Allocate instances to the latest revision

When you deploy a new revision, you can allocate 100% of instances to this revision and all future ones, overriding any established instance split.

###  gcloud 

To allocate 100% of the instances to the [latest revision](https://docs.cloud.google.com/sdk/gcloud/reference/run/worker-pools/update-instance-split#--to-latest), run the following commands:

  * Use the `--to-latest` flag to direct 100% of instances to the latest revision and automatically allocate all instances to any new revision you deploy:
        
        gcloud run worker-pools update-instance-split WORKER_POOL --to-latest
        

  * Optionally, use the `--to-revisions` flag with the `LATEST` keyword to always allocate a floating percentage of instances to the newest revision when you deploy one. To set a percentage of instances that always float to the latest revision, run the following command:
        
        gcloud run worker-pools update-instance-split WORKER_POOL --to-revisions=LATEST=PERCENTAGE
        

Replace the following:

    * WORKER_POOL: the name of the worker pool.
    * PERCENTAGE: the percentage of instances to allocate for the latest and future latest revisions.



### YAML

  1. If you are creating a new worker pool, skip this step. If you are updating an existing worker pool, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run worker-pools describe WORKER_POOL --format export > worker-pool.yaml

  2. The following example contains the YAML configuration:
         
         apiVersion: run.googleapis.com/v1
         kind: WorkerPool
         metadata:
           name: WORKER_POOL
           labels:
             cloud.googleapis.com/location: REGION
         spec:
           template:
             spec:
               containers:
               - image: IMAGE_URL
           instanceSplits:
           - latestRevision: true
             percent: 100
         

Replace the following:

     * WORKER_POOL: the name of the worker pool.
     * REGION: the Google Cloud region—for example, `us-central1`.
     * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`
  3. Create or update the worker pool using the following command:
         
         gcloud run worker-pools replace worker-pool.yaml

The `gcloud run worker-pools replace` command defaults to using `worker-pool.yaml` file if present.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).
    
    
    resource "google_cloud_run_v2_worker_pool" "default" {
      name     = "WORKER_POOL"
      location = "REGION"
    
      template {
        containers {
          image = "IMAGE_URL"
        }
      }
    
      instance_splits {
        type = "INSTANCE_SPLIT_ALLOCATION_TYPE_LATEST"
        percent  = 100
      }
    }
    

Replace the following:

  * WORKER_POOL: the name of the worker pool.
  * REGION: the Google Cloud region—for example, `us-central1`.
  * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`



## What's next

  * Learn about [using Cloud Deploy to set up a continuous-delivery pipeline to deploy to Cloud Run](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-cloud-run).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
