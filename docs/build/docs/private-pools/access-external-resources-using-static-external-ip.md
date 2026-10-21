---
url: https://docs.cloud.google.com/build/docs/private-pools/access-external-resources-using-static-external-ip/
title: Access external resources in a private network using a static external IP \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:51:10.696978+00:00
---

# Access external resources in a private network using a static external IP  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/private-pools/access-external-resources-using-static-external-ip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Access external resources in a private network using a static external IP Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how you can set up your private pools to access external resources through a static external IP.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/getting-started?walkthrough_tutorial_id=build--cloud-build-static-external-ip)

* * *

## Before you begin

  * Enable the Cloud Build, Compute Engine, and Service Networking APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,compute.googleapis.com,servicenetworking.googleapis.com&redirect=/build/docs/private-pools/access-external-resources-using-static-external-ip)



  * To get the permissions that you need to set up a private connection, ask your administrator to grant you the [Compute Engine Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role on the Cloud project in which the VPC network resides. For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  * To use `gcloud` commands on this page, install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk).

**Note:** If you've installed the gcloud CLI previously, make sure you have the latest available version by running `gcloud components update`.



### Create a VPC network

###  Console 

To create a VPC network using the Google Cloud console, complete the following steps:

  1. Open the **VPC networks** page in the Google Cloud console.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network** to create a new network.

