---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/openstack-abm-install/
title: Deploy Distributed Cloud on OpenStack \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:14.280716+00:00
---

# Deploy Distributed Cloud on OpenStack  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/openstack-abm-install/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Deploy Distributed Cloud on OpenStack Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/openstack-abm-install)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/openstack-abm-install)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



Google Distributed Cloud supports using OpenStack as a private cloud platform. This support allows you to use the following OpenStack services:

  * Infrastructure as a Service (IaaS)
  * Load balancing as a Service (LBaaS)
  * Storage



You can deploy Google Distributed Cloud running in OpenStack virtual machines (VMs) with supported operating systems. Google Distributed Cloud doesn't provision the VMs automatically, and provisioning the VMs is outside the scope of this guide. To learn the VM requirements and review an example deployment, [see the Terraform example to create OpenStack VMs](https://github.com/GoogleCloudPlatform/anthos-samples/tree/master/anthos-bm-openstack-terraform#terraform-example-to-create-openstack-vms-for-anthos).

You can use the OpenStack LBaaS and the Kubernetes OpenStack Cloud Provider in Google Distributed Cloud to expose the Kubernetes services outside of the OpenStack cluster.

The guide consists of the following sections:

  1. Deploy Google Distributed Cloud
  2. Configure the [OpenStack Cloud Provider for Kubernetes](https://github.com/kubernetes/cloud-provider-openstack) in Google Distributed Cloud to integrate with the Octavia load balancers
  3. Validate the OpenStack Cloud Provider for Kubernetes integration



This guide uses [OpenStack Ussuri](https://www.openstack.org/software/ussuri/), but it could work with older versions of OpenStack. Older OpenStack versions haven't been tested. The guide uses OpenStack VMs to provide you with a two-node Google Distributed Cloud proof of concept environment running on OpenStack. For information about creating a production environment with a high-availability control plane, see the Google Distributed Cloud documentation for production environment requirements. 

## Example deployment

This guide provides you with an example deployment of Google Distributed Cloud on OpenStack that integrates with OpenStack's LBaaS. You must understand and adjust the commands and configuration values to suit your OpenStack environment. The following diagram shows the resulting deployment:

[ ![Google Distributed Cloud installed on OpenStack.](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/images/openstack-setup.png)](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/images/openstack-setup.png)

## Prerequisites

  * OpenStack Ussuri with LBaaS v2 deployed and functional 
  * Service account for downloading the bmctl tool
  * Configure your OpenStack VMs and network as shown in the example deployment. To provision a similar setup in your OpenStack environment, you have the following options: 
    1. Use this [Terraform script](https://github.com/GoogleCloudPlatform/anthos-samples/tree/master/anthos-bm-openstack-terraform#terraform-example-to-create-openstack-vms-for-anthos) to provision the resources automatically.
    2. Provision the resources manually. 
  * The following OpenStack VMs must be ready and available through SSH:

Name | Usage | IP address  
---|---|---  
abm-ws |  10.200.0.10 **_(private IP)_** floating_ip **_(public IP)_** | Acts as the **admin workstation** It is used to deploy Anthos on bare metal to the other machines.  
abm-cp1 | 10.200.0.11 | **Anthos cluster control plane:** This host runs the Kubernetes control plane and load balancer.  
abm-w1 | 10.200.0.12 | **Anthos cluster worker node:**This host runs the Kubernetes workloads.****  
  
## Deploy Google Distributed Cloud

This section shows you how to complete the following tasks:

  1. Install the tools you need on the `abm-ws` admin workstation VM.
  2. Configure the project ID and service account needed to securely complete the deployment
  3. Create a cluster configuration file
  4. Deploy Google Distributed Cloud

**Warning:** All the commands that follow assumes that the environment for Google Distributed Cloud in OpenStack was setup using this [Terraform script](https://github.com/GoogleCloudPlatform/anthos-samples/tree/master/anthos-bm-openstack-terraform#terraform-example-to-create-openstack-vms-for-anthos). Thus, the names (VM name, Network name, Root user etc.) used in the commands are what is used by the Terraform script. Please adjust the commands according to your setup if you configured the OpenStack environment manually.

### Install the tools you need

  1. Fetch the **public floating IP address** of the `abm-ws` VM.
         
         export OPENSTACK_IPS=$(openstack floating ip list --tags=abm_ws_floatingip -f json)
         export FLOATING_IP=$(jq -c '.[]."Floating IP Address"' <<< $OPENSTACK_IPS | tr -d '"')
         

  2. Ensure you can connect securely into the `abm-ws` VM via SSH and log in as a `root` user. The `root` user as configured by the [Terraform scripts](https://github.com/GoogleCloudPlatform/anthos-samples/tree/master/anthos-bm-openstack-terraform#terraform-example-to-create-openstack-vms-for-anthos) is `abm`.
         
         ssh ubuntu@$FLOATING_IP
         sudo -u abm -i
         

**Note:** If you have public key authentication configured for your VM use the `"-o IdentitiesOnly=yes -i <PATH_TO_KEY>"` flags with the SSH command.
  3. Verify that you can SSH into the other nodes.
         
         ssh abm@10.200.0.11 'echo SSH to $HOSTNAME succeeded'
         ssh abm@10.200.0.12 'echo SSH to $HOSTNAME succeeded'
         

The expected output for the above commands are:
         
         SSH to abm-cp1 succeeded
         SSH to abm-w1 succeeded
         

  4. Download the `kubectl` command line utility on the `abm-ws` VM.
         
         curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
         chmod +x kubectl
         sudo mv kubectl /usr/local/sbin/
         

  5. Install Docker on the `abm-ws` VM.
         
         curl -fsSL https://get.docker.com -o get-docker.sh
         sh get-docker.sh
         sudo usermod -aG docker abm
         newgrp docker
         




### Configure the Google Cloud project and service account

  1. Obtain Google Cloud CLI access credentials for your user account. This will be used when using the `gcloud` commands that follow.
         
         gcloud auth login
         

  2. Make sure the Google Cloud CLI is configured to use the Google Cloud project in which you want your Google Distributed Cloud to be registered.
         
         gcloud config set project PROJECT_ID
         

  3. Set the [Application Default Credentials (ADC)](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/login) for your user account in the admin workstation. This will be used when the `bmctl` tool is used for cluster creation.
         
         gcloud auth application-default login
         

  4. Create the `bm-gcr` service account. You use this service account to authenticate from the Google Distributed Cloud cluster.
         
         gcloud iam service-accounts create bm-gcr
         
         gcloud iam service-accounts keys create bm-gcr.json \
           --iam-account=bm-gcr@PROJECT_ID.iam.gserviceaccount.com
         

  5. Enable the necessary APIs.
         
         gcloud services enable \
           anthos.googleapis.com \
           anthosaudit.googleapis.com \
           anthosgke.googleapis.com \
           cloudresourcemanager.googleapis.com \
           connectgateway.googleapis.com \
           container.googleapis.com \
           gkeconnect.googleapis.com \
           gkehub.googleapis.com \
           gkeonprem.googleapis.com \
           iam.googleapis.com \
           logging.googleapis.com \
           monitoring.googleapis.com \
           opsconfigmonitoring.googleapis.com \
           serviceusage.googleapis.com \
           stackdriver.googleapis.com \
           storage.googleapis.com
         

  6. Give additional permissions to the `bm-gcr` service account. Adding the permissions means you don't need to create multiple service accounts for individual services.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member="serviceAccount:bm-gcr@PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/gkehub.connect"
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member="serviceAccount:bm-gcr@PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/gkehub.admin"
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member="serviceAccount:bm-gcr@PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/logging.logWriter"
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member="serviceAccount:bm-gcr@PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/monitoring.metricWriter"
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member="serviceAccount:bm-gcr@PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/monitoring.dashboardEditor"
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member="serviceAccount:bm-gcr@PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/stackdriver.resourceMetadata.writer"
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member="serviceAccount:bm-gcr@PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/opsconfigmonitoring.resourceMetadata.writer"
         




### Create a cluster configuration file

  1. Download the `bmctl` command line utility.
         
         mkdir baremetal && cd baremetal
         gcloud storage cp gs://anthos-baremetal-release/bmctl/1.16.8/linux-amd64/bmctl .
         chmod a+x bmctl
         sudo mv bmctl /usr/local/sbin/
         

  2. Create a Google Distributed Cloud workspace for your cluster.
         
         bmctl create config -c CLUSTER_NAME
         

  3. Create the configuration file for your Google Distributed Cloud cluster.
         
         cat > bmctl-workspace/CLUSTER_NAME/CLUSTER_NAME.yaml << EOB
         ---
         gcrKeyPath: /home/abm/bm-gcr.json
         sshPrivateKeyPath: /home/abm/.ssh/id_rsa
         gkeConnectAgentServiceAccountKeyPath: /home/abm/bm-gcr.json
         gkeConnectRegisterServiceAccountKeyPath: /home/abm/bm-gcr.json
         cloudOperationsServiceAccountKeyPath: /home/abm/bm-gcr.json
         ---
         apiVersion: v1
         kind: Namespace
         metadata:
           name: openstack-cluster-ns
         ---
         apiVersion: baremetal.cluster.gke.io/v1
         kind: Cluster
         metadata:
           name: CLUSTER_NAME
           namespace: openstack-cluster-ns
           annotations:
             baremetal.cluster.gke.io/external-cloud-provider: "true"
         spec:
           type: hybrid
           anthosBareMetalVersion: 1.16.8
           gkeConnect:
             projectID: PROJECT_ID
           controlPlane:
             nodePoolSpec:
               clusterName: CLUSTER_NAME
               nodes:
               - address: 10.200.0.11
           clusterNetwork:
             pods:
               cidrBlocks:
               - 192.168.0.0/16
             services:
               cidrBlocks:
               - 10.96.0.0/20
           loadBalancer:
             mode: manual
             ports:
               controlPlaneLBPort: 443
             vips:
               controlPlaneVIP: 10.200.0.101
               ingressVIP: 10.200.0.102
           clusterOperations:
             location: us-central1
             projectID: PROJECT_ID
           storage:
             lvpNodeMounts:
               path: /mnt/localpv-disk
               storageClassName: node-disk
             lvpShare:
               numPVUnderSharedPath: 5
               path: /mnt/localpv-share
               storageClassName: standard
           nodeAccess:
             loginUser: abm
         
         ---
         apiVersion: baremetal.cluster.gke.io/v1
         kind: NodePool
         metadata:
           name: node-pool-1
           namespace: openstack-cluster-ns
         spec:
           clusterName: CLUSTER_NAME
           nodes:
           - address: 10.200.0.12
         EOB
         




### Deploy

  1. Deploy the cluster.
         
         bmctl create cluster -c CLUSTER_NAME
         




Running the `bmctl` command starts setting up a new hybrid cluster. This includes doing preflight checks on the nodes, creating the admin and user clusters and also registering the cluster with Google Cloud using [Connect](https://docs.cloud.google.com/anthos/multicluster-management/connect/overview). The whole setup can take up to 15 minutes. You see the following output as the cluster is being created:
    
    
    Please check the logs at bmctl-workspace/CLUSTER_NAME/log/create-cluster-20210926-020741/create-cluster.log
    [2021-09-26 02:07:59+0000] Creating bootstrap cluster... ⠦ kind get kubeconfig --name bmctl > ~/.kube/config && k get pods --all-namespaces
    [2021-09-26 02:07:59+0000] Creating bootstrap cluster... OK
    [2021-09-26 02:10:48+0000] Installing dependency components... OK
    [2021-09-26 02:13:42+0000] Waiting for preflight check job to finish... OK
    [2021-09-26 02:15:22+0000] - Validation Category: machines and network
    [2021-09-26 02:15:22+0000]  - [PASSED] gcp
    [2021-09-26 02:15:22+0000]  - [PASSED] node-network
    [2021-09-26 02:15:22+0000]  - [PASSED] 10.200.0.11
    [2021-09-26 02:15:22+0000]  - [PASSED] 10.200.0.11-gcp
    [2021-09-26 02:15:22+0000]  - [PASSED] 10.200.0.12
    [2021-09-26 02:15:22+0000]  - [PASSED] 10.200.0.12-gcp
    [2021-09-26 02:15:22+0000] Flushing logs... OK
    [2021-09-26 02:15:23+0000] Applying resources for new cluster
    [2021-09-26 02:15:24+0000] Waiting for cluster to become ready OK
    [2021-09-26 02:25:04+0000] Writing kubeconfig file
    [2021-09-26 02:25:04+0000] kubeconfig of created cluster is at bmctl-workspace/CLUSTER_NAME/CLUSTER_NAME-kubeconfig, please run
    [2021-09-26 02:25:04+0000] kubectl --kubeconfig bmctl-workspace/CLUSTER_NAME/CLUSTER_NAME-kubeconfig get nodes
    [2021-09-26 02:25:04+0000] to get cluster node status.
    [2021-09-26 02:25:04+0000] Please restrict access to this file as it contains authentication credentials of your cluster.
    [2021-09-26 02:25:04+0000] Waiting for node pools to become ready OK
    [2021-09-26 02:25:24+0000] Moving admin cluster resources to the created admin cluster
    [2021-09-26 02:25:53+0000] Flushing logs... OK
    [2021-09-26 02:25:53+0000] Deleting bootstrap cluster...
    

## Verify and interact with the cluster

You can find your cluster's `kubeconfig` file on the `abm-ws` VM inside the `bmctl-workspace` directory. To verify your deployment, complete the following steps.

  1. Set the `KUBECONFIG` environment variable with the path to the cluster's configuration file to run `kubectl` commands on the cluster:
         
         export KUBECONFIG=$HOME/bmctl-workspace/CLUSTER_NAME/CLUSTER_NAME-kubeconfig
         kubectl get nodes
         

You should see the nodes of the cluster printed, similar to the following output:
         
         NAME      STATUS   ROLES                  AGE     VERSION
         abm-cp1   Ready    control-plane,master   5m24s   v1.20.5-gke.1301
         abm-w1    Ready    <none>                 2m17s   v1.20.5-gke.1301  
         




## Log in to your cluster from Google Cloud console

To observe your workloads in the Google Cloud console, you must log in to the cluster. For instructions and more information about logging into your cluster, see [Logging in to a cluster from Google Cloud console](https://docs.cloud.google.com/anthos/multicluster-management/console/logging-in).

## Clean up

You can clean up the cluster by issuing the following command in your admin workstation (`abm-ws`) VM.
    
    
    export KUBECONFIG=$HOME/bmctl-workspace/CLUSTER_NAME/CLUSTER_NAME-kubeconfig
    bmctl reset --cluster CLUSTER_NAME
    

## What's next?

You can now install the **OpenStack Cloud Provider** on the newly created Google Distributed Cloud cluster by following the [Configure the OpenStack Cloud Provider for Kubernetes](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/openstack-k8s-provider) guide. This enables you to expose your applications using a `LoadBalancer` type service, leveraging [OpenStack's LBaaS](https://docs.openstack.org/mitaka/networking-guide/config-lbaas.html).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
