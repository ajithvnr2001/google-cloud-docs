---
url: https://docs.cloud.google.com/nat/docs/gke-example/
title: Use Public NAT with GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:43.977742+00:00
---

# Use Public NAT with GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nat/docs/gke-example/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NAT ](https://docs.cloud.google.com/nat/docs)
  * [ Guides ](https://docs.cloud.google.com/nat/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use Public NAT with GKE

This page shows you how to configure a sample Public NAT setup with Google Kubernetes Engine (GKE). Before setting up Public NAT, read the [Public NAT overview](https://docs.cloud.google.com/nat/docs/public-nat).

## Prerequisites

You need to do the following before setting up Public NAT.

### Get IAM permissions

The [roles/compute.networkAdmin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute) role gives you permissions to create a NAT gateway on Cloud Router, reserve and assign NAT IP addresses, and specify subnetworks (subnets) whose traffic should use network address translation by the NAT gateway.

### Set up Google Cloud

Before you get started, set up the following items in Google Cloud.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




**Note:**

The Google Cloud CLI instructions on this page assume that you have set your project ID before issuing commands. You can set a project ID with the following command:
    
    
        gcloud config set project PROJECT_ID
      

You can also view a project ID that is already set:
    
    
        gcloud config list --format='text(core.project)'
      

## Setting up the GKE example

Use this example if you want to see a simple Public NAT configuration working with GKE.

### Step 1: Create a VPC network and subnet

If you already have a network and subnet, you can skip this step.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to the VPC networks page](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. Enter a **Name** of `custom-network1`.

  4. Under **Subnets** , set **Subnet creation mode** to **Custom**.

  5. Under **New subnet** , enter a **Name** of `subnet-us-east-192`.

  6. In **Region** , select **us-east4**.

  7. Enter an **IP address range** of `192.168.1.0/24`.

  8. Click **Done** , and then click **Create**.




###  gcloud 

  1. Create a new custom mode Virtual Private Cloud (VPC) network in your project:
         
         gcloud compute networks create custom-network1 \
             --subnet-mode custom

Output: 
         
         NAME             MODE     IPV4_RANGE   GATEWAY_IPV4
         custom-network1  custom

**Note:** Because this is a VPC network, there is no network-level IPv4 range or gateway IP address, so none is displayed.
  2. Specify the subnet prefix for your first region. In this example, we assign `192.168.1.0/24` to region `us-east4`.
         
         gcloud compute networks subnets create subnet-us-east-192 \
            --network custom-network1 \
            --region us-east4 \
            --range 192.168.1.0/24

Output: 
         
         NAME                REGION    NETWORK          RANGE
         subnet-us-east-192  us-east4  custom-network1  192.168.1.0/24




### Terraform

You can use a [Terraform module](https://github.com/terraform-google-modules/terraform-google-cloud-network) to create a custom Virtual Private Cloud network and subnet.
    
    
    module "test-vpc-module" {
      source       = "terraform-google-modules/network/google"
      version      = "~> 13.0"
      project_id   = var.project_id # Replace this with your project ID in quotes
      network_name = "custom-network1"
      mtu          = 1460
    
      subnets = [
        {
          subnet_name   = "subnet-us-east-192"
          subnet_ip     = "192.168.1.0/24"
          subnet_region = "us-east4"
        }
      ]
    }

### Step 2: Create a private cluster

###  Console 

  1. In the Google Cloud console, go to the **Kubernetes clusters** page.

[Go to the Kubernetes clusters page](https://console.cloud.google.com/kubernetes/list)

  2. Click **Create cluster**.

  3. For **Name** , enter `nat-test-cluster`.

  4. Set the **Location type** to **Zonal**.

  5. Set the **Zone** to **us-east4-c**.

  6. In the navigation pane, click **Networking**.

  7. Select **Private cluster**.

  8. Clear the **Access control plane using its external IP address** checkbox.

  9. Enter a **Control plane IP range** of `172.16.0.0/28`.

  10. Set **Network** to **`custom-network1`**.

  11. To create and start the cluster, click **Create**.




###  gcloud 
    
    
    gcloud container clusters create "nat-test-cluster" \
        --zone "us-east4-c" \
        --cluster-version "latest" \
        --machine-type "e2-medium" \
        --disk-type "pd-standard" \
        --disk-size "100" \
        --scopes "https://www.googleapis.com/auth/compute","https://www.googleapis.com/auth/devstorage.read_only","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring","https://www.googleapis.com/auth/servicecontrol","https://www.googleapis.com/auth/service.management.readonly","https://www.googleapis.com/auth/trace.append" \
        --num-nodes "3" \
        --enable-private-nodes \
        --enable-private-endpoint \
        --master-ipv4-cidr "172.16.0.0/28" \
        --enable-ip-alias \
        --network "projects/PROJECT_ID/global/networks/custom-network1" \
        --subnetwork "projects/PROJECT_ID/regions/us-east4/subnetworks/subnet-us-east-192" \
        --max-nodes-per-pool "110" \
        --enable-master-authorized-networks \
        --addons HorizontalPodAutoscaling,HttpLoadBalancing \
        --enable-autoupgrade \
        --enable-autorepair
    

### Terraform

You can use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster) to create a private cluster.
    
    
    resource "google_container_cluster" "primary" {
      project            = var.project_id
      name               = "nat-test-cluster"
      location           = "us-east4-c"
      initial_node_count = 3
      network            = var.network # Replace with a reference or self link to your network, in quotes
      subnetwork         = var.subnet  # Replace with a reference or self link to your subnet, in quotes
      private_cluster_config {
        master_ipv4_cidr_block  = "172.16.0.0/28"
        enable_private_endpoint = true
        enable_private_nodes    = true
      }
      ip_allocation_policy {
      }
      master_authorized_networks_config {
      }
    }

### Step 3: Create a firewall rule that allows SSH connections

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to the Firewall policies page](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. Click **Create firewall rule**.

  3. Enter a **Name** of `allow-ssh`.

  4. Specify a **Network** of **`custom-network1`**.

  5. Set **Direction of traffic** to **Ingress**.

  6. Set **Action on match** to **Allow**.

  7. Set **Targets** to **All instances in the network**.

  8. Set **Source filter** to **IPv4 ranges**.

  9. Set **Source IP ranges** to `35.235.240.0/20`.

  10. Set **Protocols and ports** to **Specified protocols and ports**.

  11. Select the **tcp** checkbox and enter port `22`.

  12. Click **Create**.




###  gcloud 
    
    
    gcloud compute firewall-rules create allow-ssh \
        --network custom-network1 \
        --source-ranges 35.235.240.0/20 \
        --allow tcp:22

### Terraform

You can use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_firewall) to create a firewall rule.
    
    
    resource "google_compute_firewall" "rules" {
      project = var.project_id
      name    = "allow-ssh"
      network = var.network
      allow {
        protocol = "tcp"
        ports    = ["22"]
      }
      source_ranges = ["35.235.240.0/20"]
    }

### Step 4: Create IAP SSH permissions for one of your nodes

In a later step, use IAP to connect to your node.

###  Console 

  1. In the Google Cloud console, go to the **Identity-Aware Proxy** page.

[Go to the Identity-Aware Proxy page](https://console.cloud.google.com/security/iap)

  2. Select the **SSH and TCP resources** tab.

  3. Select the checkbox next to the first node in the list under **All Tunnel Resources > us-east4-c**. Its name will be similar to `gke-nat-test-cluster-default-pool-b50db58d-075t`.

  4. Write down the name of the node; later you'll use it to test connectivity.

  5. In the right pane, click **Add principal**.

  6. To grant users, groups, or service accounts access to the resources, in the **New principals** field, specify their email addresses.

If you are just testing this feature, you can enter your own email address.

  7. To grant the principals access to the resources through Cloud IAP's TCP forwarding feature, in the **Role** drop-down list, select **Cloud IAP > IAP-secured Tunnel User**.

  8. Click **Save**.




###  gcloud 

For this step, use the **Console** instructions.

### Step 5: Log in to the node and confirm that it cannot reach the internet

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Find the node that you created IAP SSH permissions for. In the **Connect** column, click the **SSH** drop-down arrow, and then select **Open in browser window**.

If this is the first time that you are connecting to the instance, Google Cloud generates the SSH keys for you.

  3. From the node prompt, find the process ID of the `kube-dns` container:
         
         pgrep '^kube-dns$'

  4. Access the container:
         
         sudo nsenter --target PROCESS_ID --net /bin/bash

  5. From `kube-dns`, attempt to connect to the internet:
         
         curl example.com

You should get no result. If you do, you might not have created your cluster as a private cluster, or there might be some other problem. To troubleshoot, see [VMs can reach the internet unexpectedly without Public NAT](https://docs.cloud.google.com/nat/docs/troubleshooting#internet-wo-nat).

To end the command, you might have to enter `Ctrl+C`.




###  gcloud 

  1. Find the name of one of your cluster nodes:
         
         gcloud compute instances list

A node name looks something like `gke-nat-test-cluster-default-pool-1a4cbd06-3m8v`. Make a note of the node name and use that name wherever you see `NODE_NAME` in the following commands.

  2. Connect to the node:
         
         gcloud compute ssh NODE_NAME \
             --zone us-east4-c \
             --tunnel-through-iap

  3. From the node prompt, find the process ID of the `kube-dns` container:
         
         pgrep '^kube-dns$'

  4. Access the container:
         
         sudo nsenter --target PROCESS_ID --net /bin/bash

  5. From `kube-dns`, attempt to connect to the internet:
         
         curl example.com

You should get no result.To end the command, you might have to enter `Ctrl+C`.




### Step 6: Create a NAT configuration using Cloud Router

You must create the Cloud Router in the same region as the instances that use Public NAT. Public NAT is only used to place NAT information onto the VMs. It is not used as part of the actual NAT gateway.

This configuration allows all instances in the region to use Public NAT for all primary and [alias IP ranges](https://docs.cloud.google.com/vpc/docs/alias-ip). It also automatically allocates the external IP addresses for the NAT gateway. For more options, see the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers) documentation.

**Note:** Public NAT uses Cloud Router only to group NAT configuration information (control plane). Public NAT does not direct a Cloud Router to use BGP or to add routes. NAT traffic _does not pass through_ a Cloud Router (data plane).

###  Console 

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to the Cloud NAT page](https://console.cloud.google.com/net-services/nat/list)

  2. Click **Get started** or **Create NAT gateway**.

  3. Enter a **Gateway name** of `nat-config`.

  4. Set the **VPC network** to **`custom-network1`**.

  5. Set the **Region** to **us-east4**.

  6. Under **Cloud Router** , select **Create new router**.

     1. Enter a **Name** of `nat-router`.
     2. Click **Create**.
  7. Click **Create**.




###  gcloud 

  1. Create a Cloud Router:
         
         gcloud compute routers create nat-router \
             --network custom-network1 \
             --region us-east4

  2. Add a configuration to the router:
         
         gcloud compute routers nats create nat-config \
             --router-region us-east4 \
             --router nat-router \
             --nat-all-subnet-ip-ranges \
             --auto-allocate-nat-external-ips




### Terraform

You can use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_router) to create a Cloud Router.
    
    
    resource "google_compute_router" "router" {
      project = var.project_id
      name    = "nat-router"
      network = var.network
      region  = "us-east4"
    }

You can use a [Terraform module](https://github.com/terraform-google-modules/terraform-google-cloud-nat) to create a NAT configuration.
    
    
    module "cloud-nat" {
      source                             = "terraform-google-modules/cloud-nat/google"
      version                            = "~> 5.0"
      project_id                         = var.project_id
      region                             = "us-east4"
      router                             = google_compute_router.router.name
      name                               = "nat-config"
      source_subnetwork_ip_ranges_to_nat = "ALL_SUBNETWORKS_ALL_IP_RANGES"
    }

### Step 7: Attempt to connect to the internet again

It might take up to three minutes for the NAT configuration to propagate, so wait at least a minute before trying to access the internet again.

If you are not still logged in to `kube-dns`, reconnect by using the procedure in Step 5. After you are logged in, rerun the `curl` command:
    
    
    curl example.com

You should see output that contains the following content:
    
    
    
    <html>
    <head>
    <title>Example Domain</title>
    ...
    ...
    ...
    </head>
    
    <body>
    <div>
        <h1>Example Domain</h1>
        <p>This domain is established to be used for illustrative examples in documents. You can use this
        domain in examples without prior coordination or asking for permission.</p>
        <p><a href="http://www.iana.org/domains/example">More information...</a></p>
    </div>
    </body>
    </html>
    

## What's next

  * [Set up and manage network address translation with Public NAT](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation)
  * [Use Public NAT with Compute Engine](https://docs.cloud.google.com/nat/docs/gce-example) (tutorial)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