You will see the **Create a VPC network** page.

  3. Enter a **Name** for your network.

  4. Under **Subnet creation mode** , select **Automatic**.

  5. If you would like to further customize other fields, refer to [Create and manage VPC networks](https://cloud.google.com/vpc/docs/create-modify-vpc-networks). Otherwise, leave all fields as is.

  6. Click **Create** to create your VPC network.

After you click **Create** , you will see your new VPC network on the [**VPC networks**](https://console.cloud.google.com/networking/networks/list) page.




###  gcloud 

To create a VPC network using the `gcloud` command-line tool, enter the following command in your terminal where NETWORK_NAME is the name of your VPC network:
    
    
    gcloud compute networks create NETWORK_NAME \
      --subnet-mode=auto
    

After you click **Create** , you will see your new VPC network on the [**VPC networks**](https://console.cloud.google.com/networking/networks/list) page.

To learn more about creating and managing VPC networks, see [Create and manage VPC networks](https://cloud.google.com/vpc/docs/create-modify-vpc-networks).

### Create a private connection

###  Console 

To create a private connection between your VPC network and the service producer network, complete the following steps:

  1. Open the **VPC networks** page in the Google Cloud console.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click on your network name.

You will see the **VPC network details** page.

  3. Click on the **Private Service Connection** tab.

     1. Select the **Allocated IP ranges for services** tab.

     2. Click **Allocate IP range**.

You will see the **Allocate an internal IP range** pop-up box.

        1. Enter a **Name** for your IP range.

        2. Under **IP Range** , select **Automatic**.

        3. In the **Prefix length** field, enter a prefix length for your network.

**Note:** The prefix length must be `/24` or lower, such as `/22`, `/21`, etc.
        4. Click **Allocate** to allocate your IP range.

**Note:** Take note of the Internal IP range that is generated for use in following steps.
     3. Select the **Private Connections to Services** tab.

     4. Click **Create Connection**.

You will see the **Create a private connection** pop-up.

        1. Under **Assigned allocation** , select your IP range.

        2. Click **Connect**.

You will now see your connection in the table under the **Private Connections to Services** tab.

Click **Enable** (Export custom route) to ensure that the routes for VPC are applied to the network where your private pool instances are running.




You have now configured your network.

###  gcloud 

To create a private connection between your VPC network and the service producer network, complete the following steps:

  1. Enter the following command in your terminal to allocate an IP range for your service:
         
         gcloud compute addresses create ALLOCATED_RANGE_NAME \
               --global \
               --prefix-length=PREFIX_LENGTH \
               --network=VPC_NETWORK \
               --project=PROJECT_ID
         

Where:

     * ALLOCATED_RANGE_NAME is the name of your allocated range. For example, `my-allocated-range`.
     * PREFIX_LENGTH is the prefix length for your network. Your prefix length must be `/24` or lower, such as `/22`, `/21`, etc.
     * VPC_NETWORK is the name of your VPC network, such as `my-vpc-network`.
     * PROJECT_ID is the ID of your project that contains your VPC network.
  2. Enter the following command in your terminal to create a private connection:
         
         gcloud services vpc-peerings connect \
               --service=servicenetworking.googleapis.com \
               --ranges=ALLOCATED_RANGE_NAME \
               --network=VPC_NETWORK \
               --project=PROJECT_ID
         

Where:

     * ALLOCATED_RANGE_NAME is the name of the allocated range you created in the previous step.
     * VPC_NETWORK is the name of your VPC network, such as `my-vpc-network`.
     * PROJECT_ID is the ID of your project that contains your VPC network.
  3. Enter the following command in your terminal to ensure that the routes for VPC are applied to the network where your private pool instances are running:
         
         gcloud compute networks peerings update servicenetworking-googleapis-com \
               --export-custom-routes \
               --network=VPC_NETWORK \
               --project=PROJECT_ID
         

Where:

     * VPC_NETWORK is the name of your VPC network, such as `my-vpc-network`.
     * PROJECT_ID is the ID of your project that contains your VPC network.



You have now configured your network.

To learn more about configuring a network, see [Setting up a private connection between your VPC network and the service producer network](https://docs.cloud.google.com/build/docs/private-pools/set-up-private-pool-to-use-in-vpc-network#setup-private-connection).

### Create a private pool

###  Console 

To create a private pool using the Google Cloud console, complete the following steps:

  1. Open the **Worker Pool** page in the Google Cloud console:

[ Open the Cloud Build Worker pool page](https://console.cloud.google.com/cloud-build/settings/worker-pool)

  2. Select the project where you want to create the private pool.

  3. In the **Worker pool** page, click **Create**.

You will see the **Create private pool** panel.

  4. In the **Create private pool** side panel, enter the following information:

     1. Enter a **Name** for your private pool.

     2. Select a **Region** from the drop-down menu.

     3. Under **Network** , enter the following information:

     * **Project** : Enter your project ID or number.
     * **Network** : Enter the name of your VPC network.
     1. (Optional) Uncheck the box for **Assign external IPs** for the most restricted network configuration.



You have now created a private pool.

###  gcloud 

To create a private pool using the `gcloud` command-line tool, enter the following command in your terminal:
    
    
          gcloud builds worker-pools create PRIVATEPOOL_ID \
            --project=PRIVATEPOOL_PROJECT_ID \
            --region=REGION \
            --peered-network=PEERED_NETWORK \
            --no-public-egress
    

Where:

  * PRIVATEPOOL_ID is the unique identifier for your private pool.
  * PRIVATEPOOL_PROJECT_ID is the ID of the Google Cloud project where you want to create your private pool.
  * REGION is one of the [supported regions](https://docs.cloud.google.com/build/docs/locations).
  * PEERED_NETWORK is the network resource URL
  * `--no-public-egress`: If this flag is set, the private pool is created without an external IP address.



You have now created a private pool.

To learn more about how to create and manage private pools, see [Creating and managing private pools](https://docs.cloud.google.com/build/docs/private-pools/create-manage-private-pools).

## Access external resources in a private network

By default, external IP addresses associated with Cloud Build private pools are not static or configurable. They are assigned by Google Cloud. If you want to set your private pools up to access external resources from your private network with a static external IP, you must set up a virtual machine (VM) in your project to act as a self-managed NAT gateway to proxy requests to the public internet. Following that, you must set up custom routes to forward these requests to your VM to ensure routes are exchanged with the service networking project.

This section outlines how you can set up your private pools to access external resources through a static external IP by completing the following steps:

  1. Create a startup script to configure the VM to proxy any traffic routed to the VM, and masquerade that traffic as originating from its IP address:
         
         #! /bin/bash
         set -e
         
         sysctl -w net.ipv4.ip_forward=1
         IFACE=$(ip -brief link | tail -1 | awk  {'print $1'})
         iptables -t nat -A POSTROUTING -o "$IFACE" -j MASQUERADE
         

  2. Set up a VM in the same VPC as your private pool with a rule to allow requests to be proxied through the VPC:
         
         gcloud compute instances create VM_NAME \
           --image-project=ubuntu-os-cloud --image-family=ubuntu-2204-lts \
           --network=NETWORK_NAME \
           --private-network-ip=INTERNAL_IP --can-ip-forward \
           --zone=ZONE \
           --subnet=SUBNETWORK \
           --tags=NAT_TAG  \
           --metadata-from-file=startup-script=STARTUP_SCRIPT
         

Where:

     * VM_NAME is the name you want to provide for your VM.
     * NETWORK_NAME is the name of the network you created in the previous section.
     * INTERNAL_IP is any valid internal IP address within the range of the your VM region's subnetwork. For example, `10.128.0.2`.
     * ZONE is the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) associated with your network such as `us-central1-a`.
     * (Optional) SUBNETWORK is the name of your subnetwork. The name of your subnetwork can be found in the equivalent REST for your subnet in the following format: `projects/project-id/regions/region/subnetworks/subnetwork-name`. If you selected **Automatic** under **Subnet connection mode** when creating a VPC network, you do not need to specify this field.
     * NAT_TAG is the name of the NAT gateway tag that allows you to route requests conditionally, based on whether or not they have a tag from this VM. You can specify any name for the tag.
     * STARTUP_SCRIPT is the name of the startup script you created in the previous step. For example, `startup-script-example.sh`. In this example, the `--metadata-from-file` flag is used to pass the contents of the startup script you specified to a key called `startup-script`.

After running this command, you will see an output that contains the external IP value. Take note of the external IP value. All traffic from your private pool to your external resource comes through this address. You may choose to use this address for further configuration, such as configuring firewall rules in your external network.

  3. Set up a route to direct all requests to the external resource to go to the instance created in the previous step, allowing your requests to be forwarded to your private pool instances:
         
         gcloud compute routes create PRIVATE_POOL_ROUTE_NAME \
           --destination-range=DESTINATION_RANGE \
           --next-hop-address=INTERNAL_IP \
           --network=NETWORK_NAME \
           --priority=POOL_ROUTE_PRIORITY
         

Where:

     * PRIVATE_POOL_ROUTE_NAME is the name you want to give your route.
     * DESTINATION_RANGE is a valid CIDR address range containing the destination you want to route to. For example, a GitHub Enterprise Edition instance. For example, `8.8.8.0/24`.
     * INTERNAL_IP is the internal IP value obtained from the previous step. For example, `10.128.0.2`.
     * NETWORK_NAME is the name of the network you created in the previous section.
     * POOL_ROUTE_PRIORITY is the priority number you want to specify for your route.
**Note:** If you want to direct all traffic to the internet (0.0.0.0/0) from your private pool to your NAT gateway VM, you need to specify four different routing rules. To mimic the `0.0.0.0/0` address space, you need to set a range for both `0.0.0.0/1` and `128.0.0.0/1`.

This command ensures that any traffic from a build within a private pool instance is routed to the proxy VM you created, not directly routed to the public internet.

  4. Set up a route to forward requests from your proxy from your tagged instances to the external destination IP range. The following command creates a route to forward requests to the public internet associated with your private pool instances.
         
         gcloud compute routes create NAT_EGRESS_ROUTE_NAME \
           --destination-range=DESTINATION_RANGE \
           --next-hop-gateway=default-internet-gateway \
           --network=NETWORK_NAME \
           --priority=NAT_ROUTE_PRIORITY \
           --tags=NAT_TAG
         

Where:

     * NAT_EGRESS_ROUTE_NAME is the name you want to give your NAT gateway route.
     * DESTINATION_RANGE is the address of the destination you want to route to. For example, a GitHub Enterprise Edition instance. For example, `8.8.8.0/24`.
     * NETWORK_NAME is the name of the network you created in the previous section.
     * NAT_TAG is the name of the NAT gateway tag that allows you to route requests conditionally, based on whether or not they have a tag from this VM. You can specify any name for the tag.
     * NAT_ROUTE_PRIORITY is the priority number you want to specify for your route.

**Note:** The value that you specify for NAT_ROUTE_PRIORITY must be lower than the value you specified for POOL_ROUTE_PRIORITY. A lower value means a higher priority.

This command ensures that any traffic from the proxy VM can be directed to the public internet.

  5. Add a firewall rule to allow traffic from your private pool into your NAT gateway VM:
         
         gcloud compute firewall-rules create RULE_NAME \
           --direction=INGRESS --priority=FIREWALL_PRIORITY --action=ALLOW --rules=all \
           --network=NETWORK_NAME \
           --source-ranges=ALLOCATED_RANGE \
           --target-tags=NAT_TAG
         

Where:

     * RULE_NAME is the name you want to give to your firewall rule.
     * FIREWALL_PRIORITY is the priority number you want to specify for your firewall rule.
     * NETWORK_NAME is the name of the network you created in the previous section.
     * ALLOCATED_RANGE is the CIDR range that you allocated when creating your Private Service Connection.
     * NAT_TAG is the name of the NAT gateway tag that allows you to route requests conditionally, based on whether or not they have a tag from this VM. You can specify any name for the tag.



You can now access external resources from the static IP address of the self-managed NAT gateway in your VPC.

## What's next

  * Learn more about [private pools](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview).
  * Learn how to [set up your environment to create private pools](https://docs.cloud.google.com/build/docs/private-pools/set-up-private-pool-environment).
  * Learn how to [access resources in a private JFrog Artifactory with private pools](https://docs.cloud.google.com/build/docs/private-pools/access-resources-in-private-jfrog-artifactory).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
