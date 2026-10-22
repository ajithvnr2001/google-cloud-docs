---
url: https://docs.cloud.google.com/migration-center/docs/import-data-tables/
title: Manually create and upload data tables \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:58.793984+00:00
---

# Manually create and upload data tables  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/import-data-tables/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Manually create and upload data tables Stay organized with collections  Save and categorize content based on your preferences. 

Migration Center lets you upload tables of data that you fill in manually using the templates provided. This is useful if your infrastructure has a limited number of assets and you want to manually create the data.

To manually create and upload data tables, follow these steps:

  1. Download the templates from the list of available templates.
  2. Manually fill in the tables with the data from your infrastructure.
  3. Upload the tables to Migration Center.



## Limitations

  * The maximum size for a file upload is 100 Mb.



## Available data templates

The following table provides you with the file templates that you can use to upload your infrastructure data to Migration Center. The templates contain sample data as a suggestion on how to fill in the table. For a detailed description of the required data format, see Import files specifications.

**File name** | **Data type** | **Description**  
---|---|---  
[vmInfo.csv](https://storage.googleapis.com/mc-release/mc-templates/vmInfo.csv) | Machine information | Use this template to provide information about individual assets, including CPU, memory, and other configuration parameters. This table is required every time you create a new import.  
[perfInfo.csv](https://storage.googleapis.com/mc-release/mc-templates/perfInfo.csv) | Performance data | Optional: Use this template to provide performance data for your assets in a time-series format.  
[diskInfo.csv](https://storage.googleapis.com/mc-release/mc-templates/diskInfo.csv) | Disk data | Optional: Use this template to provide information about disks and their utilization.  
[tagInfo.csv](https://storage.googleapis.com/mc-release/mc-templates/tagInfo.csv) | System tags | Optional: Use this template to assign key-value attributes to your Amazon Web Services (AWS) assets. The attributes are formatted as `"tag:KEY" : "VALUE"`. For example, `"tag:Name" : "AWS-example"`.  
  
For more information about the specifications for each file, see Import files specifications.

## Upload the tables

To upload the files, follow these steps:

###  Console 

  1. Go to the **Data import** page.

[Go to Data import](https://console.cloud.google.com/migration/discovery/dataImport)

  2. Click **Add data > Upload files**.

  3. In the **Set up file upload** section, enter the name of the file upload.

  4. From the **File format** list, select **Manually populated CSV templates**. 

  5. Click **Select files to upload** , then select all the files that you want to upload.

  6. To confirm and start uploading the files, click **Upload files**.

  7. If the files are validated correctly, to create the assets from the files, click **Import data** , then click **Confirm**.




###  API 

  1. Create an import job.
         
         POST https://migrationcenter.googleapis.com/v1alpha1/projects/PROJECT_ID/locations/REGION/importJobs?importJobId=IMPORT_JOB_ID
         
         {
           "asset_source": "projects/PROJECT_ID/locations/REGION/sources/SOURCE_ID"
         }
         

Replace the following:

     * `PROJECT_ID`: ID of the project to create the import job.
     * `REGION`: Region to create the import job.
     * `IMPORT_JOB_ID`: ID of the new import job.
     * `SOURCE_ID`: ID of an **existing** source to be associated with the import job.
  2. Optional: To confirm that the import job was correctly created, get the import job.
         
         GET https://migrationcenter.googleapis.com/v1alpha1/projects/PROJECT_ID/locations/REGION/importJobs/IMPORT_JOB_ID
         

  3. Create a import data file attached to the import job.
         
         POST https://migrationcenter.googleapis.com/v1alpha1/projects/PROJECT_ID/locations/REGION/importJobs/IMPORT_JOB_ID/importDataFiles?import_data_file_id=DATA_FILE_ID
         
         {
           "format": "IMPORT_JOB_FORMAT"
         }
         

Replace the following:

     * `DATA_FILE_ID`: ID of the new data file
     * `IMPORT_JOB_FORMAT`: `IMPORT_JOB_FORMAT_MANUAL_CSV`
  4. Get the data file.
         
         GET https://migrationcenter.googleapis.com/v1alpha1/projects/PROJECT_ID/locations/REGION/importJobs/IMPORT_JOB_ID/importDataFiles/DATA_FILE_ID
         

  5. Copy the URL from the `signedUrl` field from the response.

  6. Upload a file to the copied URL.
         
         PUT -H 'Content-Type: application/octet-stream' --upload-file UPLOAD_FILE_PATH 'COPIED_URL'
         

Replace the following:

     * `UPLOAD_FILE_PATH`: The local path of the file that is uploaded.
     * `COPIED_URL`: The copied signed URL from the previews steps.
  7. Optional: Repeat steps 3-6 to create more data files under the same import job.

  8. Optional: Get all data files of an import job.
         
         GET https://migrationcenter.googleapis.com/v1alpha1/projects/PROJECT_ID/locations/REGION/importJobs/IMPORT_JOB_ID/importDataFiles
         

  9. Validate the import job.
         
         POST https://migrationcenter.googleapis.com/v1alpha1/projects/PROJECT_ID/locations/REGION/importJobs/IMPORT_JOB_ID:validate
         

  10. Get the import job and view the validation report. If the state is `READY`, it is possible to continue to the next steps. Otherwise, you need to fix the job or specific files, this might require deleting files or uploading new ones.
         
         GET https://migrationcenter.googleapis.com/v1alpha1/projects/PROJECT_ID/locations/REGION/importJobs/IMPORT_JOB_ID
         

  11. Run the import job.
         
         POST https://migrationcenter.googleapis.com/v1alpha1/projects/PROJECT_ID/locations/REGION/importJobs/IMPORT_JOB_ID:run
         

  12. Get the import job and view the execution report. If the state is `COMPLETED`, the job was executed successfully. Otherwise, if the job failed and in a terminal state, the execution report includes the errors. Create a new import job and apply the required changes.
         
         GET https://migrationcenter.googleapis.com/v1alpha1/projects/PROJECT_ID/locations/REGION/importJobs/IMPORT_JOB_ID
         




If you experience problems with your file upload, see how to [troubleshoot common error messages](https://docs.cloud.google.com/migration-center/docs/troubleshooting/file-import-errors).

## Review the upload

After you upload your files, Migration Center validates them to check if they are formally correct. If the validation is successful, Migration Center then processes the data to create new assets, or update existing ones. You can check the status of your upload jobs from the Google Cloud console.

To review the status of your upload job, follow these steps:

  1. In the Google Cloud console, go to the **Data import** page.

[Go to Data import](https://console.cloud.google.com/migration/discovery/dataImport)

  2. In the **File uploads** tab, from the list of file imports, click the import job that you want to review.

  3. Review the **Status** for your uploaded files.

You can see your files in one of the following statuses:

     * **Completed**. The import of your file was successful.
     * **Ready**. Your file passed validation, and is ready to be imported.
     * **Pending**. Your file is waiting for another file to finish processing.
     * **Running**. Your file is processing.
     * **Validating**. Your file is in the validation stage.
     * **Failed validation**. Your file contains some errors. Fix the errors and then try to upload your file again.
     * **Failed**. Your file couldn't be imported.



### Review error details

If you encounter errors after importing your files, you can review the error message directly in the Google Cloud console.

To review the errors of your upload job, follow these steps:

  1. In the Google Cloud console, go to the **Data import** page.

[Go to Data import](https://console.cloud.google.com/migration/discovery/dataImport)

  2. In the **File uploads** tab, from the list of file imports, click the import file that shows a warning or error.

The import file details page shows the complete list of errors.




On the import file details page, you can review the assets and data fields that cause the errors, and view a description of the error. Errors in the file import job might prevent Migration Center from creating new assets or update existing ones with the new changes. To fix the error, edit your files and create a new file import job to upload them again.

For more information about the possible error messages, see [Troubleshoot file import errors](https://docs.cloud.google.com/migration-center/docs/troubleshooting/file-import-errors).

## Import files specifications

The following tables show the technical specifications for the template files used for manual import.

### `vmInfo` file

**Column** | **Expected type** | **Description**  
---|---|---  
MachineId | string | The virtual machine unique identifier.  
MachineName | string | The virtual machine display name.  
PrimaryIPAddress | string | The IP address of the machine.  
PrimaryMACAddress | string | The MAC address of the machine. This is used only to identify the machine.  
PublicIPAddress | string | The public IP address of the machine.  
IpAddressListSemiColonDelimited | List of messages | The list of allocated or assigned network addresses.  
TotalDiskAllocatedGiB | int64 | The total capacity of the disk.  
TotalDiskUsedGiB | int64 | The total amount of used space in the disk.  
MachineTypeLabel | string | The AWS or Azure machine type label.  
AllocatedProcessorCoreCount | int64 | Number of CPU cores in the virtual machine.  
MemoryGiB | int32 | The amount of memory of the virtual machine.  
HostingLocation | string | The location of the machine in AWS or Azure format.  
OsType | string | The OS of the machine.  
OsName | string | The OS of the machine.  
OsVersion | string | The version of the OS of the machine.  
MachineStatus | string | The power state of the machine.  
ProvisioningState | string | The provisioning state, for Azure VMs only.  
CreateDate | Timestamp | The creation timestamp of the machine.  
IsPhysical | string | If the machine is a physical or virtual machine.  
Source | message | The details of the source for AWS or Azure machines.  
  
### `diskInfo` file

**Column** | **Expected type** | **Description**  
---|---|---  
MachineId | string | The virtual machine unique identifier.  
DiskLabel | string | The disk label.  
SizeInGib | int64 | The total capacity of the disk.  
UsedInGib | int64 | The total amount of used space in the disk.  
StorageTypeLabel | string | The disk label type (for example BIOS or GPT).  
  
### perfInfo file

**Column** | **Expected type** | **Description**  
---|---|---  
MachineId | string | The virtual machine unique identifier.  
TimeStamp |  | The timestamp when the sample was collected.  
CpuUtilizationPercentage | float | The percentage of total CPU capacity used. It must be in the interval 0-100.  
MemoryUtilizationPercentage | float | The percentage of system memory used. It must be in the interval 0-100.  
UtilizedMemoryBytes | float | The total memory used in bytes.  
DiskReadOperationsPerSec | float | The average IOPS sampled over a short window.  
DiskWriteOperationsPerSec | float | The average IOPS sampled over a short window.  
NetworkBytesPerSecSent | float | The average network egress in B/s, sampled over a short window.  
NetworkBytesPerSecReceived | float | The average network ingress in B/s, sampled over a short window.  
  
### tagInfo file

**Column** | **Expected type** | **Description**  
---|---|---  
Key | string | The attribute key.  
Value | string | The attribute value.  
  
## What's next

  * Learn more about [Migration Center collection methods](https://docs.cloud.google.com/migration-center/docs/start-asset-discovery#collection_methods).
  * Learn how to [manage your file uploads](https://docs.cloud.google.com/migration-center/docs/manage-file-uploads).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
