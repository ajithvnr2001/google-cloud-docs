---
url: https://docs.cloud.google.com/functions/1stgendocs/building/
title: Build process overview \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:34.236454+00:00
---

# Build process overview  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/building/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Build process overview

When you deploy your function's source code to Cloud Run functions, that source is stored in a Cloud Storage bucket. Cloud Build then automatically builds your code into a container image and pushes that image to an image registry. Cloud Run functions accesses this image when it needs to run the container to execute your function.

**Caution:** Container Registry is deprecated. Effective March 18, 2025, Container Registry is shut down, and writing images to Container Registry is unavailable. For details on the deprecation and how to migrate to Artifact Registry, see [Container Registry deprecation](https://docs.cloud.google.com/container-registry/docs/deprecations/container-registry-deprecation).

The process of building the image is entirely automatic and requires no direct input from you. All the resources used in the build process execute in your own user project.

Executing the build process within your project means that:

  * You have direct access to all build logs.

  * There is no preset build-time quota, although Cloud Build does have its own [default concurrency quota](https://docs.cloud.google.com/build/quotas).

  * You can view the current container image and the previously deployed container images, both of which are stored in Artifact Registry.

  * Cloud Storage is used in your project to store the source code directory for your functions. Note the following:

    * If you create a function, an upload bucket is created to hold your source code. This upload bucket is named `gcf-uploads-PROJECT_NUMBER-REGION.cloudfunctions.appspot.com`.
    * After the code is uploaded, function code is stored in a separate source bucket: 
      * If you're using default encryption, this bucket is named `gcf-sources-PROJECT_NUMBER-REGION`.
      * If you're [protecting your data with CMEK](https://docs.cloud.google.com/functions/1stgendocs/securing/cmek), the bucket is named `gcf-sources-PROJECT_NUMBER-REGION-CMEK_KEY_HASH`.
    * Both source and upload buckets have no retention period.

**Note:** If you accidentally delete a Cloud Run function, you can restore it using the source files from the `gcf-sources` bucket by downloading the zip file and redeploying it. Note that the `gcf-sources bucket` retains only the last two versions of the source code. When cleaning up, deleting the function and disabling the Cloud Run functions API won't automatically delete the `gcf-sources` bucket. To fully remove all Cloud Run functions-related resources, you must manually delete the `gcf-sources` bucket.

### Characteristics of the build process

The build process has the following characteristics:

  * The [Cloud Build API](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com) must be enabled for your project.

To enable the API manually, click the above link, select your project from the dropdown menu, and follow the prompts to enable the UI.

  * Because the entire build process takes place within the context of your project, the project is subject to the pricing of the included resources:

    * For Cloud Build pricing, see the [Pricing](https://cloud.google.com/build/pricing) page. This process uses the default instance size of Cloud Build, as these instances are pre-warmed and are available more quickly. Cloud Build does provide a free tier: review the pricing document for further details.

    * For Cloud Storage pricing, see the [Pricing](https://cloud.google.com/storage/pricing) page. Cloud Storage does provide a free tier: review the pricing document for further details.

    * For Artifact Registry pricing, see the [Pricing](https://cloud.google.com/artifact-registry/pricing) page.

    * For Container Registry ([deprecated](https://docs.cloud.google.com/container-registry/docs/deprecations/container-registry-deprecation)) pricing, see the [Pricing](https://cloud.google.com/container-registry/pricing) page.

  * Because the build process is subject to billing, your project must have a [Cloud Billing Account](https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account) attached to it.


**Note:** If you are using [gcp.resourceLocations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#constraints-supported-by-multiple-google-cloud-services) in your organization policy constraints, you should include the appropriate multi-region location. For example, if you are deploying in any of the `us` regions, you should include `us-locations`. This allows Cloud Build to access the Artifact Registry storage bucket.

### View your build image logs

A key benefit of having the build image process in your user project is access to build logs. You can use either the gcloud CLI or the Google Cloud console to reach the logs, which are available through [Cloud Logging](https://docs.cloud.google.com/logging/docs).

###  gcloud 

  1. Deploy your function using the `gcloud functions deploy` [command](https://docs.cloud.google.com/functions/1stgendocs/deploy#basics).

  2. The URL of the logs is shown as part of the response in your terminal window. For example:
         
         Deploying function (may take a while - up to 2 minutes)...⠹
         **For Cloud Build Stackdriver Logs**, visit:
         https://console.cloud.google.com/logs/viewer?project=&advancedFilter=resource.type%
         3Dbuild%0Aresource.labels.build_id%3D38d5b662-2315-45dd-8aa2-
         380d50d4f5e8%0AlogName%3Dprojects%2F%
         2Flogs%2Fcloudbuild
         Deploying function (may take a while - up to 2 minutes)...done.




###  Google Cloud console 

  1. From the [Cloud Run functions Overview](https://console.cloud.google.com/functions/list) window, click the name of the function you're investigating.
  2. Click the **Details** tab.
  3. In the **General Information** pane, click the **Container build log** link to open the **Logs explorer** pane.
  4. Click any row to view the details of that build log entry. If it's an error entry associated with a file, these details include the name, line and column of the file.



## Image registry

**Important:** As of February 18, 2025, Cloud Run functions (1st gen) deployments will transition to using Artifact Registry, regardless of the previous selection. This is to navigate [Container Registry shutdown](https://docs.cloud.google.com/artifact-registry/docs/transition/prepare-gcr-shutdown) without impacting 1st gen functions still pointing to Container Registry.

Cloud Run functions uses Artifact Registry to store the images built from your function source code. Images are stored in a repository named `REGION-docker.pkg.dev/PROJECT_ID/gcf-artifacts`.

Your Artifact Registry must be in the same project as your function. You can create or update an Artifact Registry-based function as follows:

###  gcloud 

For **Customer managed Artifact Registry** , run the following command:
    
    
    gcloud functions deploy --no-gen2 FUNCTION \
    --docker-repository=REPOSITORY
    [FLAGS...]

Replace the following:

  * FUNCTION: The name of the function.
  * REPOSITORY: The fully qualified Artifact Registry repository name, in the following format: `projects/PROJECT_NAME/locations/LOCATION/repositories/REPOSITORY`.



For **Google-managed Artifact Registry** , use:
    
    
    gcloud functions deploy --no-gen2 FUNCTION \
    --docker-registry=artifact-registry
    [FLAGS...]

###  Google Cloud console 

  1. Go to the Cloud Run functions page in the Google Cloud console:   
[Go to the Cloud Run functions page](https://console.cloud.google.com/functions)

  2. Click the name of the function for which you want to use Artifact Registry.

  3. Click **Edit**.

  4. Click **Runtime, build...** to expand the advanced configuration options.

  5. Click **Security and Image Repo** from the menu bar to open the security tab.

  6. Under **Image repository** , select one of the following, depending on which type of Artifact Registry you are using:

     * **Customer managed Artifact Registry**. Use this option if you set up your own Docker repository.
     * **Google managed Artifact Registry**. Use this option if you want to use a Google-managed Docker repository instead of setting up your own.
  7. For **Customer managed Artifact Registry** , use the **Artifact registry** drop-down to select the Artifact Registry repository you want, or follow the prompts and create a new one.

  8. Click **Next**.

  9. Click **Deploy**.




For detailed pricing information, see [Cloud Run functions Pricing](https://cloud.google.com/functions/pricing).

## Secure your build with private pools

To allow your functions to use dependencies (for example, npm packages), Cloud Build has by default unlimited internet access during the build process. If you have set up a VPC Service Controls (VPC SC) perimeter and wish to limit the build's access only to dependencies stored inside the perimeter, you can use the [Cloud Build private worker pools](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview) feature.

In general, follow these steps to set up your private pool:

  1. Create your private worker pool. See [Creating and managing private pools](https://docs.cloud.google.com/build/docs/private-pools/create-manage-private-pools).
  2. Configure your VPC Service Controls perimeter. See [Using VPC Service Controls](https://docs.cloud.google.com/build/docs/private-pools/using-vpc-service-controls).

  3. If your private worker pool is in a different project than your function, you need to grant the Cloud Run functions [Service Agent](https://docs.cloud.google.com/iam/docs/service-agents) Service Account (`service-FUNCTION_PROJECT_NUMBER@gcf-admin-robot.iam.gserviceaccount.com`) the `cloudbuild.workerPoolUser` role so that the Cloud Build service can access the worker pool.
         
         gcloud projects add-iam-policy-binding PRIVATE_POOL_PROJECT_ID \
             --member serviceAccount:service-FUNCTION_PROJECT_NUMBER@gcf-admin-robot.iam.gserviceaccount.com
             --role roles/cloudbuild.workerPoolUser

where FUNCTION_PROJECT_NUMBER is the _number_ of the project where the function runs and PRIVATE_POOL_PROJECT_ID is the _id_ of the project in which the worker pool is located. See [Running builds in a private pool](https://docs.cloud.google.com/build/docs/private-pools/run-builds-in-private-pool#permissions) for more information.

  4. Deploy your function to build using a private pool:




###  gcloud 
    
    
    gcloud functions deploy FUNCTION_NAME --no-gen2\
      --runtime RUNTIME \
      --build-worker-pool PRIVATE_POOL_NAME
      [FLAGS...]

where FUNCTION_NAME is the name of the function, RUNTIME is the runtime you are using, and PRIVATE_POOL_NAME is the name of your pool.

To **stop** using a given private pool and instead use the default Cloud Build pool, use the `--clear-build-worker-pool` flag when re-deploying.
    
    
    gcloud functions deploy FUNCTION_NAME --no-gen2 \
      --runtime RUNTIME \
      --clear-build-worker-pool
      [FLAGS...]

where FUNCTION_NAME is the name of the function and RUNTIME is the runtime you are using.

###  Google Cloud console 

  1. From the [Cloud Run functions overview](https://console.cloud.google.com/functions/list) page, select **Create function**.

  2. In the **Runtime, build...** section, click the **Build** tab and enter the full resource name of your private pool in the **Build worker pools** text box.




For more information, see [Run builds in a private pool](https://docs.cloud.google.com/build/docs/private-pools/run-builds-in-private-pool#running_builds).

## Secure your build with a custom service account

Cloud Run functions takes your source code and sends it to Cloud Build to be containerized. The containerized function is stored in Artifact Registry and deployed to Cloud Run as a service. By default, Cloud Build assigns a service account to act as the principal when performing your build. As of July 2024, new projects in an organization will use the Compute Engine default Service Account to act as the principal running a build. For details, see [Cloud Build default service account change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates). For security reasons, the Compute Engine default Service Account has insufficient permissions to perform the build.

For Google Cloud projects created before July 2024, Cloud Build uses the legacy Cloud Build service account. This service account was designed to help users execute a broad range of use cases that may be too permissive for your project's needs. If you want to move your existing projects away from this service account, you can take the following steps to further secure your functions build environment:

  1. Prevent the legacy Cloud Build service account from being used for the build.
  2. Prevent the default Compute service account from being used for the build.
  3. Configure a new service account with appropriately scoped permissions to be used for the build.
  4. Use the configured service account for the build.



### Prevent the legacy Cloud Build service account from being used for build

**Warning:** This will temporarily break all deployments until you assign a new service account.

You can verify that your project is using the legacy Cloud Build service account by inspecting the details of your function's build. The default build service account has the following format:

`PROJECT_NUMBER@cloudbuild.gserviceaccount.com`.

You can forcibly disable use of this service account by setting the org policy constraint `cloudbuild.useBuildServiceAccount` to `Not Enforced`. Alternatively, removing all of its role grants will limit its ability to access Google Cloud resources.

### Prevent the default compute service account from being used for build

**Warning:** This will temporarily break all deployments until you assign a new service account.

The default compute service account has the format `PROJECT_NUMBER-compute@developer.gserviceaccount.com`. You can disable it from being the default used for the build by setting the org policy `cloudbuild.useComputeServiceAccount` to `Not Enforced`. Alternatively, disabling this service account prevents it from being used to access Google Cloud resources.

### Provide a service account for building functions

As part of a function's configuration, a build service account can be specified when deploying the function. When the legacy Cloud Build service account and the default compute service account are prevented from being used for build, you must specify a build service account in order to deploy a function.

See [Custom Service Account for Cloud Build](https://docs.cloud.google.com/functions/1stgendocs/securing/build-custom-sa#configure_service_account) for configuring and using a build service account for your function.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
