---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-fortanix-kms/
title: Configuring vSAN encryption using Fortanix KMS \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:49.870416+00:00
---

# Configuring vSAN encryption using Fortanix KMS  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-fortanix-kms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configuring vSAN encryption using Fortanix KMS

To encrypt data at rest using [vSAN encryption](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-vsan-encryption), one option is to use the Fortanix Key Management Service (KMS).

## Before you begin

  * Create a Google Cloud project or use an existing one.
  * Verify that you have at least three `n1-standard-4` or higher virtual machine (VM) instances.



## Deploy Fortanix KMS on Google Cloud

### Create a VPC network

For security purposes, create a new Virtual Private Cloud (VPC) network. You can control who has access by adding [firewall rules](https://docs.cloud.google.com/vmware-engine/docs/concepts-firewall-tables) or by using another [access control method](https://docs.cloud.google.com/vmware-engine/docs/concepts-permission-model). If your project has a default VPC network, don't use it. Instead, create your own VPC network with a different subnet IP range so that the only firewall rules in effect are those that you create explicitly.

### Create a VM instance template

  1. Follow the steps in [Creating instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates) to create a new instance template.
  2. Under **Machine type** , select **n1-standard-4 (4 vCPU, 15GB memory)** or higher. 
     1. In the **Boot disk** field, select **Ubuntu 16.04 LTS + 200GB SSD**.



### Create a managed instance group

Using the steps in [Creating managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances), create a managed instance group that uses the instance template you created in the previous step.

  * Disable [autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler).
  * Under **Number of instances** , enter the number of Fortanix KMS cluster nodes you want.



### Create a health check

On the **Create a health check** page, check for port 443. Click **Create** to create a health check.

### Create an internal TCP load balancer

  1. On the **Create a load balancer** page, under the **Internal facing or internal only** field, select **Only between my VMs**.
  2. Click **Continue** to create a new internal load balancer.
  3. Select **Backend configuration** in the left panel. 
     1. Select the new VPC network that you created.
     2. Select the managed instance group that you created.
  4. In the left panel, select **Frontend configuration**. 
     1. Select the new VPC network that you created.
     2. Under **Internal IP** , reserve an internal IP address.
     3. Under **Port number** , expose ports 443, 4445, and 5696.



### Create an external load balancer

  1. On the **Create a load balancer** page, under **Internal facing or internal only** , select **From internet to my VMs**.
  2. Click **Continue**.
  3. In the left panel, select **Backend configuration**. 
     1. Select the **Region**.
     2. Select the managed instance group that you created.
     3. Select the health check that you created.
  4. In the left panel, select **Frontend configuration**. 
     1. Select the VPC network that you created.
     2. Reserve a public IP address in the **IP** field.
     3. Under **Port number** , expose ports 443, 4445, and 5696.



### Add a firewall rule

By default, the [implied deny ingress](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules) VPC network firewall rule blocks unsolicited incoming connections to VMs in the VPC network.

To allow incoming connections, set up a firewall rule for your VM. After an incoming connection is established with a VM, traffic is permitted in both directions over that connection.

You can [create a firewall rule](https://docs.cloud.google.com/vmware-engine/docs/concepts-firewall-tables) to allow external access to specified ports, or to restrict access between VMs on the same network.

Add a firewall rule to allow the ports 443, 4445, and 5696. Select the VPC network you created and restrict the source IP, based on your security requirements.

### Create a DNS

You can create a DNS for internal and external load balancers by using [Cloud DNS](https://docs.cloud.google.com/dns/docs). On this page, `sdkms.vpc.gcloud` is the endpoint of the Fortanix KMS that's reachable from the VPC network and `sdkms.external.gcloud` is the endpoint that's reachable from the internet.

### Download and install Fortanix KMS

Install the Fortanix KMS software on each VM instance. For instructions, see the [Fortanix Self-Defending KMS installation guide](https://support.fortanix.com/hc/en-us/articles/360043996952-Using-Fortanix-Self-Defending-KMS-For-VMware-Encryption-on-GCP#4.0VPCPeeringwithGCVE-VPC). For the installation package compatible with Google Cloud, contact Fortanix Support.

### Configure UI/KMIP access

The UI can be accessed by using the `sdkms.external.gcloud` command. The Key Management Interoperability Protocol (KMIP) for VMware can be accessed by using `sdkms.vpc.gcloud`.

## Set up private services access

Set up private services access to VMware Engine and connect your VPC network to your private cloud. For instructions, see [Setting up private services access](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-setup-private-service-access).

## Establish trust between vCenter and Fortanix KMS

  1. In Fortanix KMS, configure a new app.
  2. In the **Applications** page, click **View credentials** for the app that you just created. Then, select the **Username/Password** tab and note the username and password to configure KMS in vCenter.
  3. In vCenter under **Key Management Servers** , configure internal IP `sdkms.vpc.gcloud`.
  4. Make vCenter trust Fortanix KMS: 
     1. In the vCenter **Configure** tab, click the listed Fortanix KMS.
     2. Click **Establish trust** , then click **Make vCenter trust KMS**.
     3. Click **Trust**.
  5. Make Fortanix KMS trust vCenter: 
     1. Click **Establish trust** , then click **Make KMS trust vCenter**.
     2. Under **Choose a method** , click **vCenter certificate**.
     3. Under **Download vCenter certificate** , click **Download** , then click **Done**.
  6. Enable vSAN encryption. 
     1. In the vSphere client, go to **Cluster > vSAN > Services**.
     2. Enable vSAN encryption.



Fortanix KMS is ready for use with vSAN encryption and vCenter VM encryption. A tamper-proof audit log captures all the crypto operations performed by the application. For VSAN encryption, new security keys are created in Fortanix KMS using the KMIP protocol.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
