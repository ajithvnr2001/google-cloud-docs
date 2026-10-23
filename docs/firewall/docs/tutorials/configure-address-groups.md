---
url: https://docs.cloud.google.com/firewall/docs/tutorials/configure-address-groups/
title: Configure address groups for firewall policies \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:01.828766+00:00
---

# Configure address groups for firewall policies  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/tutorials/configure-address-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Configure address groups for firewall policies Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial describes how to create and configure address groups for firewall policies in your network. It walks through an example of creating a Virtual Private Cloud (VPC) network with subnets, creating a project-scoped address group, setting up a firewall policy that uses the address group with firewall rules, and then testing the firewall rules. For more information, see [Address groups for firewall policies](https://docs.cloud.google.com/firewall/docs/address-groups-firewall-policies). 

## Objectives

This tutorial shows you how to complete the following tasks:

  * Create two custom VPC networks with subnets.
  * Create three virtual machine (VM) instances (two _consumer_ VMs in separate subnets of one VPC network and a _producer_ VM in a second VPC network). All VMs are created without an external IP address.
  * Install the Apache server on the producer VM.
  * Create VPC Network Peering.
  * Create a Cloud Router and a Cloud NAT gateway, which let the producer VM access the public internet.
  * Create a project-scoped address group.
  * Create a global network firewall policy with the following rules: 
    * Allow Identity-Aware Proxy (IAP) SSH connectivity to the VMs.
    * Allow traffic from the allowed consumer VM to the producer VM using the project-scoped address group.
  * Test the connection.



The following diagram shows the traffic between producer and consumer VMs in the `us-central1` region within two custom VPC networks. A global network firewall policy uses a project-scoped address group rule to allow ingress traffic between the `vm-consumer-allowed` and `vm-producer` VMs. Traffic between the `vm-consumer-blocked` VM and `vm-producer` VM is denied because every VM has an implicit ingress firewall rule that denies all traffic.

