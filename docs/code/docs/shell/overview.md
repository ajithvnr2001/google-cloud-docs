---
url: https://docs.cloud.google.com/code/docs/shell/overview/
title: Cloud Code overview \u00a0|\u00a0 Cloud Code for Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:16:46.104959+00:00
---

# Cloud Code overview  |  Cloud Code for Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/shell/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for Cloud Shell ](https://docs.cloud.google.com/code/docs/shell)
  * [ Guides ](https://docs.cloud.google.com/code/docs/shell/quickstart)



Send feedback 

#  Cloud Code overview Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Code is an extension that brings many Google Cloud services, like Google Kubernetes Engine and Cloud Run, directly into your IDE, so you can develop your applications without having to context switch. You can also code with assistance from [Gemini](https://docs.cloud.google.com/gemini/docs/overview), an AI-powered collaborator, to help you solve problems with your code, generate code for your project, and receive inline suggestions while you code.

You have support for the full development cycle of GKE and Cloud Run applications, from creating an app using an existing template to monitoring your deployed app's resources. Cloud Code also comes with run-ready samples and out-of-the-box configuration snippets to get you started quickly.

Cloud Code works with Google's command-line container tools like [minikube](https://minikube.sigs.k8s.io/docs/) and [kubectl](https://kubernetes.io/docs/tasks/tools/), providing local, continuous feedback on your project as you build, edit, run, and deploy your applications locally or in the cloud. Cloud Code also integrates with [Google Cloud SDK](https://docs.cloud.google.com/sdk) to provide a unified authentication experience when you develop with Google Cloud services.

While Cloud Code works with any cloud platform, it provides a streamlined Google Cloud experience. For example, you can create clusters hosted on Google Cloud, and have better integration with tools like Cloud Source Repositories, Cloud Build, and Cloud Client Libraries.

In short, Cloud Code is a powerful tool that can speed up your workflow when developing cloud-native applications. It provides a streamlined experience for the entire development cycle, from creating and deploying applications to debugging and monitoring them.

## Supported IDEs

You can install the Cloud Code extension in the following IDEs:

  * [VS Code](https://docs.cloud.google.com/code/docs/vscode/install).
  * [IntelliJ](https://docs.cloud.google.com/code/docs/intellij/install) and other [supported JetBrains IDEs](https://docs.cloud.google.com/code/docs/intellij/ides). Cloud Code for IntelliJ also provides limited support for [Android Studio](https://developer.android.com/studio).



Cloud Code is available by default in the [Cloud Shell Editor](https://docs.cloud.google.com/code/docs/shell).

## Supported languages

Cloud Code supports the following languages:

  * Go
  * Java
  * Node.js
  * Python
  * .NET Core



To view the Cloud Code sample applications that you can use to test Cloud Code's capabilities, see the [`cloud-code-samples` GitHub repository](https://github.com/GoogleCloudPlatform/cloud-code-samples).

## Features

This section lists all of the features for Cloud Code for Cloud Shell Editor that you can explore. 

### Code with assistance from Gemini Code Assist Standard and Enterprise

**Note:** We have unified our tools into a single, multi-agent platform called Antigravity, with Antigravity CLI now available. Starting June 18, 2026, Gemini Code Assist IDE Extensions and Gemini CLI stopped serving requests for the Gemini Code Assist for individuals, Google AI Pro, and Google AI Ultra tiers. Affected users should migrate to Antigravity and Antigravity CLI. To learn more, see the [deprecation page](https://developers.google.com/gemini-code-assist/docs/deprecations/code-assist-individuals).

Cloud Code integrates with [Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/codeassist/overview) Standard and Enterprise, an AI-powered collaborator, to simplify development. Use Gemini Code Assist Standard or Enterprise to accomplish tasks more effectively and efficiently.

Gemini Code Assist Standard and Enterprise aren't auto-enabled by default. [Code with Gemini Code Assist](https://docs.cloud.google.com/code/docs/shell/write-code-gemini) shows you how to connect to Google Cloud, select a Google Cloud project, and enable the IAM permissions, before you can begin using Gemini Code Assist.

For more information on how Cloud Code with Gemini Code Assist handles your data, see [How Cloud Code with Gemini Code Assist handles your data](https://docs.cloud.google.com/code/docs/cloud-code-gemini-code-assist-data-governance).

### Develop Google Kubernetes Engine applications

Create and run a new application with Cloud Code's GKE support. You can also work on an existing application, customize its YAML with Cloud Code's intelligent authoring support, and run it on any of your GKE clusters. Regardless of your workflow, Cloud Code helps you spend less time on configuration and context-switching, so you can focus on developing your app.

To learn more about Cloud Code's support for deploying to Arm and mixed-architecture GKE and minikube clusters, see [Arm support](https://docs.cloud.google.com/code/docs/shell/arm-support). 

#### Develop parts of a GKE application independently

Cloud Code supports using modules to develop and debug parts of your application independently. Dependencies can be defined between `skaffold.yaml` configuration files and to specific modules.

### Develop Cloud Run services

Create and deploy a new service with Cloud Code's Cloud Run support, monitoring your service's progress with the Cloud Run Explorer and service logs accessible in the Log Viewer. If you'd prefer a local development workflow, you can also develop and debug a service locally with the built-in Cloud Run emulator.

### Create container images

Create secure, production-ready container images from source code without having to worry about a Dockerfile with Cloud Code's built-in support for Google Cloud buildpacks. You get to focus on building your application, not containerizing it.

### Manage secrets

Protect sensitive information and keep your app secure with Cloud Code integrated Secret Manager support. You can create, view, update, and use secrets in the Secret Manager view without having them in your codebase.

### Browse Cloud APIs

Browse available Cloud APIs, enable services, and install and learn how to integrate client libraries in your app without leaving your IDE and breaking your development flow, all with the API library browser.

### Manage virtual machine instances

Browse Compute Engine virtual machines and their relevant properties without leaving your IDE. Connect to your VM using the terminal window and transfer files from your local environment to your VM all with Cloud Code support for Compute Engine.

### Manage data workloads with Data Agent Kit

Google Cloud Data Agent Kit is integrated into Cloud Code, letting you run data science and data engineering workflows with your Google Cloud data in your IDE without a separate installation process. For more information, see [Data Agent Kit overview](https://docs.cloud.google.com/data-agent-kit/overview).

## What's next

  * [Create and deploy a containerized web app](https://docs.cloud.google.com/code/docs/shell/deploy-gke-app).
  * [Deploy a Cloud Run service](https://docs.cloud.google.com/code/docs/shell/deploy-cloud-run-app).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
