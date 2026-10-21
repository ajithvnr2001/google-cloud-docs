---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateless-apps/
title: Deploying a stateless Linux application \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:33:50.466748+00:00
---

# Deploying a stateless Linux application  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateless-apps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Deploying a stateless Linux application Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to deploy a stateless Linux application using Google Kubernetes Engine (GKE). You can also learn how to [deploy a stateless Windows application](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-windows-app).

## Overview

_Stateless applications_ are applications which do not store data or application state to the [cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-container-cluster) or to persistent storage. Instead, data and application state stay with the client, which makes stateless applications more scalable. For example, a frontend application is stateless: you deploy multiple replicas to increase its availability and scale down when demand is low, and the replicas have no need for unique identities.

Kubernetes uses the [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) controller to deploy stateless applications as uniform, non-unique [Pods](https://kubernetes.io/docs/concepts/workloads/pods). Deployments manage the _desired state_ of your application: how many Pods should run your application, what version of the container image should run, what the Pods should be labelled, and so on. The desired state can be changed dynamically through updates to the Deployment's [Pod specification](https://kubernetes.io/docs/concepts/workloads/pods/#pod-templates).

Stateless applications are in contrast to [stateful applications](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateful-apps), which use [persistent storage](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) to save data and which use [StatefulSets](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/statefulset) to deploy Pods with unique identities.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure your containerized application is stored in an image registry, such as [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/docker/pushing-and-pulling).

  * If you are new to GKE, you should complete the [quickstart](https://docs.cloud.google.com/kubernetes-engine/docs/deploy-app-cluster), in which you'll enable the GKE API and learn how the product works.




## Anatomy of a Deployment

The following is an example of a simple Deployment manifest file. This Deployment creates three replicated Pods labelled `run=my-app` that run the `hello-app` image stored in [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/docker/pushing-and-pulling):
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-app
    spec:
      replicas: 3
      selector:
        matchLabels:
          run: my-app
      template:
        metadata:
          labels:
            run: my-app
        spec:
          containers:
          - name: hello-app
            image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
    

In this example:

  * `.spec.replicas`: is the number of replicated Pods that the Deployment manages.
  * `.spec.template.metadata.labels`: is the label given to each Pod, which the Deployment uses to manage the Pods.
  * `.spec.template.spec`: is the [Pod specification](https://kubernetes.io/docs/concepts/workloads/pods/#pod-templates), which defines how each Pod should run. `spec.containers` includes the name of the container to run in each Pod and the container image that should run.



For more information about the Deployment specification, refer to the [Deployment API reference](https://v1-30.docs.kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#deployment-v1-apps).

## Creating a Deployment

You create a Deployment using one of the following methods:

  * You can use the Deploy feature in the Google Cloud console's [Workloads](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dashboards#workloads) menu to create a simple Deployment from a container image you've stored in [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/docker/pushing-and-pulling)
  * You can write a Deployment manifest and run [`kubectl apply`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply) to create the resource




### kubectl apply

You can [declaratively](https://kubernetes.io/docs/tutorials/object-management-kubectl/declarative-object-management-configuration/) create and update Deployments from manifest files using `kubectl apply`. This method also retains updates made to live resources without merging the changes back into the manifest files.

To create a Deployment from its manifest file, run the following command:
    
    
    kubectl apply -f DEPLOYMENT_FILE

Replace `DEPLOYMENT_FILE` with the manifest file, such as `config.yaml`.

You can also use `kubectl apply -f DIRECTORY/` to create all objects (except existing ones) defined in manifest files stored a directory.

**Note:** `kubectl apply` fails if you do not have an active cluster.

### Console

To create a Deployment, perform the following steps:

  1. Go to the **Workloads** page in the Google Cloud console.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload)

  2. Click _add_box_ **Deploy**.

  3. Under **Specify container** , select one of the following:

     * **Existing container image** to choose a container image available from Artifact Registry or DockerHub. In **Image path** , enter the path to the container image and the version.

     * **New container image** to use an image created with [Cloud Source Repositories](https://docs.cloud.google.com/source-repositories) and [Cloud Build](https://docs.cloud.google.com/source-repositories/docs/integrating-with-cloud-build).

  4. Optionally, configure your deployment with:

     * **Environment variables** to pass into the container.
     * **Initial commands** to customize the container's entrypoint at runtime.
  5. Click **Done** , and then click **Continue**.

  6. In the **Configuration** section, give your deployment an **Application name** and specify the Kubernetes **Namespace** to deploy it in.

  7. Optionally, under **Labels** , you can add Kubernetes [Labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) to the deployment.

  8. To save the YAML that creates this deployment to update it later, click **View YAML**. Copy and paste the YAML into a file, then save it and click **Close** on the **YAML Output** dialog.

  9. From the **Kubernetes Cluster** drop-down menu, choose the desired cluster.

  10. Click **Deploy**.




## Inspecting the Deployment

After you create a Deployment, you can use one of the following methods to inspect it:

  * You can use the [Workloads](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dashboards#workloads) menu
  * You can use [`kubectl describe`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#describe) and [`kubectl get`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get)




### kubectl

To get detailed information about the Deployment, run the following command:
    
    
    kubectl describe deployment DEPLOYMENT_NAME

Replace `DEPLOYMENT_NAME` with the name of the Deployment.

To list the Pods created by the Deployment, run the following command:
    
    
    kubectl get pods -l KEY=VALUE

In this command, the `-l` flag instructs `kubectl` to get all Pods with a key-value label. For example, if you labelled the Deployment `run: my-app`, you'd run `kubectl get pods -l run=my-app` to see Pods with that label.

To get information about a specific Pod:
    
    
    kubectl describe pod POD_NAME

To view a Deployment's manifest, run the following command:
    
    
    kubectl get deployments DEPLOYMENT_NAME -o yaml

This command displays the Deployment's live configuration in YAML format.

### Console

To inspect a Deployment, perform the following steps:

  1. Go to the **Workloads** page in the Google Cloud console.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload)

  2. In the workloads list, click the name of the Deployment you want to inspect.

  3. On the **Deployment details** page, do any of the following:

     * Click the **Revision History** tab to see the Deployment's revision history.
     * Click the **Events** tab to see all events related to the Deployment.
     * Click the **Logs** tab to see container activity logs in the Deployment.
     * Click the **YAML** tab to see, copy, and download the YAML manifest for the Deployment.



## Updating the Deployment

You can roll out updates to a Deployment's [Pod specification](https://kubernetes.io/docs/concepts/workloads/pods/#pod-templates), such as their image, resource usage/requests, or configuration.

You can update a Deployment using the following methods:

  * You can use the **Rolling update** menu and YAML editor from the Google Cloud console [Workloads](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dashboards#workloads) menu.
  * You can make changes to a manifest file and apply them with [`kubectl apply`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply).
  * You can update the Pod specification's `image`, `resources`, or `selector` fields using [`kubectl set`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#set).
  * You can update a Deployment directly from your shell or in a preferred editor using [`kubectl edit`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#edit).




### kubectl apply

You can update the Deployment by _applying_ a new or updated manifest file. This is useful for making various changes to your Deployment, such as for _scaling_ or for specifying a new _version_ of your application.

**Note:** To update a resource with `kubectl apply`, the resource would need to have been created using either `kubectl apply` or `kubectl create --save-config`.

To update a Deployment, run the following command:
    
    
    kubectl apply -f DEPLOYMENT_FILE

Replace `DEPLOYMENT_FILE` with the updated manifest file.

The `kubectl apply` command applies a manifest file to a resource. If the specified resource does not exist, it is created by the command.

### kubectl set

You can use `kubectl set` to change a Deployment's image, resources (requests or limits), or selector fields.

To change a Deployment's image, run the following command:
    
    
    kubectl set image deployment DEPLOYMENT_NAME IMAGE IMAGE:TAG

For example, to update a Deployment from `nginx` version 1.7.9 to 1.9.1, run the following command:
    
    
    kubectl set image deployment nginx nginx=nginx:1.9.1

### Console

To access the Deployment's **Rolling update** menu:

  1. Go to the **Workloads** page in the Google Cloud console.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload)

  2. In the workloads list, click the name of the Deployment you want to modify.

  3. Click _list_ **Actions > Rolling update**.

  4. Configure the following optional parameters for the update strategy:

     * **Minimum seconds ready:** Specifies the minimum number of seconds for which newly-created Pods should be ready to be considered available.
     * **Maximum surge:** Specifies the maximum number of Pods that can be created over the desired number of Pods. Value can be an absolute number or a percentage.
     * **Maximum unavailable:** Specifies the maximum number of Pods that can be unavailable during the update process. Value can be an absolute number or a percentage.
  5. Under **Container images** , enter the image path and version for the updated container image.

  6. Click **Update**.




### Rolling back an update

You can roll back an update using [`kubectl rollout undo`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#rollout).

You can roll back an in-progress or completed update to its previous revision:
    
    
    kubectl rollout undo deployment my-deployment

You can also roll back to a specific revision:
    
    
    kubectl rollout undo deployment my-deployment --to-revision=3

## Scaling a Deployment

You can manually scale a Deployment using the Google Cloud console or [`kubectl scale`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#scale).

You can learn more about [autoscaling Deployments](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/scaling-apps#autoscaling-deployments).

### kubectl

`kubectl scale` can be used at any time to scale your Deployment.

To manually scale a Deployment, run the following command:
    
    
    kubectl scale deployment DEPLOYMENT_NAME --replicas NUMBER_OF_REPLICAS

Replace `NUMBER_OF_REPLICAS` with the desired number of replicated Pods.

### Console

To scale a Deployment, perform the following steps:

  1. Go to the **Workloads** page in the Google Cloud console.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload)

  2. In the workloads list, click the name of the Deployment you want to modify.

  3. Click _list_ **Actions > Scale > Edit replicas**

  4. Enter the new number of **Replicas** for the Deployment.

  5. Click **Scale**.




## Deleting a Deployment

You can delete a Deployment using the Google Cloud console or [`kubectl delete`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#delete).

### kubectl

To delete a Deployment, run the following command:
    
    
    kubectl delete deployment DEPLOYMENT_NAME

### Console

To delete a Deployment, perform the following steps:

  1. Go to the **Workloads** page in the Google Cloud console.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload)

  2. In the workloads list, select one or more Deployments to delete.

  3. Click _delete_ **Delete**.

  4. When prompted to confirm, click **Delete**.




## What's next

  * [Learn more about Deployments](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/deployment).
  * [Learn about stateful applications](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateful-apps).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
