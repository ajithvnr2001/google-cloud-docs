---
url: https://docs.cloud.google.com/code/docs/intellij/deploy-service/
title: Deploy a service to Cloud Run in Cloud Code for IntelliJ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:02:35.874706+00:00
---

# Deploy a service to Cloud Run in Cloud Code for IntelliJ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/intellij/deploy-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ IntelliJ Cloud Code ](https://docs.cloud.google.com/code/docs/intellij)
  * [ Guides ](https://docs.cloud.google.com/code/docs/intellij/quickstart)



Send feedback 

#  Deploy a service to Cloud Run in Cloud Code for IntelliJ Stay organized with collections  Save and categorize content based on your preferences. 

Now that you're all set up, you can deploy your service to Cloud Run and view your service live.

## Defining your run configuration

Before you deploy your service, you must create your run configuration:

  1. Navigate to Run/Debug configurations selector in the Navigation bar and click **Edit Configurations**.
  2. In the left pane, click **Cloud Run: Deploy**.
  3. Set your Google Cloud project ID.
  4. Choose your platform preferences under **Deployment Platform** , either **Cloud Run** or **Knative serving**. For a detailed description of each option, see the [Cloud Run platform guide](https://docs.cloud.google.com/run/docs/choosing-a-platform).

     * If **Cloud Run** is selected, choose a region to deploy to.
     * If **Knative serving** is selected, configure the Kubernetes cluster information.

![Deployment platform options: Fully Managed \(chosen\) and Anthos on GKE with a region specified](https://docs.cloud.google.com/static/code/docs/intellij/images/deploy-platform.png)

  5. If your service is a public API or website, choose **Allow unauthenticated invocations** in the Authentication section. Otherwise, select **Require authentication**.

  6. Under Revision Settings, Cloud Code automatically populates the container image URL field with the storage location of your container image (where it stores your service, once it builds and containerizes it). This value is based on your Google Cloud project and service name.

If you need to, you can override this value:

     * For both Cloud Run and Knative serving, you can store your images on either: 
       * [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs), using the format **REGION -docker.pkg.dev/PROJECT_ID/REPO_NAME/IMAGE_PATH**
         * REGION is the repository's supported region
         * PROJECT_ID is the ID of your Google Cloud project containing your cluster
         * REPO_NAME is the name of your repository where your image is stored
         * IMAGE_PATH is the path to your image
**Note:** Consider [transitioning from Container Registry](https://docs.cloud.google.com/artifact-registry/docs/transition/transition-from-gcr) since Artifact Registry is the recommended service for managing container images. [Container Registry](https://docs.cloud.google.com/container-registry/docs) is still supported but will only receive critical security fixes.
     * Container Registry, using the format **gcr.io/ PROJECT_ID/IMAGE_NAME**
       * PROJECT_ID is the ID of your Google Cloud project
       * IMAGE_NAME refers to the container image repository
     * If you're using Knative serving, you can store your images on Docker Hub using the format, **docker.io/ ACCOUNT**, where ACCOUNT is the name of your Docker Hub account. Make sure that you're [properly authenticated](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry) if you're using a private Docker Hub repository.

![Run/Debug configuration open with sample fields \(project ID and region\) filled in](https://docs.cloud.google.com/static/code/docs/intellij/images/deploy-config.png)

  7. Under Build settings, choose whether to build locally or on Cloud Build.

  8. Choose a builder and plugin.

Cloud Code supports Docker, Jib, and Buildpacks [artifact types](https://skaffold.dev/docs/builders/).

  9. Click **OK**.




### Optional: Customizing your configuration

When deploying your service, you can specify additional settings such as a service account, environment variables, and, when using Cloud Run, a VPC Connector and SQL connections. Specify the additional settings in the **Advanced revision settings** section when you choose **Edit Configurations**.

**Environment variables:**

The following environment variables are automatically added to the running containers:

Name  | Description  | Example   
---|---|---  
PORT  | The port your HTTP server should listen on.  | 8080   
K_SERVICE  | The name of the Cloud Run service being run.  | hello-world   
K_REVISION  | The name of the Cloud Run revision being run.  | hello-world.1   
K_CONFIGURATION  | The name of the Cloud Run configuration that created the revision.  | hello-world   
  
## Deploying your service

To deploy your service, follow these steps:

  1. Choose your run target from the Run/Debug configurations dialog on the top taskbar.
  2. Click ![run action icon](https://docs.cloud.google.com/static/code/docs/intellij/images/run-action-icon.png)**Run**.
  3. View your running service by following the URL displayed in the **output window**.
  4. You can also view the status of your service (metrics, revision details, and more) by following the logs URL displayed in the output window.

![Viewing the status of your service in the Console](https://docs.cloud.google.com/static/code/docs/intellij/images/cccr-view-logs.png)




## Get support

To submit feedback or report an issue in your IntelliJ IDE, go to **Tools** > **Cloud Code** > **Help / About** > **Submit feedback or report an issue** to report an issue on [GitHub](https://github.com/GoogleCloudPlatform/cloud-code-intellij/issues). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
