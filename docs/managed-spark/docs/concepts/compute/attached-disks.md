---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/compute/attached-disks/
title: Attach hyperdisks to Managed Service for Apache Spark VMs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:25.362475+00:00
---

# Attach hyperdisks to Managed Service for Apache Spark VMs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/compute/attached-disks/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Attach hyperdisks to Managed Service for Apache Spark VMs Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to attach hyperdisks to virtual machines (VMs) in a Managed Service for Apache Spark cluster. You can configure the disks independently for master, primary worker, and secondary worker node groups. These disks are attached to cluster nodes in addition to the [boot disk](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/dataproc-persistent-disks) and any [local SSDs](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/dataproc-local-ssds) attached to cluster nodes.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. Verify that you have the permissions required to complete this guide. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Managed Service for Apache Spark API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataproc.googleapis.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. Verify that you have the permissions required to complete this guide. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Managed Service for Apache Spark API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataproc.googleapis.com)




### Required roles

Certain IAM roles are required to run the examples on this page. Depending on organization policies, these roles may have already been granted. To check role grants, see [Do you need to grant roles?](https://docs.cloud.google.com/managed-spark/docs/concepts/iam#do_you_need_to_grant_roles).

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

#### User roles

To get the permissions that you need to create a Managed Service for Apache Spark cluster, ask your administrator to grant you the following IAM roles: 

  * [Dataproc Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.editor) (`roles/dataproc.editor`) on the project
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the Compute Engine default service account



#### Service account role

To ensure that the Compute Engine default service account has the necessary permissions to create a Managed Service for Apache Spark cluster, ask your administrator to grant the [Dataproc Worker ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`) IAM role to the Compute Engine default service account on the project. **Important:** You must grant this role to the Compute Engine default service account, _not_ to your user account. Failure to grant the role to the correct principal might result in permission errors. 

## Disk characteristics

Attached disks have the following characteristics:

  * **Lifecycle** : The lifetime of an attached disk matches the lifetime of the VM that it is attached to. Managed Service for Apache Spark creates the disk when it creates the VM and deletes the disk when it deletes the VM.
  * **Immutability** : You cannot update the properties of an attached disk, such as size, IOPS, or throughput, after the cluster is created.
  * **Mounting and usage** : Managed Service for Apache Spark mounts disks at `/mnt/N`, where `N` is a positive integer (for example, `/mnt/1`, `/mnt/2`). HDFS and scratch data, such as shuffle outputs, use the attached disks instead of the boot persistent disk.



## Disk configuration

You can specify the following disk configuration parameters when you attach disks to Managed Service for Apache Spark cluster nodes:

  * **Disk type** \- required: The type of disk to attach to VM instances. The following [hyperdisks](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) are supported:

    * `hyperdisk-balanced`
    * `hyperdisk-extreme`
    * `hyperdisk-ml`
    * `hyperdisk-throughput`

The [`hyperdisk balanced high availability`](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha) type and [persistent](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) disks can't be attached to cluster nodes.

To attach a hyperdisk to a cluster node, the machine type used in the node must support hyperdisks. See [Machine series support for hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support).
  * **Size** \- optional: The size of the disk. The value must be a whole number followed by a `GB` for gigabyte or `TB` for terabyte. For example, `10GB` attaches a 10 gigabyte disk. For more information, see [Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits).

  * **IOPs** \- optional: Indicates the [IOPS](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#hd-performance-limits) to provision for the attached disk. This parameter sets the limit for disk I/O operations per second. For more information, see [Default performance levels](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-performance#default-perf).

  * **Throughput** \- optional: Indicates the [throughput](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#hd-performance-limits) to provision for the attached disk. This parameter sets the limit for throughput in `MiB` per second. For more information, see [Default performance levels](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-performance#default-perf).




## Attach disks to a cluster

You can attach disks when you [create a Managed Service for Apache Spark cluster](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-console#create_a_cluster) using the gcloud CLI or the Dataproc API to specify the disk configurations.

### gcloud CLI

  * To attach disks when you create a cluster, use the `--master-attached-disks`, `--worker-attached-disks`, or `--secondary-worker-attached-disks` flag with the `gcloud dataproc clusters create` command.

  * Each flag accepts a list of disk configurations separated by semicolons. Each disk configuration is a comma-separated list of key-value pairs for `type`, `size`, `iops`, and `throughput` (see Disk configuration).




Example: The following command creates a cluster and attaches two hyperdisks to each primary worker node.
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region=REGION \
        --worker-attached-disks='type=hyperdisk-balanced,size=100GB,iops=5000,throughput=200;type=hyperdisk-throughput,size=9000GB'
    

### API

  * To attach disks, include an [`attachedDiskConfigs`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/InstanceGroupConfig#attacheddiskconfig) array in the `diskConfig` object for the `masterConfig`, `workerConfig`, or `secondaryWorkerConfig` instance group.

  * Provide the configuration in the body of a `clusters.create` API request.




Example: The following JSON snippet shows an `attachedDiskConfigs` array that attaches two hyperdisks.

**Note:** The `diskType` field in `attachedDiskConfigs` is deprecated. Use `type` instead.
    
    
    [
      {
        "type": "hyperdisk-balanced",
        "diskSizeGb": 100,
        "provisionedIops": 5000,
        "provisionedThroughput": 200
      },
      {
        "type": "hyperdisk-throughput",
        "diskSizeGb": 9000
      }
    ]
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
