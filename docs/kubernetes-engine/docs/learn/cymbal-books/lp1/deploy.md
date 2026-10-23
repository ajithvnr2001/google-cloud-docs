---
url: https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/deploy/
title: Learning Path: Transform a monolith into a GKE app - Deploy the app to a GKE cluster \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:53.570155+00:00
---

# Learning Path: Transform a monolith into a GKE app - Deploy the app to a GKE cluster  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/deploy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Learning Path: Transform a monolith into a GKE app - Deploy the app to a GKE cluster Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This is the fifth and final tutorial in a learning path that teaches you how to modularize and containerize a monolithic app.

The learning path consists of the following tutorials:

  1. [Overview](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/overview)
  2. [Understand the monolith](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/monolith)
  3. [Modularize the monolith](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/modular)
  4. [Prepare the modular app for containerization](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/prep-containerization)
  5. [Containerize the modular app](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/containerize)
  6. Deploy the app to a GKE cluster (this tutorial)



In the previous tutorial, [Containerize the modular app](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/containerize), you prepared the modular Cymbal Books app for deployment. You containerized the app's modules, tested the resulting containers, and pushed the container images to [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs).

In this tutorial, you deploy the containerized app to a Google Kubernetes Engine cluster. This step completes the transformation of the Cymbal Books app into a modular and scalable system that runs on a Kubernetes cluster.

## Costs

