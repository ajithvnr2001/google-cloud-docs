---
url: https://docs.cloud.google.com/code/docs/vscode/image-build-settings/
title: Explore your build options with buildpacks, Jib, or Docker \u00a0|\u00a0 Cloud Code for VS Code \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:27.030485+00:00
---

# Explore your build options with buildpacks, Jib, or Docker  |  Cloud Code for VS Code  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/vscode/image-build-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for VS Code ](https://docs.cloud.google.com/code/docs/vscode)
  * [ Guides ](https://docs.cloud.google.com/code/docs/vscode/quickstart)



Send feedback 

#  Explore your build options with buildpacks, Jib, or Docker Stay organized with collections  Save and categorize content based on your preferences. 

To run or debug an application on Kubernetes, you'll need to set your preference for how your container image is built by configuring it in the **Develop on Kubernetes** run configuration.

In a project that doesn't contain a `skaffold.yaml` file at the root or doesn't reference `skaffold.yaml` you can use the Cloud Code UI to choose a builder and build environment.

Building locally is free of charge since it uses your own resources. Building with [Cloud Build](https://docs.cloud.google.com/build) is good for slower machines or machines that don't match the processor architecture of the target cluster. For information about the cost of building your application using Cloud Build, see [Cloud Build Pricing](https://cloud.google.com/build/pricing).

## Specify how your images are built

Cloud Code supports [Docker](https://skaffold.dev/docs/pipeline-stages/builders/docker/), [Jib](https://skaffold.dev/docs/pipeline-stages/builders/jib/), and [Buildpacks](https://skaffold.dev/docs/pipeline-stages/builders/buildpacks/) [artifact types](https://skaffold.dev/docs/builders/).

### Without a skaffold.yaml

When importing an existing application without a `skaffold.yaml` file or running an application that doesn't have a `skaffold.yaml`, you're prompted to specify settings when initializing.

If you're using one of the Cloud Code sample applications, to use the UI, delete the `skaffold.yaml` file before running a build action. For steps to choose a builder and build environment without the UI, see [Manually creating a `skaffold.yaml` configuration](https://docs.cloud.google.com/code/docs/vscode/use-existing-kubernetes-app#manually_create_a_skaffold_configuration).

  1. In a project without a `skaffold.yaml` file, open the command palette (press `Ctrl`/`Cmd`+`Shift`+`P` or click **View** > **Command Palette**) and then run **Cloud Code: Run on Kubernetes** or **Cloud Code: Debug on Kubernetes**.
  2. In the **Build environment** section, choose a build environment.
  3. In the **Deploy settings** section, if you chose Cloud Build, specify the image registry you want Cloud Build to push images to.
  4. In the **Build settings** section, specify a builder (Docker, Jib, or buildpacks) for each image and its settings.
  5. Select or clear any of the configuration options and then click **Debug** or **Run**.



The options you choose are saved to a [`skaffold.yaml`](https://skaffold.dev/docs/references/yaml) file that you can edit directly for further customization.

### With an existing skaffold.yaml

For a project with an existing `skaffold.yaml` file, you need to manually edit your build options. Cloud Code provides snippets for common YAML schema viewable by pressing `Command/Ctrl + Space`. See the [Skaffold Build documentation](https://skaffold.dev/docs/builders/) for more details. 

## Use Skaffold profiles in Cloud Code

Cloud Code uses the Skaffold tool under the hood to power Cloud Code's build functionality. To configure Cloud Code for different build or deploy environments such as local or remote builds, [Skaffold profiles](https://skaffold.dev/docs/environment/profiles/) are used 

## Create a new skaffold profile

If you'd like to define build, test and deployment configurations for different contexts, you can have different Skaffold profiles.

The following sample shows a profile named `cloudbuild` used to to build images with Cloud Build: 
    
    
    profiles:
    # use the cloudbuild profile to build images using Google Cloud Build
    - name: cloudbuild
       build:
       googleCloudBuild: {}
    

If you have multiple profiles, add the profile you want to use to your `launch.json` file. For more information on Skaffold profiles, see the [Skaffold profiles documentation](https://skaffold.dev/docs/environment/profiles/)

## What's next

  * Use [file sync and hot reloading](https://docs.cloud.google.com/code/docs/vscode/speed-up-k8s-development#enable-skaffold-file-sync-and-hot-reloading) to speed up development.
  * Learn more about [Cloud Native Buildpacks](https://buildpacks.io/).
  * Read about the benefits of [Cloud Build](https://docs.cloud.google.com/build).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
