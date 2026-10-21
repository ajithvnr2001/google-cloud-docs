---
url: https://docs.cloud.google.com/sql/docs/mysql/issues-updating-storage-capacity/
title: Issues updating storage capacity \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:53.282491+00:00
---

# Issues updating storage capacity  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/issues-updating-storage-capacity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Issues updating storage capacity Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/issues-updating-storage-capacity "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/issues-updating-storage-capacity "View this page for the SQL Server database engine")

This page describes common error messages you might receive when attempting to reduce or [shrink instance storage capacity](https://docs.cloud.google.com/sql/docs/mysql/about-storage-shrink).

### Storage shrink fails for C4, C4A and N4 machine types

The following error might occur when you try to apply a storage shrink operation to a C4, C4A or N4 machine type:
    
    
      ERROR: (gcloud.sql.instances.perform-storage-shrink) HTTPError 400: Invalid
      request: Requested provisioned IOPS is too high for the machine type and/or data disk size.
    

The C4, C4A and N4 machine types use [Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-throughput), which lets users tune disk throughput and IOPS values. If you try to shrink the disk size to a point where the configured throughput and IOPS values become invalid, then the disk shrink operation fails and returns an error.

In this example error message, the requested instance IOPS value is greater than the new small disk maximum IOPS value and the operation fails.

To resolve this issue, recalculate the target storage size you want to use based on your machine's [Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-throughput) limitations and run the storage shrink operation again.

### Operations fail for a read pool

The following errors occur when you try to run any storage shrink related operation on a read pool:

#### Example 1
    
    
    gcloud sql instances perform-storage-shrink READ_POOL_NAME
    
    ERROR: (gcloud.sql.instances.perform-storage-shrink) HTTPError 400: Invalid
    request: Requested operation is not supported on a read pool.
    

Storage shrink operations aren't supported for read pools or read pool nodes.

#### Example 2
    
    
    gcloud sql instances get-disk-shrink-config READ_POOL_NAME
    
    ERROR: (gcloud.sql.instances.get-storage-shrink-config) HTTPError 400: Invalid
    request: Requested operation is not supported on a read pool.
    

You can't check the storage shrink configuration of a read pool, read pool node, or replica.

You can, however, check the available storage capacity of the associated primary instance.

### Can't check cancellation status

The following error might occur when you try to check the status of a cancellation request for a storage shrink operation:
    
    
      {
        "kind": "sql#operation",
        "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/example_instance",
        "status": "RUNNING",
        "user": "user@example.com",
        "insertTime": "2023-12-18T22:54:11.663Z",
        "startTime": "2023-12-18T22:54:12.047Z",
        "error": {
          "kind": "sql#operationErrors",
          "errors": [
            {
              "kind": "sql#operationError",
              "code": "CANCEL_ERROR",
              "message": "The UPDATE operation 490cdbe6-8b75-415c-99c1-ccc80000004f can not be cancelled."
            }
          ]
        },
        "operationType": "UPDATE",
        "name": "OPERATION_ID",
        "targetId": "example_instance",
        "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
        "targetProject": "PROJECT_ID"
      }
    

To resolve this issue, follow these steps:

  1. This error message might indicate that the cancellation request is almost complete. Try checking the operation status again in a few minutes.
  2. If you still receive the same error message, reach out to [Cloud SQL support](https://docs.cloud.google.com/sql/docs/mysql/getting-support) for assistance.
  3. When successful, a message similar to the following is returned:
         
         {
           "kind": "sql#operation",
           "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/example_instance",
           "status": "DONE",
           "user": "user@example.com",
           "insertTime": "2023-12-18T22:54:11.663Z",
           "startTime": "2023-12-18T22:54:12.047Z",
           "error": {
             "kind": "sql#operationErrors",
             "errors": [
               {
                 "kind": "sql#operationError",
                 "code": "CANCEL_SUCCESSFUL",
                 "message": "The UPDATE operation is canceled."
               }
             ]
           },
           "operationType": "UPDATE",
           "name": "OPERATION_ID",
           "targetId": "example_instance",
           "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
           "targetProject": "PROJECT_ID"
         }
         




### Storage shrink fails

The following error might occur when you try to run a storage shrink operation:
    
    
      There is a pending blocking operation for instance: INSTANCE_NAME
    

This error message might indicate that another operation is still running, such as the following:

  * Backup operation
  * Import operation
  * A previous storage shrink operation on the instance
  * A storage shrink operation still running on a primary instance associated with the read replica you want to modify



To resolve the issue, wait for the previous operation to complete.

If a previous `IMPORT` operation is stuck, contact [Cloud SQL support](https://docs.cloud.google.com/sql/docs/mysql/getting-support) to request help to cancel the operation.

For more information, see [Limitations](https://docs.cloud.google.com/sql/docs/mysql/about-storage-shrink#limitations).

### Invalid storage size for a primary instance

The following errors might occur when you try to run a storage shrink operation on a primary instance and the requested target size is invalid:

#### Example 1
    
    
      Invalid target storage size SIZE. Target storage
      size should be at least 10GB, which is the minimum storage size for a
      Cloud SQL instance.
    

  * The requested target size needs to be greater than or equal to the minimum allowed storage size for the instance.

To resolve the issue, specify a larger target storage size and run the operation again.

For more information, see [Limitations](https://docs.cloud.google.com/sql/docs/mysql/about-storage-shrink#limitations).




#### Example 2
    
    
      Instance INSTANCE_NAME cannot shrink storage further
      because the storage size is 10GB and the minimum storage size for a Cloud SQL
      instance is 10GB.
    

  * The requested target size is too small. If the requested target size for `--storage-size` is already at the minimum size of 10 GB, you can't shrink it further.

To resolve the issue, specify a larger target storage size and run the operation again.

For more information, see [Limitations](https://docs.cloud.google.com/sql/docs/mysql/about-storage-shrink#limitations).




#### Example 3
    
    
      ERROR: (gcloud.sql.instances.perform-storage-shrink) argument --storage-size: VALUE
      must be greater than or equal to 10GB; received: SIZE
    

  * If the requested target size for `--storage-size` is too small, run the following command on the primary instance to get the minimum allowed storage capacity:
        
        gcloud sql instances get-storage-shrink-config PRIMARY_INSTANCE_NAME
        

The response includes a value for `minimalTargetSizeGb`. You can use this value for the `--storage-size` parameter and run the operation again.




#### Example 4
    
    
      Invalid target storage size SIZE. Target storage
      size should be smaller than present storage size CURRENT_SIZE.
    

  * If the requested target size for `--storage-size` is too large this indicates that the value is bigger than the current storage size of the primary instance and you need to use a smaller value.

If you want to have a larger disk, [edit the instance](https://docs.cloud.google.com/sql/docs/mysql/edit-instance#edit_an_instance) first and try the operation again.




#### Example 5
    
    
      Requested storage size is too close to current storage usage, request storage
      size should be minimum SIZEGB.
    

  * If the requested target size is too close to the existing storage size, then you need to modify the value and run the operation again. Options for modification include the following:

    * Increase the target value.
    * Set the target value to be the same as the `minimalTargetSizeGb` value.

For more information, see [Limitations](https://docs.cloud.google.com/sql/docs/mysql/about-storage-shrink#limitations).




### Invalid storage size for a replica

The following errors might occur when you try to run a storage shrink operation on a replica and the requested target size is invalid:

#### Example 1
    
    
      Cannot shrink storage further for replica INSTANCE_NAME
      because the minimum storage size for a Cloud SQL replica is 10GB.
    

If the requested target size for `--storage-size` is already at the minimum size of 10GB, you can't shrink it further.

To resolve the issue, specify a target storage size that falls within an acceptable range and run the operation again.

For more information, see [Limitations](https://docs.cloud.google.com/sql/docs/mysql/about-storage-shrink#limitations).

#### Example 2
    
    
      Cannot shrink storage further for replica REPLICA_INSTANCE_NAME
      because current replica storage size isn't greater than primary instance
      PRIMARY_INSTANCE_ID storage size. If you want to shrink
      both primary and replica instance, please shrink primary instance first.
    

A read replica can't, at any time, have a smaller storage capacity than its associated primary instance. If you want to shrink the storage capacity of a replica, you must complete a storage shrink operation on its associated primary instance first.

For more information, see [Limitations](https://docs.cloud.google.com/sql/docs/mysql/about-storage-shrink#limitations).

### Insufficient storage space

The following error might occur when you try to set the storage shrink size:
    
    
      {
        "error": {
          "code": 400,
          "message": "Invalid target storage size TARGET_SIZE. ...",
          "errors": ...
      }
    
    

This error message might indicate that you don't have enough storage on the instance.

To resolve this issue, follow these steps:

  1. Make sure to follow all storage shrink steps.
  2. Make sure that the target storage size is larger than the minimum target size you previously set.



### Storage shrink fails after 10 days

Storage shrink operations time out if the operation persists for more than 10 days.

To resolve the issue, upgrade the CPU of the instance to reduce overall operation time.

### Storage shrink fails with internal error

Unsuccessful storage shrink operations might return a message indicating an internal error.

To resolve the issue, reach out to [Cloud SQL support](https://docs.cloud.google.com/sql/docs/mysql/getting-support) for assistance.

### Storage shrink `gcloud` command fails after 10 minutes

The following error might occur when you try to shrink the storage size of an instance using the [`gcloud sql instances`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances) command:
    
    
      Performing a storage size decrease on a Cloud SQL instance....failed.
    

You might receive this error message if the operation lasts longer than 10 minutes.

To resolve the issue, add the [`--async`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create#--async) flag to the end of the command to wait for the operation asynchronously.

## What's next

  * [About storage shrink](https://docs.cloud.google.com/sql/docs/mysql/about-storage-shrink)
  * [Shrink instance storage capacity](https://docs.cloud.google.com/sql/docs/mysql/shrink-instance-storage-capacity)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