Following the steps in this tutorial incurs charges on your Google Cloud account. Costs begin when you enable GKE and deploy the Cymbal Books sample app. These costs include per-cluster charges for GKE, as outlined on the [Pricing page](https://cloud.google.com/kubernetes-engine/pricing), and charges for running Compute Engine VMs.

To avoid unnecessary charges, ensure that you disable GKE or delete the project once you have completed this tutorial.

## Before you begin

Before you begin this tutorial, make sure that you completed the earlier tutorials in the series. For an overview of the whole series, and links to particular tutorials, see [Learning Path: Transform a monolith into a GKE app - Overview](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/overview).

In particular, you need to have performed the steps in the previous tutorial, [Containerize the modular app](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/containerize).

## Set up the GKE cluster

Before you can deploy the modular Cymbal Books app, you must first create a GKE cluster. This cluster provides the infrastructure in which your app's containers will run.

In this tutorial, you use the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) to create the cluster. Alternatively, you can use the [Google Cloud console](https://console.cloud.google.com/), which provides a graphical user interface (GUI) for creating and managing Google Cloud resources such as GKE clusters.

### Create and verify a GKE cluster

A GKE cluster provides the computing resources that are needed to run your containers in Kubernetes. Follow these steps to create a cluster by using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

  1. Go to the [Google Cloud console](https://console.cloud.google.com/).

  2. In the console, click the **Activate Cloud Shell** button: ![Activate Cloud Shell](https://docs.cloud.google.com/static/kubernetes-engine/images/cloud-shell.png)

A Cloud Shell session opens inside a frame lower on the console.

  3. Set your default project in the Google Cloud CLI:
         
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with the project ID of the project that you created or selected in the [select or create a Google Cloud project](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/containerize#select-create-project) section of the previous tutorial. A project ID is a unique string that differentiates your project from all other projects in Google Cloud. To locate the project ID, go to the [project selector](https://console.cloud.google.com/projectselector2/home/dashboard). On that page, you can see the project IDs for each of your Google Cloud projects.

  4. Create a GKE cluster:
         
         gcloud container clusters create CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --num-nodes=2
         

Replace the following:

     * `CLUSTER_NAME`: a name for your cluster, such as `cymbal-cluster`.

     * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters, such as `us-central1` or `europe-west1-b`.

  5. Retrieve the cluster's credentials so that the `kubectl` CLI can connect to the cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION
         

This command updates your Kubernetes config file, which is stored by default in `~/.kube/config`. This config file contains the credentials that `kubectl` requires to interact with your GKE cluster.

  6. Verify that `kubectl` is connected to the cluster by listing the cluster nodes:
         
         kubectl get nodes
         

If the setup is successful, this command lists the nodes in your GKE cluster. Because you created the cluster with `--num-nodes=2`, you should see information about two nodes, similar to the following:
         
         NAME                                         STATUS    ROLES    AGE    VERSION
         gke-nov18-default-pool-6a8f9caf-bryg   Ready     <none>   30s    v1.30.8-gke.1128000
         gke-nov18-default-pool-6a8f9caf-ut0i   Ready     <none>   30s    v1.30.8-gke.1128000
         

In this example, both nodes are in the `Ready` state. This state means that the GKE cluster is ready to host your containerized workloads!




## Deploy the app

Now that you've created a GKE cluster, you can deploy the Cymbal Books app to it. To deploy an app to a cluster, you apply the Kubernetes manifest to the cluster.

### Apply the Kubernetes manifest

In Cloud Shell, deploy the app to the GKE cluster by running the following commands:

  1. Navigate to the root directory of the containerized application:
         
         cd kubernetes-engine-samples/quickstarts/monolith-to-microservices/containerized/
         

  2. Apply the Kubernetes manifest:
         
         kubectl apply -f kubernetes_manifest.yaml
         




The previous command instructs Kubernetes to create the resources specified in the `kubernetes-manifest.yaml` file. These resources include Services, a Deployment, and Pods.

You first encountered Services in the [Change the modular code](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/prep-containerization#change-mod-code) section in the [Prepare the modular app for containerization](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/prep-containerization) tutorial. In that tutorial, you updated the app's code to use Service names instead of `localhost`. That update enables Kubernetes to route requests between modules and ensures that the modules can communicate with each other within a cluster. Now, when you apply the manifest, Kubernetes creates the Services inside the cluster.

A _Deployment_ is a Kubernetes API object that lets you run multiple replicas of Pods that are distributed among the nodes in a cluster.. The next section explains what Pods are.

### What is a Kubernetes Pod?

In the previous tutorial, you created a container image for each module of the Cymbal Books app. For example, you created container images based on the `home_app` and `book_details_app` modules.

When you use the `kubectl apply` command to deploy the Kubernetes manifest, Kubernetes pulls your container images from Artifact Registry into the cluster. In the cluster, the container images become containers, and the containers run inside Pods.

A Pod is an isolated environment in which containers run, and it performs the following tasks:

  * **Allocates CPU and memory** : a Pod provides the resources that containers need to operate.
  * **Provides networking** : each Pod has its own IP address. This enables the Pod to communicate with other Pods.



Pods run on _nodes_ , which are the machines that provide computing power for the cluster. Kubernetes automatically assigns Pods to nodes and distributes the Pods across the cluster's nodes to reduce the risk of overloading any single node. This distribution helps the cluster use its computing and memory resources efficiently.

## Verify the Deployment

After you apply the Kubernetes manifest with the `kubectl apply` command, verify that the app was deployed successfully to the cluster. To verify the Deployment, check that the Pods and Services are running correctly.

### Check the Pods

To view the Pods in your cluster, run the following command:
    
    
    kubectl get pods
    

This command lists the Pods and their current status. Look for the **STATUS** column to confirm that all Pods are marked as `Running`, which indicates that they are successfully running and ready to serve requests. The expected output looks like the following:
    
    
    NAME                             READY   STATUS    RESTARTS   AGE
    home-app-67d59c6b6d-abcde        1/1     Running   0          30s
    book-details-app-6d8bcbc58f-xyz  1/1     Running   0          30s
    book-reviews-app-75db4c4d7f-def  1/1     Running   0          30s
    images-app-7f8c75c79c-ghi        1/1     Running   0          30s
    

A Pod's status initially appears as `Pending` while it's being created and its containers are in the process of starting. If a Pod remains `Pending` for an extended period, the cluster might lack sufficient resources for that Pod to enter a healthy `Running` state. If a Pod has a status of `CrashLoopBackOff`, there might be a problem with the container. Troubleshooting steps are provided later in the tutorial.

### Check the Services

Services enable communication between Pods and allow external clients (for example, users, automated scripts, or monitoring tools) to access the app. To view the Services in your cluster, run the following command:
    
    
    kubectl get services
    

Output from this command looks like the following:
    
    
    NAME               TYPE           CLUSTER-IP      EXTERNAL-IP       PORT(S)        AGE
    home-app-service   LoadBalancer   10.12.3.4       35.185.1.2        80:30837/TCP   30s
    details-service    ClusterIP      10.12.3.5       <none>            80/TCP         30s
    reviews-service    ClusterIP      10.12.3.6       <none>            80/TCP         30s
    images-service     LoadBalancer   10.12.3.7       34.125.6.3        80:32014/TCP   30s
    

Key fields to observe in the output are the following:

  * `TYPE`: this field indicates how the Service is exposed. Services of type `LoadBalancer` provide external access to the app.
  * `EXTERNAL-IP`: for a Service of type `LoadBalancer`, the `EXTERNAL-IP` field shows the public IP address that users can enter into their web browser to access the app. For a Service of type `ClusterIP`, this field is empty because `ClusterIP` Services are only accessible within the cluster.



## Test the deployment

After you deploy the Cymbal Books app to the GKE cluster, verify that the app is accessible and that the containers can communicate with each other.

### Access the app

Confirm that the app is accessible by following these steps:

  1. Retrieve the external IP address for the `home-app-service`:
         
         kubectl get services
         

Look for the `**EXTERNAL-IP**` column in the output, and note the IP address that's associated with `home-app-service`.

  2. Open a web browser and enter the following URL:
         
         http://EXTERNAL-IP
         

Replace `EXTERNAL-IP` with the IP address that you found in the previous step.

  3. Verify that the homepage of the Cymbal Books app loads correctly.




### Verify inter-service communication

The containers in the Cymbal Books app rely on Services to exchange information. Ensure that the containers can communicate effectively by following these steps:

  1. Retrieve the external IP address for the `home-app-service` as described earlier.

  2. Use the app's interface to test interactions between containers. To do that, confirm that the following features work by clicking all available links in the app's interface:

     * **Check book cover images** : confirm that the book cover images load correctly on both the homepage and the book details page. If they do, `home_app` and `book_details_app` containers are successfully communicating with the `images_app` container.
     * **View book details** : navigate to a book details page from the home page. If you see a book's details, the `home_app` container is correctly communicating with the `book_details_app`.
     * **View book reviews** : click a book review link to verify that the `home_app` container can communicate with the `book_reviews_app` container.



## Your app is now running on a GKE cluster!

Congratulations! You've seen how to transform a monolithic app into a modular, containerized system that runs on a live GKE cluster. Along the way, you learned how to divide tightly coupled code into independent modules, build and push container images to a repository, define Kubernetes manifests, and deploy your app from the registry to GKE. That's a major accomplishment, and it reflects the real-world steps teams take to modernize applications for the cloud!

## Troubleshooting

If the app doesn't respond or containers fail to communicate, use the following troubleshooting steps to diagnose and resolve common issues.

### Check the status of your Pods

Start by listing all Pods in your cluster to determine if they are running as expected:
    
    
    kubectl get pods
    

Review the output to confirm that each Pod is in the `Running` state. If any Pod isn't running, note its name for further inspection.

### Inspect Pod logs

If a Pod isn't handling requests properly, check its logs to look for any error messages:
    
    
    kubectl logs POD_NAME
    

Replace `POD_NAME` with the name of the Pod you want to inspect. This command is useful for identifying startup issues or runtime errors.

### Describe a Pod for detailed information

If a Pod remains in a non-`Running` state for longer than five minutes—for example, it's in a `Pending`, `ContainerCreating`, or `CrashLoopBackOff` state—you can see detailed information about the Pod's status and events by using the following command:
    
    
    kubectl describe pod POD_NAME
    

Replace `POD_NAME` with the name of the Pod that you want detailed information about.

The `Events` section in the output might indicate that resource constraints or issues with image pulls are preventing the Pod from starting properly.

### Verify Service configuration

Ensure that your Services are set up correctly, especially the Service that exposes the home module with an external IP address. List the Services with the following command:
    
    
    kubectl get services
    

If you notice that the Service for the home module has an `EXTERNAL-IP` address that's listed as `Pending`, run the following command:
    
    
    kubectl describe service SERVICE_NAME
    

Replace `SERVICE_NAME` with the name of the home module Service.

This command provides more details about the Service configuration and helps you identify delays in assigning the external IP address or other configuration issues.

### Check cluster events

You can examine cluster events to determine if a problem is affecting multiple components of your cluster:
    
    
    kubectl get events
    

This command can determine if broader resource or network issues are affecting your deployment.

## Clean up resources

Running a GKE cluster incurs costs. After you complete this tutorial, clean up your resources to avoid additional charges. Follow these steps to remove the cluster and, optionally, the entire project.

### Delete the GKE cluster

To delete the GKE cluster, use the following command:
    
    
    gcloud container clusters delete CLUSTER_NAME
        --location=CONTROL_PLANE_LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster you created, such as `cymbal-cluster`.

  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.




When prompted, confirm the deletion.

### Verify that the cluster is deleted

To ensure that the cluster was deleted, run the following command:
    
    
    gcloud container clusters list
    

The cluster should no longer appear in the output. If it does, wait a few moments and try again.

### (Optional) Delete the Google Cloud project

If you created a Google Cloud project specifically for this tutorial and you no longer need it, you can delete the entire Google Cloud project. Deleting the project removes all resources and stops billing for the project:

  1. In the Google Cloud console, open the **Manage Resources** page.
  2. Select the project you want to delete.
  3. Click **Delete Project** and follow the prompts to confirm.



## Summary of the series

Congratulations! By completing this learning path, you've learned the fundamentals of converting a monolithic app into a modular, containerized app that runs on a Kubernetes cluster. The following steps summarize the process:

  1. [Understand the monolith](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/monolith)

     * Explored the structure of the Cymbal Books monolithic app.
     * Set up a local Python environment to run the monolith and tested its endpoints.
     * Gained an understanding of the app's codebase to prepare it for modularization.
  2. [Modularize the monolith](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/modular)

     * Learned how to split monolithic code into separate modules. Each module handles a distinct feature, such as displaying book details or reviews.
     * Saw how these modules are implemented as independent Flask apps running on different ports.
     * Tested the modularized app.
  3. [Prepare the modular code for containerization](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/prep-containerization)

     * Learned that you had to update URLs in `home.py` to use Service names instead of `localhost`.
     * Learned how the Kubernetes manifest defines Services that enable the app's modules, which already communicate with each other, to find each other within the context of a Kubernetes cluster.
  4. [Containerize the modular app](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/containerize)

     * Set up a Google Cloud project and cloned the app from GitHub into Cloud Shell.
     * Built container images for each module using Docker and tested containers locally.
     * Pushed the container images to Artifact Registry to prepare the app for deployment to a cluster.
     * Updated the Kubernetes manifest to refer to the container image paths in Artifact Registry.
  5. Deploy the app to a GKE cluster (the tutorial you're in now):

     * Created a GKE cluster.
     * Deployed the container images from Artifact Registry to the GKE cluster.
     * Tested the final version of the app, which is now scalable and runs in a Kubernetes environment!



## What's next

For further practical training about how to create clusters, see our series, [Learning Path: Scalable applications](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
