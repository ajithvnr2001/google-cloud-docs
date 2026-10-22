---
url: https://docs.cloud.google.com/managed-lustre/docs/vpc/
title: Configure a VPC network \u00a0|\u00a0 Managed Lustre \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:09.582529+00:00
---

# Configure a VPC network  |  Managed Lustre  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  Configure a VPC network Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Managed Lustre instances are provisioned in a Google-managed network that connects to your Virtual Private Cloud (VPC) using [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access).

You can connect your Managed Lustre instance to client Compute Engine VMs or Google Kubernetes Engine clusters using either of the following network setups:

  * **Same VPC network** : Connect your client resources and your Managed Lustre instance to the same VPC network.

  * **Separate VPC networks** : Deploy your client resources in a separate VPC network and connect both networks using Network Connectivity Center. For instructions on setting up NCC, see the [Network Connectivity Center documentation](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes).




For both setups, follow the instructions on this page to configure the VPC network where the Managed Lustre instance will be provisioned. If you're using separate VPC networks, the instructions include a callout with the required steps for your client VPC network.

## Required permissions

You must have the following IAM permissions:

  * `serviceusage.services.enable`
  * `compute.networks.create`
  * `compute.addresses.create`
  * `compute.addresses.get`
  * `compute.firewalls.create`
  * `servicenetworking.services.addPeering`



These permissions can be granted by adding all of the following predefined roles:

  * [Service Usage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)
  * [Compute Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Compute Security Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin) (`roles/compute.securityAdmin`)



Or, [create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) containing the specific permissions.

To grant a role to a user:

###  Google Cloud console 

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Click **Grant access**.

  3. In the **New principals** field, enter the user's email address.

  4. In the **Select a role** drop-down menu, select the role to grant.

  5. To grant multiple roles, click **Add another role** and select the next role.

  6. Click **Save**.




###  gcloud 
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member="user:EMAIL_ADDRESS" \
      --role=ROLE
    

## Create and peer the VPC

To create a VPC network and set up a [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access) connection for Managed Lustre, perform the following steps:

###  Google Cloud console 

  1. Enable the Service Networking API.

[Enable Service Networking API](https://console.cloud.google.com/marketplace/product/google/servicenetworking.googleapis.com)

  2. Create a VPC network in custom mode:

     1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

     2. Click **Create VPC network**.

     3. Enter a **Name** for the network.

     4. Unselect **Set MTU automatically** and enter `8896` in the **Maximum transmission unit (MTU)** field.

**Note:** Setting the value of `mtu` (_maximum transmission unit_ , or the size of the largest IP packet that can be transmitted on this network) to the maximum allowed value of 8896 improves performance up to 10% compared to the default value of 1460 bytes.
     5. Under **Subnet creation mode** , select **Custom**.

  3. Create a primary subnet for your GKE or Compute Engine resources:

     1. In the **New subnet** section, enter a **Name** for the subnet.
     2. Select a **Region**.
     3. In the **IPv4 range** field, enter the primary IPv4 range (for example, `10.128.0.0/20`).
     4. Click **Done**.
     5. Click **Create** to create the VPC network.
  4. Allocate an IP range for private services access.

This internal IP range is used for the private services access connection, which peers your VPC network with the Google-managed network where Managed Lustre resources are provisioned. This allocated range is used to provide IPs for Managed Lustre instances, and must not overlap with any subnets in your VPC network.

Each Managed Lustre instance requires a contiguous CIDR block with a prefix length of at least 23.

We recommend creating a larger IP range of /20 to allow for the creation of multiple Managed Lustre instances or the use of other Google Cloud services.

     1. On the **VPC networks** page, click the name of your VPC network.
     2. Select the **Private services access** tab.
     3. Select the **Allocated IP ranges for services** tab.
     4. Click **Allocate IP range**.
     5. Enter a **Name** and **Description** for the allocated range (for example, `Managed Lustre VPC Peering`).
     6. Specify the IP address range:
     7. To let Google select an available range, select **Automatic** and enter a prefix length of `20`.
     8. To specify a specific range, select **Custom** and enter a CIDR block with a prefix length of at least `/23` (such as `10.128.0.0/20`).
     9. Click **Allocate**.
  5. Note the CIDR block associated with the allocated range.

In the **Allocated IP ranges for services** table, find the range you created and note the value in the **Internal IP range** column (for example, `10.128.0.0/20`). You will specify this range as the source in the next step.

  6. Create a firewall rule to allow TCP traffic from the IP range you created. 

     1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies)

     1. Click **Create firewall rule**.
     2. Enter a **Name** for the firewall rule.
     3. In the **Network** field, select your VPC network.
     4. For **Direction of traffic** , select **Ingress**.
     5. For **Action on match** , select **Allow**.
     6. For **Targets** , select **All instances in the network**.
     7. For **Source filter** , select **IPv4 ranges**.
     8. In the **Source IPv4 ranges** field, enter the CIDR block from the allocated range noted in the previous step.
     9. Under **Protocols and ports** , select **Specified protocols and ports**.
     10. Select the **TCP** checkbox and enter `988, 6988` in the **Ports** field.
     11. Click **Create**.

