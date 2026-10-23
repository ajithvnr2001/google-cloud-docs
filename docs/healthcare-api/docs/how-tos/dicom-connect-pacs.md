---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-connect-pacs/
title: Connect a PACS to the Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:18.102674+00:00
---

# Connect a PACS to the Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-connect-pacs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Connect a PACS to the Cloud Healthcare API Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use the open source [Cloud Healthcare API DICOM adapter](https://github.com/GoogleCloudPlatform/healthcare-dicom-dicomweb-adapter) on Google Kubernetes Engine (GKE) to complete the following tasks:

  * Connect a Picture Archiving and Communication System (PACS) to the Cloud Healthcare API.
  * Import DICOM data from the PACS to a DICOM store in the Cloud Healthcare API.



This guide provides a simple way to set up a prototype using Google Kubernetes Engine and a Compute Engine virtual machine (VM). The Compute Engine VM simulates the on-premise PACS. For more detailed information, see the [DICOM adapter README](https://github.com/GoogleCloudPlatform/healthcare-dicom-dicomweb-adapter).

## DICOM adapter overview

The adapter consists of two primary components: the import adapter and the export adapter. This guide shows how to use the import adapter to store DICOM images in a DICOM store.

Use the DICOM adapter to translate data between traditional protocols and RESTful protocols. For example, you can translate from the C-STORE format to the STOW-RS format.

## Costs

This guide uses billable components of Google Cloud, including the following:

  * Cloud Healthcare API
  * Google Kubernetes Engine
  * Compute Engine



Use the [Pricing Calculator](https://cloud.google.com/products/calculator) to generate a cost estimate based on your projected usage. New Cloud Platform users might be eligible for a [free trial](https://cloud.google.com/free).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Healthcare API, Google Kubernetes Engine, and Container Registry APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=healthcare,gke,container)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Healthcare API, Google Kubernetes Engine, and Container Registry APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=healthcare,gke,container)

  8. Wait for the GKE API and related services to be enabled. This can take several minutes.
  9. [Create a DICOM store](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom#creating_a_dicom_store) if you haven't already.



## Choose a shell

To complete this guide, use [Cloud Shell](https://docs.cloud.google.com/shell) or your local shell.

Cloud Shell is a shell environment for managing resources hosted on Google Cloud. Cloud Shell comes preinstalled with the following tools, which you use in this guide:

  * [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud): provides the primary command-line interface for Google Cloud
  * [`kubectl`](https://kubernetes.io/docs/reference/kubectl/overview/): provides the command-line interface for running commands against GKE clusters



To open Cloud Shell or configure your local shell, complete the following steps:

### Cloud Shell

  1. Go to Google Cloud console.

[Google Cloud console](https://console.cloud.google.com/)

  2. From the top-right corner of the console, click the **Activate Google Cloud Shell** button: ![](https://docs.cloud.google.com/static/kubernetes-engine/images/cloud-shell.png)




A Cloud Shell session opens inside a frame at the bottom of the console. You use this shell to run `gcloud` and `kubectl` commands.

### Local shell

If you prefer to use your local shell, you must install the gcloud CLI. See [Installing Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) for instructions.

## Deploy the adapter using Google Kubernetes Engine

The import adapter and export adapter are containerized applications staged in a pre-built Docker image in [Container Registry](https://docs.cloud.google.com/container-registry). In this guide, you deploy the `dicom-import-adapter` image to run on a GKE cluster.

### Grant the Compute Engine service account permissions

Follow the instructions in [Creating and enabling service accounts for instances](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#using_the_default_service_account) to grant the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) the `roles/healthcare.dicomEditor` role. For more information, see [DICOM store roles](https://docs.cloud.google.com/healthcare-api/docs/access-control#dicom_store_roles).

**Note:** If you start the GKE cluster using a different service account, grant the role `roles/healthcare.dicomEditor` to the different service account instead.

### Create the cluster

**Note:** The following command creates a GKE cluster in the [default VPC network](https://docs.cloud.google.com/vpc/docs/vpc#default-network) and uses the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account). Changes to the service account or network might affect other parts of this guide. If you change the service account or VPC network, this guide describes the additional changes you must make.

### gcloud

To create a cluster in GKE named `dicom-adapter`, run the [`gcloud container clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create) command. 

Before using any of the command data below, make the following replacements: 

  * COMPUTE_ZONE: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) where your cluster is deployed. A zone is an approximate regional location where your clusters and their resources are deployed. For example, `us-west1-a` is a zone in the `us-west` region. If you've set a default zone using the `gcloud config set compute/zone` command, the value of the flag in the previous command overrides the default.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters create dicom-adapter \
      --zone=COMPUTE_ZONE \
      --scopes=https://www.googleapis.com/auth/cloud-healthcare

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters create dicom-adapter `
      --zone=COMPUTE_ZONE `
      --scopes=https://www.googleapis.com/auth/cloud-healthcare

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters create dicom-adapter ^
      --zone=COMPUTE_ZONE ^
      --scopes=https://www.googleapis.com/auth/cloud-healthcare

You should receive a response similar to the following:
    
    
    Creating cluster dicom-adapter in COMPUTE_ZONE... Cluster is being health-checked (master is healthy)...done.
    Created [https://container.googleapis.com/v1/projects/PROJECT_ID/zones/COMPUTE_ZONE/clusters/dicom-adapter].
    To inspect the contents of your cluster, go to: https://console.cloud.google.com/kubernetes/workload_/gcloud/COMPUTE_ZONE/dicom-adapter?project=PROJECT_ID
    kubeconfig entry generated for dicom-adapter.
    NAME           LOCATION    MASTER_VERSION  MASTER_IP        MACHINE_TYPE   NODE_VERSION   NUM_NODES  STATUS
    dicom-adapter  COMPUTE_ZONE 1.18.16-gke.502   123.456.789.012  n1-standard-1  1.18.16-gke.502  3     RUNNING
    

### Configure the Deployment

When deploying an application to GKE, you define properties of the [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) using a Deployment manifest file, which is typically a YAML file. For information on Deployment manifest files, see [Creating Deployments](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/deployment#creating_deployments).

Using a text editor, create a Deployment manifest file for the import adapter called `dicom_adapter.yaml` with the following content:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: dicom-adapter
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: dicom-adapter
      template:
        metadata:
          labels:
            app: dicom-adapter
        spec:
          containers:
            - name: dicom-import-adapter
              image: gcr.io/cloud-healthcare-containers/healthcare-api-dicom-dicomweb-adapter-import:0.2.43
              ports:
                - containerPort: 2575
                  protocol: TCP
                  name: "port"
              args:
                - "--dimse_aet=IMPORTADAPTER"
                - "--dimse_port=2575"
                - "--dicomweb_address=https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb"

Replace the following:

  * PROJECT_ID: project ID
  * LOCATION: location of the dataset
  * DATASET_ID: ID for the parent dataset of your DICOM store
  * DICOM_STORE_ID: ID for the DICOM store to which you're importing DICOM data



### Configure the Service

To make the DICOM adapter accessible to applications outside of the GKE cluster (such as a PACS), you must configure an internal load balancer. The load balancer lets you internally expose the [DIMSE](https://dicom.nema.org/dicom/2013/output/chtml/part07/sect_3.10.html) port (in this guide, port 2575).

Create a [Service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service) manifest file to configure load balancing. In the directory where you created the Deployment manifest file, use a text editor to create a file called `dicom_adapter_load_balancer.yaml` with the following content. You create and deploy the Service manifest file in Deploying the Service and the internal load balancer.
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: dicom-adapter-load-balancer
      # The "Internal" annotation will result in an load balancer that can only
      # be accessed from within the VPC the Kubernetes cluster is in.
      # You can remove this annotation to get an externally accessible load balancer.
      annotations:
        cloud.google.com/load-balancer-type: "Internal"
    spec:
      ports:
      - port: 2575
        targetPort: 2575
        protocol: TCP
        name: port
      selector:
        app: dicom-adapter
      type: LoadBalancer
    

**Note:** Use an internal load balancer only if you will be accessing the DICOM adapter from the same VPC network to which the GKE cluster is attached, as described on this page. If you are deploying a DICOM adapter to use from other networks, such as on-premises, delete the `cloud.google.com/load-balancer-type: "Internal"` line from the file shown previously.

### Deploy the Deployment

To deploy the adapter to a GKE cluster, run the following command in the directory containing the `dicom_adapter.yaml` Deployment manifest file:
    
    
    kubectl apply -f dicom_adapter.yaml
    

The output is the following:
    
    
    deployment.apps/dicom-adapter created
    

### Inspect the Deployment

After you create the Deployment, use the `kubectl` tool to inspect it.

To get detailed information about the Deployment, run the following command:
    
    
    kubectl describe deployment dicom-adapter
    

To view the [Pod](https://kubernetes.io/docs/concepts/workloads/pods) created by the Deployment, run the following command:
    
    
    kubectl get pods -l app=dicom-adapter
    

To get information about the created Pod, run the following command using the name of the Pod returned from the previous command:
    
    
    kubectl describe pod POD_NAME

If the Deployment was successful, the last part of the output from the previous command contains the following information. The adapter is ready to serve requests when the `dicom-import-adapter` container has the `Started` value in the `Reason` column.
    
    
    Events:
      Type    Reason     Age    From                                                   Message
      ----    ------     ----   ----                                                   -------
      Normal  Scheduled  3m33s  default-scheduler                                      Successfully assigned default/dicom-adapter-69d579778-qrm7n to gke-dicom-adapter-default-pool-6f6e0dcd-9cdd
      Normal  Pulling    3m31s  kubelet, gke-dicom-adapter-default-pool-6f6e0dcd-9cdd  Pulling image "gcr.io/cloud-healthcare-containers/healthcare-api-dicom-dicomweb-adapter-import:0.2.43"
      Normal  Pulled     3m10s  kubelet, gke-dicom-adapter-default-pool-6f6e0dcd-9cdd  Successfully pulled image "gcr.io/cloud-healthcare-containers/healthcare-api-dicom-dicomweb-adapter-import:0.2.43"
      Normal  Created    3m7s   kubelet, gke-dicom-adapter-default-pool-6f6e0dcd-9cdd  Created container dicom-import-adapter
      Normal  Started    3m7s   kubelet, gke-dicom-adapter-default-pool-6f6e0dcd-9cdd  Started container dicom-import-adapter
    

### Deploy the Service and the internal load balancer

To create the internal load balancer, in the directory containing the `dicom_adapter_load_balancer.yaml` Service manifest file, run the following command:
    
    
    kubectl apply -f dicom_adapter_load_balancer.yaml
    

The output is the following:
    
    
    service/dicom-adapter-load-balancer created
    

### Inspect the Service

After creating the Service, inspect it to verify that it has been configured correctly.

To inspect the load balancer, run the following command:
    
    
    kubectl describe service dicom-adapter-load-balancer
    

The output is the following:
    
    
    Name:                     dicom-adapter-load-balancer
    Namespace:                default
    Labels:                   <none>
    Annotations:              cloud.google.com/load-balancer-type: Internal
    Selector:                 app=dicom-adapter
    Type:                     LoadBalancer
    IP:                       198.51.100.1
    LoadBalancer Ingress:     203.0.113.1
    Port:                     port  2575/TCP
    TargetPort:               2575/TCP
    NodePort:                 port  30440/TCP
    Endpoints:                192.0.2.1:2575
    Session Affinity:         None
    External Traffic Policy:  Cluster
    Events:
    
    Events:
      Type    Reason                Age   From                Message
      ----    ------                ----  ----                -------
      Normal  EnsuringLoadBalancer  1m    service-controller  Ensuring load balancer
      Normal  EnsuredLoadBalancer   1m    service-controller  Ensured load balancer
    

The `LoadBalancer Ingress` IP address might take up to a minute to populate. Save the `LoadBalancer Ingress` IP address. You use it to access the Service from outside the cluster in the next section.

## Create a Compute Engine virtual machine

To simulate your on-premises PACS, create a Compute Engine VM to send requests to the DICOM adapter. Because you deployed an internal load balancer the VM you create and the existing GKE cluster must be [in the same region and use the same VPC network](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing#overview).

Complete the following steps to create a Linux virtual machine instance in Compute Engine:

### Console

  1. In the Google Cloud console, go to the **VM Instances** page.

[Go to VM Instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. Choose a **Region** and **Zone** for the instance that matches the zone you selected when you created the cluster. For example, if you used `us-central1-a` for the COMPUTE_ZONE when you created the cluster, select `us-central1 (Iowa)` for the **Region** and `us-central1-a` for the **Zone**.

  4. In the **Boot disk** section, click **Change** to configure your boot disk.

  5. On the **Public images** tab, choose version **9** of the **Debian** operating system.

  6. Click **Select**.

  7. In the **Firewall** section, select **Allow HTTP traffic**.

  8. Click **Create** to create the instance. 




### gcloud

Run the [`gcloud compute instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) command. The command uses the `http-server` tag to allow HTTP traffic. 

Before using any of the command data below, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * COMPUTE_ZONE: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) that you selected when you [created the cluster](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-connect-pacs#create_the_cluster)
  * INSTANCE_NAME: name of the [VM](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format)



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud compute instances create INSTANCE_NAME \
      --project=PROJECT_ID \
      --zone=COMPUTE_ZONE \
      --image-family=debian-9 \
      --image-project=debian-cloud \
      --tags=http-server

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud compute instances create INSTANCE_NAME `
      --project=PROJECT_ID `
      --zone=COMPUTE_ZONE `
      --image-family=debian-9 `
      --image-project=debian-cloud `
      --tags=http-server

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud compute instances create INSTANCE_NAME ^
      --project=PROJECT_ID ^
      --zone=COMPUTE_ZONE ^
      --image-family=debian-9 ^
      --image-project=debian-cloud ^
      --tags=http-server

You should receive a response similar to the following:
    
    
    Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/COMPUTE_ZONE/instances/INSTANCE_NAME].
    NAME          ZONE           MACHINE_TYPE   PREEMPTIBLE  INTERNAL_IP  EXTERNAL_IP    STATUS
    INSTANCE_NAME  COMPUTE_ZONE           n1-standard-1               INTERNAL_IP  EXTERNAL_IP    RUNNING
    

Allow a short time for the instance to start up. After the instance starts, it's listed on the VM Instances page with a green status icon.

By default, the instance and the cluster both use the [default VPC network](https://docs.cloud.google.com/vpc/docs/vpc#default-network), which means that traffic can be sent from the instance to the cluster. If the GKE cluster where the DICOM adapter is running was created in a different VPC network, do either of the following: 

  * Change the previous procedure to start the VM in the different VPC network.
  * Remove the `cloud.google.com/load-balancer-type: "Internal"` annotation from the load balancer service definition.



### Connect to the VM

To connect to the VM, complete the following steps:

### Console

  1. In the Google Cloud console, go to the **VM Instances** page. 

[Go to VM Instances](https://console.cloud.google.com/compute/instances)

  2. In the list of virtual machine instances, click **SSH** in the row of the instance that you created. 




### gcloud

Run the [`gcloud compute ssh`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh) command. 

Before using any of the command data below, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * COMPUTE_ZONE: the zone of the [VM](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format)
  * INSTANCE_NAME: the name of the [VM](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format)



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud compute ssh INSTANCE_NAME \
      --project PROJECT_ID \
      --zone COMPUTE_ZONE

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud compute ssh INSTANCE_NAME `
      --project PROJECT_ID `
      --zone COMPUTE_ZONE

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud compute ssh INSTANCE_NAME ^
      --project PROJECT_ID ^
      --zone COMPUTE_ZONE

You now have a terminal window for interacting with your Linux instance.

## Import DICOM images to the DICOM store

There are multiple software options available that you can use to send DICOM images over a network. In the following sections, you use the [DCMTK DICOM toolkit](https://dcmtk.org/dcmtk.php.en).

To import DICOM images to your DICOM store, complete the following steps from the VM you created in the previous section:

  1. Install the DCMTK DICOM toolkit software:
         
         sudo apt-get install -y dcmtk
         

  2. Save the DICOM image to the VM. For example, if the DICOM image is stored in a Cloud Storage bucket, run the following command to download it to your current working directory:
         
         gcloud storage cp gs://BUCKET/DCM_FILE .

To use a DICOM image made freely available by Google Cloud from the `gcs-public-data--healthcare-tcia-lidc-idri` dataset, run the following command:
         
         gcloud storage cp gs://gcs-public-data--healthcare-tcia-lidc-idri/dicom/1.3.6.1.4.1.14519.5.2.1.6279.6001.100036212881370097961774473021/1.3.6.1.4.1.14519.5.2.1.6279.6001.130765375502800983459674173881/1.3.6.1.4.1.14519.5.2.1.6279.6001.100395847981751414562031366859.dcm . --billing-project=PROJECT_ID

  3. Run the [`dcmsend`](https://support.dcmtk.org/docs/dcmsend.html) command, which is available through the DCMTK DICOM toolkit. When you run the command, set the Application Entity (AE) Title to `IMPORTADAPTER`. You can optionally add the `--verbose` flag to show processing details. The port used in this guide is 2575.
         
         dcmsend --verbose PEER 2575 DCM_FILE_IN -aec IMPORTADAPTER

Replace the following:

     * PEER: `LoadBalancer Ingress` IP address that was returned when you inspected the Service
     * DCMFILE_IN: path to the DICOM image on the VM

When running `dcmsend` with a single DICOM image, the output is thee following:
    
    I: checking input files ...
    I: starting association #1
    I: initializing network ...
    I: negotiating network association ...
    I: Requesting Association
    I: Association Accepted (Max Send PDV: 16366)
    I: sending SOP instances ...
    I: Sending C-STORE Request (MsgID 1, MR)
    I: Received C-STORE Response (Success)
    I: Releasing Association
    I:
    I: Status Summary
    I: --------------
    I: Number of associations   : 1
    I: Number of pres. contexts : 1
    I: Number of SOP instances  : 1
    I: - sent to the peer       : 1
    I:   * with status SUCCESS  : 1
    

  4. To verify that the DICOM image was successfully imported to your DICOM store. [search for instances](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicomweb#search-dicom) in the DICOM store and ensure that the new DICOM image is in the store.




After completing this section, you have successfully deployed the DICOM adapter to GKE and sent a DICOM image from a PACS instance through the adapter to the Cloud Healthcare API.

## Troubleshoot

### GKE troubleshooting

If the DICOM adapter encounters a failure after you deploy it to GKE, follow the steps in [Troubleshooting issues with deployed workloads](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting#workload_issues).

### Adapter troubleshooting

The import and export adapters generate logs that you can use to diagnose any issues. When you run an adapter using GKE, the logs are stored in [Cloud Logging](https://docs.cloud.google.com/logging/docs). To view the logs, complete the following steps using either the Google Cloud console or the `kubectl` tool:

### Console

  1. Go to the GKE Workloads dashboard in Google Cloud console.

[Go to GKE Workloads](https://console.cloud.google.com/kubernetes/workload)

  2. Select the `dicom-adapter` workload.

  3. In the **Deployment details** page, click **Container logs**.




### kubectl

To see all Pods running in your cluster, run the following command:
    
    
    kubectl get pods
    

Look for the Pod whose name begins with `dicom-adapter`.

To get the Pod's logs, run the following command:
    
    
    kubectl logs POD_NAME

If you missed any of the steps in this guide, the `dcmsend` command might fail to upload images. To investigate this issue, re-run the command with the `-d` flag (for "debug"). The flag prints a more verbose log of actions, including messages that provide information about the failure.

### Permission and authorization troubleshooting

The following sections describe errors that can occur in `dcmsend` when permissions or authorizations are incorrectly configured.

**Note:** Error messages might not display at the end of the `dcmsend` output. You must scan the whole output of `dcmsend` to check for the following error messages.

#### Peer aborted association error

The following issue occurs when network traffic cannot flow from the PACS to port 2575 of the load balancer:
    
    
    cannot send SOP instance: Peer aborted Association (or never connected)
    

To resolve this issue, ensure that the PACS VM and the GKE cluster are running in the same VPC network. If they are not running in the same VPC network, check the following:

  * The load balancer is not configured as "internal."
  * There are no firewall rules blocking connections to port 2575.



This error can also happen when either the load balancer service or the adapter Pod are not correctly set up in the GKE cluster. To ensure that they are correctly set up, review [Inspecting the Deployment](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-connect-pacs#inspecting_the_deployment) and [Inspecting the Service](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-connect-pacs#inspecting_the_service) in this guide.

#### Required APIs not enabled error

The following issue occurs when the Cloud Healthcare API has not been enabled in the project where the GKE cluster with the adapter is running:
    
    
    LO [Http_403, PERMISSION_DENIED, Cloud Healthcare API has not been u]
    

To resolve this issue, ensure all needed APIs are enabled by following the instructions in [Before you begin](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-connect-pacs#before_you_begin).

#### Insufficient scope error

The following issue occurs when the GKE cluster where the adapter is running does not have the correct scope value set:
    
    
    LO [Http_403, PERMISSION_DENIED, Request had insufficient authentica]
    

To resolve this issue, update the GKE cluster or create a new cluster with the following flag:
    
    
    --scopes=https://www.googleapis.com/auth/cloud-healthcare
    

#### DICOM store permission denied error

The following error occurs when the service account used by the GKE cluster where the adapter is running does not have the `roles/healthcare.dicomEditor` role:
    
    
    LO [Http_403, PERMISSION_DENIED, Permission healthcare.dicomStores.d]
    

To resolve this issue, follow the instructions in Granting the Compute Engine service account permissions.

## What's next

After configuring the prototype in this guide, you can start using [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) to encrypt traffic between your PACS and the Cloud Healthcare API.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
