---
url: https://docs.cloud.google.com/deploy/docs/run-targets/
title: Deploy a Cloud Run service, job, or worker pool \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:44.507889+00:00
---

# Deploy a Cloud Run service, job, or worker pool  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/run-targets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Deploy a Cloud Run service, job, or worker pool Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to deploy your applications, including Cloud Run services, Cloud Run jobs, and Cloud Run worker pools.

Cloud Deploy lets you to deploy your container-based workloads to any [Cloud Run service](https://docs.cloud.google.com/run/docs/deploying), [job](https://docs.cloud.google.com/run/docs/create-jobs), or [worker pool](https://docs.cloud.google.com/run/docs/deploy-worker-pools). All Cloud Deploy features are supported when you deploy to Cloud Run targets for Cloud Run services or worker pools, but canary deployments aren't supported for Cloud Run jobs.

This document describes the three main configurations you need to complete in order to deploy to Cloud Run:

  * Create your target configuration
  * Create your Skaffold configuration
  * Create your Cloud Run service definitions, job definitions, or worker pool definitions



## Limitations

  * You can only deploy one Cloud Run service, job, or worker pool per target.

  * You can't run a [canary deployment](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/cloud-run) against a Cloud Run job.

Cloud Run services and worker pools, however, can use a canary deployment.

  * To deploy a [Cloud Run function](https://docs.cloud.google.com/functions/docs/concepts/overview) using Cloud Deploy, you need to modify your CI workflow to build the function into a container and deploy it as a Cloud Run service.




## Before you begin

  * Make sure you're using [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/components/update) version `541.0.0` or greater.

  * [Have a Cloud Deploy delivery pipeline](https://docs.cloud.google.com/deploy/docs/create-pipeline-targets).




## Create your [target configuration](https://docs.cloud.google.com/deploy/docs/config-files#for_run_targets)

The target can be configured in your delivery pipeline YAML, or can be in a separate file. Also, you can configure more than one target in the same file.

Targets must be defined in the same project and region as the delivery pipeline. But the services, jobs, or worker pools the targets deploy to can be in different projects and regions, as long as the service account has access to those projects.

In the target definition, create a `run` stanza to identify the location where the Cloud Run service will be created.

The syntax for specifying the Cloud Run service, job, or worker pool in your target definition is as follows:
    
    
    run:
     location: projects/[project_name]/locations/[region_name]
    

This resource identifier uses the following elements:

  * `project_name` is the name of the Google Cloud project in which your Cloud Run service, job, or worker pool will be created.

You'll do this for each target. We recommend a different project for each Cloud Run service, job, or worker pool. If you want more than one service, job, or worker pool in the same project, you need to use [Skaffold profiles](https://cloud.google.com/deploy/docs/using-skaffold/managing-manifests) in your `skaffold.yaml` configuration file.

  * `region_name` is the region in which the service, job, or worker pool will be created. Your service, job, or worker pool can be in any [region that Cloud Run supports](https://cloud.google.com/about/locations).




The following is an example target configuration, defining the Cloud Run service, job, or worker pool to create:
    
    
          apiVersion: deploy.cloud.google.com/v1
          kind: Target
          metadata:
           name: dev
          description: development service
          run:
           location: projects/my-app/locations/us-central1
    

You can define this target inside a Cloud Deploy delivery pipeline definition, or separately. Either way, you must [register the target](https://docs.cloud.google.com/deploy/docs/create-pipeline-targets#register_the_delivery_pipeline_and_targets) before you create the release to deploy your Cloud Run service, job, or worker pool.

## Create your Skaffold configuration

The following is an _example_ `skaffold.yaml` file for a [Cloud Run deployment](https://skaffold-v2.web.app/docs/pipeline-stages/deployers/cloudrun/):
    
    
    apiVersion: skaffold/v4beta7
    kind: Config
    metadata: 
      name: cloud-run-application
    manifests:
      rawYaml:
      - service.yaml
    deploy:
      cloudrun: {}
    

In this `skaffold.yaml` file...

  * `manifests.rawYaml` provides the names of the Cloud Run service definitions.

In this example, `service.yaml` is the file that defines a Cloud Run service that Skaffold will deploy. This filename can be anything, but by convention it's `service.yaml` for a service, `job.yaml` for a job, and `workerpool.yaml` for a worker pool.

  * The `deploy` stanza specifies how you want the manifest to be deployed, specifically, the project and location. `deploy` is required.

We recommend you leave the empty `{}`. Cloud Deploy populates this during rendering, based on the project and location from the target definition.

For local development, however, you can provide values here. However, Cloud Deploy always use the project and location from the target definition, regardless of whether values are provided here.




## Create your Cloud Run service definitions

To create a Cloud Run service definition, you can either create one manually, or copy one from an existing service. Both are described in this section.

### Option 1: Create a new Cloud Run `service.yaml`

The [service.yaml](https://docs.cloud.google.com/run/docs/reference/yaml/v1) defines your Cloud Run service. When you create a release, Skaffold uses this definition to deploy your service.

Here's a simplified example:
    
    
    apiVersion: serving.knative.dev/v1
    kind: Service
    metadata:
     name: [SERVICE_NAME]
    spec:
     template:
      spec:
       containers:
       - image: [IMAGE_PATH]
    

Where:

  * `[SERVICE_NAME]` is a name for this Cloud Run service.

  * `[IMAGE_PATH]` points to the container image or images you're deploying with this service.




### Option 2: Copy a `service.yaml` from an existing service using Google Cloud console

You can create a service using Google Cloud console or use an existing one, and copy your `service.yaml` from there.

To get the `service.yaml` using Google Cloud CLI:
    
    
    gcloud run services describe [service_name] --format=export
    

To get the `service.yaml` from Google Cloud console:

  1. In Google Cloud console, go to the Cloud Run Services page.

  2. Select the existing service whose definition you want to use.




Or you can [create a new one](https://docs.cloud.google.com/run/docs/deploying#service), then select it. When you select the service, the Service details page is shown:

![service details page
Google Cloud console, showing the YAML tab](https://docs.cloud.google.com/static/deploy/images/service-details.png)

  1. Select the **YAML** tab.

  2. Click **Edit** , then copy the contents of the YAML into a new file called `service.yaml`, in your file system, such that Skaffold can use it when you [create a release](https://docs.cloud.google.com/deploy/docs/deploying-application#invoke_your_delivery_pipeline_to_create_a_release).




## Create your Cloud Run job definitions

To deploy a Cloud Run job definition, you can either create one manually, or copy one from an existing job. Both are described in this section.

Note that jobs aren't necessarily run upon being deployed by Cloud Deploy. This is different from services, which are running applications after they're deployed. How a job is invoked depends on the job itself.

### Option 1: Create a new Cloud Run `job.yaml`

The [job.yaml](https://docs.cloud.google.com/run/docs/reference/yaml/v1#job) defines your Cloud Run job. When you create a release, Skaffold uses this definition to deploy the job.

Here's a simplified example:
    
    
    apiVersion: run.googleapis.com/v1
    kind: Job
    metadata:
     name: [JOB_NAME]
    spec:
      template:
      spec:
       containers:
       - image: [IMAGE_PATH]
    

Where:

  * `[JOB_NAME]` is a name for this Cloud Run job.

  * `[IMAGE_PATH]` points to the container image you're deploying for this job.




### Option 2: Copy a `job.yaml` from an existing job using Google Cloud console

You can create a job using Google Cloud console or use an existing one, and copy your `job.yaml` from there.

To get the `job.yaml` using Google Cloud CLI:
    
    
    gcloud run jobs describe [job_name] --format=export
    

To get the `job.yaml` from Google Cloud console:

  1. In Google Cloud console, go to the Cloud Run Jobs page.

  2. Select the existing job whose definition you want to use.




Or you can [create a new one](https://docs.cloud.google.com/run/docs/create-jobs#job), then select it. When you select the job, the Job details page is shown:

![job details page
Google Cloud console, showing the YAML tab](https://docs.cloud.google.com/static/deploy/images/job-details.png)

  1. Select the **YAML** tab.

  2. Click **Edit** , then copy the contents of the YAML into a new file called `job.yaml`, in your file system, such that Skaffold can use it when you [create a release](https://docs.cloud.google.com/deploy/docs/deploying-application#invoke_your_delivery_pipeline_to_create_a_release).




## Create your Cloud Run worker pool definitions

To deploy a Cloud Run worker pool definition, you can either create one manually, or copy one from an existing worker pool. Both are described in this section.

### Option 1: Create a new Cloud Run `workerpool.yaml`

The [workerpool.yaml](https://docs.cloud.google.com/run/docs/reference/yaml/v1) defines your Cloud Run worker pool. When you create a release, Skaffold uses this definition to deploy the worker pool.

Here's a simplified example:
    
    
    apiVersion: run.googleapis.com/v1
    kind: WorkerPool
    metadata:
     name: [WORKERPOOL_NAME]
     annotations:
      run.googleapis.com/launch-stage: BETA
    spec:
      template:
       spec:
        containers:
        - image: [IMAGE_PATH]
    

Where:

  * `[WORKERPOOL_NAME]` is a name for this Cloud Run worker pool.

  * `[IMAGE_PATH]` points to the container image you're deploying for this worker pool.




### Option 2: Copy a `workerpool.yaml` from an existing worker pool using Google Cloud console

You can create a worker pool using Google Cloud console or use an existing one, and copy your `workerpool.yaml` from there.

To get the `workerpool.yaml` using Google Cloud CLI:
    
    
    gcloud beta run worker-pools describe [workerpool_name] --format=export
    

To get the `workerpool.yaml` from Google Cloud console:

  1. In Google Cloud console, go to the Cloud Run Worker pools page.

  2. Select the existing worker pool whose definition you want to use.




Or you can [create a new one](https://docs.cloud.google.com/run/docs/deploy-worker-pools#worker-pool), then select it. When you select the worker pool, the Worker pool details page is shown:

![worker pool details page
Google Cloud console, showing the YAML tab](https://docs.cloud.google.com/static/deploy/images/workerpool-details.png)

  1. Select the **YAML** tab.

  2. Copy the contents of the YAML into a new file called `workerpool.yaml`, in your file system, such that Skaffold can use it when you [create a release](https://docs.cloud.google.com/deploy/docs/deploying-application#invoke_your_delivery_pipeline_to_create_a_release).




## Putting it all together

Now that you have your Cloud Run service, job, or worker pool definition, your `skaffold.yaml` configuration, and your Cloud Deploy target definition, and you've [registered your target](https://docs.cloud.google.com/deploy/docs/create-pipeline-targets#register_the_delivery_pipeline_and_targets) as a Cloud Deploy resource, you can now [invoke your delivery pipeline](https://cloud.google.com/deploy/docs/deploying-application#invoke_your_delivery_pipeline_to_create_a_release) to create a release and progress it through the progression of targets defined in the pipeline.

The quickstart [Deploy an app to Cloud Run using Cloud Deploy](https://docs.cloud.google.com/deploy/docs/deploy-app-run) shows all of this in action.

## Behavior of services across revisions

When you re-deploy a service, the new revision is based on the newly deployed `service.yaml`. Nothing about the previous revision is maintained, unless it's the same in the newly deployed YAML. For example, if there are configuration settings or labels in the previous revision that are not in the new YAML, those settings or labels are absent from the new revision.

## Triggering Cloud Run jobs

After you deploy a job, you can trigger it as described [in the Cloud Run documentation](https://cloud.google.com/run/docs/execute/jobs#execute_jobs).

## Deploying Cloud Run services, jobs, and worker pools in multiple projects

If you need to deploy services, jobs, or worker pools that are in different projects, your [execution service account](https://docs.cloud.google.com/deploy/docs/cloud-deploy-service-account) needs permission to access the projects in which those services, jobs, or worker pools are defined.

See [Cloud Deploy execution service account](https://docs.cloud.google.com/deploy/docs/cloud-deploy-service-account#execution_service_account) and [Identity and Access Management roles and permissions](https://docs.cloud.google.com/deploy/docs/iam-roles-permissions) for more information.

## Deploying Cloud Run functions

Cloud Run functions builds your source code every time a function is deployed. Because of this, each target runtime in your pipeline might get a slightly different artifact. This is contrary to best practices in Cloud Deploy. Instead, we suggest you use a Cloud Run service directly. This lets you build a single artifact and promote it across your environments.

  1. Check in the `service.yaml` for your Cloud Run function.

You can get this by running the following command:
         
         gcloud run services describe FUNCTION_NAME \
         --format=export \
         --region=REGION \
         --project=PROJECT
         

  2. Remove the following annotations, if present:

     * `run.googleapis.com/build-base-image`
     * `run.googleapis.com/build-name`
     * `run.googleapis.com/build-source-location`
     * `run.googleapis.com/build-enable-automatic-updates`
  3. Replace the value in `spec.spec.containers.image` with `IMAGE_TAG`.

  4. Create your [delivery pipeline and targets](https://docs.cloud.google.com/deploy/docs/create-pipeline-targets), with the Cloud Run service as a target.

  5. Separate the build step from the deploy step in your CI process. Instead of using the Google Cloud CLI to deploy your function, replace it with the following steps:

     1. [Build the function](https://docs.cloud.google.com/run/docs/building/functions#build_with_command) into a container using Cloud Build:
            
            gcloud builds submit --pack image=REGION-docker.pkg.dev/PROJECT/cloud-run-source-deploy/IMAGE_NAME \
            --project=PROJECT \
            --region=REGION
            

     2. [Create a release](https://docs.cloud.google.com/deploy/docs/deploy-app-run#create_a_release) using Cloud Deploy:
            
            gcloud deploy releases create RELEASE_NAME \
            --project=DEPLOY_PROJECT \
            --region=REGION \
            --delivery-pipeline=DELIVERY_PIPELINE \
            --images=IMAGE_TAG=REGION-docker.pkg.dev/PROJECT/cloud-run-source-deploy/IMAGE_NAME
            

In this command...

        * `RELEASE_NAME` is a name to give to this release. The name must be unique among all releases for this delivery pipeline.

        * `DEPLOY_PROJECT` is the project ID of the project where you created the deploy pipeline.

        * `DELIVERY_PIPELINE` is the name of the delivery pipeline that will manage deployment of this release through the progression of targets. This name must match the [`name` field in the pipeline definition](https://docs.cloud.google.com/deploy/docs/config-files#name).

        * `REGION` is the name of the region in which you're creating the release, for example `us-central1`. This is required.

        * `IMAGE_NAME` is the name you gave the image in the previous step, when you built the function.




## What's next

  * Try the [quickstart: deploy an application to Cloud Run](https://docs.cloud.google.com/deploy/docs/deploy-app-run)

  * Learn more about [configuring Cloud Deploy targets](https://docs.cloud.google.com/deploy/docs/config-files#target_definitions)

  * Learn about Cloud Deploy [execution environments](https://docs.cloud.google.com/deploy/docs/execution-environment).

  * Learn more about [Skaffold support for Cloud Run](https://skaffold-v2.web.app/docs/pipeline-stages/deployers/cloudrun/)

  * Learn more about [Cloud Run](https://docs.cloud.google.com/run/docs)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