**For separate VPC networks** : If your client VMs or GKE clusters reside in a separate VPC network connected through [ Network Connectivity Center](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes), the firewall rules in both VPC networks must allow traffic from the allocated IP range. Repeat the **Create a firewall rule ...** step to create a firewall rule in the client VPC network allowing ingress TCP traffic on ports `988` and `6988` from the allocated CIDR block.

  7. Establish the private services access connection.

This connection is only required in the VPC network where the Managed Lustre instance is provisioned.

     1. On the **VPC networks** page, click the name of your VPC network.
     2. Select the **Private services access** tab.
     3. Select the **Private connections to services** tab.
     4. Click **Create connection**.
     5. In the **Assigned allocation** list, select the allocated IP range you created.
     6. Click **Connect**.



###  gcloud 

  1. Enable service networking.
         
         gcloud services enable servicenetworking.googleapis.com
         

  2. Create a VPC network in custom mode.
         
         gcloud compute networks create NETWORK_NAME \
           --subnet-mode=custom \
           --mtu=8896
         

**Note:** Setting the value of `mtu` (_maximum transmission unit_ , or the size of the largest IP packet that can be transmitted on this network) to the maximum allowed value of 8896 improves performance up to 10% compared to the default value of 1460 bytes.
  3. Create a primary subnet for your GKE or Compute Engine resources.
         
         gcloud compute networks subnets create SUBNET_NAME \
           --network=NETWORK_NAME \
           --range=10.128.0.0/20 \
           --region=REGION
         

  4. Allocate an IP range for private services access.

This internal IP range is used for the private services access connection, which peers your VPC network with the Google-managed network where Managed Lustre resources are provisioned. This allocated range is used to provide IPs for Managed Lustre instances, and must not overlap with any subnets in your VPC network.

Each Managed Lustre instance requires a contiguous CIDR block with a prefix length of at least 23.

We recommend creating a larger IP range of /20 to allow for the creation of multiple Managed Lustre instances or the use of other Google Cloud services.
         
         gcloud compute addresses create IP_RANGE_NAME \
           --global \
           --purpose=VPC_PEERING \
           --prefix-length=20 \
           --description="Managed Lustre VPC Peering" \
           --network=NETWORK_NAME
         

  5. Get the CIDR block associated with the range you created in the previous step.
         
         CIDR_BLOCK=$(
           gcloud compute addresses describe IP_RANGE_NAME \
             --global  \
             --format="value[separator=/](address, prefixLength)"
         )
         

  6. Create a firewall rule to allow TCP traffic from the IP range you created. 
         
         gcloud compute firewall-rules create FIREWALL_NAME \
           --allow=tcp:988,tcp:6988 \
           --network=NETWORK_NAME \
           --source-ranges=$CIDR_BLOCK
         

**For separate VPC networks** : If your client VMs or GKE clusters reside in a separate VPC network connected through [ Network Connectivity Center](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes), the firewall rules in both VPC networks must allow traffic from the allocated IP range (`$CIDR_BLOCK`). Run the `firewall-rules create` command a second time to create the firewall rule in the client VPC network:
         
         gcloud compute firewall-rules create CLIENT_FIREWALL_NAME \
             --allow=tcp:988,tcp:6988 \
             --network=CLIENT_NETWORK_NAME \
             --source-ranges=$CIDR_BLOCK
          

  7. Establish the private services access connection.
         
         gcloud services vpc-peerings connect \
           --network=NETWORK_NAME \
           --ranges=IP_RANGE_NAME \
           --service=servicenetworking.googleapis.com
         

