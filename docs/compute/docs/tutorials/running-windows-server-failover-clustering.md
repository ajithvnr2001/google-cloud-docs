---
url: https://docs.cloud.google.com/compute/docs/tutorials/running-windows-server-failover-clustering/
title: Running Windows Server Failover Clustering \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:29:03.785532+00:00
---

# Running Windows Server Failover Clustering  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/tutorials/running-windows-server-failover-clustering/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Running Windows Server Failover Clustering Stay organized with collections  Save and categorize content based on your preferences. 

You can create a failover cluster using Windows Server on Google Cloud. A group of servers works together to provide higher availability (HA) for your Windows applications. If one _cluster node_ fails, another node can take over running the software. You can configure the failover to happen automatically, which is the usual configuration, or you can manually trigger a failover.

This tutorial assumes you are familiar with failover clustering, Active Directory (AD), and administration of Windows Server.

For a brief overview of networking in Google Cloud, see [Google Cloud for Data Center Pros: Networking](https://docs.cloud.google.com/docs/compare/data-centers/networking).

## Architecture

This tutorial walks you through how to create an example failover cluster on Compute Engine. The example system contains the following two servers:

  * A primary Compute Engine VM instance running Windows Server 2016 in zone `a`.
  * A second instance, configured to match the primary instance in zone `b`.



Additionally, you deploy an AD domain controller, which, for this tutorial, serves the following purposes:

  * Provides a Windows domain.
  * Resolves hostnames to IP addresses.
  * Hosts the _file share witness_ that acts as a third "vote" to achieve the [required quorum for the cluster](https://technet.microsoft.com/en-us/library/jj612870\(v=ws.11\).aspx).



You can create the domain controller in any zone. This tutorial uses zone `c`. In a production system, you can host the file share witness elsewhere, and you don't need a separate AD system only to support your failover cluster. See What's next for links to articles about using AD on Google Cloud.

The two servers that you will use to deploy the failover cluster are located in different zones to ensure that each server is on a different physical machine and to protect against the unlikely possibility of a zonal failure.

The following diagram describes the architecture you deploy by following this tutorial.

![Architecture diagram showing two Compute Engine VMs in a failover cluster](https://docs.cloud.google.com/static/compute/docs/tutorials/images/failover-clustering-architecture.svg)

### Shared storage options

This tutorial does not cover setting up a file server for high-availability shared storage.

Google Cloud supports multiple shared storage solutions that you can use with Windows Server Failover Clustering, including:

  * [SIOS Datakeeper Cluster Edition](https://us.sios.com/products/sios-datakeeper/)
  * [Native Microsoft Windows options](https://docs.microsoft.com/en-us/windows-server/failover-clustering/clustering-requirements)



For information about other possible shared storage solutions, see:

  * [Google Cloud Windows Partners](https://cloud.google.com/windows/partners/)
  * [File servers on Compute Engine](https://docs.cloud.google.com/solutions/filers-on-compute-engine).



### Understanding the network routing

When the cluster fails over, requests must go to the newly active node. The clustering technology normally handles routing by using [address resolution protocol](https://wikipedia.org/wiki/Address_Resolution_Protocol) (ARP), which associates IP addresses with MAC addresses. In Google Cloud, the Virtual Private Cloud (VPC) system uses [software-defined networking](https://wikipedia.org/wiki/Software-defined_networking), which doesn't leverage MAC addresses. This means the changes broadcast by ARP don't affect routing at all. To make routing work, the cluster requires some software-level help from the [Internal Load Balancer](https://docs.cloud.google.com/compute/docs/load-balancing/internal).

Usually, internal load balancing distributes incoming network traffic among multiple backend instances that are internal to your VPC, to share the load. For failover clustering, you instead use internal load balancing to route all traffic to just one instance: the currently active cluster node. Here's how internal load balancing detects the correct node:

  * Each VM instance runs a Compute Engine agent instance that provides support for Windows failover clustering. The agent keeps track of the IP addresses for the VM instance.
  * The load balancer's frontend provides the IP address for incoming traffic to the application.
  * The load balancer's backend provides a health check. The health check process periodically pings the agent on each cluster node by using the fixed IP address of the VM instance through a particular port. The default port is 59998.
  * The health check includes the application's IP address as a payload in the request.
  * The agent compares the IP address in the request to the list of IP addresses for the host VM. If the agent finds a match, it responds with a value of 1. Otherwise, it responds with 0.
  * The load balancer marks any VM that passes the health check as _healthy_. At any moment, only one VM ever passes the health check because only one VM has the IP address for the workload.



### What happens during a failover

When a failover happens in the cluster, the following changes take place:

  * Windows failover clustering changes the status of the active node to indicate that it has failed.
  * Failover clustering moves any cluster resources and roles from the failing node to the best node, as defined by the quorum. This action includes moving the associated IP addresses.
  * Failover clustering broadcasts ARP packets to notify hardware-based network routers that the IP addresses have moved. For this scenario, Google Cloud networking ignores these packets.
  * After the move, the Compute Engine agent on the VM for the failing node changes its response to the health check from 1 to 0, because the VM no longer hosts the IP address specified in the request.
  * The Compute Engine agent on the VM for the newly active node likewise changes its response to the health check from 0 to 1.
  * The internal load balancer stops routing traffic to the failing node and instead routes traffic to the newly active node.



### Putting it together

Now that you've reviewed some of the concepts, here are some details to notice about the architecture diagram:

  * The Compute Engine agent for the VM named `wsfc-2` is responding to the health check with the value 1, indicating it is the active cluster node. For `wsfc-1`, the response is 0.
  * The load balancer is routing requests to `wsfc-2`, as indicated by the arrow.
  * The load balancer and `wsfc-2`both have the IP address `10.0.0.9`. For the load balancer, this is the specified frontend IP address. For the VM, it's the IP address of the application. The failover cluster sets this IP address on the currently active node.
  * The failover cluster and `wsfc-2` both have the IP address `10.0.0.8`. The VM has this IP address because it currently hosts the cluster resources.



## Advice for following this tutorial

This tutorial has a lot of steps. Sometimes, you are asked to follow steps in external documents, such as Microsoft documentation. Don't miss the notes in this document providing specifics for following the external steps.

This tutorial uses Cloud Shell in the Google Cloud console. Though it's possible to use the Google Cloud console user interface or the gcloud CLI to set up failover clustering, this tutorial mainly uses Cloud Shell to make it easy for you. This approach helps you to complete the tutorial faster. When more appropriate, some steps use the Google Cloud console instead.

![Cloud Shell](https://docs.cloud.google.com/static/compute/docs/tutorials/images/failover-clustering-cloud-shell.png)

It's a good idea to [take snapshots of your Compute Engine persistent disks](https://docs.cloud.google.com/compute/docs/disks/create-snapshots) along the way. If something goes wrong, you can use a snapshot to avoid starting over from the beginning. This tutorial suggests good times to take the snapshots.

If you find that things aren't working as you expect, there might be instructions in the section you're reading. Otherwise, refer to the Troubleshooting section.

## Objectives

  * Create a network.
  * Install Windows Server 2016 on two Compute Engine VMs.
  * Install and configure Active Directory on a third instance of Windows Server.
  * Set up the failover cluster, including a file share witness for the quorum and a role for the workload.
  * Set up the internal load balancer.
  * Test the failover operation to verify that the cluster is working.



## Costs

This tutorial uses Compute Engine images that include Windows Server licenses. This means the cost to run this tutorial can be significant if you leave VMs running. It's a good idea to stop the VMs when you're not using them.

See the [Pricing Calculator](https://cloud.google.com/products/calculator/#id=fbf3d50a-1f20-4ac0-9c9e-d99c50529899) for an estimate of the costs to complete this tutorial.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute)

  8. Start an instance of Cloud Shell.  
[Go to Cloud Shell](https://console.cloud.google.com/?cloudshell=true)



## Creating the network

Your cluster requires a custom network. Use VPC to create a custom network and one subnetwork by running `gcloud` commands in Cloud Shell.

  1. Create the network:
         
         gcloud compute networks create wsfcnet --subnet-mode custom
         

The name of the network you created is `wsfcnet`.

  2. Create a subnetwork. Replace `[YOUR_REGION]` with a nearby Google Cloud region:
         
         gcloud compute networks subnets create wsfcnetsub1 --network wsfcnet --region [YOUR_REGION] --range 10.0.0.0/16
         

The name of the subnetwork you created is `wsfcnetsub1`.




Notice that the [CIDR](https://wikipedia.org/wiki/Classless_Inter-Domain_Routing) range for IP addresses in this subnetwork is `10.0.0.0/16`. This is an example range used for this tutorial. In production systems, work with your network administrators to allocate appropriate ranges for IP addresses for your systems.

### Create firewall rules

By default, your network is closed to external traffic. You must open ports in the firewall to enable remote connections to the servers. Use `gcloud` commands in Cloud Shell to create the rules.

  1. For this tutorial, open port 3389 on the main network to enable RDP connections. In the following command, replace `[YOUR_IPv4_ADDRESS]` with the IP address of the computer you use to connect to your VM instances. In a production system, [you can provide an IP address range or a series of addresses](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create).
         
         gcloud compute firewall-rules create allow-rdp --network wsfcnet --allow tcp:3389 --source-ranges [YOUR_IPv4_ADDRESS]
         

  2. On the subnetwork, allow all protocols on all ports to enable the servers to communicate with each other. In production systems, consider opening only specific ports, as needed.
         
         gcloud compute firewall-rules create allow-all-subnet --network wsfcnet --allow all --source-ranges 10.0.0.0/16
         

Notice that the `source-ranges` value matches the CIDR range you used to create the subnetwork.

  3. View your firewall rules:
         
         gcloud compute firewall-rules list
         

You should see output similar to the following:
         
         NAME              NETWORK  DIRECTION  PRIORITY  ALLOW            DENY  DISABLED
         allow-all-subnet  wsfcnet  INGRESS    1000      all                    False
         allow-rdp         wsfcnet  INGRESS    1000      tcp:3389               False




## Enabling failover clustering in Compute Engine

To enable failover clustering in the Compute Engine agent, you need to add the flag `enable-wsfc=true` to your VM definitions either by specifying it as custom metadata for the VM or by creating a configuration file on each VM, as described in the [Compute Engine documentation](https://docs.cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances#windows_server_failover_clustering).

This tutorial defines the flag as custom metadata when the VMs are created, as described in the next section. The tutorial also relies on the default behavior for `wsfc-addrs` and `wsfc-agent-port`, so you don't need to set these values.

## Creating the servers

Next, create the 3 servers. Use the `gcloud` command in Cloud Shell.

### Create the first cluster-node server

Create a new Compute Engine instance. Configure the instance as follows:

  * Name the instance `wsfc-1`.
  * Set the `--zone` flag to a convenient zone near you. For example, `us-central1-a`.
  * Set the `--machine-type` flag to `n1-standard-2.`
  * Set the`--image-project` flag to `windows-cloud`.
  * Set the `--image-family` flag to `windows-2016`.
  * Set the`--scopes` flag to `https://www.googleapis.com/auth/compute`.
  * Set the `--can-ip-forward` flag to enable IP forwarding.
  * Set the `--private-network-ip` flag to `10.0.0.4`.
  * Set the network to `wsfcnet` and the subnetwork to `wsfcnetsub1`.
  * Use the `--metadata` parameter to set `enable-wsfc=true`.



Run the following command, replacing `[YOUR_ZONE_1]` with the name of your first zone:
    
    
    gcloud compute instances create wsfc-1 --zone [YOUR_ZONE_1] --machine-type n1-standard-2 --image-project windows-cloud --image-family windows-2016 --scopes https://www.googleapis.com/auth/compute --can-ip-forward --private-network-ip 10.0.0.4 --network wsfcnet --subnet wsfcnetsub1 --metadata enable-wsfc=true
    

### Create the second cluster-node server

For the second server, follow the same steps, except:

  * Set the instance name to: `wsfc-2`.
  * Set the `--zone` flag to a different zone than the zone that you used for the first server. For example, `us-central1-b`.
  * Set the `--private-network-ip` flag to `10.0.0.5`.



Replace `[YOUR_ZONE_2]` with the name of your second zone:
    
    
    gcloud compute instances create wsfc-2 --zone [YOUR_ZONE_2] --machine-type n1-standard-2 --image-project windows-cloud --image-family windows-2016 --scopes https://www.googleapis.com/auth/compute --can-ip-forward --private-network-ip 10.0.0.5 --network wsfcnet --subnet wsfcnetsub1  --metadata enable-wsfc=true
    

### Create the third server for Active Directory

For the domain controller, follow the same steps, except:

  * Set the instance name to: `wsfc-dc`.
  * Set the `--zone` flag to a different zone than the zones that you used for the other servers. For example, `us-central1-c`.
  * Set the `--private-network-ip` flag to `10.0.0.6`.
  * Omit `--metadata enable-wsfc=true`.



Replace `[YOUR_ZONE_3]` with the name of your zone:
    
    
    gcloud compute instances create wsfc-dc --zone [YOUR_ZONE_3] --machine-type n1-standard-2 --image-project windows-cloud --image-family windows-2016 --scopes https://www.googleapis.com/auth/compute --can-ip-forward --private-network-ip 10.0.0.6 --network wsfcnet --subnet wsfcnetsub1
    

### View your instances

You can see the details about the instances you created.
    
    
    gcloud compute instances list
    

You will see output similar to the following:
    
    
    NAME     ZONE           MACHINE_TYPE  PREEMPTIBLE INTERNAL_IP  EXTERNAL_IP     STATUS
    wsfc-1   us-central1-a  n1-standard-2             10.0.0.4     35.203.131.133  RUNNING
    wsfc-2   us-central1-b  n1-standard-2             10.0.0.5     35.203.130.194  RUNNING
    wsfc-dc  us-central1-c  n1-standard-2             10.0.0.6     35.197.27.2     RUNNING
    

## Connecting to your VMs

To connect to a Windows-based VM, you must first generate a password for the VM. You can then connect to the VM using RDP.

### Generating passwords

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of the VM instance for which you need a new password.

  3. On the instance details page, click the **Set Windows Password** button. A password is generated for you. Copy the password and store it in a secure place.




### Connecting through RDP

The Compute Engine documentation provides details about how to connect to your Windows VM instances by using RDP. You can either:

  * Use an existing client.
  * Add a Chrome RDP plugin to your browser and then [connect](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) through the Google Cloud console.



Whenever this tutorial tells you to connect to a Windows instance, use your preferred RDP connection.

## Configuring Windows networking

The internal IP addresses that you assigned when you created the VMs are static. To ensure that Windows treats the IP addresses as static, you need to add them, along with the IP addresses of the default gateway and the DNS server, to the Windows Server networking configuration.

Use RDP to connect to `wsfc-1`, `wsfc-2`, and `wsfc-dc`, and repeat the following steps for each instance:

  1. In Server Manager, in the left pane, select **Local Server**.
  2. In the **Ethernet** entry of the **Properties** pane, click **IPv4 address assigned by DHCP, IPv6 enabled**.
  3. Right-click **Ethernet** and select **Properties**.
  4. Double-click **Internet Protocol Version 4 (TCP/IPv4)**.
  5. Select **Use the following IP address**.
  6. Enter the internal IP address that you assigned to the VM when you created it.

     * For `wsfc-1`, enter "10.0.0.4".
     * For `wsfc-2` enter "10.0.0.5".
     * For `wsfc-dc` enter "10.0.0.6".
  7. For **Subnet mask** , enter "255.255.0.0".

  8. For **Default gateway** , enter `10.0.0.1`, the IP address that was automatically reserved for the default gateway when you created the subnet `wsfcnetsub1`.

The IP address for the default gateway is always the second address in the primary IP range for a subnet. See [Unusable addresses in IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#unusable-ip-addresses-in-every-subnet).

  9. For `wsfc-1` and `wsfc-2` only:

     1. Click **Use the following DNS server addresses**.

     2. For **Preferred DNS server** , enter "10.0.0.6".

  10. Close all the dialog boxes.

You lose RDP connectivity because these changes reset the virtual network adapter for the VM instance.

  11. Close the RDP session and then reconnect to the instance. If a dialog box from the previous step is still open, close it.

  12. In the properties section for the local server, verify that the **Ethernet** setting reflects the local server IP address (`10.0.0.4`, `10.0.0.5`,``or`10.0.0.6`). If it doesn't, re-open the **Internet Protocol Version 4 (TCP/IPv4)** dialog box and update the setting.




This is a good time to take snapshots of `wsfc-1` and `wsfc-2`.

## Setting up Active Directory

Now, set up the domain controller.

  1. Use RDP to connect to the server named `wsfc-dc`.
  2. Using the Windows Computer Management desktop app, set a password for the [local Administrator account](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/local-accounts#sec-default-accounts).
  3. Enable the local Administrator account.
  4. Follow the steps in the Microsoft instructions below to set up the domain controller, with these additional notes. You can use default values for most settings.

     * Select the DNS Server role check box. This step is not specified in the instructions.
     * Select the **Restart the destination server automatically if required** check box.
     * Promote the file server to a domain controller.
     * During the **Add a new forest** step, name your domain "WSFC.TEST".
     * Set the NetBIOS domain name to "WSFC" (the default).

[Microsoft instructions](https://social.technet.microsoft.com/wiki/contents/articles/12370.windows-server-2012-set-up-your-first-domain-controller-step-by-step.aspx)




This is a good time to take a snapshot of `wsfc-dc`.

### Create the domain user account

It can take some time for `wsfc-dc` to restart. Before joining servers to the domain, use RDP to sign in to `wsfc-dc` to validate that the domain controller is running.

You need a domain user that has administrator privileges for the cluster servers. Follow these steps:

  1. On the domain controller (`wsfc-dc`) click **Start** , and then type **dsa** to find and open the Active Directory Users and Computers app.
  2. Right-click **WSFC.TEST** , point to **New** , and then click **User**.
  3. For the **Full name** and the **User logon name** , enter `cluster-admin`.
  4. Click **Next**.
  5. Enter and confirm a password for the user. Select password options in the dialog box. For example, you can set the password to never expire.
  6. Confirm the settings and then click **Finish**.
  7. Make `cluster-admin` an administrator on `wsfc-dc`:

     * Right-click `cluster-admin` and select **Add to a group**.
     * Type **Administrators** , and click **OK**.



This tutorial uses the `WSFC.TEST\cluster-admin` account as an administrator account wherever such an account is required. In a production system, follow your usual security practices for allocating accounts and permissions. For more information, see [Overview of Active Directory accounts needed by a failover cluster](https://docs.microsoft.com/en-us/windows-server/failover-clustering/configure-ad-accounts#overview-of-active-directory-accounts-needed-by-a-failover-cluster).

### Join the servers to the domain

Add the two cluster-node servers to the `WSFC.TEST` domain. Perform the following steps on each cluster-node server (`wsfc-1` and `wsfc-2`):

  1. In **Server Manager** > **Local Server** , in the **Properties** pane, click **WORKGROUP**.
  2. Click **Change**.
  3. Select **Domain** and then enter "WSFC.TEST".
  4. Click **OK**.
  5. Provide the credentials for `WSFC.TEST\cluster-admin` to join the domain.
  6. Click **OK**.
  7. Close the dialog boxes and follow the prompts to restart the server.
  8. In **Server Manager** , make `cluster-admin` an administrator on `wsfc-1` and `wsfc-2`. Alternatively, you can manage administrative privileges by using a group policy.

     * On the **Tools** menu, select **Computer Management** > **Local Users and Groups** > **Groups** > **Administrators** , and then click **Add**.
     * Enter "cluster-admin" and the click **Check names**.
     * Click **OK**.



This is a good point to take snapshots of all three VMs.

## Setting up failover clustering

### Reserve an IP address for the cluster in Compute Engine

When you create the failover cluster, you assign an IP address to create an administrative access point. In a production environment, you might use an IP address from a separate subnet. However, in this tutorial you reserve an IP address from the subnet you already created. Reserving the IP address prevents conflicts with other IP assignments.

  1. Open a terminal on a host VM or open Cloud Shell.

[Go to Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Reserve an IP address. For this tutorial, use `10.0.0.8`:
         
         gcloud compute addresses create cluster-access-point --region [YOUR_REGION] --subnet wsfcnetsub1 --addresses 10.0.0.8

  3. To confirm the reservation of the IP address:
         
         gcloud compute addresses list




### Create the cluster

To create and configure the failover cluster:

  1. Use RDP to connect `wsfc-1` and `wsfc-2`.
  2. Follow the steps in the Microsoft instructions below, with these additional notes:

     * Install the Failover Clustering feature on `wsfc-1` and `wsfc-2`. Don't install the Failover Clustering feature on `wsfc-dc`.
     * Run the Failover Cluster Manager app as the domain user `WSFC.TEST\cluster-admin`. Otherwise, you might encounter permissions issues. It's a good idea to always run Failover Cluster Manager this way or to connect to a server as `cluster-admin` to ensure you have the required permissions.
     * Add `wsfc-1` and `wsfc-2` to the cluster as nodes.
     * When validating the configuration:

       * On the **Testing Options** ​ page, select **Run only tests I select** ​, ​and then click **Next​**.
       * On the **Test Selection** ​ page, clear **Storage** because the **Storage​** option will fail when running on Compute Engine (as it would for separate standalone physical servers).

Common issues you might encounter during cluster validation include:

         * **Only one network interface between replicas**. You can ignore this one, because it doesn't apply in a cloud-based setup.
         * **Windows Updates not the same on both replicas**. If you configured your Windows instances to apply updates automatically, one of the nodes might have applied updates that the other hasn't downloaded yet. You should keep the servers in identical configurations.
         * **Pending reboot**. You've made changes to one of the servers, and it needs a reboot to apply. Don't ignore this one.
         * **The servers do not all have the same domain role**. You can ignore this one.
         * **The servers are not all in the same Organizational Unit (OU)**. This tutorial doesn't use an OU at all, but in a production system consider putting your cluster in its own OU. The Microsoft instructions describe this best practice.
         * **Unsigned drivers were found**. You can ignore this one.
     * On the **Summary** page, you can select **Create the cluster now using the validated nodes** to continue on to create the cluster, rather than closing the wizard and reopening it.

     * In the Create Cluster Wizard, on the **Access point** page:

       * Name your cluster "testcluster".
       * In the **Address** field, enter the IP address that you reserved earlier, `10.0.0.8`.

[Microsoft instructions](https://docs.microsoft.com/en-us/windows-server/failover-clustering/create-failover-cluster)




### Add the cluster administrator

Adding a domain account as an administrator for the cluster enables you to perform actions on the cluster from tools such as Windows PowerShell. Add the `cluster-admin` domain account as a cluster admin.

  1. On the cluster node that hosts the cluster resources, in Failover Cluster Manager, select your cluster in the left pane and then click **Properties** in the right pane.
  2. Select the **Cluster Permissions** tab.
  3. Click **Add** and then add `cluster-admin`.
  4. With `cluster-admin` selected in the **Group or user names list** , select **Full Control** in the **Permissions** pane.
  5. Click **Apply** and **OK**.



This is a good point to take snapshots.

## Creating the file share witness

You have a two-node failover cluster, but the cluster uses a voting mechanism to decide which node should be active. To achieve a quorum, you can add a file share witness.

This tutorial simply adds a shared folder to the domain controller server. If this server were to go offline at the same time one of the cluster nodes is restarting, the entire cluster could stop working because the remaining server can't vote by itself. For this tutorial, the assumption is that the Google Cloud infrastructure features, such as [Live Migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process) and [automatic restart](https://docs.cloud.google.com/compute/docs/instances/setting-instance-scheduling-options#autorestart), provide enough reliability to keep the shared folder alive.

If you want to create a more-highly-available file share witness, you have these options:

  * Use a cluster of Windows Servers to provide the share by using [Storage Spaces Direct](https://docs.microsoft.com/en-us/windows-server/storage/storage-spaces/storage-spaces-direct-overview). This Windows Server 2016 feature can provide a highly available share for the quorum witness. For example, you could create a cluster for your Active Directory domain controller to provide both highly available domain services and provide the file share witness at the same time.
  * Use data replication software, such as SIOS Datakeeper, with Windows Failover Server Clustering for synchronous or asynchronous replication.



Follow these steps to create the file share for the witness:

  1. Connect to `wsfc-dc`. This server hosts the file share.
  2. In Explorer, browse to the `C` drive.
  3. In the title bar, click the **New Folder** button.
  4. Name the new folder `shares`.
  5. Double-click the `shares` folder to open it.
  6. Add a new folder and name it `clusterwitness-testcluster`.



### Configure sharing for the file share witness

You must set permissions on the file share witness folder to enable the cluster to use it.

  1. From Explorer, right-click the `clusterwitness-testcluster` folder and select **Properties**.
  2. On the **Sharing** tab, click **Advanced Sharing**.
  3. Select **Share this folder**.
  4. Click **Permissions** and then click **Add**.
  5. Click **Object Types** , select **Computers** , and then click **OK**.
  6. Add the machine account `testcluster$`.
  7. Give **Full Control** permissions to `testcluster$`.
  8. Click **Apply** and then close all the dialog boxes.



### Add the file share witness to the failover cluster

Now, configure the failover cluster to use the file share witness as a quorum vote.

  1. On the computer that hosts the cluster resources (`wsfc-1`), open the Failover Cluster Manager.
  2. In the left pane, right-click the name of the cluster (**testcluster.WSFC.TEST**) then point to **More Actions** , and then click **Configure Cluster Quorum Settings**.
  3. On the **Select Quorum Configuration Option** panel, choose **Select the quorum witness**.
  4. On the **Select Quorum Witness panel** , choose **Configure a file share witness**.
  5. For the **File Share Path** , enter the path to the shared folder, such as `\\wsfc-dc\clusterwitness-testcluster`.
  6. Confirm the settings and then click **Finish**.



## Testing the failover cluster

Your Windows Server failover cluster should now be working. You can test manually moving cluster resources between your instances. You're not done yet, but this is a good checkpoint to validate that everything you've done so far is working.

  1. On `wsfc-1`, note the name of the **Current Host Server** in Failover Cluster Manager.
  2. Run Windows PowerShell as `cluster-admin`.
  3. In PowerShell, run the following command to change the current host server:
         
         Move-ClusterGroup -Name "Cluster Group"
         




You should see the name of the current host server change to the other VM.

If this didn't work, review the previous steps and see if you missed anything. The most common issue is a missing firewall rule that is blocking access on the network. Refer to the Troubleshooting section for more issues to check.

Otherwise, you can now move on to setting up the internal load balancer, which is required in order to route network traffic to the current host server in the cluster.

This is a good time to take snapshots.

## Adding a role to the failover cluster

In Windows failover clustering, _roles_ host clustered workloads. You can use a role to specify in the cluster the IP address that your application uses. For this tutorial, you add a role for the test workload, which is the Internet Information Services (IIS) web server, and assign an IP address to the role.

### Reserve an IP address for the role in Compute Engine

To prevent IP addressing conflicts within your subnet in Compute Engine, reserve the IP address for the role.

  1. Open a terminal on a host VM or open Cloud Shell.

[Go to Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Reserve an IP address. For this tutorial, use `10.0.0.9`:
         
         gcloud compute addresses create load-balancer-ip --region [YOUR_REGION] --subnet wsfcnetsub1 --addresses 10.0.0.9

  3. To confirm the reservation of the IP address:
         
         gcloud compute addresses list




### Add the role

Follow these steps:

  1. In Failover Cluster Manager, in the **Actions** pane, select **Configure Role**.
  2. In the **Select Role** page, select **Other Server**.
  3. In the **Client Access Point** page, enter the name `IIS`.
  4. Set the address to `10.0.0.9`.
  5. Skip **Select Storage** and **Select Resource Types**.
  6. Confirm the settings and then click **Finish**.



![Confirmation dialog shows settings for role.](https://docs.cloud.google.com/static/compute/docs/tutorials/images/failover-clustering-add-role.png)

## Creating the internal load balancer

Create and configure the internal load balancer, which is required in order to route network traffic to the active cluster host node. You will use the Google Cloud console, because the user interface gives you a good view into how internal load balancing is organized.

You will also create a Compute Engine instance group for each zone in the cluster, which the load balancer uses to manage the cluster nodes.

### Create the instance groups

Create an instance group in each zone that contains a cluster node and then add each node to the instance group in its zone. Don't add the domain controller `wsfc-dc` to an instance group.

  1. Create an instance group for each zone in the cluster, replacing `[ZONE_1]` with the name of your first zone and `[ZONE_2]` with the name of your second:
         
         gcloud compute instance-groups unmanaged create wsfc-group-1 --zone=[ZONE_1]
         
         gcloud compute instance-groups unmanaged create wsfc-group-2 --zone=[ZONE_2]

  2. Add the server in each zone to the instance group for that zone:
         
         gcloud compute instance-groups unmanaged add-instances wsfc-group-1 --instances wsfc-1 --zone [ZONE_1]
         
         gcloud compute instance-groups unmanaged add-instances wsfc-group-2 --instances wsfc-2 --zone [ZONE_2]

  3. Confirm that your instance groups were created and that each group contains one instance:
         
         gcloud compute instance-groups unmanaged list
         
         NAME          ZONE           NETWORK  NETWORK_PROJECT   MANAGED  INSTANCES
           wsfc-group-1  us-central1-a  wsfcnet  exampleproject    No       1
           wsfc-group-2  us-central1-b  wsfcnet  exampleproject    No       1




### Create the load balancer

#### Start your configuration

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click **Create load balancer**.
  3. For **Type of load balancer** , select **Network Load Balancer (TCP/UDP/SSL)** and click **Next**.
  4. For **Proxy or passthrough** , select **Passthrough load balancer** and click **Next**.
  5. For **Public facing or internal** , select **Internal** and click **Next**.
  6. Click **Configure**.



#### Basic configuration

  1. For **Name** , enter "wsfc-lb".
  2. Select your current region.
  3. Select `wsfcnet` for **Network**.



#### Configure the backend

Recall that the Google Cloud internal load balancer uses a periodic health check to determine the active node. The health check pings the Compute Engine cluster host agent that is running on the active cluster node. The health check payload is the IP address of the application, which is represented by the clustered role. The agent responds with a value of 1 if the node is active or 0 if it is not.

  1. Click **Backend configuration**.
  2. Under **Backends** , add each instance group that you created by selecting its name and clicking **Done**.
  3. Create a health check.

     * For **Name** , enter "wsfc-hc".
     * Accept the default **Protocol** setting of **TCP** and change the **Port** to "59998" for cluster host agent responses.
     * For **Request** , enter "10.0.0.9".
     * For **Response** , enter "1".
     * For **Check interval** , enter "2".
     * For **Timeout** enter "1".
     * Click **Save and continue**.



#### Configure the frontend

The frontend configuration creates a forwarding rule that defines how the load balancer handles incoming requests. For this tutorial, to keep it simple, you will test the system by making requests between the VMs in the subnetwork.

In your production system, you probably want to open the system up to external traffic, such as Internet traffic. To do this, you can [create a bastion host](https://cloud.google.com/solutions/connecting-securely#bastion) that accepts external traffic and forwards it to your internal network. Using a bastion host is not covered in this tutorial.

  1. In the center pane, click **Frontend configuration**.
  2. For **Name** , enter "wsfc-lb-fe".
  3. Select your subnetwork (`wsfcnetsub1`).
  4. For **Internal IP** , select **load-balancer-ip (10.0.0.9)**. This is the same IP address that you set for the role.
  5. For **Ports** , enter "80".
  6. Click **Done**.



#### Review and finalize

  1. To see a summary of the internal load balancer settings, in the center pane, click **Review and finalize**. The summary appears in the right pane.
  2. Click **Create**. It takes a moment to create the load balancer.

![Google Cloud console shows final settings for internal load balancing.](https://docs.cloud.google.com/static/compute/docs/tutorials/images/failover-clustering-ilb-final.png)




### Create firewall rules for the health check

You might have noticed that the Google Cloud console notified you that the health-check system would require a firewall rule to enable the health checks to reach their targets. In this section, you set up the firewall rule.

**Note:** The documentation about [setting up an internal load balancer](https://docs.cloud.google.com/compute/docs/load-balancing/internal#configure-a-firewall-rule-to-allow-internal-load-balancing) instructs you to create a firewall rule for the load balancer itself. For this tutorial, this is not needed because you already created a rule that allows all traffic between nodes on the subnet, and the load balancer is operating within this CIDR range and using only allowed ports.

  1. In the Google Cloud console, go to the **Cloud Shell**.

[Go to Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Run the following command to create the firewall rule:
         
         gcloud compute firewall-rules create allow-health-check --network wsfcnet --source-ranges 130.211.0.0/22,35.191.0.0/16 --allow tcp:59998
         




### Open the Windows Firewall

On each cluster node, `wsfc-1` and `wsfc-2`, create a firewall rule in the Windows firewall to allow the load balancer to access each Windows system.

  1. Open the Windows Firewall with Advanced Security app.

  2. In the left navigation pane, select **Inbound Rules**.

  3. In the right navigation pane, select **New Rule**.

  4. On the **Rule Type** panel, select **Custom** as the rule type and click **Next**.

  5. On the **Program** panel, accept the default and click **Next**.

  6. On the **Protocol and Ports** panel:

     1. In the **Protocol type:** field, select **TCP**.
     2. In the **Local port:** field, select **Specific Ports** and enter `59998`.
  7. On the **Scope** panel, under **Which remote IP addresses does this rule apply to** :

     1. Select **These IP addresses:**.
     2. Add each of the following IP address to the **This IP address or subnet** field by clicking **Add** :

        * `130.211.0.0/22`
        * `35.191.0.0/16`
     3. Click **Next**.

  8. On the **Action** panel, accept **Allow the connection** and click **Next**.

  9. On the **Profile** panel, accept the defaults and click **Next**.

  10. Specify a name for the firewall rule and click **Finish**.




## Validating the load balancer

After your internal load balancer is running, you can inspect its status to validate that it can find a healthy instance, and then test failover again.

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/loadBalancers/list)

  2. Click the name of the load balancer (`wsfc-lb`).

In the **Backend** section of the summary, you should see the instance groups listed.

In the following image from the details page of the `wsfc-lb` load balancer, instance group `wsfc-group-1` contains the active node, as indicated by **1 / 1** in the **Healthy** column. Instance group `wsfc-group-2` contains the inactive node, as indicated by **0 / 1**.

![Load balancer status shows 1 / 1 healthy instances in instance group
wsfc-group-1, which indicates that it contains the active node.](https://docs.cloud.google.com/static/compute/docs/tutorials/images/failover-clustering-ilb-validation.png)

If both instance groups show **0 / 1** , the load balancer might still be syncing with the nodes. Sometimes, you need to do at least one failover action to get the load balancer to find the IP address.

  3. In Failover Cluster Manager, expand the cluster name and click on **Roles**. In the **Owner Node** column, note the server name for the **IIS** role.

  4. Start a failover by right-clicking the **IIS** role and selecting **Move** > **Best Possible Node**. This action moves the role to the other node, as shown in the **Owner Node** column.

![Owner Node field shown in failover cluster manager.](https://docs.cloud.google.com/static/compute/docs/tutorials/images/failover-clustering-owner-node-field.png)

  5. Wait until the **Status** shows **Running**.

  6. Return to the **Load balancer details** page, click **Refresh** , and verify that the **1 / 1** and **0 / 1** values in the **Healthy** column have switched instance groups.

![Load balancer status shows 1 healthy instance out of 2.](https://docs.cloud.google.com/static/compute/docs/tutorials/images/failover-clustering-ilb-status.png)


**Tip:** You can use the gcloud CLI to check which instance is healthy, where `[REGION]` is your region:
    
    
    gcloud compute backend-services get-health wsfc-lb --region=[REGION]

The output looks like the following:
    
    
    backend: https://compute.googleapis.com/compute/v1/projects/exampleproject/zones/us-central1-a/instanceGroups/wsfc-group-1
    status:
      healthStatus:
      - healthState: HEALTHY
        instance: https://compute.googleapis.com/compute/v1/projects/exampleproject/zones/us-central1-a/instances/wsfc-1
        ipAddress: 10.0.0.4
        port: 80
      kind: compute#backendServiceGroupHealth
    ---
    backend: https://compute.googleapis.com/compute/v1/projects/exampleproject/zones/us-central1-b/instanceGroups/wsfc-group-2
    status:
      healthStatus:
      - healthState: UNHEALTHY
        instance: https://compute.googleapis.com/compute/v1/projects/exampleproject/zones/us-central1-b/instances/wsfc-2
        ipAddress: 10.0.0.5
        port: 80
      kind: compute#backendServiceGroupHealth

## Installing your application

Now that you have a cluster, you can set up your application on each node and configure it for running in a clustered environment.

For this tutorial, you need to set up something that can demonstrate that the cluster is really working with the internal load balancer. Set up IIS on each VM to serve a simple web page.

You're not setting up IIS for HA in the cluster. You are creating separate IIS instances that each serve a different web page. After a failover, the web server serves its own content, not shared content.

Setting up your application or IIS for HA is beyond the scope of this tutorial.

### Set up IIS

  1. On each cluster node, [install IIS](https://docs.microsoft.com/en-us/iis/get-started/whats-new-in-iis-8/installing-iis-8-on-windows-server-2012).

     * On the **Select role services** page, be sure that **Default Document** is selected under **Common HTTP Features**.
     * On the **Confirmation** page, select the checkbox that enables automatic restarting of the destination server.
  2. Validate that each web server is working.

     1. Use RDP to connect to the VM named `wsfc-dc`.
     2. In Server Manager, click **Local Server** in the navigation pane on the left side of the window.
     3. in the **Properties** section at the top, turn off **IE Enhanced Security Configuration**.
     4. Open Internet Explorer.
     5. Browse to the IP address of each server:
            
            http://10.0.0.4/
            
            http://10.0.0.5/




In each case, you see the **Welcome** page, which is the default IIS web page.

### Edit the default web pages

Change each default web page so you can easily see which server is currently serving the page.

  1. Use RDP to connect to the VM named `wsfc-1`.
  2. Run Notepad as administrator.
  3. Open `C:\inetpub\wwwroot\iisstart.htm` in Notepad. Remember to browse for **All Files** , not just text files.
  4. In the `<title>` element, change the text to the name of the current server. For example:
         
         <title>wsfc-1</title>
         

  5. Save the HTML file.

  6. Repeat these steps for `wsfc-2`, setting the `<title>` element to `wsfc-2`.




Now, when you view a web page served from one of these servers, the name of the server appears as the title in the Internet Explorer tab.

### Test the failover

  1. Use RDP to connect to the VM named `wsfc-dc`.
  2. Open Internet Explorer.
  3. Browse to the IP address of the load balancer role:
         
         http://10.0.0.9/
         

You see the **Welcome** page with the name of the current server displayed in the tab title.

  4. Stop the current server to simulate a failure. In Cloud Shell, run the following command, replacing `[INSTANCE_NAME]` with the name of the current server you saw in the previous step, such as `wsfc-1`:
         
         gcloud compute instances stop [INSTANCE_NAME] --zone=[ACTIVE_ZONE]
         

  5. Switch to your RDP connection to `wsfc-dc`.

It can take a few moments for the load balancer to detect the move and reroute the traffic.

  6. After 30 seconds or so, refresh the page in Internet Explorer.

You should now see the name of the new active node displayed in the tab title. For example, if you started with `wsfc-1` active, you now see `wsfc-2` in the title. If you don't see the change right away or see a page-not-found error, refresh the browser again.




Congratulations! You now have a working Windows Server 2016 failover cluster running on Google Cloud.

## Troubleshooting

Here are some common issues you can check if things aren't working.

### Google Cloud firewall rules blocks health check

If the health check isn't working, double-check that you have a firewall rule to enable incoming traffic from the IP addresses that the health check system uses: `130.211.0.0/22`and `35.191.0.0/16`.

### Windows Firewall blocks health check

Make sure port 59998 is open in Windows Firewall on each cluster node. See Open the Windows Firewall.

### Cluster nodes using DHCP

It's important that each VM in the cluster has a static IP address. If a VM is configured to use DHCP in Windows, change the networking settings in Windows to make the IPv4 address match the IP address of the VM as shown in the Google Cloud console. Also set the gateway IP address to match the address of the subnetwork gateway in the Google Cloud VPC.

### Google Cloud network tags in firewall rules

If you use network tags in your firewall rules, be sure the correct tags are set on every VM instance. This tutorial doesn't use tags, but if you've set them for some other reason, they must be used consistently.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

After you finish the tutorial, you can clean up the resources that you created so that they stop using quota and incurring charges. The following sections describe how to delete or turn off these resources. 

### Deleting the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Cleaning up resources without deleting the project

If you need to keep your project, you can clean up the tutorial resources by deleting them individually.

#### Deleting instances

To delete a Compute Engine instance: 

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the checkbox for the instance that you want to delete. 
  3. To delete the instance, click more_vert **More actions** , click **Delete** , and then follow the instructions. 



#### Deleting instance groups

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups/list)

  2. Select the checkbox for the instance group that you want to delete. 
  3. To delete the instance group, click delete **Delete**. 



#### Deleting a load balancer

To delete a load balancer:

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing)

  2. Select the checkbox next to the name of the load balancer you want to delete.

  3. Click the **Delete** button at the top of the page.




#### Deleting a VPC network

To delete a VPC network:

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks)

  2. Click the name of the network you want to delete.

  3. Click the **DELETE VPC NETWORK** button at the top of the page.




#### Release reserved IP addresses

Use Cloud Shell to release the reserved IP addresses:

  1. In the Google Cloud console, go to the **Cloud Shell**.

[Go to Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Release the reserved IP addresses:
         
         gcloud compute addresses delete cluster-access-point load-balancer-ip




#### Deleting persistent disks

To delete a persistent disk:

  1. In the Google Cloud console, go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. Select the checkbox next to the name of the disk you want to delete.

  3. Click the **Delete** button at the top of the page.




## What's next

  * [Tutorials about Active Directory](https://docs.cloud.google.com/architecture?text=Active%20Directory).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
