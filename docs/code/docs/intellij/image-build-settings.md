---
url: https://docs.cloud.google.com/code/docs/intellij/image-build-settings/
title: Explore your build options with buildpacks, Jib, or Docker \u00a0|\u00a0 Cloud Code for IntelliJ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:21:35.121464+00:00
---

# Explore your build options with buildpacks, Jib, or Docker  |  Cloud Code for IntelliJ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/intellij/image-build-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ IntelliJ Cloud Code ](https://docs.cloud.google.com/code/docs/intellij)
  * [ Guides ](https://docs.cloud.google.com/code/docs/intellij/quickstart)



Send feedback 

#  Explore your build options with buildpacks, Jib, or Docker Stay organized with collections  Save and categorize content based on your preferences. 

To run or debug an application on Kubernetes, you'll need to set your preference for how your container image is built by configuring it in the **Develop on Kubernetes** run configuration.

In a project that doesn't contain a `skaffold.yaml` file at the root or doesn't reference `skaffold.yaml` you can use the Cloud Code UI to choose a builder and build environment.

Building locally is free of charge since it uses your own resources. Building with [Cloud Build](https://docs.cloud.google.com/build) is good for slower machines or machines that don't match the processor architecture of the target cluster. For information about the cost of building your application using Cloud Build, see [Cloud Build Pricing](https://cloud.google.com/build/pricing).

## Specify how your images are built

Cloud Code supports [Docker](https://skaffold.dev/docs/pipeline-stages/builders/docker/), [Jib](https://skaffold.dev/docs/pipeline-stages/builders/jib/), and [Buildpacks](https://skaffold.dev/docs/pipeline-stages/builders/buildpacks/) [artifact types](https://skaffold.dev/docs/builders/).

To set or edit build options, navigate to the Run/Debug configuration selector in the Navigation bar or the top-level main menu: **Run** > **Edit Configurations** > **Develop on Kubernetes** and then click the **Build/Deploy** tab. 

### Without a skaffold.yaml

When importing an existing application without a `skaffold.yaml` file or running an application that doesn't have a `skaffold.yaml`, you're prompted to specify settings when initializing.

If you're using one of the Cloud Code sample applications, to use the UI, delete the `skaffold.yaml` file before running a build action. For steps to choose a builder and build environment without the UI, see [Manually creating a `skaffold.yaml` configuration](https://docs.cloud.google.com/code/docs/intellij/use-existing-kubernetes-app#manually_create_a_skaffold_configuration).

To edit the builder for an image, follow these steps: 

  1. Navigate to the Run/Debug configuration selector in the Navigation bar or the top-level main menu: **Run** > **Edit Configurations** > **Develop on Kubernetes** and click the **Build/Deploy** tab.
  2. Click **Initialize**.
  3. In the **Initialize Kubernetes project with Cloud Code** dialog under **Build settings** , select the image you want to build, and then click the **Edit** icon or press **Enter**.
  4. Select the builder that you want to use and then click **Okay**.

The builder and settings you specify are stored in your [`skaffold.yaml`](https://skaffold.dev/docs/references/yaml) configuration as your default build preference.

  5. To return to your Run Configuration dialog with your new settings, click **Initialize**.




### With an existing skaffold.yaml

On the **Build/Deploy** tab of your Run configuration settings, you can configure the build settings for your default profile.

You can also view the image name, builder, and builder arguments for all your existing images. 

## Use Skaffold profiles in Cloud Code

Cloud Code uses the Skaffold tool under the hood to power the functionality in the **Build/Deploy** tab. To configure Cloud Code for different build or deploy environments such as local or remote builds, [Skaffold profiles](https://skaffold.dev/docs/environment/profiles/) are used. 

## Create a new skaffold profile

If you'd like to define build, test and deployment configurations for different contexts, you can have different Skaffold profiles.

1\. To create a new profile, navigate to **Run** > **Edit Configurations** > **Develop on Kubernetes** and choose the **Build/Deploy** tab. 

  1. In the **Deployment profile** box, click **\+ Add Skaffold profile**.

  2. In the Create a new profile dialog, enter a profile name, select the build environment, and then click **OK**.

After you've created the new profile, it will be automatically selected in the **Deployment profile** combo box in the run configuration panel.




You can also add profiles by editing your `skaffold.yaml` file manually. The following sample shows a profile named `cloudbuild` used to to build images with Cloud Build:
    
    
    profiles:
    # use the cloudbuild profile to build images using Google Cloud Build
    - name: cloudbuild
       build:
       googleCloudBuild: {}
    

For more information on Skaffold profiles, see the [Skaffold profiles documentation](https://skaffold.dev/docs/environment/profiles/)

## Filter profiles by build environment

Using the **Build environment filter** input in the **Cloud Code: Kubernetes** run configuration panel, you can filter your Skaffold profiles based on the build environment you're interested in.

  1. Navigate to the Run/Debug configuration selector in the Navigation bar or the top-level main menu: **Run** > **Edit Configurations** > **Develop on Kubernetes** and click the **Build/Deploy** tab.

By default, **Any** build environment will be selected. This filter shows all Skaffold profiles in the selected Skaffold profile.

  2. In the **Build environment filter** drop-down menu, select the build environment you want to see.

Profiles matching your build environment selection are available in the **Deployment profile** drop down. If you select a build environment that has no available profiles, you may be prompted to create a profile.




## What's next

  * Use [file sync and hot reloading](https://docs.cloud.google.com/code/docs/intellij/speed-up-k8s-development#enable-skaffold-file-sync-and-hot-reloading) to speed up development.
  * Learn more about [Cloud Native Buildpacks](https://buildpacks.io/).
  * Read about the benefits of [Cloud Build](https://docs.cloud.google.com/build).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
