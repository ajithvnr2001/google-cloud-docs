---
url: https://docs.cloud.google.com/firewall/docs/tutorials/configure-fwpolicy-deny-egress-geolocation/
title: Configure global network firewall policy to deny egress connections to specific geolocations \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:25:50.976187+00:00
---

# Configure global network firewall policy to deny egress connections to specific geolocations  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/tutorials/configure-fwpolicy-deny-egress-geolocation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Configure global network firewall policy to deny egress connections to specific geolocations Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial describes how to create and configure a global network firewall policy to block egress traffic to specific geolocations in your network. It walks through an example of creating a Virtual Private Cloud (VPC) network with two subnets, setting up a firewall policy with geolocation firewall rules, and then testing the firewall rules. 

## Objectives

This tutorial shows you how to complete the following tasks:

  * Create a custom VPC network with two subnets in different regions.
  * Create a virtual machine (VM) instance in each of the following regions: the US and Singapore.
  * Create a Cloud Router and a Cloud NAT gateway, to allow the US VM to access the public internet.
  * Create a global network firewall policy and add a firewall rule to enable Identity-Aware Proxy (IAP).
  * Install Apache server on the Singapore VM.
  * Add a firewall rule to block traffic to specific geolocations.
  * Test the geolocation firewall rule.



The following diagram shows traffic between VMs in the`us-central1` and `asia-southeast1` regions within a custom VPC network. A global network firewall policy blocks egress traffic to a specific geolocation. The VM in the `us-central1` region uses Cloud Router and a Cloud NAT for internet access, without using an external IP address. The VM in the `us-central1` region uses the external IP address of the VM in the `asia-southeast1` region to test the firewall rule.

