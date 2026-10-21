---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/user/dl-container/
title: Deploy and use a Deep Learning (DL) container \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:22:11.214431+00:00
---

# Deploy and use a Deep Learning (DL) container  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/user/dl-container/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Deploy and use a Deep Learning (DL) container Stay organized with collections  Save and categorize content based on your preferences. 

A Deep Learning (DL) container is a Docker container with preinstalled data science frameworks, libraries, and tools. A user, such as a data scientist, chooses a single DL container and deploys it. The deployed container has a performance-optimized, consistent environment that helps with quickly prototyping and implementing workflows.

## Deploy a DL container

Before using a DL container, you must choose and deploy a container image that runs your Machine Learning (ML) task. Preinstalled frameworks, libraries, and tools provision a DL container.

### Deploy a DL container using `kubeconfig` files

Google Distributed Cloud (GDC) air-gapped appliance provides the following `kubeconfig` file that deploys your DL container:

  * `CLUSTER_KUBECONFIG`: the kubeconfig file for the bare metal Kubernetes cluster. GDC provides one cluster for all workloads.



For more information about signing into the UI and the `kubectl` tool, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/sign-in#sign-in). In order to retrieve the `CLUSTER_KUBECONFIG` file, see [Get a `kubeconfig` file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-auth#get_a_kubeconfig_file).

### Download the sample Machine Learning (ML) script and dataset

Download the sample ML script, `beginner.ipynb`, and dataset, `mnist.npz`, to run the ML quickstart tutorial. The tutorial demonstrates how to deploy and use a DL container to run ML experiments.
    
    
    mkdir -p /tmp/datasets
    cd /tmp/datasets
    
    wget --no-check-certificate
    https://GDC_APPLIANCE_URL/.well-known/static/dl-container-tutorial/beginner.ipynb
    
    wget --no-check-certificate
    https://GDC_APPLIANCE_URL/.well-known/static/dl-container-tutorial/mnist.npz
    

Replace `GDC_APPLIANCE_URL` with the domain name used to access GDC. When opening any URL for the first time, GDC redirects you to your identity provider login page.

### Look up the IP address of the Harbor registry

Before using the sample script and dataset, you must find the DL container image location in the Harbor registry. The Harbor registry is a service that stores private container images.

The first line of sample code sets the path of the `KUBECONFIG` environment variable, which gets the Harbor registry address. The Harbor registry address provides access to a list of available container images.

In the second line of sample code, the `kubectl` tool uses the `KUBECONFIG` environment variable.

In the third line of sample code, the `REGISTRY_URL#https://` command removes the prefix `https://` from the URL and stores the Harbor registry domain in the `REGISTRY_IP` environment variable.

In the last line of the sample code, the kubectl tool fetches the password for the `admin` user.
    
    
    export KUBECONFIG=CLUSTER_KUBECONFIG
    
    REGISTRY_URL=$(kubectl get harborcluster harbor -n harbor-system -o=jsonpath='{.spec.externalURL}')
    REGISTRY_IP=${REGISTRY_URL#https://}
    ADMIN_PASS=$(kubectl -n harbor-system get secret harbor-admin -o jsonpath="{.data.secret}" | base64 -d)
    
    

### Choose a container image

You must choose a container image to deploy before you can run an ML task. Use the Harbor registry domain and the path in the following table from the Harbor registry to view the list of available container images:

Framework | Processor | Container Image Name  
---|---|---  
Base | GPU | base-cu113  
Base | CPU | base-cpu  
TensorFlow Enterprise 2.x | GPU | tf2-gpu  
PyTorch | GPU | pytorch-gpu  
  
This table is organized by framework and processor. To choose a DL container image that can process your ML experiment, follow these steps:

  1. Identify the framework, which contains the ML tools.
  2. Choose the processor. You choose the processor based on the kind of ML task to run and the compute intensity of that task. For example, choose one of the GPU processors when you have a compute-intensive ML task, and allocate a GPU resource to the DL container.



### Create and deploy a DL container to the Kubernetes cluster

To create the GDC instance, specify the path to the `kubeconfig` file of the bare metal Kubernetes cluster. The `KUBECONFIG` environment variable specifies to which cluster the `kubectl` tool deploys the DL container. The `kubectl apply` command deploys the DL container instance.

Replace `CONTAINER_IMAGE_NAME` with the image selected from the list of images in Choose a container image, and be sure to supply the tag.
    
    
    export KUBECONFIG=CLUSTER_KUBECONFIG
    
    kubectl apply -f - <<EOF
    apiVersion: v1
    kind: Pod
    metadata:
      name: dl-container-pod
      namespace: NAMESPACE
    spec:
      containers:
      - image: gcr.io/private-cloud-staging/notebooks/deeplearning-platform-release/CONTAINER_IMAGE_NAME:CONTAINER_IMAGE_TAG
        command: ["tail", "-f", "/dev/null"]
        name: training
    EOF
    

## Use a deployed DL container

The following topics provide an example of how to use a DL container image to train and use a model to generate predictions.

### Copy the tutorial files to the DL container pod

Copy the quickstart tutorial files into your DL container pod. The `beginner.ipynb` contains the steps to train and use a model to make predictions. The ML training tutorial uses the `mnist.npz` dataset file to train a model.
    
    
    cd /tmp/datasets
    
    kubectl cp beginner.ipynb dl-container-pod:/tmp
    kubectl cp mnist.npz dl-container-pod:/tmp
    

### Run the ML quickstart tutorial

Run the tutorial with the following commands. Use the first line to enter the container pod. After you are in the container pod, change directory to `tmp`, and run the `papermill` tool that is packaged in the DL container. The `papermill` tool runs the tutorial to create a notebook that generates predictions.

  1. Enter an interactive terminal into the DL pod:
         
         kubectl exec -it dl-container-pod -- /bin/bash
         

  2. In the DL pod context, run the following commands:
         
         cd tmp
         papermill beginner.ipynb result.ipynb
         

The deployment generates a `result.ipynb` file in the `/tmp` directory.

  3. View the content and the prediction outputs from the generated ML model:
         
         cat result.ipynb
         




### Optional: Delete the DL container pod

After you finish running your experiment in the DL container pod, delete the pod as a best practice:
    
    
    kubectl delete pod dl-container-pod
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
