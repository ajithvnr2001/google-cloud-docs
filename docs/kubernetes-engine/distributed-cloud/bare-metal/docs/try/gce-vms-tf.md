---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/try/gce-vms-tf/
title: Create a Google Distributed Cloud hybrid cluster on Compute Engine VMs using Terraform \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:48.881060+00:00
---

# Create a Google Distributed Cloud hybrid cluster on Compute Engine VMs using Terraform  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/try/gce-vms-tf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Create a Google Distributed Cloud hybrid cluster on Compute Engine VMs using Terraform Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to set up VMs on Compute Engine with Terraform so that you can install and try Google Distributed Cloud in high availability (HA) mode. For information about how to use the Google Cloud CLI for this, see [Try Google Distributed Cloud on Compute Engine VMs](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/try/gce-vms).

**Important:** This deployment is for evaluation purposes only. Don't run Google Distributed Cloud on Compute Engine VMs in production. To deploy Google Distributed Cloud in production, follow the steps in our [quickstart](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/quickstart).

You can try out Google Distributed Cloud quickly and without having to prepare any hardware. The provided Terraform scripts create a network of VMs on Compute Engine that can be used to run Google Distributed Cloud. In this tutorial we use the [hybrid cluster deployment](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/install-prep#hybrid_cluster_deployment) model.

Complete the following steps to get a sample cluster running:

  1. Execute the Terraform script to set up a network of VMs on Compute Engine
  2. Deploy a hybrid cluster
  3. Verify your cluster



## Before you begin

The deployment requires the following resources:

  * One workstation with access to the internet and the following tools installed: [Git](https://www.atlassian.com/git/tutorials/install-git), [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) and [Terraform](https://releases.hashicorp.com/terraform/1.1.9/) (>= v0.15.5, < 1.2).
  * A Google Cloud project.

[Go to project select](https://console.cloud.google.com/projectselector2/home/dashboard)

  * A service account in the project that satisfies one of the following requirements and its [key file downloaded](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys) to the workstation:

    1. The service account has Owner permissions
    2. The service account has both Editor and Project IAM Admin permissions

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)


**Note:** All the commands are run on the workstation that has Git, Google Cloud CLI, Terraform (~v0.14.10) installed and the service account key downloaded.

## Set up the VM network on Compute Engine

In this section you use the Terraform scripts from the [anthos-samples](https://github.com/GoogleCloudPlatform/anthos-samples) repository. The scripts configure Compute Engine with the following resources:

  * Six VMs to deploy the hybrid cluster: 
    * One admin VM used to deploy the hybrid cluster to the other machines.
    * Three VMs for the three control plane nodes needed to run the hybrid cluster control plane.
    * Two VMs for the two worker nodes needed to run workloads on the hybrid cluster.
  * A `VxLAN` overlay network between all the nodes to emulate L2 connectivity.
  * SSH access to the **_control-plane_** and **_worker_** nodes from the **_admin VM_**.

**Note:** Since we use SSH keys for Compute Engine VM login, [`oslogin` has been disabled](https://github.com/GoogleCloudPlatform/anthos-samples/blob/v0.8.0/anthos-bm-gcp-terraform/main.tf#L117) for these machines.

![Bare metal infrastructure on Google Cloud using Compute Engine VMs](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/images/abm_gcp_infra.svg)

You can change the number of nodes in the cluster by adding new node names to the `instance_count` Terraform variable: 
    
    
    ###################################################################################
    # The recommended instance count for High Availability (HA) is 3 for Control plane
    # and 2 for Worker nodes.
    ###################################################################################
    variable "instance_count" {
      description = "Number of instances to provision per layer (Control plane and Worker nodes) of the cluster"
      type        = map(any)
      default = {
        "controlplane" : 3
        "worker" : 2
      }
    }

  1. Download the Terraform scripts for `anthos-bm-gcp-terraform` sample:
         
         git clone https://github.com/GoogleCloudPlatform/anthos-samples
         cd anthos-samples/anthos-bm-gcp-terraform
         

  2. Update the `terraform.tfvars.sample` file to include variables specific to your environment:
         
         project_id       = "PROJECT_ID"
         region           = "GOOGLE_CLOUD_REGION"
         zone             = "GOOGLE_CLOUD_ZONE"
         credentials_file = "PATH_TO_GOOGLE_CLOUD_SERVICE_ACCOUNT_KEY_FILE"
         

  3. Rename the `terraform.tfvars.sample` file to the default name used by terraform for the variables file:
         
         mv terraform.tfvars.sample terraform.tfvars
         

**Note:** Note: You can skip renaming the variables file if you use the `-var-file` flag to explicitly reference the file when you run `terraform apply` later in this procedure.
  4. Initialize the sample directory as a Terraform working directory. This sets up the required Terraform state management configurations, similar to `git init`:
         
         terraform init
         

  5. Create a Terraform execution plan. This step compares the state of the resources, verifies the scripts and creates an execution plan:
         
         terraform plan
         

  6. Apply the changes described in the Terraform script. This step executes the plan on the given provider _(in this case Google Cloud)_ to reach the targeted state of resources:
         
         terraform apply  # when prompted to confirm the Terraform plan, type 'Yes' and enter
         

**Note:** The `apply` command sets up the Compute Engine VMs based infrastructure. This can take a few minutes (approximately 3-5 mins) for the entire bare-metal cluster to be set up.



## Deploy the hybrid cluster

After the Terraform execution completes you are ready to deploy the hybrid cluster.

  1. Use SSH to connect to the admin host:
         
         gcloud compute ssh tfadmin@cluster1-abm-ws0-001 --project=PROJECT_ID --zone=GOOGLE_CLOUD_ZONE
         

You can ignore any messages about updating the VM and complete this tutorial. If you plan to keep the VMs as a test environment, you might want to update the OS or upgrade to the next release as described in the [Ubuntu documentation](https://ubuntu.com/server/docs/upgrade-introduction).

  2. Run the following code block to create the `cluster1` hybrid cluster on the configured Compute Engine VMs:
         
         sudo ./run_initialization_checks.sh && \
         sudo bmctl create config -c cluster1 && \
         sudo cp ~/cluster1.yaml bmctl-workspace/cluster1 && \
         sudo bmctl create cluster -c cluster1
         




Running the `bmctl` command starts setting up a new hybrid cluster. This includes doing preflight checks on the nodes, creating the admin and user clusters and also registering the cluster with Google Cloud using [Connect Agent](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent). The whole setup can take up to 15 minutes. You see the following output as the cluster is being created:

**Note:** The logs for checks on node initialization have been left out. They appear before the following logs from the hybrid cluster setup:
    
    
        Created config: bmctl-workspace/cluster1/cluster1.yaml
        Creating bootstrap cluster... OK
        Installing dependency components... OK
        Waiting for preflight check job to finish... OK
        - Validation Category: machines and network
                - [PASSED] 10.200.0.3
                - [PASSED] 10.200.0.4
                - [PASSED] 10.200.0.5
                - [PASSED] 10.200.0.6
                - [PASSED] 10.200.0.7
                - [PASSED] gcp
                - [PASSED] node-network
        Flushing logs... OK
        Applying resources for new cluster
        Waiting for cluster to become ready OK
        Writing kubeconfig file
        kubeconfig of created cluster is at bmctl-workspace/cluster1/cluster1-kubeconfig, please run
        kubectl --kubeconfig bmctl-workspace/cluster1/cluster1-kubeconfig get nodes
        to get cluster node status.
        Please restrict access to this file as it contains authentication credentials of your cluster.
        Waiting for node pools to become ready OK
        Moving admin cluster resources to the created admin cluster
        Flushing logs... OK
        Deleting bootstrap cluster... OK
    

## Verify and interact with the cluster

You can find your cluster's `kubeconfig` file on the admin machine in the `bmctl-workspace` directory. To verify your deployment, complete the following steps.

  1. If you disconnected from the admin host, use SSH to connect to the host:
         
         # You can copy the command from the output of the Terraform execution above
         gcloud compute ssh tfadmin@cluster1-abm-ws0-001 --project=PROJECT_ID --zone=GOOGLE_CLOUD_ZONE
         

  2. Set the `KUBECONFIG` environment variable with the path to the cluster's configuration file to run `kubectl` commands on the cluster:
         
         export CLUSTER_ID=cluster1
         export KUBECONFIG=$HOME/bmctl-workspace/$CLUSTER_ID/$CLUSTER_ID-kubeconfig
         kubectl get nodes
         

You should see the nodes of the cluster printed, similar to the following output:
         
         NAME          STATUS   ROLES    AGE   VERSION
         cluster1-abm-cp1-001   Ready    master   17m   v1.18.6-gke.6600
         cluster1-abm-cp2-001   Ready    master   16m   v1.18.6-gke.6600
         cluster1-abm-cp3-001   Ready    master   16m   v1.18.6-gke.6600
         cluster1-abm-w1-001    Ready    <none>   14m   v1.18.6-gke.6600
         cluster1-abm-w2-001    Ready    <none>   14m   v1.18.6-gke.6600
         




## Log in to your cluster from Google Cloud console

To observe your workloads in the Google Cloud console, you must log in to the cluster.

For instructions and more information about logging into your cluster, see [Work with clusters from the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/console).

## Clean up

You can clean up the cluster setup in two ways.

###  Console 

  * If you created a dedicated project for this procedure, delete the Google Cloud project from the Google Cloud console.   


[Delete Project](https://console.cloud.google.com/cloud-resource-manager)




###  Terraform 

  * Unregister the cluster before deleting all the resources created by Terraform.


    
    
    # Use SSH to connect to the admin host
    gcloud compute ssh tfadmin@cluster1-abm-ws0-001 --project=PROJECT_ID --zone=GOOGLE_CLOUD_ZONE
    
    # Reset the cluster
    export CLUSTER_ID=cluster1
    export KUBECONFIG=$HOME/bmctl-workspace/$CLUSTER_ID/$CLUSTER_ID-kubeconfig
    sudo bmctl reset --cluster $CLUSTER_ID
    
    # log out of the admin host
    exit
    

  * Use Terraform to delete all resources.


    
    
    terraform destroy --auto-approve
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
