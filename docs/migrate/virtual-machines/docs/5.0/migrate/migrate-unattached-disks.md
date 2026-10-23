---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrate-unattached-disks/
title: Migrate disks \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:14.494346+00:00
---

# Migrate disks  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrate-unattached-disks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Guides ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle)



Send feedback 

#  Migrate disks Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Migrate to Virtual Machines lets you migrate unattached disks from an AWS source to Persistent Disk volumes on Google Cloud. This feature is useful when you want to migrate your unattached disks, that is, disks that are not connected to any virtual machine (VM) instance to Google Cloud.

## Before you begin

Before you begin the migration process, do the following:

  * [Enable Migrate to Virtual Machines services](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/enable-services) to configure the migration environment on your [migration source](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/architecture#migration_sources_and_targets) and [migration target](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/architecture#migration_targets).
  * [Create an AWS IAM policy](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/create-an-aws-source#create-an-iam-policy) with `ec2:CreateSnapshot` by ensuring that you add `ec2:CreateSnapshot` to the referenced policy.



## Limitations

The following limitations apply:

  * You can only migrate disks from AWS sources.
  * Regional disks and hyperdisk disks are not supported.



## Disk migration process

To migrate unattached disks to Google Cloud, use the following steps:

###  Console 

To migrate unattached disks by using the Google Cloud console, use the following steps.

  1. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  2. Select the **Sources** tab.

  3. From the source drop-down list, select the migration source from which you want to migrate disks.

**Note:** You can migrate unnattached disks only from AWS sources.

Below the drop-down you see the **Source status** of the migration source as follows:

     * **Active** : the source is active and connected to Migrate to Virtual Machines.
     * **Offline** : the source is unavailable.
     * **Pending** : the source is in the process of being connected and verified.

If you don't see any entries in the drop-down list, it indicates that you haven't configured the migration source properly. Review the steps for your migration source settings and try again.

  4. If the source is **Active** , the **Source disks** tab displays all the source disks in the migration source available for migration. Select one or more source disks.

  5. Click **Migration**. The **Create disk migrations** page appears.

  6. Provide the details required for the disk migration. The following table describes these fields detail.

Field name | Description  
---|---  
Disk name | Enter a name for the migrated disk. For more information on the naming rules, see [Naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).  
Target project | The target project in which you want to create the migrated disk. If you've not already added a target project, do so using the instructions given in [Add a target project](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/target-project).   
Zone | Select the zone in which you want to create the migrated disk. See [ Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones).   
Disk type | Select the type of disk. See [ Persistent Disk types](https://docs.cloud.google.com/compute/docs/disks#disk-types).   
Labels | To organize your project, add labels as key-value pairs to your resources. See [Organize resources using labels](https://docs.cloud.google.com/compute/docs/labeling-resources).   
  7. You can now do one of the following:

     * Click **Create** to create the migration. Creating a migration only onboards the disk, however, the disk is not migrated yet. This migration appears in the **Disk migrations** tab. To run the migration, go to the **Disk migrations** tab, select the disk migration you want to run, and click **Run**.

     * Click **Create and run** to create the migration and start the migration immediately.

  8. After the migration completes, the status of the migration is displayed in the **Disk migrations** tab.




###  gcloud 

To migrate unattached disks by using the Google Cloud CLI, run the following command.
    
    
    gcloud alpha compute migration disk-migrations create DISK_MIGRATION_JOB_NAME \
    --source=AWS_SOURCE_NAME \
    --source-volume-id=AWS_VOLUME_ID \
    --location=REGION_ID \
    --target-project=TARGET_PROJECT_RESOURCE_PATH
    

Replace the following:

  * `DISK_MIGRATION_JOB_NAME`: the name of the unnattached disk you want to migrate. For more information on the naming rules, see [Naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).
  * `AWS_SOURCE_NAME`: the AWS source from which you want to import the unnattached disk.
  * `AWS_VOLUME_ID`: the ID of the AWS volume that you want to migrate to Google Cloud.
  * `REGION_ID`: the region to which you want to migrate the unnattached disk to.
  * `TARGET_PROJECT`: the target project to which you want to migrate the unnattached disk. If you've not already added a target project, do so using the instructions given in [Add a target project](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/target-project).



For more information, see [`gcloud alpha compute migration disk-migrations create`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/migration/disk-migrations/create).

###  REST API 

To migrate unattached by using the REST API, complete the following steps.

  1. In the Cloud Shell terminal, define a shell alias for calling Google REST APIs:
         
         alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
         

  2. Create a disk migration job using the following REST command:
         
         gcurl https://vmmigration.googleapis.com/v1alpha1/projects/HOST_PROJECT/locations/LOCATION/sources/M2VM_SOURCE/diskMigrationJobs/?disk_migration_job_id=DISK_MIGRATION_JOB -X POST --data '{
         "aws_source_disk_details":{"volume_id":"AWS_VOLUME_ID"},
         "target_details":{
           "target_disk":{
             "disk_id":"TARGET_DISK_ID",
             "zone":"TARGET_ZONE",
             "disk_type":"DISK_TYPE"
           },
           "target_project":"projects/HOST_PROJECT/locations/global/targetProjects/TARGET_PROJECT",
           "labels":{CUSTOM_LABELS},
           "encryption":{"kms_key":"KMS_KEY"}
         }
         }'
         

Replace the following:

     * `HOST_PROJECT`: the name of the host project in which you want to run the disk migration process.
     * `LOCATION`: the region in which you want the disk migration process to run. For a list of supported zones, see [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones).
     * `M2VM_SOURCE`: the cloud source from which you want to migrate the disks. Note that you can only migrate disks from AWS sources.
     * `DISK_MIGRATION_JOB`: the ID of the disk migration job. For information on naming convention for Compute Engine resources, see [Naming conventions](https://docs.cloud.google.com/compute/docs/naming-resources).
     * `AWS_VOLUME_ID`: the names of the disks that you want to migrate.
     * `TARGET_DISK_ID`: the ID of the target disk. For information on naming convention for Compute Engine resources, see [Naming conventions](https://docs.cloud.google.com/compute/docs/naming-resources).
     * `TARGET_PROJECT`: the ID of the target project to which you want to migrate the disks. If you've not already added a target project, do so using the instructions given in [Add a target project](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/target-project).
     * `TARGET_ZONE`: zone of the target project. See [ Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones).
     * `DISK_TYPE`: the [type of persistent disk](https://docs.cloud.google.com/compute/docs/disks#disk-types) that you want to migrate your disks to. Migrate to Virtual Machines supports the following disk types:
     * `COMPUTE_ENGINE_DISK_TYPE_STANDARD`: a Standard Persistent Disk.
     * `COMPUTE_ENGINE_DISK_TYPE_SSD`: a Performance Persistent Disk.
     * `COMPUTE_ENGINE_DISK_TYPE_BALANCED`: a Balanced Persistent Disk that balance performance and cost.
     * (Optional) `CUSTOM_LABELS`: any labels you want to give the migrated disk. For example, `"key1":"val1", "key2":"val2"`.
     * (Optional) `KMS_KEY`: the KMS key you want to use for the migrated disk. For more information, see [Cloud Key Management Service overview](https://docs.cloud.google.com/kms/docs/key-management-service).
  3. (Optional) Update the target details. The target project is the project that contains the migrated disk. You can configure the target details including project, zone, and disk type based on your preferences. You can modify the target details at any time. You can use the command given in the previous step to update the target details as well.
         
         gcurl https://vmmigration.googleapis.com/v1alpha1/projects/HOST_PROJECT/locations/LOCATION/sources/M2VM_SOURCE/diskMigrationJobs/DISK_MIGRATION_JOB\?update_mask\=target_details  -X PATCH --data '{
         "target_details":{
          "target_disk":{
              "disk_id":"TARGET_DISK_ID",
              "zone":"TARGET_ZONE",
              "disk_type":"DISK_TYPE"
            },
          "target_project":"projects/HOST_PROJECT/locations/global/targetProjects/TARGET_PROJECT",
          "labels":{CUSTOM_LABELS},
          "encryption":{"kms_key":"KMS_KEY"}
          }
         }'
         

  4. Run the migration job by using the following REST command:
         
         gcurl https://vmmigration.googleapis.com/v1alpha1/projects/HOST_PROJECT/locations/LOCATION/sources/M2VM_SOURCE/diskMigrationJobs/DISK_MIGRATION_JOB:run -X POST

  5. Poll the job to check its status by using the following REST command:
         
         gcurl https://vmmigration.googleapis.com/v1alpha1/projects/HOST_PROJECT/locations/LOCATION/sources/M2VM_SOURCE/diskMigrationJobs/DISK_MIGRATION_JOB




## Supported REST API operations for single disk migrations

Migrate to Virtual Machines supports the following REST API operations to migrate a single disk:

### Create a disk migration job
    
    
    gcurl https://vmmigration.googleapis.com/v1alpha1/projects/HOST_PROJECT/locations/LOCATION/sources/M2VM_SOURCE/diskMigrationJobs/?disk_migration_job_id=DISK_MIGRATION_JOB -X POST --data '{
      "aws_source_disk_details":{"volume_id":"AWS_VOLUME_ID"},
      "target_details":{
        "target_disk":{
          "disk_id":"TARGET_DISK_ID",
          "zone":"TARGET_ZONE",
          "disk_type":"DISK_TYPE"
        },
        "target_project":"projects/HOST_PROJECT/locations/global/targetProjects/TARGET_PROJECT",
        "labels":{CUSTOM_LABELS},
        "encryption":{"kms_key":"KMS_KEY"}
      }
    }'
    

Replace the following:

  * `HOST_PROJECT`: the name of the host project in which you want to run the disk migration process.
  * `LOCATION`: the region in which you want the disk migration process to run. For a list of supported zones, see [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones).
  * `M2VM_SOURCE`: the cloud source from which you want to migrate the disks.
  * `DISK_MIGRATION_JOB`: the ID of the disk migration job. For information on naming convention for Compute Engine resources, see [Naming conventions](https://docs.cloud.google.com/compute/docs/naming-resources).
  * `AWS_VOLUME_ID`: the names of the disks that you want to migrate.
  * `TARGET_DISK_ID`: the ID of the target disk. For information on naming convention for Compute Engine resources, see [Naming conventions](https://docs.cloud.google.com/compute/docs/naming-resources).
  * `TARGET_PROJECT`: the ID of the target project to which you want to migrate the disks. If you've not already added a target project, do so using the instructions given in [Add a target project](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/target-project).
  * `TARGET_ZONE`: zone of the target project. See [ Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones).
  * `DISK_TYPE`: the [type of persistent disk](https://docs.cloud.google.com/compute/docs/disks#disk-types) that you want to migrate your disks to. Migrate to Virtual Machines supports the following disk types: 
    * `COMPUTE_ENGINE_DISK_TYPE_STANDARD`: a Standard disk type.
    * `COMPUTE_ENGINE_DISK_TYPE_SSD`: a SSD hard disk type.
    * `COMPUTE_ENGINE_DISK_TYPE_BALANCED`: an alternative to SSD persistent disks that balance performance and cost.
  * (Optional) `CUSTOM_LABELS`: any labels you want to give the migrated disk. For example, `"key1":"val1", "key2":"val2"`.
  * (Optional) `KMS_KEY`: the KMS key you want to use for the migrated disk. For more information, see [Cloud Key Management Service overview](https://docs.cloud.google.com/kms/docs/key-management-service).



### Update a disk migration job
    
    
    gcurl https://vmmigration.googleapis.com/v1alpha1/projects/HOST_PROJECT/locations/LOCATION/sources/M2VM_SOURCE/diskMigrationJobs/DISK_MIGRATION_JOB\?update_mask\=target_details  -X PATCH --data '{
      "target_details":{
        "target_disk":{
          "disk_id":"TARGET_DISK_ID",
          "zone":"TARGET_ZONE",
          "disk_type":"DISK_TYPE"
        },
        "target_project":"projects/HOST_PROJECT/locations/global/targetProjects/TARGET_PROJECT",
        "labels":{CUSTOM_LABELS},
        "encryption":{"kms_key":"KMS_KEY"}
      }
    }'

### Get a disk migration job
    
    
    gcurl https://vmmigration.googleapis.com/v1alpha1/projects/HOST_PROJECT/locations/LOCATION/sources/M2VM_SOURCE/diskMigrationJobs/DISK_MIGRATION_JOB
    

### List disk migration jobs
    
    
    gcurl https://vmmigration.googleapis.com/v1alpha1/projects/HOST_PROJECT/locations/LOCATION/sources/M2VM_SOURCE/diskMigrationJobs
    

### Run a disk migration job
    
    
    gcurl https://vmmigration.googleapis.com/v1alpha1/projects/HOST_PROJECT/locations/LOCATION/sources/M2VM_SOURCE/diskMigrationJobs/DISK_MIGRATION_JOB:run -X POST
    

### Cancel a disk migration job
    
    
    gcurl https://vmmigration.googleapis.com/v1alpha1/projects/HOST_PROJECT/locations/LOCATION/sources/M2VM_SOURCE/diskMigrationJobs/DISK_MIGRATION_JOB:cancel -X POST
    

### Delete a disk migration job
    
    
    gcurl https://vmmigration.googleapis.com/v1alpha1/projects/HOST_PROJECT/locations/LOCATION/sources/M2VM_SOURCE/diskMigrationJobs/DISK_MIGRATION_JOB -X DELETE
    

## REST API scripts for batch disk migrations

Use the following the REST API scripts to perform batch disk migration tasks.

### Create a batch disk migration job
    
    
    token=`gcloud auth print-access-token`
    for PAIR in `echo "SRC_TARGET_PAIRS" |tr -d ' '|tr ',' ' '`;
    do
      vol=${PAIR%:*}
      disk=${PAIR#*:}
      curl -H "Authorization: Bearer $token" -H "Content-Type: application/json" https://vmmigration.googleapis.com/v1alpha1/projects/HOST_PROJECT/locations/LOCATION/sources/M2VM_SOURCE/diskMigrationJobs\?disk_migration_job_id\=dmj-${vol}  -X POST -d '{
        "aws_source_disk_details":{"volume_id":"'${vol}'"},
        "target_details":{
          "target_disk":{
            "disk_id":"'${disk}'",
            "zone":"TARGET_ZONE",
            "disk_type":"DISK_TYPE"
          },
          "target_project":"projects/HOST_PROJECT/locations/global/targetProjects/TARGET_PROJECT",
          "labels":{CUSTOM_LABELS},
          "encryption":{"kms_key":"KMS_KEY"}
        }
      }'
    done
    

Replace the following:

  * `SRC_TARGET_PAIRS`: a comma-separated list of `SOURCE:TARGET` pairs. For example, `vol1:disk1, vol2:disk2`.
  * `HOST_PROJECT`: the name of the host project in which you want to run the disk migration process.
  * `LOCATION`: the region in which you want the disk migration process to run. For a list of supported zones, see [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones).
  * `M2VM_SOURCE`: the cloud source from which you want to migrate the disks.
  * `DISK_MIGRATION_JOB`: the ID of the disk migration job. For information on naming convention for Compute Engine resources, see [Naming conventions](https://docs.cloud.google.com/compute/docs/naming-resources).
  * `AWS_VOLUME_ID`: the names of the disks that you want to migrate.
  * `TARGET_DISK_ID`: the ID of the target disk. For information on naming convention for Compute Engine resources, see [Naming conventions](https://docs.cloud.google.com/compute/docs/naming-resources).
  * `TARGET_PROJECT`: the ID of the target project to which you want to migrate the disks. If you've not already added a target project, do so using the instructions given in [Add a target project](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/target-project).
  * `TARGET_ZONE`: zone of the target project. See [ Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones).
  * `DISK_TYPE`: the [type of persistent disk](https://docs.cloud.google.com/compute/docs/disks#disk-types) that you want to migrate your disks to. Migrate to Virtual Machines supports the following disk types: 
    * `COMPUTE_ENGINE_DISK_TYPE_STANDARD`: a Standard disk type.
    * `COMPUTE_ENGINE_DISK_TYPE_SSD`: a SSD hard disk type.
    * `COMPUTE_ENGINE_DISK_TYPE_BALANCED`: an alternative to SSD persistent disks that balance performance and cost.
    * `COMPUTE_ENGINE_DISK_TYPE_HYPERDISK_BALANCED`: hyperdisk balanced disk type.
  * `CUSTOM_LABELS`: any labels you want to give the migrated disk. For example, `"key1":"val1", "key2":"val2"`.
  * `KMS_KEY`: the KMS key you want to use for the migrated disk. For more information, see [Cloud Key Management Service overview](https://docs.cloud.google.com/kms/docs/key-management-service).



### Update a batch disk migration job
    
    
    token=`gcloud auth print-access-token`
    for PAIR in `echo "SRC_TARGET_PAIRS" |tr -d ' '|tr ',' ' '`;
    do
      vol=${PAIR%:*}
      disk=${PAIR#*:}
      curl -H "Authorization: Bearer $token" -H "Content-Type: application/json" https://vmmigration.googleapis.com/v1alpha1/projects/HOST_PROJECT/locations/LOCATION/sources/M2VM_SOURCE/diskMigrationJobs/dmj-${vol}\?update_mask\=target_details -X PATCH -d '{
        "target_details":{
          "target_disk":{
            "disk_id":"'${disk}'",
            "zone":"TARGET_ZONE",
            "disk_type":"DISK_TYPE"
          },
          "target_project":"projects/HOST_PROJECT/locations/global/targetProjects/TARGET_PROJECT",
          "labels":{CUSTOM_LABELS},
          "encryption":{"kms_key":"KMS_KEY"}
        }
      }'
    done
    

### Get a batch disk migration job
    
    
    token=`gcloud auth print-access-token`
    for PAIR in `echo "SRC_TARGET_PAIRS" |tr -d ' '|tr ',' ' '`;
    do
      vol=${PAIR%:*}
      disk=${PAIR#*:}
      curl -H "Authorization: Bearer $token" -H "Content-Type: application/json" https://vmmigration.googleapis.com/v1alpha1/projects/HOST_PROJECT/locations/LOCATION/sources/M2VM_SOURCE/diskMigrationJobs/dmj-${vol};
    done
    

### List batch disk migration jobs
    
    
    token=`gcloud auth print-access-token`
      curl -H "Authorization: Bearer $token" -H "Content-Type: application/json" https://vmmigration.googleapis.com/v1alpha1/projects/HOST_PROJECT/locations/LOCATION/sources/M2VM_SOURCE/diskMigrationJobs
    

### Run a batch disk migration job
    
    
    token=`gcloud auth print-access-token`
    for PAIR in `echo "SRC_TARGET_PAIRS" |tr -d ' '|tr ',' ' '`;
    do
      vol=${PAIR%:*}
      disk=${PAIR#*:}
      curl -H "Authorization: Bearer $token" -H "Content-Type: application/json" https://vmmigration.googleapis.com/v1alpha1/projects/HOST_PROJECT/locations/LOCATION/sources/M2VM_SOURCE/diskMigrationJobs/dmj-${vol}:run -X POST;
    done
    

### Cancel a batch disk migration job
    
    
    token=`gcloud auth print-access-token`
    for PAIR in `echo "SRC_TARGET_PAIRS" |tr -d ' '|tr ',' ' '`;
    do
      vol=${PAIR%:*}
      disk=${PAIR#*:}
      curl -H "Authorization: Bearer $token" -H "Content-Type: application/json" https://vmmigration.googleapis.com/v1alpha1/projects/HOST_PROJECT/locations/LOCATION/sources/M2VM_SOURCE/diskMigrationJobs/dmj-${vol}:cancel -X POST;
    done
    

### Delete a batch disk migration job
    
    
    token=`gcloud auth print-access-token`
    for PAIR in `echo "SRC_TARGET_PAIRS" |tr -d ' '|tr ',' ' '`;
    do
      vol=${PAIR%:*}
      disk=${PAIR#*:}
      curl -H "Authorization: Bearer $token" -H "Content-Type: application/json" https://vmmigration.googleapis.com/v1alpha1/projects/HOST_PROJECT/locations/LOCATION/sources/M2VM_SOURCE/diskMigrationJobs/dmj-${vol} -X DELETE;
    done
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