[ ![A global network firewall policy allowing ingress traffic from a subnet to a target VM in another VPC network.](https://docs.cloud.google.com/static/firewall/images/firewall-policies/address-group-tutorial.svg)](https://docs.cloud.google.com/static/firewall/images/firewall-policies/address-group-tutorial.svg) A global network firewall policy allowing ingress traffic from a subnet to a target VM in another VPC network (click to enlarge).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the [Compute Engine API](https://console.cloud.google.com/marketplace/product/google/compute.googleapis.com) for your project. 
  7. Make sure that you have the [Compute Network Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`). 
  8. Enable the [Identity-Aware Proxy API](https://console.cloud.google.com/marketplace/product/google/iap.googleapis.com) for your project.
  9. If you prefer to work from the command line, install the Google Cloud CLI. For the conceptual and installation information about the tool, see [gcloud CLI overview](https://docs.cloud.google.com/sdk/gcloud). 

**Note:** If you haven't run the Google Cloud CLI previously, initialize your gcloud CLI directory by running the [`gcloud init` command.](https://docs.cloud.google.com/sdk/gcloud/reference/init)




## Create a consumer VPC network with subnets

In this section, you create a consumer VPC network with two IPv4 subnets: `subnet-consumer-allowed` and `subnet-consumer-blocked`.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. For **Name** , enter `vpc-consumer`.

  4. For **Subnet creation mode** , select **Custom**.

  5. In the **New subnet** section, specify the following configuration parameters for a subnet:

     * **Name** : `subnet-consumer-allowed`
     * **Region** : `us-central1`
     * **IPv4 range** : `192.168.10.0/29`
  6. Click **Done**.

  7. Click **Add subnet** and specify the following configuration parameters:

     * **Name** : `subnet-consumer-blocked`
     * **Region** : `us-central1`
     * **IPv4 range** : `192.168.20.0/29`
  8. Click **Done**.

  9. Click **Create**.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. To create a VPC network, run the following command:
         
         gcloud compute networks create vpc-consumer \
           --subnet-mode=custom
         

  3. In the **Authorize cloud shell** dialog, click **Authorize**.

  4. To create a subnet, run the following command:
         
         gcloud compute networks subnets create subnet-consumer-allowed \
           --network=vpc-consumer \
           --region=us-central1 \
           --range=192.168.10.0/29
         

  5. To create another subnet, run the following command:
         
         gcloud compute networks subnets create subnet-consumer-blocked \
           --network=vpc-consumer \
           --region=us-central1 \
           --range=192.168.20.0/29
         




## Create a producer VPC network with subnet

In this section, you create a producer VPC network with an IPv4 subnet.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. For **Name** , enter `vpc-producer`.

  4. For **Subnet creation mode** , select **Custom**.

  5. In the **New subnet** section, specify the following configuration parameters for a subnet:

     * **Name** : `subnet-vpc-producer`
     * **Region** : `us-central1`
     * **IPv4 range** : `172.16.10.0/29`
  6. Click **Done**.

  7. Click **Create**.




###  gcloud 

  1. To create a VPC network, run the following command:
         
         gcloud compute networks create vpc-producer \
           --subnet-mode=custom
         

  2. To create the subnet, run the following command:
         
         gcloud compute networks subnets create subnet-vpc-producer \
           --network=vpc-producer \
           --region=us-central1 \
           --range=172.16.10.0/29
         




## Create a Cloud Router and a Cloud NAT gateway

To let the `vm-producer` VM access the public internet, you create a Cloud Router and a Cloud NAT gateway.

###  Console 

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. Click **Get started** or **Create Cloud NAT gateway**.

  3. For **Gateway name** , enter `nat-gateway-addressgrp`.

  4. For **NAT type** , select **Public**.

  5. In the **Select Cloud Router** section, specify the following configuration parameters:

     * **Network** : **`vpc-producer`**
     * **Region** : **`us-central1 (lowa)`**
     * **Cloud Router** : Click **Create new router**. 
       1. For **Name** , enter `router-addressgrp`.
       2. Click **Create**.
  6. Click **Create**.




###  gcloud 

  1. To create a Cloud Router, run the following command:
         
         gcloud compute routers create router-addressgrp \
           --network=vpc-producer \
           --region=us-central1
         

  2. To create a Cloud NAT gateway, run the following command:
         
         gcloud compute routers nats create nat-gateway-addressgrp \
           --router=router-addressgrp \
           --region=us-central1 \
           --auto-allocate-nat-external-ips \
           --nat-all-subnet-ip-ranges
         




## Create VMs

In each subnet of the VPC network you created in the preceding section, create VMs without an external IP address.

### Create a VM for the consumer-allowed VPC network

Create a VM in the `subnet-consumer-allowed` subnet.

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Machine configuration** pane, do the following:

     1. For **Name** , enter `vm-consumer-allowed`.
     2. For **Region** , select `us-central1 (Iowa)`.
  3. In the navigation menu, click **Networking**.

     1. In the **Network interfaces** section, click **`default`** and specify the following configuration parameters: 
        * **Network** : **`vpc-consumer`**
        * **Subnetwork** : **`subnet-consumer-allowed IPv4 (192.168.10.0/29)`**
        * **External IPv4 address** : **None**
     2. Click **Done**.
  4. Click **Create**.




###  gcloud 
    
    
    gcloud compute instances create vm-consumer-allowed \
         --network=vpc-consumer \
         --zone=us-central1-a \
         --stack-type=IPV4_ONLY \
         --no-address \
         --subnet=subnet-consumer-allowed
    

### Create a VM for the consumer blocked VPC network

In this section, you create a VM in the `subnet-consumer-blocked` subnet.

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Machine configuration** pane, do the following:

     1. For **Name** , enter `vm-consumer-blocked`.
     2. For **Region** , select `us-central1 (Iowa)`.
  3. In the navigation menu, click **Networking**.

     1. In the **Network interfaces** section, click **`default`** and specify the following configuration parameters: 
        * **Network** : **`vpc-consumer`**
        * **Subnetwork** : **`subnet-consumer-blocked IPv4 (192.168.20.0/29)`**
        * **External IPv4 address** : **None**
     2. Click **Done**.
  4. Click **Create**.




###  gcloud 
    
    
    gcloud compute instances create vm-consumer-blocked \
        --network=vpc-consumer \
        --zone=us-central1-a \
        --stack-type=IPV4_ONLY \
        --no-address \
        --subnet=subnet-consumer-blocked
    

### Create a VM for the producer VPC network

Create a VM in the subnet `subnet-vpc-producer` and install an Apache server on it.

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Machine configuration** pane, do the following:

     1. For **Name** , enter `vm-producer`.
     2. For **Region** , select `us-central1 (Iowa)`.
  3. In the navigation menu, click **Networking**.

     1. In the **Network interfaces** section, click **`default`** and specify the following configuration parameters: 
        * **Network** : **`vpc-producer`**
        * **Subnetwork** : **`subnet-vpc-producer IPv4 (172.16.10.0/29)`**
     2. Click **Done**.
  4. In the navigation menu, click **Advanced** and enter the following script in the **Startup script** field:
         
         #! /bin/bash
           apt-get update
           apt-get install apache2 -y
           a2ensite default-ssl
           a2enmod ssl
           # Read VM network configuration:
           md_vm="http://169.254.169.254/computeMetadata/v1/instance/"
           vm_hostname="$(curl $md_vm/name -H "Metadata-Flavor:Google" )"
           filter="{print \$NF}"
           vm_network="$(curl $md_vm/network-interfaces/0/network \
           -H "Metadata-Flavor:Google" | awk -F/ "${filter}")"
           vm_zone="$(curl $md_vm/zone \
           -H "Metadata-Flavor:Google" | awk -F/ "${filter}")"
           # Apache configuration:
           echo "Page on $vm_hostname in network $vm_network zone $vm_zone" | \
           tee /var/www/html/index.html
           systemctl restart apache2
         

The preceding script deploys and starts an Apache web server in this VM.

  5. Click **Create**.




###  gcloud 

To create a producer VM, run the following command:
    
    
      gcloud compute instances create vm-producer \
          --network=vpc-producer \
          --zone=us-central1-a \
          --stack-type=IPV4_ONLY \
          --no-address \
          --subnet=subnet-vpc-producer \
          --image-project=debian-cloud \
          --image-family=debian-10 \
          --metadata=startup-script='#! /bin/bash
            apt-get update
            apt-get install apache2 -y
            a2ensite default-ssl
            a2enmod ssl
            # Read VM network configuration:
            md_vm="http://169.254.169.254/computeMetadata/v1/instance/"
            vm_hostname="$(curl $md_vm/name -H "Metadata-Flavor:Google" )"
            filter="{print \$NF}"
            vm_network="$(curl $md_vm/network-interfaces/0/network \
            -H "Metadata-Flavor:Google" | awk -F/ "${filter}")"
            vm_zone="$(curl $md_vm/zone \
            -H "Metadata-Flavor:Google" | awk -F/ "${filter}")"
            # Apache configuration:
            echo "Page on $vm_hostname in network $vm_network zone $vm_zone" | \
            tee /var/www/html/index.html
            systemctl restart apache2'
    

## Create a VPC Network Peering connection

To privately connect your `vpc-consumer` and `vpc-producer` VPC networks in the same project, use VPC Network Peering. The VPC Network Peering enables internal IP address connectivity across two VPC networks, regardless of whether the VPC networks belong to the same project or organization.

### Peer `vpc-consumer` with `vpc-producer`

To successfully establish VPC Network Peering, you must separately configure the peering association for the `vpc-consumer` and the `vpc-producer` networks.

###  Console 

To create VPC Network Peering between the `vpc-consumer` and the `vpc-producer` networks, follow these steps:

  1. In the Google Cloud console, go to the **VPC network peering** page.

[Go to VPC network peering](https://console.cloud.google.com/networking/vpc-connectivity/peering)

  2. Click **Create connection**.

  3. Click **Continue**.

  4. In the **Name** field, enter `peering-cp`.

  5. Under **Your VPC network** , select **`vpc-consumer`**.

  6. Under **VPC network name** , select **`vpc-producer`**.

  7. Click **Create**.

**Note:** At this point, the peering state remains **INACTIVE** because of the absence of a matching configuration in the `vpc-producer` network.



###  gcloud 

To create VPC Network Peering between `vpc-consumer` and `vpc-producer`, run the following command:
    
    
    gcloud compute networks peerings create peering-cp \
        --network=vpc-consumer \
        --peer-network=vpc-producer \
        --stack-type=IPV4_ONLY
    

**Note:** At this point, the peering state remains **INACTIVE** because of the absence of a matching configuration in `vpc-producer`.

### Peer the `vpc-producer` network with the `vpc-consumer` network

###  Console 

To create VPC Network Peering between `vpc-producer` and `vpc-consumer`, follow these steps:

  1. In the Google Cloud console, go to the **VPC network peering** page .

[Go to VPC network peering](https://console.cloud.google.com/networking/vpc-connectivity/peering)

  2. Click **Create connection**.

  3. Click **Continue**.

  4. In the **Name** field, enter `peering-pc`.

  5. Under **Your VPC network** , select **`vpc-producer`**.

  6. Under **VPC network name** , select **`vpc-consumer`**.

  7. Click **Create**.

**Note:** As soon as the peering moves to an **ACTIVE** state, subnet routes and custom routes are exchanged.



###  gcloud 

To create VPC Network Peering between `vpc-producer` and `vpc-consumer`, run the following command:
    
    
    gcloud compute networks peerings create peering-pc \
        --network=vpc-producer \
        --peer-network=vpc-consumer \
        --stack-type=IPV4_ONLY
    

**Note:** As soon as the peering moves to an **ACTIVE** state, subnet routes and custom routes are exchanged.

## Create a global network firewall policy to enable IAP

To enable IAP, create a global network firewall policy and add a firewall rule. IAP enables administrative access to the VM instances.

The firewall rule includes the following characteristics.

  * Ingress traffic from IP range `35.235.240.0/20`. This range contains all IP addresses that IAP uses for TCP forwarding.
  * A connection to all ports that you want to be accessible by using IAP TCP forwarding, for example, port `22` for SSH.




###  Console 

To allow IAP access to all VM instances in the `vpc-consumer` and the `vpc-producer` networks, follow these steps:

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. Click **Create firewall policy**.

  3. In the **Configure policy** section, for **Policy name** , enter `fw-policy-addressgrp`.

  4. For **Deployment scope** , select **Global** and click **Continue**.

  5. To create rules for your policy, in the **Add rules** section, click **Add rule**.

     1. For **Priority** , enter `100`.
     2. For **Direction of traffic** , select **Ingress**.
     3. For **Action on match** , select **Allow**.
     4. In the **Target** section, for **Target type** , select **All instances in the network**.
     5. In the **Source** section, for **IP ranges** , enter `35.235.240.0/20`.
     6. In the **Protocol and ports** section, select **Specified protocols and ports**.
     7. Select the **TCP** checkbox, and for **Ports** , enter `22`.
     8. Click **Create**.
  6. Click **Continue**.

  7. To associate a VPC network with the policy, in the **Associate policy with VPC networks** section, click **Associate**.

  8. Select the checkboxes of **`vpc-producer`** and **`vpc-consumer`** , and then click **Associate**.

  9. Click **Continue**.

  10. Click **Create**.




###  gcloud 

To let IAP access the VM instances in the `vpc-producer` network, run the following command:

  1. To create a firewall policy, run the following command:
         
         gcloud compute network-firewall-policies create fw-policy-addressgrp \
             --global
         

  2. To create a firewall rule that allows traffic to all destinations and enables logs, run the following command:
         
         gcloud compute network-firewall-policies rules create 100 \
             --firewall-policy=fw-policy-addressgrp \
             --direction=INGRESS \
             --action=ALLOW \
             --layer4-configs=tcp:22 \
             --src-ip-ranges=35.235.240.0/20 \
             --global-firewall-policy
         

  3. To associate the firewall policy with the producer VPC network, run the following command:
         
         gcloud compute network-firewall-policies associations create \
             --firewall-policy=fw-policy-addressgrp \
             --network=vpc-producer \
             --name=pol-association-vpc-producer \
             --global-firewall-policy
         

  4. To associate the firewall policy with the consumer VPC network, run the following command:
         
         gcloud compute network-firewall-policies associations create \
             --firewall-policy=fw-policy-addressgrp \
             --network=vpc-consumer \
             --name=pol-association-vpc-consumer \
             --global-firewall-policy
         




## Create a project-scoped address group

Create a project-scoped address group that uses the IP address assigned to the `subnet-consumer-allowed` subnet of the `vpc-consumer`VPC network.

For more information about the project-scoped address groups, see [Use address groups in firewall policies](https://docs.cloud.google.com/firewall/docs/use-address-groups-firewall-policies).

###  Console 

  1. In the Google Cloud console, go to the **Address groups** page.

[Go to Address groups](https://console.cloud.google.com/net-security/address-groups/list)

  2. Click add_box**Create Address Group**.

  3. In the **Name** field, enter `address-group-pc`.

  4. For **Scope** , choose **Global**.

  5. For **Type** , select **IPv4**.

  6. In the **Capacity** field, enter `1000`.

  7. In the **IP Addresses** field, enter `192.168.10.0/29`.

  8. Click **Create**.




###  gcloud 

  1. If you are using the Cloud Shell terminal for the first time, click ![alt=''](https://docs.cloud.google.com/static/shell/docs/images/activate-cloud-shell-button.svg)**Activate Cloud Shell** in the Google Cloud console.

  2. To create an address group, run the following command:
         
         gcloud network-security address-groups create address-group-pc \
             --type IPv4 \
             --capacity 1000 \
             --location global
         

  3. In the **Authorize cloud shell** dialog, click **Authorize**.

  4. To add an item to an address group, run the following command:
         
         gcloud network-security address-groups add-items address-group-pc \
             --items 192.168.10.0/29 \
             --location global
         

Remember, the IP range `192.168.10.0/29` is assigned to the **`subnet-consumer-allowed`** subnet of the `vpc-consumer` VPC network.




## Add a firewall rule to allow traffic to an address group

To allow ingress connections from the `vm-consumer-allowed` VM, create a firewall rule that adds the project-scoped address group `address-group-pc` as the source IP address.

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the **Network firewall policies** section, click **`fw-policy-addressgrp`**.

  3. Click **Create rule**.

  4. For **Priority** , enter `150`.

  5. For **Direction of traffic** , select **Ingress**.

  6. For **Action on match** , select **Allow**.

  7. For **Logs** , select **On**.

  8. In the **Target** section, for **Target type** , select **All instances in the network**.

  9. In the **Source** section, for **Address group** , select **`address-group-pc ( PROJECT_ID)`** and click **OK**.

Remember, the `address-group-pc` IP address group has an IP range of `192.168.10.0/29` which is assigned to the subnet `subnet-consumer-allowed` of the consumer VPC network.

  10. Click **Create**.




###  gcloud 

To update the firewall policy, run the following command:
    
    
    gcloud compute network-firewall-policies rules create 150 \
        --firewall-policy=fw-policy-addressgrp \
        --direction=INGRESS \
        --action=ALLOW \
        --src-address-groups=projects/PROJECT_ID/locations/global/addressGroups/address-group-pc \
        --layer4-configs=all \
        --global-firewall-policy \
        --enable-logging
    

## Test the connection

Test the connection from the `vm-consumer-allowed` VM to the`vm-producer` VM, and from the `vm-consumer-blocked` VM to the `vm-producer` VM.

### Test the traffic from the `vm-consumer-allowed` VM to the `vm-producer` VM

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. From the **Internal IP** column of the **`vm-producer`** VM, copy the internal IP address of the VM.

  3. In the **Connect** column of the **`vm-consumer-allowed`** VM, click **SSH**.

  4. In the **SSH-in-browser** dialog, click **Authorize** and wait for the connection to establish.

  5. To verify the connection, run the following command:
         
         curl INTERNAL_IP -m 2
         

Replace `INTERNAL_IP` with the IP address of the **`vm-producer`** VM.

The output is similar to the following:

`<!doctype html><html><body><h1>Hello World!</h1></body></html>`

  6. Close the **SSH-in-browser** dialog.




###  gcloud 

  1. To view the internal IP address of the `vm-producer` VM, run the following command:
         
         gcloud compute instances describe vm-producer \
            --zone=us-central1-a \
            --format='get(networkInterfaces[0].networkIP)'
         

When prompted, press `n` to confirm, and then press `Enter`. Make sure to note the internal IP address of your `vm-producer` VM.

  2. To use SSH to connect to the `vm-consumer-allowed` VM, run the following command:
         
         gcloud compute ssh vm-consumer-allowed \
            --zone=us-central1-a \
            --tunnel-through-iap
         

**Note:** While the SSH connection to the `vm-consumer-allowed` VM is connected, ignore any warning messages you see.
  3. To verify the connection, run the following command:
         
         curl INTERNAL_IP -m 2
         

Replace `INTERNAL_IP` with the internal IP address of the **`vm-producer`** VM.

The expected response message is as follows:

`<!doctype html><html><body><h1>Hello World!</h1></body></html>`

  4. To exit the SSH connection, enter `exit`.




### Test the traffic from the `vm-consumer-blocked` VM to the `vm-producer` VM

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. From the **Internal IP** column of the **`vm-producer`** VM, copy the internal IP address of the VM.

  3. In the **Connect** column of the **`vm-consumer-blocked`** VM, click **SSH**.

  4. In the **SSH-in-browser** dialog, click **Authorize** and wait for the connection to establish.

  5. To verify the connection, run the following command:
         
         curl INTERNAL_IP -m 2
         

Replace `INTERNAL_IP` with the IP address of the **`vm-producer`** VM.

The `Connection timed out` message is expected because every VM creates an implicit ingress firewall rule that denies all traffic. To allow traffic, you add an ingress rule to the firewall policy.

  6. Close the **SSH-in-browser** dialog.




###  gcloud 

  1. To view the internal IP address of the `vm-producer` VM, run the following command:
         
         gcloud compute instances describe vm-producer \
            --zone=us-central1-a \
            --format='get(networkInterfaces[0].networkIP)'
         

When prompted, press `n` to confirm, and then press `Enter`. Make sure to note the internal IP address of your `vm-producer` VM.

  2. To use SSH to connect to the `vm-consumer-blocked` VM, run the following command:
         
         gcloud compute ssh vm-consumer-blocked \
            --zone=us-central1-a \
            --tunnel-through-iap
         

**Note:** While the SSH connection to the `vm-consumer-blocked` VM is connected, ignore any warning messages you see.
  3. To verify the connection, run the following command:
         
         curl INTERNAL_IP -m 2
         

Replace `INTERNAL_IP` with the internal IP address of the **`vm-producer`** VM.

The `Connection timed out` message is expected because every VM creates an implicit ingress firewall rule that denies all traffic. To allow traffic, you add an ingress rule to the firewall policy.

  4. To exit the SSH connection, enter `exit`.




## View the logs

To verify that the address group firewall rules were applied to the ingress traffic, access the logs. To view the log details, follow these steps:

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the **Network firewall policies** section, click the **`fw-policy-addressgrp`** name.

  3. In the **Hit count** column, select the number for the rule you created during Add a firewall rule to allow traffic to an address group. The **Logs explorer** page opens.

  4. To view the firewall rule applied to the ingress traffic, expand the individual log. You can view the rule details, disposition, and instance details.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources.

To delete the resources created in this tutorial, complete the following.

### Delete an address group

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the **Network firewall policies** section, click `fw-policy-addressgrp`.

  3. In the **Firewall rules** section, select the checkbox of the firewall rule `150`.

  4. Click delete**Delete**.

  5. In the Google Cloud console, go to the **Address groups** page.

[Go to Address groups](https://console.cloud.google.com/net-security/address-groups/list)

  6. In the **Address groups** section, select the checkbox next to `address-group-pc`.

  7. Click delete**Delete** , and then click **Delete** again to confirm.




###  gcloud 

  1. To delete the firewall rule associated with the `address-group-pc` IP address group, run the following command:
         
         gcloud compute network-firewall-policies rules delete 150 \
             --firewall-policy fw-policy-addressgrp \
             --global-firewall-policy
         

  2. To remove an existing item from an address group, run the following command:
         
         gcloud network-security address-groups remove-items address-group-pc \
             --items 192.168.10.0/29 \
             --location global
         

  3. To delete an IP address group, run the following command:
         
         gcloud network-security address-groups delete address-group-pc \
             --location global
         

When prompted, press `Y` to confirm, and then press `Enter`.




### Delete the firewall policy

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the **Network firewall policies** section, click the **`fw-policy-addressgrp`** name.

  3. Click the **Associations** tab.

  4. Select the checkbox of the **`vpc-producer`** VM and the **`vpc-consumer`** VM, and then click **Remove association**.

  5. In the **Remove a firewall policy association** dialog, click **Remove**.

  6. Next to the **`fw-policy-addressgrp`** title, click **Delete**.

  7. In the **Delete a firewall policy** dialog, click **Delete**.




###  gcloud 

  1. Remove the association between the firewall policy and the VPC producer network.
         
         gcloud compute network-firewall-policies associations delete \
           --name=pol-association-vpc-producer \
           --firewall-policy=fw-policy-addressgrp \
           --global-firewall-policy
         

**Note:** If you used the Google Cloud console to set up the association between the firewall policy and the VPC network, don't use the gcloud CLI command to remove the association. If you can't remember how you created the association, or you get the `The network firewall policy does not have an association with pol-association-vpc-consumer.` error when you run the command, use the Google Cloud console to remove the association.
  2. Remove the association between the firewall policy and the VPC consumer network.
         
         gcloud compute network-firewall-policies associations delete \
           --name=pol-association-vpc-consumer \
           --firewall-policy=fw-policy-addressgrp \
           --global-firewall-policy
         

  3. Delete the firewall policy.
         
         gcloud compute network-firewall-policies delete fw-policy-addressgrp \
             --global
         




### Delete VPC Network Peering

###  Console 

  1. In the Google Cloud console, go to the **VPC network peering** page.

[Go to VPC network peering](https://console.cloud.google.com/networking/vpc-connectivity/peering)

  2. Select the checkboxes of **`peering-cp`** and **`peering-pc`**.

  3. Click **Delete**.

  4. In the **Delete 2 peerings?** dialog, click **Delete**.




###  gcloud 

  1. To delete the peering between consumer VPC and producer VPC, run the following command:
         
         gcloud compute networks peerings delete peering-cp \
             --network=vpc-consumer
         

  2. To delete the peering between producer VPC and consumer VPC , run the following command:
         
         gcloud compute networks peerings delete peering-pc \
             --network=vpc-producer
         




### Delete the Cloud NAT gateway and Cloud Router

###  Console 

  1. In the Google Cloud console, go to the **Cloud routers** page.

[Go to Cloud routers](https://console.cloud.google.com/hybrid/routers/list)

  2. Select the **`router-addressgrp`** checkbox.

  3. Click **Delete**.

  4. In the **Delete router-addressgrp** dialog, click **Delete**.




When you delete a Cloud Router, the associated Cloud NAT gateway is also deleted.

###  gcloud 

To delete the `router-addressgrp` Cloud Router, run the following command:
    
    
    gcloud compute routers delete router-addressgrp \
        --region=us-central1
    

When prompted, press `Y` to confirm, and then press `Enter`.

When you delete a Cloud Router, the associated Cloud NAT gateway is also deleted.

### Delete the VMs

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the checkboxes of the **`vm-consumer-allowed`** , **`vm-consumer-blocked`** , and **`vm-producer`** VMs.

  3. Click **Delete**.

  4. In the **Delete 3 instances?** dialog, click **Delete**.




###  gcloud 

  1. To delete all of the VMs, run the following command:
         
         gcloud compute instances delete vm-consumer-allowed vm-consumer-blocked vm-producer \
             --zone=us-central1-a
         

When prompted, press `Y` to confirm, and then press `Enter`.




### Delete the consumer VPC network and its subnets

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. In the **Name** column, click **`vpc-consumer`**.

  3. Click **Delete VPC network**.

  4. In the **Delete a network** dialog, click **Delete**.




When you delete a VPC, its subnets are also deleted.

###  gcloud 

  1. To delete the subnets of the `vpc-consumer` VPC network, run the following command:
         
         gcloud compute networks subnets delete subnet-consumer-allowed subnet-consumer-blocked \
            --region=us-central1
         

When prompted, press `Y` to confirm, and then press `Enter`.

  2. To delete the `vpc-consumer` VPC network, run the following command:
         
         gcloud compute networks delete vpc-consumer
         

When prompted, press `Y` to confirm, and then press `Enter`.




### Delete the producer VPC network and its subnet

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. In the **Name** column, click **`vpc-producer`**.

  3. Click **Delete VPC network**.

  4. In the **Delete a network** dialog, click **Delete**.




When you delete a VPC, its subnets are also deleted.

###  gcloud 

  1. To delete the subnet of the `vpc-producer` VPC network, run the following command:
         
         gcloud compute networks subnets delete subnet-vpc-producer \
            --region=us-central1
         

When prompted, press `Y` to confirm and press `Enter`.

  2. To delete the `vpc-producer` VPC network, run the following command:
         
         gcloud compute networks delete vpc-producer
         

When prompted, press `Y` to confirm, and then press `Enter`.




## What's next

  * For conceptual information about firewall policies, see [Firewall policies and rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview).
  * For conceptual information about firewall policy rules, see [Firewall policy rule components](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details).
  * To create, update, monitor, and delete VPC firewall rules, see [Use VPC firewall rules](https://docs.cloud.google.com/firewall/docs/using-firewalls).
  * To determine costs, see [Cloud NGFW pricing](https://cloud.google.com/firewall/pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
