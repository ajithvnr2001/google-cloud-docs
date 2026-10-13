---
url: https://docs.cloud.google.com/sap/docs/sap-maxdb-ha-config-rhel/
title: Manual HA cluster configuration guide for SAP MaxDB on RHEL \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:20.235343+00:00
---

# Manual HA cluster configuration guide for SAP MaxDB on RHEL  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/sap-maxdb-ha-config-rhel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Manual HA cluster configuration guide for SAP MaxDB on RHEL Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to deploy an SAP MaxDB system in a Red Hat Enterprise Linux (RHEL) high-availability cluster on Google Cloud, with active/passive cluster configuration.

To deploy a single-node SAP MaxDB system on Linux, contact [Customer Care](https://cloud.google.com/support).

This guide is intended for advanced SAP MaxDB users who are familiar with Linux HA configurations for SAP systems.

## The system that this guide deploys

This guide includes the steps for:

  * Configuring an [internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal/failover-overview) to reroute traffic in the event of a failure
  * Configuring a Pacemaker cluster on RHEL to manage the SAP systems and other resources during a failover



The deployed cluster includes the following functions and features:

  * Two Compute Engine VMs in different zones, able to run an instance of SAP MaxDB
  * A Regional Persistent Disk for the installation of SAP MaxDB.
  * The Pacemaker high-availability cluster resource manager.
  * A STONITH fencing mechanism.



A high-availability installation of SAP NetWeaver is not covered in this guide.

## Prerequisites

Before you create the SAP MaxDB high availability cluster, make sure that the following prerequisites are met:

  * You have read the [SAP MaxDB planning guide](https://docs.cloud.google.com/sap/docs/sap-maxdb-planning-guide).
  * You have a Red Hat subscription.
  * You or your organization has a Google Cloud account and you have created a project for the SAP MaxDB deployment.
  * If you require your SAP workload to run in compliance with data residency, access control, support personnel, or regulatory requirements, then you must create the required Assured Workloads folder. For more information, see [Compliance and sovereign controls for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/compliance-and-sovereign-controls). 

  * If [OS login](https://docs.cloud.google.com/compute/docs/instances/access-overview#oslogin) is enabled in your project metadata, then you need to disable OS login temporarily until your deployment is complete. For deployment purposes, this procedure configures SSH keys in instance metadata. When OS login is enabled, metadata-based SSH key configurations are disabled, and this deployment fails. After deployment is complete, you can enable OS login again.

For more information, see:

    * [Enabling or disabling OS Login](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access#enable_oslogin)
    * [Add SSH keys to VMs that use metadata-based SSH keys](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#metadata)

To avoid unintentionally exposing your VM instance to the internet, follow these recommendations: 

  * Use a NAT gateway.
  * [Create firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules) that block all external access that you don't require.
  * When you create your VMs: 
    * Specify a network tag for each VM for use in routing and firewall rules.
    * Create the VMs without an external IP.



## Creating a network

For security purposes, create a new network. You can control who has access by adding firewall rules or by using another access control method.

If your project has a default VPC network, then don't use it. Instead, create your own VPC network so that the only firewall rules in effect are those that you create explicitly.

During deployment, Compute Engine instances typically require access to the internet to download Google Cloud's Agent for SAP. If you are using one of the SAP-certified Linux images that are available from Google Cloud, then the compute instance also requires access to the internet in order to register the license and to access OS vendor repositories. A configuration with a NAT gateway and with VM network tags supports this access, even if the target compute instances don't have external IPs. 

To set up networking:

### Console

  1. In the Google Cloud console, go to the **VPC networks** page. 

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.
  3. Enter a **Name** for the network. 

The name must adhere to the [naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format). VPC networks use the Compute Engine naming convention. 

  4. For **Subnet creation mode** , choose **Custom**.
  5. In the **New subnet** section, specify the following configuration parameters for a subnet: 
     1. Enter a **Name** for the subnet.
     2. For **Region** , select the [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones) where you want to create the subnet.
     3. For **IP stack type** , select **IPv4 (single-stack)** and then enter an IP address range in the [CIDR format](https://wikipedia.org/wiki/Classless_Inter-Domain_Routing), such as `10.1.0.0/24`. 

This is the [primary IPv4 range](https://docs.cloud.google.com/vpc/docs/vpc#manually_created_subnet_ip_ranges) for the subnet. If you plan to add more than one subnet, then assign non-overlapping CIDR IP ranges for each subnetwork in the network. Note that each subnetwork and its internal IP ranges are mapped to a single region.

     4. Click **Done**. 
  6. To add more subnets, click **Add subnet** and repeat the preceding steps. You can add more subnets to the network after you have created the network.
  7. Click **Create**. 



### gcloud

  1. Go to Cloud Shell. 

[Go to Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. To create a new network in the custom subnetworks mode, run: 
         
         gcloud compute networks create NETWORK_NAME --subnet-mode custom

Replace `NETWORK_NAME` with the name of the new network. The name must adhere to the [naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format). VPC networks use the Compute Engine naming convention. 

Specify `--subnet-mode custom` to avoid using the default auto mode, which automatically creates a subnet in each Compute Engine region. For more information, see [Subnet creation mode](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges).

  3. Create a subnetwork, and specify the region and IP range: 
         
         gcloud compute networks subnets create SUBNETWORK_NAME \
             --network NETWORK_NAME --region REGION --range RANGE

Replace the following:

     * `SUBNETWORK_NAME`: the name of the new subnetwork
     * `NETWORK_NAME`: the name of the network you created in the previous step
     * `REGION`: the [region](https://docs.cloud.google.com/compute/docs/regions-zones) where you want the subnetwork 
     * `RANGE`: the IP address range, [specified in CIDR format](https://wikipedia.org/wiki/Classless_Inter-Domain_Routing), such as `10.1.0.0/24`

If you plan to add more than one subnetwork, assign non-overlapping CIDR IP ranges for each subnetwork in the network. Note that each subnetwork and its internal IP ranges are mapped to a single region.

  4. Optionally, repeat the previous step and add additional subnetworks.



## Setting up a NAT gateway

If you need to create one or more compute instances without public IP addresses, then you need to use network address translation (NAT) to enable the instances to access the internet. Use Cloud NAT, a Google Cloud distributed, software-defined managed service that lets the compute instances send outbound packets to the internet and receive any corresponding established inbound response packets. Alternatively, you can set up a separate compute instance as a NAT gateway.

**Key Point:** When you configure Cloud NAT, specify at least 160 as the minimum number of ports per compute instance. Certain operating system updates run concurrent processes that might exceed the Cloud NAT default for the number of ports, which can result in activation or download errors. 

When you create a Cloud NAT instance, specify the number of ports in the **Minimum ports per VM** field under **Advanced configurations** on the Create a NAT gateway page in the Google Cloud console.

To create a Cloud NAT instance for your project, see [Using Cloud NAT](https://docs.cloud.google.com/nat/docs/set-up-network-address-translation).

After you configure Cloud NAT for your project, your compute instances can securely access the internet without a public IP address.

## Adding firewall rules

By default, an _implied firewall rule_ blocks incoming connections from outside your Virtual Private Cloud (VPC) network. To allow incoming connections, set up a firewall rule for your VM. After an incoming connection is established with a VM, traffic is permitted in both directions over that connection.

You can also create a firewall rule to allow external access to specified ports, or to restrict access between VMs on the same network. If the `default` VPC network type is used, some additional default rules also apply, such as the `default-allow-internal` rule, which allows connectivity between VMs on the same network on all ports.

Depending on the IT policy that is applicable to your environment, you might need to isolate or otherwise restrict connectivity to your database host, which you can do by creating firewall rules.

Depending on your scenario, you can create firewall rules to allow access for:

  * The default SAP ports that are listed in [TCP/IP of All SAP Products](https://help.sap.com/viewer/575a9f0e56f34c6e8138439eefc32b16/2.0/en-US/616a3c0b1cc748238de9c0341b15c63c.html).
  * Connections from your computer or your corporate network environment to your Compute Engine instance. If you are unsure of what IP address to use, talk to your company's network administrator.

**Note:** The following procedure is a simplified version of the instructions for creating firewall rules. For more detailed instructions, see [Creating firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules).

To create a firewall rule, complete the following steps:

###  Console 

  1. In the Google Cloud console, go to the Compute Engine **Firewall** page.

[Go to Firewall](https://console.cloud.google.com/networking/firewalls/list)

  2. At the top of the page, click **Create firewall rule**.

     * In the **Network** field, select the network where your VM is located.
     * In the **Targets** field, specify the resources on Google Cloud that this rule applies to. For example, specify **All instances in the network**. Or to to limit the rule to specific instances on Google Cloud, enter tags in **Specified target tags**.
     * In the **Source filter** field, select one of the following: 
       * **IP ranges** to allow incoming traffic from specific IP addresses. Specify the range of IP addresses in the **Source IP ranges** field.
       * **Subnets** to allow incoming traffic from a particular subnetwork. Specify the subnetwork name in the following **Subnets** field. You can use this option to allow access between the VMs in a 3-tier or scaleout configuration.
     * In the **Protocols and ports** section, select **Specified protocols and ports** and enter `tcp:PORT_NUMBER`.
  3. Click **Create** to create your firewall rule.




###  gcloud 

Create a firewall rule by using the following command:
    
    
    $ [gcloud compute firewall-rules create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create) firewall-name
    --direction=INGRESS --priority=1000 \
    --network=network-name --action=ALLOW --rules=protocol:port \
    --source-ranges ip-range --target-tags=network-tags

## Deploying the VMs and installing MaxDB

Before you begin configuring the HA cluster, you define and deploy the VM instances and SAP MaxDB systems that serve as the primary and secondary nodes in your HA cluster.

### Create a VM for MaxDB deployment

As part of the HA deployment, two Google Cloud Compute Engine VMs will need to be created. You can refer to the guide [Create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

Note that Regional Persistent Disk only supports the use E2, N1, N2, and N2D machine types. See more details on the [Regional Persistent Disk guide](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#repd_limitations).

See [ SAP Note 2456432 - SAP Applications on Google Cloud: Supported Products and Google Cloud machine types](https://launchpad.support.sap.com/#/notes/2456432) to select the right machine type based on your sizing.

Create the two VMs in separate zones to achieve zonal resilience, with the following minimum requirements:

  1. VM details:

     * `Instance Name`
     * `Zone` \- Your preferred zone
     * `Machine Type` \- Based on sizing
     * `Subnet` \- Subnet name created for this region
  2. Service account with at least access scope to the following APIs:

     * https://www.googleapis.com/auth/compute
     * https://www.googleapis.com/auth/servicecontrol
     * https://www.googleapis.com/auth/service.management.readonly
     * https://www.googleapis.com/auth/logging.write
     * https://www.googleapis.com/auth/monitoring.write
     * https://www.googleapis.com/auth/trace.append
     * https://www.googleapis.com/auth/devstorage.read_write
  3. Additional disk on each VM with minimum of 20 GB to be used for `/usr/sap`




### Create a single regional disk for SAP MaxDB

For this deployment, one [regional disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) will be used to hold the MaxDB files within the `/sapdb` directory.

[Create](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk#repd_create_disk) the disk, making sure the replication zones for the regional disk match the zones in which you created the two VMs.

[Attach](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk#repd_add_disk) the regional disk to one of the VMs where you will perform the MaxDB installation, and configuration tasks.

### Prepare RHEL OS for SAP installation

SAP Product requires specific operating system settings and packages to be installed. Follow the guidelines in the following SAP notes:

  * [3562909 - Red Hat Enterprise Linux 10.x: Installation and Configuration](https://me.sap.com/notes/3562909)
  * [3108316 - Red Hat Enterprise Linux 9.x: Installation and Configuration](https://me.sap.com/notes/3108316)
  * [2772999 - Red Hat Enterprise Linux 8.x: Installation and Configuration](https://me.sap.com/notes/2772999)



This task must be performed on both nodes.

### Create filesystems

  1. Connect to both instances using SSH and create the `/usr/sap/SID` and `/sapdb` mount points.
         
         # sudo mkdir -p /usr/sap/SID
         # sudo mkdir -p /sapdb

  2. Create the filesystems in the two additional disks attached to the VMs using `mkfs`.

Note that at this time the regional disk will only be attached in one of the VMs, hence, the creation of the `/sapdb` file system will only be done once.

  3. Edit the `/etc/fstab` file to always mount `/usr/sap/SID` at reboot on both nodes.

  4. Manually mount the `/sapdb` file system into the node where you will perform the MaxDB installation.

For additional reference on creating and mounting the filesystems, see the guide [Format and mount a non-boot disk on a Linux VM](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-linux).




### Modify the LVM configuration

You need to modify the logical volume management (LVM) configuration so the shared volume group (VG) is always only attached and accessible by one node.

To do so, perform the following steps on both nodes:

  1. As root, edit the `/etc/lvm/lvm.conf` file and modify the `system_id_source` value to `uname` from `none`

  2. Check the results:
         
         # grep -i system_id_source /etc/lvm/lvm.conf

You should see a similar output to the following:
         
         # Configuration option global/system_id_source.
                 system_id_source = "uname"
         

  3. Additionally to prevent the VMs from activating cluster-managed VGs when a node reboots, maintain the following parameter in the`/etc/lvm/lvm.conf` configuration file with comma-separated full VG names that are not managed by the cluster.

**Note:** By default, there is no value maintained on this file, hence, you need to navigate to the section describing the usage of the parameter `auto_activation_volume_list` and manually add it.

For example, when `usrsap` is a VG name that is not managed by cluster:
         
         auto_activation_volume_list = [ usrsap ]

When there are no VGs that are not managed by cluster, for example, this parameter must be added with empty values:
         
         auto_activation_volume_list = [  ]




### Installing the database and the SAP host agent

Now that your operating system is configured, you can install your SAP MaxDB database and SAP Host Agent. MaxDB is typically installed with the SAP product that it is integrated with.

Note that the installation will only be performed once, in the one which you have attached the Regional Persistent Disk.

To install SAP MaxDB on your VM:

  1. Establish an SSH connection to your Linux-based VM.
  2. Download the SAP Software Provisioning Manager (SWPM), the SAP product installation media, and MaxDB installation Media according to SAP installation guides.
  3. Install your SAP product and SAP MaxDB database according to the SAP installation guides for your SAP product. For additional guidance, see the [SAP MaxDB documentation](https://help.sap.com/viewer/9d62a6d2a95149718db6b65b7ffa2052/113/en-US).



SAP provides additional installation information in [SAP Note 1020175 - FAQ: SAP MaxDB installation, upgrade or applying a patch](https://launchpad.support.sap.com/#/notes/0001020175).

Once the installation is completed, execute the following validations:

  1. As sidadm user, check the status of MaxDB.
         
         # dbmcli -d  SID -u control,password db_state

You should see output similar to the following example:
         
         >dbmcli -d  MDB -u control, my_p4$$w0rd db_state
         OK
         State
         ONLINE
         

  2. Check as well the status of `x_server`:
         
         # x_server

You should see output similar to the following example:
         
         >x_server
         2024-10-23 19:01:43 11968 19744 INF  12916          Found running XServer on port 7200
         2024-10-23 19:01:43 11968 19744 INF  13011            version 'U64/LIX86 7.9.10   Build 004-123-265-969'
         2024-10-23 19:01:43 11968 19744 INF  13010            installation MDB  - path: /sapdb/MDB/db
         2024-10-23 19:01:45 11971 13344 INF  12916          Found running sdbgloballistener on port 7210
         2024-10-23 19:01:45 11971 13344 INF  13011            version 'U64/LIX86 7.9.10   Build 004-123-265-969'
         

  3. Check if SAP Host agent is running:
         
         # ps -ef | grep -i hostctrl

You should see output similar to the following example:
         
         >ps -ef | grep -i hostctrl
         root      1543     1  0 Oct18 ?        00:00:15 /usr/sap/hostctrl/exe/saphostexec pf=/usr/sap/hostctrl/exe/host_profile
         sapadm    1550     1  0 Oct18 ?        00:03:00 /usr/sap/hostctrl/exe/sapstartsrv pf=/usr/sap/hostctrl/exe/host_profile -D
         root      1618     1  0 Oct18 ?        00:03:48 /usr/sap/hostctrl/exe/saposcol -l -w60 pf=/usr/sap/hostctrl/exe/host_profile
         mdbadm   12751 11261  0 19:03 pts/0    00:00:00 grep --color=auto -i hostctrl
         

  4. Once the Installation is verified, stop MaxDB instance and x_server.
         
         # dbmcli -d SID -u control, and password db_offline
         # x_server stop
         




### Performing post-installation tasks

Before using your SAP MaxDB instance, we recommend that you perform the following post-deployment steps:

  1. Update your SAP MaxDB software with the latest patches, if available.
  2. Install any additional components.
  3. Configure and back up your new SAP MaxDB database.



For more information, see [SAP MaxDB Database Administration](https://help.sap.com/viewer/2c2effc99b6746019aeb1af52ad59f5d/113/en-US/1a32c42a0fcf40b5b95ff7040a60aa41.html).

After the SAP MaxDB systems have deployed successfully, you define and configure the HA cluster.

## Configure the Cloud Load Balancing failover support

The internal passthrough Network Load Balancer service with failover support routes traffic to the active host in an SAP MaxDB cluster based on a health check service.

### Reserve an IP address for the virtual IP

The virtual IP (VIP) address , which is sometimes referred to as a _floating_ IP address, follows the active SAP MaxDB system. The load balancer routes traffic that is sent to the VIP to the VM that is hosting the active SAP MaxDB system.

  1. Open Cloud Shell:

[Go to Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Reserve an IP address for the virtual IP. This is the IP address that applications use to access SAP MaxDB. If you omit the `--addresses` flag, an IP address in the specified subnet is chosen for you:
         
         $ [gcloud compute addresses create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create) VIP_NAME \
           --region CLUSTER_REGION --subnet CLUSTER_SUBNET \
           --addresses VIP_ADDRESS

For more information about reserving a static IP, see [Reserving a static internal IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address).

  3. Confirm IP address reservation:
         
         $ [gcloud compute addresses describe](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/describe) VIP_NAME \
           --region CLUSTER_REGION

You should see output similar to the following example:
         
         address: 10.0.0.19
         addressType: INTERNAL
         creationTimestamp: '2024-10-23T14:19:03.109-07:00'
         description: ''
         id: '8961491304398200872'
         kind: compute#address
         name: vip-for-maxdb-ha
         networkTier: PREMIUM
         purpose: GCE_ENDPOINT
         region: https://www.googleapis.com/compute/v1/projects/example-project-123456/regions/us-central1
         selfLink: https://www.googleapis.com/compute/v1/projects/example-project-123456/regions/us-central1/addresses/vip-for-maxdb-ha
         status: RESERVED
         subnetwork: https://www.googleapis.com/compute/v1/projects/example-project-123456/regions/us-central1/subnetworks/example-subnet-us-central1




### Create instance groups for your host VMs

  1. In Cloud Shell, create two unmanaged instance groups and assign the primary host VM to one and the secondary host VM to the other:
         
         $ [gcloud compute instance-groups unmanaged create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/create) PRIMARY_IG_NAME \
           --zone=PRIMARY_ZONE
         $ [gcloud compute instance-groups unmanaged add-instances](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/add-instances) PRIMARY_IG_NAME \
           --zone=PRIMARY_ZONE \
           --instances=PRIMARY_HOST_NAME
         $ [gcloud compute instance-groups unmanaged create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/create) SECONDARY_IG_NAME \
           --zone=SECONDARY_ZONE
         $ [gcloud compute instance-groups unmanaged add-instances](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/add-instances) SECONDARY_IG_NAME \
           --zone=SECONDARY_ZONE \
           --instances=SECONDARY_HOST_NAME
         

  2. Confirm the creation of the instance groups:
         
         $ [gcloud compute instance-groups unmanaged list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/list)

You should see output similar to the following example:
         
         NAME          ZONE           NETWORK          NETWORK_PROJECT        MANAGED  INSTANCES
         maxdb-ha-ig-1  us-central1-a  example-network  example-project-123456 No       1
         maxdb-ha-ig-2  us-central1-c  example-network  example-project-123456 No       1




### Create a Compute Engine health check

  1. In Cloud Shell, create the health check. For the port used by the health check, choose a port that is in the private range, 49152-65535, to avoid clashing with other services. The check-interval and timeout values are slightly longer than the defaults so as to increase failover tolerance during Compute Engine live migration events. You can adjust the values, if necessary:
         
         $ [gcloud compute health-checks create tcp](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/tcp) HEALTH_CHECK_NAME --port=HEALTHCHECK_PORT_NUM \
           --proxy-header=NONE --check-interval=10 --timeout=10 --unhealthy-threshold=2 \
           --healthy-threshold=2

  2. Confirm the creation of the health check:
         
         $ [gcloud compute health-checks describe HEALTH_CHECK_NAME](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-checks/describe)

You should see output similar to the following example:
         
         checkIntervalSec: 10
         creationTimestamp: '2023-10-23T21:03:06.924-07:00'
         healthyThreshold: 2
         id: '4963070308818371477'
         kind: compute#healthCheck
         name: maxdb-health-check
         selfLink: https://www.googleapis.com/compute/v1/projects/example-project-123456/global/healthChecks/maxdb-health-check
         tcpHealthCheck:
          port: 60000
          portSpecification: USE_FIXED_PORT
          proxyHeader: NONE
         timeoutSec: 10
         type: TCP
         unhealthyThreshold: 2




### Create a firewall rule for the health checks

Define a firewall rule for a port in the private range that allows access to your host VMs from the IP ranges that are used by Compute Engine health checks, `35.191.0.0/16` and `130.211.0.0/22`. For more information, see [Creating firewall rules for health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks#fw-rule).

  1. If you don't already have one, add a network tag to your host VMs. This network tag is used by the firewall rule for health checks.
         
         $ [gcloud compute instances add-tags](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-tags) PRIMARY_HOST_NAME \
           --tags NETWORK_TAGS \
           --zone PRIMARY_ZONE
         $ [gcloud compute instances add-tags](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-tags) SECONDARY_HOST_NAME \
           --tags NETWORK_TAGS \
           --zone SECONDARY_ZONE
         

  2. If you don't already have one, create a firewall rule to allow the health checks:
         
         $ [gcloud compute firewall-rules create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create) RULE_NAME \
           --network NETWORK_NAME \
           --action ALLOW \
           --direction INGRESS \
           --source-ranges 35.191.0.0/16,130.211.0.0/22 \
           --target-tags NETWORK_TAGS \
           --rules tcp:HLTH_CHK_PORT_NUM

For example:
         
         gcloud compute firewall-rules create  fw-allow-health-checks \
         --network example-network \
         --action ALLOW \
         --direction INGRESS \
         --source-ranges 35.191.0.0/16,130.211.0.0/22 \
         --target-tags cluster-ntwk-tag \
         --rules tcp:60000




### Configure the load balancer and failover group

  1. Create the load balancer backend service:
         
         $ [gcloud compute backend-services create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create) BACKEND_SERVICE_NAME \
           --load-balancing-scheme internal \
           --health-checks HEALTH_CHECK_NAME \
           --no-connection-drain-on-failover \
           --drop-traffic-if-unhealthy \
           --failover-ratio 1.0 \
           --region CLUSTER_REGION \
           --global-health-checks

  2. Add the primary instance group to the backend service:
         
         $ [gcloud compute backend-services add-backend](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-backend) BACKEND_SERVICE_NAME \
           --instance-group PRIMARY_IG_NAME \
           --instance-group-zone PRIMARY_ZONE \
           --region CLUSTER_REGION

  3. Add the secondary, failover instance group to the backend service:
         
         $ [gcloud compute backend-services add-backend](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-backend) BACKEND_SERVICE_NAME \
           --instance-group SECONDARY_IG_NAME \
           --instance-group-zone SECONDARY_ZONE \
           --failover \
           --region CLUSTER_REGION

  4. Create a forwarding rule. For the IP address, specify the IP address that you reserved for the VIP. If you need to access the SAP MaxDB system from outside of the region that is specified below, include the flag `--allow-global-access` in the definition:
         
         $ [gcloud compute forwarding-rules create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create) RULE_NAME \
           --load-balancing-scheme internal \
           --address VIP_ADDRESS \
           --subnet CLUSTER_SUBNET \
           --region CLUSTER_REGION \
           --backend-service BACKEND_SERVICE_NAME \
           --ports ALL

For more information about cross-region access to your SAP MaxDB high-availability system, see [Internal TCP/UDP Load Balancing](https://docs.cloud.google.com/load-balancing/docs/internal#client-access).


**Note:** Your backend instance groups won't register as healthy until you have completed the Pacemaker cluster configuration.

### Test the load balancer configuration

Even though your backend instance groups won't register as healthy until later, you can test the load balancer configuration by setting up a listener to respond to the health checks. After setting up a listener, if the load balancer is configured correctly, the status of the backend instance groups changes to healthy.

The following sections present different methods that you can use to test the configuration.

#### Testing the load balancer with the `socat` utility

You can use the `socat` utility to temporarily listen on the health check port. 

  1. On both host VMs, install the `socat` utility:
         
         $ sudo yum install -y socat

  2. Start a `socat` process to listen for 60 seconds on the health check port:
         
         $ sudo timeout 60s socat - TCP-LISTEN:HLTH_CHK_PORT_NUM,fork

  3. In Cloud Shell, after waiting a few seconds for the health check to detect the listener, check the health of your backend instance groups:
         
         $ [gcloud compute backend-services get-health](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/get-health) BACKEND_SERVICE_NAME \
           --region CLUSTER_REGION

You should see output similar to the following:
         
         ---
         backend: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-a/instanceGroups/maxdb-ha-ig-1
         status:
          healthStatus:
          ‐ healthState: HEALTHY
            instance: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-a/instances/maxdb-ha-vm-1
            ipAddress: 10.0.0.35
            port: 80
          kind: compute#backendServiceGroupHealth
         ---
         backend: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-c/instanceGroups/maxdb-ha-ig-2
         status:
          healthStatus:
          ‐ healthState: HEALTHY
            instance: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-c/instances/maxdb-ha-vm-2
            ipAddress: 10.0.0.34
            port: 80
          kind: compute#backendServiceGroupHealth




#### Testing the load balancer using port 22

If port 22 is open for SSH connections on your host VMs, you can temporarily edit the health checker to use port 22, which has a listener that can respond to the health checker.

To temporarily use port 22, follow these steps:

  1. Click your health check in the console:

[Go to Health checks page](https://console.cloud.google.com/compute/healthChecks)

  2. Click **Edit**.

  3. In the **Port** field, change the port number to 22.

  4. Click **Save** and wait a minute or two.

  5. In Cloud Shell, check the health of your backend instance groups:
         
         $ [gcloud compute backend-services get-health](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/get-health) BACKEND_SERVICE_NAME \
           --region CLUSTER_REGION

You should see output similar to the following:
         
         ---
         backend: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-a/instanceGroups/maxdb-ha-ig-1
         status:
          healthStatus:
          ‐ healthState: HEALTHY
            instance: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-a/instances/maxdb-ha-vm-1
            ipAddress: 10.0.0.35
            port: 80
          kind: compute#backendServiceGroupHealth
         ---
         backend: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-c/instanceGroups/maxdb-ha-ig-2
         status:
          healthStatus:
          ‐ healthState: HEALTHY
            instance: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-c/instances/maxdb-ha-vm-2
            ipAddress: 10.0.0.34
            port: 80
          kind: compute#backendServiceGroupHealth

  6. When you are done, change the health check port number back to the original port number.




## Set up Pacemaker

The following procedure configures the Red Hat implementation of a Pacemaker cluster on Compute Engine VMs for SAP MaxDB.

The procedure is based on Red Hat documentation for configuring high-availability clusters, including:

  * [Installing and Configuring a Red Hat Enterprise Linux 7.6 (and later) High-Availability Cluster on Google Cloud](https://access.redhat.com/articles/3479821)



### Install the cluster agents on both nodes

Complete the following steps on both nodes.

  1. As root, install the Pacemaker components:
         
         # yum -y install pcs pacemaker fence-agents-gce resource-agents-gcp resource-agents-sap-hana
         # yum update -y

If you are using a Google-provided RHEL-for-SAP image, these packages are already installed, but some updates might be required.

  2. Set the password for the `hacluster` user, which is installed as part of the packages:
         
         # passwd hacluster

  3. Specify a password for `hacluster` at the prompts.

  4. In the RHEL images provided by Google Cloud, the OS firewall service is active by default. Configure the firewall service to allow high-availability traffic:
         
         # firewall-cmd --permanent --add-service=high-availability
         
         # firewall-cmd --reload

  5. Start the pcs service and configure it to start at boot time:
         
         # systemctl start pcsd.service
         # systemctl enable pcsd.service

  6. Check the status of the pcs service:
         
         # systemctl status pcsd.service

You should see output similar to the following:
         
         ● pcsd.service - PCS GUI and remote configuration interface
           Loaded: loaded (/usr/lib/systemd/system/pcsd.service; enabled; vendor preset: disabled)
           Active: active (running) since Sat 2023-10-23 21:17:05 UTC; 25s ago
             Docs: man:pcsd(8)
                   man:pcs(8)
         Main PID: 31627 (pcsd)
           CGroup: /system.slice/pcsd.service
                   └─31627 /usr/bin/ruby /usr/lib/pcsd/pcsd
         Oct 23 21:17:03 maxdb-ha-vm-1 systemd[1]: Starting PCS GUI and remote configuration interface...
         Oct 23 21:17:05 maxdb-ha-vm-1 systemd[1]: Started PCS GUI and remote configuration interface.

  7. Ensure all the required HA services are enabled and up and running on both nodes.
         
         # systemctl enable pcsd.service pacemaker.service corosync.service

  8. In the `/etc/hosts` file, add the full hostname and the internal IP addresses of both hosts in the cluster. For example:
         
         127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
         ::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
         **10.0.0.40 maxdb-ha-vm-1.us-central1-a.c.example-project-123456.internal maxdb-ha-vm-1**  # Added by Google
         **10.0.0.41 maxdb-ha-vm-2.us-central1-c.c.example-project-123456.internal maxdb-ha-vm-2**
         169.254.169.254 metadata.google.internal  # Added by Google

For more information from Red Hat about setting up the `/etc/hosts` file on RHEL cluster nodes, see <https://access.redhat.com/solutions/81123>.




### Create the cluster

  1. As root on either node, authorize the `hacluster` user. Click the tab for your RHEL version to see the command:

### RHEL 8 and later
         
         # pcs host auth primary-host-name secondary-host-name

### RHEL 7
         
         # pcs cluster auth primary-host-name secondary-host-name

  2. At the prompts, enter the `hacluster` username and the password that you set for the `hacluster` user.

  3. Create the cluster:

### RHEL 8 and later
         
         # pcs cluster setup cluster-name primary-host-name secondary-host-name

### RHEL 7
         
         # pcs cluster setup --name cluster-name primary-host-name secondary-host-name




### Edit the corosync.conf default settings

Edit the `/etc/corosync/corosync.conf` file on the primary host to set a more appropriate starting point for testing the fault tolerance of your HA cluster on Google Cloud.

  1. On either host, use your preferred text editor to open the `/etc/corosync/corosync.conf` file for editing:
         
         # /etc/corosync/corosync.conf

  2. If `/etc/corosync/corosync.conf` is a new file or is empty, you can check the `/etc/corosync/` directory for an example file to use as the base for the corosync file.

  3. In the `totem` section of the corosync.conf file, add the following properties with the suggested values as shown for your RHEL version:

### RHEL 8 and later

     * `transport: knet`
     * `token: 20000`
     * `token_retransmits_before_loss_const: 10`
     * `join: 60`
     * `max_messages: 20`

For example:
    
    totem {
    version: 2
    cluster_name: hacluster
    secauth: off
    **transport: knet**
    **token: 20000**
    **token_retransmits_before_loss_const: 10**
    **join: 60**
    **max_messages: 20**
    }
    ...

### RHEL 7

     * `transport: udpu`
     * `token: 20000`
     * `token_retransmits_before_loss_const: 10`
     * `join: 60`
     * `max_messages: 20`

For example:
    
    totem {
    version: 2
    cluster_name: hacluster
    secauth: off
    **transport: udpu**
    **token: 20000**
    **token_retransmits_before_loss_const: 10**
    **join: 60**
    **max_messages: 20**
    }
    ...

  4. From the host that contains the edited `corosync.conf` file, sync the corosync configuration across the cluster:

### RHEL 8 and later
         
         # pcs cluster sync corosync

### RHEL 7
         
         # pcs cluster sync

  5. Set the cluster to start automatically:
         
         # pcs cluster enable --all
         
         # pcs cluster start --all

  6. Confirm that the new corosync settings are active in the cluster by using the corosync-cmapctl utility:
         
         # corosync-cmapctl




### Set up fencing

RHEL images that are provided by Google Cloud include a `fence_gce` fencing agent that is specific to Google Cloud. You use `fence_gce` to create fence devices for each host VM.

To ensure the correct sequence of events after a fencing action, you configure the operating system to delay the restart of Corosync after a VM is fenced. You also adjust the Pacemaker timeout for reboots to account for the delay.

To see all of the options that are available with the `fence_gce` fencing agent, issue `fence_gce -h`.

**Note:** If you have changed the host names so that they are no longer the same as the VM instance names, see [Installing and Configuring a Red Hat Enterprise Linux 7.6 (and later) High-Availability Cluster on Google Compute Cloud](https://access.redhat.com/articles/3479821). The following steps require the host names and VM instance names to be the same.

#### Create the fencing device resources

  1. On the primary host as root:

     1. Create a fencing device for each host VM:
            
            # pcs stonith create primary-fence-name fence_gce \
              port=primary-host-name \
              zone=primary-host-zone \
              project=project-id \
              pcmk_reboot_timeout=300 pcmk_monitor_retries=4 pcmk_delay_max=30 \
              op monitor interval="300s" timeout="120s" \
              op start interval="0" timeout="60s"
            # pcs stonith create secondary-fence-name fence_gce \
              port=secondary-host-name \
              zone=secondary-host-zone \
              project=project-id \
              pcmk_reboot_timeout=300 pcmk_monitor_retries=4 \
              op monitor interval="300s" timeout="120s" \
              op start interval="0" timeout="60s"

     2. Constrain each fence device to the other host VM:
            
            # pcs constraint location primary-fence-name avoids primary-host-name
            # pcs constraint location secondary-fence-name avoids secondary-host-name

  2. On the primary host as root, test the secondary fence device:

     1. Shut down the secondary host VM:
            
            # fence_gce -o off -n secondary-host-name --zone=secondary-host-zone

If the command is successful, you lose connectivity to the secondary host VM and it appears stopped on the [**VM instances** page](https://console.cloud.google.com/compute/instances) in the Google Cloud console. You might need to refresh the page.

     2. Restart the secondary host VM:
            
            # fence_gce -o on -n secondary-host-name --zone=secondary-host-zone

  3. On the secondary host as root, test the primary fence device by repeating the preceding steps using the values for the primary host in the commands.

  4. On either host as root, check the status of the cluster:
         
         # pcs status

The fence resources appear in the resources section of the cluster status, similar to the following example:
         
         [root@maxdb-ha-vm-2 ~]# pcs status
         Cluster name: maxdb-ha-cluster
         Stack: corosync
         Current DC: maxdb-ha-vm-1 (version 1.1.19-8.el7_6.5-c3c624ea3d) - partition with quorum
         Last updated: Mon Jun 15 17:19:07 2020
         Last change: Mon Jun 15 17:18:33 2020 by root via cibadmin on maxdb-ha-vm-1
         
         2 nodes configured
         2 resources configured
         
         Online: [ maxdb-ha-vm-1 maxdb-ha-vm-2 ]
         
         Full list of resources:
         
          STONITH-maxdb-ha-vm-1   (stonith:fence_gce):    Started maxdb-ha-vm-2
          STONITH-maxdb-ha-vm-2   (stonith:fence_gce):    Started maxdb-ha-vm-1
         
         Daemon Status:
           corosync: active/enabled
           pacemaker: active/enabled
           pcsd: active/enabled




#### Set a delay for the restart of Corosync

  1. On both hosts as root, create a `systemd` drop-in file that delays the startup of Corosync to ensure the proper sequence of events after a fenced VM is rebooted:
         
         systemctl edit corosync.service

  2. Add the following lines to the file:
         
         [Service]
         ExecStartPre=/bin/sleep 60

  3. Save the file and exit the editor.

  4. Reload the systemd manager configuration.
         
         systemctl daemon-reload

  5. Confirm the drop-in file was created:
         
         service corosync status

You should see a line for the drop-in file, as shown in the following example:
         
         ● corosync.service - Corosync Cluster Engine
            Loaded: loaded (/usr/lib/systemd/system/corosync.service; disabled; vendor preset: disabled)
           **Drop-In: /etc/systemd/system/corosync.service.d
                    └─override.conf**
            Active: active (running) since Tue 2021-07-20 23:45:52 UTC; 2 days ago




## Install listeners and create a health check resource

To configure a health check resource, you need to install the listeners first.

### Install a listener

The load balancer uses a listener on the health-check port of each host to determine where the MaxDB instance is running.

  1. As root on the both hosts, install a TCP listener. These instructions install and use HAProxy as the listener.
         
         # yum install haproxy

  2. Open the configuration file `haproxy.cfg` for editing:
         
         # vi /etc/haproxy/haproxy.cfg

     1. In the **defaults** section of the `haproxy.cfg`, change the `mode` to `tcplog`.

     2. After the **defaults** section, create a new section by adding:
            
            #---------------------------------------------------------------------
            # Health check listener port for SAP MaxDB HA cluster
            #---------------------------------------------------------------------
            listen healthcheck
              bind *:healthcheck-port-num

The bind port is the same port that you used when you created the health check.

When you are done, your updates should look similar to the following example:
            
            #---------------------------------------------------------------------
            # common defaults that all the 'listen' and 'backend' sections will
            # use if not designated in their block
            #---------------------------------------------------------------------
            defaults
              **mode                    tcp**
              log                     global
              **option                  tcplog**
              option                  dontlognull
              option http-server-close
              # option forwardfor       except 127.0.0.0/8
              option                  redispatch
              retries                 3
              timeout http-request    10s
              timeout queue           1m
              timeout connect         10s
              timeout client          1m
              timeout server          1m
              timeout http-keep-alive 10s
              timeout check           10s
              maxconn                 3000
            
            **#---------------------------------------------------------------------
            # Set up health check listener for SAP MaxDB HA cluster
            #---------------------------------------------------------------------
            listen healthcheck
             bind *:60000**

  3. On each host as root, start the service to confirm it is correctly configured:
         
         # systemctl start haproxy.service

  4. On the Load balancer page in the Google Cloud console, click your load balancer entry:

[Load balancing page](https://console.cloud.google.com/net-services/loadbalancing/loadBalancers/list)

In the **Backend** section on the **Load balancer details** page, if the HAProxy service is active on both hosts, you see `1/1` in the **Healthy** column of each instance group entry.

  5. On each host, stop the HAProxy service:
         
         # systemctl stop haproxy.service

After you stop the HAProxy service on each host, `0/1` displays in the **Healthy** column of each instance group.

Later, when the health check is configured, the cluster restarts the listener on the active node.




### Create the health check resource

  1. On either host as root, create a health check resource for the HAProxy service:
         
         # pcs resource create healthcheck_resource_name service:haproxy op monitor interval=10s timeout=20s —-group SAPMaxDB_Group

  2. Confirm that the health check service is active on the same host as your SAP MaxDB instance:
         
         # pcs status

If the health check resource is not on the same host were the MaxDB is, move it with the following command:
         
         # pcs resource move healthcheck_resource_name target_host_name
         # pcs resource clear healthcheck_resource_name

The command `pcs resource clear` leaves the resource at its new location but removes the unwanted location constraint that the `pcs resource move` command created.

In the status, the resources section should look similar to the following example:
         
         Full list of resources:
         
         STONITH-maxdb-ha-vm-1   (stonith:fence_gce):    Started maxdb-ha-vm-2
         STONITH-maxdb-ha-vm-2   (stonith:fence_gce):    Started maxdb-ha-vm-1
         
         Resource Group: SAPMaxDB_Group
           rsc_healthcheck_MDB    (service:haproxy):      Started maxdb-ha-vm-1




## Set the cluster defaults

Set up migration thresholds and stickiness to determine the number of failovers to attempt before failure and to set the system to try restarting on the current host first. This only needs to be set on one node to apply to the cluster.

  1. As root on either host, set the resource defaults:
         
         # pcs resource defaults resource-stickiness=1000
         # pcs resource defaults migration-threshold=5000

The property `resource-stickiness` controls how likely a service is to stay running where it is. Higher values make the service more sticky. A value of `1000` means that the service is very sticky.

The property `migration-threshold` specifies the number of failures that must occur before a service fails over to another host. A value of 5000 is high enough to prevent failover for shorter-lived error situations.

You can check the resource defaults by entering `pcs resource defaults`.

  2. Set the resource operation timeout defaults:
         
         # pcs resource op defaults timeout=600s

You can check the resource op defaults by entering `pcs resource op defaults`.

  3. Set the following cluster properties:
         
         # pcs property set stonith-enabled="true"
         # pcs property set stonith-timeout="300s"
         

You can check your property settings with `pcs property list`.




## Create MaxDB resources in the cluster

Before performing these steps, make sure MaxDB and `x_server` is stopped and `/sapdb` file system is unmounted.

### Create gcp-pd-move resource

The `gcp-pd-move` resource is a resource agent that is used to move the persistent disk from one node to another during a cluster failover.

  1. Create the resource using the following command as root on either node:
         
         # pcs resource create pd_move_resource_name gcp-pd-move \
           disk_name=regional_pd_name mode="READ_WRITE" disk_scope=regional \
           op monitor interval=10s timeout=15s \
           op start interval=0s timeout=300s \
           op stop interval=0s timeout=15s \
           --group SAPMaxDB_Group




### Create LVM resource

An LVM-activated resource agent is used to activate the LVM after the disk is moved to the other node. 

  1. Create the LVM resource using the following command as root on either node:
         
         # pcs resource create lvm_resource_name LVM-activate \
           vgname=vgname_for_maxdb \
           vg_access_mode=system_id activation_mode=exclusive \
           --group SAPMaxDB_Group

For example:
         
         # pcs resource create sapdb_lvm LVM-activate \
           vgname=sapdb vg_access_mode=system_id \
           activation_mode=exclusive \
           --group SAPMaxDB_Group




### Create the file system resource

File system resource is used in the cluster to unmount `/sapdb` and mount it on another node during the failover operation.

  1. Create the file system resource using the following command as root on either node:
         
         # pcs resource create fs_resource_name Filesystem \
           device=filesystem directory=/sapdb fstype=fs_type \
           --group SAPMaxDB_Group

For example:
         
         # pcs resource create sapdb_FS Filesystem \
           device=/dev/mapper/sapdb-sapdblv directory=/sapdb fstype=ext4 \
           --group SAPMaxDB_Group




### Preparations for MaxDB resource group

To enable the MaxDB resource group, you need to perform the following steps.

  1. Sync users and groups from the node on which you have performed the MaxDB installation to the other node.

     1. The SAP MaxDB users must be synced between nodes by copying the entries in `/etc/passwd`, for example:
            
            sdb:x:1002:1003:MaxDB User:/home/sdb:/bin/false
             madbadm:x:1003:1005:SAP System Administrator:/home/mdbadm:/bin/csh

     2. Similarly, the SAP groups must be synced as well by copying the entries in `/etc/group` from one node to the other, for example:
            
            dba:x:1003:mdbadm
             sapsys:x:1005:

  2. Sync MaxDB specific files that get stored under the operating system directories. As root user, execute the following commands:
         
         # rsync -av /etc/services target_host:/etc/services
         # rsync -av /home/* target_host:/home
         # rsync -av --exclude=sapservices /usr/sap/* target_host:/usr/sap
         # rsync -av --ignore-existing /usr/sap/sapservicestarget_host:/usr/sap/sapservices
         # rsync -av /etc/init.d/sapinittarget_host:/etc/init.d/
         
         # MaxDB specific files
         # rsync -av /etc/opttarget_host:/etc
         # rsync -av /var/lib/sdbtarget_host:/var/lib

  3. For the SAP OS users on the second node, rename the following environment files to use its respective hostname in their home directories, for example:
         
         mv .sapenv_maxdb-ha-vm-1.sh .sapenv_maxdb-ha-vm-2.sh
         mv .sapenv_maxdb-ha-vm-1.csh .sapenv_maxdb-ha-vm-2.csh
         mv .sapsrc_maxdb-ha-vm-1.sh  .sapsrc_maxdb-ha-vm-2.sh
         mv .sapsrc_maxdb-ha-vm-1.csh  .sapsrc_maxdb-ha-vm-2.csh
         mv .dbenv_maxdb-ha-vm-1.sh .sapenv_maxdb-ha-vm-2.sh
         mv .dbenv_maxdb-ha-vm-1.csh .dbenv_maxdb-ha-vm-2.csh




The `SAPDatabase` resource agent does not use any DB specific commands to stop or start the database but relies upon `saphostctrl` commands to perform the same. SAP Host Agent requires `xuser` entries to be created for successful monitoring and control of MAXDB using saphostctrl. See [SAP Note 2435938 - SAP Host Agent SAP MaxDB: DBCredentials for DB connect](https://me.sap.com/notes/2435938/E) for more information.

  1. As root, execute the following command to `SetDatabaseProperty` on the active node:
         
         /usr/sap/hostctrl/exe/saphostctrl -host primary-host-name -user sapadm password \
           -dbname SID -dbtype ada -function SetDatabaseProperty DBCredentials=SET \
           -dboption User=SUPERDBA -dboption Password=password

Test the entries using the following command, even if the database is stopped the command should be able to bring the status back:
         
         /usr/sap/hostctrl/exe/saphostctrl -host secondary-host-name -dbname SID \
           -dbtype ada -function GetDatabaseStatus




The saphostctrl agent command uses the `xuser` program from MaxDB installation and hence to prepare the second node now, you will move the `SAPMaxDB_group` to maxdb-node-b.

  1. On any node execute the following command as root:
         
         pcs resource move SAPMaxDB_group




Observe that the four created resources, Health check, `gcp-pd-move`, LVM and File System are now migrated and successfully started on the second node.

  1. You can use the following command on any node to watch the actions being performed:
         
         watch pcs status




Once all four resources are successfully started on the second node, perform the `saphostctrl` command.

  1. As root, execute the following command to SetDatabaseProperty on the now active node:
         
         /usr/sap/hostctrl/exe/saphostctrl -host secondary-host-name -user sapadm password \
           -dbname SID -dbtype ada -function SetDatabaseProperty DBCredentials=SET \
           -dboption User=SUPERDBA -dboption Password=password

  2. On the node b, manually start MaxDB and `x_server` to check if they can be started properly:
         
         # dbmcli -d SID -u control, and password db_online
         # x_server start
         




Proceed to the next step of creating a resource for the SAP database. If any errors are observed at this point, don't create the database resource.

### Create resource for SAP MaxDB

RHEL Pacemaker uses the SAP database resource agent to monitor and control the SAP database.

  1. Create the database resource on the node where SAPMaxDB_group is active using the following command:
         
         # pcs resource create SAPDatabase_resource_name SAPDatabase \
           DBTYPE="ADA" SID="SID" STRICT_MONITORING="TRUE" \
           MONITOR_SERVICES="Database|x_server" AUTOMATIC_RECOVER="TRUE"
           --group SAPMaxDB_Group

The final cluster resources can be seen using `pcs status` and the expected result is as follows:
         
         # pcs status
           Cluster name: maxdb-cluster
           Stack: corosync
           Current DC: maxdb-ha-vm-1 (version 1.1.23-1.el7_9.1-9acf116022) - partition with quorum
           Last updated: Wed Oct 23 02:04:32 2024
           Last change: Wed Oct 23 02:01:41 2024 by hacluster via crmd on maxdb-ha-vm-1
         
           2 nodes configured
           7 resource instances configured
         
           Online: [ maxdb-ha-vm-1 maxdb-ha-vm-2 ]
         
           Full list of resources:
         
           STONITH-maxdb-ha-vm-1  (stonith:fence_gce):    Started maxdb-ha-vm-2
           STONITH-maxdb-ha-vm-2  (stonith:fence_gce):    Started maxdb-ha-vm-1
           Resource Group: SAPMaxDB_Group
              healthcheck_maxdb  (service:haproxy):      Started maxdb-ha-vm-1
              sapdb_regpd        (ocf::heartbeat:gcp-pd-move):   Started maxdb-ha-vm-1
              lvm_sapdb  (ocf::heartbeat:LVM-activate):  Started maxdb-ha-vm-1
              sapdb_fs   (ocf::heartbeat:Filesystem):    Started maxdb-ha-vm-1
              MDB_SAPMaxDB       (ocf::heartbeat:SAPDatabase):   Started maxdb-ha-vm-1
         
           Daemon Status:
           corosync: active/enabled
           pacemaker: active/enabled
           pcsd: active/enabled




## Test failover

Test your cluster by simulating a failure on the active host. Use a test system or run the test on your production system before you release the system for use.

Backup the system before the test.

You can simulate a failure in a variety of ways, including:

  * Manually stop MaxDB or `x_server`
  * Kill MaxDB or `x_server` process
  * `reboot` (on the active node)
  * `ip link set eth0 down` for instances with a single network interface
  * `iptables ... DROP` for instances with multiple network interfaces
  * `echo c > /proc/sysrq-trigger`



These instructions use `ip link set eth0 down` or `iptables` to simulate a network disruption between your two hosts in the cluster. Use the `ip link` command on an instance with a single network interface and use the `iptables` command on instances with one or more network interfaces. The test validates both failover as well as fencing. In the case where your instances have multiple network interfaces defined, you use the `iptables` command on the secondary host to drop incoming and outgoing traffic based on the IP used by the primary host for cluster communication, thereby simulating a network connection loss to the primary.

  1. On the active host, as root, take the network interface offline:
         
         # ip link set eth0 down

  2. Reconnect to either host using SSH and change to the root user.

  3. Enter `pcs status` to confirm that the previously passive host has now the Regional Persistent Disk attached and is running the MaxDB services. Automatic restart is enabled in the cluster, so the stopped host will restart and assume the role of passive host, as shown in the following example:
         
         Cluster name: maxdb-ha-cluster
         Stack: corosync
         Current DC: maxdb-ha-vm-2 (version 1.1.23-1.el7_9.1-9acf116022) - partition with quorum
         Last updated: Wed Oct 23 02:01:45 2024
         Last change: Wed Oct 23 02:01:41 2024 by hacluster via crmdon maxdb-ha-vm-2
         
         2 nodes configured
         7 resources configured
         
         Online: [ maxdb-ha-vm-1 maxdb-ha-vm-2 ]
         
         Full list of resources:
         
         STONITH-maxdb-ha-vm-1   (stonith:fence_gce):    Started maxdb-ha-vm-2
         STONITH-maxdb-ha-vm-2   (stonith:fence_gce):    Started maxdb-ha-vm-1
         
         Resource Group: SAPMaxDB_Group
          healthcheck_maxdb  (service:haproxy):      Started maxdb-ha-vm-2
          sapdb_regpd        (ocf::heartbeat:gcp-pd-move):   Started maxdb-ha-vm-2
          lvm_sapdb  (ocf::heartbeat:LVM-activate):  Started maxdb-ha-vm-2
          sapdb_fs   (ocf::heartbeat:Filesystem):    Started maxdb-ha-vm-2
          MDB_SAPMaxDB       (ocf::heartbeat:SAPDatabase):   Started maxdb-ha-vm-2
         
         Daemon Status:
          corosync: active/enabled
          pacemaker: active/enabled
          pcsd: active/enabled




## Troubleshoot

To troubleshoot problems with high-availability configurations for SAP systems on RHEL, see [Troubleshooting high-availability configurations for SAP](https://docs.cloud.google.com/sap/docs/troubleshooting/troubleshooting-sap-ha).

## Get support for SAP HANA on RHEL

If you need help resolving a problem with high-availability clusters for SAP HANA on RHEL, then gather the required diagnostic information and contact Cloud Customer Care. For more information, see [High-availability clusters on RHEL diagnostic information](https://docs.cloud.google.com/sap/docs/getting-support-diag-info-ha-rhel).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
