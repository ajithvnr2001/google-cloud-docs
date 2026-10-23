---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/private-registry-no-secrets/
title: Use a private image registry without Secrets \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:18.849715+00:00
---

# Use a private image registry without Secrets  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/private-registry-no-secrets/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Use a private image registry without Secrets Stay organized with collections  Save and categorize content based on your preferences. 

GKE on AWS provides a way of pulling private images from [Artifact Registry](https://docs.cloud.google.com/artifact-registry) or Container Registry without having to use a Kubernetes Secret. Previously, you had to perform the following steps:

  1. Create a Google Identity and Access Management (IAM) service account.
  2. Grant the service account permissions to access the private registry.
  3. Download the service account key and save it as a Kubernetes Secret in your cluster.
  4. Reference this Secret in your YAML manifest for Pods or Deployments so that they can access images from the private container repository.
  5. Regularly rotate and manage the keys associated with the Google IAM service account.



GKE on AWS eliminates all of these manual steps, and automatically handles the authentication and authorization required for pulling private images.

## Before you begin

To perform the steps on this page, first complete the following:

  * [Create a cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-cluster).
  * [Create a node pool](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-node-pool).
  * [Configure cluster access for kubectl](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/configure-cluster-access-for-kubectl).

  * Build a Docker image and push it to Artifact Registry. The examples in this page use the `hello-app` container. To build this container, follow the steps to [Build a container image](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/hello-app#building_the_container_image) and [Push the Docker image to Artifact Registry](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/hello-app#pushing_the_docker_image_to), part of the GKE on Google Cloud documentation.

  * Upgrade to version 1.28 of GKE on AWS so that you can pull private images from [Artifact Registry](https://docs.cloud.google.com/artifact-registry) or Container Registry without having to use a Kubernetes Secret.




## Check for images on Artifact Registry

To complete the rest of these steps, you need a container image. Get the name of your container images by performing the following steps:

  1. Configure the Docker command-line tool to authenticate to [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs) with Google Cloud SDK:
         
         gcloud auth configure-docker
         

The Google Cloud CLI registers a credential helper for all Google-supported Docker registries.

  2. Confirm that your Artifact Registry includes an image with the `docker images` command:
         
         docker images
         

Docker connects to Artifact Registry and returns the images available in your repository. For example, the following response shows a container image named `hello-app` in the `PROJECT_NAME` repository on `us-west1-docker.pkg.dev`.
         
         REPOSITORY                                                            TAG          IMAGE ID       CREATED          SIZE
         us-west1-docker.pkg.dev/PROJECT_NAME/hello-repo/hello-app   v1           f7cfe0d58569   21 minutes ago   11.5MB
         




If you don't have a container image ready, create one by following the steps at [Deploying a containerized application](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/hello-app).

## Create Pods with private images without image pull Secrets

To create a Pod that can access a private container image from a registry, you no longer need to provide the `spec.imagePullSecrets` field in your Pod specification. To set up your Pod, perform these steps:

  1. Create a Pod definition without the `spec.imagePullSecrets` field:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: POD_NAME
         spec:
           containers:
           - name: CONTAINER_NAME
             image: LOCATION-docker.pkg.dev/PROJECT_NAME/REPOSITORY_NAME/IMAGE_NAME:IMAGE_VERSION
         

Replace the following:

     * `POD_NAME`: the name of the Pod.
     * `CONTAINER_NAME`: the name of the container inside the Pod.
     * `LOCATION`: the Google Cloud region that contains your registry. For example, `us-west1`.
     * `PROJECT_NAME`: the name of the Google Project hosting your Artifact Registry repository, which might be the same as your cluster's project. If the repository is in a different project, see Use Artifact Registry when it's not in the same project as your cluster for additional steps.
     * `REPOSITORY_NAME`: the name of your repository.
     * `IMAGE_NAME`: the name of the image.
     * `IMAGE_VERSION`: the version of the image.
  2. Apply the configuration to your cluster with `kubectl`:
         
         kubectl apply -f YAML_FILE_NAME
         

Replace `YAML_FILE_NAME` with the name of your YAML file.




### Example of creating Pods without image pull Secrets

Here's an example of creating a Kubernetes Pod without the need for image pull Secrets. The Pod pulls the `hello-app` image from Artifact Registry.

  1. To pull the image `hello-app`, copy the following YAML into a file named `hello-pod.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: hello-pod
         spec:
           containers:
           - name: hello-container
             image: us-west1-docker.pkg.dev/example-project/hello-repo/hello-app:v1
         

  2. Apply the configuration to your cluster with `kubectl`:
         
         kubectl apply -f hello-pod.yaml
         

  3. Confirm the Pod is running with `kubectl get`:
         
         kubectl get pod/hello-pod
         

The response includes one Pod with a status of `Running`.
         
         NAME        READY   STATUS    RESTARTS   AGE
         hello-pod   1/1     Running   0          15s
         




## Create Deployments with private images without image pull Secrets

To create a [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) that can access a private container image from a registry, you no longer need to provide the `spec.imagePullSecrets` field in your Deployment specification. To set up your Deployment, perform these steps:

  1. Create a Deployment definition without the `spec.imagePullSecrets` field:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: DEPLOYMENT_NAME
         spec:
           replicas: NUMBER_OF_REPLICAS
           template:
             spec:
               containers:
               - name: CONTAINER_NAME
                 image: LOCATION-docker.pkg.dev/PROJECT_NAME/REPOSITORY_NAME/IMAGE_NAME:IMAGE_VERSION
         

Replace the following:

     * `DEPLOYMENT_NAME`: the name of your Deployment.
     * `NUMBER_OF_REPLICAS`: how many instances of the Pod defined in the Deployment should be running at any given time.
     * `CONTAINER_NAME`: the name of the container inside the Pod.
     * `LOCATION`: the Google Cloud region that contains your registry. For example, `us-west1`.
     * `PROJECT_NAME`: the name of the Google Project hosting your Artifact Registry repository, which might not be the same as your cluster's project. If the repository is in a different project, see Use Artifact Registry when it's not in the same project as your cluster for additional steps.
     * `REPOSITORY_NAME`: the name of your repository.
     * `IMAGE_NAME`: the name of the image.
     * `IMAGE_VERSION`: the version of the image.
  2. Apply the configuration to your cluster with `kubectl`.
         
         kubectl apply -f name-of-your-yaml-file.yaml
         




### Example of creating a Deployment without image pull Secrets

Here's an example of creating a Deployment without image pull Secrets. The Deployment pulls a `hello-app` image from Artifact Registry.

  1. Create a file named `hello-deployment.yaml` with the following contents:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: hello-app-deployment
         spec:
           selector:
             matchLabels:
               app: products
               department: sales
           replicas: 3
           template:
             metadata:
               labels:
                 app: products
                 department: sales
             spec:
               containers:
               - name: hello
                 image: LOCATION-docker.pkg.dev/PROJECT_NAME/hello-repo/hello-app:v1
                 env:
                 - name: "PORT"
                   value: "50001"
         

Replace the following:

     * `LOCATION`: the Google Cloud region that contains your registry. For example, `us-west1`.
     * `PROJECT_NAME`: the name of the Google Project hosting your Artifact Registry repository, which might not be the same as your cluster's project. If the repository is in a different project, see Use Artifact Registry when it's not in the same project as your cluster for additional steps.
  2. Apply the configuration to your cluster with `kubectl`.
         
         kubectl apply -f hello-deployment.yaml
         

  3. Confirm that your Deployment is running with `kubectl pods`.
         
         kubectl get pods --selector=app=products
         

The output displays three `Running` Pods.
         
         NAME                                    READY   STATUS    RESTARTS   AGE
         hello-app-deployment-67d9c6d98c-b69f2   1/1     Running   0          14m
         hello-app-deployment-67d9c6d98c-d6k5c   1/1     Running   0          14m
         hello-app-deployment-67d9c6d98c-p2md5   1/1     Running   0          14m
         




## Use Artifact Registry when it's not in the same project as your cluster

To use an Artifact Registry repository that's in a Google Project different from the one containing your cluster, perform the following steps:

Give the service account for your cluster's node pool virtual machine instances, known as the [Node pool Machine Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#anthos-multi-cloud-node-pool-machine-service-agent), the necessary permissions to access this registry.
    
    
    gcloud projects add-iam-policy-binding AR_PROJECT_ID \
      --member=NODE_POOL_MACHINE_SERVICE_AGENT \
      --role=ROLE
    

This step ensures your cluster can retrieve artifacts from the registry in that separate project.

Replace the following:

  * `AR_PROJECT_ID`: the ID of the Google project hosting the Artifact Registry.
  * `NODE_POOL_MACHINE_SERVICE_AGENT`: the service account for your cluster's Node Pool, which has the following format: `service-CLUSTER_RESOURCE_PROJECT_NUMBER@gcp-sa-gkemulticloudnpmachine.iam.gserviceaccount.com`
  * `ROLE`: the role `roles/artifactregistry.reader` or a custom role that grants sufficient permissions for accessing images in the Artifact Registry repository.



## Use private Google Container Registry

To integrate a private Google Container Registry with your GKE on AWS cluster, regardless of its Google project location, follow these steps:

Allow the Node Pool Machine Service Agent, the service account for your cluster's node pool virtual machine instances, to access the Container Registry:
    
    
    gcloud projects add-iam-policy-binding GCR_PROJECT_ID \
      --member=NODE_POOL_MACHINE_SERVICE_AGENT \
      --role=ROLE
    

This step enables cluster service account access to the private container images.

Replace the following:

  * `GCR_PROJECT_ID`: the ID of the project hosting the Container Registry.
  * `NODE_POOL_MACHINE_SERVICE_AGENT`: the node pool service account, in the format `service-CLUSTER_RESOURCE_PROJECT_NUMBER@gcp-sa-gkemulticloudnpmachine.iam.gserviceaccount.com`.
  * `ROLE`: choose `storage.objectViewer` or a custom role for sufficient Container Registry access. Be cautious of broad access with `storage.objectViewer`.



## Clean up

To remove the resources you created on this page, run these commands:
    
    
    kubectl apply -f POD_YAML_FILE
    kubectl delete -f DEPLOYMENT_YAML_FILE
    

Replace the following:

  * `POD_YAML_FILE`: the name of the YAML file in which you defined the Pod.
  * `DEPLOYMENT_YAML_FILE`: the name of the YAML file in which you defined the Deployment.



## What's next

  * Read the [Artifact Registry overview](https://docs.cloud.google.com/artifact-registry/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
