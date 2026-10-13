---
url: https://docs.cloud.google.com/run/docs/deployment-options-for-services/
title: Deployment options for Cloud Run services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:13:36.415035+00:00
---

# Deployment options for Cloud Run services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/deployment-options-for-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Deployment options for Cloud Run services Stay organized with collections  Save and categorize content based on your preferences. 

As described in the [Cloud Run deployment types and resource model](https://docs.cloud.google.com/run/docs/resource-model), Cloud Run offers multiple deployment options and deployment methods. This page provides an overview of the different deployment types and some of the tools and interfaces that you can use for Cloud Run service deployments.

## Deployment types

When deploying to a Cloud Run service, you can choose from the following options:

### Deploy containers

To deploy to Cloud Run using a container image, you must package your application code and its dependencies into a container registry, and then run the deployment.

  * If you already have a container ready to deploy, see [Deploying container images](https://docs.cloud.google.com/run/docs/deploying).



### Deploy from source code

You can deploy your code directly from a local directory or repository without manually building container images first.

  * [Deploy services from source code](https://docs.cloud.google.com/run/docs/deploying-source-code): Use `gcloud run deploy --source` to package your source code. You can choose to deploy with Cloud Build using Google Cloud's buildpacks (default) or bypass the Cloud Build step to deploy prebuilt artifacts directly (Preview) for faster deployment.
  * [Deploy a Cloud Run function](https://docs.cloud.google.com/run/docs/deploy-functions): Deploy single-purpose code snippets that trigger in response to Google Cloud events, such as Eventarc events. Functions use Google Cloud's buildpacks and Cloud Build to construct and deploy the container image.
  * If you need to package your code, dependencies, and system libraries into a container, see the following pages before you deploy to Cloud Run: 
    * [Containerize your code](https://docs.cloud.google.com/run/docs/building/containerize-your-code): Declare your environment configuration using a standard `Dockerfile` or build directly using [Google Cloud's buildpacks](https://docs.cloud.google.com/docs/buildpacks/builders).
    * [Build sources to containers](https://docs.cloud.google.com/run/docs/building/containers): Build your container images locally using Docker or in the cloud using Cloud Build, and push the images to a supported registry such as Artifact Registry.



### Continuous deployment from git

To set up Cloud Run to build and deploy new revisions when you push changes to your repository, see [Continuously deploy from a repository](https://docs.cloud.google.com/run/docs/continuous-deployment).

You can connect your GitHub, GitLab, or Bitbucket repository directly in the Google Cloud console using Cloud Build triggers or Developer Connect.

## Deployment methods and tools

You can use any of the following core methods and interfaces to deploy a Cloud Run service:

  * **Google Cloud console** : Use the interactive graphical user interface in the Google Cloud console to deploy container images and functions, or configure continuous deployment manually. The Google Cloud console provides helpful tooltips, forms, and immediate feedback when you set up configuration settings.
  * **Google Cloud CLI** : Use the `gcloud run deploy` command to enable scripting and rapid command-line deployments of container images. This method works well for most deployment types, and is convenient for building and deploying local source code using a single command.
  * **YAML** : Use the YAML file for your Cloud Run service to manifest your service specs in Knative-compliant declarative configuration files. Then apply the changes using `gcloud run services replace service.yaml`. This approach enables a GitOps continuous deployment model where the configuration lives in your repository as the source of truth.
  * **Terraform** : Use the standard Google Cloud provider resource (`google_cloud_run_v2_service`) to deploy and update serverless compute infrastructure deterministically alongside other cloud resources, such as databases, load balancers, and security policies.
  * **Client libraries** : Use the Cloud Client Libraries for languages like Go, Java, Node.js, Python, Ruby, PHP, and .NET to programmatically configure and trigger deployments.
  * **REST API** : Directly invoke the REST API endpoint using HTTP operations to integrate with custom deployment systems. 
  * [**Deploy services using Compose**](https://docs.cloud.google.com/run/docs/deploy-run-compose): Define your application stack with multiple containers (such as backend services or sidecars) using a standard `compose.yaml` file, and deploy them together onto Cloud Run using the `gcloud run deploy --compose` command.
  * [**Use the remote MCP server**](https://docs.cloud.google.com/run/docs/use-cloud-run-mcp): Connect your generative AI assistants and code agents to a remote Model Context Protocol (MCP) server so they can deploy, inspect, or manage your public and private Cloud Run services.
  * [**Deployment previews**](https://github.com/GoogleCloudPlatform/devrel-demos/tree/main/app-dev/cloud-run-deployment-previews): Automate the deployment process through Cloud Build. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
