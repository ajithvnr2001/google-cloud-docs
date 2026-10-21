---
url: https://docs.cloud.google.com/kubernetes-engine/docs/learn/containers/
title: Introducing containers \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:44.316992+00:00
---

# Introducing containers  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/learn/containers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Introducing containers Stay organized with collections  Save and categorize content based on your preferences. 

If you're not familiar with containerized workloads at all, this tutorial is for you. It introduces you to containers and container orchestration by walking you through setting up a simple application from source code to a container running on GKE.

This tutorial doesn't require any previous experience with containers or Kubernetes. However, if you want to read an overview of core Kubernetes terminology before starting this tutorial, see [Start learning about Kubernetes](https://docs.cloud.google.com/kubernetes-engine/docs/learn/get-started-with-kubernetes) (or if you'd prefer to learn about Kubernetes in comic form, see our [Kubernetes comic](https://cloud.google.com/kubernetes-engine/kubernetes-comic). You'll find more detailed resources in the What's next section at the end of the tutorial.

If you're already familiar with containers and Kubernetes, you can skip this tutorial and [start learning about GKE itself](https://docs.cloud.google.com/kubernetes-engine/docs/learn#gke).

**GKE or Cloud Run?** GKE isn't Google Cloud's only way to run containerized applications. _Cloud Run_ is a serverless platform that also lets you run containerized workloads — "serverless" means that the container runs directly on Google Cloud infrastructure rather than on Kubernetes clusters. Each option offers different advantages, and caters to different levels of workload complexity. To learn more about the differences between these container platforms and when you might want to use one, the other, or both for your applications, see [GKE and Cloud Run](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-and-cloud-run). 

## Objectives

  1. Explore a simple multi-service "hello world" application.
  2. Run the application from source.
  3. Containerize the application.
  4. Create a Kubernetes cluster.
  5. Deploy the containers to the cluster.



## Before you begin

Take the following steps to enable the Kubernetes Engine API: 

  1. Visit the [ Kubernetes Engine page](https://console.cloud.google.com/projectselector/kubernetes) in the Google Cloud console. 
  2. Create or select a project. 
  3. Wait for the API and related services to be enabled. This can take several minutes. 
  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 




### Prepare Cloud Shell

This tutorial uses [Cloud Shell](https://docs.cloud.google.com/shell/docs), which provisions a [g1-small Compute Engine](https://docs.cloud.google.com/compute/docs/machine-types) virtual machine (VM) running a Debian-based Linux operating system.

Using Cloud Shell has the following advantages:

  * A Python 3 development environment (including `virtualenv`) is fully setup.
  * The `gcloud`, `docker`, `git`, and `kubectl` command-line tools used in this tutorial are already installed.
  * You have your choice of built-in [text editors](https://docs.cloud.google.com/shell/docs/features#tools):

    * [Cloud Shell Editor](https://docs.cloud.google.com/shell/docs/features#code_editor), which you access by clicking edit **Open Editor** at the top of the Cloud Shell window.

    * Emacs, Vim, or Nano, which you access from the command-line in Cloud Shell.




In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

## Download the sample code

  1. Download the `helloserver` source code:
         
         git clone https://github.com/GoogleCloudPlatform/anthos-service-mesh-samples
         

  2. Change to the sample code directory:
         
         cd anthos-service-mesh-samples/docs/helloserver
         




## Explore the multi-service application

The sample application is written in Python. It has the following components that communicate using [REST](https://wikipedia.org/wiki/Representational_state_transfer):

  * `server`: A basic server with one `GET` endpoint, `/` , that prints "hello world" to the terminal window.
  * `loadgen`: A script that sends traffic to the `server`, with a configurable number of requests per second (RPS).



![Sample application](https://docs.cloud.google.com/static/service-mesh/docs/images/helloserver-loadgen.svg)

### Run the application from source

To get familiar with the sample application, run it in Cloud Shell:

  1. From the `sample-apps/helloserver` directory, run the `server`:
         
         python3 server/server.py
         

On startup, the `server` displays the following:
         
         INFO:root:Starting server...
         

  2. Open another terminal window so that you can send requests to the `server`. To do this in Cloud Shell, click add **Open a new tab** to open another session.

  3. In the new terminal window, send a request to the `server`:
         
         curl http://localhost:8080
         

The output from `server` is the following:
         
         Hello World!
         

  4. In the same tab, change to the directory that contains the `loadgen` script:
         
         cd anthos-service-mesh-samples/docs/helloserver/loadgen

  5. Create the following environment variables:
         
         export SERVER_ADDR=http://localhost:8080
         export REQUESTS_PER_SECOND=5
         

  6. Start `virtualenv`:
         
         virtualenv --python python3 env
         

  7. Activate the virtual environment:
         
         source env/bin/activate
         

  8. Install the requirements for `loadgen`:
         
         pip3 install -r requirements.txt
         

  9. Run the `loadgen` application to generate traffic for the `server`:
         
         python3 loadgen.py
         

On startup, the output from `loadgen` is similar to the following:
         
         Starting loadgen: 2024-10-11 09:49:51.798028
         5 request(s) complete to http://localhost:8080
         

  10. Now open the terminal window that's running the `server`. You should see messages similar to the following:
         
         127.0.0.1 - - [11/Oct/2024 09:51:28] "GET / HTTP/1.1" 200 -
         INFO:root:GET request,
         Path: /
         Headers:
         Host: localhost:8080
         User-Agent: python-requests/2.32.3
         Accept-Encoding: gzip, deflate
         Accept: */*
         Connection: keep-alive
         

From a networking perspective, the entire application is now running on the same host, which lets you use `localhost` to send requests to the `server`.

  11. To stop the `loadgen` and the `server`, press `Ctrl-c` in each terminal window.

  12. In the `loadgen` terminal window, deactivate the virtual environment:
         
         deactivate
         




## Containerize the application

To run the application on GKE, you need to package both the components of the sample application into [containers](https://docs.cloud.google.com/containers). A _container_ is a package that contains all of the necessary elements for your application to run in any environment. This tutorial uses [Docker](https://docs.docker.com/get-started/docker-overview/) to containerize the application.

To containerize the application with Docker, you need a `Dockerfile`. A `Dockerfile` is a text file that defines the commands needed to assemble the application source code and its dependencies into a container _image_. After you build the image, you upload it to a container registry, such as [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview).

The source code for this tutorial includes a `Dockerfile` for both the `server` and the `loadgen` with all the commands required to build the images. The following is the `Dockerfile` for the `server`:
    
    
    FROM python:3.14-slim as base
    FROM base as builder
    RUN apt-get -qq update \
        && apt-get install -y --no-install-recommends \
            g++ \
        && rm -rf /var/lib/apt/lists/*
    
    # Enable unbuffered logging
    FROM base as final
    ENV PYTHONUNBUFFERED=1
    
    RUN apt-get -qq update \
        && apt-get install -y --no-install-recommends \
            wget
    
    WORKDIR /helloserver
    
    # Grab packages from builder
    COPY --from=builder /usr/local/lib/python3.* /usr/local/lib/
    
    # Add the application
    COPY . .
    
    EXPOSE 8080
    ENTRYPOINT [ "python", "server.py" ]
    

In this file, you can see the following:

  * The `FROM python:3-slim as base` instruction tells Docker to use the latest [Python 3 image](https://hub.docker.com/_/python) as the base image.
  * The `COPY . .` instruction copies the source files from the current working directory (in this case, `server.py`) to the container's file system.
  * The `ENTRYPOINT` defines the instruction that is used to run the container. In this example, the instruction is similar to the one you used to run `server.py` from the source code.
  * The `EXPOSE` instruction specifies that the `server` listens on port `8080`. This instruction doesn't [expose any ports](https://docs.docker.com/engine/reference/builder/#expose), but serves as documentation that you need to open port `8080` when you run the container.



### Prepare to containerize the application

Before you containerize the application, you need to do some setup for the tools and services that you're going to use:

  1. Set the default Google Cloud project for the Google Cloud CLI.
         
         gcloud config set project PROJECT_ID

  2. Set the default region for the Google Cloud CLI.
         
         gcloud config set compute/region us-central1
         




#### Create the repository

To create a new repository for Docker container images in Artifact Registry, do the following:

  1. Make sure that the Artifact Registry service is enabled in your Google Cloud project.
         
         gcloud services enable artifactregistry.googleapis.com
         
         

  2. Create the Artifact Registry repository:
         
         gcloud artifacts repositories create container-intro --repository-format=docker \
             --location=us-central1 \
             --description="My new Docker repository"
         

  3. Set up authentication from Docker to Artifact Registry using the Google Cloud CLI:
         
         gcloud auth configure-docker us-central1-docker.pkg.dev
         




### Containerize the `server`

Now it's time to containerize your application. First containerize the "hello world" `server` and push the image to Artifact Registry:

  1. Change to the directory where the sample `server` is located:
         
         cd ~/anthos-service-mesh-samples/docs/helloserver/server/

  2. Build the image using the `Dockerfile`:
         
         docker build -t us-central1-docker.pkg.dev/PROJECT_ID/container-intro/helloserver:v0.0.1 .
         

     * Replace `PROJECT_ID` with the ID of your Google Cloud project.

The `-t` flag represents the Docker tag. This is the name of the image that you use when you deploy the container.

  3. Push the image to Artifact Registry:
         
         docker push us-central1-docker.pkg.dev/PROJECT_ID/container-intro/helloserver:v0.0.1
         




### Containerize the `loadgen`

Next, containerize the load generator service in the same way:

  1. Change to the directory where the sample `loadgen` is located:
         
         cd ../loadgen
         

  2. Build the image:
         
         docker build -t us-central1-docker.pkg.dev/PROJECT_ID/container-intro/loadgen:v0.0.1 .
         

  3. Push the image to Artifact Registry:
         
         docker push us-central1-docker.pkg.dev/PROJECT_ID/container-intro/loadgen:v0.0.1
         




### List the images

Get a list of the images in the repository to confirm that the images were pushed:
    
    
    gcloud container images list --repository us-central1-docker.pkg.dev/PROJECT_ID/container-intro
    

The output should list the image names that you pushed, similar to the following:
    
    
    NAME
    us-central1-docker.pkg.dev/PROJECT_ID/container-intro/helloserver
    us-central1-docker.pkg.dev/PROJECT_ID/container-intro/loadgen
    

## Create a GKE cluster

At this point you could just run the containers on the Cloud Shell VM by using the `docker run` command. However, to run reliable production workloads you need to manage containers in a more unified way. For example, you need to make sure that the containers restart if they fail, and you need a way to scale up and start additional instances of a container to handle traffic increases.

[GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) can help you meet these needs. GKE is a container orchestration platform that works by connecting VMs into a _cluster_. Each VM is referred to as a _node_. GKE clusters are powered by the Kubernetes open source cluster management system. Kubernetes provides the mechanisms through which you interact with your cluster.

To run the containers on GKE, you first need to create and then connect to a cluster:

  1. Create the cluster:
         
         gcloud container clusters create-auto container-intro
         

The `gcloud` command creates a cluster in the default Google Cloud project and region that you set previously.

The command to create the cluster takes a few minutes to complete. When the cluster is ready, the output is similar to the following:
         
         NAME: container-intro
          LOCATION: us-central1
          MASTER_VERSION: 1.30.4-gke.1348000
          MASTER_IP: 34.44.14.166
          MACHINE_TYPE: e2-small
          NODE_VERSION: 1.30.4-gke.1348000
          NUM_NODES: 3
          STATUS: RUNNING
         

  2. Provide credentials to the [`kubectl`](https://kubernetes.io/docs/reference/kubectl/overview/) command- line tool so that you can use it to manage the cluster:
         
         gcloud container clusters get-credentials container-intro
         




## Examine Kubernetes manifests

When you ran the application from the source code, you used an imperative command: `python3 server.py`

Imperative means verb-driven: "do this."

By contrast, Kubernetes operates on a [declarative model](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-workloads-overview#declarative_object_configuration). This means that rather than telling Kubernetes exactly what to do, you provide Kubernetes with a desired state. For example, Kubernetes starts and terminates Pods as needed so that the actual system state matches the desired state.

You specify the desired state in a file called a manifest. Manifests are written in languages like [YAML](https://wikipedia.org/wiki/YAML) or JSON and contain the specification for one or more Kubernetes objects.

The sample contains a manifest each for the `server` and `loadgen`. Each manifest specifies the desired state for the Kubernetes Deployment object (which manages running your container, packaged for management as a Kubernetes Pod) and Service (which provides an IP address for the Pod). A Pod is the smallest deployable unit of computing that you can create and manage in Kubernetes, and holds one or more containers.

The following diagram depicts the application running on GKE:

![Containerized application running on
GKE](https://docs.cloud.google.com/static/service-mesh/docs/images/gke-pods.svg)

You can learn more about Pods, Deployments, and Services in [Start learning about Kubernetes](https://docs.cloud.google.com/kubernetes-engine/docs/learn/get-started-with-kubernetes), or in the resources at the end of this page.

### Server

First, look at the manifest for the "hello world" `server`:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: helloserver
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: helloserver
      template:
        metadata:
          labels:
            app: helloserver
        spec:
          containers:
          - image: gcr.io/google-samples/istio/helloserver:v0.0.1
            imagePullPolicy: Always
            name: main
          restartPolicy: Always
          terminationGracePeriodSeconds: 5

This manifest contains the following fields:

  * `kind` indicates the type of object.
  * `metadata.name` specifies the name of the Deployment.
  * The first `spec` field contains a description of the desired state.
  * `spec.replicas` specifies the number of desired Pods.
  * The `spec.template` section defines a Pod template. Included in the specification for the Pods is the `image` field, which is the name of the image to pull from Artifact Registry. In the next step, you'll update this to the new image that you just created.



The `hellosvc` Service is defined as follows:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: hellosvc
    spec:
      ports:
      - name: http
        port: 80
        targetPort: 8080
      selector:
        app: helloserver
      type: LoadBalancer

  * `LoadBalancer`: Clients send requests to the IP address of a network load balancer, which has a stable IP address and is reachable outside of the cluster.
  * `targetPort`: Recall that the `EXPOSE 8080` command in the `Dockerfile` doesn't actually expose any ports. You expose port `8080` so that you can reach the `server` container outside of the cluster. In this case, `hellosvc.default.cluster.local:80` (shortname: `hellosvc`) maps to the `helloserver` Pod IP's port `8080`.
  * `port`: This is the port number that other services in the cluster use when sending requests.



### Load generator

The Deployment object in `loadgen.yaml` is similar to `server.yaml`. One notable difference is that the Pod specification for the `loadgen` Deployment has a field called `env`. This section defines the environment variables that are required by `loadgen`, which you set previously when you ran the application from source.
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: loadgenerator
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: loadgenerator
      template:
        metadata:
          labels:
            app: loadgenerator
        spec:
          containers:
          - env:
            - name: SERVER_ADDR
              value: http://hellosvc:80/
            - name: REQUESTS_PER_SECOND
              value: '10'
            image: gcr.io/google-samples/istio/loadgen:v0.0.1
            imagePullPolicy: Always
            name: main
            resources:
              limits:
                cpu: 500m
                memory: 512Mi
              requests:
                cpu: 300m
                memory: 256Mi
          restartPolicy: Always
          terminationGracePeriodSeconds: 5

Because the `loadgen` doesn't accept incoming requests, the `type` field is set to `ClusterIP`. This type of Service provides a stable IP address that entities in the cluster can use, but the IP address isn't exposed to external clients.
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: loadgensvc
    spec:
      ports:
      - name: http
        port: 80
        targetPort: 8080
      selector:
        app: loadgenerator
      type: ClusterIP

## Deploy the containers to GKE

To deploy the containers, you _apply_ the manifests that specify your desired state by using `kubectl`.

### Deploy the `server`

  1. Change to the directory where the sample `server` is located:
         
         cd ~/anthos-service-mesh-samples/docs/helloserver/server/

  2. Open `server.yaml` in the [Cloud Shell Editor](https://docs.cloud.google.com/shell/docs/features#code_editor) (or your preferred text editor).

  3. Replace the name in the `image` field with the name of your Docker image.
         
         image: us-central1-docker.pkg.dev/PROJECT_ID/container-intro/helloserver:v0.0.1
         

Replace PROJECT_ID with your Google Cloud project ID.

     * If you are using Cloud Shell Editor, the file is saved automatically. Go back to the terminal window by clicking **Open terminal**.
     * If you are using a text editor in Cloud Shell, save and close `server.yaml`.
  4. Deploy the manifest to Kubernetes:
         
         kubectl apply -f server.yaml
         

The output is similar to the following: 
         
         deployment.apps/helloserver created
         service/hellosvc created
         




### Deploy the `loadgen`

  1. Change to the directory where `loadgen` is located.
         
         cd ../loadgen
         

  2. Open `loadgen.yaml` in a text editor, as before.

  3. Again, replace the name in the `image` field with the name of your Docker image.
         
         image: us-central1-docker.pkg.dev/PROJECT_ID/container-intro/loadgen:v0.0.1
         

Replace PROJECT_ID with your Google Cloud project ID.

     * If you are using Cloud Shell Editor, the file is saved automatically. Go back to the terminal window by clicking **Open terminal**.
     * If you are using a text editor in Cloud Shell, save and close `loadgen.yaml`.
  4. Deploy the manifest to your cluster:
         
         kubectl apply -f loadgen.yaml
         

On success, the command responds with the following: 
         
         deployment.apps/loadgenerator created
         service/loadgensvc created
         




### Verify your deployment

After deploying your manifests to the cluster, verify that your containers have been deployed successfully:

  1. Check the status of the Pods in your cluster:
         
         kubectl get pods
         

The command responds with the status similar to the following:
         
         NAME                             READY   STATUS    RESTARTS   AGE
         helloserver-69b9576d96-mwtcj     1/1     Running   0          58s
         loadgenerator-774dbc46fb-gpbrz   1/1     Running   0          57s
         

  2. Get the application logs from the `loadgen` Pod. Replace POD_ID with the load generator Pod identifier from the previous output.
         
         kubectl logs POD_ID
         

  3. Get the external IP addresses of `hellosvc`:
         
         kubectl get service hellosvc
         

The output is similar to the following:
         
         NAME         TYPE           CLUSTER-IP     EXTERNAL-IP     PORT(S)        AGE
         hellosvc     LoadBalancer   10.81.15.158   192.0.2.1       80:31127/TCP   33m
         

  4. Send a request to the `hellosvc`. Replace EXTERNAL_IP with the external IP address of your `hellosvc`.
         
         curl http://EXTERNAL_IP
         

You should see a "Hello World!" message from the server.


**Success:** You just containerized a microservices-based application and deployed it to GKE!

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

If you don't want to delete the entire project:

  * Delete the GKE cluster. Deleting the cluster deletes all the resources that make up the cluster, such as the Compute Engine instances, disks, and network resources.
        
        gcloud container clusters delete container-intro
        

  * Delete the Artifact Registry repository:
        
        gcloud artifacts repositories delete container-intro --location=us-central1
        




## What's next

  * Learn more about the technologies used in this tutorial:

    * [Containers](https://docs.cloud.google.com/containers)
    * [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs)
    * [Kubernetes](https://kubernetes.io/)
    * [GKE](https://docs.cloud.google.com/kubernetes-engine/docs)
    * [Docker](https://docs.docker.com/get-started/)
  * Learn more about the tools:

    * [gcloud CLI](https://docs.cloud.google.com/sdk/docs/how-to)
    * [`gcloud` reference](https://docs.cloud.google.com/sdk/gcloud/reference)
    * [`kubectl`](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
    * [`docker`](https://docs.docker.com/engine/reference/commandline/cli/)
  * Learn more about Kubernetes concepts:

    * [Clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture)
    * [Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#nodes)
    * [Pods](https://kubernetes.io/docs/concepts/workloads/pods)
    * [Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service)
    * [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
