---
url: https://docs.cloud.google.com/sap/docs/oracle-deployment-single-node/
title: Deploy Oracle Database for SAP NetWeaver \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:21.401984+00:00
---

# Deploy Oracle Database for SAP NetWeaver  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/oracle-deployment-single-node/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Deploy Oracle Database for SAP NetWeaver Stay organized with collections  Save and categorize content based on your preferences. 

This deployment guide shows you how to provision the resources required to run an Oracle Database with Oracle Linux for use with SAP NetWeaver based applications on Google Cloud. 

For information about planning this implementation, see [Plan Oracle Database implementation for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/oracle-planning).

## Before you begin

  1. Read the [Plan Oracle Database implementation for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/oracle-planning). 

  2. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  3. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  11. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  12. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  13. If you require your SAP workload to run in compliance with data residency, access control, support personnel, or regulatory requirements, then you must create the required Assured Workloads folder. For more information, see [Compliance and sovereign controls for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/compliance-and-sovereign-controls). 
  14. Make sure that you have access to the Oracle Database installation media.



## Create a VPC network

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



## Set up a NAT gateway

If you need to create one or more compute instances without public IP addresses, then you need to use network address translation (NAT) to enable the instances to access the internet. Use Cloud NAT, a Google Cloud distributed, software-defined managed service that lets the compute instances send outbound packets to the internet and receive any corresponding established inbound response packets. Alternatively, you can set up a separate compute instance as a NAT gateway.

**Key Point:** When you configure Cloud NAT, specify at least 160 as the minimum number of ports per compute instance. Certain operating system updates run concurrent processes that might exceed the Cloud NAT default for the number of ports, which can result in activation or download errors. 

When you create a Cloud NAT instance, specify the number of ports in the **Minimum ports per VM** field under **Advanced configurations** on the Create a NAT gateway page in the Google Cloud console.

