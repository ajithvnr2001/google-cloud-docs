---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/testing/local/
title: Local testing \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:22.855258+00:00
---

# Local testing  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/testing/local/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Local testing Stay organized with collections  Save and categorize content based on your preferences. 

During development, you can run and test your container image locally, prior to deploying. You can use [Cloud Code](https://docs.cloud.google.com/code) or [Docker installed locally](https://docs.docker.com/install/) to run and test locally, including running locally with access to Google Cloud services.

## Running in a Knative serving emulator

The [Cloud Code](https://cloud.google.com/code) plugin for [VS Code](https://code.visualstudio.com/) and [JetBrains IDEs](https://www.jetbrains.com/) lets you locally run and debug your container image in a Knative serving emulator within your IDE. The emulator allows you configure an environment that is representative of your service running on Knative serving.

You can configure properties like CPU and memory allocation, specify environment variables, and set Cloud SQL database connections.

  1. Install Cloud Code for [VS Code](https://docs.cloud.google.com/code/docs/vscode/install) or a [JetBrains IDE](https://docs.cloud.google.com/code/docs/intellij/install).
  2. Follow the instructions for locally developing and debugging within your IDE. 
     * **VS Code** : Locally [developing](https://docs.cloud.google.com/code/docs/vscode/developing-a-cloud-run-app) and [debugging](https://docs.cloud.google.com/code/docs/vscode/debugging-a-cloud-run-app)
     * **IntelliJ** : Locally [developing](https://docs.cloud.google.com/code/docs/intellij/developing-a-cloud-run-app) and [debugging](https://docs.cloud.google.com/code/docs/intellij/debugging-a-cloud-run-app)



## Running locally using Docker

To test your container image locally using Docker:

  1. Use the Docker command:
         
         PORT=8080 && docker run -p 9090:${PORT} -e PORT=${PORT} IMAGE_URL

Replace IMAGE_URL with a reference to the container image, for example, `gcr.io/cloudrun/hello`.

The `PORT` environment variable specifies the port your application will use to listen for HTTP or HTTPS requests. This is a requirement from the [Container Runtime Contract](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/reference/container-contract). In this example, we use port 8080.

  2. Open <http://localhost:9090> in your browser.




If you are new to working with containers, you may want to review the [Docker Getting Started](https://docs.docker.com/get-started/) guide. To learn more about Docker commands, refer to the [Docker documentation](https://docs.docker.com/engine/reference/run/).

## Running locally using Docker with access to Google Cloud services

If you are using Google Cloud client libraries to integrate your application with Google Cloud services, and have not yet secured those services to control external access, you can set up your local container to authenticate with Google Cloud services using a service account key.

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

To run locally:

  1. Refer to [Service account key](https://docs.cloud.google.com/docs/authentication/set-up-adc-on-premises#wlif-key) for help with setting up your credentials.

  2. The following Docker run flags inject the credentials and configuration from your local system into the local container:

     1. Use the `--volume` (`-v`) flag to inject the credential file into the container (assumes you have already set your `GOOGLE_APPLICATION_CREDENTIALS` environment variable on your machine): 
            
            -v $GOOGLE_APPLICATION_CREDENTIALS:/tmp/keys/FILE_NAME.json:ro

     2. Use the `--environment` (`-e`) flag to set the `GOOGLE_APPLICATION_CREDENTIALS` variable inside the container: 
            
            -e GOOGLE_APPLICATION_CREDENTIALS=/tmp/keys/FILE_NAME.json

  3. Optionally, use this fully configured Docker `run` command:
         
         PORT=8080 && docker run \
         -p 9090:${PORT} \
         -e PORT=${PORT} \
         -e K_SERVICE=dev \
         -e K_CONFIGURATION=dev \
         -e K_REVISION=dev-00001 \
         -e GOOGLE_APPLICATION_CREDENTIALS=/tmp/keys/FILE_NAME.json \
         -v $GOOGLE_APPLICATION_CREDENTIALS:/tmp/keys/FILE_NAME.json:ro \
         IMAGE_URL

Note that the path 
         
         /tmp/keys/FILE_NAME.json

shown in the example above is a reasonable location to place your credentials inside the container. 

However, other directory locations will also work. The crucial requirement is that the `GOOGLE_APPLICATION_CREDENTIALS` environment variable must match the bind mount location inside the container.

Note also, that with some Google Cloud services, you may want to use an alternate configuration to isolate local troubleshooting from production performance and data.




## What's next

To learn how to deploy your built containers, follow [Deploying Services](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/deploying).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
