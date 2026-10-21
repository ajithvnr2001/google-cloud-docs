---
url: https://docs.cloud.google.com/sql/docs/postgres/delete-instance/
title: Delete instances \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:56.007139+00:00
---

# Delete instances  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/delete-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Delete instances Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/delete-instance "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/delete-instance "View this page for the SQL Server database engine")

This page describes how to delete Cloud SQL instances.

**Warning:** All data on an instance, including backups, is permanently lost when that instance is deleted. To preserve your data, [export it to Cloud Storage](https://docs.cloud.google.com/sql/docs/postgres/import-export) before you delete it. The Cloud SQL Admin role includes the permission to delete the instance. To prevent accidental deletion, grant this role only as needed. Additionally, consider [deletion protection](https://docs.cloud.google.com/sql/docs/postgres/deletion-protection).

Note the following when you plan to delete an instance:

  * You cannot delete an instance that has any replicas. You must delete all replicas first. You can reduce your chances of accidentally deleting an instance by creating a replica; a replica must be deleted before its primary instance.
  * After you delete an instance, it might continue to appear in your project with an "unknown" size but with a "Being deleted" status. This is normal and the instance disappears completely after a brief period of time.
  * It can take up to four days for the underlying resources related to an instance to be completely deleted, with the exception of read replicas, which are often deleted within a few minutes.
  * The deleted instance name can be reused immediately to create a new instance.
  * If [ deletion protection](https://docs.cloud.google.com/sql/docs/postgres/deletion-protection) is enabled on an instance, you must disable it before deleting the instance.
  * In case of contingencies, take a [final backup](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups#final-backups) to restore the deleted instance.



## Required permissions

By default, only user or service accounts with the `Cloud SQL Admin` (`roles/cloudsql.admin`) or `Owner` (`roles/owner`) role have the permission to delete a Cloud SQL instance (`cloudsql.instances.delete`).

You can also define an [IAM custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) for the user or service account that includes the `cloudsql.instances.delete` permission. This permission is [supported](https://docs.cloud.google.com/iam/docs/custom-roles-permissions-support) in IAM custom roles.

## Delete an instance

You can delete a Cloud SQL instance by using the Google Cloud console, [](https://docs.cloud.google.com/sdk/gcloud)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), or the API. If you want to retain backups for your instance prior to deleting, see [Manage retained backups](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/manage-retained-backups).

**Note:** Before you delete an instance, confirm that it's safe to do so. Then, confirm that [deletion protection](https://docs.cloud.google.com/sql/docs/postgres/deletion-protection) is deactivated for the instance. Also, we strongly recommend that you take a final backup of the instance before you delete it.

If you used [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs) to encrypt your instance, but the KMS keys aren't accessible, then after you delete the instance, the status of the final backup is `FAILED`. If this occurs, then request to recover your instance by contacting [Cloud Customer Care](https://docs.cloud.google.com/support) within 4 days from the time that you deleted the instance.

If you delete an instance that has [Private Service Connect](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect) enabled for it, then the following actions occur:

  * The [service attachment](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#service-attachment) is removed automatically. However, the [Private Service Connect endpoint](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#psc-endpoint) that points to the service attachment isn't deleted automatically. By listing the forwarding rule that's associated with the endpoint, you can see that the rule has a `CLOSED` status. After you receive this status, you can delete the endpoint.
  * You see the connection to the endpoint time out.



To avoid incurring additional costs, we strongly recommend that you also delete the corresponding [DNS zone](https://docs.cloud.google.com/dns/docs/dns-overview#zones) and [DNS record](https://docs.cloud.google.com/dns/docs/dns-overview#records).

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Delete**.
  4. In the **Delete instance** dialog, complete the following actions:
     1. In the text field, enter the instance ID that appears.
     2. If you want to take a [final backup](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups#final-backups) of the instance, leave the **Take a final backup** checkbox selected, expand the **Retention options** menu, and then, in the **Retain for** field, enter the number of days to retain the final backup. You can specify from 1 to 365 days.

If you want to delete the instance without taking a final backup, then clear the checkbox.

     3. In the **Describe this backup** text area, you can provide a description of the backup.
     4. Click **Delete**.



### gcloud

To delete an instance, use the [`gcloud sql instances delete`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/delete) command:
    
    
    gcloud sql instances delete INSTANCE_NAME \
    --project=PROJECT_ID

Make the following replacements:

  * INSTANCE_NAME: the name of the instance
  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance that you want to delete



**Note:** If you want to take a final backup of the instance, then use the following flags:

  * `--enable-final-backup`: set the value of this flag to `true` to take a final backup. If you want to delete the instance without taking a final backup, then set the value to `false`.
  * `--final-backup-description`: provide details about the final backup. The default value is empty.
  * `--final-backup-ttl-days`: specify the number of days to retain the final backup. This is known as time to live (TTL). The default value is 30 days. The allowed retention period varies, from 1 to 365 days. To provide the retention period, use either this flag or `--final-backup-expiry-time`.
  * `--final-backup-expiry-time`: this is a timestamp (in UTC) of when the backup is set to expire. This can't exceed 1 year. To provide the retention period, use either this flag or `--final-backup-ttl-days`.



### REST v1

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance that you want to delete
  * INSTANCE_NAME: the name of the instance



**Note:** If you want to take a final backup of the instance, then use the following query parameters:

  * `enable_final_backup`: set the value of this parameter to `true` to take a final backup. If you want to delete the instance without taking a final backup, then set the value to `false`.
  * `final_backup_description`: provide details about the final backup. The default value is empty.
  * `final_backup_ttl_days`: specify the number of days to retain the final backup. This is known as time to live (TTL). The default value is 30 days. The allowed retention period varies, from 1 to 365 days. To provide the retention period, use either this parameter or `final_backup_expiry_time`.
  * `final_backup_expiry_time`: this is a timestamp (in UTC) of when the backup is set to expire. This can't exceed 1 year. To provide the retention period, use either this parameter or `final_backup_ttl_days`.



HTTP method and URL: 
    
    
    DELETE https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-15T00:10:22.078Z",
      "operationType": "DELETE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

To see how the [underlying REST API request](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/delete) is constructed for this task, see the [APIs Explorer on the instances:delete page](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/delete). 

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance that you want to delete
  * INSTANCE_NAME: the name of the instance



**Note:** If you want to take a final backup of the instance, then use the following query parameters:

  * `enable_final_backup`: set the value of this parameter to `true` to take a final backup. If you want to delete the instance without taking a final backup, then set the value to `false`.
  * `final_backup_description`: provide details about the final backup. The default value is empty.
  * `final_backup_ttl_days`: specify the number of days to retain the final backup. This is known as time to live (TTL). The default value is 30 days. The allowed retention period varies, from 1 to 365 days. To provide the retention period, use either this parameter or `final_backup_expiry_time`.
  * `final_backup_expiry_time`: this is a timestamp (in UTC) of when the backup is set to expire. This can't exceed 1 year. To provide the retention period, use either this parameter or `final_backup_ttl_days`.



HTTP method and URL: 
    
    
    DELETE https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-15T00:10:22.078Z",
      "operationType": "DELETE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

To see how the [underlying REST API request](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/delete) is constructed for this task, see the [APIs Explorer on the instances:delete page](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/delete). 

## Restore a deleted instance

When you delete an instance, Cloud SQL deletes all resources for the instance, including [on-demand backups](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups#on-demand-backups) and [automated backups](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups#automated-backups).

If you take a [final backup](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups#final-backups) as part of deleting an instance, then you can use this backup to recover the instance, either by creating an instance from the final backup or by restoring the final backup to an existing instance.

If you use a final backup to recover your instance, then your instance might have a different IP address from the original, deleted instance.

If you delete an instance accidentally without taking a final backup, then you can request to recover the instance by contacting [Cloud Customer Care](https://docs.cloud.google.com/support) within 4 days from the time that the instance is deleted. If the instance can be recovered, then the instance configuration, including IP addresses used before the deletion, are restored. All backups available at the time of deletion are also recovered.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
