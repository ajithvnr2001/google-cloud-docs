---
url: https://docs.cloud.google.com/code/docs/vscode/use-existing-kubernetes-app/
title: Use an existing application in Cloud Code for VS Code \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:23.118612+00:00
---

# Use an existing application in Cloud Code for VS Code  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/vscode/use-existing-kubernetes-app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for VS Code ](https://docs.cloud.google.com/code/docs/vscode)
  * [ Guides ](https://docs.cloud.google.com/code/docs/vscode/quickstart)



Send feedback 

#  Use an existing application in Cloud Code for VS Code Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Code leverages [Skaffold](https://skaffold.dev/) under the hood to run or debug your application.

If you have an existing application already configured with Kubernetes manifests and a Dockerfile to build your images, you can open and use it with Cloud Code.

The only additional configuration necessary is a [`skaffold.yaml` file](https://skaffold.dev/docs/references/yaml/) and a [launch configuration](https://code.visualstudio.com/docs/editor/debugging#_launch-configurations) of type `cloudcode.kubernetes`. Cloud Code guides you through creating these when you run or debug your application for the first time.

## Setting up configuration

**Note:** Automatic `skaffold.yaml` generation doesn't support projects without a Dockerfile. For these projects, create a skaffold.yaml file manually.

If your application has a Dockerfile but doesn't have the necessary `skaffold.yaml` and launch configurations, complete the following steps:

  1. In the Cloud Code status bar, click the active project name.

![Active project name in status bar](https://docs.cloud.google.com/static/code/docs/vscode/images/cloudcode-status-bar.png)

  2. In the Quick Pick menu that appears, select **Run on Kubernetes** or **Debug on Kubernetes**.

  3. In the Run/Debug on Kubernetes dialog, specify your preferred builder and its settings. You can also customize your configuration name.

  4. Click **Debug** or **Run**. 

  5. If prompted, [authenticate your credentials to run and debug an application locally](https://docs.cloud.google.com/code/docs/vscode/install#authenticate_credentials_for_debugging_applications_locally).

The newly created `skaffold.yaml` and `cloudcode.kubernetes` launch configuration are added to your workspace and your app [runs](https://docs.cloud.google.com/code/docs/vscode/run-application) or is ready for [debugging](https://docs.cloud.google.com/code/docs/vscode/debug).




## Setting up configuration for applications that already have skaffold.yaml

If your application already has a `skaffold.yaml` file, follow these steps:

  1. In the Cloud Code status bar, click the active project name.

![Active project name in status bar](https://docs.cloud.google.com/static/code/docs/vscode/images/cloudcode-status-bar.png)

  2. In the Quick Pick menu that appears, select **Run on Kubernetes** or **Debug on Kubernetes**.

  3. If more than one `skaffold.yaml` file exists in your workspace, select your preferred skaffold.yaml file.

  4. If more than one [Skaffold profile](https://skaffold.dev/docs/environment/profiles/) exists in the `skaffold.yaml` file you chose, select your preferred Skaffold profile.

The newly created `cloudcode.kubernetes` launch configuration is added to your workspace (in .vscode/launch.json) and your app is [running](https://docs.cloud.google.com/code/docs/vscode/run-application) or ready for [debugging](https://docs.cloud.google.com/code/docs/vscode/debug).




## Manually creating a `skaffold.yaml` configuration

You might want to manually create your `skaffold.yaml` configuration to define custom options. Cloud Code comes with live templating to support manual `skaffold.yaml` configuration creation.

To manually create a `skaffold.yaml` configuration:

  1. Create a new file named `skaffold.yaml` in the root directory of your workspace.

  2. In the file, press `Command/Ctrl+Space` to see a list of snippet suggestions and then select the **Skaffold - Getting-started** snippet.

![Create Skaffold configuration manually intellisense](https://docs.cloud.google.com/static/code/docs/vscode/images/skaffold-config-manual-generation.png)

  3. Enter your project image name in the `image` field and enter a list of the Kubernetes resources to deploy in the `manifests` field.

Example for Dockerfile based builds:
         
         build:
           artifacts:
             - image: image_name
         deploy:
           kubectl:
             manifests:
               - k8s/web.yaml
               - k8s/backend.yaml
         

If you'd like to define build, test and deployment configurations for different contexts, you can have different Skaffold profiles. The following sample shows a Cloud Build profile to configure Cloud Code to build images with Cloud Build:
         
         profiles:
         # use the cloudbuild profile to build images using Google Cloud Build
         - name: cloudbuild
           build:
             googleCloudBuild: {}
         

For comprehensive schema details, see [the skaffold.yaml reference](https://skaffold.dev/docs/references/yaml).




## What's next

  * Use [file sync and hot reloading](https://docs.cloud.google.com/code/docs/vscode/speed-up-k8s-development#enable-skaffold-file-sync-and-hot-reloading) to speed up development.
  * [Debug your application in Cloud Code](https://docs.cloud.google.com/code/docs/vscode/debug).



## Get Support

To send feedback, ask a question on [Stack Overflow](https://stackoverflow.com/questions/ask?tags=cloud-code-vscode). If you are a Google Cloud customer, you can file tickets through [standard Google Cloud support channels](https://cloud.google.com/support?e=48754805). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
