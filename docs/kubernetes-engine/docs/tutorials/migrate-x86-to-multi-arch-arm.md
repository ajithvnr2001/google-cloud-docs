---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/migrate-x86-to-multi-arch-arm/
title: Migrate x86 application on GKE to multi-arch with Arm \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:16.049709+00:00
---

# Migrate x86 application on GKE to multi-arch with Arm  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/migrate-x86-to-multi-arch-arm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Migrate x86 application on GKE to multi-arch with Arm Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Note** : This tutorial provides instructions for working with this app: Docker. The instructions might not represent newer versions of the app. For more information, see the documentation: [Docker](https://docs.docker.com/). 

This tutorial describes how to migrate an application built for nodes using an x86 (Intel or AMD) processor in a Google Kubernetes Engine (GKE) cluster to a multi-architecture (multi-arch) application that runs on either x86 or Arm nodes. The intended audience for this tutorial is Platform Admins, App Operators, and App Developers who want to run their existing x86-compatible workloads on Arm.

With GKE clusters, you can run workloads on Arm nodes using the [C4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series), [N4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_series), or [Tau T2A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2a_machines) machine series. This tutorial uses C4A nodes, which, like N4A and T2A nodes, can run in your GKE cluster just like any other node using x86 (Intel or AMD) processors. C4A nodes provide Arm-based consistently high performance for your workloads.

For more information, see [Arm workloads on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke).

This tutorial assumes that you are familiar with Kubernetes and Docker. The tutorial uses Google Kubernetes Engine and Artifact Registry.

## Objectives

In this tutorial, you will complete the following tasks:

  * Store container images with Docker in Artifact Registry.
  * Deploy an x86-compatible workload to a GKE cluster.
  * Rebuild an x86-compatible workload to run on Arm.
  * Add an Arm node pool to an existing cluster.
  * Deploy an Arm-compatible workload to run on an Arm node.
  * Build a multi-arch image to run a workload across multiple architectures.
  * Run workloads across multiple architectures in one GKE cluster.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ GKE](https://docs.cloud.google.com/kubernetes-engine/pricing)
  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

Take the following steps to enable the Kubernetes Engine API: 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Artifact Registry and Google Kubernetes Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,container.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Artifact Registry and Google Kubernetes Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,container.googleapis.com)




When you finish this tutorial, you can avoid continued billing by deleting the resources you created. See Clean up for more details.

## Launch Cloud Shell

