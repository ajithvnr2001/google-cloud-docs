---
url: https://docs.cloud.google.com/filestore/docs/create-instance-console/
title: Quickstart: Create a Filestore instance using the Google Cloud console \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:38.702194+00:00
---

# Quickstart: Create a Filestore instance using the Google Cloud console  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/create-instance-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a Filestore instance using the Google Cloud console

This quickstart shows you how to perform basic operations in Filestore using this Google Cloud console. In the quickstart, you will:

  * Create a Filestore instance.
  * Mount the file share from that instance on a Compute Engine client VM instance.
  * Create a file on the mounted file share.
  * Delete the Filestore instance.



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Filestore API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=file.googleapis.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Filestore API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=file.googleapis.com)


**Important:** If you choose to use an existing project with this quickstart, it must have a non-legacy default VPC network with unmodified firewall rules. Production Filestore instances can have other network configurations, see [Networking](https://docs.cloud.google.com/filestore/docs/networking) for more information.

### Required roles

To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles on your project: 

  * Create and manage Filestore instances: [Cloud Filestore Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.editor) (`roles/file.editor`) 
  * Create and manage Compute Engine instances: [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) 
  * Create, modify, and delete networking resources, except for firewall rules: [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) 
  * Run operations on IAM service accounts: [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) 
  * Manage network and related Google Cloud resources: Network Administrator (`roles/iam.networkAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Create a Compute Engine VM instance to be the client

  1. In the Google Cloud console, go to the VM Instances page.

[Go to the Compute Engine instances page](https://console.cloud.google.com/compute/instances)

  2. Click **Create Instance** and configure the instance as follows.

     * Set **Name** to `nfs-client`.
     * Set **Zone** to **us-central1-c**.
     * Keep the default boot disk.
     * In the **Networking** > **Firewall** section, select the **Allow HTTP traffic** checkbox.
     * Keep the network as **default**.
  3. Click **Create** to create the instance.




## Create a Filestore instance

This quickstart shows how to create an instance in the **Regional** tier with custom performance enabled. For details on creating instances, see [create an instance](https://docs.cloud.google.com/filestore/docs/creating-instances).

  1. In the Google Cloud console, go to the Filestore **Instances** page.

[Go Instances](https://console.cloud.google.com/filestore/instances)

  2. Click **Create Instance** and configure the instance as follows:

     * Set **Instance ID** to `nfs-server`.
     * Set **Instance type** to **Regional**.
     * In **Capacity** , enter `1 TiB`.
     * In **Performance** , configure your performance based on the workload and scale. The **Scale performance with capacity** checkbox is checked, so if you change the value in the **Capacity** field, performance scales accordingly.

For more information on configuration options, see [configure performance](https://docs.cloud.google.com/filestore/docs/creating-instances#configure-performance).

**Note:** After activating custom performance for an instance you can't deactivate it for that instance. Instances with activated custom performance are billed according to purchased IOPS. For details, see [ configure custom performance](https://docs.cloud.google.com/filestore/docs/custom-performance#enable-custom-performance) and [ Filestore pricing](https://docs.cloud.google.com/filestore/pricing).
     * Set **Protocol** to **NFSv4.1**.

     * Set the **IP stack type** to **IPv6**.

     * Set **Region** to **us-central1**.

     * For **VPC network** , select a network from the list. For more information on creating VPC networks, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).

**Note:** When you create a zonal or regional instance using Google Cloud console, you must use Private Service Connect as the connectivity method and create a service connection policy. For more information, see [Create a Filestore instance with Private Service Connect](https://docs.cloud.google.com/filestore/docs/configure-psc). If you use gcloud CLI or Filestore API, you can also use VPC Network Peering with either direct peering or private services access.
     * Set **File share name** to `vol1`.

     * Set **Allocated IP range** to **Use an automatically allocated IP range**.

     * Set **Access controls** to **Grant access to all clients**.

  3. Click **Create**.




## Mount the Filestore file share on the client

  1. In the Google Cloud console, go to the VM Instances page.

[Go VM instances](https://console.cloud.google.com/compute/instances)

  2. In the list of VM instances, click the **SSH** button for **nfs-client** to open a terminal window connected to that instance.

  3. Install NFS by running the following commands:
         
         sudo apt-get -y update &&
         sudo apt-get -y install nfs-common
         

  4. Make a mount directory for the Filestore file share by running the following command:
         
         sudo mkdir -p /mnt/test
         

  5. Mount the file share by running the `mount` command and specifying the Filestore instance IP address and file share name:
         
         sudo mount MOUNT-POINT-DIRECTORY /mnt/test
         

where:

MOUNT-POINT-DIRECTORY is the path to the directory where the Filestore file share is mounted. For example: `10.0.0.2:/vol1`

  6. Optional: Confirm that the Filestore file share is mounted:
         
         df -h --type=nfs
         

  7. Make the file share accessible by changing the permissions:
         
         sudo chmod go+rw /mnt/test
         

**Important:** We recommend setting more specific permissions in a production environment. For more information, see [Configuring access on a file share](https://docs.cloud.google.com/filestore/docs/access-control#fileshare-access).



## Create a file on the file share

  1. In the terminal window that is connected to the **nfs-client** instance, create a file named `testfile` by running the following command:
         
         echo 'This is a test' > /mnt/test/testfile
         

  2. Confirm that the file was created by running the following command:
         
         ls /mnt/test
         

and verifying that `testfile` is listed.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

### Delete the Google Cloud project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the Filestore instance

  1. In the Google Cloud console, go to the Filestore Instances page.

[Go to the Filestore instances page](https://console.cloud.google.com/filestore/instances)

  2. Click the **`nfs-server`** instance ID to open the instance details page.

  3. Click **Delete** _delete_.

  4. When prompted, type the instance ID.

  5. Click **Delete**.




### Delete the Compute Engine instance

  1. In the Google Cloud console, go to the Filestore Instances page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Select the checkbox next to the **`nfs-client`** instance name.

  3. Click **Delete** _delete_.

  4. When prompted, click **Delete** again.




## What's next

  * Read the [Filestore Overview](https://docs.cloud.google.com/filestore/docs/overview) to learn more about the basics of Filestore.
  * Set up a Filestore instance on your own by following the instructions at [Creating Instances](https://docs.cloud.google.com/filestore/docs/creating-instances).
  * Read the [Access Control](https://docs.cloud.google.com/filestore/docs/access-control) page to learn how to control access to Filestore operations and the resources on an instance.
  * See how to [copy data to or from a Filestore instance](https://docs.cloud.google.com/filestore/docs/copying-data).
  * See how to [transfer large datasets from Cloud Storage to Filestore](https://docs.cloud.google.com/filestore/docs/transfer-data-from-gcs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
