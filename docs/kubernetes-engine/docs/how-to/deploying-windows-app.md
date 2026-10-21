---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-windows-app/
title: Deploying a Windows Server application \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:24:59.071526+00:00
---

# Deploying a Windows Server application  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-windows-app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Deploying a Windows Server application Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

In this page, you learn how to deploy a stateless Windows Server application on a Google Kubernetes Engine (GKE) cluster. You can also learn how to [deploy a stateful Windows application](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateful-apps).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Artifact Registry API and the Google Kubernetes Engine API. 
[ Enable APIs ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,artifactregistry.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Deploying a Windows Server application to a cluster with public nodes

To deploy a Windows Server application to a GKE cluster with only public nodes, you'll need to perform the following tasks:

  1. Create a cluster with public nodes.
  2. Create a Deployment manifest file.
  3. Create and expose the Deployment.
  4. Verify that the Pod is running.



### Create a cluster with public nodes

If you already have a GKE cluster that uses Windows Server node pools, continue to the next step. Otherwise, [create a cluster using Windows Server node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows). To provision nodes with external IP addresses (public nodes), use the `--no-enable-private-nodes` flag when creating the cluster.

### Create a Deployment manifest file

Windows Server nodes are [tainted](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) with the following key-value pair: `node.kubernetes.io/os=windows:NoSchedule`.

This taint helps ensure that the GKE scheduler does not attempt to run Linux containers on Windows Server nodes. To schedule Windows Server containers on Windows Server nodes, your manifest file must include this node selector:
    
    
    nodeSelector:
     kubernetes.io/os: windows
    

An admission webhook running in the cluster checks new workloads for the presence of this Windows node selector and when found, applies the following toleration to the workload which lets it run on the tainted Windows Server nodes:
    
    
    tolerations:
    - effect: NoSchedule
      key: node.kubernetes.io/os
      operator: Equal
      value: windows
    

In some cases you may need to include this toleration explicitly in your manifest file. For example, if you are deploying a DaemonSet with a [multi-arch](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows#building_multi-arch_images) container image to run on all Linux and Windows Server nodes in the cluster, then your manifest file won't include the Windows node selector. You must explicitly include the toleration for the Windows taint.

#### Example manifest file

The following example Deployment file (`iis.yaml`) deploys Microsoft's IIS image to a single Pod:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: iis
      labels:
        app: iis
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: iis
      template:
        metadata:
          labels:
            app: iis
        spec:
          nodeSelector:
            kubernetes.io/os: windows
          containers:
          - name: iis-server
            image: mcr.microsoft.com/windows/servercore/iis
            ports:
            - containerPort: 80
    

This file is for a cluster where all workloads use the same Windows Server node image type and version. For details on how to work with mixed node images, see the Using mixed node images section.

### Create and expose the Deployment

Create and expose the Deployment file you created in the preceding step as a Kubernetes Service with an external load balancer Deployment.

  1. To create the Deployment resource, run the following command:
         
         kubectl apply -f iis.yaml
         

  2. To expose the Deployment as an external load balancer, run the following command:
         
         kubectl expose deployment iis \
             --type=LoadBalancer \
             --name=iis
         




### Verify that the Pod is running

Make sure the Pod is functioning by validating it.

  1. Check the status of the Pod using `kubectl`:
         
         kubectl get pods
         

  2. Wait until the returned output shows that the Pod has `Running` as its status:
         
         NAME                   READY     STATUS    RESTARTS   AGE
         iis-5c997657fb-w95dl   1/1       Running   0          28s
         

  3. Get the status of the service, and wait until the `EXTERNAL-IP` field is populated:
         
         kubectl get service iis
         

You should see the following output:
         
         NAME   TYPE           CLUSTER-IP    EXTERNAL-IP      PORT(S)        AGE
         iis    LoadBalancer   10.44.2.112   external-ip    80:32233/TCP   17s
         




Now, you can use your browser to open `http://EXTERNAL_IP` to see the IIS web page.

## Deploying a Windows Server application to a cluster with private nodes

This section shows you how to deploy a Windows Server container application to a GKE cluster enabled with private nodes only.

Windows Server container images have several layers and the base layers are provided by Microsoft. The base layers are stored as a foreign layer instead of being embedded with the image as Linux Docker image layers are. When a Windows Server container image is pulled for the first time, the base layers must typically be downloaded from Microsoft servers. Because private nodes don't have connectivity to the internet, the Windows Server base container layers cannot be pulled from Microsoft servers directly.

To use clusters with private nodes enabled, you can configure the Docker daemon to allow pushing non-distributable layers to private registries. To learn more, see [Allow push of non-distributable artifacts](https://docs.docker.com/reference/cli/dockerd/#allow-push-of-non-distributable-artifacts) on Docker's GitHub page.

To deploy your Windows Server application to a cluster enabled with private nodes:

  1. Create a cluster with Windows Server nodes and enable private nodes.
  2. Build the Windows Server application Docker image.
  3. Deploy the application to a cluster enabled with private nodes.
  4. Verify that the Pod is running.



### Create a cluster with private nodes

Follow the instructions in [Creating a cluster with Windows Server nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows). To provision nodes with only internal IP addresses (private nodes), use the `--enable-private-nodes` flag when creating the cluster.

### Build the Windows Server application Docker image

  1. To build the Docker image, start a [Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances) with the Windows Server version that you want to run your application containers on, such as Windows Server 2019 or Windows Server version 20H2. Also, ensure you have internet connectivity.

  2. In the Compute Engine instance, navigate to the Docker daemon config:
         
         cat C:\ProgramData\docker\config\daemon.json
         

  3. Configure the Docker `daemon.json` file to allow foreign layers to be pushed to your private registry by adding these lines:
         
         {
           "allow-nondistributable-artifacts": ["REGISTRY_REGION-docker.pkg.dev"]
         }
         

In this example, `REGISTRY_REGION-docker.pkg.dev` refers to [Artifact Registry](https://docs.cloud.google.com/artifact-registry), where the image will be hosted.

  4. Restart the Docker daemon:
         
         Restart-Service docker
         

  5. [Create a Docker repository in Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/manage-repos#create).

  6. Build and tag the Docker image for your application:
         
         cd C:\my-app
         
         
         docker build -t REGISTRY_REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/my-app:v2 .
         

This command instructs Docker to build the image using the Dockerfile in the current directory and tag it with a name, such as `us-central1-docker.pkg.dev/my-project/my-repository/my-app:v2`.

  7. Push the application's Docker image to the Artifact Registry repository in your project. The `allow-nondistributable-artifacts` configuration set causes the Windows base layers to be pushed to your private registry.
         
         docker push REGISTRY_REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/my-app:v2
         




### Create a Deployment manifest file

The following is a sample Deployment manifest file named `my-app.yaml`. The image in this example is the one you pushed in the previous step (`REGISTRY_REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/my-app:v2`).
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-app
      labels:
        app: my-app
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: my-app
      template:
        metadata:
          labels:
            app: my-app
        spec:
          nodeSelector:
            kubernetes.io/os: windows
          containers:
          - name: my-server
            image: REGISTRY_REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/my-app:v2
    

  1. Use the [`get-credentials`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/get-credentials) command to enable `kubectl` to work with the cluster you created:
         
         gcloud container clusters get-credentials CLUSTER_NAME
         

Replace `CLUSTER_NAME` with the name of the cluster you created.

  2. Deploy the application specified in the `my-app.yaml` file to your cluster:
         
         kubectl apply -f my-app.yaml
         




### Verify the Pod is running

List all Pods to ensure the application is running correctly:
    
    
    kubectl get pods
    

You should see the Pod with a status of `Running` like in the following output:
    
    
    NAME                     READY   STATUS    RESTARTS   AGE
    my-app-c95fc5596-c9zcb   1/1     Running   0          5m
    

## Using mixed node images

Your clusters can contain node pools with multiple Windows Server versions. They can also combine Windows Server and Linux workloads. The following sections provide details on how to configure your workloads to use these types of clusters.

### Using workloads with different Windows Server LTSC OS versions

Windows Server nodes support both LTSC2022 and LTSC2019 OS images. You can specify the Windows OS version to use (LTSC2022) with the following key-value pair in nodeSelector: `cloud.google.com/gke-windows-os-version=2022`.

This node label helps ensure that the GKE scheduler will choose the correct Windows Server nodes to run either LTSC2022 or LTSC2019 workloads. The Windows Server nodes both belong to image type `windows_ltsc_containerd`. The value of the node label can be `2022` or `2019`. If the node label is not specified, then both LTSC2019 or LTSC2022 nodes can be used to schedule containers. To schedule Windows Server containers only on Windows Server LTSC2022 nodes, your manifest file must include this node selector:
    
    
    nodeSelector:
       kubernetes.io/os: windows
       cloud.google.com/gke-os-distribution: windows_ltsc
       cloud.google.com/gke-windows-os-version: 2022
    

### Using workloads with different Windows Server versions

If you need to run Windows Server node pools with multiple different LTSC versions, we recommend building your container images as [multi-arch images](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows#building_multi-arch_images) that can run on all of the Windows Server versions in use in your cluster. The `gke-os-distribution` node label is not sufficient to prevent your workloads from potentially being scheduled onto incompatible nodes.

### Using Linux and Windows Server workloads in a cluster

Add the following node selector to your Linux workloads to ensure they are always scheduled to Linux nodes:
    
    
    nodeSelector:
       kubernetes.io/os: linux
    

This provides additional protection to avoid Linux workloads being scheduled onto Windows Server nodes in case the `NoSchedule` taint is accidentally removed from the Windows Server nodes.

**Note:** For DaemonSets that run on Linux only, this nodeSelector is _required_.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
