---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deploy-app/
title: Quickstart: Deploy an application on GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:19.565622+00:00
---

# Quickstart: Deploy an application on GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deploy-app/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deploy an application on GKE on Azure

This page describes how to create a cluster and node pool, and then deploy a sample application using GKE on Azure.

## Terraform support

If you're familiar with Terraform, you can use the [Terraform scripts available on GitHub](https://github.com/GoogleCloudPlatform/anthos-samples/tree/main/anthos-multi-cloud/Azure) to automate the prerequisites and create a cluster.

## Before you begin

Before creating a cluster, you must complete the [prerequisites](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/prerequisites). In particular, you must provide the following resources:

  * An Azure virtual network where the cluster will run.
  * A subnet for the Kubernetes control plane replicas.
  * Azure role assignments that will grant GKE on Azure access to your Azure environment using a service principal.
  * A AzureClient resource that GKE on Azure uses to authenticate to Azure services and manage resources in your Azure account.
  * An SSH key pair for accessing Azure virtual machines in the cluster.



It is your responsibility to create and manage these resources, which can be shared between all your clusters. All other underlying Azure resources for your cluster are managed by GKE on Azure.

## Set default settings for the gcloud CLI

Use the gcloud CLI to configure default settings for your default project and Google Cloud region.

Your project has a project ID as a unique identifier. When you create a project, you can use the automatically generated project ID or you can create your own.

Your Google Cloud region is a location where your clusters will be managed from. For example, `us-west1`. See [Management regions](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/gcp-managed-regions) for more details.

When you configure these default settings, you don't need to include them when you run the Google Cloud CLI. You can also specify settings or override default settings by passing the `--project` and `--location` flags to the Google Cloud CLI.

When you create GKE on Azure resources after configuring your default project and location, the resources are automatically created in that project and location.

**Note:** The gcloud CLI might return an error if these settings are either not configured or not specified.

To set defaults, follow these steps:

  1. Set the default project:
         
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with your project ID.

  2. Set the default management location:
         
         gcloud config set container_azure/location GOOGLE_CLOUD_LOCATION
         

Replace `GOOGLE_CLOUD_LOCATION` with your location, such as `us-west1`.


**Note:** the `container_azure/location` property was previously named `azure/location`. If you have previously set the property `azure/location`, its value is copied to `container_azure/location` next time you run a command.

## Select Azure resource IDs for your cluster

### Select a resource group ID

Save your cluster's resource group to an environment variable running the following command:
    
    
    CLUSTER_RESOURCE_GROUP_ID=$(az group show --query id --output tsv \
        --resource-group=CLUSTER_RESOURCE_GROUP_NAME)
    

Replace `CLUSTER_RESOURCE_GROUP_NAME` with the name of the resource group to provision your cluster resources in, that you set up in the [Create an Azure resource group](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-azure-resource-group) prerequisite step.

### Select a virtual network ID

Save your cluster's VNet ID to an environment variable by running the following command:
    
    
    VNET_ID=$(az network vnet show --query id --output tsv \
        --resource-group=VNET_RESOURCE_GROUP_NAME \
        --name=VNET_NAME)
    

Replace the following:

  * `VNET_RESOURCE_GROUP_NAME` with the name of the resource group that contains your virtual network, as set up in the [Create an Azure virtual network](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-azure-vnet) prerequisite step.
  * `VNET_NAME` with the name of your virtual network, as set up in the [Create an Azure virtual network](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-azure-vnet) prerequisite step.



### Select a subnet ID

Save your cluster's subnet ID to an environment variable by running the following command:
    
    
    SUBNET_ID=$(az network vnet subnet show --query id --output tsv \
        --resource-group VNET_RESOURCE_GROUP_NAME \
        --vnet-name VNET_NAME \
        --name SUBNET_NAME)
    

Replace:

  * `VNET_RESOURCE_GROUP_NAME` with an existing resource group name that contains your virtual network. This can be the resource group name that you set up in [Create an Azure virtual network](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-azure-vnet).
  * `VNET_NAME` with the name of your virtual network. This can be the name of your virtual network that you set up in [Create an Azure virtual network](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-azure-vnet).
  * `SUBNET_NAME` with the name of your subnet— for example, `default`.



### Select CIDR ranges for your cluster

Kubernetes requires two CIDR ranges to be provided for the cluster. These CIDR ranges should be chosen so that they do not overlap with CIDR ranges used by your VPC subnets. They should be large enough for the maximum expected size of your cluster.

  * **Pod address CIDR range** : When a new `Pod` is created, it is allocated an IP address from this range. Example range: 192.168.208.0/20

  * **Service address CIDR range** : When a new Service is created, it is allocated an IP address from this range. Example range: 192.168.224.0/20




## Create a cluster

Use the following command to create a cluster under GKE on Azure.
    
    
    gcloud container azure clusters create azure-cluster-0 \
        --cluster-version 1.35.3-gke.300 \
        --azure-region AZURE_REGION \
        --fleet-project FLEET_PROJECT_ID \
        --client CLIENT_NAME \
        --resource-group-id $CLUSTER_RESOURCE_GROUP_ID \
        --vnet-id $VNET_ID \
        --subnet-id $SUBNET_ID \
        --pod-address-cidr-blocks POD_CIDR_BLOCK \
        --service-address-cidr-blocks SERVICE_CIDR_BLOCK \
        --ssh-public-key "SSH_PUBLIC_KEY" \
        --tags "google:gkemulticloud:cluster=azure-cluster-0"
    

