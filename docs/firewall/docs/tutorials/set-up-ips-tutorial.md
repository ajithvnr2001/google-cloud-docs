---
url: https://docs.cloud.google.com/firewall/docs/tutorials/set-up-ips-tutorial/
title: Set up intrusion detection and prevention service in your network \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:06:38.378492+00:00
---

# Set up intrusion detection and prevention service in your network  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/tutorials/set-up-ips-tutorial/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Set up intrusion detection and prevention service in your network Stay organized with collections  Save and categorize content based on your preferences. 

[Intrusion detection and prevention service](https://docs.cloud.google.com/firewall/docs/about-intrusion-prevention) monitors your Google Cloud workload traffic for any malicious activity and takes preemptive actions to prevent it. To enable this service on your network, you must set up multiple Cloud Next Generation Firewall components. This tutorial describes the end-to-end workflow to configure intrusion detection and prevention service in your network.

## Objectives

This tutorial shows you how to complete the following tasks:

  * Create a Virtual Private Cloud (VPC) network with two subnets.
  * Create a server virtual machine (VM) instance in the first subnet of the VPC network and install the Apache server on the VM.
  * Create a client VM instance in the second subnet of the VPC network.
  * Create a security profile and a security profile group.
  * Create a firewall endpoint and associate it with the VPC network.
  * Add a global network firewall policy with the following firewall rules: 
    * A firewall rule to enable Identity-Aware Proxy (IAP) access to the VM instances in the VPC network.
    * A firewall rule to direct all ingress traffic for Layer 7 inspection.
  * Verify whether malicious traffic to the server VM instance is blocked.
  * Clean up the resources.



The following diagram shows the high-level architecture of the deployment setup in this tutorial. The firewall policy `fw-policy-ips` on VPC `vpc-ips`, redirects the ingress traffic to the firewall endpoint in zone `asia-southeast1-a`. The firewall endpoint `endpoint-ips` inspects the traffic for any threats. If any threat is detected, it applies the preventive actions by using the directions specified in the security profile `sec-profile-ips`.

[ ![Intrusion prevention and detection service in a custom VPC network to identify and prevent any threats.](https://docs.cloud.google.com/static/firewall/images/firewall-ips/ips-tutorial.svg)](https://docs.cloud.google.com/static/firewall/images/firewall-ips/ips-tutorial.svg) Intrusion detection and prevention service in a custom VPC network (click to enlarge).

## Costs

There is a cost associated with creating the firewall endpoints. For pricing details, see [Cloud Next Generation Firewall pricing](https://cloud.google.com/firewall/pricing).

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
  7. Enable the [Network Security API](https://console.cloud.google.com/marketplace/product/google/networksecurity.googleapis.com) for your project. 
  8. Enable the [Identity-Aware Proxy API](https://console.cloud.google.com/marketplace/product/google/iap.googleapis.com) for your project.
  9. Have the [Compute Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role on your organization. 
  10. If you prefer to work from the command line, install the Google Cloud CLI. For conceptual and installation information about the tool, see [gcloud CLI overview](https://docs.cloud.google.com/sdk/gcloud). 

**Note:** If you haven't run the gcloud CLI previously, first run [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) to initialize your gcloud CLI directory.




## Create a custom VPC network with subnets

In this section, you create a custom mode VPC network with two IPv4 subnets.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. For **Name** , enter `vpc-ips`.

  4. For **Description** , enter `VPC network to set up intrusion detection and prevention service`.

  5. For **Subnet creation mode** , select **Custom**.

  6. In the **New subnet** section, specify the following configuration parameters for a subnet:

     * **Name** : `subnet-server-ips`
     * **Region** : SERVER_REGION
     * **IPv4 range** : `10.0.0.0/24`
  7. Click **Done**.

  8. Click **Add subnet** and specify the following configuration parameters:

     * **Name** : `subnet-client-ips`
     * **Region** : CLIENT_REGION
     * **IPv4 range** : `192.168.10.0/24`
  9. Click **Done**.

  10. Click **Create**.




###  gcloud 

  1. To create a VPC network, run the following command:
         
         gcloud compute networks create vpc-ips \
           --subnet-mode custom \
           --description "VPC network to set up intrusion detection and prevention service."
         

  2. In the **Authorize cloud shell** dialog, click **Authorize**.

  3. To create a subnet, run the following command:
         
         gcloud compute networks subnets create subnet-server-ips \
           --network=vpc-ips \
           --region=SERVER_REGION \
           --range=10.0.0.0/24
         

Replace `SERVER_REGION` with the region where the subnet is created.

  4. To create another subnet, run the following command:
         
         gcloud compute networks subnets create subnet-client-ips \
           --network=vpc-ips \
           --region=CLIENT_REGION \
           --range=192.168.10.0/24
         

Replace `CLIENT_REGION` with the region where the subnet is created.




## Create a Cloud Router and a Cloud NAT gateway

Before you create client and server Linux VM instances without public IPv4 addresses in the next section, you must create a Cloud Router and a Cloud NAT gateway, which enables these VMs to access the public internet.

###  Console 

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. Click **Get started** or **Create Cloud NAT gateway**.

  3. For **Gateway name** , enter `gateway-ips`.

  4. For **NAT type** , select **Public**.

  5. In the **Select Cloud Router** section, specify the following configuration parameters:

     * **Network** : **`vpc-ips`**
     * **Region** : **SERVER_REGION**
     * **Cloud Router** : **Create new router**. 
       1. For **Name** , enter `router-ips`.
       2. Click **Create**.
  6. Click **Create**.




###  gcloud 

  1. To create a Cloud Router, run the following command:
         
         gcloud compute routers create router-ips \
           --network=vpc-ips \
           --region=SERVER_REGION
         

Replace `SERVER_REGION` with the region where the Cloud Router is created.

  2. To create a Cloud NAT gateway, run the following command:
         
         gcloud compute routers nats create gateway-ips \
           --router=router-ips \
           --region=SERVER_REGION \
           --auto-allocate-nat-external-ips \
           --nat-all-subnet-ip-ranges
         

Replace `SERVER_REGION` with the region where the Cloud NAT gateway is created.




## Create VM instances

In this section, you create server and client VM instances.

### Create the server VM instance

In this section, you create a VM instance in the subnet `subnet-server-ips` and install the Apache server on it.

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Machine configuration** pane, do the following:

     1. For **Name** , enter `vm-server-ips`.
     2. For **Region** , select SERVER_REGION.
     3. For **Zone** , select SERVER_ZONE.
  3. In the navigation menu, click **OS and Storage**.

In the **Operating system and storage** section, verify that **Image** is **Debian GNU/Linux 12 (bookworm)**. If it isn't, click **Change** and set the **Operating system** field to **Debian** and the **Version** field to **Debian GNU/Linux 12 (bookworm)**.

  4. In the navigation menu, click **Networking**.

     1. In the **Network interfaces** section, click **`default`** and specify the following configuration parameters: 
        * **Network** : **`vpc-ips`**
        * **Subnetwork** : **`subnet-server-ips IPv4 (10.0.0.0/24)`**
        * **External IPv4 address** : **None**
     2. Click **Done**.
  5. In the navigation menu, click **Advanced** and enter the following script in the **Startup script** field:
         
         #! /bin/bash
           apt update
           apt -y install apache2
           cat <<EOF > /var/www/html/index.html
           <html><body><p>Hello world.</p></body></html>
           EOF
         

  6. Click **Create**.

  7. Make a note of the **External IP** address of the server VM after it is created.




###  gcloud 

To create the server VM, run the following command:
    
    
    gcloud compute instances create vm-server-ips \
        --network=vpc-ips \
        --zone=SERVER_ZONE \
        --subnet=subnet-server-ips \
        --stack-type=IPV4_ONLY \
        --image-project=debian-cloud \
        --image-family=debian-11 \
        --metadata=startup-script='#! /bin/bash
         apt update
         apt -y install apache2
         cat <<EOF > /var/www/html/index.html
         <html><body><p>Hello World.</p></body></html>
         EOF'
    

Replace `SERVER_ZONE` with the zone where the server VM instance is created.

Make a note of the external IP address of the VM in the returned status.

### Create the client VM instance

In this section, you create a VM instance in the subnet `subnet-client-ips`.

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Machine configuration** pane, do the following:

     1. For **Name** , enter `vm-client-ips`.
     2. For **Region** , select CLIENT_REGION.
     3. For **Zone** , select CLIENT_ZONE.
  3. In the navigation menu, click **Networking**.

     1. In the **Network interfaces** section, click **`default`** and specify the following configuration parameters: 
        * **Network** : **`vpc-ips`**
        * **Subnetwork** : **`subnet-client-ips IPv4 (192.168.10.0/24)`**
     2. Click **Done**.
  4. Click **Create**.




###  gcloud 

To create the client VM, run the following command:
    
    
    gcloud compute instances create vm-client-ips \
        --network=vpc-ips \
        --zone=CLIENT_ZONE \
        --subnet=subnet-client-ips \
        --stack-type=IPV4_ONLY
    

Replace `CLIENT_ZONE` with the zone where the client VM instance is created.

## Create a threat prevention security profile

In this section, you create a security profile of type `threat-prevention` in your organization. To view the permissions required to create a security profile, see [Create a threat prevention security profile](https://docs.cloud.google.com/firewall/docs/configure-security-profiles#create-tp-security-profile).

###  Console 

  1. In the Google Cloud console, go to the **Security profiles** page.

[Go to Security profiles](https://console.cloud.google.com/net-security/security-profiles/profiles/list)

  2. In the project selector menu, select your organization.

  3. Select the **Security profiles** tab.

  4. Click **Create profile**.

  5. For **Name** , enter `sec-profile-ips`.

  6. For **Description** , enter `Security profile to set up intrusion detection and prevention service`.

  7. To create a security profile for Cloud Next Generation Firewall Enterprise, in the **Purpose** section, select **Cloud NGFW Enterprise**.

  8. To create a threat prevention security profile, for **Type** , select **Threat prevention**.

  9. Click **Create**.




###  gcloud 

To create a security profile, run the following command:
    
    
    gcloud network-security security-profiles \
        threat-prevention \
        create sec-profile-ips \
        --organization ORGANIZATION_ID \
        --location global \
        --project PROJECT_ID \
        --description "Security profile to set up intrusion detection and prevention service."
    

Replace the following:

  * `ORGANIZATION_ID`: the organization where the security profile is created.
  * `PROJECT_ID`: a project ID to use for quotas and access restrictions on the security profile.



## Create a security profile group

In this section, you create a security profile group to include the security profile that you created in the preceding section. To view the permissions required to create a security profile group, see [Permissions required for this task](https://docs.cloud.google.com/firewall/docs/configure-security-profile-groups#create-security-profile-group).

###  Console 

  1. In the Google Cloud console, go to the **Security profiles** page.

[Go to Security profiles](https://console.cloud.google.com/net-security/security-profiles/profiles/list)

  2. In the project selector menu, select your organization.

  3. Select the **Security profile groups** tab.

  4. Click **Create profile group**.

  5. For **Name** , enter `sec-profile-group-ips`.

  6. For **Description** , enter `Security profile group to set up intrusion detection and prevention service`.

  7. To create a security profile group for Cloud Next Generation Firewall Enterprise, in the **Purpose** section, select **Cloud NGFW Enterprise**.

  8. In the **Threat prevention profile** list, select `sec-profile-ips`.

  9. Click **Create**.




###  gcloud 

To create a security profile group, run the following command:
    
    
    gcloud network-security security-profile-groups \
        create sec-profile-group-ips \
        --organization ORGANIZATION_ID \
        --location global \
        --project PROJECT_ID \
        --threat-prevention-profile  \
        organizations/ORGANIZATION_ID/locations/global/securityProfiles/sec-profile-ips \
        --description "Security profile group to set up intrusion detection and prevention service."
    

Replace the following:

  * `ORGANIZATION_ID`: the organization where the security profile group is created.
  * `PROJECT_ID`: a project ID to use for quotas and access restrictions on the security profile group.



## Create a firewall endpoint

In this section you create a firewall endpoint in a specific zone. To view the permissions required to create a firewall endpoint, see [Permissions required for this task](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoints#create-firewall-endpoint).

**Note** : When you create a firewall endpoint, the state of the firewall endpoint is set to `Creating`. After the firewall endpoint is ready, the state changes to `Active`.

###  Console 

  1. In the Google Cloud console, go to the **Firewall endpoints** page.

[Go to Firewall endpoints](https://console.cloud.google.com/net-security/firewall-endpoints/list)

  2. In the project selector menu, select your organization.

  3. Click **Create**.

  4. In the **Region** list, select SERVER_REGION.

  5. In the **Zone** list, select SERVER_ZONE.

  6. For **Name** , enter `endpoint-ips`.

  7. In the **Billing project** list, select the Google Cloud project that you want to use for billing the firewall endpoint.

  8. Click **Create**.




###  gcloud 

To create a firewall endpoint, run the following command:
    
    
    gcloud network-security firewall-endpoints \
        create endpoint-ips \
        --organization=ORGANIZATION_ID \
        --zone=SERVER_ZONE \
        --billing-project=PROJECT_ID
    

Replace the following:

  * `ORGANIZATION_ID`: the organization where the firewall endpoint is created.
  * `SERVER_ZONE`: the zone where the firewall endpoint is created.
  * `PROJECT_ID`: a project ID to use for the billing of the firewall endpoint.



## Create a firewall endpoint association

In this section, you associate the firewall endpoint to the VPC network that you created in the preceding step.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the **`vpc-ips`** network to show its **VPC network details** page.

  3. Select the **Firewall endpoints** tab.

  4. Click **Create endpoint association**.

  5. In the **Region** list, select SERVER_REGION.

  6. In the **Zone** list, select SERVER_ZONE.

  7. In the **Firewall endpoint** list, select **`endpoint-ips`**.

  8. Click **Create**.




###  gcloud 

To create a firewall endpoint association, run the following command:
    
    
    gcloud network-security firewall-endpoint-associations \
        create endpoint-association-ips \
        --endpoint=organizations/ORGANIZATION_ID/locations/SERVER_ZONE/firewallEndpoints/endpoint-ips \
        --network=vpc-ips \
        --zone=SERVER_ZONE \
        --project=PROJECT_ID
    

Replace the following:

  * `ORGANIZATION_ID`: the organization where the firewall endpoint is created.
  * `SERVER_ZONE`: the zone where the firewall endpoint association is created.
  * `PROJECT_ID`: a project ID where the association is created.



## Create a global network firewall policy

In this section, you create a global network firewall policy that contains the following two firewall rules:

  1. An ingress firewall rule with priority `100` to allow TCP traffic to ports `3389` and `22`. This rule enables IAP access to the VM instances in the VPC network.
  2. An ingress firewall rule with priority `200` to perform Layer 7 inspection on the incoming traffic to the server VM in a specific zone.



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector list, select your project within your organization.

  3. Click **Create firewall policy**.

  4. For **Policy name** , enter `fw-policy-ips`.

  5. For **Policy type** , select **VPC policy**.

  6. For **Deployment scope** , select **Global**.

  7. Click **Continue** , and then click **Create firewall rule**.

  8. In the **Priority** field, enter `100`.

  9. For **Direction of traffic** , select **Ingress**.

  10. For **Action on match** , select **Allow**.

  11. For **Logs** , select **Enabled**.

  12. For the **Source** filter, select **IPv4** , and then in the **IP ranges** field enter `35.235.240.0/20`.

  13. In the **Protocols and ports** section, select **Specified protocols and ports**.

  14. Select **TCP** , and for **Ports** , enter `22,3389`.

  15. Click **Create**.

  16. Click **Create firewall rule**.

  17. In the **Priority** field, enter `200`.

  18. For **Direction of traffic** , select **Ingress**.

  19. For **Action on match** , select **Apply security profile group**.

  20. For **Logs** , select **Enabled**.

  21. In the **Security profile group** list, select **`sec-profile-group-ips`**.

  22. In the **Destination** filter, select **IPv4** , and then in the **IP ranges** field enter the external IP address of the server VM that you created in the Create the server VM instances section.

  23. Click **Create**.

  24. Click **Continue** to proceed to the **Add mirroring rules** section.

  25. Click **Continue** again to open the **Associate policy with networks** section.

  26. Select **`vpc-ips`** network.

  27. Click **Associate**.

  28. Click **Create**.




###  gcloud 

  1. To create a global network firewall policy, run the following command:
         
         gcloud compute network-firewall-policies \
           create fw-policy-ips \
           --global \
           --project PROJECT_ID
         

Replace the following:

     * `PROJECT_ID`: a project ID where the global network firewall policy is created.
  2. To add the firewall rule to enable IAP access, run the following command:
         
         gcloud compute network-firewall-policies rules create 100 \
           --firewall-policy fw-policy-ips \
           --direction INGRESS \
           --action ALLOW \
           --src-ip-ranges 35.235.240.0/20 \
           --layer4-configs tcp:22, tcp:3389 \
           --global-firewall-policy \
           --enable-logging
         

  3. To add the firewall rule to enable Layer 7 inspection for threat prevention and detection, run the following command:
         
         gcloud compute network-firewall-policies rules create 200 \
           --direction INGRESS \
           --firewall-policy fw-policy-ips \
           --action apply_security_profile_group \
           --src-ip-ranges 35.235.240.0/20 \
           --dest-ip-ranges SERVER_VM_IP \
           --layer4-configs tcp:0-65535 \
           --global-firewall-policy \
           --security-profile-group \
           //networksecurity.googleapis.com/organizations/ORGANIZATION_ID \
           /locations/global/securityProfileGroups/sec-profile-group-ips \
           --enable-logging
         

Replace the following:

     * `SERVER_VM_IP`: the external IP address of the server VM that you created in the Create the server VM instances section.

     * `ORGANIZATION_ID`: the organization where the secure profile group is created.

  4. To associate the firewall policy with the VPC network, run the following command:
         
         gcloud compute network-firewall-policies associations create \
          --firewall-policy fw-policy-ips \
          --network vpc-ips \
          --name fw-pol-association-ips \
          --global-firewall-policy \
          --project PROJECT_ID
         

Replace the following:

     * `PROJECT_ID`: the project ID where the VPC association is created.



## Test the setup

In this section, you test the setup by generating traffic that is intercepted by the endpoint, and the global network firewall policy is applied to perform Layer 7 inspection.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. From the **External IP** column of the **`vm-server-ips`** VM, copy the external IP address of the VM.

  3. In the **Connect** column of the **`vm-client-ips`** VM, click **SSH**.

  4. In the **SSH-in-browser** dialog, click **Authorize** and wait for the connection to establish.

  5. To verify whether a non-threat request isn't blocked, run the following command: 
         
         curl EXTERNAL_IP -m 2
         

Replace `EXTERNAL_IP` with the external IP of the `vm-server-ips` VM.

The expected response message is as follows:

`<!doctype html><html><body><h1>Hello World!</h1></body></html>`

  6. To verify that a malicious request is blocked, run the following command. This command sends a request to access the password file, which is forbidden.
         
         curl -m 2 EXTERNAL_IP:80/cgi-bin/../../../../bin/cat%20/etc/passwd/
         

Replace `EXTERNAL_IP` with the external IP of `vm-server-ips` VM.

A `Connection timed out` message is expected because the firewall endpoint detects the threat in the request and blocks the packet.

  7. Close the **SSH-in-browser** dialog.




###  gcloud 

  1. To connect to the `vm-client-ips` VM, run the following command:
         
         gcloud compute ssh vm-client-ips \
            --zone=CLIENT_ZONE \
            --tunnel-through-iap
         

Replace `CLIENT_ZONE` with the zone where the client VM instance is located.

When prompted, press `Y` to confirm, and then press `Enter`.

**Note:** While the SSH to the `vm-client-ips` VM is connected, ignore any warning messages that you see.
  2. To verify whether a non-threat request isn't blocked, run the following command: 
         
         curl EXTERNAL_IP -m 2
         

Replace `EXTERNAL_IP` with the external IP of the `vm-server-ips` VM.

The expected response message is as follows:

`<!doctype html><html><body><h1>Hello World!</h1></body></html>`

  3. To verify that a malicious request is blocked, run the following command:
         
         curl -m 2 EXTERNAL_IP:80/cgi-bin/../../../../bin/cat%20/etc/passwd/
         

Replace `EXTERNAL_IP` with the external IP of the `vm-server-ips` VM.

A `Connection timed out` message is expected because the firewall endpoint detects the threat in the request and blocks the packet.

  4. To close the **SSH-in-browser** , enter **`exit`**.




## View the threat logs

  1. In the Google Cloud console, go to the **Threats** page.

[Go to Threats](https://console.cloud.google.com/net-security/threats/list)

  2. If necessary, select your Google Cloud project.

  3. In the **Threat** section, you can see the logs entry for the threat detected on your `vpc-ips` network.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources.

In this section, you delete the resources created in this tutorial.

### Delete the firewall endpoint association

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the **`vpc-ips`** network to show its **VPC network details** page.

  3. Select the **Firewall endpoints** tab. The tab shows a list of configured firewall endpoint associations.

  4. Select the checkbox next to **`endpoint-ips`** , and then click **Delete**.

  5. Click **Delete** again to confirm.




###  gcloud 

To delete the firewall endpoint association, run the following command:
    
    
    gcloud network-security firewall-endpoint-associations \
        delete endpoint-ips \
        --zone=SERVER_ZONE
    

Replace `SERVER_ZONE` with the zone where the firewall endpoint association is located.

### Delete the firewall endpoint

###  Console 

  1. In the Google Cloud console, go to the **Firewall endpoints** page.

[Go to Firewall endpoints](https://console.cloud.google.com/net-security/firewall-endpoints/list)

  2. Select **`endpoint-ips`** , and then click **Delete**.

  3. Click **Delete** again to confirm.




###  gcloud 

To delete the firewall endpoint, run the following commands:
    
    
    gcloud network-security firewall-endpoints delete endpoint-ips \
        --organization=ORGANIZATION_ID \
        --zone=SERVER_ZONE
    

Replace the following:

  * `ORGANIZATION_ID`: the organization where the endpoint is created.
  * `SERVER_ZONE`: the zone where the endpoint is located.



### Delete the global network firewall policy

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select your project that contains the policy.

  3. Click **`fw-policy-ips`**.

  4. Click the **Associations** tab.

  5. Select all associations.

  6. Click **Remove Association**.

  7. After all associations are removed, click **Delete**.




###  gcloud 

  1. To remove the association between firewall policy and VPC network, run the following command:
         
         gcloud compute network-firewall-policies associations delete \
           --name fw-pol-association-ips \
           --firewall-policy fw-policy-ips \
           --global-firewall-policy
         

**Note:** If you set up the association between the firewall policy and the VPC network through Google Cloud console, don't use the gcloud CLI command to remove the association. If you can't remember how you created the association or get the `The network firewall policy does not have an association with pol-association-fw-rules` error when you run the command, use the Google Cloud console to remove the association.
  2. Delete the firewall policy.
         
         gcloud compute network-firewall-policies delete fw-policy-ips --global
         

When prompted, press `Y` to confirm, and then press `Enter`.




### Delete the security profile group

###  Console 

  1. In the Google Cloud console, go to the **Security profiles** page.

[Go to Security profiles](https://console.cloud.google.com/net-security/security-profiles/profiles/list)

  2. Select the **Security profile groups** tab.

  3. Select **`sec-profile-group-ips`** , and then click **Delete**.

  4. Click **Delete** again to confirm.




###  gcloud 

To delete the security profile group, run the following command:
    
    
    gcloud network-security security-profile-groups \
        delete sec-profile-group-ips \
        --organization ORGANIZATION_ID \
        --location global
    

Replace the following:

  * `ORGANIZATION_ID`: the organization where the security profile group is created.



### Delete the security profile

###  Console 

  1. In the Google Cloud console, go to the **Security profiles** page.

[Go to Security profiles](https://console.cloud.google.com/net-security/security-profiles/profiles/list)

  2. Select the **Security profiles** tab. The tab shows a list of configured security profiles.

  3. Select **`sec-profile-ips`** , and then click **Delete**.

  4. Click **Delete** again to confirm.




###  gcloud 

To delete the security profile, run the following command:
    
    
    gcloud network-security security-profiles threat-prevention \
        delete sec-profile-ips \
        --organization ORGANIZATION_ID \
        --location global
    

Replace the following:

  * `ORGANIZATION_ID`: the organization where the security profile is created.



### Delete the VMs

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the checkboxes of both the **`vm-client-ips`** and **`vm-server-ips`** VMs.

  3. Click **Delete**.

  4. In the **Delete 2 instances?** dialog, click **Delete**.




###  gcloud 

  1. To delete the `vm-client-ips` VM, run the following command:
         
         gcloud compute instances delete vm-client-ips \
           --zone=CLIENT_ZONE
         

Replace `CLIENT_ZONE` with the zone where the client VM instance is located.

When prompted, press `Y` to confirm, and then press `Enter`.

  2. To delete the `vm-server-ips` VM, run the following command:
         
         gcloud compute instances delete vm-server-ips \
           --zone=SERVER_ZONE
         

Replace `SERVER_ZONE` with the zone where the server VM instance is located.

When prompted, press `Y` to confirm, and then press `Enter`.




### Delete Cloud NAT gateway and Cloud Router

###  Console 

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. Select the checkbox next to the **`gateway-ips`** gateway configuration.

  3. On the more_vert**Menu** , click **Delete**.

  4. In the Google Cloud console, go to the **Cloud Routers** page.

[Go to Cloud Routers](https://console.cloud.google.com/hybrid/routers/list)

  5. Select the checkbox next to the **`router-ips`** router.

  6. Click **Delete**.




###  gcloud 

  1. To delete the Cloud NAT gateway, run the following command:
         
         gcloud compute routers nats delete gateway-ips \
           --router=router-ips \
           --region=SERVER_REGION
         

Replace `SERVER_REGION` with the region where the Cloud NAT gateway is located.

  2. To delete the Cloud Router, run the following command:
         
         gcloud compute routers delete router-ips \
           --project=PROJECT_ID \
           --region=SERVER_REGION
         




Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the Cloud Router.
  * `SERVER_REGION`: the region of the Cloud Router.



### Delete the VPC network and its subnets

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. In the **Name** column, click **`vpc-ips`**.

  3. Click **Delete VPC network**.

  4. In the **Delete network** dialog, click **Delete**.




When you delete a VPC, its subnets are also deleted.

###  gcloud 

  1. To delete the subnet `subnet-client-ips` of the `vpc-ips` VPC network, run the following command:
         
         gcloud compute networks subnets delete subnet-client-ips \
           --region=CLIENT_REGION
         

Replace `CLIENT_REGION` with the region where the subnet is located.




When prompted, press `Y` to confirm, and then press `Enter`.

  1. To delete the subnet `subnet-server-ips` of the `vpc-ips` VPC network, run the following command:
         
         gcloud compute networks subnets delete subnet-server-ips \
           --region=SERVER_REGION
         

Replace `SERVER_REGION` with the region where the subnet is located.

When prompted, press `Y` to confirm, and then press `Enter`.

  2. To delete the `vpc-ips` VPC network, run the following command:
         
         gcloud compute networks delete vpc-ips
         




## What's next

  * For conceptual information about intrusion detection and prevention service, see [Intrusion detection and prevention service overview](https://docs.cloud.google.com/firewall/docs/about-intrusion-prevention).
  * For conceptual information about firewall policies, see [Firewall policies and rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview).
  * For conceptual information about firewall policy rules, see [Firewall policy rule components](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details).
  * To determine costs, see [Cloud NGFW pricing](https://cloud.google.com/firewall/pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
