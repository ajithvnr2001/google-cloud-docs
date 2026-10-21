---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/deploy-application/
title: Quickstart: Deploy an application to Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:21:23.679875+00:00
---

# Quickstart: Deploy an application to Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/deploy-application/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deploy an application to Knative serving

Learn how to use the Google Cloud console to deploy a prebuilt sample container to run as a Knative serving service.

## Before you begin

You must have access to the Google Cloud project and cluster where Knative serving is installed. For details, see [Knative serving fleet installation overview](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install).

**Tip** : See the [GKE Enterprise tutorial](https://docs.cloud.google.com/anthos/docs/tutorials/explore-anthos) for details about the shortest path to setting up a GKE Enterprise environment that includes a GKE cluster and Cloud Service Mesh.

## Deploying a sample container

Use the Google Cloud console to deploy a sample container and create a service in your cluster:

  1. In the Google Cloud console, go to the **Knative serving** page.

[Go to Knative serving](https://console.cloud.google.com/projectselector2/kubernetes/run)

  2. Select the Google Cloud project in which your GKE cluster resides.

  3. In the list of available clusters, click **Login** to connect.

  4. Open the **Create service** form by clicking **Create service**.

  5. In the available clusters dropdown menu, select your cluster.

  6. Leave `default` as the name of the [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) where you want your service to run.

  7. Enter a service name of your choice. For example, `hello`.

  8. Click **Next**.

  9. Select **Deploy one revision from an existing container image** , then select **hello** from in the **Demo containers** list.

  10. Click **Next**.

  11. Select **External** under _Connectivity_ , so that you can access your service from the web.

  12. Click **Create** to deploy the `hello` image to Knative serving and wait for the deployment to finish.




Congratulations! You have just deployed a service to a Knative serving enabled cluster.

## Accessing your deployed service

Now that you have a service running, you can send requests to it. In this section, assuming that your cluster uses default name of the ingress gateway, the default test domain is used to demonstrate how to access your service and verify that it's working:

  1. In the Google Cloud console, go to the **Knative serving** page.

[Go to Knative serving](https://console.cloud.google.com/kubernetes/run)

  2. Click the name of your new Knative serving service to open the **Service details** page. For example, **hello**.

  3. At the top of the page, click the **URL** to access your deployed service through your web browser. For example, if you named your service `hello`, the URL is similar to the following but includes your cluster's external IP address: `http://hello.default.kuberun.11.111.11.111.nip.io`




Congratulations! Your Knative serving service is live and handling requests.

## Clean up

You can delete the Knative serving service to avoid incurring costs from running those resources.

The following considerations apply to deleting a service:

  * Deleting a service deletes all resources related to this service, including all revisions of this service whether they are serving traffic or not.
  * Deleting a service does not automatically remove container images from Artifact Registry. To delete container images used by the deleted revisions from Artifact Registry, refer to [Deleting images](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images#deleting_images).

  * Deleting a service with one or more Eventarc triggers does not automatically delete these triggers. To delete the triggers refer to [Manage triggers](https://docs.cloud.google.com/eventarc/docs/managing-triggers#trigger-delete).

  * After deletion, the service remains visible in the Google Cloud console and in the command line interface until the deletion is fully complete. However, you cannot update the service.

  * Deleting a service is permanent: there is no undo or restore. However, if after deleting a service, you deploy a new service with the same name in the same region, it will have the same endpoint URL.




To permanently delete the service and all its resources:

  1. In the Google Cloud console, go to the **Knative serving** page.

[Go to Knative serving](https://console.cloud.google.com/kubernetes/run)

  2. In the services list, locate the Knative serving service that you created and click its checkbox to select it.

  3. Click **DELETE**.




## What's next

To learn how to build a container from code source, push to Container Registry, and then deploy, see:

  * [Building containers](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/building/containers)
  * [Deploying container images](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/deploying)



To learn more about how Knative serving works, see the [Architectural overview](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
