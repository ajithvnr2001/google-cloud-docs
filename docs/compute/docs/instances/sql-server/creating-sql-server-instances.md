---
url: https://docs.cloud.google.com/compute/docs/instances/sql-server/creating-sql-server-instances/
title: Create SQL Server VM instances \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:02.001756+00:00
---

# Create SQL Server VM instances  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/sql-server/creating-sql-server-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create SQL Server VM instances Stay organized with collections  Save and categorize content based on your preferences. 

Microsoft SQL Server is a database system that runs on Windows Server and some Linux distributions. You can use SQL Server on Compute Engine as part of the backend for your applications, as a flexible development and test environment, or in addition to your on-premises systems for backup and disaster recovery.

Compute Engine provides images with Microsoft SQL Server preinstalled on Windows Server. For these SQL Server images, Compute Engine manages the license for both Windows Server and SQL Server, and includes the cost in your monthly bill. Create virtual machine (VM) instances with SQL Server and scale out to large multi-node configurations when you need them.

Compute Engine stores your data on durable [block storage disks](https://docs.cloud.google.com/compute/docs/disks) with automatic redundancy and automatic encryption at rest. Use these disks to store your SQL Server data and you don't need to worry about the durability or security of your data. For additional performance, create your VM instances with a [Local SSD](https://docs.cloud.google.com/compute/docs/disks#localssds) as a cache that provides additional IOPS and performance for SQL Server queries.

You can create Compute Engine VM instances that run SQL Server in the following ways:

  * Create a VM instance using a SQL Server image. These images include one of several SQL Server editions that run on Windows Server. You can use these images to run SQL Server on Compute Engine and you don't need to obtain your own separate license from Microsoft.

  * [Migrate your existing SQL Server licenses](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing) to a Windows Server VM instance on Compute Engine and manage those licenses yourself.

  * [Install SQL Server on a Compute Engine Linux VM](https://docs.cloud.google.com/compute/docs/instances/sql-server/adding-sql-server-license-to-linux).




For a full list of the available images that include SQL Server preinstalled, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#sql_server).

### Machine type requirements for SQL Server images

The best machine type for SQL Server depends on the edition of SQL Server that you run.

#### SQL Server Standard

You can run SQL Server Standard on VM instances created with any machine type, but [shared-core machine types](https://docs.cloud.google.com/compute/docs/machine-resource#shared-core-types) don't provide optimal performance. Google recommends that you use VM instances with at least one vCPU to run SQL Server Standard.

#### SQL Server Enterprise

VM instances that run SQL Server Enterprise must have at least 4 vCPUs. For optimal performance, Google recommends that you run SQL Server Enterprise on VM instances with larger memory capacities. Depending on your workload, you should use `highmem` predefined machine types with 8 vCPUs or more, such as for [N2](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2-high-mem). The `highmem` predefined machine types maximize the ratio of memory to each vCPU that is available on Compute Engine, which is optimal for SQL Server Enterprise VMs.

You can use SQL Server Enterprise on Compute Engine to [create SQL Server Availability Groups](https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-availability).

### Default components

SQL Server images include several components by default. The default components depend on the edition of SQL Server that you selected.

For information about the default components included with your version of SQL Server, see [Editions and supported features of SQL Server 2019](https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2019?view=sql-server-ver15).

For information about modifying the SQL Server components, see [Add Features to an Instance of SQL Server](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/add-features-to-an-instance-of-sql-server-setup?view=sql-server-ver15).

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### Terraform

To use the Terraform samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Create a SQL Server instance

To create a SQL Server instance, specify the image family for the specific version of SQL Server that you need. For a list of the SQL Server image families, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#sql_server).

**Note:** If you create a SQL Server instance from a Google-provided public image, then the SQL Server instance name (returned by `SELECT @@SERVERNAME`) is preset within the image. This preset name doesn't match the hostname of your VM instance. To ensure that the SQL Server instance name matches the hostname of your VM instance, update the name after you create the instance. For instructions, see Update SQL Server instance names.

For optimal performance, database server platforms require machine types with more virtual CPUs and larger amounts of memory. Google recommends that you use machine types with at least 2 vCPUs and at least 4 GB of memory when you run SQL Server instances. You can use [custom machine types](https://docs.cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types) to configure SQL Server instances to match the performance requirements for your workload. You can use larger disks or faster disk types to improve the performance of your applications.

You must set specific firewall rules to allow SQL Server traffic on the VPC network or subnet that your VM instance is a part of. For more information see [Best practices for SQL Server](https://docs.cloud.google.com/compute/docs/instances/sql-server/best-practices#windows_firewall).

###  Console 

To create a SQL Server instance, follow these steps:

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. Specify the VM instance details.

  3. Click the **OS and storage** vertical tab.

  4. Click **Change** , and then do the following:

     1. On the **Public images** tab, click the **Operating system** list, and then select **SQL Server on Windows Server**.
     2. In the **Version** list, select a version.
     3. In the **Boot disk type** list, select a boot disk type.
     4. In the **Size (GB)** field, set the boot disk size.
     5. Optional: To modify the advanced configuration for the boot disk, click **Show advanced configuration** , and then specify your settings.
     6. To save the boot disk configuration, click **Select**.
  5. In the **Create an instance** window, click **Create**.




After you create the VM instance, create a firewall rule to allow access to SQL Server on your instance. The default SQL Server port is `1433`.

  1. In the Google Cloud console, go to the **Firewall Rules** page.

[Go to Firewall Rules](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. At the top of the page, click **Create firewall rule**.

  3. Specify the details for this firewall rule.

     * In the **Name** field, specify a name for the firewall rule.
     * In the **Network** field, select the VPC network where your SQL Server instance is located.
     * For the **Direction of traffic** , select Ingress.
     * In the **Targets** field, choose the targets for the firewall rule, which can be all instances, or specified target tags or service accounts. For example, you can select the option **All instances in the network**. If you configured a tag or service account for your SQL Server instance, then you can limit the firewall rule to the specific tag or service account.
     * In **Source filter** field, select the range of IPs that you want to allow access on this port. For an ingress rule, you can select Source IPv4 ranges, source IPv6 ranges, source tags, or service accounts. Use the fields after **Source filter** to supply additional information about your choice.
     * In the **Protocols and ports** section, choose **Specified protocols and ports** and enter the port that SQL Server uses. For this example, choose **TCP** and enter `1433`, which is the default port.
  4. Click **Create** to create this firewall rule and allow access to your SQL Server instance over the specified port.




If you need to add additional firewall rules to your VM instance, see the [firewall rules documentation](https://docs.cloud.google.com/firewall/docs/using-firewalls).

###  gcloud 

Use the [`compute images list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list) command to see a list of available SQL Server images: 
    
    
    gcloud compute images list --project windows-sql-cloud --no-standard-images
    

Use the [`compute instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) command to create a new VM and specify the image family for one of the Windows Server or SQL Server [public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).
    
    
    gcloud compute instances create VM_NAME \
        --image-project windows-sql-cloud \
        --image-family IMAGE_FAMILY \
        --machine-type MACHINE_TYPE \
        --boot-disk-size BOOT_DISK_SIZE \
        --boot-disk-type BOOT_DISK_TYPE
    

Replace the following:

  * VM_NAME: the [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) for the new instance.
  * IMAGE_FAMILY: one of the [public image families](https://docs.cloud.google.com/compute/docs/images#os-compute-support) for Windows Server or SQL Server images.
  * MACHINE_TYPE: one of the available [machine types](https://docs.cloud.google.com/compute/docs/machine-resource).
  * BOOT_DISK_SIZE: the size of the boot disk in GB. Larger Persistent Disks have [higher throughput](https://docs.cloud.google.com/compute/docs/disks/performance#size_price_performance).
  * BOOT_DISK_TYPE: the [type](https://docs.cloud.google.com/compute/docs/disks#disk-types) of the boot disk for your instance. For example, `pd-balanced`.



After you create the VM, create a firewall rule to allow access to SQL Server on your VM. The default SQL Server port is 1433.
    
    
    gcloud compute firewall-rules create sql-server-1433 \
        --description "Allow SQL Server access from all sources on port 1433." \
        --allow tcp:1433 --network NETWORK
    

where NETWORK is the name of the VPC network where your VM is located.

If you need to add additional firewall rules to your VM, see the [firewall rules documentation](https://docs.cloud.google.com/firewall/docs/using-firewalls).

###  Terraform 

To create the SQL Server VM instances, use the [`google_compute_instance` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance).
    
    
    resource "google_compute_instance" "sqlserver_vm" {
      provider = google-beta
      name     = "sqlserver-vm"
      boot_disk {
        auto_delete = true
        device_name = "persistent-disk-0"
        initialize_params {
          image = "windows-sql-cloud/sql-std-2019-win-2022"
          size  = 50
          type  = "pd-balanced"
        }
        mode = "READ_WRITE"
      }
      machine_type = "n1-standard-4"
      zone         = "europe-west1-b"
      network_interface {
        access_config {
          network_tier = "PREMIUM"
        }
        network    = google_compute_network.default.id
        stack_type = "IPV4_ONLY"
        subnetwork = google_compute_subnetwork.default.id
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

To create a VM with the API, include the [`initializeParams` property](https://docs.cloud.google.com/compute/docs/reference/latest/instances#disks.initializeParams) in your VM creation request and specify a Windows image.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    instance = {
      "name": "VM_NAME",
      "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
      "disks": [{
          "boot": "true",
          "type": "PERSISTENT",
          "initializeParams": {
             "diskName": "DISK_NAME",
             "sourceImage": "projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY",
             "diskSizeGb": "BOOT_DISK_SIZE",
             "diskType": "BOOT_DISK_TYPE",
           }
        }],
      "networkInterfaces": [{
        "accessConfigs": [{
          "type": "ONE_TO_ONE_NAT",
          "name": "External NAT"
         }],
        "network": "global/networks/default"
      }],
      "serviceAccounts": [{
           "email": DEFAULT_SERVICE_EMAIL,
           "scopes": DEFAULT_SCOPES
      }]
    }
    

Replace the following:

  * PROJECT_ID: the ID for your project.
  * ZONE: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) for this instance.
  * VM_NAME: the [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) for the new VM.
  * MACHINE_TYPE: the available [machine types](https://docs.cloud.google.com/compute/docs/machine-resource).
  * IMAGE_PROJECT: either `windows-cloud` for Windows Server images or `windows-sql-cloud` for Windows Server images with SQL Server preinstalled.
  * IMAGE_FAMILY: the [public image families](https://docs.cloud.google.com/compute/docs/images#os-compute-support) for Windows Server or SQL Server images.
  * BOOT_DISK_SIZE: the size of the boot disk in GB. Larger Persistent Disks have [higher throughput](https://docs.cloud.google.com/compute/docs/disks/performance#size_price_performance).
  * BOOT_DISK_TYPE: the [type](https://docs.cloud.google.com/compute/docs/disks#disk-types) of the boot disk for your VM. For example, `pd-ssd`.



After you create the VM, use the [`firewalls.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert) to create a firewall rule that allows access to SQL Server on your VM. The default SQL Server port is `1433`.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/firewalls
    
    {
     "name": "sql-server-1433",
     "network": "global/networks/NETWORK",
     "allowed": [
      {
       "IPProtocol": "tcp",
       "ports": [
        "1433"
       ]
      }
     ]
    }
    

Replace the following:

  * PROJECT_ID: the ID for your project.
  * NETWORK: the name of the VPC network where your VM is located.



After you create your SQL Server instance, [set the initial password for the VM](https://docs.cloud.google.com/compute/docs/instances/windows/generating-credentials) so that you can [connect to the VM](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) using RDP. Run the SQL Server Management Studio as an administrator to manage databases on your SQL Server instance.

You can enhance the SQL Server installation with one or more of the following items:

  * Install SQL Server Data Tools (SSDT) on your SQL Server instance so that you can create and manage your SQL Server databases using Visual Studio. [Connect to Windows VMs using RDP](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) and [download and install SSDT](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver16) from the Microsoft website.
  * SQL Server images include several [default components](https://docs.cloud.google.com/compute/docs/instances/windows#sql_server_components). You can [add features to your SQL Server installation](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/add-features-to-an-instance-of-sql-server-setup?view=sql-server-ver16). SQL Server images always include the setup executable at `C:\sql_server_install\setup.exe`.
  * To install SQL Server to a secondary disk, [add a non-boot disk to your VM](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk). Then, connect to the VM instance and run the `C:\sql_server_install\setup.exe` installer and select a new installation path on your secondary disk.
  * If you require additional storage space on your boot disk or on any secondary storage disks, you can [Modify the size and provisioned performance of a Hyperdisk volume](https://docs.cloud.google.com/compute/docs/disks/modify-hyperdisks) or [Modify the size of a Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk), even while your VM instance is running.



## Manage SQL Server databases

Run the SQL Server Management Studio as an administrator to configure SQL Server databases. You can [download and install](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16) the SQL Server Management Studio on your local workstation, and use it to [connect to the database engine](https://learn.microsoft.com/en-us/sql/relational-databases/lesson-1-connecting-to-the-database-engine?view=sql-server-ver16) on your VM instance.

If you can't install the Management Studio on your local workstation, then [connect to Windows VMs using RDP](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) and run the Management Studio on the VM instance itself. SQL Server 2012 and SQL Server 2014 both include the SQL Server Management Studio by default. For SQL Server 2016, you must download the SQL Server Management Studio from the Microsoft website and install it on the VM instance.

By default, SQL Server uses Windows Authentication mode to control access to SQL Server itself. To use SQL Server Authentication mode, you can [change the authentication mode](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/change-server-authentication-mode?view=sql-server-ver16&tabs=ssms).

## Update SQL Server instance names

If you [rename a VM](https://docs.cloud.google.com/compute/docs/instances/rename-instance) that hosts SQL Server, then you must update the SQL Server instance name. For more information, see [Rename a computer that hosts a stand-alone instance of SQL Server](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/rename-a-computer-that-hosts-a-stand-alone-instance-of-sql-server?view=sql-server-ver15#rename-a-computer-that-hosts-a-stand-alone-instance-of-%22).

## What's next

  * [Verify that an instance has successfully started](https://docs.cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances#start_check).
  * [Create a new Hyperdisk volume](https://docs.cloud.google.com/compute/docs/disks/add-hyperdisk) or [create a new Persistent Disk volume](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk) and attach it to your VM instance to store your data separately from the boot disk.
  * [Learn best practices for SQL Server on Google Cloud](https://docs.cloud.google.com/compute/docs/instances/sql-server/best-practices).
  * [Create and configure a high-performance SQL Server instance](https://docs.cloud.google.com/compute/docs/tutorials/creating-high-performance-sql-server-instance).
  * Use HammerDB to run [Load testing on SQL Server](https://docs.cloud.google.com/compute/docs/tutorials/load-testing-sql-server-hammerdb).
  * [Use SQL Server with .NET applications](https://docs.cloud.google.com/dotnet/getting-started/using-sql-server).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
