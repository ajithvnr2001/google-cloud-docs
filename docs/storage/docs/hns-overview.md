---
url: https://docs.cloud.google.com/storage/docs/hns-overview/
title: Hierarchical namespace \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:07.687160+00:00
---

# Hierarchical namespace  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/hns-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Hierarchical namespace Stay organized with collections  Save and categorize content based on your preferences. 

Hierarchical namespace is a capability offered by Cloud Storage that lets you organize objects into folders and store your data in a logical file system structure, making it easier to streamline data management tasks. Hierarchical namespace provides the high-performance directory semantics and atomic folder operations that are required to accelerate data-intensive AI/ML and analytics workloads.

This page provides an overview of hierarchical namespace and its use cases, including its capabilities, benefits, and limitations.

## How it works

To use folders in a bucket, you must enable hierarchical namespace when you create the bucket. Your bucket's hierarchical namespace setting can't be changed after the bucket is created. For information about enabling hierarchical namespace for your bucket, see [Create and manage buckets with hierarchical namespace enabled](https://docs.cloud.google.com/storage/docs/create-hns-bucket).

The following diagram shows an example of a bucket with hierarchical namespace enabled where objects are organized in a hierarchical structure of folders. A folder in a bucket with hierarchical namespace enabled can contain both objects and child folders.

![Figure 1. Bucket hierarchy with folders and objects.](https://docs.cloud.google.com/static/storage/images/hns-intro.svg)**Figure 1.** Bucket hierarchy with folders and objects.

## Capabilities and benefits

Hierarchical namespace provides the following capabilities and benefits:

  * **Higher initial queries per second (QPS)** : Buckets with hierarchical namespace enabled offer up to 8 times higher initial QPS limits for reading and writing objects compared to buckets without hierarchical namespace enabled. The higher initial QPS makes it easier to scale data-intensive workloads and provides enhanced throughput. For information about performance optimization methods while using folders in buckets with hierarchical namespace enabled, see [Folder management](https://docs.cloud.google.com/storage/docs/hns-buckets-best-practices#folder-management).

  * **Ability to use folders** : [Folders](https://docs.cloud.google.com/storage/docs/folders-overview) serve as a container for objects and child folders, enabling a real directory structure within Cloud Storage buckets. Storing your data in a folder structure enhances performance, ensures consistency, and simplifies the management of data-intensive and file-oriented workloads.

[Folder operations](https://docs.cloud.google.com/storage/docs/folders-overview#folder-operations) provide reliability and management capabilities, including creating, listing, deleting, and atomic renaming.

    * **Renaming folders** : The rename folders operation helps you to atomically rename the path of a folder and its underlying folders without deleting any objects. This technique is efficient and time-saving, especially for large folders with multiple objects.

    * **Listing folders** : The list folders operation lists all folders in the bucket or underneath a specific folder, helping you manage and understand the structure of your stored data.




## When should you use hierarchical namespace?

You should consider enabling hierarchical namespace when working with applications that expect a file system hierarchy and semantics. Hierarchical namespace is beneficial for data-intensive tasks like analytics and AI/ML workloads. Here are some common scenarios where you should consider using hierarchical namespace:

  * **Hadoop based processing** : Hadoop and Spark workloads traditionally expect a file system storage structure and time-based naming for files and folders. Hierarchical namespace integrates with the [Cloud Storage connector](https://docs.cloud.google.com/dataproc/docs/concepts/connectors/cloud-storage) to provide enhanced throughput and atomic folder renames, improving data integrity and consistency for many data processing pipelines.

  * **File-oriented workloads processing** : Workloads such as batch analytics processing, financial services, or high performance computing are structured into partitions based on a hierarchy of folders and files. Hierarchical namespace helps to manage these environments with a dedicated API for folder management. Additionally, hierarchical namespace simplifies managing folders that contain other folders and objects. With a single API command, you can swiftly rename a folder along with all its contents, saving valuable time and resources.

  * **AI/ML processing** : AI/ML tools such as TensorFlow, Pandas, and PyTorch expect file system access control and semantics. Hierarchical namespace, especially when combined with Cloud Storage FUSE, delivers increased throughput and efficient data access. As a result, hierarchical namespace enhances the performance and reliability of the ML model iteration.




Before enabling hierarchical namespace for your bucket, you should consider the limitations of hierarchical namespace. For information about hierarchical namespace limitations, see Limitations.

## Benefits of hierarchical namespace

When you enable Hierarchical namespace for your buckets, you can do the following:

  * **Optimize organization** : You can organize your data into a hierarchical folder structure, that helps you to manage and locate files or datasets.

  * **Establish a file system ecosystem** : Hierarchical namespace introduces file system features such as folders, folder renaming, and folder listing, which are beneficial for file-oriented applications, including the Hadoop ecosystem and AI/ML workloads.

  * **Performance improvement** : By scaling data-intensive workloads to handle higher throughput, you can enhance the overall performance of your application.




## Platform support

Buckets with hierarchical namespace support the following Cloud Storage platform capabilities:

  * All Cloud Storage object APIs and widely-used Cloud Storage features. For details about unsupported features, see Limitations.

  * Data transfer from a standard bucket to a bucket with hierarchical namespace using Storage Transfer Service.

  * Integration with the following products:

    * Cloud Storage Connector, maintained by Managed Service for Apache Spark for Hadoop workloads. For more information, see [Use hierarchical namespace enabled buckets for Hadoop workloads](https://docs.cloud.google.com/storage/docs/hns-hadoop-workloads).

    * [Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview) for file system-like bucket access using clients.

    * [GCSFS Python library](https://github.com/fsspec/gcsfs) for Pythonic file system-like bucket access. Hierarchical namespace is supported by the GCSFS Python library versions 2026.3.0 and later.




## Compatibility with Cloud Storage operations and features

Buckets with hierarchical namespace enabled interact with Cloud Storage operations differently than buckets without hierarchical namespace.

### Interactions with object operations

Buckets with hierarchical namespace enabled handle [object](https://docs.cloud.google.com/storage/docs/objects) operations in the following ways:

  * Operations like [`Upload`](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/insert), [`Rewrite`](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/rewrite), and [`Compose`](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/compose) automatically create any missing parent folders, as long as you have the necessary permissions. As a result, you don't need to pre-create folders before uploading objects.
  * While folders can be created automatically during object operations, you need to delete them explicitly using the [`DeleteFolder`](https://docs.cloud.google.com/storage/docs/json_api/v1/folders/delete) operation.
  * When using the [`ListObjects`](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/list) operation with the `delimiter` parameter, buckets return each child folder as a `prefix.` However, empty folders are excluded by default. To include empty folders, similar to a typical file system listing, you must set the `includeFoldersAsPrefixes` parameter. For information about performance optimization methods while listing objects in buckets with hierarchical namespace enabled, see [Listing objects](https://docs.cloud.google.com/storage/docs/hns-buckets-best-practices#listing-objects).



### Interactions with bucket operations

The following sections describe how bucket operations are handled when hierarchical namespace is enabled.

  * You can list all buckets with hierarchical namespace enabled, regardless of their storage layout. A bucket's storage layout describes how objects are arranged within a bucket, either in a flat namespace or a hierarchical namespace. For instructions on viewing a bucket's storage layout, see [Get a bucket's storage layout](https://docs.cloud.google.com/storage/docs/getting-storage-layout). To list all buckets, follow the instructions detailed in [List buckets](https://docs.cloud.google.com/storage/docs/listing-buckets).

  * You can [delete buckets](https://docs.cloud.google.com/storage/docs/deleting-buckets) with hierarchical namespace enabled as long as the bucket is empty. Empty buckets contain no objects or [managed folders](https://docs.cloud.google.com/storage/docs/managed-folders). Empty buckets can contain empty folders (with no objects within).




### Interactions with Object Lifecycle Management operations

[Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle) lets you automate actions on objects based on conditions, such as age or prefix. However, Object Lifecycle Management rules can behave differently in buckets with hierarchical namespace and in buckets with a flat namespace due to the `RenameFolder` operation:

  * **Object Lifecycle Management rules for buckets with a flat namespace** : The renaming operation involves renaming every object using tools by copying every object to a destination location and deleting the original object from the source location. As a result, new objects are created with new creation times at the destination location. If [age-based Object Lifecycle Management rules](https://docs.cloud.google.com/storage/docs/lifecycle#age) are applied for the destination location, they won't apply to the new objects immediately as their creation times are reset.

  * **Object Lifecycle Management rules for buckets with hierarchical namespace enabled** : Renaming a folder operates at the folder level, without having to rename every single object. As a result, the creation time of the objects is preserved, meaning the [age-based Object Lifecycle Management rules](https://docs.cloud.google.com/storage/docs/lifecycle#age) are applied to renamed objects immediately if they meet the age criteria.




## Access control for folders with associated managed folders

In Cloud Storage, a folder is the actual directory that holds your data, while a [managed folder](https://docs.cloud.google.com/storage/docs/managed-folders) is a separate, specialized resource used to apply IAM permissions to the directory. To control access to a folder and the resources within it, you create an **associated managed folder** and set IAM policies on the associated managed folder. An associated managed folder is a managed folder that has the same name and path as your actual folder.

The associated managed folder acts as an administrative layer over the directory created by the folder, meaning that a folder and its associated managed folder are inextricably linked. For example, if you delete a folder that has an associated managed folder, the associated managed folder also gets deleted along with its IAM policies. For details about how folder operations affect associated managed folders, see [Interactions between folders and associated managed folders](https://docs.cloud.google.com/storage/docs/folders-overview#associated-managed-folders).

### Naming for folders with associated managed folders

Both [folder naming rules](https://docs.cloud.google.com/storage/docs/folders-overview#considerations) and [managed folder naming rules](https://docs.cloud.google.com/storage/docs/managed-folders#managed_folder_names) apply when creating folders with associated managed folders. Folder names can be nested up to 50 levels deep, but managed folder names can only be nested up to 15 levels deep. The maximum size for a managed folder name is 512 bytes when UTF-8 encoded. This means if you plan to create a folder and an associated managed folder for it, the folder can only have 15 stacked child folders, and its maximum name size is 512 bytes when UTF-8 encoded.

## Pricing

For pricing information, refer to [Cloud Storage pricing](https://docs.cloud.google.com/storage/pricing).

## Limitations

The following are the limitations of hierarchical namespace:

  * You must choose whether or not to use hierarchical namespace when you create the bucket; your bucket's hierarchical namespace setting can't be changed after the bucket is created.

  * In order to enable hierarchical namespace, a bucket must also enable [ uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access).

  * In buckets with hierarchical namespace enabled, the maximum size of an object's name is 1024 bytes when UTF-8 encoded, where the folder name segment and the base name segment each have a limit of 512 bytes when UTF-8 encoded. In flat namespace buckets, object names don't contain folder name segments and have a limit of 1024 bytes when UTF-8 encoded. For more information about object name limits, see [About objects](https://docs.cloud.google.com/storage/docs/objects).

  * Folder names can be [nested up to 50 levels deep](https://docs.cloud.google.com/storage/docs/folders-overview#considerations) (or 15 levels deep if the folder has an associated managed folder).

  * The following Cloud Storage capabilities are not supported for buckets that use hierarchical namespace:

    * Bucket Lock
    * Bucket relocations with write downtime
    * Cross-bucket replication
    * Object holds
    * Object-level access control lists (ACLs)
    * Object Retention Lock
    * Object Versioning



## What's next

  * [Create buckets with hierarchical namespace enabled](https://docs.cloud.google.com/storage/docs/create-hns-bucket).
  * [Create and manage folders](https://docs.cloud.google.com/storage/docs/create-folders).
  * [Rename folders](https://docs.cloud.google.com/storage/docs/rename-hns-folders).
  * [Use hierarchical namespace for Hadoop workloads](https://docs.cloud.google.com/storage/docs/hns-hadoop-workloads).
  * [Optimize performance](https://docs.cloud.google.com/storage/docs/hns-buckets-best-practices).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud Storage performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud Storage free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