Replace:

  * `AZURE_REGION`: a [supported Azure region](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/supported-regions) associated to your Google Cloud region
  * `FLEET_PROJECT_ID` with the [fleet](https://docs.cloud.google.com/anthos/multicluster-management/fleets) host project ID where the cluster will be registered.
  * `CLIENT_NAME`: your [AzureClient](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-azure-client) name.
  * `POD_CIDR_BLOCK`: your cluster's Pod address range
  * `SERVICE_CIDR_BLOCK`: your cluster's Service address range
  * `SSH_PUBLIC_KEY` with the text of your SSH public key as created in the [Create an SSH key pair](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-ssh-keypair) prerequisite step. If you saved your public key to an environment variable in that step, you can use `${SSH_PUBLIC_KEY}`. 



For more information and optional parameters, see the [gcloud container azure clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create) reference page.

## Create a node pool

Create a node pool with the Google Cloud CLI:
    
    
    gcloud container azure node-pools create pool-0 \
        --cluster azure-cluster-0 \
        --node-version 1.35.3-gke.300 \
        --vm-size Standard_B2s \
        --max-pods-per-node 110 \
        --min-nodes 1 \
        --max-nodes 5 \
        --ssh-public-key "SSH_PUBLIC_KEY" \
        --subnet-id $SUBNET_ID \
        --tags "google:gkemulticloud:cluster=azure-cluster-0"
    

Replace `SSH_PUBLIC_KEY` with the text of your SSH public key, as created in the [Create an SSH key pair](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-ssh-keypair) prerequisite step. If you saved your public key to an environment variable, you can use `${SSH_PUBLIC_KEY}`.

## View your cluster status

After you create a cluster and node pool, you can view a cluster's status with the Google Cloud CLI or the Google Cloud console. To view the cluster's status, choose if you are using the Google Cloud CLI or Google Cloud console and follow these steps:

###  gcloud 

Use the `gcloud container azure clusters describe` command to get details about your cluster:
    
    
    gcloud container azure clusters describe CLUSTER_NAME \
        --location GOOGLE_CLOUD_LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: your cluster's name
  * `GOOGLE_CLOUD_LOCATION`: the name of the Google Cloud location that manages the cluster



###  Google Cloud console 

  1. In the Google Cloud console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Your clusters are listed by their name and location.

  3. Click the cluster's name. A panel with information on the cluster, including its status and enabled features, appears.




## Get authentication credentials for the cluster

After creating your cluster, you need to get authentication credentials to interact with the cluster:
    
    
    gcloud container azure clusters get-credentials azure-cluster-0
    

This command configures `kubectl` to access the cluster you created using [Connect gateway](https://docs.cloud.google.com/anthos/multicluster-management/gateway/using). You need at least one node pool to use Connect gateway because it relies on the Connect agent, which runs as a Deployment in the cluster.

## Deploy an application to the cluster

Now that you have created a cluster, you can deploy a containerized application to it. For this quickstart, you can deploy our example web application, `hello-app`.

You use Kubernetes objects to create and manage your cluster's resources. You use the Deployment object for deploying stateless applications like web servers. [Service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service) objects define rules and load balancers for accessing your application from the internet.

### Create the Deployment

To run `hello-app` in your cluster, you need to deploy the application by running the following command:
    
    
    kubectl create deployment hello-server --image=us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
    

This Kubernetes command, [`kubectl create deployment`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#create) creates a Deployment named `hello-server`. The Deployment's [Pod](https://kubernetes.io/docs/concepts/workloads/pods) runs the `hello-app` container image.

In this command:

  * `--image` specifies a container image to deploy. In this case, the command pulls the example image from an Artifact Registry repository, `us-docker.pkg.dev/google-samples/containers/gke/hello-app`. The `:1.0` indicates the specific image version to pull. If you don't specify a version, the image tagged with `latest` is used.



### Expose the Deployment

After deploying the application, you need to expose it to the internet so that users can access it. You can expose your application by creating a Service, a Kubernetes resource that exposes your application to external traffic.

To expose your application, run the following [`kubectl expose`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#expose) command:
    
    
    kubectl expose deployment hello-server --type LoadBalancer --port 80 --target-port 8080
    

Passing in the `--type LoadBalancer` flag creates an Azure load balancer for your container. The `--port` flag initializes public port 80 to the internet and the `--target-port` flag routes the traffic to port 8080 of the application.

Load balancers are billed according to Azure load balancer pricing.

### Inspect and view the application

  1. Inspect the running Pods by using `kubectl get pods`:
         
         kubectl get pods
         

You should see one `hello-server` Pod running on your cluster.

  2. Inspect the `hello-server` Service by using `kubectl get service`:
         
         kubectl get service hello-server
         

From this command's output, copy the Service's external IP address from the `EXTERNAL-IP` column.

**Note:** You might need to wait several minutes before the Service's external IP address is available. If the application's external IP is `<pending>`, run `kubectl get service` again.
  3. View the application from your web browser by using the external IP with the exposed port:
         
         http://EXTERNAL-IP
         




You have just deployed a containerized web application to GKE on Azure.

## Clean up

  1. Delete the application's Service and Deployment:
         
         kubectl delete service hello-server
         kubectl delete deployment hello-server
         

  2. Delete your node pool by running `gcloud container azure node-pools delete`:
         
         gcloud container azure node-pools delete pool-0 --cluster azure-cluster-0
         

  3. Delete your cluster by running `gcloud container azure clusters delete`:
         
         gcloud container azure clusters delete azure-cluster-0
         




## What's next

  * [Install Anthos Config Management](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/install-config-management)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
