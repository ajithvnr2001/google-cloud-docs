---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/openstack-abm-install/
title: Deploy a cluster on OpenStack \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:40.845601+00:00
---

# Deploy a cluster on OpenStack  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/openstack-abm-install/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Deploy a cluster on OpenStack Stay organized with collections  Save and categorize content based on your preferences. 

Distributed Cloud software only for bare metal lets you deploy a hybrid cluster on OpenStack virtual machines (VMs). This deployment lets you integrate OpenStack Load Balancing as a Service (LBaaS) and the [OpenStack Cloud Provider for Kubernetes](https://github.com/kubernetes/cloud-provider-openstack) to expose Kubernetes services outside your OpenStack environment.

Google Distributed Cloud doesn't provision OpenStack VMs automatically. To review VM requirements and configure the two-node proof-of-concept environment, see the [Terraform example to create OpenStack VMs](https://github.com/GoogleCloudPlatform/anthos-samples/tree/master/anthos-bm-openstack-terraform#terraform-example-to-create-openstack-vms-for-anthos). Although this deployment demonstrates [OpenStack Ussuri](https://www.openstack.org/software/ussuri/), Google Distributed Cloud doesn't require a specific OpenStack version. For production environments, see the [installation prerequisites](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/install-prereq).

## Example deployment

This guide provides you with an example deployment of a bare metal cluster on OpenStack that integrates with OpenStack LBaaS. You must understand and adjust the commands and configuration values to suit your OpenStack environment. The following diagram shows the resulting deployment:

![Google Distributed Cloud installed on OpenStack.](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/images/openstack-setup.png)

## Prerequisites

  * OpenStack Ussuri with LBaaS v2 deployed and functional
  * Service account for downloading the bmctl tool
  * Configure your OpenStack VMs and network as shown in the example deployment. To provision a similar setup in your OpenStack environment, you have the following options: 
    1. Use this [Terraform script](https://github.com/GoogleCloudPlatform/anthos-samples/tree/master/anthos-bm-openstack-terraform#terraform-example-to-create-openstack-vms-for-anthos) to provision the resources automatically.
    2. Provision the resources manually.
  * The following OpenStack VMs must be ready and available through SSH:

Name | IP address | Purpose  
---|---|---  
abm-ws |  10.200.0.10 **_(private IP)_**  
floating_ip **_(public IP)_** | Acts as the **admin workstation** : It's used to deploy Google Distributed Cloud to the other machines.  
abm-cp1 | 10.200.0.11 | **Cluster control plane:** This host runs the Kubernetes control plane and load balancer.  
abm-w1 | 10.200.0.12 | **Cluster worker node:** This host runs the Kubernetes workloads.  
  
## Deploy Google Distributed Cloud

This section shows you how to complete the following tasks:

  1. Install the tools you need on the `abm-ws` admin workstation VM.
  2. Configure the project ID and service account needed to securely complete the deployment
  3. Create a cluster configuration file
  4. Create a cluster

**Warning:** The commands in this guide are based on the assumption that the environment for Google Distributed Cloud in OpenStack was set up using the supplied [Terraform script](https://github.com/GoogleCloudPlatform/anthos-samples/tree/master/anthos-bm-openstack-terraform#terraform-example-to-create-openstack-vms-for-anthos). The names (for example, VM name, network name, root user name) used in the commands match what is used by the Terraform script. If you configured the OpenStack environment manually, adjust the commands according to your setup.

### Install the tools you need

  1. Fetch the **public floating IP address** of the `abm-ws` VM:
         
         export OPENSTACK_IPS=$(openstack floating ip list --tags=abm_ws_floatingip -f json)
         export FLOATING_IP=$(jq -c '.[]."Floating IP Address"' <<< $OPENSTACK_IPS | tr -d '"')
         

  2. Ensure you can use SSH to connect securely into the `abm-ws` VM and sign in as a `root` user. The `root` user configured by the [Terraform scripts](https://github.com/GoogleCloudPlatform/anthos-samples/tree/master/anthos-bm-openstack-terraform#terraform-example-to-create-openstack-vms-for-anthos) is `abm`.
         
         ssh ubuntu@$FLOATING_IP
         sudo -u abm -i
         

**Note:** If you have public key authentication configured for your VM use the `"-o IdentitiesOnly=yes -i <PATH_TO_KEY>"` flags with the SSH command.
  3. Verify that you can use SSH to connect to the other nodes:
         
         ssh abm@10.200.0.11 'echo SSH to $HOSTNAME succeeded'
         ssh abm@10.200.0.12 'echo SSH to $HOSTNAME succeeded'
         

The expected responses for the preceding commands are:
         
         SSH to abm-cp1 succeeded
         SSH to abm-w1 succeeded
         

  4. Download the `kubectl` command line utility on the `abm-ws` VM.
         
         curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
         chmod +x kubectl
         sudo mv kubectl /usr/local/sbin/
         

  5. Install Docker on the `abm-ws` VM:
         
         curl -fsSL https://get.docker.com -o get-docker.sh
         sh get-docker.sh
         sudo usermod -aG docker abm
         newgrp docker
         




### Configure the Google Cloud project and service account

  1. Obtain Google Cloud CLI access credentials for your user account.

These credentials are used with subsequent `gcloud` commands.
         
         gcloud auth login
         

  2. Make sure the Google Cloud CLI is configured to use the Google Cloud project in which you want your cluster to be registered.
         
         gcloud config set project PROJECT_ID
         

  3. Set the [Application Default Credentials (ADC)](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/login) for your user account in the admin workstation. This will be used when the `bmctl` tool is used for cluster creation.
         
         gcloud auth application-default login
         

  4. Create the `bm-gcr` service account. You use this service account to authenticate from the cluster.
         
         gcloud iam service-accounts create bm-gcr
         gcloud iam service-accounts keys create bm-gcr.json \
             --iam-account=bm-gcr@PROJECT_ID.iam.gserviceaccount.com
         

  5. Enable the necessary APIs:
         
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
         gcloud storage cp gs://anthos-baremetal-release/bmctl/1.36.200-gke.118/linux-amd64/bmctl .
         chmod a+x bmctl
         sudo mv bmctl /usr/local/sbin/
         

  2. Create a cluster configuration file for your cluster:
         
         bmctl create config -c CLUSTER_NAME
         

  3. Update the configuration file for use with OpenStack:
         
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
           anthosBareMetalVersion: 1.36.200-gke.118
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
         




### Create the cluster

  1. Create the cluster:
         
         bmctl create cluster -c CLUSTER_NAME
         




Running the `bmctl` command starts setting up a new hybrid cluster. This includes doing preflight checks on the nodes, creating the admin and user clusters and also registering the cluster with Google Cloud using [Connect Agent](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent). The whole setup can take up to 15 minutes. You see the following output as the cluster is being created:
    
    
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

You can find your cluster `kubeconfig` file on the `abm-ws` VM inside the `bmctl-workspace` directory. To verify your deployment, complete the following steps:

  1. Set the `KUBECONFIG` environment variable with the path to the cluster configuration file to run `kubectl` commands on the cluster:
         
         export KUBECONFIG=$HOME/bmctl-workspace/CLUSTER_NAME/CLUSTER_NAME-kubeconfig
         kubectl get nodes
         

You should see the nodes of the cluster printed, similar to the following output:
         
         NAME      STATUS   ROLES                  AGE     VERSION
         abm-cp1   Ready    control-plane,master   5m24s   v1.20.5-gke.1301
         abm-w1    Ready    <none>                 2m17s   v1.20.5-gke.1301
         




## Sign in to your cluster from Google Cloud console

To observe your workloads in the Google Cloud console, you must sign in to the cluster. For instructions and more information about signing in to your cluster, see [Work with clusters from the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/console).

## Clean up

You can clean up the cluster by issuing the following command in your admin workstation (`abm-ws`) VM:

**Note:** If you want to install the OpenStack Cloud Provider on the newly created cluster, follow the [Configure the OpenStack Cloud Provider for Kubernetes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/openstack-k8s-provider) guide before you clean up.
    
    
    export KUBECONFIG=$HOME/bmctl-workspace/CLUSTER_NAME/CLUSTER_NAME-kubeconfig
    bmctl reset --cluster CLUSTER_NAME
    

## What's next?

  * To install the OpenStack Cloud Provider on the newly created cluster, follow the [Configure the OpenStack Cloud Provider for Kubernetes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/openstack-k8s-provider) guide.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
