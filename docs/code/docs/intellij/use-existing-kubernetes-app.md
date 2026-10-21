---
url: https://docs.cloud.google.com/code/docs/intellij/use-existing-kubernetes-app/
title: Use an existing application in Cloud Code for IntelliJ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:21:35.037672+00:00
---

# Use an existing application in Cloud Code for IntelliJ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/intellij/use-existing-kubernetes-app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ IntelliJ Cloud Code ](https://docs.cloud.google.com/code/docs/intellij)
  * [ Guides ](https://docs.cloud.google.com/code/docs/intellij/quickstart)



Send feedback 

#  Use an existing application in Cloud Code for IntelliJ Stay organized with collections  Save and categorize content based on your preferences. 

If you have an existing project already configured with Kubernetes manifests, a Dockerfile, or [Jib](https://github.com/GoogleContainerTools/jib) to build your images, you can open and use it with the plugin. The only additional configuration necessary is a [`skaffold.yaml` file](https://skaffold.dev/) which either can be generated for you automatically or created using the provided template.

After you're done with configuring your `skaffold.yaml` file, be sure to [specify where your container images are stored](https://docs.cloud.google.com/code/docs/intellij/use-k8s-existing-app#specifying_where_container_images_are_stored) where the project image is about to be pushed.

## Automatic project bootstrapping

Your project must have one or more Kubernetes manifests. If Cloud Code detects _any_ Kubernetes manifests in the project, Cloud Code will try to bootstrap.

If Cloud Code doesn't detect an existing `skaffold.yaml` configuration, you will be prompted to help set it up.

### Prerequisites

Your project must meet the following prerequisites in order to be prompted to create a `skaffold.yaml` file and run any necessary configurations:

  * (Option 1) Your project has a Dockerfile and is configured for [Jib](https://github.com/GoogleContainerTools/jib), or

  * (Option 2) Your project is buildable using Buildpacks and has Kubernetes resources.




### Set up Kubernetes run configuration

If the prerequisites are met, Cloud Code will prompt you with a notification to create a `skaffold.yaml` file (if one doesn't already exist) and any necessary run configurations:

![Notification with a link to create your Cloud Code Kubernetes run configurations](https://docs.cloud.google.com/static/code/docs/intellij/images/run-config-notification.png)

  1. Click the notification. This automatically creates your configuration if possible.

If automatic `skaffold.yaml` configuration is not possible due to multiple images or builders being detected, Cloud Code will display a dialog asking you to provide mappings between the detected images and builders.

![Specify build settings to be used in your `skaffold.yaml` file](https://docs.cloud.google.com/static/code/docs/intellij/images/initialize-skaffold.png)

Alternatively, you can also set up a `skaffold.yaml` file by navigating to **Tools** > **Cloud Code** > **Kubernetes** and selecting **Add Kubernetes Support**.

This option analyzes your project's Kubernetes resources and generates a `skaffold.yaml` file (if one doesn't already exist) as well as necessary run configurations. The two run configurations generated include one to run your project on Kubernetes and one for development on a Kubernetes cluster.

  2. After support is added, you can start running and debugging your project on Kubernetes using the newly added run configurations.




## Manually create a Cloud Code `skaffold.yaml` configuration

You can choose to manually create a new `skaffold.yaml` file or add an existing one to your project.

To create a `skaffold.yaml` file manually using live templating, follow these steps:

  1. Create a new file named `skaffold.yaml` in the root directory of your project (right-click > **New** > **File**).

  2. With the cursor in the new file, press `Ctrl+Space` to bring up the live template suggestions and then choose a `skaffold.yaml` template.

![Using the `skaffold.yaml` template](https://docs.cloud.google.com/static/code/docs/intellij/images/skaffold-yaml-template.png)

  3. Populate the image field with your project image name and the manifests field with a list of the Kubernetes resources you want to deploy from the IDE.

  4. After Cloud Code determines that your `skaffold.yaml` file is valid, click the prompt to create Kubernetes run configurations.

![Create Kubernetes run target notification](https://docs.cloud.google.com/static/code/docs/intellij/images/create-k8-targets.png)




### Examples of Cloud Code `skaffold.yaml` configurations

  * Dockerfile based builds:
        
        build:
          artifacts:
            - image: image_name
        deploy:
          kubectl:
            manifests:
              - k8s/web.yaml
              - k8s/backend.yaml
        

  * Build section for Java Maven/Gradle projects with the Jib plugin (deploy section stays the same as the example above):
        
        build:
        artifacts:
        - image: image_name
          jib: {}
        

  * If you'd like to define build, test, and deployment configurations for different contexts, you can have different profiles. Here's an example of a Cloud Build profile to configure Cloud Code to build images with Cloud Build:
        
        profiles:
        # use the cloudbuild profile to build images using Google Cloud Build
        - name: cloudbuild
          build:
            googleCloudBuild: {}
        

  * If you'd like to deploy your project with Helm, see the [Helm documentation](https://skaffold.dev/docs/pipeline-stages/deployers/helm/).




## Specifying where container images are stored

### Container image storage

Before you deploy your application, you'll need to define a default image repository to use with your project.

By default, the project is configured to use the image name specified in your Kubernetes manifests. You can also customize this image specification. Once you have your preferred repository set up ([Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs), [DockerHub](https://hub.docker.com/), or a private repository), edit the run configurations and specify it as a default image repository in run configuration settings.

These are accessible from the Run/Debug configurations dialog on the top taskbar under **Edit Configurations** > **Develop on Kubernetes** > **Image repository**.

![Default image repository in run configuration being set with the 'gcr.io/' format and being presented autocomplete options based on current project and active cluster](https://docs.cloud.google.com/static/code/docs/intellij/images/cloud-code-run-config-image-repo.png)

For more on specifying your container image preferences, refer to the [Configuring container image settings guide](https://docs.cloud.google.com/code/docs/intellij/configuring-container-image-settings).

### Build settings

Once you set your container image, you can configure its build settings. Cloud Code supports Docker, Jib, and Buildpacks artifact types.

On the **Build / Deploy** tab of your Run configuration settings (**Edit Configurations** > **Develop on Kubernetes**), you can configure the build settings for your default profile.

![Build settings displayed in Build/Deploy tab](https://docs.cloud.google.com/static/code/docs/intellij/images/existing-skaffold.png)

For more on specifying the build settings for your image, refer to the [Configuring container image build preferences guide](https://docs.cloud.google.com/code/docs/intellij/image-build-settings).

## What's next

  * Use [file sync and hot reloading](https://docs.cloud.google.com/code/docs/intellij/speed-up-k8s-development#enable-skaffold-file-sync-and-hot-reloading) to speed up development.
  * [Debug your application in Cloud Code](https://docs.cloud.google.com/code/docs/intellij/debug).



## Get support

To submit feedback or report an issue in your IntelliJ IDE, go to **Tools** > **Cloud Code** > **Help / About** > **Submit feedback or report an issue** to report an issue on [GitHub](https://github.com/GoogleCloudPlatform/cloud-code-intellij/issues). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