[ ![A global network firewall policy blocking egress traffic from a subnet to a specific geolocation.](https://docs.cloud.google.com/static/firewall/images/firewall-policies/geolocation-tutorial.svg)](https://docs.cloud.google.com/static/firewall/images/firewall-policies/geolocation-tutorial.svg) A global network firewall policy blocking egress traffic from a subnet to a specific geolocation (click to enlarge).

## Before you begin

  * Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  * In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

    * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
    * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  * [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  * In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

    * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
    * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  * [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  * Make sure that you have the [Compute Network Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`). 
  * Enable the Compute Engine and Identity-Aware Proxy (IAP) APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,iap.googleapis.com)

  * If you prefer to work from the command line, install the Google Cloud CLI. For the conceptual and installation information about the tool, see [gcloud CLI overview](https://docs.cloud.google.com/sdk/gcloud). 

**Note:** If you haven't run the Google Cloud CLI previously, initialize your gcloud CLI directory by running the [`gcloud init` command](https://docs.cloud.google.com/sdk/gcloud/reference/init). 




## Create a custom VPC network with subnets

Create a custom mode VPC network with two IPv4 subnets.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. For **Name** , enter `vpc-geo-location`.

  4. For **Subnet creation mode** , select **Custom**.

  5. In the **New subnet** section, specify the following configuration parameters for a subnet:

     * **Name** : `subnet-1-us`
     * **Region** : `us-central1`
     * **IPv4 range** : `10.0.0.0/24`
  6. Click **Done**.

  7. Click **Add subnet** and specify the following configuration parameters:

     * **Name** : `subnet-2-sg`
     * **Region** : `asia-southeast1`
     * **IPv4 range** : `192.168.200.0/24`
  8. Click **Done**.

  9. Click **Create**.




###  gcloud 

  1. To open the terminal, click **Activate Cloud Shell**.
  2. To create a VPC network, run the following command:
         
         gcloud compute networks create vpc-geo-location \
           --subnet-mode=custom
         

  3. In the **Authorize cloud shell** dialog, click **Authorize**.

  4. To create a subnet, run the following command:
         
         gcloud compute networks subnets create subnet-1-us \
           --network=vpc-geo-location \
           --region=us-central1 \
           --range=10.0.0.0/24
         

  5. To create another subnet, run the following command:
         
         gcloud compute networks subnets create subnet-2-sg \
           --network=vpc-geo-location \
           --region=asia-southeast1 \
           --range=192.168.200.0/24
         




## Create VMs

In this section, you create two VMs in the subnets you configured in the preceding section.

### Create a VM in the `us-central1` region

Create a VM in the `us-central1` region without an external IP address.

###  Console 

To create a VM in the `us-central1` region, follow these steps:

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Machine configuration** pane, do the following:

     1. For **Name** , enter `instance-1-us`.
     2. For **Region** , select `us-central1 (Iowa)`.
  3. In the navigation menu, click **Networking**.

     1. In the **Network interfaces** section, click **`default`** and specify the following configuration parameters: 
        * **Network** : **`vpc-geo-location`**
        * **Subnetwork** : **`subnet-1-us IPv4 (10.0.0.0/24)`**
        * **External IPv4 address** : **None**
     2. Click **Done**.
  4. Click **Create**.




###  gcloud 

To create a VM in the `us-central1` region, run the following command:
    
    
    gcloud compute instances create instance-1-us \
         --network=vpc-geo-location \
         --zone=us-central1-a \
         --stack-type=IPV4_ONLY \
         --no-address \
         --subnet=subnet-1-us
    

### Create a VM in the `asia-southeast1` region

###  Console 

To create a VM in the `asia-southeast1` region, follow these steps:

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Machine configuration** pane, do the following:

     1. For **Name** , enter `instance-2-sg`.
     2. For **Region** , select **`asia-southeast1 (Singapore)`**.
  3. In the navigation menu, click **Networking**.

     1. In the **Network interfaces** section, click **`default`** and specify the following configuration parameters: 
        * **Network** : **`vpc-geo-location`**
        * **Subnetwork** : **`subnet-2-sg IPv4 (192.168.200.0/24)`**
        * **External IPv4 address** : **None**
     2. Click **Done**.
  4. Click **Create**.




###  gcloud 

To create a VM in the `asia-southeast1` region, run the following command:
    
    
    gcloud compute instances create instance-2-sg \
        --network=vpc-geo-location \
        --zone=asia-southeast1-b \
        --subnet=subnet-2-sg \
        --stack-type=IPV4_ONLY
    

## Create a Cloud Router and a Cloud NAT gateway

In the previous section, you created two VMs, `instance-1-us` and `asia-southeast1`. To allow `instance-1-us` VMs to access the public internet, create a Cloud Router and a Cloud NAT gateway.

###  Console 

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. Click **Get started** or **Create Cloud NAT gateway**.

  3. For **Gateway name** , enter `nat-gateway`.

  4. For **NAT type** , select **Public**.

  5. In the **Select Cloud Router** section, specify the following configuration parameters:

     * **Network** : **`vpc-geo-location`**
     * **Region** : **`us-central1`**
     * **Cloud Router** : **Create new router**. 
       1. For **Name** , enter `router-fw-rules`.
       2. Click **Create**.
  6. Click **Create**.

  7. In the Google Cloud console, go to the **IP addresses** page.

[Go to IP addresses](https://console.cloud.google.com/networking/addresses/list)

  8. Click the **External IP Addresses** tab, and then copy the IP address of your Cloud NAT (`nat-auto-ip`). This IP address is used when you validate the connection between the `instance-1-us` VM and `instance-2-sg` VM.




###  gcloud 

  1. To create a Cloud Router, run the following command:
         
         gcloud compute routers create router-fw-rules \
           --network=vpc-geo-location \
           --region=us-central1
         

  2. To create a Cloud NAT gateway, run the following command:
         
         gcloud compute routers nats create nat-gateway \
           --router=router-fw-rules \
           --region=us-central1 \
           --auto-allocate-nat-external-ips \
           --nat-all-subnet-ip-ranges
         

  3. To view the Cloud NAT IP address, run the following command:
         
         gcloud compute routers get-nat-ip-info \
           router-fw-rules \
           --region=us-central1
         

Remember to copy the IP address of your Cloud NAT (`natIp`). This IP address is used when you validate the connection between the `instance-1-us` VM and the `instance-2-sg` VM.




## Create a global network firewall policy to enable IAP

In this section, you create a global network firewall policy and add a firewall rule to enable IAP. IAP allows administrative access to the VM instances.

The firewall rule includes the following characteristics.

  * Ingress traffic from IP range `35.235.240.0/20`. This range contains all IP addresses that IAP uses for TCP forwarding.
  * A connection to all ports that you want to be accessible by using IAP TCP forwarding, for example, port `22` for SSH.




###  Console 

To allow IAP access to all VM instances in the `vpc-geo-location` network, follow these steps:

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. Click **Create firewall policy**.

  3. In the **Configure policy** section, for **Policy name** , enter `fw-policy`.

  4. For **Deployment scope** , select **Global** and click **Continue**.

  5. To create rules for your policy, in the **Add rules** section, click **Add rule**.

     1. For **Priority** , enter `100`.
     2. For **Direction of traffic** , select **Ingress**.
     3. For **Action on match** , select **Allow**.
     4. For **Logs** , select **On**.
     5. In the **Target** section, for **Target type** , select **All instances in the network**.
     6. In the **Source** section, for **IP ranges** , enter `35.235.240.0/20`.
     7. In the **Protocol and ports** section, select **Specified protocols and ports**.
     8. Select the **TCP** checkbox, and for **Ports** , enter `22`.
     9. Click **Create**.
  6. Click **Continue**.

  7. To associate a VPC network with the policy, in the **Associate policy with VPC networks** section, click **Associate**.

  8. Select the checkbox of **`vpc-geo-location`** and click **Associate**.

  9. Click **Continue**.

  10. Click **Create**.




###  gcloud 

To allow IAP access to all VM instances in the `vpc-geo-location` network, run the following command:

  1. To create a firewall policy, run the following command:
         
         gcloud compute network-firewall-policies create fw-policy \
             --global
         

  2. To create a firewall rule that allows traffic to all destinations and enables logs, run the following command:
         
         gcloud compute network-firewall-policies rules create 100 \
             --firewall-policy=fw-policy \
             --direction=INGRESS \
             --action=ALLOW \
             --layer4-configs=tcp:22 \
             --src-ip-ranges=35.235.240.0/20 \
             --global-firewall-policy \
             --enable-logging
         
         

  3. To associate the firewall policy with the VPC network, run the following command:
         
         gcloud compute network-firewall-policies associations create \
             --firewall-policy=fw-policy \
             --network=vpc-geo-location \
             --name=pol-association-fw-rules \
             --global-firewall-policy
         




## Create a firewall rule

In this section, you create a firewall rule to allow ingress connection on the `instance-2-sg` VM.

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the **Network firewall policies** section, click `fw-policy`.

  3. Click **Create rule**.

  4. For **Priority** , enter `500`.

  5. For **Direction of traffic** , select **Ingress**.

  6. For **Action on match** , select **Allow**.

  7. For **Logs** , select **On**.

  8. In the **Target** section, for **Target type** , select **All instances in the network**.

  9. In the **Source** section, for **IP ranges** , enter NAT_IP_ADDRESS.

Replace `NAT_IP_ADDRESS` with the IP address assigned to your Cloud NAT. For more information, see Create a Cloud Router and a Cloud NAT gateway.

  10. Click **Create**.




###  gcloud 

To update the firewall policy, run the following command:
    
    
    gcloud compute network-firewall-policies rules create 500 \
        --firewall-policy=fw-policy \
        --direction=INGRESS \
        --action=ALLOW \
        --src-ip-ranges=NAT_IP_ADDRESS \
        --layer4-configs=all \
        --global-firewall-policy \
        --enable-logging
    

Replace `NAT_IP_ADDRESS` with the IP address assigned to your Cloud NAT. For more information, see Create a Cloud Router and a Cloud NAT gateway.

## Install the Apache server

In this section, you install the Apache server on the `instance-2-sg` VM.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the **Connect** column of the **`instance-2-sg`** VM, click **SSH**.

  3. In the **SSH-in-browser** dialog, click **Authorize** and wait for the connection to establish.

  4. To update the package lists on your instance, run the following command:
         
         sudo apt-get update
         

When the process is finished, it generates the following message:

`Reading package lists... Done.`

  5. To install the `apache2 HTTP Server` package, at the command prompt, run the following command:
         
         sudo apt-get install apache2 php7.0
         

While the process is in progress, it generates the following message:

`After this operation, 56.0 MB of additional disk space will be used. Do you want to continue? [Y/n]`

Press `Y` to confirm, and then press `Enter`.

  6. To overwrite the Apache web server default web page, run the following command:
         
         echo '<!doctype html><html><body><h1>Hello World!</h1></body></html>' | sudo tee /var/www/html/index.html
         

  7. Close the **SSH-in-browser** dialog.




###  gcloud 

  1. To use SSH to connect to the `instance-2-sg` VM, run the following command:
         
         gcloud compute ssh instance-2-sg \
             --zone=asia-southeast1-b \
             --tunnel-through-iap
         

When prompted, press `Y` to confirm, and then press `Enter`.

**Note:** While the SSH connection to the `instance-2-sg` VM is connected, ignore any warning messages you see.
  2. To update the package lists on your instance, run the following command:
         
         sudo apt-get update
         

When the process is finished, it generates the following message:

`Reading package lists... Done.`

  3. To install the `apache2 HTTP Server` package, at the command prompt, run the following command:
         
         sudo apt-get install apache2 php7.0
         

While the process is in progress, it generates the following message:

`After this operation, 56.0 MB of additional disk space will be used. Do you want to continue? [Y/n]`

Press `Y` to confirm, and then press `Enter`.

  4. To overwrite the Apache web server default web page, run the following command:
         
         echo '<!doctype html><html><body><h1>Hello World!</h1></body></html>' | sudo tee /var/www/html/index.html
         

  5. To close the **SSH-in-browser** , enter **`exit`**.




## Validate the connection

After installing the Apache server on the `instance-2-sg` VM, connect to the `instance-1-us` VM from the `instance-2-sg` VM using the external IP address of the `instance-2-sg` VM.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. From the **External IP** column of the **`instance-2-sg`** VM, copy the external IP address of the VM.

  3. In the **Connect** column of the **`instance-1-us`** VM, click **SSH**.

  4. In the **SSH-in-browser** dialog, click **Authorize** and wait for the connection to establish.

  5. To verify the connection, run the following command:
         
         curl EXTERNAL_IP -m 2
         

Replace `EXTERNAL_IP` with the IP address of the **`instance-2-sg`** VM.

The expected response message is as follows:

`<!doctype html><html><body><h1>Hello World!</h1></body></html>`

  6. Close the **SSH-in-browser** dialog.




###  gcloud 

  1. To view the external IP address of the `instance-2-sg` VM, run the following command:
         
         gcloud compute instances describe instance-2-sg \
             --zone=asia-southeast1-b \
             --format='get(networkInterfaces[0].accessConfigs[0].natIP)'
         

When prompted, press `Y` to confirm, and then press `Enter`. Make sure to note the external IP address of the `instance-2-sg` VM.

  2. To use SSH to connect to the `instance-1-us` VM, run the following command:
         
         gcloud compute ssh instance-1-us \
             --zone=us-central1-a \
             --tunnel-through-iap
         

**Note:** While the SSH connection to the `instance-1-us` VM is connected, ignore any warning messages you see.
  3. To verify the connection, run the following command:
         
         curl EXTERNAL_IP -m 2
         

Replace `EXTERNAL_IP` with the IP address of the **`instance-2-sg`** VM.

The expected response message is as follows:

`<!doctype html><html><body><h1>Hello World!</h1></body></html>`

  4. To close the **SSH-in-browser** , enter **`exit`**.




## Add a firewall rule to block traffic to specific geolocations

In this section you add a firewall rule for the VPC `vpc-geo-location` to block egress traffic to Italy, Poland, and Singapore.

###  Console 

To add a new rule in the **`fw-policy`** that you created in the Create a global network firewall policy section, follow these steps:

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the **Network firewall policies** section, click **`fw-policy`**.

  3. Click **Create rule**.

  4. For **Priority** , enter `200`.

  5. For **Direction of traffic** , select **Egress**.

  6. For **Action on match** , select **Deny**.

  7. For **Logs** , select **On**.

  8. In the **Destination** section, for **Geolocations** , select **Singapore (SG)** , **Poland (PL)** , and **Italy (IT)**.

  9. Click **OK**.

  10. Click **Create**.




###  gcloud 

To add a new rule in the **`fw-policy`** that you created in the Create a global network firewall policy section, run the following command:
    
    
    gcloud compute network-firewall-policies rules create 200 \
        --firewall-policy=fw-policy \
        --direction=EGRESS \
        --action=DENY \
        --dest-region-codes=SG,PL,IT \
        --layer4-configs=all \
        --global-firewall-policy \
        --enable-logging
    

## Test the geolocation firewall rule

###  Console 

After you have added the rule to block egress traffic to Singapore (SG), Poland (PL), and Italy (IT), follow these steps to test the rule:

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. From the **External IP** column of the **`instance-2-sg`** VM, copy the external IP address of the VM.

  3. In the **Connect** column of the **`instance-1-us`** VM, click **SSH**.

  4. In the **SSH-in-browser** dialog, click **Authorize** and wait for the connection to establish.

  5. To verify that egress traffic to the **`instance-2-sg`** VM is blocked, run the following command:
         
         curl EXTERNAL_IP -m 2
         

Replace `EXTERNAL_IP` with the IP address of the **`instance-2-sg`** VM.

The `Connection timed out` message is expected because you created a firewall rule to deny external traffic from the US VM to the Singapore VM.

  6. To verify that the egress traffic to Poland is blocked, run the following command:
         
         curl  `https://www.gov.pl` -m 2
         

The `Connection timed out` message is expected because you created a firewall rule to deny external traffic to the Poland website.

**Note:** You can use any website whose domain name resolves to an IP address associated with the geolocation Poland (PL).
  7. To verify that the egress traffic to Italy is blocked, run the following command:
         
         curl  `https://www.esteri.it/it/` -m 2
         

The `Connection timed out` message is expected because you created a firewall rule to deny external traffic to the Italy website.

**Note:** You can use any website whose domain name resolves to an IP address associated with the geolocation Italy (IT).
  8. Close the **SSH-in-browser** dialog.




###  gcloud 

After you have added the rule to block egress traffic to Singapore (SG), Poland (PL), and Italy (IT), run the following command to test the rule:

  1. To view the external IP address of the `instance-2-sg` VM, run the following command:
         
         gcloud compute instances describe instance-2-sg \
            --format='get(networkInterfaces[0].accessConfigs[0].natIP)'
         

When prompted, press `Y` to confirm, and then press `Enter`. Make sure to note the external IP address of the `instance-2-sg` VM.

  2. To use SSH to connect to the `instance-1-us` VM, run the following command:
         
         gcloud compute ssh instance-1-us \
            --zone=us-central1-a \
            --tunnel-through-iap
         

**Note:** While the SSH connection to the `instance-1-us` VM is connected, ignore any warning messages you see.
  3. To verify that the egress traffic to Singapore is blocked, run the following command:
         
         curl EXTERNAL_IP -m 2
         

Replace `EXTERNAL_IP` with the IP address of the **`instance-2-sg`** VM.

The `Connection timed out` message is expected because you created a firewall rule to deny external traffic from the US VM to the Singapore VM.

  4. To verify that the egress traffic to Poland is blocked, run the following command:
         
         curl https://www.gov.pl -m 2
         

The `Connection timed out` message is expected because you created a firewall rule to deny external traffic from the Poland website.

**Note:** You can use any website whose domain name resolves to an IP address associated with the geolocation Poland (PL).
  5. To verify that the egress traffic to Italy is blocked, run the following command:
         
         curl  https://www.esteri.it/it/ -m 2
         

The `Connection timed out` message is expected because you created a firewall rule to deny external traffic to the Italy website.

**Note:** You can use any website whose domain name resolves to an IP address associated with the geolocation Italy (IT).
  6. To close the **SSH-in-browser** dialog, enter **`exit`**.




## View the logs

You can verify that the firewall rules were applied to the egress traffic by accessing the logs. To view the log details, follow these steps:

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the **Network firewall policies** section, click the **`fw-policy`** name.

  3. Click view_column **Column display options**.

  4. In the **Displayed columns** dialog, select **Hit count** and then click **OK**.

  5. In the **Hit count** column, select the number for the rule you created during Create a global network firewall policy. The **Logs Explorer** page opens.

  6. To view the firewall rule applied to the egress traffic, expand the individual log. You can view the connection, disposition, and remote location details.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources.

In this section, you delete the resources created in this tutorial.

### Delete the firewall policy

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the **Network firewall policies** section, click the **`fw-policy`** name.

  3. Click the **Associations** tab.

  4. Select the checkbox of **`vpc-geo-location`** and click **Remove association**.

  5. In the **Remove a firewall policy association** dialog, click **Remove**.

  6. Next to the **`fw-policy`** title, click **Delete**.

  7. In the **Delete a firewall policy** dialog, click **Delete**.




###  gcloud 

  1. Remove the association between the firewall policy and VPC network.
         
         gcloud compute network-firewall-policies associations delete \
           --name=pol-association-fw-rules \
           --firewall-policy=fw-policy \
           --global-firewall-policy
         

**Note:** If you set up the association between the firewall policy and the VPC network through Google Cloud console, don't use the gcloud CLI command to remove the association. If you can't remember how you created the association or get the `The network firewall policy does not have an association with pol-association-fw-rules.` error when you run the command, use the Google Cloud console to remove the association.
  2. Delete the firewall policy.
         
         gcloud compute network-firewall-policies delete fw-policy \
             --global
         

When prompted, press `Y` to confirm, and then press `Enter`.




### Delete the VMs

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the checkboxes of **`instance-1-us`** and **`instance-2-sg`** VMs.

  3. Click **Delete**.

  4. In the **Delete 2 instances?** dialog, click **Delete**.




###  gcloud 

  1. To delete the **`instance-1-us`** VM, run the following command:
         
         gcloud compute instances delete instance-1-us \
             --zone=us-central1-a
         

When prompted, press `Y` to confirm, and then press `Enter`.

  2. To delete the **`instance-2-sg`** VM, run the following command:
         
         gcloud compute instances delete instance-2-sg \
             --zone=asia-southeast1-b
         

When prompted, press `Y` to confirm, and then press `Enter`.




### Delete the Cloud NAT gateway and Cloud Router

###  Console 

  1. In the Google Cloud console, go to the **Cloud routers** page.

[Go to Cloud routers](https://console.cloud.google.com/hybrid/routers/list)

  2. Select the **`router-fw-rules`** checkbox.

  3. Click **Delete**.

  4. In the **Delete router-fw-rules** dialog, click **Delete**.




When you delete a Cloud Router, the associated Cloud NAT gateway is also deleted.

###  gcloud 

To delete the **`router-fw-rules`** Cloud Router, run the following command:
    
    
    gcloud compute routers delete router-fw-rules \
        --region=us-central1
    

When prompted, press `Y` to confirm, and then press `Enter`.

When you delete a Cloud Router, the associated Cloud NAT gateway is also deleted.

### Delete the VPC network and its subnets

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. In the **Name** column, click **`vpc-geo-location`**.

  3. Click **Delete VPC network**.

  4. In the **Delete a network** dialog, click **Delete**.




When you delete a VPC, its subnets are also deleted.

###  gcloud 

  1. To delete the subnet **`subnet-1-us`** of the **`vpc-geo-location`** VPC network, run the following command:
         
         gcloud compute networks subnets delete subnet-1-us \
             --region=us-central1
         

When prompted, press `Y` to confirm, and then press `Enter`.

  2. To delete the subnet **`subnet-2-sg`** of the **`vpc-geo-location`** VPC network, run the following command:
         
         gcloud compute networks subnets delete subnet-2-sg \
             --region=asia-southeast1
         

When prompted, press `Y` to confirm and press `Enter`.

  3. To delete the **`vpc-geo-location`** VPC network, run the following command:
         
         gcloud compute networks delete vpc-geo-location
         

When prompted, press `Y` to confirm, and then press `Enter`.




## What's next

  * For conceptual information about firewall policies, see [Firewall policies and rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview).
  * For conceptual information about firewall policy rules, see [Firewall policy rule components](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details).
  * To create, update, monitor, and delete VPC firewall rules, see [Use VPC firewall rules](https://docs.cloud.google.com/firewall/docs/using-firewalls).
  * To determine costs, see [Cloud NGFW pricing](https://cloud.google.com/firewall/pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