To create a Cloud NAT instance for your project, see [Using Cloud NAT](https://docs.cloud.google.com/nat/docs/set-up-network-address-translation).

After you configure Cloud NAT for your project, your compute instances can securely access the internet without a public IP address.

## Prepare the Oracle Linux image

###  Image from Compute Engine 

If you use an Oracle Linux image provided by Compute Engine, then you can skip this section because these images contain the packages required to run Oracle Database with SAP NetWeaver systems on Google Cloud.

###  Image from Oracle 

To prepare the Oracle Linux image that you need to run your Oracle Database for SAP systems, you need to import the image into your Google Cloud project and install the necessary drivers.

To prepare the Oracle Linux image, follow these steps:

  1. From Oracle, download an Oracle Linux image that is certified by SAP for use with SAP NetWeaver based applications on Google Cloud.

For information about SAP-certified OS versions, see [Supported operating systems](https://docs.cloud.google.com/sap/docs/oracle-planning#supported_operating_systems).

  2. Import the image to a Compute Engine image:

     * To import an image of the QCOW2 format, follow the instructions provided in [Import virtual disk images](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/image_import).
     * To import an image of the OVA format, follow the instructions provided in [Import machine images](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/machine-image-import).
  3. Create a custom OS image:

     1. Create a small VM by using the imported image, and set the instance name to `vm-ol-gvnic`.

For information about how to do this, see [Create an instance from a custom image](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-custom-image).

     2. Connect to your instance by using SSH.

     3. Install the `gve` driver:
            
            yum install kernel-uek-modules-extra.x86_64
            echo gve > /etc/modules-load.d/gve.conf
            

     4. Stop the instance.

For information about how to do this, see [Stop or restart a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance).

     5. Turn off the default auto-delete behavior of the disk attached to your compute instance. This prevents the boot disk from being deleted when you delete the compute instance.
            
            [gcloud compute instances set-disk-auto-delete](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/set-disk-auto-delete) vm-ol-gvnic \
             --no-auto-delete \
             --disk=vm-ol-gvnic

     6. Create a temporary image for the boot disk:
            
            [gcloud compute images create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/create) ol-uek-temp \
             --source-disk=vm-ol-gvnic \
             --source-disk-zone=ZONE \
             --storage-location=LOCATION

Replace the following:

        * `ZONE`: the zone where the boot disk is deployed
        * `LOCATION`: the Cloud Storage location where you want to store the image
     7. Create a boot disk image that supports [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/networking/using-gvnic), by using the temporary image you created:
            
            gcloud compute images create ol-uek-production \
             --source-image=ol-uek-temp \
             --source-image-project=PROJECT_ID \
             --guest-os-features="GVNIC" \
             --storage-location=LOCATION

Replace the following:

        * `PROJECT_ID`: the project ID of the Google Cloud project where the source image exists
        * `LOCATION`: the Cloud Storage location where you want to store the image
     8. Except the gVNIC-enabled boot disk image, delete the temporary image and the VM that you created in this section:
            
            [gcloud compute images delete](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/delete) ol-uek-temp
            [gcloud compute instances delete vm-ol-gvnic](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/delete) --zone=ZONE
            [gcloud compute disks delete](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/delete) DISK_NAME --zone=ZONE

Replace the following:

        * `ZONE`: the zone where the boot disk is deployed
        * `DISK_NAME`: the name of the boot disk of the temporary VM that you want to delete



## Create a Compute Engine instance for the Oracle Database

While creating a Compute Engine instance, you can specify several options such as the machine type, the region where the instance is created, and additional disks for storage.

To create a Compute Engine instance for the Oracle Database, complete the following steps:

###  Image from Compute Engine 

  1. In the Google Cloud console, go to the Compute Engine **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. In the **Name** field, enter a name for your instance.

Limit the name to 13 characters, as this is the maximum supported by SAP. For more information, see the SAP note [611361 \- Hostnames of SAP ABAP platform servers](https://me.sap.com/notes/611361).

  4. In the **Region** and **Zone** fields, select the region and zone where you want to create the instance.

While selecting these, make sure to consider the location of your internal resources and users, and availability of the machine type that you want to use. For information about selecting the region and zone, see [Plan regions and zones](https://docs.cloud.google.com/sap/docs/oracle-planning#plan_regions_and_zones).

  5. Change the machine type to one of the supported machine types.

For information about the supported machine types and their persistent-disk limitations, see the [Plan Oracle Database implementation for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/oracle-planning).

  6. Go to the **OS and storage** tab.

  7. Click **Change**.

  8. In the **Boot disk** pane, perform the following:

     1. In the **Operating system** field, select **Oracle Linux**.
     2. In the **Version** field, select the required version.
     3. Review the other default settings and modify them if required.
     4. Click **Select**.
  9. Create additional disks for your Oracle Database. For information about the drives for which you need to provision disks, see [Deployment architecture](https://docs.cloud.google.com/sap/docs/oracle-planning#deployment_architecture).

To create a disk, follow these steps:

     1. Under **Additional disks** , click **Add new disk**.
     2. In the **Name** field, enter a name for the disk.
     3. In the **Disk storage type** field, select **Blank disk**.
     4. In the **Disk type** field, select a supported disk type. For information about supported disk types, see [Block storage](https://docs.cloud.google.com/sap/docs/oracle-planning#block_storage) in the planning guide.
     5. In the **Size** field, set a value that meets your performance requirements.
     6. Click **Save**.
     7. Repeat the preceding set of steps for each disk that you need to provision.
  10. Click **Create**.




###  Image from Oracle 

  1. In the Google Cloud console, go to the Compute Engine **Images** page.

[Go to Images](https://console.cloud.google.com/compute/images)

  2. Select the Oracle Linux image that you prepared in the previous section, and then click **Create instance**.

  3. In the **Name** field, enter a name for your instance.

Limit the name to 13 characters, as this is the maximum supported by SAP. For more information, see the SAP note [611361 \- Hostnames of SAP ABAP platform servers](https://me.sap.com/notes/611361).

  4. In the **Region** and **Zone** fields, select the region and zone where you want to create the instance.

While selecting these, make sure to consider the location of your internal resources and users, and availability of the machine type that you want to use. For information about selecting the region and zone, see [Plan regions and zones](https://docs.cloud.google.com/sap/docs/oracle-planning#plan_regions_and_zones).

  5. Change the machine type to one of the supported machine types.

For information about the supported machine types and their persistent-disk limitations, see the [Plan Oracle Database implementation for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/oracle-planning).

  6. Go to the **OS and storage** tab.

  7. Create additional disks for your Oracle Database. For information about the drives for which you need to provision disks, see [Deployment architecture](https://docs.cloud.google.com/sap/docs/oracle-planning#deployment_architecture).

  8. To create a disk, follow these steps:

     1. Under **Additional storage and VM backups** , click **Add new disk**.
     2. In the **Name** field, enter a name for the disk.
     3. In the **Disk storage type** field, select **Blank disk**.
     4. In the **Disk type** field, select a supported disk type. For information about supported disk types, see [Block storage](https://docs.cloud.google.com/sap/docs/oracle-planning#block_storage) in the planning guide.
     5. In the **Size** field, set a value that meets your performance requirements.
     6. Click **Save**.
     7. Repeat the preceding set of steps for each disk that you need to provision.
  9. Click **Create**.




## Format and mount disk drives

  1. Connect to your compute instance by using SSH.
  2. Make sure that the Hyperdisk or Persistent Disk volumes you've attached to the compute instance are large enough to provide performant storage for the instance.
  3. Format and mount drives with logical volumes for all required drives by using LVM.



For information about the disk drives and their grouping, see [Deployment architecture](https://docs.cloud.google.com/sap/docs/oracle-planning#deployment_architecture).

## Prepare the OS

  1. Connect to your Compute Engine instance by using SSH.
  2. As recommended by Oracle, make sure that the Transparent HugePages feature is disabled.

To verify this, follow these steps:

     1. Check if the Transparent HugePages feature is enabled by running the following command:
            
            cat /sys/kernel/mm/transparent_hugepage/enabled
            

     2. If the Transparent HugePages feature is enabled, then disable it by running the following commands:
            
            ORIGINAL=$(grep GRUB_CMDLINE_LINUX /etc/default/grub)
            INSERT=" transparent_hugepage=never"
            TARGET=$(printf '%s\n' "$ORIGINAL" | sed -e "s/\"$/$INSERT&/")
            sed -i "s%^GRUB_CMDLINE_LINUX.*$%$TARGET%" /etc/default/grub
            grub2-mkconfig -o /boot/grub2/grub.cfg
            

     3. Restart your instance. For information about how to do this, see [Restart an instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#restart-vm).

For information from SAP about these features, see the following SAP notes:

     * [1770532 - HugePages on Linux for Oracle Database](https://me.sap.com/notes/1770532)
     * [1672954 - Oracle 11g, 12c, 18c and 19c: Usage of hugepages on Linux](https://me.sap.com/notes/1672954)
  3. Install the Oracle Database preinstallation RPM:
         
         yum install oracle-database-preinstall-19c
         

If you're using Oracle Linux 9, then run the following command as well:
         
         yum in libxcrypt-compat
         




## Set up Oracle ASM

Skip this section if you don't intend to use Oracle Automatic Storage Management (ASM).

To use Oracle ASM, as the root user, complete the following steps:

  1. Install the latest version of the ASMlib library.

For information about how to do this, see [Updating ULN Subscriptions or Downloading Packages](https://docs.oracle.com/en/operating-systems/oracle-linux/asmlib/asmlib-InstallingASMLib.html#update_uln_subscriptions_or_enable_yum_repositories).

  2. Configure the ASMlib library:
         
         oracleasm configure -i -u oracle -g dba
         systemctl enable --now oracleasm
         

  3. For the disks that you want Oracle ASM to manage, complete the following steps:

     1. Identify the disk:
            
            ls -l /dev/disk/by-id | grep DISK_NAME | awk -F \/ '{ print $3 }'
            

Replace `DISK_NAME` with the name of the disk.

     2. On the identified disk, create a partition:
            
            parted -s -a optimal /dev/DISK_ID mklabel gpt mkpart primary 0% 100%
            

Replace `DISK_ID` with the disk ID that you noted in the previous step.

     3. Verify the disk partition:
            
            ASMDISKID=DISK_ID"p1"
            ls -l /dev/$ASMDISKID
            

     4. Create an ASM disk with a label:
            
            oracleasm createdisk LABEL /dev/$ASMDISKID
            

Replace `LABEL` with a name that is used by Oracle ASM to manage the disk.




## Install Google Cloud's Agent for SAP

Google Cloud's Agent for SAP is required for SAP support of SAP systems running on Google Cloud, including SAP NetWeaver, SAP HANA, SAP ASE, SAP MaxDB, and others.

When you install Google Cloud's Agent for SAP on a Compute Engine instance, for SAP Host Agent metrics, the agent combines monitoring data from Cloud Monitoring and the Compute Engine APIs and provides that data to the SAP Host Agent.

If you use the following RHEL or SLES "for SAP" OS images that Google Cloud provides, then Google Cloud's Agent for SAP is packaged with the OS images:

  * RHEL: all "for SAP" images
  * SLES: SLES 15 SP4 for SAP and later versions



For information about the operating systems supported by Google Cloud's Agent for SAP, see [Supported operating systems](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#supported_operating_systems).

### Prerequisites for the agent

Before you install Google Cloud's Agent for SAP, you need to ensure that the following prerequisites are met.

#### Set the required IAM roles

To ensure that the service account has the necessary permissions to let Google Cloud's Agent for SAP collect metrics, ask your administrator to grant the following IAM roles to the service account on your project: 

**Important:** You must grant these roles to the service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * Collect metrics from the Compute Engine instances that host your SAP workload: [Compute Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`) 
  * Read the collected metrics from Cloud Monitoring: [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`) 
  * Write the collected metrics to Workload Manager data warehouse: [Workload Manager Insights Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.insightWriter) (`roles/workloadmanager.insightWriter`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to let Google Cloud's Agent for SAP collect metrics. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to let Google Cloud's Agent for SAP collect metrics:

  * Collect the metrics from the host Compute Engine instance and write them to Cloud Monitoring and Workload Manager data warehouse: 
    * `compute.instances.get`
    * `compute.instances.list`
    * `monitoring.metricDescriptors.get`
    * `monitoring.metricDescriptors.list`
    * `monitoring.timeSeries.create`
    * `workloadmanager.insights.writer`



Your administrator might also be able to give the service account these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

#### Enable access to Google Cloud APIs

Compute Engine recommends configuring your compute instances to allow all access scopes to all Cloud APIs and using only the IAM permissions of the instance service account to control access to Google Cloud resources. For more information, see [Create a VM that uses a user-managed service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances).

If you do limit access to the Cloud APIs, then Google Cloud's Agent for SAP requires the following minimum Cloud API access scopes on the host Compute Engine instance:

  * **Cloud Platform** : **Enabled**
  * **Compute Engine** : **Read Only**
  * **Stackdriver Monitoring API** : **Read Only**



If you are running SAP applications on a compute instance that does not have an external IP address, then you need to enable [Private Google Access ](https://docs.cloud.google.com/vpc/docs/private-google-access) on the subnet of the compute instance so that Google Cloud's Agent for SAP can access Google APIs and services. To enable Private Google Access on a subnet, see [Configuring Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).

### Install the agent

To install Google Cloud's Agent for SAP on a Compute Engine instance that uses Oracle Linux, follow these steps:

  1. Establish an SSH connection to your compute instance.

  2. To install version 3.15 (latest) of the agent, run the following command:
         
         sudo tee /etc/yum.repos.d/google-cloud-sap-agent.repo << EOM
         [google-cloud-sap-agent]
         name=Google Cloud Agent for SAP
         baseurl=https://packages.cloud.google.com/yum/repos/google-cloud-sap-agent-el$(cat /etc/redhat-release | cut -d . -f 1 | tr -d -c 0-9)-x86_64
         enabled=1
         gpgcheck=1
         repo_gpgcheck=0
         gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
         EOM
         sudo yum install google-cloud-sap-agent




### Verify that the agent is running

To verify that the agent is running, follow these steps:

  1. Establish an SSH connection with your Compute Engine instance. 

  2. Run the following command: 
         
         systemctl status google-cloud-sap-agent

If the agent is functioning properly, then the output contains `active (running)`. For example: 
         
         google-cloud-sap-agent.service - Google Cloud Agent for SAP
         Loaded: loaded (/usr/lib/systemd/system/google-cloud-sap-agent.service; enabled; vendor preset: disabled)
         Active: **active (running)** since Fri 2022-12-02 07:21:42 UTC; 4 days ago
         Main PID: 1337673 (google-cloud-sa)
         Tasks: 9 (limit: 100427)
         Memory: 22.4 M (max: 1.0G limit: 1.0G)
         CGroup: /system.slice/google-cloud-sap-agent.service
                └─1337673 /usr/bin/google-cloud-sap-agent
         




If the agent isn't running, then [restart the agent](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#agent4sap-restart).

### Verify that SAP Host Agent is receiving metrics

To verify that the infrastructure metrics are collected by Google Cloud's Agent for SAP and sent correctly to the SAP Host Agent, follow these steps:

  1. In your SAP system, enter transaction `ST06`.
  2. In the overview pane, check the availability and content of the following fields for the correct end-to-end setup of the SAP and Google monitoring infrastructure:

     * **Cloud Provider** : `Google Cloud Platform`
     * **Enhanced Monitoring Access** : `TRUE`
     * **Enhanced Monitoring Details** : `ACTIVE`



## Install the Oracle Database

  * Install a supported Oracle Database on the Compute Engine instance that you created.

If you've set up Oracle ASM, then make sure to select Oracle ASM as the storage mechanism for the Oracle Database files, redo log files, control files, and temp files.

For information about supported Oracle Database versions and features, see [Supported Oracle Database versions and features](https://docs.cloud.google.com/sap/docs/oracle-planning#supported_oracle_database_versions_and_features).

For information about how to install the database, refer to the following SAP notes:

    * [2660017 - Oracle Database Software Installation on Unix](https://me.sap.com/notes/2660017)
    * [3296921 - Installing Oracle Database 19c on Oracle Linux 9 and Red Hat Enterprise Linux 9](https://me.sap.com/notes/3296921)
    * [2799920 - Patches for 19c: Database](https://me.sap.com/notes/2799920)
    * [2470718 - Oracle Database Parameter 12.2 / 18c / 19c](https://me.sap.com/notes/2470718)
    * [2378252 - Oracle Database Initialization Parameters for SAP NetWeaver Systems](https://me.sap.com/notes/2378252)
    * [1915299 - Troubleshooting Oracle Software Installation ( 12.1 / 12.2 / 18c / 19c )](https://me.sap.com/notes/1915299)



## Get support

For issues with Google Cloud infrastructure or services, contact Cloud Customer Care. You can find the contact information on the [Support Overview](https://console.cloud.google.com/support) page in the Google Cloud console. If Customer Care determines that a problem resides in your SAP systems, then you are referred to SAP Support.

For SAP product-related issues, log your support request with SAP support. SAP evaluates the support ticket and, if it appears to be a Google Cloud infrastructure issue, then SAP transfers that ticket to the appropriate Google Cloud component in its system: `BC-OP-LNX-GOOGLE` or `BC-OP-NT-GOOGLE`.

### Support requirements

  * To receive support from Oracle and SAP for your Oracle Linux based Oracle Database, make sure that you have purchased Oracle Linux Premier Support.
  * Before you can receive support for SAP systems and the Google Cloud infrastructure and services that they use, you must meet the minimum support plan requirements.

For more information about the minimum support requirements for SAP on Google Cloud, see:

    * [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support)
    * [ SAP Note 2456406 - SAP on Google Cloud Platform: Support Prerequisites](https://launchpad.support.sap.com/#/notes/2456406) (An SAP user account is required)

For information about SAP support for Oracle, see the SAP note [2799900 - Central Technical Note for Oracle Database 19c](https://me.sap.com/notes/2799900).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
