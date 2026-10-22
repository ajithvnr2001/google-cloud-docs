---
url: https://docs.cloud.google.com/compute/docs/tutorials/creating-high-performance-sql-server-instance/
title: Creating a high-performance SQL Server instance \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:11.313439+00:00
---

# Creating a high-performance SQL Server instance  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/tutorials/creating-high-performance-sql-server-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Creating a high-performance SQL Server instance Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to create a Compute Engine VM instance running SQL Server that is optimized for performance. This tutorial guides you through creating the instance and then configuring SQL Server for optimal performance on Google Cloud. You will learn about a number of configuration options that are available to help you adjust the performance of the system.

This tutorial uses SQL Server Standard Edition 2022, so not every configuration option presented in this guide works for everyone, and not all of them provide noticeable performance benefits for every workload.

## Objectives

  * Setting up the Compute Engine instance and disks.
  * Configuring the Windows operating system.
  * Configuring SQL Server.



## Costs

This tutorial uses billable components of Google Cloud, including:

  * Compute Engine high-memory instance
  * Compute Engine SSD Persistent Disk storage
  * Compute Engine Local SSD disk storage
  * SQL Server Standard preconfigured image



The [Pricing Calculator](https://cloud.google.com/products/calculator/#id=2cf85e80-02ce-4417-8f24-f90eb770fd97) can generate a cost estimate based on your projected usage. The provided link shows the cost estimate for the products used in this tutorial, which can cost over 4 dollars (US) per hour and over 3,000 dollars per month.

New Google Cloud users might be eligible for a [free trial](https://console.cloud.google.com/freetrial). 

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




## Creating the Compute Engine VM with disks

To create a high-performance SQL Server instance, you must first create a VM instance with SQL Server and two Persistent Disk volumes.

### Persistent Disk considerations

To select the type of Persistent Disk volumes for your VM, review the following considerations:

  * A [Local SSD disk](https://docs.cloud.google.com/compute/docs/disks#localssds) provides a high-performance location for `tempdb` and the Windows pagefile.

There are some important considerations to note when using a Local SSD disk. When you shut down your instance from Windows or reset it by using the API, the Local SSD disk is removed. This action renders the instance unbootable. To get the machine running again, you would need to detach your persistent disks, create a new instance with them, and then define a new Local SSD disk. After startup you would also need to format the new disk and reboot. Therefore, you shouldn't permanently store critical data on a Local SSD disk, or power off the instance, unless you are prepared to rebuild it.

  * An [SSD Persistent Disk](https://docs.cloud.google.com/compute/docs/disks#pdspecs) provides high-performance storage for the database files.

Persistent Disk performance is based on a calculation that uses the number of CPUs and the size of the disk. With 32 vCPUs and a 1 TB disk, the performance peaks at 40,000 read operations per second (ops) and 30,000 write ops. The total sustained throughput for reads and writes is 800 MB per second and 400 MB per second respectively. These measurements represent a summation of all the Persistent Disk volumes attached to the virtual machine, including the `C:\` drive. To ensure consistent performance, create a Local SSD disk and offload all the IOPS needed for the paging file, `tempdb`, staging data, and backups.




To read more about disk performance, see [Configure disks to meet performance requirements](https://docs.cloud.google.com/compute/docs/disks/performance).

### Creating Compute Engine VM with disks

To create a VM that has SQL Server 2022 Standard preinstalled on Windows Server 2022, follow these steps:

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. For **Name** , enter `ms-sql-server`.

  3. In the **Machine configuration** section, select **General Purpose** , and then do the following:

     1. In the **Series** list, click **N2**.
     2. In the **Machine type** list, click **n2-highmem-16 (16vCPU, 128 GB memory)**.
  4. In the **Boot disk** section, click **Change** , and then do the following:

     1. On the **Public images** tab, click the **Operating system** list, and then select **SQL Server on Windows Server**.
     2. In the **Version** list, click **SQL Server 2022 Standard on Windows Server 2022 Datacenter**.
     3. In the **Boot disk type** list, click **Standard persistent disk**.
     4. In the **Size (GB)** field, set the boot disk size to **50** GB.
     5. To save the boot disk configuration, click **Select**.
  5. Expand the **Advanced options** section, and do the following:

     1. Expand the **Disks** section.
     2. To create local disks, click **Add Local SSD** , and then do the following:

        1. In the **Interface** list, select the protocol that meets your system's performance requirements.
        2. In the **Disk capacity** list, select a disk capacity that supports the anticipated size of `tempdb` files.
        3. To finish creating this disk, click **Save**.
     3. To create additional disks, click **Add New Disk**.

        1. Keep the **Name** field unchanged.
        2. In the **Disk source type** list, select **Blank disk**.
        3. In the **Disk type** list, select **SSD persistent disk**.
        4. In the **Size** field, enter the disk size that can accommodate the database size.
        5. To finish creating the second disk, click **Save**.
  6. To create the VM, click **Create**.




## Configuring Windows

Now that you have a working instance running SQL Server, connect to your instance and configure the Windows operating system. After that, you learn to configure SQL Server in an upcoming section.

### Connect to your instance

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Under the **Name** column, click the name of your instance, `ms-sql-server`.

  3. At the top of the instance's details page, click the **Set Windows Password** button.

  4. Specify a username.

  5. Click **Set** to generate a new password for this Windows instance.

  6. Note the username and password so you can log into the instance.

  7. Connect to your instance [by using RDP](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows#connecting_to_windows_vms_by_using_rdp).




### Setting up disk volumes

Create and format the volumes:

  1. From the **Start** menu, search for "Computer Management" and then open it.
  2. Under **Storage** section, select **Disk Management**.
  3. When prompted to initialize disks, accept the default selections and click **OK**.
  4. Create partition for Local SSD disk(s):

To locate a Local SSD disk, right-click on a disk and select **Properties**. The Local SSD disk properties name will be `Google EphemeralDisk` for a SCSI interface or `nvme_card` for an NVMe interface. Both Local SSD disks and persistent SSDs are marked as having `Unallocated` partitions.

     1. If the VM contains only 1 Local SSD drive, follow these steps:

        1. Under the list of disk drives, right-click the 374.98 GB local SSD disk and select **New Simple Volume**.
        2. On the Welcome screen, click **Next** to start the disk volume wizard.
        3. In the **Specify Volume Size** step, leave the volume size at the default value and click **Next** to proceed.
        4. In the **Assign Drive Letter or Path** step, choose **P:** for the drive letter and click **Next** to proceed.
        5. In the **Format Volume** step, change the **Allocation unit size** to 8192 and enter "pagefile" for the **Volume label**. Click **Next** to proceed.

![New Volume Wizard](https://docs.cloud.google.com/static/compute/docs/tutorials/images/high-perf-sql-disks.png)

        6. Click **Finish** to complete the disk volume wizard.

     2. If the VM contains multiple local SSD drives, follow these steps:

        1. Under the list of disk drives, right-click the first 374.98 GB local SSD disk and select **New Striped Volume**.
        2. On the Welcome screen, click **Next** to start the disk volume wizard.
        3. In the **Select Disks** step, add all the available disks with the size 383,982 MB to the Selected section. Click **Next** to proceed.

![Add striped disks](https://docs.cloud.google.com/static/compute/docs/tutorials/images/high-perf-sql-striped-volume.png)

        4. In the **Assign Drive Letter or Path** step, choose **P:** for the drive letter and click **Next** to proceed.

        5. In the **Format Volume** step, change the **Allocation unit size** to 8192 and enter "pagefile" for the **Volume label**. Click **Next** to proceed.

![New Volume Wizard](https://docs.cloud.google.com/static/compute/docs/tutorials/images/high-perf-sql-disks.png)

        6. Click **Finish** to complete the disk volume wizard.

  5. Repeat the previous steps to create a **New Simple Volume** for the SSD disk, with the following three changes:

     * Choose **D:** for the drive letter.

     * Set the **Allocation unit size** to `64k`.

For details on selecting an allocation unit size, see [Best practices for SQL Server instances](https://docs.cloud.google.com/compute/docs/instances/sql-server/best-practices#formatting_secondary_disks).

     * Enter `sqldata` for the **Volume label**.




### Moving the Windows paging file

Now that the new volumes are created and mounted, move the Windows paging file onto the Local SSD disk, which frees up Persistent Disk IOPS and improves the access time of your virtual memory.

  1. From the **Start** menu, search for **View advanced system settings** and then open the dialog.
  2. Click the **Advanced** tab, and in the **Performance** section, click **Settings**.
  3. In the **Virtual memory** section, click the **Change** button.
  4. Clear the checkbox **Automatically manage paging file size for all drives**. The system should have already set up your paging file on the `C:\` drive, and you need to move it.
  5. Click **C:** and then click the **No paging file** radio button.
  6. Click the **Set** button.
  7. To create the new paging file, click the **P:** drive, and then click the **System managed size** radio button.
  8. Click the **Set** button.
  9. Click **OK** three times to exit the advanced system properties.

Microsoft Support has published [additional tips for virtual memory settings](http://windows.microsoft.com/en-au/windows/change-virtual-memory-size#1TC=windows-7).




### Setting the power profile

Set the power profile to `High-Performance` instead of `Balanced`.

  1. From the **Start** menu, search for "Choose a Power Plan", and then open the power options.
  2. Select the **High Performance** radio button.
  3. Exit the dialog.



## Configuring SQL Server

Use SQL Server Management Studio to perform most administrative tasks. The preconfigured images for SQL Server come with Management Studio already installed. Launch Management Studio and then click **Connect** to connect to the default database.

### Moving the data and log files

The preconfigured image for SQL Server comes with everything installed on the `C:\` drive, including the system databases. To optimize your setup, move those files to the new `D:\` drive you created. Also remember to create all new databases on the `D:\` drive. Because you are using an SSD, you don't need to store the data files and log files on separate disk partitions.

There are two ways to move the installation to the secondary disk: using the installer or moving the files manually.

#### Using the installer

To use the installer, run `c:\setup.exe` and select a new installation path on your secondary disk.

#### Moving the files manually

Move the system databases and configure SQL Server to save the data and log files on the same volume:

  1. Create a new folder named `D:\SQLData`.
  2. Open a Command Window.
  3. Enter the following command to grant full access to `NT Service\MSSQLSERVER`:
         
         icacls D:\SQLData /Grant "NT Service\MSSQLServer:(OI)(CI)F"
         

  4. Use Management Studio and the following guides to [move your system databases](https://msdn.microsoft.com/en-us/library/ms345408\(v=sql.120\).aspx) and [change the default file locations](https://msdn.microsoft.com/en-us/library/dd206993.aspx) for new databases.

  5. If you plan on using **Report Server** features, move the **ReportServer** and **ReportServerTempDB** files as well.


**Important:** Don't modify the `tempdb` files yet because you must first change some permission settings and then move the DB to the Local SSD volume.

After you move the primary configuration database files and restart, you need to configure the system to point to the new location for the model and MSDB databases. Here is a helper script to run in Management Studio:
    
    
    ALTER DATABASE model MODIFY FILE ( NAME = modeldev , FILENAME = 'D:\SQLData\model.mdf' )
    ALTER DATABASE model MODIFY FILE ( NAME = modellog , FILENAME = 'D:\SQLData\modellog.ldf' )
    ALTER DATABASE msdb MODIFY FILE ( NAME = MSDBData , FILENAME = 'D:\SQLData\MSDBData.mdf' )
    ALTER DATABASE msdb MODIFY FILE ( NAME = MSDBlog , FILENAME = 'D:\SQLData\MSDBLog.ldf' )
    

After you execute these commands:

  1. Use the `services.msc` snap-in to stop the SQL Server database service.
  2. Use the Windows file explorer to move the physical files from the `C:\` drive where the `master` database was located to the `D:\SQLData` directory.
  3. Start the SQL Server database service.



### Setting system permissions

After moving the system databases, modify some additional settings, starting with permissions for the Windows user account created to run your SQL Server process, which is named `NT Service\MSSQLSERVER`.

#### Granting the `Lock Pages in Memory` permission

The group policy `Lock Pages in Memory` permission prevents Windows from moving pages in physical memory to virtual memory. To keep physical memory free and organized, Windows tries to swap old, rarely modified pages to the virtual-memory paging file on disk.

SQL Server stores important information in memory, such as table structures, execution plans, and cached queries. Some of this information rarely changes, so it becomes a target for the paging file. If this information gets moved to the paging file, SQL Server performance can degrade. Granting the group policy `Lock Pages in Memory` permission for SQL Server's service account prevents this swapping.

Follow these steps:

  1. Click **Start** and then search for **Edit Group Policy** to open the console.
  2. Expand **Local Computer Policy > Computer Configuration > Windows Settings > Security Settings > Local Policies > User Rights Assignment**.
  3. Search for and then double-click **Lock pages in memory**.
  4. Click **Add User or Group**.
  5. Search for "NT Service\MSSQLSERVER".
  6. If you see multiple names, double-click the **MSSQLSERVER** name.
  7. Click **OK** twice.
  8. Keep the **Group Policy Editor** console open.



![Lock pages](https://docs.cloud.google.com/static/compute/docs/tutorials/images/high-perf-sql-lock-pages.png)

**Important:** After completing these steps and restarting SQL Server, you can verify the setting is working by viewing the SQL Server log. The log contains an entry such as, "Using locked pages in the memory manager."

#### Granting the `Perform volume maintenance tasks` permission

By default, when an application requests a slice of disk space from Windows, the operating system locates an appropriately sized chunk of disk space, and then zeroes out the entire chunk of disk, before handing it back to the application. Because SQL Server is good at growing files and filling disk space, this behavior is not optimal.

There is a separate API for allocating disk space to an application, often referred to as _instant file initialization_. Unfortunately, this setting only works for data files, but you will learn in an upcoming section about log-file growth. Instant file initialization requires the service account running the SQL Server process to have another group policy permission, called `Perform volume maintenance tasks`.

  1. In the **Group Policy Editor** , search for "Perform volume maintenance tasks".
  2. Add the "NT Service\MSSQLSERVER" account as you did in the previous section.
  3. Restart the SQL Server process to activate both settings.



### Setting up `tempdb`

It used to be a best practice to optimize the SQL Server CPU usage by creating one `tempdb` file per CPU. However, because CPU counts have grown over time, following this guideline can cause performance to decrease. As a good starting point, use 4 `tempdb` files. As you measure your system's performance, in rare cases you might need to incrementally increase the number of `tempdb` files to a maximum of 8.

You can run a Transact-SQL (T-SQL) script inside SQL Server Management Studio to move the `tempdb` files to a folder in the `p:` drive.

  1. Create the directory `p:\tempdb`.
  2. Grant full security access to the "NT Service\MSSQLSERVER" user account:
         
         icacls p:\tempdb /Grant "NT Service\MSSQLServer:(OI)(CI)F"
         

  3. Run the following script inside SQL Server Management Studio, to move the `tempdb` data file and log file:
         
         USE master
         GO
         ALTER DATABASE [tempdb] MODIFY FILE (NAME = tempdev, FILENAME = 'p:\tempdb\tempdb.mdf')
         GO
         ALTER DATABASE [tempdb] MODIFY FILE (NAME = templog, FILENAME = 'p:\tempdb\templog.ldf')
         GO
         

  4. Restart SQL Server.

  5. Run the following script to modify the file sizes and create three additional data files for the new `tempdb`.
         
         ALTER DATABASE [tempdb] MODIFY FILE (NAME = tempdev, FILENAME = 'p:\tempdb\tempdb.mdf', SIZE=8GB)
         ALTER DATABASE [tempdb] MODIFY FILE (NAME = templog, FILENAME = 'p:\tempdb\templog.ldf' , SIZE = 2GB)
         ALTER DATABASE [tempdb] ADD FILE (NAME = 'tempdev1', FILENAME = 'p:\tempdb\tempdev1.ndf' , SIZE = 8GB, FILEGROWTH = 0);
         ALTER DATABASE [tempdb] ADD FILE (NAME = 'tempdev2', FILENAME = 'p:\tempdb\tempdev2.ndf' , SIZE = 8GB, FILEGROWTH = 0);
         ALTER DATABASE [tempdb] ADD FILE (NAME = 'tempdev3', FILENAME = 'p:\tempdb\tempdev3.ndf' , SIZE = 8GB, FILEGROWTH = 0);
         GO
         

If you use SQL Server 2016, there are 3 additional `tempdb` files to remove after you do the previous steps:
         
         ALTER DATABASE [tempdb] REMOVE FILE temp2;
         ALTER DATABASE [tempdb] REMOVE FILE temp3;
         ALTER DATABASE [tempdb] REMOVE FILE temp4;
         

  6. Restart SQL Server again.

  7. Delete the `model`, `MSDB`, `master`, and `tempdb` files from the original location on the `C:\` drive.




You successfully moved your `tempdb` files onto the Local SSD disk partition. This move carries some risks, mentioned earlier, but if they are lost for any reason,SQL Server rebuilds the `tempdb` files. Moving `tempdb` gives you the added performance of the Local SSD, and decreases the IOPS used on your Persistent Disk volumes.

**Caution:** Local SSD is not intended for storage of permanent or critical data, because the disk is pinned to the local host. Therefore, use Local SSD only for temporary storage. In some cases, if you shut down Windows from within the instance, the Local SSD disk is also removed, and you have to delete and recreate your instance.

#### Setting `max degree of parallelism`

The recommended default setting for `max degree of parallelism` is to match it to the number of CPUs on the server. However, there is a point where executing a query in 16 or 32 parallel chunks and merging the results is much slower than running it in a single process. If you are using a 16- or 32-core instance, you can set the `max degree of parallelism` value to 8 using the following T-SQL:
    
    
    USE master
    GO
    EXEC sp_configure 'show advanced options', 1
    GO
    RECONFIGURE WITH OVERRIDE
    GO
    EXEC sp_configure 'max degree of parallelism', 8
    GO
    RECONFIGURE WITH OVERRIDE
    GO
    

#### Setting `max server memory`

This setting defaults to a very high number, but you should set it to the number of megabytes of available physical RAM, minus a couple gigabytes for operating system and overhead. The following T-SQL example adjusts `max server memory` to 100 GB. Modify it to adjust the value to match your instance. Review the [Server memory server configuration options](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/server-memory-server-configuration-options?view=sql-server-2017) document for more information.
    
    
    EXEC sp_configure 'show advanced options', 1
    GO
    RECONFIGURE WITH OVERRIDE
    GO
    exec sp_configure 'max server memory', 100000
    GO
    RECONFIGURE WITH OVERRIDE
    GO
    

### Finishing up

Restart the instance one more time to make sure all of the new settings take effect. Your SQL Server system is configured and you are ready to create your own databases and start testing your specific workloads. Review the [SQL Server Best Practices guide](https://docs.cloud.google.com/compute/docs/instances/sql-server/best-practices) for more information on operational activities, other performance considerations, and Enterprise Edition capabilities.

## Clean up

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



### Deleting instances

To delete a Compute Engine instance: 

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the checkbox for the instance that you want to delete. 
  3. To delete the instance, click more_vert **More actions** , click **Delete** , and then follow the instructions. 



### Deleting Persistent Disk volumes

To delete the Persistent Disk:

  1. In the Google Cloud console, go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. Select the checkbox next to the name of the disk you want to delete.

  3. Click the **Delete** button at the top of the page.




## What's next

  * [Load test your SQL Server instance](https://docs.cloud.google.com/compute/docs/tutorials/load-testing-sql-server-hammerdb).
  * Review the [SQL Server Best Practices guide](https://docs.cloud.google.com/compute/docs/instances/sql-server/best-practices).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
