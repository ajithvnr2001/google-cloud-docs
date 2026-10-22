---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/private-registry/
title: Use a private image registry \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:24.560147+00:00
---

# Use a private image registry  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/private-registry/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Use a private image registry Stay organized with collections  Save and categorize content based on your preferences. 

Your GKE on AWS installation can access public container images by default. This topic explains how to use GKE on AWS with a private container image repository, such as [Artifact Registry](https://docs.cloud.google.com/artifact-registry).

Starting from version 1.28, GKE on AWS provides a way of pulling private images from [Artifact Registry](https://docs.cloud.google.com/artifact-registry) or Container Registry without having to use a Kubernetes Secret. For details, see [Use a private image registry without Secrets](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/private-registry-no-secrets). 

## Before you begin

To perform the steps on this page, first complete the following:

  * [Create a cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-cluster).
  * [Create a node pool](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-node-pool).
  * [Configure cluster access for kubectl](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/configure-cluster-access-for-kubectl).

  * Build a Docker image and push it to Artifact Registry. The examples in this page use the `hello-app` container. To build this container, follow the steps to [Build a container image](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/hello-app#building_the_container_image) and [Push the Docker image to Artifact Registry](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/hello-app#pushing_the_docker_image_to), part of the GKE on Google Cloud documentation.




## Check for images on Artifact Registry

To complete the rest of these steps, you need a container image. Get the name of your container images by performing the following steps:

  1. Configure the Docker command-line tool to authenticate to [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs) with Google Cloud SDK:
         
         gcloud auth configure-docker
         

The `gcloud` command-line tool registers a credential helper for all Google-supported Docker registries.

  2. Confirm that your Artifact Registry includes an image with the `docker images` command.
         
         docker images
         

Docker connects to Artifact Registry and returns the images available in your repository. For example, the response below shows a container image named `hello-app` in the `PROJECT_NAME` repository on `us-west1-docker.pkg.dev`.
         
         REPOSITORY                                                            TAG          IMAGE ID       CREATED          SIZE
         us-west1-docker.pkg.dev/PROJECT_NAME/hello-repo/hello-app   v1           f7cfe0d58569   21 minutes ago   11.5MB
         




If you do not have a container image ready, create one by following the steps at [Deploying a containerized application](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/hello-app).

### Create a Service Account

**Note:** The following service account will have access to all images in your project. For more information about restricting access, see [Granting permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) in the Artifact Registry documentation.

Your clusters authenticate using an Identity and Access Management (IAM) [service account](https://docs.cloud.google.com/iam/docs/service-accounts).

To create a new service account, follow these steps:

  1. Create an IAM service account with the Google Cloud CLI.
         
         gcloud iam service-accounts create ACCOUNT_NAME
         

Replace ACCOUNT_NAME with the name of the new Google Cloud service account.

  2. Grant the service account [Artifact Registry permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control#roles).
         
         gcloud projects add-iam-policy-binding PROJECT_NAME \
           --member serviceAccount:ACCOUNT_NAME@PROJECT_NAME.iam.gserviceaccount.com \
           --role roles/artifactregistry.reader
         

Replace the following:

     * `PROJECT_NAME` with your Google Cloud project
     * `ACCOUNT_NAME` with your Google Cloud service account name
  3. Download the account's service account key.
         
         gcloud iam service-accounts keys create registry-access-key.json \
           --iam-account ACCOUNT_NAME@PROJECT_NAME.iam.gserviceaccount.com
         

Replace the following:

     * `PROJECT_NAME`
     * `ACCOUNT_NAME`
**Note:** The service account key allows access to privileged resources. Protect the key file after downloading it.



You are now ready to configure your user cluster to connect to Artifact Registry.

### Save the key to your cluster

To provide the key to authenticate to Artifact Registry, save the service account key as a Kubernetes [Secret](https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure) with these steps:

  1. Use `kubectl` to create the Secret.
         
         kubectl create secret docker-registry registry-secret \
           --docker-server=LOCATION-docker.pkg.dev \
           --docker-username=_json_key \
           --docker-email=ACCOUNT_NAME@PROJECT_NAME.iam.gserviceaccount.com \
           --docker-password="$(cat registry-access-key.json)"
         

Replace the following:

     * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository.
     * `PROJECT_NAME`
     * `ACCOUNT_NAME`
  2. Delete the local copy of your service account key.
         
         rm registry-access-key.json
         




You can now reference this Secret in your workloads.

## Create a workload with a private image

To use an image from a private container repository with a workload, set the field `spec.imagePullSecrets` to your Secret name. This field is in different locations for Pods and Deployments.

### Creating a Pod

To create a Pod that can access the container registry, you set the field `spec.imagePullSecrets` to your Secret name.

  1. Create a Pod that specifies `spec.imagePullSecrets`.
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: POD_NAME
         spec:
           containers:
           - name: CONTAINER_NAME
             image: LOCATION-docker.pkg.dev/PROJECT_NAME/hello-repo/hello-app:v1
           imagePullSecrets:
           - name: registry-secret
         

Replace the following:

     * `POD_NAME`: your Pod's name
     * `CONTAINER_NAME`: the name of the container inside the Pod
     * `LOCATION`
     * `PROJECT_NAME`

For example, to pull the image `hello-app`, copy the following YAML into a file named `hello-pod.yaml`.
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: hello-pod
    spec:
      containers:
      - name: hello-container
        image: us-west1-docker.pkg.dev/example-project/hello-repo/hello-app:v1
      imagePullSecrets:
      - name: registry-secret
    

  2. Apply the configuration to your cluster with `kubectl`.
         
         kubectl apply -f hello-pod.yaml
         

  3. Confirm the pod is running with `kubectl get`.
         
         kubectl get pod/hello-pod
         

The response includes one Pod with a status of `Running`.
         
         NAME        READY   STATUS    RESTARTS   AGE
         hello-pod   1/1     Running   0          15s
         




### Creating a Deployment

  1. To use a private repository in a Deployment, you specify the `imagePullSecret` inside the template.

For example, to configure a [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) that uses the `hello-app` image, create a file named `hello-deployment.yaml` with the following contents:
         
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
               imagePullSecrets:
               - name: registry-secret
         

**Note:** `imagePullSecrets` must have the same level of indentation as `containers`.

Replace the following:

     * `LOCATION`
     * `PROJECT_NAME`
  2. Apply the configuration to your cluster with `kubectl`.
         
         kubectl apply -f hello-deployment.yaml
         

  3. Confirm that your Deployment is running with `kubectl pods`.
         
         kubectl get pods --selector=app=products
         

The output displays three `Running` pods.
         
         NAME                                    READY   STATUS    RESTARTS   AGE
         hello-app-deployment-67d9c6d98c-b69f2   1/1     Running   0          14m
         hello-app-deployment-67d9c6d98c-d6k5c   1/1     Running   0          14m
         hello-app-deployment-67d9c6d98c-p2md5   1/1     Running   0          14m
         




## Clean up

To remove the resources you created on this page, run these commands:
    
    
    kubectl apply -f hello-pod.yaml
    kubectl delete -f hello-deployment.yaml
    

## What's next

  * Read the [Artifact Registry overview](https://docs.cloud.google.com/artifact-registry/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
