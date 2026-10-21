---
url: https://docs.cloud.google.com/service-mesh/v1.22/docs/prepare-app-for-anthos-service-mesh/
title: Prepare an application for Cloud Service Mesh \u00a0|\u00a0 Cloud Service Mesh v1.22 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:40.123928+00:00
---

# Prepare an application for Cloud Service Mesh  |  Cloud Service Mesh v1.22  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.22/docs/prepare-app-for-anthos-service-mesh/

You are viewing archived v1.22 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.22 ](https://docs.cloud.google.com/service-mesh/v1.22/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.22/docs/overview)



Send feedback 

#  Prepare an application for Cloud Service Mesh Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Service Mesh is a powerful tool for managing and monitoring distributed applications. To get the most out of Cloud Service Mesh, it is helpful to understand its underlying abstractions, including containers and Kubernetes. This tutorial explains how to prepare an application for Cloud Service Mesh from source code to a container running on GKE, up to the point just before installing Cloud Service Mesh.

If you're already familiar with Kubernetes and service mesh concepts, you can skip this tutorial and go straight to the Cloud Service Mesh [installation guide](https://docs.cloud.google.com/service-mesh/v1.22/docs/unified-install/install-anthos-service-mesh).

## Objectives

  1. Explore a simple multi-service "hello world" application.
  2. Run the application from source
  3. Containerize the application.
  4. Create a Kubernetes cluster.
  5. Deploy the containers to the cluster.



## Before you begin

Take the following steps to enable the Cloud Service Mesh API: 

  1. Visit the [ Kubernetes Engine page](https://console.cloud.google.com/projectselector/kubernetes) in the Google Cloud console. 
  2. Create or select a project. 
  3. Wait for the API and related services to be enabled. This can take several minutes. 
  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 




This tutorial uses Cloud Shell, which provisions a [g1-small Compute Engine](https://docs.cloud.google.com/compute/docs/machine-types) virtual machine (VM) running a Debian-based Linux operating system.

### Prepare Cloud Shell

The advantages to using [Cloud Shell](https://docs.cloud.google.com/shell/docs) are:

  * Both the Python 2 and Python 3 development environments (including `virtualenv`) are all setup.
  * The `gcloud`, `docker`, `git`, and `kubectl` command-line tools used in this tutorial are already installed.
  * You have your choice of [text editors](https://docs.cloud.google.com/shell/docs/features#tools):

    * [Code editor](https://docs.cloud.google.com/shell/docs/features#code_editor), which you access by clicking edit at the top of the Cloud Shell window.

    * Emacs, Vim, or Nano, which you access from the command line in Cloud Shell.




In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

## Download the sample code

  1. Download the `helloserver` source code:
         
         git clone https://github.com/GoogleCloudPlatform/anthos-service-mesh-samples
         

  2. Change to the sample code directory:
         
         cd anthos-service-mesh-samples/docs/helloserver
         




## Explore the multi-service application

The sample application is written in Python, and it has two components that communicate using [REST](https://wikipedia.org/wiki/Representational_state_transfer):

  * `server`: A simple server with one `GET` endpoint, `/` , that prints "hello world" to the console.
  * `loadgen`: A script that sends traffic to the `server`, with a configurable number of requests per second (RPS).



![sample application](https://docs.cloud.google.com/static/service-mesh/v1.22/docs/images/helloserver-loadgen.svg)

### Run the application from source

To get familiar with the sample application, run it in Cloud Shell.

  1. From the `sample-apps/helloserver` directory, run the `server`:
         
         python3 server/server.py
         

On startup, the `server` displays the following:
         
         INFO:root:Starting server...
         

  2. Open another terminal window so that you can send requests to the `server`. Click add to open another session.

  3. Send a request to the `server`:
         
         curl http://localhost:8080
         

The `server` responds:
         
         Hello World!
         

  4. From the directory where you downloaded the sample code, change to the directory that contains the `loadgen`:
         
         cd YOUR_WORKING_DIRECTORY/anthos-service-mesh-samples/docs/helloserver/loadgen

  5. Create the following environment variables:
         
         export SERVER_ADDR=http://localhost:8080
         export REQUESTS_PER_SECOND=5
         

  6. Start `virtualenv`:
         
         virtualenv --python python3 env
         

  7. Activate the virtual environment:
         
         source env/bin/activate
         

  8. Install the requirements for `loadgen`:
         
         pip3 install -r requirements.txt
         

  9. Run the `loadgen`:
         
         python3 loadgen.py
         

On startup, the `loadgen` outputs a message similar to the following:
         
         Starting loadgen: 2019-05-20 10:44:12.448415
         5 request(s) complete to http://localhost:8080
         

In the other terminal window, the `server` writes messages to the console similar to the following:
         
         127.0.0.1 - - [21/Jun/2019 14:22:01] "GET / HTTP/1.1" 200 -
         INFO:root:GET request,
         Path: /
         Headers:
         Host: localhost:8080
         User-Agent: python-requests/2.22.0
         Accept-Encoding: gzip, deflate
         Accept: */*
         

From a networking standpoint, the entire application is now running on the same host. For this reason you can use `localhost` to send requests to the `server`.

  10. To stop the `loadgen` and the `server`, enter `Ctrl-c` in each terminal window.

  11. In the `loadgen` terminal window, deactivate the virtual environment:
         
         deactivate
         




## Containerize the application

To run the application on GKE, you need to package the sample application—both `server` and `loadgen`—into [containers](https://docs.cloud.google.com/containers). A _container_ is a way to package an application such that it is isolated from the underlying environment.

To containerize the application, you need a `Dockerfile`. A `Dockerfile` is a text file that defines the commands needed to assemble the application source code and its dependencies into a [Docker _image_](https://docs.docker.com/get-started/). After you build the image, you upload it to a container registry, such as Docker Hub or [Container Registry](https://docs.cloud.google.com/container-registry/docs).

The sample comes with a `Dockerfile` for both the `server` and the `loadgen` with all the commands required to build the images. The following is the `Dockerfile` for the `server`:
    
    
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
    

  * The `FROM python:3-slim as base` command tells Docker to use the latest [Python 3 image](https://hub.docker.com/_/python) as the base image.
  * The `COPY . .` command copies the source files in the current working directory (in this case, just `server.py`) into the container's file system.
  * The `ENTRYPOINT` defines the command that is used to run the container. In this case, the command is almost the same as the one you used to run `server.py` from the source code.
  * The `EXPOSE` command specifies that the `server` listens on port `8080`. This command doesn't [expose any ports](https://docs.docker.com/engine/reference/builder/#expose), but serves as documentation that you need to open port `8080` when you run the container.



### Prepare to containerize the application

  1. Set the following environment variables. Replace `PROJECT_ID` with the ID of your Google Cloud project.
         
         export PROJECT_ID="PROJECT_ID"
         
         export GCR_REPO="asm-ready"

You use the value of `PROJECT_ID` and `GCR_REPO` to tag the Docker image when you build and then push it to your private Container Registry.

  2. Set the default Google Cloud project for the Google Cloud CLI.
         
         gcloud config set project $PROJECT_ID

  3. Set the default zone for the Google Cloud CLI.
         
         gcloud config set compute/zone us-central1-b
         

  4. Make sure that the Container Registry service is enabled in your Google Cloud project.
         
         gcloud services enable containerregistry.googleapis.com
         




### Containerize the `server`

  1. Change to the directory where the sample `server` is located:
         
         cd YOUR_WORKING_DIRECTORY/anthos-service-mesh-samples/docs/helloserver/server/

  2. Build the image using the `Dockerfile` and the environment variables that you defined previously:
         
         docker build -t gcr.io/$PROJECT_ID/$GCR_REPO/helloserver:v0.0.1 .
         

The `-t` flag represents the Docker tag. This is the name of the image that you use when you deploy the container.

  3. Push the image to Container Registry:
         
         docker push gcr.io/$PROJECT_ID/$GCR_REPO/helloserver:v0.0.1
         




### Containerize the `loadgen`

  1. Change to the directory where the sample `loadgen` is located:
         
         cd ../loadgen
         

  2. Build the image:
         
         docker build -t gcr.io/$PROJECT_ID/$GCR_REPO/loadgen:v0.0.1 .
         

  3. Push the image to Container Registry:
         
         docker push gcr.io/$PROJECT_ID/$GCR_REPO/loadgen:v0.0.1
         




### List the images

Get a list of the images in the repository to confirm that the images were pushed:
    
    
    gcloud container images list --repository gcr.io/$PROJECT_ID/asm-ready
    

The command responds with the image names that you just pushed:
    
    
    NAME
    gcr.io/PROJECT_ID/asm-ready/helloserver
    gcr.io/PROJECT_ID/asm-ready/loadgen
    

## Create a GKE cluster

You could run these containers on the Cloud Shell VM by using the `docker run` command. But in production, you need to orchestrate containers in a more unified way. For example, you need a system that makes sure that the containers are always running, and you need a way to scale up and start additional instances of a container to handle traffic increases.

You can use [GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) to run containerized applications. GKE is a container orchestration platform that works by connecting VMs into a _cluster_. Each VM is referred to as a _node_. GKE clusters are powered by the Kubernetes open source cluster management system. Kubernetes provides the mechanisms through which you interact with your cluster.

To create a GKE cluster:

  1. Create the cluster:
         
         gcloud container clusters create asm-ready \
           --cluster-version latest \
           --machine-type=n1-standard-4 \
           --num-nodes 4
         

The `gcloud` command creates a cluster in the Google Cloud project and zone that you set previously. To run Cloud Service Mesh, we recommend at least 4 nodes and the [n1-standard-4](https://docs.cloud.google.com/compute/docs/machine-types#general_purpose) machine type.

The command to create the cluster takes a few minutes to complete. When the cluster is ready, the command outputs a message similar to the following:
         
         NAME        LOCATION       MASTER_VERSION  MASTER_IP      MACHINE_TYPE   NODE_VERSION   NUM_NODES  STATUS
         asm-ready  us-central1-b  1.13.5-gke.10   203.0.113.1    n1-standard-2  1.13.5-gke.10  4          RUNNING
         

  2. Provide credentials to the [`kubectl`](https://kubernetes.io/docs/reference/kubectl/overview/) command- line tool so that you can use it to manage the cluster:
         
         gcloud container clusters get-credentials asm-ready
         

  3. Now you can use `kubectl` to communicate with Kubernetes. For example, you can run the following command to get the status of the nodes:
         
         kubectl get nodes
         

The command responds with a list of the nodes, similar to the following:
         
         NAME                                       STATUS   ROLES    AGE    VERSION
         gke-asm-ready-default-pool-dbeb23dc-1vg0   Ready    <none>   99s    v1.13.6-gke.13
         gke-asm-ready-default-pool-dbeb23dc-36z5   Ready    <none>   100s   v1.13.6-gke.13
         gke-asm-ready-default-pool-dbeb23dc-fj7s   Ready    <none>   99s    v1.13.6-gke.13
         gke-asm-ready-default-pool-dbeb23dc-wbjw   Ready    <none>   99s    v1.13.6-gke.13
         




## Understand key Kubernetes concepts

The following diagram depicts the application running on GKE:

![containerized application](https://docs.cloud.google.com/static/service-mesh/v1.22/docs/images/gke-pods.svg)

Before you deploy the containers to GKE, you might want to review some key Kubernetes concepts. The end of this tutorial provides links so that you can learn more about each concept.

  * **Nodes and clusters** : In GKE, a node is a VM. On other Kubernetes platforms, a node could be either a physical or virtual machine. A cluster is a set of nodes that can be treated together as a single machine, on which you deploy a containerized application.

  * **Pods** : In Kubernetes, containers run inside a _Pod_. A Pod is the atomic unit in Kubernetes. A Pod holds one or more containers. You deploy the `server` and `loadgen` containers each in their own Pod. When a Pod runs multiple containers (for example, an application server and a [proxy server](https://wikipedia.org/wiki/Proxy_server)), the containers are managed as a single entity and share the Pod's resources.

  * **Deployments** : A Deployment is a Kubernetes object that represents a set of identical Pods. A Deployment runs multiple replicas of the Pods distributed among the nodes of a cluster. A Deployment automatically replaces any Pods that fail or become unresponsive.

  * **Kubernetes Service** : Running the application code in GKE changes the networking between the `loadgen` and the `server`. When you ran the services in a Cloud Shell VM, you could send requests to the `server` using the address `localhost:8080`. After you deploy to GKE, the Pods are scheduled to run on the available nodes. By default, you can't control which node the Pod is running on, so the [Pods](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview#pods) don't have stable IP addresses.

To get an IP address for the `server`, you must define a networking abstraction on top of the Pods called a [Kubernetes Service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview#services). A Kubernetes Service provides a stable networking endpoint for a set of Pods. There are several [types of Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service#types_of_services). The `server` uses a `LoadBalancer`, which exposes an external IP address so that you can reach the `server` from outside the cluster.

Kubernetes also has a built-in DNS system, which assigns DNS names (for example, `helloserver.default.cluster.local`) to Services. This allows Pods inside the cluster to reach other Pods in the cluster with a stable address. You can't use this DNS name outside the cluster, such as from Cloud Shell.




### Kubernetes manifests

When you ran the application from the source code, you used an imperative command: `python3 server.py`

Imperative means verb-driven: "do this."

By contrast, Kubernetes operates on a [declarative model](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-workloads-overview#declarative_object_configuration). This means that rather than telling Kubernetes exactly what to do, you provide Kubernetes with a desired state. For example, Kubernetes starts and terminates Pods as needed so that the actual system state matches the desired state.

You specify the desired state in a set of manifests, or [YAML](https://wikipedia.org/wiki/YAML) files. A YAML file contains the specification for one or more Kubernetes objects.

The sample contains a YAML file for the `server` and `loadgen`. Each YAML file specifies the desired state for the Kubernetes Deployment object and Service.

#### Server
    
    
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

  * `kind` indicates the type of object.
  * `metadata.name` specifies the name of the Deployment.
  * The first `spec` field contains a description of the desired state.
  * `spec.replicas` specifies the number of desired Pods.
  * The `spec.template` section defines a Pod template. Included in the specification for the Pods is the `image` field, which is the name of the image to pull from Container Registry.



The Service is defined as follows:
    
    
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



#### Load Generator

The Deployment object in `loadgen.yaml` is similar to `server.yaml`. One notable difference is that the Deployment object contains a section called `env`. This section defines the environment variables required by `loadgen`, which you set previously when you ran the application from source.
    
    
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

Because the `loadgen` doesn't accept incoming requests, the `type` field is set to `ClusterIP`. This type provides a stable IP address that services in the cluster can use, but the IP address isn't exposed to external clients.
    
    
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

  1. Change to the directory where the sample `server` is located:
         
         cd YOUR_WORKING_DIRECTORY/anthos-service-mesh-samples/docs/helloserver/server/

  2. Open `server.yaml` in a text editor.

  3. Replace the name in the `image` field with the name of your Docker image.
         
         image: gcr.io/PROJECT_ID/asm-ready/helloserver:v0.0.1
         

Replace `PROJECT_ID` with your Google Cloud project ID.

  4. Save and close `server.yaml`.

  5. Deploy the YAML file to Kubernetes:
         
         kubectl apply -f server.yaml
         

On success, the command responds with the following: 
         
         deployment.apps/helloserver created
         service/hellosvc created
         

  6. Change to the directory where `loadgen` is located.
         
         cd ../loadgen
         

  7. Open `loadgen.yaml` in a text editor.

  8. Replace the name in the `image` field with the name of your Docker image.
         
         image: gcr.io/PROJECT_ID/asm-ready/loadgen:v0.0.1
         

Replace `PROJECT_ID` with your Google Cloud project ID.

  9. Save and close `loadgen.yaml`, and close the text editor.

  10. Deploy the YAML file to Kubernetes:
         
         kubectl apply -f loadgen.yaml
         

On success, the command responds with the following: 
         
         deployment.apps/loadgenerator created
         service/loadgensvc created
         

  11. Check the status of the Pods:
         
         kubectl get pods
         

The command responds with the status similar to the following:
         
         NAME                             READY   STATUS    RESTARTS   AGE
         helloserver-69b9576d96-mwtcj     1/1     Running   0          58s
         loadgenerator-774dbc46fb-gpbrz   1/1     Running   0          57s
         

  12. Get the application logs from the `loadgen` Pod. Replace `POD_ID` with the identifier from the previous output.
         
         kubectl logs loadgenerator-POD_ID
         

  13. Get the external IP addresses of `hellosvc`:
         
         kubectl get service
         

The command's response is similar to the following:
         
         NAME         TYPE           CLUSTER-IP     EXTERNAL-IP     PORT(S)        AGE
         hellosvc     LoadBalancer   10.81.15.158   192.0.2.1       80:31127/TCP   33m
         kubernetes   ClusterIP      10.81.0.1      <none>          443/TCP        93m
         loadgensvc   ClusterIP      10.81.15.155   <none>          80/TCP         4m52s
         

  14. Send a request to the `hellosvc`. Replace `EXTERNAL_IP` with the external IP address of your `hellosvc`.
         
         curl http://EXTERNAL_IP
         




## Ready for Cloud Service Mesh

Now you have the application deployed to GKE. The `loadgen` can use Kubernetes DNS (`hellosvc:80`) to send requests to the`server`, and you can send requests to the `server` with an external IP address. Although Kubernetes gives you many features, some information about the services is missing:

  * **How do the services interact?** What's the relationship between the services? How does traffic flow between the services? You know the `loadgen` sends requests to the `server`, but imagine you are unfamiliar with the application. You can't answer these questions by looking at the list of running Pods on GKE.
  * **Metrics** : How long does the `server` take to respond to incoming requests? How many requests per second (RPS) are inbound to the `server`? Are there any error responses?
  * **Security information** : Is traffic between `loadgen` and the `server` plain `HTTP` or mTLS?



Cloud Service Mesh can provide answers to these questions. [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.22/docs/overview) is a Google Cloud-managed version of the [open-source Istio project](https://istio.io). Cloud Service Mesh works by placing an [Envoy](https://www.envoyproxy.io) sidecar proxy in each Pod. The Envoy proxy intercepts all inbound and outbound traffic to the application containers. This means that the `server` and `loadgen` each get an Envoy sidecar proxy, and all traffic from the `loadgen` to `server` is mediated by the Envoy proxies. The connections between these Envoy proxies forms the service mesh. This service mesh architecture provides a control layer on top of Kubernetes.

![service mesh](https://docs.cloud.google.com/static/service-mesh/v1.22/docs/images/service-mesh.svg)

Because the Envoy proxies run in their own containers, you can install Cloud Service Mesh on top of a GKE cluster with no substantial changes to your application code. However, there are a few key ways in which you prepared the application to be instrumented with Cloud Service Mesh:

  * Services for all containers: Both the `server` and `loadgen` Deployments have a Kubernetes service attached. Even the `loadgen`, which doesn't receive any inbound requests, has a service.
  * Ports in services must be named: Although GKE allows you to define unnamed service ports, Cloud Service Mesh requires that you provide a [name for a port](https://docs.cloud.google.com/service-mesh/v1.22/docs/naming-service-ports) that matches the port's protocol. In the YAML file, the port for the `server` is named `http` because the `server` uses the `HTTP` communication protocol. If the `service` used `gRPC`, you would name the port `grpc`.
  * Deployments are labeled: This allows you to use Cloud Service Mesh traffic management features such as splitting traffic between versions of the same service.



## Install Cloud Service Mesh

Visit the [Cloud Service Mesh installation guide](https://docs.cloud.google.com/service-mesh/v1.22/docs/unified-install/install-anthos-service-mesh) and follow the instructions to install Cloud Service Mesh on your cluster.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

To clean up, delete the GKE cluster. Deleting the cluster deletes all the resources that make up the container cluster, such as the compute instances, disks and network resources.
    
    
    gcloud container clusters delete asm-ready

## What's next

  * Learn more about the technologies used in this tutorial:

    * [Docker](https://docs.docker.com/get-started/)
    * [Containers](https://docs.cloud.google.com/containers)
    * [Container Registry](https://docs.cloud.google.com/container-registry/docs)
    * [Kubernetes](https://kubernetes.io/)
    * [GKE](https://docs.cloud.google.com/kubernetes-engine/docs)
    * [The Service Mesh Era](https://services.google.com/fh/files/misc/the_service_mesh_era_architecting_securing_and_managing_microservices_with_istio_white_paper.pdf)
    * [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs)
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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
