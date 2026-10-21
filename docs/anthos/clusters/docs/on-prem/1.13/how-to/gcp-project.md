---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/gcp-project/
title: Set up minimal infrastructure \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:03:11.946194+00:00
---

# Set up minimal infrastructure  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/gcp-project/

**Version 1.13**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.13 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/overview)



Send feedback 

#  Set up minimal infrastructure Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.13 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/minimal-infrastructure)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/minimal-infrastructure)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This is the first part of a guide that walks you through a small proof-of-concept installation of Google Distributed Cloud with a single user cluster.

This document shows you how to set up minimal vSphere and Google Cloud environments for this installation and plan your IP addresses, while the follow-up [Create basic clusters](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/minimal-create-clusters) shows you how to create an admin workstation, an admin cluster, and a user cluster.

The infrastructure you set up using this guide may not be suitable for your actual production needs and use cases. For more information about production installations, see the [Installation overview](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/install-overview) and guides.

## Before you begin

  * Read the [Google Distributed Cloud overview](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/overview), which provides an overview of how Google Distributed Cloud works, including the role of each component that you will install in this setup.

  * See [vSphere supported versions](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/vsphere-requirements#supported_versions).

  * See [vSphere license requirements](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/vsphere-requirements#license_requirements). For this minimal installation, a vSphere Standard license is sufficient.

  * You need a running instance of [vCenter Server](https://www.vmware.com/products/vcenter-server.html).

  * You need a vCenter user account with [sufficient privileges](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/vsphere-requirements#vcenter-user-account-privileges). Make a note of the username and password for this account.

  * You should be familiar with some basic Google Cloud concepts, including projects, IAM permissions, and service accounts. If not, see the following guides for more information:

    * [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects)
    * [IAM overview](https://docs.cloud.google.com/iam/docs/overview)
    * [Service accounts](https://docs.cloud.google.com/iam/docs/service-accounts)



## Procedure overview

These are the primary steps involved in this setup:

  1. **Set up your environment**. Ensure you can meet resource requirements. We provide an example configuration for an ESXi host and vSphere datastore that meet the requirements for this installation.
  2. **Set up vSphere objects**. Google Distributed Cloud components run within a vSphere object hierarchy.
  3. **Plan your IP addresses**. Google Distributed Cloud requires you to provide IP addresses for all nodes, in addition to virtual IP addresses (VIPs) for administrator and user access to your deployment. For this setup you will use static IP addresses for your cluster nodes. We provide examples, though we recommend you consult with your network administrator to help you choose suitable addresses for your own network.
  4. **Configure your firewall and proxy rules**
  5. **Set up Google Cloud resources** , including a Google Cloud project you will use when setting up and managing Google Distributed Cloud, and a service account with the necessary permissions to access and download Google Distributed Cloud component software.



## Set up your environment

### CPU, RAM and storage requirements

For this minimal installation, you can use a single physical host running [ESXi](https://www.vmware.com/products/esxi-and-esx.html).

These are the minimum resource requirements for your ESXi host:

  * 8 physical CPUs @ 2.7GHz with hyperthreading enabled
  * 80 gibibytes (GiB) RAM



The minimum storage requirement is 470 GiB.

### Example host and datastore

Here's an example of an [ESXi host](https://www.vmware.com/products/esxi-and-esx.html) and a [vSphere datastore](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.storage.doc/GUID-3CC7078E-9C30-402C-B2E1-2542BEE67E8F.html) that meet the requirements:

  * ESXi host configuration:

    * Manufacturer: Dell Inc.
    * Physical CPUs: 8 CPUs @ 2.7 GHz
    * Processor type: Intel(R) Xeon(R) Platinum 8168 CPU @ 2.70 GHz
    * Processor sockets: 2
    * ESXi version: 7.0u2 or above
    * vCenter Server version: 7.0u2 or above
    * Hyperthreading: enabled
  * Datastore configuration:

    * Type: VMFS 6.82
    * Drive type: SSD
    * Vendor: DELL
    * Drive type: logical
    * RAID level: RAID1



## Set up vSphere objects

Set up the following objects in your vSphere environment:

  * [vSphere data center](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vcenterhost.doc/GUID-7FDFBDBE-F8AC-4D00-AE5E-3F14D7472FAF.html)

  * [vSphere cluster](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-487C09CE-8BE2-4B89-BA30-0E4F7E3C66F7.html)

  * [vSphere datastore](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.storage.doc/GUID-3CC7078E-9C30-402C-B2E1-2542BEE67E8F.html)

  * [vSphere network](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.networking.doc/GUID-35B40B0B-0C13-43B2-BC85-18C9C91BE2D4.html)




## Load balancing

The clusters in this minimal installation use the bundled [MetalLB](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/bundled-load-balance-metallb) load balancer. This load balancer runs on the cluster nodes, so no additional VMs are needed for load balancing

## Plan your IP addresses

As you saw in the [Google Distributed Cloud overview](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/overview), an Google Distributed Cloud installation requires enough IP addresses for all its nodes, as well as virtual IP addresses (VIPs) for access to control plane components such as Kubernetes API servers and to applications running on your user clusters. You also need to specify suitable CIDR address ranges for communication between the Pods and Services on your clusters. Because of this, an important part of setting up Google Distributed Cloud is planning your IP addresses, including making sure that you don't create any addressing conflicts. You may need your network administrator to help you find suitable values to configure, even for this simple installation. In the rest of this section we provide illustrative examples of values that work for this installation in a hypothetical network - your values will be different.

Google Distributed Cloud lets you choose between providing [static IP addresses](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/manage-node-ip-addresses) for your cluster nodes, or using a DHCP server. In this simple installation, you will use static IP addresses.

For this small installation, we recommend that you put your admin workstation, admin cluster nodes, and user cluster nodes on the same VLAN in your vSphere network. For example, suppose all IP addresses in the 172.16.20.0/24 range are routed to a particular VLAN. Also suppose your network administrator says you can use 172.16.20.49 - 172.16.20.72 for VMs and virtual IP addresses (VIPs).

The following diagram illustrates a VLAN that has an admin workstation, an admin cluster, and a user cluster. Notice that VIPs are not shown associated with any particular node in a cluster. That is because the MetalLB load balancer can choose which node announces the VIP for an individual Service. For example, in the user cluster, one worker node could announce 172.16.20.63, and a different worker node could announce 172.16.20.64.

[ ![IP addresses for an admin cluster and a user cluster.](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.13/images/ip-addresses-minimal.svg)](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.13/images/ip-addresses-minimal.svg) IP addresses for an admin cluster and a user cluster (Click to enlarge)

### Example IP address: admin workstation

For the admin workstation, this example uses the first address in the range given to you by your network administrator: 172.16.20.49.

### Example IP addresses: cluster nodes

The following table gives an example of how IP addresses could be used for cluster nodes. The table shows two extra nodes: admin-vm-5 and user-vm-4. The extra nodes are needed during cluster upgrades, updates, and auto repair. For more information, see [Manage node IP addresses](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/manage-node-ip-addresses).

VM hostname | Description | IP address  
---|---|---  
admin-vm-1 | Control-plane node for the admin cluster | 172.16.20.50  
admin-vm-2 | Admin cluster add-on node | 172.16.20.51  
admin-vm-3 | Admin cluster add-on node | 172.16.20.52  
admin-vm-4 | Control-plane node for the user cluster.  
This node is in the admin cluster. | 172.16.20.53  
admin-vm-5 |  | 172.16.20.54  
user-vm-1 | User cluster worker node | 172.16.20.55  
user-vm-2 | User cluster worker node | 172.16.20.56  
user-vm-3 | User cluster worker node | 172.16.20.57  
user-vm-4 |  | 172.16.20.58  
  
### Example IP addresses: VIPs for the admin cluster

The following table gives an example of how you could specify VIPs for your admin cluster:

VIP | Description | IP address  
---|---|---  
VIP for the Kubernetes API server of the admin cluster | Configured on the load balancer for the admin cluster | 172.16.20.59  
  
### Example IP addresses: VIPs for the user cluster

The following table gives an example of how you could specify VIPs for your user cluster.

Notice that the VIP for the Kubernetes API server of the _user cluster_ is configured on the _admin cluster_ 's load balancer. That is because, as you learned in the overview, the Kubernetes API server for a user cluster runs on a node in the admin cluster.

VIP | Description | IP address  
---|---|---  
VIP for the Kubernetes API server of the user cluster | Configured on the load balancer for the admin cluster | 172.16.20.61  
Ingress VIP | Configured on the load balancer for the user cluster | 172.16.20.62  
Service VIPs | Ten addresses for Services of type `LoadBalancer`.  
Configured as needed on the load balancer for the user cluster.  
Notice that this range includes the ingress VIP.  
This is a requirement for the MetalLB load balancer. | 172.16.20.62 - 172.16.20.71  
  
### IP addresses for Pods and Services

In addition to the IP addresses for your cluster nodes and for accessing your deployment, you also need to specify the address ranges that can be used within each cluster for in-cluster traffic.

To do this you specify a [CIDR](https://datatracker.ietf.org/doc/html/rfc1519) range to be used for Pod IP addresses and another CIDR range to be used for the `ClusterIP` addresses of Kubernetes Services. This is specified as part of cluster configuration, as you will see in the next part of this guide.

As part of your IP planning, decide what CIDR ranges you want to use for Pods and Services. Unless you have a reason to do otherwise, use the following default ranges:

Purpose| Default CIDR range  
---|---  
Admin cluster Pods| 192.168.0.0/16  
User cluster Pods| 192.168.0.0/16  
Admin cluster Services| 10.96.232.0/24  
User cluster Services| 10.96.0.0/20  
  
The default values illustrate these points:

  * The Pod CIDR range can be the same for multiple clusters.

  * The Service CIDR range of a cluster must not overlap with the Service CIDR range of any other cluster.

  * Typically you need more Pods than Services, so for a given cluster, you probably want a Pod CIDR range that is larger than the Service CIDR range. For example, the default Pod range for a user cluster has 2^(32-16) = 2^16 addresses, but the default Service range for a user cluster has only 2^(32-20) = 12^12 addresses.




#### Avoid overlap

In some cases you might need to use non-default CIDR ranges to avoid overlapping with IP addresses that are reachable on your network. The Service and Pod ranges must not overlap with any address outside the cluster that you want to reach from inside the cluster.

For example, suppose your Service range is 10.96.232.0/24, and your Pod range is 192.168.0.0/16. Any traffic sent from a Pod to an address in either of those ranges will be treated as in-cluster and will not reach any destination outside the cluster.

In particular, the Service and Pod ranges must not overlap with:

  * IP addresses of nodes in any cluster

  * IP addresses used by load balancer machines

  * VIPs used by control-plane nodes and load balancers

  * IP address of vCenter servers, DNS servers, and NTP servers




We recommend that you use the private IP address ranges defined by [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918) for your Pod and Service ranges.

Here is one reason for the recommendation to use RFC 1918 addresses. Suppose your Pod or Service range contains external IP addresses. Any traffic sent from a Pod to one of those external addresses will be treated as in-cluster traffic and will not reach the external destination.

### DNS server and default gateway

Before you create your admin and user clusters, you must also know the IP addresses of:

  * A DNS server that can be used by your admin workstation and cluster nodes

  * An NTP server that can be used by your cluster nodes

  * The IP address of the default gateway for the subnet that has your admin workstation and cluster nodes. For example, suppose your admin workstation, admin cluster nodes, and user cluster nodes are all in the 172.16.20.0/24 subnet. The address of the default gateway for the subnet might be 172.16.20.1.




## Configure your firewall and proxy

Configure your firewall and proxy to allow necessary Google Distributed Cloud traffic, following the [Proxy and firewall rules](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/firewall-rules). You will need the cluster node IP addresses that you identified in the previous section to carry out this task. Note that because the IP addresses for user and admin clusters are not assigned to specific nodes, you must make sure that all of the relevant firewall rules apply to all of the IP addresses for each cluster.

## Set up Google Cloud resources

Google Cloud projects form the basis for creating, enabling, and using all Google Cloud services, including those used to install and manage Google Distributed Cloud. If you're not familiar with working with Google Cloud projects, you can find lots more information in [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

To start setting up Google Cloud resources:

  1. Choose an existing project for your installation, or create a new one.
  2. Make a note of your Google Cloud project ID.

**Note:** This simple example uses a single project to manage all aspects of your deployment. For more complex production installations you may want to use [separate projects](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/gcp-project/) for different aspects of Google Distributed Cloud: for example, a specific project for collecting and viewing your logging and monitoring data.

### Required permissions

If you are the project owner (for example, if you created the project yourself), you already have all the permissions necessary to perform the rest of this simple installation. If you are _not_ the project owner, you or your project administrator must ensure your Google account has the necessary permissions.

The following [IAM roles](https://docs.cloud.google.com/iam/docs/overview) let you create a service account, assign IAM roles to it, enable APIs, and ensure that the `gkeadm` tool can create and manage service accounts for you in the second part of this setup:

  * `resourcemanager.projectIamAdmin`
  * `serviceusage.serviceUsageAdmin`
  * `iam.serviceAccountCreator`
  * `iam.serviceAccountKeyAdmin`



For details of the permissions required to grant IAM roles yourself, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). If you don't have these permissions, someone else in your organization must grant the roles for you.

To grant the roles:

### Linux and macOS
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="user:ACCOUNT" \
        --role="roles/resourcemanager.projectIamAdmin"
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="user:ACCOUNT" \
        --role="roles/serviceusage.serviceUsageAdmin"
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="user:ACCOUNT" \
        --role="roles/iam.serviceAccountCreator"
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="user:ACCOUNT" \
        --role="roles/iam.serviceAccountKeyAdmin"
    

### Windows
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID ^
        --member="user:ACCOUNT" ^
        --role="roles/resourcemanager.projectIamAdmin"
    
    gcloud projects add-iam-policy-binding PROJECT_ID ^
        --member="user:ACCOUNT" ^
        --role="roles/serviceusage.serviceUsageAdmin"
    
    gcloud projects add-iam-policy-binding PROJECT_ID ^
        --member="user:ACCOUNT" ^
        --role="roles/iam.serviceAccountCreator"
    
    gcloud projects add-iam-policy-binding PROJECT_ID ^
        --member="user:ACCOUNT" ^
        --role="roles/iam.serviceAccountKeyAdmin"
    

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `ACCOUNT`: the identifying email address for your Google account



### Set up the Google Cloud CLI

The Google Cloud CLI is a command line tool you can use to work with your project. Follow the instructions in [Installing Google Cloud SDK](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/cloud-sdk) to ensure you have the most up to date version.

### Set up your component access service account

In your project, set up a [service account](https://docs.cloud.google.com/iam/docs/service-accounts) that Google Distributed Cloud can use to download cluster component code on your behalf from Container Registry. This is known as your _component access service account_ , and is the only service account you must create manually in this simple installation.

  1. In your chosen Google Cloud project, create a new service account as follows:
         
         gcloud iam service-accounts create component-access-sa \
             --display-name "Component Access Service Account" \
             --project PROJECT_ID
         

Replace PROJECT_ID with the ID of your Google Cloud project.

  2. Create a JSON key for your component access service account:
         
         gcloud iam service-accounts keys create component-access-key.json \
            --iam-account SERVICE_ACCOUNT_EMAIL
         

Replace SERVICE_ACCOUNT_EMAIL with your service account's unique identifying email address.

  3. Add the following [IAM roles](https://docs.cloud.google.com/iam/docs/understanding-roles) to your component access service account:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member "serviceAccount:SERVICE_ACCOUNT_EMAIL" \
             --role "roles/serviceusage.serviceUsageViewer"
         
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member "serviceAccount:SERVICE_ACCOUNT_EMAIL" \
             --role "roles/iam.roleViewer"
         
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member "serviceAccount:SERVICE_ACCOUNT_EMAIL" \
             --role "roles/iam.serviceAccountViewer"
         




For more information about the component access service account and granting IAM roles, see [Service accounts and keys](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/service-accounts).

### Enable Google APIs

Enable the following Google APIs in your Google Cloud project. This lets you use all the Google Cloud services needed by Google Distributed Cloud in your project.
    
    
    gcloud services enable --project PROJECT_ID \
        anthos.googleapis.com \
        anthosgke.googleapis.com \
        anthosaudit.googleapis.com \
        cloudresourcemanager.googleapis.com \
        connectgateway.googleapis.com \
        container.googleapis.com \
        gkeconnect.googleapis.com \
        gkehub.googleapis.com \
        serviceusage.googleapis.com \
        stackdriver.googleapis.com \
        opsconfigmonitoring.googleapis.com \
        monitoring.googleapis.com \
        logging.googleapis.com \
        iam.googleapis.com \
        storage.googleapis.com
     

## What's next

[Create basic clusters](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/minimal-create-clusters)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