In this tutorial you will use [Cloud Shell](https://docs.cloud.google.com/shell/docs), which is a shell environment for managing resources hosted on Google Cloud.

Cloud Shell comes preinstalled with the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) and [`kubectl`](https://kubernetes.io/docs/reference/kubectl/) command-line tool. The gcloud CLI provides the primary command-line interface for Google Cloud, and `kubectl` provides the primary command-line interface for running commands against Kubernetes clusters.

Launch Cloud Shell:

  1. Go to the Google Cloud console.

[Google Cloud console](https://console.cloud.google.com/)

  2. From the upper-right corner of the console, click the **Activate Cloud Shell** button: ![](https://docs.cloud.google.com/static/kubernetes-engine/images/cloud-shell.png)




A Cloud Shell session appears inside the console. You use this shell to run `gcloud` and `kubectl` commands.

## Prepare your environment

In this section, you prepare your environment to follow the tutorial.

### Set the default settings for the gcloud CLI

Set environment variables for your project ID, the Compute Engine location for your cluster, and the name of your new cluster.

**Caution:** The following environment variables are used throughout the commands of this tutorial. You might need to set the environment variables again if you close the Cloud Shell.
    
    
    export PROJECT_ID=PROJECT_ID
    export CONTROL_PLANE_LOCATION=us-central1-a
    export CLUSTER_NAME=my-cluster
    

Replace `PROJECT_ID` with the project ID you chose for this tutorial in the Before you begin section.

In this tutorial, you create resources in us-central1-a. To see a complete list of where the C4A machine series is available, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).

### Clone the git repository

  1. Clone the repository:
         
         git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples
         

  2. Change your current working directory to the repository cloned in the previous step:
         
         cd kubernetes-engine-samples/workloads/migrate-x86-app-to-multi-arch/
         

This repository contains the files you need to complete this tutorial. This tutorial uses Kubernetes Deployments. A _Deployment_ is a Kubernetes API object that lets you run multiple replicas of Pods that are distributed among the nodes in a cluster..




## Create a GKE cluster and deploy the x86 application

In the first part of this tutorial, you create a cluster with x86 nodes and deploy an x86 application. The example application is a service which responds to HTTP requests. It is built with the Golang programming language.

This setup represents what a typical cluster environment might look like, using x86-compatible applications and x86 nodes.

### Create a GKE cluster

First, create a GKE using nodes with x86 processors. With this configuration, you create a typical cluster environment to run x86 applications.

Create the cluster:
    
    
    gcloud container clusters create $CLUSTER_NAME \
        --release-channel=rapid \
        --location=$CONTROL_PLANE_LOCATION \
        --machine-type=e2-standard-2 \
        --num-nodes=1 \
        --async
    

This cluster has autoscaling disabled in order to demonstrate specific functionality in later steps.

It might take several minutes to finish creating the cluster. The `--async` flag lets this operation run in the background while you complete the next steps.

You can [create clusters with only Arm nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/create-arm-clusters-nodes#create-cluster-arm-node-pool), however for this tutorial you will create a cluster with only x86 nodes first to learn about the process of making x86-only applications compatible with Arm.

### Create the Artifact Registry Docker repository

  1. Create a repository in Artifact Registry to store Docker images:
         
         gcloud artifacts repositories create docker-repo \
               --repository-format=docker \
               --location=us-central1 \
               --description="Docker repository"
         

  2. Configure the Docker command-line tool to authenticate to this repository in Artifact Registry:
         
         gcloud auth configure-docker us-central1-docker.pkg.dev
         




### Build the x86 image and push it to Artifact Registry

  1. Build the x86-compatible version of the application:
         
         docker build -t us-central1-docker.pkg.dev/$PROJECT_ID/docker-repo/x86-hello:v0.0.1 .
         

  2. Push the image to Artifact Registry:
         
         docker push us-central1-docker.pkg.dev/$PROJECT_ID/docker-repo/x86-hello:v0.0.1
         




### Deploy the x86 application

  1. Check that the cluster is ready by running the following script:
         
         echo
         echo -ne "Waiting for GKE cluster to finish provisioning"
         gke_status=""
         while [ -z $gke_status ]; do
            sleep 2
            echo -ne '.'
            gke_status=$(gcloud container clusters list --format="value(STATUS)" --filter="NAME=$CLUSTER_NAME AND STATUS=RUNNING")
         done
         echo
         echo "GKE Cluster '$CLUSTER_NAME' is $gke_status"
         echo
         

When the cluster is ready, the output should be similar to the following:
         
         GKE Cluster 'my-cluster' is RUNNING
         

  2. Retrieve the cluster credentials so that `kubectl` can connect to the Kubernetes API for the cluster:
         
         gcloud container clusters get-credentials $CLUSTER_NAME --location $CONTROL_PLANE_LOCATION --project $PROJECT_ID
         

  3. Update the image using [kustomize](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/) and deploy the x86 application:
         
         $(cd k8s/overlays/x86 && kustomize edit set image hello=us-central1-docker.pkg.dev/$PROJECT_ID/docker-repo/x86-hello:v0.0.1)
         kubectl apply -k k8s/overlays/x86
         

  4. Deploy a Service to expose the application to the Internet:
         
         kubectl apply -f k8s/hello-service.yaml
         

  5. Check that the external IP address for the Service, `hello-service`, is finished provisioning:
         
         echo
         echo -ne "Waiting for External IP to be provisioned"
         external_ip=""
         while [ -z $external_ip ]; do
            sleep 2
            echo -ne '.'
            external_ip=$(kubectl get svc hello-service --template="{{range .status.loadBalancer.ingress}}{{.ip}}{{end}}")
         done
         echo
         echo "External IP: $external_ip"
         echo
         

After the external IP address is provisioned, the output should be similar to the following:
         
         External IP: 203.0.113.0
         

  6. Make an HTTP request to test that the deployment works as expected:
         
         curl -w '\n' http://$external_ip
         

The output is similar to the following:
         
         Hello from NODE:gke-my-cluster-default-pool-32019863-b41t, POD:x86-hello-deployment-6b7b456dd5-mwfkd, CPU PLATFORM:linux/amd64
         

The output shows that this x86-compatible deployment is running on a node in the default node pool on the `amd64` architecture. The nodes in the default node pool of your cluster have x86 (either Intel or AMD) processors.




## Add Arm nodes to the cluster

In the next part of this tutorial, add Arm nodes to your existing cluster. These nodes are where the Arm-compatible version of your application is deployed when it's rebuilt to run on Arm.

### Checkpoint

So far you've accomplished the following objectives:

  * create a GKE cluster using x86 nodes.
  * store an x86-compatible container image with Docker in Artifact Registry.
  * deploy an x86-compatible workload to a GKE cluster.



You've configured a cluster environment with x86 nodes and an x86-compatible workload. This configuration is similar to your existing cluster environments if you don't currently use Arm nodes and Arm-compatible workloads.

### Add an Arm node pool to your cluster

Add an Arm node pool to your existing cluster:
    
    
    gcloud container node-pools create arm-pool \
        --cluster $CLUSTER_NAME \
        --location $CONTROL_PLANE_LOCATION \
        --machine-type=c4a-standard-2 \
        --num-nodes=1
    

The `c4a-standard-2` machine type is an Arm VM from the [C4A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series).

You create a node pool with Arm nodes in the same way as creating a node pool with x86 nodes. After this node pool is created, you will have both x86 nodes and Arm nodes running in this cluster.

For more information about adding Arm node pools to existing clusters, see [Add an Arm node pool to a GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/create-arm-clusters-nodes#create-arm-node-pool).

### Scale up the existing application running on x86-based nodes

Nodes of multiple architecture types can work seamlessly together in one cluster. GKE doesn't, by default, schedule existing workloads running on x86 nodes to Arm nodes in the cluster because a taint is automatically placed on Arm nodes. However, if you want GKE to schedule x86-compatible workloads that don't have a corresponding toleration to Arm nodes, you can configure your node pools so that GKE doesn't add the taint. For more information, see [Configure the default Arm architecture taint](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-arm-workloads-for-deployment#configure-default-taint).

Scale up your existing application to see the effect of the default taint:

  1. Update the workload, scaling it up to 6 replicas:
         
         $(cd k8s/overlays/x86_increase_replicas && kustomize edit set image hello=us-central1-docker.pkg.dev/$PROJECT_ID/docker-repo/x86-hello:v0.0.1)
         kubectl apply -k k8s/overlays/x86_increase_replicas/
         

  2. Wait 30 seconds, then run the following command to check the status of the deployment:
         
         kubectl get pods -l="app=hello" --field-selector="status.phase=Pending"
         

The output should look similar to the following:
         
         NAME                                    READY   STATUS    RESTARTS   AGE
         x86-hello-deployment-6b7b456dd5-6tkxd   0/1     Pending   0          40s
         x86-hello-deployment-6b7b456dd5-k95b7   0/1     Pending   0          40s
         x86-hello-deployment-6b7b456dd5-kc876   0/1     Pending   0          40s
         

This output shows Pods with a Pending status as there is no room left on the x86-based nodes. Since Cluster Autoscaler is disabled and the Arm nodes are tainted by default, the workloads won't be deployed on any of the available Arm nodes. This taint prevents GKE from scheduling x86 workloads on Arm nodes. To deploy to Arm nodes, you must indicate that the deployment is compatible with Arm nodes. Or, you can configure GKE to remove the default taint.

  3. Check the Pods that are in the Running state:
         
         kubectl get pods -l="app=hello" --field-selector="status.phase=Running" -o wide
         

The output should look similar to the following:
         
         NAME                                    READY   STATUS    RESTARTS   AGE   IP            NODE                                        NOMINATED NODE   READINESS GATES
         x86-hello-deployment-6b7b456dd5-cjclz   1/1     Running   0          62s   10.100.0.17   gke-my-cluster-default-pool-32019863-b41t   <none>           <none>
         x86-hello-deployment-6b7b456dd5-mwfkd   1/1     Running   0          34m   10.100.0.11   gke-my-cluster-default-pool-32019863-b41t   <none>           <none>
         x86-hello-deployment-6b7b456dd5-n56rg   1/1     Running   0          62s   10.100.0.16   gke-my-cluster-default-pool-32019863-b41t   <none>           <none>
         

In this output, the `NODE` column indicates that all Pods from the deployment are running only in the default-pool, meaning that the x86-compatible Pods are only scheduled to the x86 nodes. The original Pod that was already scheduled before the creation of the Arm node pool is still running on the same node.

  4. Run the following command to access the service and see the output:
         
         for i in $(seq 1 6); do curl -w '\n' http://$external_ip; done
         

The output is similar to the following:
         
         Hello from NODE:gke-my-cluster-default-pool-32019863-b41t, POD:x86-hello-deployment-6b7b456dd5-cjclz, CPU PLATFORM:linux/amd64
         Hello from NODE:gke-my-cluster-default-pool-32019863-b41t, POD:x86-hello-deployment-6b7b456dd5-cjclz, CPU PLATFORM:linux/amd64
         Hello from NODE:gke-my-cluster-default-pool-32019863-b41t, POD:x86-hello-deployment-6b7b456dd5-n56rg, CPU PLATFORM:linux/amd64
         Hello from NODE:gke-my-cluster-default-pool-32019863-b41t, POD:x86-hello-deployment-6b7b456dd5-n56rg, CPU PLATFORM:linux/amd64
         Hello from NODE:gke-my-cluster-default-pool-32019863-b41t, POD:x86-hello-deployment-6b7b456dd5-cjclz, CPU PLATFORM:linux/amd64
         Hello from NODE:gke-my-cluster-default-pool-32019863-b41t, POD:x86-hello-deployment-6b7b456dd5-cjclz, CPU PLATFORM:linux/amd64
         

This output shows that all Pods serving requests are running on x86 nodes. Some Pods cannot respond because they are still in the Pending state as there is no space on the existing x86 nodes and they will not be scheduled to Arm nodes.




## Rebuild your application to run on Arm

In the previous section, you added an Arm node pool to your existing cluster. However, when you scaled up the existing x86 application, it did not schedule any of the workloads to the Arm nodes. In this section, you rebuild your application to be Arm-compatible, so that this application can run on the Arm nodes in the cluster.

For this example, accomplish these steps by using [`docker build`](https://docs.docker.com/engine/reference/commandline/build/). This two-step approach includes:

  * **First stage** : Build the code to Arm.
  * **Second stage** : Copy the executable to a lean container.



After following these steps, you will have an Arm-compatible image in addition to the x86-compatible image.

The second step of copying the executable to another container follows one of the best practices for building a container, which is to build the smallest image possible.

This tutorial uses an example application built with the Golang programming language. With Golang, you can cross-compile an application to different operating systems and CPU platforms by providing environment variables, `GOOS` and `GOARCH`, respectively.

  1. Run `cat Dockerfile_arm` to see the Dockerfile written for Arm:
         
         #
         # Build: 1st stage
         #
         FROM golang:1.18-alpine as builder
         WORKDIR /app
         COPY go.mod .
         COPY hello.go .
         RUN GOARCH=arm64 go build -o /hello && \
            apk add --update --no-cache file && \
            file /hello
         

The snippet shown here shows just the first stage. In the file, both stages are included.

In this file, setting `GOARCH=arm64` instructs the Go compiler to build the application for the Arm instruction set. You do not need to set `GOOS` because the base image in the first stage is a Linux Alpine image.

  2. Build the code for Arm, and push it to Artifact Registry:
         
         docker build -t us-central1-docker.pkg.dev/$PROJECT_ID/docker-repo/arm-hello:v0.0.1 -f Dockerfile_arm .
         docker push us-central1-docker.pkg.dev/$PROJECT_ID/docker-repo/arm-hello:v0.0.1
         




### Deploy the Arm version of your application

Now that the application is built to run on Arm nodes, you can deploy it to the Arm nodes in your cluster.

  1. Inspect the `add_arm_support.yaml` by running `cat k8s/overlays/arm/add_arm_support.yaml`:

The output is similar to the following:
         
         nodeSelector:
               kubernetes.io/arch: arm64
         

This `nodeSelector` specifies that the workload should run only on the Arm nodes. When you use the `nodeSelector`, GKE [adds a toleration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-arm-workloads-for-deployment#add-toleration) that matches the default taint on Arm nodes, letting GKE schedule the workload on those nodes. For more information about setting this field, see [Prepare an Arm workload for deployment](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-arm-workloads-for-deployment).

  2. Deploy one replica of the Arm-compatible version of the application:
         
         $(cd k8s/overlays/arm && kustomize edit set image hello=us-central1-docker.pkg.dev/$PROJECT_ID/docker-repo/arm-hello:v0.0.1)
         kubectl apply -k k8s/overlays/arm
         

  3. Wait 5 seconds, then check that the Arm deployment is answering `curl` requests:
         
         for i in $(seq 1 6); do curl -w '\n' http://$external_ip; done
         

The output is similar to the following:
         
         Hello from NODE:gke-my-cluster-default-pool-32019863-b41t, POD:x86-hello-deployment-6b7b456dd5-n56rg, CPU PLATFORM:linux/amd64
         Hello from NODE:gke-my-cluster-default-pool-32019863-b41t, POD:x86-hello-deployment-6b7b456dd5-n56rg, CPU PLATFORM:linux/amd64
         Hello from NODE:gke-my-cluster-default-pool-32019863-b41t, POD:x86-hello-deployment-6b7b456dd5-mwfkd, CPU PLATFORM:linux/amd64
         Hello from NODE:gke-my-cluster-default-pool-32019863-b41t, POD:x86-hello-deployment-6b7b456dd5-mwfkd, CPU PLATFORM:linux/amd64
         Hello from NODE:gke-my-cluster-arm-pool-e172cff7-shwc, POD:arm-hello-deployment-69b4b6bdcc-n5l28, CPU PLATFORM:linux/arm64
         Hello from NODE:gke-my-cluster-default-pool-32019863-b41t, POD:x86-hello-deployment-6b7b456dd5-n56rg, CPU PLATFORM:linux/amd64
         

This output should include responses from both the x86-compatible and Arm-compatible applications responding to the `curl` request.




## Build a multi-architecture image to run a workload across architectures

While you can use the strategy described in the previous section and deploy separate workloads for x86 and Arm, this would require you to maintain and keep organized two build processes and two container images.

Ideally, you want to build and run your application seamlessly across both x86 and Arm platforms. We recommend this approach. To run your application with one manifest across multiple architecture platforms, you need to use multi-architecture (multi-arch) images. For more information about multi-architecture images, see [Build multi-arch images for Arm workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/build-multi-arch-for-arm).

To use multi-architecture images, you must ensure that your application meets the following prerequisites:

  * Your application does not have any architecture platform-specific dependencies.
  * All dependencies must be built for multi-architecture or, at minimum, the targeted platforms.



The example application used in this tutorial meets both of these prerequisites. However, we recommend testing your own applications when building their multi-arch images before deploying them to production.

### Build and push multi-architecture images

You can build multi-arch images with [Docker Buildx](https://docs.docker.com/buildx/working-with-buildx/) if your workload fulfills the following prerequisites:

  * The base image supports multiple architectures. Check this by running [`docker manifest inspect`](https://docs.docker.com/engine/reference/commandline/manifest_inspect/) on the base image and checking the list of architecture platforms. See an example of how to inspect an image at the end of this section.
  * The application does not require special build steps for each architecture platform. If special steps were required, Buildx might not be sufficient. You would need to have a separate Dockerfile for each platform and create the manifest manually with [`docker manifest create`](https://docs.docker.com/engine/reference/commandline/manifest_create/).



The example application's base image is Alpine, which supports multiple architectures. There are also no architecture platform-specific steps, so you can build the multi-arch image with Buildx.

  1. Inspect the Dockerfile by running `cat Dockerfile`:
         
         # This is a multi-stage Dockerfile.
         # 1st stage builds the app in the target platform
         # 2nd stage create a lean image coping the binary from the 1st stage
         
         #
         # Build: 1st stage
         #
         FROM golang:1.18-alpine as builder
         ARG BUILDPLATFORM
         ARG TARGETPLATFORM
         RUN echo "I am running on $BUILDPLATFORM, building for $TARGETPLATFORM"
         WORKDIR /app
         COPY go.mod .
         COPY hello.go .
         RUN go build -o /hello && \
            apk add --update --no-cache file && \
            file /hello
         
         #
         # Release: 2nd stage
         #
         FROM alpine
         WORKDIR /
         COPY --from=builder /hello /hello
         CMD [ "/hello" ]
         

This Dockerfile defines two stages: the build stage and release stage. You use the same Dockerfile used for building the x86 application.

  2. Run the following command to create and use a new `docker buildx` builder:
         
         docker buildx create --name multiarch --use --bootstrap
         

Now that you have created this new builder, you can build and push an image that is compatible with both `linux/amd64` and `linux/arm64` by using the `--platform` flag. For each platform provided with the flag, Buildx builds an image in the target platform. When Buildx builds the `linux/arm64` image, it downloads `arm64` base images. In the first stage, it builds the binary on the `arm64 golang:1.18-alpine` image for `arm64`. In the second stage, the `arm64` Alpine Linux image is downloaded and the binary is copied to a layer of that image.

  3. Build and push the image:
         
         docker buildx build -t us-central1-docker.pkg.dev/$PROJECT_ID/docker-repo/multiarch-hello:v0.0.1 -f Dockerfile --platform linux/amd64,linux/arm64 --push .
         

The output is similar to the following:
         
         => [linux/arm64 builder x/x] ..
         => [linux/amd64 builder x/x] ..
         

This output shows that two images are generated, one for `linux/arm64` and one for `linux/amd64`.

  4. Inspect the manifest of your new multi-arch image:
         
         docker manifest inspect us-central1-docker.pkg.dev/$PROJECT_ID/docker-repo/multiarch-hello:v0.0.1
         

The output is similar to the following:
         
         {
            "schemaVersion": 2,
            "mediaType": "application/vnd.docker.distribution.manifest.list.v2+json",
            "manifests": [
               {
                  "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
                  "size": 739,
                  "digest": "sha256:dfcf8febd94d61809bca8313850a5af9113ad7d4741edec1362099c9b7d423fc",
                  "platform": {
                     "architecture": "amd64",
                     "os": "linux"
                  }
               },
               {
                  "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
                  "size": 739,
                  "digest": "sha256:90b637d85a93c3dc03fc7a97d1fd640013c3f98c7c362d1156560bbd01f6a419",
                  "platform": {
                     "architecture": "arm64",
                     "os": "linux"
                  }
               }
            ]
         

In this output, the `manifests` section includes two manifests, one with the `amd64` platform architecture, and the other with the `arm64` platform architecture.

When you deploy this container image to your cluster, GKE automatically downloads only the image that matches the node's architecture.




### Deploy the multi-arch version of your application

  1. Before you deploy the multi-arch image, delete the original workloads:
         
         kubectl delete deploy x86-hello-deployment arm-hello-deployment
         

  2. Inspect the `add_multiarch_support.yaml` kustomize overlay by running `cat k8s/overlays/multiarch/add_multiarch_support.yaml`:

The output includes the following toleration set:
         
         tolerations:
         - key: kubernetes.io/arch
           operator: Equal
           value: arm64
           effect: NoSchedule
         

This toleration allows the workload to run on the Arm nodes in your cluster, since the toleration matches the taint set, by default, on all Arm nodes. As this workload can now run on any node in the cluster, only the toleration is needed. With just the toleration, GKE can schedule the workload to both x86 and Arm nodes. If you want to specify where GKE can schedule workloads, use node selectors and node affinity rules. For more information about setting these fields, see [Prepare an Arm workload for deployment](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-arm-workloads-for-deployment).

  3. Deploy the multi-arch container image with 6 replicas:
         
         $(cd k8s/overlays/multiarch && kustomize edit set image hello=us-central1-docker.pkg.dev/$PROJECT_ID/docker-repo/multiarch-hello:v0.0.1)
         kubectl apply -k k8s/overlays/multiarch
         

  4. Wait 10 seconds, then confirm that all of the replicas of the application are running:
         
         kubectl get pods -l="app=hello" -o wide
         

The output is similar to the following:
         
         NAME                                         READY   STATUS    RESTARTS   AGE   IP            NODE                                        NOMINATED NODE   READINESS GATES
         multiarch-hello-deployment-65bfd784d-5xrrr   1/1     Running   0          95s   10.100.1.5    gke-my-cluster-arm-pool-e172cff7-shwc       <none>           <none>
         multiarch-hello-deployment-65bfd784d-7h94b   1/1     Running   0          95s   10.100.1.4    gke-my-cluster-arm-pool-e172cff7-shwc       <none>           <none>
         multiarch-hello-deployment-65bfd784d-7qbkz   1/1     Running   0          95s   10.100.1.7    gke-my-cluster-arm-pool-e172cff7-shwc       <none>           <none>
         multiarch-hello-deployment-65bfd784d-7wqb6   1/1     Running   0          95s   10.100.1.6    gke-my-cluster-arm-pool-e172cff7-shwc       <none>           <none>
         multiarch-hello-deployment-65bfd784d-h2g2k   1/1     Running   0          95s   10.100.0.19   gke-my-cluster-default-pool-32019863-b41t   <none>           <none>
         multiarch-hello-deployment-65bfd784d-lc9dc   1/1     Running   0          95s   10.100.0.18   gke-my-cluster-default-pool-32019863-b41t   <none>           <none>
         

This output includes a `NODE` column that indicates the Pods are running on both nodes in the Arm node pool and others in the default (x86) node pool.

  5. Run the following command to access the service and see the output:
         
         for i in $(seq 1 6); do curl -w '\n' http://$external_ip; done
         

The output is similar to the following:
         
         Hello from NODE:gke-my-cluster-arm-pool-e172cff7-shwc, POD:multiarch-hello-deployment-65bfd784d-7qbkz, CPU PLATFORM:linux/arm64
         Hello from NODE:gke-my-cluster-default-pool-32019863-b41t, POD:multiarch-hello-deployment-65bfd784d-lc9dc, CPU PLATFORM:linux/amd64
         Hello from NODE:gke-my-cluster-arm-pool-e172cff7-shwc, POD:multiarch-hello-deployment-65bfd784d-5xrrr, CPU PLATFORM:linux/arm64
         Hello from NODE:gke-my-cluster-arm-pool-e172cff7-shwc, POD:multiarch-hello-deployment-65bfd784d-7wqb6, CPU PLATFORM:linux/arm64
         Hello from NODE:gke-my-cluster-arm-pool-e172cff7-shwc, POD:multiarch-hello-deployment-65bfd784d-7h94b, CPU PLATFORM:linux/arm64
         Hello from NODE:gke-my-cluster-arm-pool-e172cff7-shwc, POD:multiarch-hello-deployment-65bfd784d-7wqb6, CPU PLATFORM:linux/arm64
         

You should see that Pods running across architecture platforms are answering the requests.

**Note:** It is possible that you run this command and receive only responses from Pods running on one architecture platform. If this occurs, run the command once or twice more and you should responses from both architecture platforms.



You built and deployed a multi-arch image to seamlessly run a workload across multiple architectures.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

After you finish the tutorial, you can clean up the resources that you created to reduce quota usage and stop billing charges. The following sections describe how to delete or turn off these resources.

### Delete the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the service, cluster, and repository

If you don't want to delete the entire project, delete the cluster and repository that you created for the tutorial:

  1. Delete the application's Service by running [`kubectl delete`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#delete):
         
         kubectl delete service hello-service
         

This command deletes the Compute Engine load balancer that you created when you exposed the Deployment.

  2. Delete your cluster by running [`gcloud container clusters delete`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/delete):
         
         gcloud container clusters delete $CLUSTER_NAME --location $CONTROL_PLANE_LOCATION
         

  3. Delete the repository:
         
         gcloud artifacts repositories delete docker-repo —location=us-central1 --async
         




## What's next

  * [Arm workloads on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke)
  * [Create clusters and node pools with Arm nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/create-arm-clusters-nodes)
  * [Build multi-architecture images for Arm workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/build-multi-arch-for-arm)
  * [Prepare an Arm workload for deployment](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-arm-workloads-for-deployment)
  * [Prepare Autopilot workloads on Arm architecture](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-arm-workloads)
  * [Best practices for running cost-optimized Kubernetes applications on GKE](https://docs.cloud.google.com/architecture/best-practices-for-running-cost-effective-kubernetes-applications-on-gke)
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
