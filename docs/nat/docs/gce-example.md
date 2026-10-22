---
url: https://docs.cloud.google.com/nat/docs/gce-example/
title: Use Public NAT with Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:42.210518+00:00
---

# Use Public NAT with Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nat/docs/gce-example/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NAT ](https://docs.cloud.google.com/nat/docs)
  * [ Guides ](https://docs.cloud.google.com/nat/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use Public NAT with Compute Engine

This page shows a demonstration of a Public NAT gateway that provides network address translation services for a Compute Engine VM instance. Before you begin, read the [Public NAT overview](https://docs.cloud.google.com/nat/docs/public-nat).

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
      

## Example

The following is an end-to-end example that demonstrates a sample Public NAT gateway and a sample Compute Engine VM that uses the Public NAT gateway.

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

  1. Create a new custom mode VPC network in your project:
         
         gcloud compute networks create custom-network1 \
             --subnet-mode custom

  2. Specify the subnet prefix for your first region. In this example, we assign `192.168.1.0/24` to region `us-east4`.
         
         gcloud compute networks subnets create subnet-us-east-192 \
            --network custom-network1 \
            --region us-east4 \
            --range 192.168.1.0/24




### Terraform

You can use a [Terraform module](https://github.com/terraform-google-modules/terraform-google-network) to create a custom Virtual Private Cloud (VPC) network and subnet.
    
    
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

### Step 2: Create a VM instance with no external IP address

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. Specify a **Name** of `nat-test-1` for your instance.

  4. Set the **Region** to **us-east4**.

  5. Set the **Zone** to **us-east4-c**.

  6. Click the **Management, security, disks, networking, sole tenancy** link.

  7. Click the **Networking** tab.

  8. Under **Network interfaces** , click edit**Edit** for the VM's default interface.

     1. Set the **Network** to **`custom-network1`**.
     2. Set the **Subnetwork** to **`subnet-us-east-192`**.
     3. Set **External IP** to **None**.
     4. Click **Done**.
  9. To create and start the instance, click **Create**.




###  gcloud 
    
    
    gcloud compute instances create nat-test-1 \
        --image-family debian-9 \
        --image-project debian-cloud \
        --network custom-network1 \
        --subnet subnet-us-east-192 \
        --zone us-east4-c \
        --no-address

### Terraform

You can use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance) to create a VM instance.
    
    
    resource "google_compute_instance" "default" {
      project      = var.project_id
      zone         = "us-east4-c"
      name         = "nat-test-1"
      machine_type = "e2-medium"
      boot_disk {
        initialize_params {
          image = "debian-cloud/debian-9"
        }
      }
      network_interface {
        network    = "custom-network1"
        subnetwork = var.subnet # Replace with a reference or self link to your subnet, in quotes
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
      network = var.network # Replace with a reference or self link to your network, in quotes
    
      allow {
        protocol = "tcp"
        ports    = ["22"]
      }
      source_ranges = ["35.235.240.0/20"]
    }

### Step 4: Create IAP SSH permissions for your test instance

In a later step, use Identity-Aware Proxy (IAP) to connect to your test instance.

###  Console 

  1. In the Google Cloud console, go to the **Identity-Aware Proxy** page.

[Go to the Identity-Aware Proxy page](https://console.cloud.google.com/security/iap)

  2. Select the **SSH and TCP resources** tab.

  3. To update member permissions on resources, select the checkbox next to **All Tunnel Resources > us-east4-c > nat-test-1**.

  4. In the right pane, click **Add member**.

  5. To grant users, groups, or service accounts access to the resources, in the **New members** field, specify their email addresses.

If you are just testing this feature, you can enter your own email address.

  6. To grant the members access to the resources through Cloud IAP's TCP forwarding feature, in the **Role** drop-down list, select **Cloud IAP > IAP-secured Tunnel User**.

  7. Click **Save**.




###  gcloud 

This command grants SSH access by using IAP to all VM instances in your project. If you want to grant SSH access by using IAP to an individual VM, use the Google Cloud console instructions.
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=MEMBER_INFO \
        --role=roles/iap.tunnelResourceAccessor

Replace the following:

  * `PROJECT_ID`: your project ID
  * `MEMBER_INFO`: a comma-separated list of member `type:email` pairs. Examples: 
    * For an individual user: `user:test-user@example.com`
    * For a group: `group:admins@example.com`
    * For a service account: `serviceAccount:test123@example.domain.com`



### Terraform

You can use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_project_iam) to create IAP SSH permissions for your test instance.
    
    
    resource "google_project_iam_member" "project" {
      project = var.project_id
      role    = "roles/iap.tunnelResourceAccessor"
      member  = "serviceAccount:test123@example.domain.com"
    }

### Step 5: Log in to `nat-test-1` and confirm that it cannot reach the internet

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. For `nat-test-1`, in the **Connect** column, click the **SSH** drop-down arrow, and then select **Open in browser window**.

  3. At the command prompt of the VM, enter `curl example.com` and then press Enter.

You should get no result. If you do, you might have created `nat-test-1` with an external IP address, or there might be some other problem. To troubleshoot, see [VMs can reach the internet unexpectedly without Cloud NAT](https://docs.cloud.google.com/nat/docs/troubleshooting#internet-wo-nat).

To end the command, you might have to enter `Ctrl+C`.




###  gcloud 

  1. Add a Compute Engine SSH key to your local host:
         
         ssh-add ~/.ssh/google_compute_engine
         

  2. Connect to **`nat-test-1`** and run a command:
         
         gcloud compute ssh nat-test-1 \
             --zone us-east4-c \
             --command "curl example.com" \
             --tunnel-through-iap

You should get no result. If you do, you might have created `nat-test-1` with an external IP address, or there might be some other problem. To troubleshoot, see [VMs can reach the internet unexpectedly without Cloud NAT](https://docs.cloud.google.com/nat/docs/troubleshooting#internet-wo-nat).

To end the command, you might have to enter `Ctrl+C`.




### Step 6: Create a NAT configuration using Cloud Router

You must create the Cloud Router in the same region as the instances that use Public NAT. Cloud Router is only used to place NAT information onto the VMs. It is not used as part of the actual NAT gateway.

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
      source  = "terraform-google-modules/cloud-nat/google"
      version = "~> 5.0"
    
      project_id                         = var.project_id
      region                             = "us-east4"
      router                             = google_compute_router.router.name
      name                               = "nat-config"
      source_subnetwork_ip_ranges_to_nat = "ALL_SUBNETWORKS_ALL_IP_RANGES"
    }

### Step 7: Attempt to connect to the internet again

It might take up to three minutes for the NAT configuration to propagate to the VM, so wait at least a minute before trying to access the internet again.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. For `nat-test-1`, in the **Connect** column, click the **SSH** drop-down arrow, and then select **Open in browser window**.

  3. At the command prompt of the VM, enter `curl example.com` and then press Enter.




###  gcloud 

Connect to **`nat-test-1`** and run a command:
    
    
    gcloud compute ssh nat-test-1 \
        --zone us-east4-c \
        --command "curl example.com" \
        --tunnel-through-iap
    

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
  * [Use Public NAT with GKE](https://docs.cloud.google.com/nat/docs/gke-example) (tutorial)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