This connection is only required in the VPC network where the Managed Lustre instance is provisioned.




## Create additional subnets for multi-NIC

If you plan to use multiple network interface cards (multi-NIC) to aggregate bandwidth, you must create a separate subnet within your VPC network for each NIC.

To benefit from multi-NIC, you must use Compute Engine machine types with multiple physical NICs that are attached to regular VPCs. NICs that attach to VPCs with RDMA network profiles cannot be used to increase general networking bandwidth. See [Networking and GPU machines](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth) for additional details.

To create a subnet for an additional physical NIC:

###  Google Cloud console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of your VPC network.

  3. Click **Add subnet**.

  4. In the **New subnet** section:

     1. Enter a **Name** for the subnet.
     2. Select a **Region**.
     3. Enter an **IP address range** (for example, `10.130.0.0/20`).
     4. Click **Add**.



###  gcloud 
    
    
    gcloud compute networks subnets create SUBNET_NAME_2 \
      --network=NETWORK_NAME \
      --range=10.130.0.0/20 \
      --region=REGION
    

Repeat this step for each additional NIC. Ensure that the IP ranges for each subnet don't overlap each other.

## VPC Service Controls

Managed Lustre supports [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) (VPC-SC). See [Secure instances with a service perimeter](https://docs.cloud.google.com/managed-lustre/docs/vpc-sc) for details.

## Troubleshooting VPC setup

### Permission denied to add peering for service `servicenetworking.googleapis.com`
    
    
    ERROR: (gcloud.services.vpc-peerings.connect) User [$(USER)] does not have
    permission to access services instance [servicenetworking.googleapis.com]
    (or it may not exist): Permission denied to add peering for service
    'servicenetworking.googleapis.com'.
    

This error means that you don't have `servicenetworking.services.addPeering` IAM permission on your user account.

See [Access control with IAM](https://docs.cloud.google.com/managed-lustre/docs/access-control) for instructions on adding one of the following roles to your account:

  * `roles/compute.networkAdmin` or
  * `roles/servicenetworking.networksAdmin`



### Cannot modify allocated ranges in CreateConnection
    
    
    ERROR: (gcloud.services.vpc-peerings.connect) The operation
    "operations/[operation_id]" resulted in a failure "Cannot modify allocated
    ranges in CreateConnection. Please use UpdateConnection."
    

This error is returned when you have already created a VPC peering on this network with different IP ranges. There are two possible solutions:

Replace the existing IP ranges:

###  Google Cloud console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of your VPC network.

  3. Select the **Private services access** tab.

  4. On the **Private services access** tab, select the **Private connections to services** tab.

  5. Click the connection name (such as `servicenetworking-googleapis-com`).

  6. In the **Assigned allocation** list, select the new allocated range and clear the checkboxes for any allocated ranges you want to replace.

  7. Click **Save**.




###  gcloud 
    
    
    gcloud services vpc-peerings update \
      --network=NETWORK_NAME \
      --ranges=IP_RANGE_NAME \
      --service=servicenetworking.googleapis.com \
      --force
    

Or, add the new IP range to the existing connection:

###  Google Cloud console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of your VPC network.

  3. Select the **Private services access** tab.

  4. On the **Private services access** tab, select the **Private connections to services** tab.

  5. Click the connection name.

  6. In the **Assigned allocation** list, keep the existing allocated ranges selected and select the new allocated range.

  7. Click **Save**.




###  gcloud 

  1. Retrieve the list of existing IP ranges for the peering:
         
         EXISTING_RANGES="$(
           gcloud services vpc-peerings list \
             --network=NETWORK_NAME \
             --service=servicenetworking.googleapis.com \
             --format="value(reservedPeeringRanges.list())" \
             --flatten=reservedPeeringRanges
         )
         

  2. Then, add the new range to the peering:
         
         gcloud services vpc-peerings update \
           --network=NETWORK_NAME \
           --ranges="${EXISTING_RANGES}",IP_RANGE_NAME \
           --service=servicenetworking.googleapis.com
         




## What's next

  * [Create a Managed Lustre instance](https://docs.cloud.google.com/managed-lustre/docs/create-instance)
  * [Troubleshoot client connectivity and mounting](https://docs.cloud.google.com/managed-lustre/docs/troubleshooting-client-connections)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
