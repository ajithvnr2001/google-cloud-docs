---
url: https://docs.cloud.google.com/spanner/docs/backup/manage-backups/
title: Manage backups \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:03.623189+00:00
---

# Manage backups  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/backup/manage-backups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Manage backups Stay organized with collections  Save and categorize content based on your preferences. 

This page offers information about Spanner backup operations. For more information about backups, see [Backups overview](https://docs.cloud.google.com/spanner/docs/backup).

## Before you begin

  * To get the permissions that you need to manage backups, ask your administrator to grant you the following IAM roles on the instance: 

    * Create, view, update, and delete backups: [Cloud Spanner Backup Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupAdmin) (`roles/spanner.backupAdmin`) 
    * Create and view backups: [Cloud Spanner Backup Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupWriter) (`roles/spanner.backupWriter`) 

**Note:** [IAM basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) might also contain permissions to manage backups. You shouldn't grant basic roles in a production environment, but you can grant them in a development or test environment. 
  * The Google Cloud CLI examples on this page make the following assumptions:

    * You have already set up [gcloud CLI](https://docs.cloud.google.com/sdk/docs) for use with Spanner. If you are new to using gcloud CLI with Spanner, see [Getting started with Spanner using gcloud CLI](https://docs.cloud.google.com/spanner/docs/getting-started/gcloud).
    * You have configured gcloud CLI with your project. For example:
          
          gcloud config set core/project PROJECT_ID




## Copy a backup

### Console

  1. In the Google Cloud console, go to the Spanner **Instances** page.

[Go to Instances](https://console.cloud.google.com/spanner/instances)

  2. Click the instance that contains the database that you want to copy.

  3. Click the database.

  4. In the navigation pane, click **Backup/Restore**.

  5. In the **Backups** table, select **Actions** for your backup and click **Copy**.

  6. Fill out the form by choosing a destination instance, providing a name, and selecting an expiration date for the backup copy.

  7. Click **Copy**.




To check the progress of a copy operation, see Check the operation progress.

If the operation takes too long, you can cancel it. For more information, see [Cancel a long-running instance operation](https://docs.cloud.google.com/spanner/docs/manage-and-observe-long-running-operations#cancel_a_long-running_instance_operation).

**Note:** If you are copying to a different instance, the copy backup operation appears in the destination instance containing the copied backup, not the instance containing the source backup. The Google Cloud console doesn't support copying a backup to an instance in a different project. To copy a backup to a different project, use the gcloud CLI, client libraries, [REST APIs](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups), or [RPC APIs](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.Backup).

###  gcloud 

You can copy a backup to a different instance in the same project, or to a different instance in a different project.

### Copy a backup in the same project

If you choose to copy the backup to a different instance in the same project, you must create a new instance (or have one ready) for the copied backup. You can't create a new instance as part of the backup copy operation. Also, the expiration time of the backup must be at least six hours from the time the current copy request is processed and at most 366 days after the `create_time` of the source backup.

Before using any of the command data below, make the following replacements: 

  * PROJECT_ID: the project ID.
  * SOURCE_INSTANCE_ID: the source Spanner instance ID.
  * SOURCE_DATABASE_ID: the source Spanner database ID.
  * SOURCE_BACKUP_NAME: the Spanner backup name.
  * DESTINATION_INSTANCE_ID: the target Spanner instance ID.
  * DESTINATION_BACKUP_NAME: the destination Spanner backup name.
  * EXPIRATION_DATE: the expiration date time stamp.
  * ENCRYPTION_TYPE: the encryption type of backup created. Valid values are `USE_CONFIG_DEFAULT_OR_BACKUP_ENCRYPTION`, `GOOGLE_DEFAULT_ENCRYPTION` , or `CUSTOMER_MANAGED_ENCRYPTION`. If you use `CUSTOMER_MANAGED_ENCRYPTION`, you must specify a `kmsKeyName`. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backups copy \
    --source-instance=SOURCE_INSTANCE_ID \
    --source-backup=SOURCE_BACKUP_NAME \
    --destination-instance=DESTINATION_INSTANCE_ID \
    --destination-backup=DESTINATION_BACKUP_NAME \
    --expiration-date=EXPIRATION_DATE \
    --encryption-type=ENCRYPTION_TYPE

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backups copy `
    --source-instance=SOURCE_INSTANCE_ID `
    --source-backup=SOURCE_BACKUP_NAME `
    --destination-instance=DESTINATION_INSTANCE_ID `
    --destination-backup=DESTINATION_BACKUP_NAME `
    --expiration-date=EXPIRATION_DATE `
    --encryption-type=ENCRYPTION_TYPE

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backups copy ^
    --source-instance=SOURCE_INSTANCE_ID ^
    --source-backup=SOURCE_BACKUP_NAME ^
    --destination-instance=DESTINATION_INSTANCE_ID ^
    --destination-backup=DESTINATION_BACKUP_NAME ^
    --expiration-date=EXPIRATION_DATE ^
    --encryption-type=ENCRYPTION_TYPE

You should receive a response similar to the following:
    
    
    createTime: '2022-03-29T22:06:05.905823Z'
    database: projects/PROJECT_ID/instances/SOURCE_INSTANCE_ID/databases/SOURCE_DATABASE_ID
    databaseDialect: GOOGLE_STANDARD_SQL
    encryptionInfo:
    encryptionType: GOOGLE_DEFAULT_ENCRYPTION
    expireTime: '2022-03-30T10:49:41Z'
    maxExpireTime: '2023-03-17T20:46:33.479336Z'
    name: projects/PROJECT_ID/instances/DESTINATION_INSTANCE_ID/backups/DESTINATION_BACKUP_NAME
    sizeBytes: '7957667'
    state: READY
    versionTime: '2022-03-16T20:46:33.479336Z'
    

### Copy a backup in a different project

If you choose to copy the backup to a different project, you must have another project with its own instance ready for the copied backup. You can't create a new project as part of the backup copy operation. Also, the expiration time of the backup must be at least six hours from the time the current copy request is processed and at most 366 days after the source backup `create_time`.

Before using any of the command data below, make the following replacements: 

  * SOURCE_PROJECT_ID: the source project ID.
  * SOURCE_INSTANCE_ID: the source Spanner instance ID.
  * SOURCE_DATABASE_ID: the source Spanner database ID.
  * SOURCE_BACKUP_NAME: the Spanner backup name.
  * DESTINATION_PROJECT_ID: the destination project ID.
  * DESTINATION_INSTANCE_ID: the target Spanner instance ID.
  * DESTINATION_BACKUP_NAME: the destination Spanner backup name.
  * EXPIRATION_DATE: the expiration date time stamp.
  * ENCRYPTION_TYPE: the encryption type of backup created. Valid values are `USE_CONFIG_DEFAULT_OR_BACKUP_ENCRYPTION`, `GOOGLE_DEFAULT_ENCRYPTION` , or `CUSTOMER_MANAGED_ENCRYPTION`. If you use `CUSTOMER_MANAGED_ENCRYPTION`, you must specify a `kmsKeyName`. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backups copy \
    --source-backup=projects/SOURCE_PROJECT_ID/instances/SOURCE_INSTANCE_ID/backups/SOURCE_BACKUP_NAME \
    --destination-backup=projects/DESTINATION_PROJECT_ID/instances/DESTINATION_INSTANCE_ID/backups/DESTINATION_BACKUP_NAME \
    --expiration-date=EXPIRATION_DATE \
    --encryption-type=ENCRYPTION_TYPE

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backups copy `
    --source-backup=projects/SOURCE_PROJECT_ID/instances/SOURCE_INSTANCE_ID/backups/SOURCE_BACKUP_NAME `
    --destination-backup=projects/DESTINATION_PROJECT_ID/instances/DESTINATION_INSTANCE_ID/backups/DESTINATION_BACKUP_NAME `
    --expiration-date=EXPIRATION_DATE `
    --encryption-type=ENCRYPTION_TYPE

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backups copy ^
    --source-backup=projects/SOURCE_PROJECT_ID/instances/SOURCE_INSTANCE_ID/backups/SOURCE_BACKUP_NAME ^
    --destination-backup=projects/DESTINATION_PROJECT_ID/instances/DESTINATION_INSTANCE_ID/backups/DESTINATION_BACKUP_NAME ^
    --expiration-date=EXPIRATION_DATE ^
    --encryption-type=ENCRYPTION_TYPE

You should receive a response similar to the following:
    
    
    createTime: '2022-03-29T22:06:05.905823Z'
    database: projects/SOURCE_PROJECT_ID/instances/SOURCE_INSTANCE_ID/databases/SOURCE_DATABASE_ID
    databaseDialect: GOOGLE_STANDARD_SQL
    encryptionInfo:
    encryptionType: GOOGLE_DEFAULT_ENCRYPTION
    expireTime: '2022-03-30T10:49:41Z'
    maxExpireTime: '2023-03-17T20:46:33.479336Z'
    name: projects/DESTINATION_PROJECT_ID/instances/DESTINATION_INSTANCE_ID/backups/DESTINATION_BACKUP_NAME
    sizeBytes: '7957667'
    state: READY
    versionTime: '2022-03-16T20:46:33.479336Z'
    

To check the progress of a copy operation, see Check the operation progress.

### Client libraries

The following code sample copies an existing backup. You can copy the backup into an instance in a different region or project. Once complete, the sample retrieves and prints some information about the newly created copied backup, such as its name, size, backup state, and [`version_time`](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups#Backup.FIELDS.version_time).

### C++
    
    
    void CopyBackup(google::cloud::spanner_admin::DatabaseAdminClient client,
                    std::string const& src_project_id,
                    std::string const& src_instance_id,
                    std::string const& src_backup_id,
                    std::string const& dst_project_id,
                    std::string const& dst_instance_id,
                    std::string const& dst_backup_id,
                    google::cloud::spanner::Timestamp expire_time) {
      google::cloud::spanner::Backup source(
          google::cloud::spanner::Instance(src_project_id, src_instance_id),
          src_backup_id);
      google::cloud::spanner::Instance dst_in(dst_project_id, dst_instance_id);
      auto copy_backup =
          client
              .CopyBackup(dst_in.FullName(), dst_backup_id, source.FullName(),
                          expire_time.get<google::protobuf::Timestamp>().value())
              .get();
      if (!copy_backup) throw std::move(copy_backup).status();
      std::cout << "Copy Backup " << copy_backup->name()  //
                << " of " << source.FullName()            //
                << " of size " << copy_backup->size_bytes() << " bytes as of "
                << google::cloud::spanner::MakeTimestamp(
                       copy_backup->version_time())
                       .value()
                << " was created at "
                << google::cloud::spanner::MakeTimestamp(copy_backup->create_time())
                       .value()
                << ".\n";
    }

### C#
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Cloud.Spanner.Admin.Database.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.html);
    using [Google.Cloud.Spanner.Common.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    
    public class CopyBackupSample
    {
        public Backup CopyBackup(
            string sourceProjectId, string sourceInstanceId, string sourceBackupId,
            string targetProjectId, string targetInstanceId, string targetBackupId,
            DateTimeOffset expireTime)
        {
            [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html) databaseAdminClient = [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_Create)();
    
            var request = new [CopyBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CopyBackupRequest.html)
            {
                SourceBackupAsBackupName = new [BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupName.html)(sourceProjectId, sourceInstanceId, sourceBackupId),
                ParentAsInstanceName = new [InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html)(targetProjectId, targetInstanceId),
                BackupId = targetBackupId,
                ExpireTime = [Timestamp](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html).[FromDateTimeOffset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html#Google_Protobuf_WellKnownTypes_Timestamp_FromDateTimeOffset_System_DateTimeOffset_)(expireTime)
            };
    
            var response = databaseAdminClient.[CopyBackup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_CopyBackup_Google_Cloud_Spanner_Admin_Database_V1_CopyBackupRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
            Console.WriteLine("Waiting for the operation to finish.");
            var completedResponse = response.PollUntilCompleted(new [PollSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PollSettings.html)([Expiration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Expiration.html).[FromTimeout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Expiration.html#Google_Api_Gax_Expiration_FromTimeout_System_TimeSpan_)(TimeSpan.FromMinutes(15)), TimeSpan.FromMinutes(2)));
    
            if (completedResponse.IsFaulted)
            {
                Console.WriteLine($"Error while creating backup: {completedResponse.Exception}");
                throw completedResponse.Exception;
            }
    
            [Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html) backup = completedResponse.Result;
    
            Console.WriteLine($"Backup created successfully.");
            Console.WriteLine($"Backup with Id {sourceBackupId} has been copied from {sourceProjectId}/{sourceInstanceId} to {targetProjectId}/{targetInstanceId} Backup {targetBackupId}");
            Console.WriteLine($"Backup {backup.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html#Google_Cloud_Spanner_Admin_Database_V1_Backup_Name)} of size {backup.[SizeBytes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html#Google_Cloud_Spanner_Admin_Database_V1_Backup_SizeBytes)} bytes was created at {backup.[CreateTime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html#Google_Cloud_Spanner_Admin_Database_V1_Backup_CreateTime)} from {backup.[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html#Google_Cloud_Spanner_Admin_Database_V1_Backup_Database)} and is in state {backup.[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html#Google_Cloud_Spanner_Admin_Database_V1_Backup_State)} and has version time {backup.[VersionTime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html#Google_Cloud_Spanner_Admin_Database_V1_Backup_VersionTime)}");
    
            return backup;
        }
    }
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	database "cloud.google.com/go/spanner/admin/database/apiv1"
    	adminpb "cloud.google.com/go/spanner/admin/database/apiv1/databasepb"
    	pbt "github.com/golang/protobuf/ptypes/timestamp"
    )
    
    // copyBackup copies an existing backup to a given instance in same or different region, or in same or different project.
    func copyBackup(w io.Writer, instancePath string, copyBackupId string, sourceBackupPath string) error {
    	// instancePath := "projects/my-project/instances/my-instance"
    	// copyBackupId := "my-copy-backup"
    	// sourceBackupPath := "projects/my-project/instances/my-instance/backups/my-source-backup"
    
    	// Add timeout to context.
    	ctx, cancel := context.WithTimeout(context.Background(), time.Hour)
    	defer cancel()
    
    	// Instantiate database admin client.
    	adminClient, err := database.NewDatabaseAdminClient(ctx)
    	if err != nil {
    		return fmt.Errorf("database.NewDatabaseAdminClient: %w", err)
    	}
    	defer adminClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/database/apiv1.html#cloud_google_com_go_spanner_admin_database_apiv1_DatabaseAdminClient_Close)()
    
    	expireTime := time.Now().AddDate(0, 0, 14)
    
    	// Instantiate the request for performing copy backup operation.
    	copyBackupReq := adminpb.CopyBackupRequest{
    		Parent:       instancePath,
    		BackupId:     copyBackupId,
    		SourceBackup: sourceBackupPath,
    		ExpireTime:   &pbt.Timestamp{Seconds: expireTime.Unix(), Nanos: int32(expireTime.Nanosecond())},
    	}
    
    	// Start copying the backup.
    	copyBackupOp, err := adminClient.CopyBackup(ctx, &copyBackupReq)
    	if err != nil {
    		return fmt.Errorf("adminClient.CopyBackup: %w", err)
    	}
    
    	// Wait for copy backup operation to complete.
    	fmt.Fprintf(w, "Waiting for backup copy %s/backups/%s to complete...\n", instancePath, copyBackupId)
    	copyBackup, err := copyBackupOp.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("copyBackup.Wait: %w", err)
    	}
    
    	// Check if long-running copyBackup operation is completed.
    	if !copyBackupOp.Done() {
    		return fmt.Errorf("backup %v could not be copied to %v", sourceBackupPath, copyBackupId)
    	}
    
    	// Get the name, create time, version time and backup size.
    	copyBackupCreateTime := time.Unix(copyBackup.CreateTime.Seconds, int64(copyBackup.CreateTime.Nanos))
    	copyBackupVersionTime := time.Unix(copyBackup.VersionTime.Seconds, int64(copyBackup.VersionTime.Nanos))
    	fmt.Fprintf(w,
    		"Backup %s of size %d bytes was created at %s with version time %s\n",
    		copyBackup.Name,
    		copyBackup.SizeBytes,
    		copyBackupCreateTime.Format(time.RFC3339),
    		copyBackupVersionTime.Format(time.RFC3339))
    
    	return nil
    }
    

### Java
    
    
    import com.google.cloud.[Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html);
    import com.google.cloud.spanner.[Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html);
    import com.google.cloud.spanner.[SpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerException.html);
    import com.google.cloud.spanner.[SpannerExceptionFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html);
    import com.google.cloud.spanner.[SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html);
    import com.google.cloud.spanner.[admin](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageRoles.html#com_google_cloud_storage_StorageRoles_admin__).[database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.PipelineSource.html#com_google_cloud_firestore_PipelineSource_database__).v1.[DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html);
    import com.google.spanner.[admin](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageRoles.html#com_google_cloud_storage_StorageRoles_admin__).[database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.PipelineSource.html#com_google_cloud_firestore_PipelineSource_database__).v1.[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Backup.html);
    import com.google.spanner.[admin](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageRoles.html#com_google_cloud_storage_StorageRoles_admin__).[database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.PipelineSource.html#com_google_cloud_firestore_PipelineSource_database__).v1.[BackupName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupName.html);
    import com.google.spanner.[admin](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageRoles.html#com_google_cloud_storage_StorageRoles_admin__).[database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.PipelineSource.html#com_google_cloud_firestore_PipelineSource_database__).v1.[InstanceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.InstanceName.html);
    import java.time.Instant;
    import java.time.OffsetDateTime;
    import java.time.ZoneId;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.[TimeUnit](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.TimeUnit.html);
    
    public class CopyBackupSample {
    
      static void copyBackup() {
        // TODO(developer): Replace these variables before running the sample.
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) projectId = "my-project";
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) instanceId = "my-instance";
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) sourceBackupId = "my-backup";
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) destinationBackupId = "my-destination-backup";
    
        try ([Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html) spanner =
            [SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html).newBuilder().setProjectId(projectId).build().getService();
            [DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html) databaseAdminClient = spanner.createDatabaseAdminClient()) {
          copyBackup(databaseAdminClient, projectId, instanceId, sourceBackupId, destinationBackupId);
        }
      }
    
      static void copyBackup(
          [DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html) databaseAdminClient,
          [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) projectId,
          [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) instanceId,
          [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) sourceBackupId,
          [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) destinationBackupId) {
    
        [Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html) expireTime =
            [Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html).[ofTimeMicroseconds](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html#com_google_cloud_Timestamp_ofTimeMicroseconds_long_)(
                [TimeUnit](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.TimeUnit.html).MICROSECONDS.convert(
                    System.currentTimeMillis() + [TimeUnit](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.TimeUnit.html).DAYS.toMillis(14),
                    [TimeUnit](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.TimeUnit.html).MILLISECONDS));
    
        // Initiate the request which returns an OperationFuture.
        System.out.println("Copying backup [" + destinationBackupId + "]...");
        [Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Backup.html) destinationBackup;
        try {
          // Creates a copy of an existing backup.
          // Wait for the backup operation to complete.
          destinationBackup = databaseAdminClient.[copyBackupAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html#com_google_cloud_spanner_admin_database_v1_DatabaseAdminClient_copyBackupAsync__org_jspecify_annotations_Nullable_com_google_spanner_admin_database_v1_InstanceName_java_lang_String__org_jspecify_annotations_Nullable_com_google_spanner_admin_database_v1_BackupName_com_google_protobuf_Timestamp_)(
              InstanceName.of(projectId, instanceId), destinationBackupId,
              BackupName.of(projectId, instanceId, sourceBackupId), expireTime.toProto()).get();
          System.out.println("Copied backup [" + destinationBackup.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Backup.html#com_google_spanner_admin_database_v1_Backup_getName__)() + "]");
        } catch (ExecutionException e) {
          throw ([SpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerException.html)) e.getCause();
        } catch (InterruptedException e) {
          throw [SpannerExceptionFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html).propagateInterrupt(e);
        }
        // Load the metadata of the new backup from the server.
        destinationBackup = databaseAdminClient.[getBackup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html#com_google_cloud_spanner_admin_database_v1_DatabaseAdminClient_getBackup__org_jspecify_annotations_Nullable_com_google_spanner_admin_database_v1_BackupName_)(destinationBackup.getName());
        System.out.println(
            [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html).format(
                "Backup %s of size %d bytes was copied at %s for version of database at %s",
                destinationBackup.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Backup.html#com_google_spanner_admin_database_v1_Backup_getName__)(),
                destinationBackup.[getSizeBytes](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Backup.html#com_google_spanner_admin_database_v1_Backup_getSizeBytes__)(),
                OffsetDateTime.ofInstant(
                    Instant.ofEpochSecond(destinationBackup.[getCreateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Backup.html#com_google_spanner_admin_database_v1_Backup_getCreateTime__)().getSeconds(),
                        destinationBackup.[getCreateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Backup.html#com_google_spanner_admin_database_v1_Backup_getCreateTime__)().getNanos()),
                    ZoneId.systemDefault()),
                OffsetDateTime.ofInstant(
                    Instant.ofEpochSecond(destinationBackup.[getVersionTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Backup.html#com_google_spanner_admin_database_v1_Backup_getVersionTime__)().getSeconds(),
                        destinationBackup.[getVersionTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Backup.html#com_google_spanner_admin_database_v1_Backup_getVersionTime__)().getNanos()),
                    ZoneId.systemDefault())));
      }
    }

**Note:** The old client library interface code samples for Java are archived in [GitHub](https://github.com/googleapis/google-cloud-java/tree/main/java-spanner/samples/snippets/src/main/java/com/example/spanner/admin/archived). 

### Node.js
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const instanceId = 'my-instance';
    // const backupId = 'my-backup',
    // const sourceBackupPath = 'projects/my-project-id/instances/my-source-instance/backups/my-source-backup',
    // const projectId = 'my-project-id';
    
    // Imports the Google Cloud Spanner client library
    const {Spanner} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    const {PreciseDate} = require('[@google-cloud/precise-date](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/overview.html)');
    
    // Creates a client
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({
      projectId: projectId,
    });
    
    // Gets a reference to a Cloud Spanner Database Admin Client object
    const databaseAdminClient = spanner.[getDatabaseAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)();
    
    async function spannerCopyBackup() {
      // Expire copy backup 14 days in the future
      const expireTime = [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html).[timestamp](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)(
        Date.now() + 1000 * 60 * 60 * 24 * 14,
      ).[toStruct](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/precise-date/precisedate.html)();
    
      // Copy the source backup
      try {
        console.log(`Creating copy of the source backup ${sourceBackupPath}.`);
        const [operation] = await databaseAdminClient.copyBackup({
          parent: databaseAdminClient.instancePath(projectId, instanceId),
          sourceBackup: sourceBackupPath,
          backupId: backupId,
          expireTime: expireTime,
        });
    
        console.log(
          `Waiting for backup copy ${databaseAdminClient.backupPath(
            projectId,
            instanceId,
            backupId,
          )} to complete...`,
        );
        await operation.promise();
    
        // Verify the copy backup is ready
        const [copyBackup] = await databaseAdminClient.getBackup({
          name: databaseAdminClient.backupPath(projectId, instanceId, backupId),
        });
    
        if (copyBackup.state === 'READY') {
          console.log(
            `Backup copy ${copyBackup.name} of size ` +
              `${copyBackup.sizeBytes} bytes was created at ` +
              `${new [PreciseDate](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/precise-date/precisedate.html)(copyBackup.createTime).[toISOString](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/precise-date/precisedate.html)()} ` +
              'with version time ' +
              `${new [PreciseDate](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/precise-date/precisedate.html)(copyBackup.versionTime).[toISOString](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/precise-date/precisedate.html)()}`,
          );
        } else {
          console.error('ERROR: Copy of backup is not ready.');
        }
      } catch (err) {
        console.error('ERROR:', err);
      }
    }
    spannerCopyBackup();

**Note:** The old client library interface code samples for Node.js are archived in [GitHub](https://github.com/googleapis/nodejs-spanner/tree/main/samples/archived). 

### PHP
    
    
    use Google\Cloud\Spanner\Admin\Database\V1\CopyBackupRequest;
    use Google\Cloud\Spanner\Admin\Database\V1\Client\DatabaseAdminClient;
    use Google\Protobuf\Timestamp;
    
    /**
     * Create a copy backup from another source backup.
     * Example:
     * ```
     * copy_backup($projectId, $destInstanceId, $destBackupId, $sourceInstanceId, $sourceBackupId);
     * ```
     *
     * @param string $projectId The Google Cloud project ID.
     * @param string $destInstanceId The Spanner instance ID where the copy backup will reside.
     * @param string $destBackupId The Spanner backup ID of the new backup to be created.
     * @param string $sourceInstanceId The Spanner instance ID of the source backup.
     * @param string $sourceBackupId The Spanner backup ID of the source.
     */
    function copy_backup(
        string $projectId,
        string $destInstanceId,
        string $destBackupId,
        string $sourceInstanceId,
        string $sourceBackupId
    ): void {
        $databaseAdminClient = new DatabaseAdminClient();
    
        $destInstanceFullName = DatabaseAdminClient::instanceName($projectId, $destInstanceId);
        $expireTime = new Timestamp();
        $expireTime->setSeconds((new \DateTime('+8 hours'))->getTimestamp());
        $sourceBackupFullName = DatabaseAdminClient::backupName($projectId, $sourceInstanceId, $sourceBackupId);
        $request = new CopyBackupRequest([
            'source_backup' => $sourceBackupFullName,
            'parent' => $destInstanceFullName,
            'backup_id' => $destBackupId,
            'expire_time' => $expireTime
        ]);
    
        $operationResponse = $databaseAdminClient->copyBackup($request);
        $operationResponse->pollUntilComplete();
    
        if ($operationResponse->operationSucceeded()) {
            $destBackupInfo = $operationResponse->getResult();
            printf(
                'Backup %s of size %d bytes was copied at %d from the source backup %s' . PHP_EOL,
                basename($destBackupInfo->getName()),
                $destBackupInfo->getSizeBytes(),
                $destBackupInfo->getCreateTime()->getSeconds(),
                $sourceBackupId
            );
            printf('Version time of the copied backup: %d' . PHP_EOL, $destBackupInfo->getVersionTime()->getSeconds());
        } else {
            $error = $operationResponse->getError();
            printf('Backup not created due to error: %s.' . PHP_EOL, $error->getMessage());
        }
    }

**Note:** The old client library interface code samples for PHP are archived in [GitHub](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/main/spanner/src/admin/archived). 

### Python
    
    
    def copy_backup(instance_id, backup_id, source_backup_path):
        """Copies a backup."""
    
        from google.cloud.spanner_admin_database_v1.types import backup as backup_pb
    
        spanner_client = spanner.Client()
        database_admin_api = spanner_client.database_admin_api
    
        # Create a backup object and wait for copy backup operation to complete.
        expire_time = datetime.utcnow() + timedelta(days=14)
        request = backup_pb.CopyBackupRequest(
            parent=database_admin_api.instance_path(spanner_client.project, instance_id),
            backup_id=backup_id,
            source_backup=source_backup_path,
            expire_time=expire_time,
        )
    
        operation = database_admin_api.copy_backup(request)
    
        # Wait for backup operation to complete.
        copy_backup = operation.result(2100)
    
        # Verify that the copy backup is ready.
        assert copy_backup.state == backup_pb.Backup.State.READY
    
        print(
            "Backup {} of size {} bytes was created at {} with version time {}".format(
                copy_backup.name,
                copy_backup.size_bytes,
                copy_backup.create_time,
                copy_backup.version_time,
            )
        )
    
    

**Note:** The old client library interface code samples for Python are archived in [GitHub](https://github.com/googleapis/python-spanner/tree/main/samples/samples/archived). 

### Ruby
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "The ID of the destination instance that will contain the backup copy"
    # backup_id = "The ID of the backup copy"
    # source_backup = "The source backup to be copied"
    
    require "google/cloud/spanner"
    require "google/cloud/spanner/admin/database"
    
    database_admin_client = Google::Cloud::Spanner::Admin::Database.database_admin
    
    instance_path = database_admin_client.instance_path project: project_id, instance: instance_id
    backup_path = database_admin_client.backup_path project: project_id,
                                                    instance: instance_id,
                                                    backup: backup_id
    source_backup = database_admin_client.backup_path project: project_id,
                                                      instance: instance_id,
                                                      backup: source_backup_id
    
    expire_time = Time.now + (14 * 24 * 3600) # 14 days from now
    
    job = database_admin_client.copy_backup parent: instance_path,
                                            backup_id: backup_id,
                                            source_backup: source_backup,
                                            expire_time: expire_time
    
    puts "Copy backup operation in progress"
    
    job.wait_until_done!
    
    backup = database_admin_client.get_backup name: backup_path
    puts "Backup #{backup_id} of size #{backup.size_bytes} bytes was copied at #{backup.create_time} from #{source_backup} for version #{backup.version_time}"

## Check the operation progress

### Console

  1. In the Google Cloud console, go to the Spanner **Instances** page.

[Go to Instances](https://console.cloud.google.com/spanner/instances)

  2. Click the instance that contains the database that you want to view the backup operation for.

  3. Click the database.

  4. In the navigation pane, click **Operations**. The **Operations** page shows a list of running operations.




###  gcloud 

Use [`gcloud spanner operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/operations/describe) to check the progress of an operation.

  1. Get the operation ID:

Before using any of the command data below, make the following replacements: 

     * INSTANCE_NAME: the Spanner instance name.
     * DATABASE_NAME: the Spanner database name.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud spanner operations list --instance=INSTANCE_NAME \
    --database=DATABASE_NAME --type=backup

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud spanner operations list --instance=INSTANCE_NAME `
    --database=DATABASE_NAME --type=backup

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud spanner operations list --instance=INSTANCE_NAME ^
    --database=DATABASE_NAME --type=backup

You should receive a response similar to the following:
    
    OPERATION_ID     DONE  @TYPE                 BACKUP          SOURCE_DATABASE       START_TIME                   END_TIME
    _auto_op_123456  True  CreateBackupMetadata  example-db-backup-7  example-db       2020-02-04T02:12:38.075515Z  2020-02-04T02:22:40.581170Z
    _auto_op_234567  True  CreateBackupMetadata  example-db-backup-6  example-db       2020-02-04T02:05:43.920377Z  2020-02-04T02:07:59.089820Z
    

Usage notes:

     * To limit the list, specify the `--filter` flag. For example:

       * `--filter="metadata.name:example-db"` only lists the operations on a specific database.
       * `--filter="error:*"` only lists the backup operations that failed.

For information on filter syntax, see [`gcloud topic filters`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters). For information on filtering backup operations, see the `filter` field in [`ListBackupOperationsRequest`](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#listbackupoperationsrequest).

     * The `--type` flag isn't case sensitive.

  2. Run `gcloud spanner operations describe`:

Before using any of the command data below, make the following replacements: 

     * OPERATION_ID: the operation ID.
     * INSTANCE_NAME: the Spanner instance name.
     * DATABASE_NAME: the Spanner database name.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud spanner operations describe OPERATION_ID \
    --instance=INSTANCE_NAME \
    --backup=BACKUP_NAME \

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud spanner operations describe OPERATION_ID `
    --instance=INSTANCE_NAME `
    --backup=BACKUP_NAME `

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud spanner operations describe OPERATION_ID ^
    --instance=INSTANCE_NAME ^
    --backup=BACKUP_NAME ^

You should receive a response similar to the following:
    
    done: true
    metadata:
    ...
    progress:
    - endTime: '2022-03-01T00:28:06.691403Z'
      progressPercent: 100
      startTime: '2022-03-01T00:28:04.221401Z'
    - endTime: '2022-03-01T00:28:17.624588Z'
      startTime: '2022-03-01T00:28:06.691403Z'
      progressPercent: 100
    ...
    

The `progress` section in the output shows the percentage of the operation that's complete. 

If the operation takes too long, you can cancel it. For more information, see [Cancel a long-running backup operation](https://docs.cloud.google.com/spanner/docs/manage-and-observe-long-running-operations#cancel_a_long-running_backup_operation).




### Client libraries

The following code sample lists all of the ongoing operations for creating backups (operations with [`CreateBackupMetadata`](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/CreateBackupMetadata)) and copying backups (operations with [`CopyBackupMetadata`](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/CopyBackupMetadata)) filtered by a given database.

For information on filtering syntax, see the `filter` parameter in [`backupOperations.list`](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backupOperations/list#query-parameters).

###  C++ 
    
    
    void ListBackupOperations(
        google::cloud::spanner_admin::DatabaseAdminClient client,
        std::string const& project_id, std::string const& instance_id,
        std::string const& database_id, std::string const& backup_id) {
      google::cloud::spanner::Instance in(project_id, instance_id);
      google::cloud::spanner::Database database(in, database_id);
      google::cloud::spanner::Backup backup(in, backup_id);
    
      google::spanner::admin::database::v1::ListBackupOperationsRequest request;
      request.set_parent(in.FullName());
    
      request.set_filter(std::string("(metadata.@type=type.googleapis.com/") +
                         "google.spanner.admin.database.v1.CreateBackupMetadata)" +
                         " AND (metadata.database=" + database.FullName() + ")");
      for (auto& operation : client.ListBackupOperations(request)) {
        if (!operation) throw std::move(operation).status();
        google::spanner::admin::database::v1::CreateBackupMetadata metadata;
        (void)operation->metadata().UnpackTo(&metadata);
        std::cout << "Backup " << metadata.name() << " of database "
                  << metadata.database() << " is "
                  << metadata.progress().progress_percent() << "% complete.\n";
      }
    
      request.set_filter(std::string("(metadata.@type:type.googleapis.com/") +
                         "google.spanner.admin.database.v1.CopyBackupMetadata)" +
                         " AND (metadata.source_backup=" + backup.FullName() + ")");
      for (auto& operation : client.ListBackupOperations(request)) {
        if (!operation) throw std::move(operation).status();
        google::spanner::admin::database::v1::CopyBackupMetadata metadata;
        (void)operation->metadata().UnpackTo(&metadata);
        std::cout << "Copy " << metadata.name() << " of backup "
                  << metadata.source_backup() << " is "
                  << metadata.progress().progress_percent() << "% complete.\n";
      }
    }

###  C# 

To list all the create backup operations: 
    
    
    using [Google.Cloud.Spanner.Admin.Database.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.html);
    using [Google.Cloud.Spanner.Common.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using System;
    using System.Collections.Generic;
    
    public class ListBackupOperationsSample
    {
        public IEnumerable<Operation> ListBackupOperations(string projectId, string instanceId, string databaseId)
        {
            // Create the DatabaseAdminClient instance.
            [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html) databaseAdminClient = [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_Create)();
    
            var filter = $"(metadata.@type:type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata) AND (metadata.database:{databaseId})";
            [ListBackupOperationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.ListBackupOperationsRequest.html) request = new [ListBackupOperationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.ListBackupOperationsRequest.html)
            {
                ParentAsInstanceName = [InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html).[FromProjectInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html#Google_Cloud_Spanner_Common_V1_InstanceName_FromProjectInstance_System_String_System_String_)(projectId, instanceId),
                Filter = filter
            };
    
            // List the create backup operations on the database.
            var backupOperations = databaseAdminClient.[ListBackupOperations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_ListBackupOperations_Google_Cloud_Spanner_Admin_Database_V1_ListBackupOperationsRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            foreach (var operation in backupOperations)
            {
                [CreateBackupMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupMetadata.html) metadata = operation.[Metadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html#Google_LongRunning_Operation_Metadata).Unpack<CreateBackupMetadata>();
                Console.WriteLine($"Backup {metadata.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupMetadata.html#Google_Cloud_Spanner_Admin_Database_V1_CreateBackupMetadata_Name)} on " + $"database {metadata.[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupMetadata.html#Google_Cloud_Spanner_Admin_Database_V1_CreateBackupMetadata_Database)} is " + $"{metadata.[Progress](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupMetadata.html#Google_Cloud_Spanner_Admin_Database_V1_CreateBackupMetadata_Progress).[ProgressPercent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.OperationProgress.html#Google_Cloud_Spanner_Admin_Database_V1_OperationProgress_ProgressPercent)}% complete");
            }
    
            return backupOperations;
        }
    }

To list all the copy backup operations: 
    
    
    using [Google.Cloud.Spanner.Admin.Database.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.html);
    using [Google.Cloud.Spanner.Common.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using System;
    using System.Collections.Generic;
    
    public class ListCopyBackupOperationsSample
    {
        public IEnumerable<Operation> ListCopyBackupOperations(string projectId, string instanceId, string databaseId, string backupId)
        {
            // Create the DatabaseAdminClient instance.
            [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html) databaseAdminClient = [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_Create)();
    
            var filter = $"(metadata.@type:type.googleapis.com/google.spanner.admin.database.v1.CopyBackupMetadata) AND (metadata.source_backup:{backupId})";
            [ListBackupOperationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.ListBackupOperationsRequest.html) request = new [ListBackupOperationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.ListBackupOperationsRequest.html)
            {
                ParentAsInstanceName = [InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html).[FromProjectInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html#Google_Cloud_Spanner_Common_V1_InstanceName_FromProjectInstance_System_String_System_String_)(projectId, instanceId),
                Filter = filter
            };
    
            // List the copy backup operations on the database.
            var backupOperations = databaseAdminClient.[ListBackupOperations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_ListBackupOperations_Google_Cloud_Spanner_Admin_Database_V1_ListBackupOperationsRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            foreach (var operation in backupOperations)
            {
                [CopyBackupMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CopyBackupMetadata.html) metadata = operation.[Metadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html#Google_LongRunning_Operation_Metadata).Unpack<CopyBackupMetadata>();
                Console.WriteLine($"Backup {metadata.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CopyBackupMetadata.html#Google_Cloud_Spanner_Admin_Database_V1_CopyBackupMetadata_Name)} from source backup {metadata.[SourceBackup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CopyBackupMetadata.html#Google_Cloud_Spanner_Admin_Database_V1_CopyBackupMetadata_SourceBackup)} is {metadata.[Progress](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CopyBackupMetadata.html#Google_Cloud_Spanner_Admin_Database_V1_CopyBackupMetadata_Progress).[ProgressPercent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.OperationProgress.html#Google_Cloud_Spanner_Admin_Database_V1_OperationProgress_ProgressPercent)}% complete");
            }
    
            return backupOperations;
        }
    }
    

###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"regexp"
    
    	database "cloud.google.com/go/spanner/admin/database/apiv1"
    	adminpb "cloud.google.com/go/spanner/admin/database/apiv1/databasepb"
    	"github.com/golang/protobuf/ptypes"
    	"google.golang.org/api/iterator"
    )
    
    // listBackupOperations lists the backup operations that are pending or have completed/failed/cancelled within the last 7 days.
    func listBackupOperations(w io.Writer, db string, backupId string) error {
    	// db := "projects/my-project/instances/my-instance/databases/my-database"
    	// backupID := "my-backup"
    
    	ctx := context.Background()
    
    	adminClient, err := database.NewDatabaseAdminClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer adminClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/database/apiv1.html#cloud_google_com_go_spanner_admin_database_apiv1_DatabaseAdminClient_Close)()
    
    	matches := regexp.MustCompile("^(.*)/databases/(.*)$").FindStringSubmatch(db)
    	if matches == nil || len(matches) != 3 {
    		return fmt.Errorf("Invalid database id %s", db)
    	}
    	instanceName := matches[1]
    	// List the CreateBackup operations.
    	filter := fmt.Sprintf("(metadata.@type:type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata) AND (metadata.database:%s)", db)
    	iter := adminClient.ListBackupOperations(ctx, &adminpb.ListBackupOperationsRequest{
    		Parent: instanceName,
    		Filter: filter,
    	})
    	for {
    		resp, err := iter.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return err
    		}
    		metadata := &adminpb.CreateBackupMetadata{}
    		if err := ptypes.UnmarshalAny(resp.Metadata, metadata); err != nil {
    			return err
    		}
    		fmt.Fprintf(w, "Backup %s on database %s is %d%% complete.\n",
    			metadata.Name,
    			metadata.Database,
    			metadata.Progress.ProgressPercent,
    		)
    	}
    
    	// List the CopyBackup operations.
    	filter = fmt.Sprintf("(metadata.@type:type.googleapis.com/google.spanner.admin.database.v1.CopyBackupMetadata) AND (metadata.source_backup:%s)", backupId)
    	iter = adminClient.ListBackupOperations(ctx, &adminpb.ListBackupOperationsRequest{
    		Parent: instanceName,
    		Filter: filter,
    	})
    	for {
    		resp, err := iter.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return err
    		}
    		metadata := &adminpb.CopyBackupMetadata{}
    		if err := ptypes.UnmarshalAny(resp.Metadata, metadata); err != nil {
    			return err
    		}
    		fmt.Fprintf(w, "Backup %s copied from %s is %d%% complete.\n",
    			metadata.Name,
    			metadata.SourceBackup,
    			metadata.Progress.ProgressPercent,
    		)
    	}
    
    	return nil
    }
    

###  Java 
    
    
    static void listBackupOperations(
        DatabaseAdminClient databaseAdminClient,
        String projectId, String instanceId,
        String databaseId, String backupId) {
      InstanceName instanceName = InstanceName.of(projectId, instanceId);
      // Get 'CreateBackup' operations for the sample database.
      String filter =
          String.format(
              "(metadata.@type:type.googleapis.com/"
                  + "google.spanner.admin.database.v1.CreateBackupMetadata) "
                  + "AND (metadata.database:%s)",
              DatabaseName.of(projectId, instanceId, databaseId).toString());
      ListBackupOperationsRequest listBackupOperationsRequest =
          ListBackupOperationsRequest.newBuilder()
              .setParent(instanceName.toString()).setFilter(filter).build();
      ListBackupOperationsPagedResponse createBackupOperations
          = databaseAdminClient.listBackupOperations(listBackupOperationsRequest);
      System.out.println("Create Backup Operations:");
      for (Operation op : createBackupOperations.iterateAll()) {
        try {
          CreateBackupMetadata metadata = op.getMetadata().unpack(CreateBackupMetadata.class);
          System.out.println(
              String.format(
                  "Backup %s on database %s pending: %d%% complete",
                  metadata.getName(),
                  metadata.getDatabase(),
                  metadata.getProgress().getProgressPercent()));
        } catch (InvalidProtocolBufferException e) {
          // The returned operation does not contain CreateBackupMetadata.
          System.err.println(e.getMessage());
        }
      }
      // Get copy backup operations for the sample database.
      filter = String.format(
          "(metadata.@type:type.googleapis.com/"
              + "google.spanner.admin.database.v1.CopyBackupMetadata) "
              + "AND (metadata.source_backup:%s)",
          BackupName.of(projectId, instanceId, backupId).toString());
      listBackupOperationsRequest =
          ListBackupOperationsRequest.newBuilder()
              .setParent(instanceName.toString()).setFilter(filter).build();
      ListBackupOperationsPagedResponse copyBackupOperations =
          databaseAdminClient.listBackupOperations(listBackupOperationsRequest);
      System.out.println("Copy Backup Operations:");
      for (Operation op : copyBackupOperations.iterateAll()) {
        try {
          CopyBackupMetadata copyBackupMetadata =
              op.getMetadata().unpack(CopyBackupMetadata.class);
          System.out.println(
              String.format(
                  "Copy Backup %s on backup %s pending: %d%% complete",
                  copyBackupMetadata.getName(),
                  copyBackupMetadata.getSourceBackup(),
                  copyBackupMetadata.getProgress().getProgressPercent()));
        } catch (InvalidProtocolBufferException e) {
          // The returned operation does not contain CopyBackupMetadata.
          System.err.println(e.getMessage());
        }
      }
    }

**Note:** The old client library interface code samples for Java are archived in [GitHub](https://github.com/googleapis/google-cloud-java/tree/main/java-spanner/samples/snippets/src/main/java/com/example/spanner/admin/archived). 

###  Node.js 
    
    
    // Imports the Google Cloud client library
    const {Spanner, protos} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const projectId = 'my-project-id';
    // const databaseId = 'my-database';
    // const backupId = 'my-backup';
    // const instanceId = 'my-instance';
    
    // Creates a client
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({
      projectId: projectId,
    });
    
    // Gets a reference to a Cloud Spanner Database Admin Client object
    const databaseAdminClient = spanner.[getDatabaseAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)();
    
    // List create backup operations
    try {
      const [backupOperations] = await databaseAdminClient.listBackupOperations({
        parent: databaseAdminClient.instancePath(projectId, instanceId),
        filter:
          '(metadata.@type:type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata) ' +
          `AND (metadata.database:${databaseId})`,
      });
      console.log('Create Backup Operations:');
      backupOperations.forEach(backupOperation => {
        const metadata =
          protos.google.spanner.admin.database.v1.CreateBackupMetadata.decode(
            backupOperation.metadata.value,
          );
        console.log(
          `Backup ${metadata.name} on database ${metadata.database} is ` +
            `${metadata.progress.progressPercent}% complete.`,
        );
      });
    } catch (err) {
      console.error('ERROR:', err);
    }
    
    // List copy backup operations
    try {
      console.log(
        '(metadata.@type:type.googleapis.com/google.spanner.admin.database.v1.CopyBackupMetadata) ' +
          `AND (metadata.source_backup:${backupId})`,
      );
      const [backupOperations] = await databaseAdminClient.listBackupOperations({
        parent: databaseAdminClient.instancePath(projectId, instanceId),
        filter:
          '(metadata.@type:type.googleapis.com/google.spanner.admin.database.v1.CopyBackupMetadata) ' +
          `AND (metadata.source_backup:${backupId})`,
      });
      console.log('Copy Backup Operations:');
      backupOperations.forEach(backupOperation => {
        const metadata =
          protos.google.spanner.admin.database.v1.CopyBackupMetadata.decode(
            backupOperation.metadata.value,
          );
        console.log(
          `Backup ${metadata.name} copied from source backup ${metadata.sourceBackup} is ` +
            `${metadata.progress.progressPercent}% complete.`,
        );
      });
    } catch (err) {
      console.error('ERROR:', err);
    }

**Note:** The old client library interface code samples for Node.js are archived in [GitHub](https://github.com/googleapis/nodejs-spanner/tree/main/samples/archived). 

###  PHP 
    
    
    use Google\Cloud\Spanner\Admin\Database\V1\Client\DatabaseAdminClient;
    use Google\Cloud\Spanner\Admin\Database\V1\CreateBackupMetadata;
    use Google\Cloud\Spanner\Admin\Database\V1\CopyBackupMetadata;
    use Google\Cloud\Spanner\Admin\Database\V1\ListBackupOperationsRequest;
    
    /**
     * List all create backup operations in an instance.
     * Optionally passing the backupId will also list the
     * copy backup operations on the backup.
     *
     * @param string $projectId The Google Cloud project ID.
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     * @param string $backupId The Spanner backup ID whose copy operations need to be listed.
     */
    function list_backup_operations(
        string $projectId,
        string $instanceId,
        string $databaseId,
        string $backupId
    ): void {
        $databaseAdminClient = new DatabaseAdminClient();
    
        $parent = DatabaseAdminClient::instanceName($projectId, $instanceId);
    
        // List the CreateBackup operations.
        $filterCreateBackup = '(metadata.@type:type.googleapis.com/' .
            'google.spanner.admin.database.v1.CreateBackupMetadata) AND ' . "(metadata.database:$databaseId)";
    
        // See https://cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#listbackupoperationsrequest
        // for the possible filter values
        $filterCopyBackup = sprintf('(metadata.@type:type.googleapis.com/' .
            'google.spanner.admin.database.v1.CopyBackupMetadata) AND ' . "(metadata.source_backup:$backupId)");
        $operations = $databaseAdminClient->listBackupOperations(
            new ListBackupOperationsRequest([
                'parent' => $parent,
                'filter' => $filterCreateBackup
            ])
        );
    
        foreach ($operations->iterateAllElements() as $operation) {
            $obj = new CreateBackupMetadata();
            $meta = $operation->getMetadata()->unpack($obj);
            $backupName = basename($meta->getName());
            $dbName = basename($meta->getDatabase());
            $progress = $meta->getProgress()->getProgressPercent();
            printf('Backup %s on database %s is %d%% complete.' . PHP_EOL, $backupName, $dbName, $progress);
        }
    
        $operations = $databaseAdminClient->listBackupOperations(
            new ListBackupOperationsRequest([
                'parent' => $parent,
                'filter' => $filterCopyBackup
            ])
        );
    
        foreach ($operations->iterateAllElements() as $operation) {
            $obj = new CopyBackupMetadata();
            $meta = $operation->getMetadata()->unpack($obj);
            $backupName = basename($meta->getName());
            $progress = $meta->getProgress()->getProgressPercent();
            printf('Copy Backup %s on source backup %s is %d%% complete.' . PHP_EOL, $backupName, $backupId, $progress);
        }
    }

**Note:** The old client library interface code samples for PHP are archived in [GitHub](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/main/spanner/src/admin/archived). 

###  Python 
    
    
    def list_backup_operations(instance_id, database_id, backup_id):
        from google.cloud.spanner_admin_database_v1.types import backup as backup_pb
    
        spanner_client = spanner.Client()
        database_admin_api = spanner_client.database_admin_api
    
        # List the CreateBackup operations.
        filter_ = (
            "(metadata.@type:type.googleapis.com/"
            "google.spanner.admin.database.v1.CreateBackupMetadata) "
            "AND (metadata.database:{})"
        ).format(database_id)
        request = backup_pb.ListBackupOperationsRequest(
            parent=database_admin_api.instance_path(spanner_client.project, instance_id),
            filter=filter_,
        )
        operations = database_admin_api.list_backup_operations(request)
        for op in operations:
            metadata = protobuf_helpers.from_any_pb(
                backup_pb.CreateBackupMetadata, op.metadata
            )
            print(
                "Backup {} on database {}: {}% complete.".format(
                    metadata.name, metadata.database, metadata.progress.progress_percent
                )
            )
    
        # List the CopyBackup operations.
        filter_ = (
            "(metadata.@type:type.googleapis.com/google.spanner.admin.database.v1.CopyBackupMetadata) "
            "AND (metadata.source_backup:{})"
        ).format(backup_id)
        request = backup_pb.ListBackupOperationsRequest(
            parent=database_admin_api.instance_path(spanner_client.project, instance_id),
            filter=filter_,
        )
        operations = database_admin_api.list_backup_operations(request)
        for op in operations:
            metadata = protobuf_helpers.from_any_pb(
                backup_pb.CopyBackupMetadata, op.metadata
            )
            print(
                "Backup {} on source backup {}: {}% complete.".format(
                    metadata.name,
                    metadata.source_backup,
                    metadata.progress.progress_percent,
                )
            )
    
    

**Note:** The old client library interface code samples for Python are archived in [GitHub](https://github.com/googleapis/python-spanner/tree/main/samples/samples/archived). 

###  Ruby 

To list all the create backup operations: 
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "Your Spanner instance ID"
    # database_id = "Your Spanner database ID"
    
    require "google/cloud/spanner"
    require "google/cloud/spanner/admin/database"
    
    database_admin_client = Google::Cloud::Spanner::Admin::Database.database_admin
    instance_path = database_admin_client.instance_path project: project_id, instance: instance_id
    
    jobs = database_admin_client.list_backup_operations parent: instance_path,
                                                        filter: "metadata.@type:type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata"
    jobs.each do |job|
      if job.error?
        puts job.error
      else
        puts "Backup #{job.results.name} on database #{database_id} is #{job.metadata.progress.progress_percent}% complete"
      end
    end

To list all the copy backup operations: 
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "Your Spanner instance ID"
    # backup_id = "You Spanner backup ID"
    
    require "google/cloud/spanner"
    require "google/cloud/spanner/admin/database"
    
    database_admin_client = Google::Cloud::Spanner::Admin::Database.database_admin
    instance_path = database_admin_client.instance_path project: project_id, instance: instance_id
    
    filter = "(metadata.@type:type.googleapis.com/google.spanner.admin.database.v1.CopyBackupMetadata) AND (metadata.source_backup:#{backup_id})"
    
    jobs = database_admin_client.list_backup_operations parent: instance_path,
                                                        filter: filter
    jobs.each do |job|
      if job.error?
        puts job.error
      else
        puts "Backup #{job.results.name} on source backup #{backup_id} is #{job.metadata.progress.progress_percent}% complete"
      end
    end

## Cancel a backup operation

### Console

The Google Cloud console doesn't support canceling a backup operation. However, you can cancel operations that take too long using the gcloud CLI, REST, or RPC API. For more information, see [Cancel a long-running instance operation](https://docs.cloud.google.com/spanner/docs/manage-and-observe-long-running-operations#cancel_a_long-running_instance_operation).

###  gcloud 

  1. Get the operation ID:

Before using any of the command data below, make the following replacements: 

     * INSTANCE_NAME: the Spanner instance name.
     * DATABASE_NAME: the Spanner database name.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud spanner operations list --instance=INSTANCE_NAME \
    --database=DATABASE_NAME --type=backup

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud spanner operations list --instance=INSTANCE_NAME `
    --database=DATABASE_NAME --type=backup

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud spanner operations list --instance=INSTANCE_NAME ^
    --database=DATABASE_NAME --type=backup

You should receive a response similar to the following:
    
    OPERATION_ID     DONE  @TYPE                 BACKUP          SOURCE_DATABASE       START_TIME                   END_TIME
    _auto_op_123456  True  CreateBackupMetadata  example-db-backup-7  example-db       2020-02-04T02:12:38.075515Z  2020-02-04T02:22:40.581170Z
    _auto_op_234567  True  CreateBackupMetadata  example-db-backup-6  example-db       2020-02-04T02:05:43.920377Z  2020-02-04T02:07:59.089820Z
    

Usage notes:

     * To limit the list, specify the `--filter` flag. For example:

       * `--filter="metadata.name:example-db"` only lists the operations on a specific database.
       * `--filter="error:*"` only lists the backup operations that failed.

For information on filter syntax, see [`gcloud topic filters`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters). For information on filtering backup operations, see the `filter` field in [`ListBackupOperationsRequest`](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#listbackupoperationsrequest).

     * The `--type` flag isn't case sensitive.

  2. Use [`gcloud spanner operations cancel`](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/operations/cancel) to cancel a backup operation. 

Before using any of the command data below, make the following replacements: 

     * OPERATION_ID: the operation ID.
     * INSTANCE_NAME: the Spanner instance name.
     * DATABASE_NAME: the Spanner database name.
     * BACKUP_NAME: the Spanner backup name.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud spanner operations cancel OPERATION_ID --instance=INSTANCE_NAME \
     --database=DATABASE_NAME --backup=BACKUP_NAME

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud spanner operations cancel OPERATION_ID --instance=INSTANCE_NAME `
     --database=DATABASE_NAME --backup=BACKUP_NAME

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud spanner operations cancel OPERATION_ID --instance=INSTANCE_NAME ^
     --database=DATABASE_NAME --backup=BACKUP_NAME




### Client libraries

The following code sample creates a backup, cancels the backup operation, and then waits until the backup operation is `done`. If the operation was successfully cancelled, it returns the `cancelTime` and an error message. If the backup operation was completed before it was cancelled, the backup exists, and you can delete it.

### C++
    
    
    void CreateBackupAndCancel(
        google::cloud::spanner_admin::DatabaseAdminClient client,
        std::string const& project_id, std::string const& instance_id,
        std::string const& database_id, std::string const& backup_id,
        google::cloud::spanner::Timestamp expire_time) {
      google::cloud::spanner::Database database(project_id, instance_id,
                                                database_id);
      google::spanner::admin::database::v1::CreateBackupRequest request;
      request.set_parent(database.instance().FullName());
      request.set_backup_id(backup_id);
      request.mutable_backup()->set_database(database.FullName());
      *request.mutable_backup()->mutable_expire_time() =
          expire_time.get<google::protobuf::Timestamp>().value();
      auto f = client.CreateBackup(request);
      f.cancel();
      auto backup = f.get();
      if (backup) {
        auto status = client.DeleteBackup(backup->name());
        if (!status.ok()) throw std::move(status);
        std::cout << "Backup " << backup->name() << " was deleted.\n";
      } else {
        std::cout << "CreateBackup operation was cancelled with the message '"
                  << backup.status().message() << "'.\n";
      }
    }

### C#
    
    
    using [Google.Cloud.Spanner.Admin.Database.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.html);
    using [Google.Cloud.Spanner.Common.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    
    public class CancelBackupOperationSample
    {
        public Operation<Backup, CreateBackupMetadata> CancelBackupOperation(string projectId, string instanceId, string databaseId, string backupId)
        {
            // Create the DatabaseAdminClient instance.
            [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html) databaseAdminClient = [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_Create)();
    
            // Initialize backup request parameters.
            [Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html) backup = new [Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html)
            {
                DatabaseAsDatabaseName = [DatabaseName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.DatabaseName.html).[FromProjectInstanceDatabase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.DatabaseName.html#Google_Cloud_Spanner_Common_V1_DatabaseName_FromProjectInstanceDatabase_System_String_System_String_System_String_)(projectId, instanceId, databaseId),
                ExpireTime = DateTime.UtcNow.AddDays(14).[ToTimestamp](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.TimeExtensions.html#Google_Protobuf_WellKnownTypes_TimeExtensions_ToTimestamp_System_DateTime_)()
            };
            [InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html) parentAsInstanceName = [InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html).[FromProjectInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html#Google_Cloud_Spanner_Common_V1_InstanceName_FromProjectInstance_System_String_System_String_)(projectId, instanceId);
    
            // Make the CreateBackup request.
            Operation<Backup, CreateBackupMetadata> operation = databaseAdminClient.[CreateBackup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_CreateBackup_Google_Cloud_Spanner_Admin_Database_V1_CreateBackupRequest_Google_Api_Gax_Grpc_CallSettings_)(parentAsInstanceName, backup, backupId);
    
            // Cancel the operation.
            operation.Cancel();
    
            // Poll until the long-running operation is completed in case the backup was
            // created before the operation was cancelled.
            Console.WriteLine("Waiting for the operation to finish.");
            Operation<Backup, CreateBackupMetadata> completedOperation = operation.PollUntilCompleted();
    
            if (completedOperation.IsFaulted)
            {
                Console.WriteLine($"Create backup operation cancelled: {operation.Name}");
            }
            else
            {
                Console.WriteLine("The backup was created before the operation was cancelled. Backup needs to be deleted.");
                [BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupName.html) backupAsBackupName = [BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupName.html).[FromProjectInstanceBackup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupName.html#Google_Cloud_Spanner_Admin_Database_V1_BackupName_FromProjectInstanceBackup_System_String_System_String_System_String_)(projectId, instanceId, backupId);
                databaseAdminClient.[DeleteBackup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_DeleteBackup_Google_Cloud_Spanner_Admin_Database_V1_BackupName_Google_Api_Gax_Grpc_CallSettings_)(backupAsBackupName);
            }
    
            return completedOperation;
        }
    }

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"regexp"
    	"time"
    
    	longrunning "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	database "cloud.google.com/go/spanner/admin/database/apiv1"
    	adminpb "cloud.google.com/go/spanner/admin/database/apiv1/databasepb"
    	pbt "github.com/golang/protobuf/ptypes/timestamp"
    	"google.golang.org/grpc/codes"
    	"google.golang.org/grpc/status"
    )
    
    func cancelBackup(ctx context.Context, w io.Writer, db, backupID string) error {
    	matches := regexp.MustCompile("^(.+)/databases/(.+)$").FindStringSubmatch(db)
    	if matches == nil || len(matches) != 3 {
    		return fmt.Errorf("cancelBackup: invalid database id %q", db)
    	}
    
    	adminClient, err := database.NewDatabaseAdminClient(ctx)
    	if err != nil {
    		return fmt.Errorf("cancelBackup.NewDatabaseAdminClient: %w", err)
    	}
    	defer adminClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/database/apiv1.html#cloud_google_com_go_spanner_admin_database_apiv1_DatabaseAdminClient_Close)()
    
    	expireTime := time.Now().AddDate(0, 0, 14)
    	// Create a backup.
    	req := adminpb.CreateBackupRequest{
    		Parent:   matches[1],
    		BackupId: backupID,
    		Backup: &adminpb.Backup{
    			Database:   db,
    			ExpireTime: &pbt.Timestamp{Seconds: expireTime.Unix(), Nanos: int32(expireTime.Nanosecond())},
    		},
    	}
    	op, err := adminClient.CreateBackup(ctx, &req)
    	if err != nil {
    		return fmt.Errorf("cancelBackup.CreateBackup: %w", err)
    	}
    
    	// Cancel backup creation.
    	err = adminClient.LROClient.CancelOperation(ctx, &longrunning.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){Name: op.Name()})
    	if err != nil {
    		return fmt.Errorf("cancelBackup.CancelOperation: %w", err)
    	}
    
    	// Cancel operations are best effort so either it will complete or be
    	// cancelled.
    	backup, err := op.Wait(ctx)
    	if err != nil {
    		if waitStatus, ok := status.FromError(err); !ok || waitStatus.Code() != codes.Canceled {
    			return fmt.Errorf("cancelBackup.Wait: %w", err)
    		}
    	} else {
    		// Backup was completed before it could be cancelled so delete the
    		// unwanted backup.
    		err = adminClient.DeleteBackup(ctx, &adminpb.DeleteBackupRequest{Name: backup.Name})
    		if err != nil {
    			return fmt.Errorf("cancelBackup.DeleteBackup: %w", err)
    		}
    	}
    
    	fmt.Fprintf(w, "Backup cancelled.\n")
    	return nil
    }
    

### Java
    
    
    static void cancelCreateBackup(
        DatabaseAdminClient dbAdminClient, String projectId, String instanceId,
        String databaseId, String backupId) {
      // Set expire time to 14 days from now.
      Timestamp expireTime =
          Timestamp.newBuilder().setSeconds(TimeUnit.MILLISECONDS.toSeconds((
              System.currentTimeMillis() + TimeUnit.DAYS.toMillis(14)))).build();
      BackupName backupName = BackupName.of(projectId, instanceId, backupId);
      Backup backup = Backup.newBuilder()
          .setName(backupName.toString())
          .setDatabase(DatabaseName.of(projectId, instanceId, databaseId).toString())
          .setExpireTime(expireTime).build();
    
      try {
        // Start the creation of a backup.
        System.out.println("Creating backup [" + backupId + "]...");
        OperationFuture<Backup, CreateBackupMetadata> op = dbAdminClient.createBackupAsync(
            InstanceName.of(projectId, instanceId), backup, backupId);
    
        // Try to cancel the backup operation.
        System.out.println("Cancelling create backup operation for [" + backupId + "]...");
        dbAdminClient.getOperationsClient().cancelOperation(op.getName());
    
        // Get a polling future for the running operation. This future will regularly poll the server
        // for the current status of the backup operation.
        RetryingFuture<OperationSnapshot> pollingFuture = op.getPollingFuture();
    
        // Wait for the operation to finish.
        // isDone will return true when the operation is complete, regardless of whether it was
        // successful or not.
        while (!pollingFuture.get().isDone()) {
          System.out.println("Waiting for the cancelled backup operation to finish...");
          Thread.sleep(TimeUnit.MILLISECONDS.convert(5, TimeUnit.SECONDS));
        }
        if (pollingFuture.get().getErrorCode() == null) {
          // Backup was created before it could be cancelled. Delete the backup.
          dbAdminClient.deleteBackup(backupName);
          System.out.println("Backup operation for [" + backupId
              + "] successfully finished before it could be cancelled");
        } else if (pollingFuture.get().getErrorCode().getCode() == StatusCode.Code.CANCELLED) {
          System.out.println("Backup operation for [" + backupId + "] successfully cancelled");
        }
      } catch (ExecutionException e) {
        throw SpannerExceptionFactory.newSpannerException(e.getCause());
      } catch (InterruptedException e) {
        throw SpannerExceptionFactory.propagateInterrupt(e);
      }
    }

**Note:** The old client library interface code samples for Java are archived in [GitHub](https://github.com/googleapis/google-cloud-java/tree/main/java-spanner/samples/snippets/src/main/java/com/example/spanner/admin/archived). 

### Node.js
    
    
    // Imports the Google Cloud client library and precise date library
    const {Spanner, protos} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const projectId = 'my-project-id';
    // const instanceId = 'my-instance';
    // const databaseId = 'my-database';
    // const backupId = 'my-backup';
    
    // Creates a client
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({
      projectId: projectId,
    });
    
    // Gets a reference to a Cloud Spanner Database Admin Client object
    const databaseAdminClient = spanner.[getDatabaseAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)();
    
    // Creates a new backup of the database
    try {
      console.log(
        `Creating backup of database ${databaseAdminClient.databasePath(
          projectId,
          instanceId,
          databaseId,
        )}.`,
      );
    
      // Expire backup one day in the future
      const expireTime = Date.now() + 1000 * 60 * 60 * 24;
      const [operation] = await databaseAdminClient.createBackup({
        parent: databaseAdminClient.instancePath(projectId, instanceId),
        backupId: backupId,
        backup: (protos.google.spanner.admin.database.v1.[Backup](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.database.v1.backup-class.html) = {
          database: databaseAdminClient.databasePath(
            projectId,
            instanceId,
            databaseId,
          ),
          expireTime: [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html).[timestamp](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)(expireTime).toStruct(),
          name: databaseAdminClient.backupPath(projectId, instanceId, backupId),
        }),
      });
    
      // Cancel the backup
      await operation.cancel();
    
      console.log('Backup cancelled.');
    } catch (err) {
      console.error('ERROR:', err);
    } finally {
      // Delete backup in case it got created before the cancel operation
      await databaseAdminClient.deleteBackup({
        name: databaseAdminClient.backupPath(projectId, instanceId, backupId),
      });
      // Close the spanner client when finished.
      // The databaseAdminClient does not require explicit closure. The closure of the Spanner client will automatically close the databaseAdminClient.
      spanner.close();
    }

**Note:** The old client library interface code samples for Node.js are archived in [GitHub](https://github.com/googleapis/nodejs-spanner/tree/main/samples/archived). 

### PHP
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Spanner\Admin\Database\V1\Backup;
    use Google\Cloud\Spanner\Admin\Database\V1\Client\DatabaseAdminClient;
    use Google\Cloud\Spanner\Admin\Database\V1\CreateBackupRequest;
    use Google\Cloud\Spanner\Admin\Database\V1\DeleteBackupRequest;
    use Google\Cloud\Spanner\Admin\Database\V1\GetBackupRequest;
    use Google\Protobuf\Timestamp;
    
    /**
     * Cancel a backup operation.
     * Example:
     * ```
     * cancel_backup($projectId, $instanceId, $databaseId);
     * ```
     *
     * @param string $projectId The Google Cloud project ID.
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     */
    function cancel_backup(string $projectId, string $instanceId, string $databaseId): void
    {
        $databaseAdminClient = new DatabaseAdminClient();
        $databaseFullName = DatabaseAdminClient::databaseName($projectId, $instanceId, $databaseId);
        $instanceFullName = DatabaseAdminClient::instanceName($projectId, $instanceId);
        $expireTime = new Timestamp();
        $expireTime->setSeconds((new \DateTime('+14 days'))->getTimestamp());
        $backupId = uniqid('backup-' . $databaseId . '-cancel');
        $request = new CreateBackupRequest([
            'parent' => $instanceFullName,
            'backup_id' => $backupId,
            'backup' => new Backup([
                'database' => $databaseFullName,
                'expire_time' => $expireTime
            ])
        ]);
    
        $operation = $databaseAdminClient->createBackup($request);
        $operation->cancel();
    
        // Cancel operations are always successful regardless of whether the operation is
        // still in progress or is complete.
        printf('Cancel backup operation complete.' . PHP_EOL);
    
        // Operation may succeed before cancel() has been called. So we need to clean up created backup.
        try {
            $request = new GetBackupRequest();
            $request->setName($databaseAdminClient->backupName($projectId, $instanceId, $backupId));
            $info = $databaseAdminClient->getBackup($request);
        } catch (ApiException $ex) {
            return;
        }
        $databaseAdminClient->deleteBackup(new DeleteBackupRequest([
            'name' => $databaseAdminClient->backupName($projectId, $instanceId, $backupId)
        ]));
    }

**Note:** The old client library interface code samples for PHP are archived in [GitHub](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/main/spanner/src/admin/archived). 

### Python
    
    
    def cancel_backup(instance_id, database_id, backup_id):
        from google.cloud.spanner_admin_database_v1.types import backup as backup_pb
    
        spanner_client = spanner.Client()
        database_admin_api = spanner_client.database_admin_api
    
        expire_time = datetime.utcnow() + timedelta(days=30)
    
        # Create a backup.
        request = backup_pb.CreateBackupRequest(
            parent=database_admin_api.instance_path(spanner_client.project, instance_id),
            backup_id=backup_id,
            backup=backup_pb.Backup(
                database=database_admin_api.database_path(
                    spanner_client.project, instance_id, database_id
                ),
                expire_time=expire_time,
            ),
        )
    
        operation = database_admin_api.create_backup(request)
        # Cancel backup creation.
        operation.cancel()
    
        # Cancel operations are the best effort so either it will complete or
        # be cancelled.
        while not operation.done():
            time.sleep(300)  # 5 mins
    
        try:
            database_admin_api.get_backup(
                backup_pb.GetBackupRequest(
                    name=database_admin_api.backup_path(
                        spanner_client.project, instance_id, backup_id
                    ),
                )
            )
        except NotFound:
            print("Backup creation was successfully cancelled.")
            return
        print("Backup was created before the cancel completed.")
        database_admin_api.delete_backup(
            backup_pb.DeleteBackupRequest(
                name=database_admin_api.backup_path(
                    spanner_client.project, instance_id, backup_id
                ),
            )
        )
        print("Backup deleted.")
    
    

**Note:** The old client library interface code samples for Python are archived in [GitHub](https://github.com/googleapis/python-spanner/tree/main/samples/samples/archived). 

### Ruby
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "Your Spanner instance ID"
    # database_id = "Your Spanner database ID"
    # backup_id = "Your Spanner backup ID"
    
    require "google/cloud/spanner"
    require "google/cloud/spanner/admin/database"
    
    database_admin_client = Google::Cloud::Spanner::Admin::Database.database_admin
    
    instance_path = database_admin_client.instance_path project: project_id, instance: instance_id
    
    db_path = database_admin_client.database_path project: project_id,
                                                  instance: instance_id,
                                                  database: database_id
    
    backup_path = database_admin_client.backup_path project: project_id,
                                                    instance: instance_id,
                                                    backup: backup_id
    
    expire_time = Time.now + (14 * 24 * 3600) # 14 days from now
    
    job = database_admin_client.create_backup parent: instance_path,
                                              backup_id: backup_id,
                                              backup: {
                                                database: db_path,
                                                  expire_time: expire_time
                                              }
    
    puts "Backup operation in progress"
    
    job.cancel
    job.wait_until_done!
    
    begin
      backup = database_admin_client.get_backup name: backup_path
      database_admin_client.delete_backup name: backup_path if backup
    rescue StandardError
      nil # no cleanup needed when a backup is not created
    end
    puts "#{backup_id} creation job cancelled"

## Get backup information

### Console

  1. In the Google Cloud console, go to the Spanner **Instances** page.

[Go to Instances](https://console.cloud.google.com/spanner/instances)

  2. Click the instance that contains the database you want to view the backup information for.

  3. Click the database to open its **Overview** page.

  4. In the navigation pane, click **Backup/Restore**. You can view backup information for your selected backup in the database.




###  gcloud 

To get information about a backup, use [`gcloud spanner backups describe`](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/backups/describe).

Before using any of the command data below, make the following replacements: 

  * PROJECT_ID: the project ID.
  * INSTANCE_ID: the Spanner instance ID.
  * DATABASE_ID: the Spanner database ID.
  * BACKUP_NAME: the Spanner backup name.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backups describe BACKUP_NAME --instance=INSTANCE_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backups describe BACKUP_NAME --instance=INSTANCE_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backups describe BACKUP_NAME --instance=INSTANCE_ID

You should receive a response similar to the following:
    
    
    createTime: '2020-02-04T02:05:43.920377Z'
    database: projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID
    expireTime: '2021-02-04T02:05:43.268327Z'
    name: projects/PROJECT_ID/instances/INSTANCE_ID/backups/BACKUP_NAME
    sizeBytes: '1000000000'
    state: READY
    

### Client libraries

Client libraries don't support getting backup information for a single backup. However, you can list all backups and their information in an instance. For more information, see List backups in an instance.

## List backups in an instance

### Console

  1. In the Google Cloud console, go to the Spanner **Instances** page.

[Go to Instances](https://console.cloud.google.com/spanner/instances)

  2. Click your instance to view all available backups and their information.

  3. In the navigation pane, click **Backup/Restore**.




###  gcloud 

To list all the backups in an instance, use [`gcloud spanner backups list`](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/backups/list).

Before using any of the command data below, make the following replacements: 

  * INSTANCE_ID: the Spanner instance ID.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backups list --instance=INSTANCE_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backups list --instance=INSTANCE_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backups list --instance=INSTANCE_ID

You should receive a response similar to the following:
    
    
      BACKUP               SOURCE_DATABASE  CREATION_TIME                EXPIRATION_TIME              STATE  BACKUP_SIZE_IN_BYTES  IN_USE_BY
      example-db-backup-6  example-db       2020-02-04T02:05:43.920377Z  2021-02-04T02:05:43.268327Z  CREATING
      example-db-backup-4  example-db       2020-02-04T01:21:20.873839Z  2021-02-04T01:21:20.530151Z  READY  32
      example-db-backup-3  example-db       2020-02-03T23:59:18.936433Z  2021-02-03T23:59:18.203083Z  READY  32
      example-db-backup-5  example-db       2020-02-03T23:48:06.259296Z  2021-02-03T23:48:05.830937Z  READY  32
      example-db-backup-2  example-db       2020-01-30T19:49:00.616338Z  2021-01-30T19:49:00.283917Z  READY  32
      example-db-backup-1  example-db       2020-01-30T19:47:09.492551Z  2021-01-30T19:47:09.097804Z  READY  32
    

To limit the list, specify the `--filter` flag. For example, to filter the list to only include the backups that are still being created, add `--filter="state:creating"`. For information about filter syntax, see [`gcloud topic filters`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters). For information on filtering backups, see the `filter` field in [`ListBackupsRequest`](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListBackupsRequest).

### Client libraries

The following code sample lists the backups in a given instance.

You can filter the list of returned backups (for example, filtering by name, version time, or backup expiration time) by providing a filter expression. For information on filtering syntax, see the `filter` parameter in [List Backups](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups/list#query-parameters).

### C++
    
    
    void ListBackups(google::cloud::spanner_admin::DatabaseAdminClient client,
                     std::string const& project_id,
                     std::string const& instance_id) {
      google::cloud::spanner::Instance in(project_id, instance_id);
      std::cout << "All backups:\n";
      for (auto& backup : client.ListBackups(in.FullName())) {
        if (!backup) throw std::move(backup).status();
        std::cout << "Backup " << backup->name() << " on database "
                  << backup->database() << " with size : " << backup->size_bytes()
                  << " bytes.\n";
      }
    }

### C#
    
    
    using [Google.Cloud.Spanner.Admin.Database.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.html);
    using [Google.Cloud.Spanner.Common.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.html);
    using System;
    using System.Collections.Generic;
    using System.Linq;
    
    public class ListBackupsSample
    {
        public IEnumerable<Backup> ListBackups(string projectId, string instanceId, string databaseId, string backupId)
        {
            // Create the DatabaseAdminClient instance.
            [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html) databaseAdminClient = [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_Create)();
    
            [InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html) parentAsInstanceName = [InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html).[FromProjectInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html#Google_Cloud_Spanner_Common_V1_InstanceName_FromProjectInstance_System_String_System_String_)(projectId, instanceId);
    
            // List all backups.
            Console.WriteLine("All backups:");
            var allBackups = databaseAdminClient.[ListBackups](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_ListBackups_Google_Cloud_Spanner_Admin_Database_V1_ListBackupsRequest_Google_Api_Gax_Grpc_CallSettings_)(parentAsInstanceName);
            PrintBackups(allBackups);
    
            [ListBackupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.ListBackupsRequest.html) request = new [ListBackupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.ListBackupsRequest.html)
            {
                ParentAsInstanceName = parentAsInstanceName,
            };
    
            // List backups containing backup name.
            Console.WriteLine($"Backups with backup name containing {backupId}:");
            request.[Filter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.ListBackupsRequest.html#Google_Cloud_Spanner_Admin_Database_V1_ListBackupsRequest_Filter) = $"name:{backupId}";
            var backupsWithName = databaseAdminClient.[ListBackups](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_ListBackups_Google_Cloud_Spanner_Admin_Database_V1_ListBackupsRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
            PrintBackups(backupsWithName);
    
            // List backups on a database containing name.
            Console.WriteLine($"Backups with database name containing {databaseId}:");
            request.[Filter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.ListBackupsRequest.html#Google_Cloud_Spanner_Admin_Database_V1_ListBackupsRequest_Filter) = $"database:{databaseId}";
            var backupsWithDatabaseName = databaseAdminClient.[ListBackups](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_ListBackups_Google_Cloud_Spanner_Admin_Database_V1_ListBackupsRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
            PrintBackups(backupsWithDatabaseName);
    
            // List backups that expire within 30 days.
            Console.WriteLine("Backups expiring within 30 days:");
            string expireTime = DateTime.UtcNow.AddDays(30).ToString("O");
            request.[Filter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.ListBackupsRequest.html#Google_Cloud_Spanner_Admin_Database_V1_ListBackupsRequest_Filter) = $"expire_time < \"{expireTime}\"";
            var expiringBackups = databaseAdminClient.[ListBackups](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_ListBackups_Google_Cloud_Spanner_Admin_Database_V1_ListBackupsRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
            PrintBackups(expiringBackups);
    
            // List backups with a size greater than 100 bytes.
            Console.WriteLine("Backups with size > 100 bytes:");
            request.[Filter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.ListBackupsRequest.html#Google_Cloud_Spanner_Admin_Database_V1_ListBackupsRequest_Filter) = "size_bytes > 100";
            var backupsWithSize = databaseAdminClient.[ListBackups](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_ListBackups_Google_Cloud_Spanner_Admin_Database_V1_ListBackupsRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
            PrintBackups(backupsWithSize);
    
            // List backups created in the last day that are ready.
            Console.WriteLine("Backups created within last day that are ready:");
            string createTime = DateTime.UtcNow.AddDays(-1).ToString("O");
            request.[Filter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.ListBackupsRequest.html#Google_Cloud_Spanner_Admin_Database_V1_ListBackupsRequest_Filter) = $"create_time >= \"{createTime}\" AND state:READY";
            var recentReadyBackups = databaseAdminClient.[ListBackups](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_ListBackups_Google_Cloud_Spanner_Admin_Database_V1_ListBackupsRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
            PrintBackups(recentReadyBackups);
    
            // List backups in pages of 500 elements each
            foreach (var page in databaseAdminClient.[ListBackups](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_ListBackups_Google_Cloud_Spanner_Admin_Database_V1_ListBackupsRequest_Google_Api_Gax_Grpc_CallSettings_)(parentAsInstanceName, pageSize: 500).AsRawResponses())
            {
                PrintBackups(page);
            }
    
            return allBackups;
        }
    
        private static void PrintBackups(IEnumerable<Backup> backups)
        {
            // We print the first 5 elements each time for demonstration purposes.
            // You can print all backups in the sequence by removing the call to Take(5).
            // If the sequence has been returned by a paginated operation it will lazily
            // fetch elements in pages as needed.
            foreach ([Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html) backup in backups.Take(5))
            {
                Console.WriteLine($"Backup Name : {backup.Name}");
            };
        }
    }

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"regexp"
    	"time"
    
    	database "cloud.google.com/go/spanner/admin/database/apiv1"
    	adminpb "cloud.google.com/go/spanner/admin/database/apiv1/databasepb"
    	"google.golang.org/api/iterator"
    )
    
    func listBackups(ctx context.Context, w io.Writer, db, backupID string) error {
    	adminClient, err := database.NewDatabaseAdminClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer adminClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/database/apiv1.html#cloud_google_com_go_spanner_admin_database_apiv1_DatabaseAdminClient_Close)()
    
    	matches := regexp.MustCompile("^(.*)/databases/(.*)$").FindStringSubmatch(db)
    	if matches == nil || len(matches) != 3 {
    		return fmt.Errorf("Invalid database id %s", db)
    	}
    	instanceName := matches[1]
    
    	printBackups := func(iter *database.[BackupIterator](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/database/apiv1.html#cloud_google_com_go_spanner_admin_database_apiv1_BackupIterator)) error {
    		for {
    			resp, err := iter.Next()
    			if err == iterator.Done {
    				return nil
    			}
    			if err != nil {
    				return err
    			}
    			fmt.Fprintf(w, "Backup %s\n", resp.Name)
    		}
    	}
    
    	var iter *database.[BackupIterator](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/database/apiv1.html#cloud_google_com_go_spanner_admin_database_apiv1_BackupIterator)
    	var filter string
    	// List all backups.
    	iter = adminClient.ListBackups(ctx, &adminpb.ListBackupsRequest{
    		Parent: instanceName,
    	})
    	if err := printBackups(iter); err != nil {
    		return err
    	}
    
    	// List all backups that contain a name.
    	iter = adminClient.ListBackups(ctx, &adminpb.ListBackupsRequest{
    		Parent: instanceName,
    		Filter: "name:" + backupID,
    	})
    	if err := printBackups(iter); err != nil {
    		return err
    	}
    
    	// List all backups that expire before a timestamp.
    	expireTime := time.Now().AddDate(0, 0, 30)
    	filter = fmt.Sprintf(`expire_time < "%s"`, expireTime.Format(time.RFC3339))
    	iter = adminClient.ListBackups(ctx, &adminpb.ListBackupsRequest{
    		Parent: instanceName,
    		Filter: filter,
    	})
    	if err := printBackups(iter); err != nil {
    		return err
    	}
    
    	// List all backups for a database that contains a name.
    	iter = adminClient.ListBackups(ctx, &adminpb.ListBackupsRequest{
    		Parent: instanceName,
    		Filter: "database:" + db,
    	})
    	if err := printBackups(iter); err != nil {
    		return err
    	}
    
    	// List all backups with a size greater than some bytes.
    	iter = adminClient.ListBackups(ctx, &adminpb.ListBackupsRequest{
    		Parent: instanceName,
    		Filter: "size_bytes > 100",
    	})
    	if err := printBackups(iter); err != nil {
    		return err
    	}
    
    	// List backups that were created after a timestamp that are also ready.
    	createTime := time.Now().AddDate(0, 0, -1)
    	filter = fmt.Sprintf(
    		`create_time >= "%s" AND state:READY`,
    		createTime.Format(time.RFC3339),
    	)
    	iter = adminClient.ListBackups(ctx, &adminpb.ListBackupsRequest{
    		Parent: instanceName,
    		Filter: filter,
    	})
    	if err := printBackups(iter); err != nil {
    		return err
    	}
    
    	// List backups with pagination.
    	request := &adminpb.ListBackupsRequest{
    		Parent:   instanceName,
    		PageSize: 10,
    	}
    	for {
    		iter = adminClient.ListBackups(ctx, request)
    		if err := printBackups(iter); err != nil {
    			return err
    		}
    		pageToken := iter.PageInfo().Token
    		if pageToken == "" {
    			break
    		} else {
    			request.PageToken = pageToken
    		}
    	}
    
    	fmt.Fprintf(w, "Backups listed.\n")
    	return nil
    }
    

### Java
    
    
    static void listBackups(
        DatabaseAdminClient dbAdminClient, String projectId,
        String instanceId, String databaseId, String backupId) {
      InstanceName instanceName = InstanceName.of(projectId, instanceId);
      // List all backups.
      System.out.println("All backups:");
      for (Backup backup : dbAdminClient.listBackups(
          instanceName.toString()).iterateAll()) {
        System.out.println(backup);
      }
    
      // List all backups with a specific name.
      System.out.println(
          String.format("All backups with backup name containing \"%s\":", backupId));
      ListBackupsRequest listBackupsRequest =
          ListBackupsRequest.newBuilder().setParent(instanceName.toString())
              .setFilter(String.format("name:%s", backupId)).build();
      for (Backup backup : dbAdminClient.listBackups(listBackupsRequest).iterateAll()) {
        System.out.println(backup);
      }
    
      // List all backups for databases whose name contains a certain text.
      System.out.println(
          String.format(
              "All backups for databases with a name containing \"%s\":", databaseId));
      listBackupsRequest =
          ListBackupsRequest.newBuilder().setParent(instanceName.toString())
              .setFilter(String.format("database:%s", databaseId)).build();
      for (Backup backup : dbAdminClient.listBackups(listBackupsRequest).iterateAll()) {
        System.out.println(backup);
      }
    
      // List all backups that expire before a certain time.
      com.google.cloud.Timestamp expireTime = com.google.cloud.Timestamp.ofTimeMicroseconds(
          TimeUnit.MICROSECONDS.convert(
              System.currentTimeMillis() + TimeUnit.DAYS.toMillis(30), TimeUnit.MILLISECONDS));
    
      System.out.println(String.format("All backups that expire before %s:", expireTime));
      listBackupsRequest =
          ListBackupsRequest.newBuilder().setParent(instanceName.toString())
              .setFilter(String.format("expire_time < \"%s\"", expireTime)).build();
    
      for (Backup backup : dbAdminClient.listBackups(listBackupsRequest).iterateAll()) {
        System.out.println(backup);
      }
    
      // List all backups with size greater than a certain number of bytes.
      listBackupsRequest =
          ListBackupsRequest.newBuilder().setParent(instanceName.toString())
              .setFilter("size_bytes > 100").build();
    
      System.out.println("All backups with size greater than 100 bytes:");
      for (Backup backup : dbAdminClient.listBackups(listBackupsRequest).iterateAll()) {
        System.out.println(backup);
      }
    
      // List all backups with a create time after a certain timestamp and that are also ready.
      com.google.cloud.Timestamp createTime = com.google.cloud.Timestamp.ofTimeMicroseconds(
          TimeUnit.MICROSECONDS.convert(
              System.currentTimeMillis() - TimeUnit.DAYS.toMillis(1), TimeUnit.MILLISECONDS));
    
      System.out.println(
          String.format(
              "All databases created after %s and that are ready:", createTime.toString()));
      listBackupsRequest =
          ListBackupsRequest.newBuilder().setParent(instanceName.toString())
              .setFilter(String.format(
                  "create_time >= \"%s\" AND state:READY", createTime.toString())).build();
      for (Backup backup : dbAdminClient.listBackups(listBackupsRequest).iterateAll()) {
        System.out.println(backup);
      }
    
      // List backups using pagination.
      System.out.println("All backups, listed using pagination:");
      listBackupsRequest =
          ListBackupsRequest.newBuilder().setParent(instanceName.toString()).setPageSize(10).build();
      while (true) {
        ListBackupsPagedResponse response = dbAdminClient.listBackups(listBackupsRequest);
        for (Backup backup : response.getPage().iterateAll()) {
          System.out.println(backup);
        }
        String nextPageToken = response.getNextPageToken();
        if (!Strings.isNullOrEmpty(nextPageToken)) {
          listBackupsRequest = listBackupsRequest.toBuilder().setPageToken(nextPageToken).build();
        } else {
          break;
        }
      }
    }

**Note:** The old client library interface code samples for Java are archived in [GitHub](https://github.com/googleapis/google-cloud-java/tree/main/java-spanner/samples/snippets/src/main/java/com/example/spanner/admin/archived). 

### Node.js
    
    
    // Imports the Google Cloud client library
    const {Spanner} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const projectId = 'my-project-id';
    // const instanceId = 'my-instance';
    // const databaseId = 'my-database';
    // const backupId = 'my-backup';
    
    // Creates a client
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({
      projectId: projectId,
    });
    
    // Gets a reference to a Cloud Spanner Database Admin Client object
    const databaseAdminClient = spanner.[getDatabaseAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)();
    
    try {
      // Get the parent(instance) of the database
      const parent = databaseAdminClient.instancePath(projectId, instanceId);
    
      // List all backups
      const [allBackups] = await databaseAdminClient.listBackups({
        parent: parent,
      });
    
      console.log('All backups:');
      allBackups.forEach(backups => {
        if (backups.name) {
          const backup = backups.name;
          const delimiter =
            'projects/' + projectId + '/instances/' + instanceId + '/backups/';
          const result = backup.substring(delimiter.length);
          console.log(result);
        }
      });
    
      // List backups filtered by backup name
      const [backupsByName] = await databaseAdminClient.listBackups({
        parent: parent,
        filter: `Name:${backupId}`,
      });
      console.log('Backups matching backup name:');
      backupsByName.forEach(backup => {
        if (backup.name) {
          const backupName = backup.name;
          const delimiter =
            'projects/' + projectId + '/instances/' + instanceId + '/backups/';
          const result = backupName.substring(delimiter.length);
          console.log(result);
        }
      });
    
      // List backups expiring within 30 days
      const expireTime = new Date();
      expireTime.setDate(expireTime.getDate() + 30);
      const [backupsByExpiry] = await databaseAdminClient.listBackups({
        parent: parent,
        filter: `expire_time < "${expireTime.toISOString()}"`,
      });
      console.log('Backups expiring within 30 days:');
      backupsByExpiry.forEach(backup => {
        if (backup.name) {
          const backupName = backup.name;
          const delimiter =
            'projects/' + projectId + '/instances/' + instanceId + '/backups/';
          const result = backupName.substring(delimiter.length);
          console.log(result);
        }
      });
    
      // List backups filtered by database name
      const [backupsByDbName] = await databaseAdminClient.listBackups({
        parent: parent,
        filter: `Database:${databaseId}`,
      });
      console.log('Backups matching database name:');
      backupsByDbName.forEach(backup => {
        if (backup.name) {
          const backupName = backup.name;
          const delimiter =
            'projects/' + projectId + '/instances/' + instanceId + '/backups/';
          const result = backupName.substring(delimiter.length);
          console.log(result);
        }
      });
    
      // List backups filtered by backup size
      const [backupsBySize] = await databaseAdminClient.listBackups({
        parent: parent,
        filter: 'size_bytes > 100',
      });
      console.log('Backups filtered by size:');
      backupsBySize.forEach(backup => {
        if (backup.name) {
          const backupName = backup.name;
          const delimiter =
            'projects/' + projectId + '/instances/' + instanceId + '/backups/';
          const result = backupName.substring(delimiter.length);
          console.log(result);
        }
      });
    
      // List backups that are ready that were created after a certain time
      const createTime = new Date();
      createTime.setDate(createTime.getDate() - 1);
      const [backupsByCreateTime] = await databaseAdminClient.listBackups({
        parent: parent,
        filter: `(state:READY) AND (create_time >= "${createTime.toISOString()}")`,
      });
      console.log('Ready backups filtered by create time:');
      backupsByCreateTime.forEach(backup => {
        if (backup.name) {
          const backupName = backup.name;
          const delimiter =
            'projects/' + projectId + '/instances/' + instanceId + '/backups/';
          const result = backupName.substring(delimiter.length);
          console.log(result);
        }
      });
    
      // List backups using pagination
      console.log('Get backups paginated:');
      const [backups] = await databaseAdminClient.listBackups({
        parent: parent,
        pageSize: 3,
      });
      backups.forEach(backup => {
        if (backup.name) {
          const backupName = backup.name;
          const delimiter =
            'projects/' + projectId + '/instances/' + instanceId + '/backups/';
          const result = backupName.substring(delimiter.length);
          console.log(result);
        }
      });
    } catch (err) {
      console.error('ERROR:', err);
    }

**Note:** The old client library interface code samples for Node.js are archived in [GitHub](https://github.com/googleapis/nodejs-spanner/tree/main/samples/archived). 

### PHP
    
    
    use Google\Cloud\Spanner\Admin\Database\V1\Client\DatabaseAdminClient;
    use Google\Cloud\Spanner\Admin\Database\V1\ListBackupsRequest;
    
    /**
     * List backups in an instance.
     * Example:
     * ```
     * list_backups($projectId, $instanceId);
     * ```
     *
     * @param string $projectId The Google Cloud project ID.
     * @param string $instanceId The Spanner instance ID.
     */
    function list_backups(string $projectId, string $instanceId): void
    {
        $databaseAdminClient = new DatabaseAdminClient();
        $parent = DatabaseAdminClient::instanceName($projectId, $instanceId);
    
        // List all backups.
        print('All backups:' . PHP_EOL);
        $request = new ListBackupsRequest([
            'parent' => $parent
        ]);
        $backups = $databaseAdminClient->listBackups($request)->iterateAllElements();
        foreach ($backups as $backup) {
            print('  ' . basename($backup->getName()) . PHP_EOL);
        }
    
        // List all backups that contain a name.
        $backupName = 'backup-test-';
        print("All backups with name containing \"$backupName\":" . PHP_EOL);
        $filter = "name:$backupName";
        $request = new ListBackupsRequest([
            'parent' => $parent,
            'filter' => $filter
        ]);
        $backups = $databaseAdminClient->listBackups($request)->iterateAllElements();
        foreach ($backups as $backup) {
            print('  ' . basename($backup->getName()) . PHP_EOL);
        }
    
        // List all backups for a database that contains a name.
        $databaseId = 'test-';
        print("All backups for a database which name contains \"$databaseId\":" . PHP_EOL);
        $filter = "database:$databaseId";
        $request = new ListBackupsRequest([
            'parent' => $parent,
            'filter' => $filter
        ]);
        $backups = $databaseAdminClient->listBackups($request)->iterateAllElements();
        foreach ($backups as $backup) {
            print('  ' . basename($backup->getName()) . PHP_EOL);
        }
    
        // List all backups that expire before a timestamp.
        $expireTime = (new \DateTime('+30 days'))->format('c');
        print("All backups that expire before $expireTime:" . PHP_EOL);
        $filter = "expire_time < \"$expireTime\"";
        $request = new ListBackupsRequest([
            'parent' => $parent,
            'filter' => $filter
        ]);
        $backups = $databaseAdminClient->listBackups($request)->iterateAllElements();
        foreach ($backups as $backup) {
            print('  ' . basename($backup->getName()) . PHP_EOL);
        }
    
        // List all backups with a size greater than some bytes.
        $size = 500;
        print("All backups with size greater than $size bytes:" . PHP_EOL);
        $filter = "size_bytes > $size";
        $request = new ListBackupsRequest([
            'parent' => $parent,
            'filter' => $filter
        ]);
        $backups = $databaseAdminClient->listBackups($request)->iterateAllElements();
        foreach ($backups as $backup) {
            print('  ' . basename($backup->getName()) . PHP_EOL);
        }
    
        // List backups that were created after a timestamp that are also ready.
        $createTime = (new \DateTime('-1 day'))->format('c');
        print("All backups created after $createTime:" . PHP_EOL);
        $filter = "create_time >= \"$createTime\" AND state:READY";
        $request = new ListBackupsRequest([
            'parent' => $parent,
            'filter' => $filter
        ]);
        $backups = $databaseAdminClient->listBackups($request)->iterateAllElements();
        foreach ($backups as $backup) {
            print('  ' . basename($backup->getName()) . PHP_EOL);
        }
    
        // List backups with pagination.
        print('All backups with pagination:' . PHP_EOL);
        $request = new ListBackupsRequest([
            'parent' => $parent,
            'page_size' => 2
        ]);
        $pages = $databaseAdminClient->listBackups($request)->iteratePages();
        foreach ($pages as $pageNumber => $page) {
            print("All backups, page $pageNumber:" . PHP_EOL);
            foreach ($page as $backup) {
                print('  ' . basename($backup->getName()) . PHP_EOL);
            }
        }
    }

**Note:** The old client library interface code samples for PHP are archived in [GitHub](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/main/spanner/src/admin/archived). 

### Python
    
    
    def list_backups(instance_id, database_id, backup_id):
        from google.cloud.spanner_admin_database_v1.types import backup as backup_pb
    
        spanner_client = spanner.Client()
        database_admin_api = spanner_client.database_admin_api
    
        # List all backups.
        print("All backups:")
        request = backup_pb.ListBackupsRequest(
            parent=database_admin_api.instance_path(spanner_client.project, instance_id),
            filter="",
        )
        operations = database_admin_api.list_backups(request)
        for backup in operations:
            print(backup.name)
    
        # List all backups that contain a name.
        print('All backups with backup name containing "{}":'.format(backup_id))
        request = backup_pb.ListBackupsRequest(
            parent=database_admin_api.instance_path(spanner_client.project, instance_id),
            filter="name:{}".format(backup_id),
        )
        operations = database_admin_api.list_backups(request)
        for backup in operations:
            print(backup.name)
    
        # List all backups for a database that contains a name.
        print('All backups with database name containing "{}":'.format(database_id))
        request = backup_pb.ListBackupsRequest(
            parent=database_admin_api.instance_path(spanner_client.project, instance_id),
            filter="database:{}".format(database_id),
        )
        operations = database_admin_api.list_backups(request)
        for backup in operations:
            print(backup.name)
    
        # List all backups that expire before a timestamp.
        expire_time = datetime.utcnow().replace(microsecond=0) + timedelta(days=30)
        print(
            'All backups with expire_time before "{}-{}-{}T{}:{}:{}Z":'.format(
                *expire_time.timetuple()
            )
        )
        request = backup_pb.ListBackupsRequest(
            parent=database_admin_api.instance_path(spanner_client.project, instance_id),
            filter='expire_time < "{}-{}-{}T{}:{}:{}Z"'.format(*expire_time.timetuple()),
        )
        operations = database_admin_api.list_backups(request)
        for backup in operations:
            print(backup.name)
    
        # List all backups with a size greater than some bytes.
        print("All backups with backup size more than 100 bytes:")
        request = backup_pb.ListBackupsRequest(
            parent=database_admin_api.instance_path(spanner_client.project, instance_id),
            filter="size_bytes > 100",
        )
        operations = database_admin_api.list_backups(request)
        for backup in operations:
            print(backup.name)
    
        # List backups that were created after a timestamp that are also ready.
        create_time = datetime.utcnow().replace(microsecond=0) - timedelta(days=1)
        print(
            'All backups created after "{}-{}-{}T{}:{}:{}Z" and are READY:'.format(
                *create_time.timetuple()
            )
        )
        request = backup_pb.ListBackupsRequest(
            parent=database_admin_api.instance_path(spanner_client.project, instance_id),
            filter='create_time >= "{}-{}-{}T{}:{}:{}Z" AND state:READY'.format(
                *create_time.timetuple()
            ),
        )
        operations = database_admin_api.list_backups(request)
        for backup in operations:
            print(backup.name)
    
        print("All backups with pagination")
        # If there are multiple pages, additional ``ListBackup``
        # requests will be made as needed while iterating.
        paged_backups = set()
        request = backup_pb.ListBackupsRequest(
            parent=database_admin_api.instance_path(spanner_client.project, instance_id),
            page_size=2,
        )
        operations = database_admin_api.list_backups(request)
        for backup in operations:
            paged_backups.add(backup.name)
        for backup in paged_backups:
            print(backup)
    
    

**Note:** The old client library interface code samples for Python are archived in [GitHub](https://github.com/googleapis/python-spanner/tree/main/samples/samples/archived). 

### Ruby
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "Your Spanner instance ID"
    # backup_id = "Your Spanner database backup ID"
    # database_id = "Your Spanner databaseID"
    
    require "google/cloud/spanner"
    require "google/cloud/spanner/admin/database"
    
    database_admin_client = Google::Cloud::Spanner::Admin::Database.database_admin
    instance_path = database_admin_client.instance_path project: project_id, instance: instance_id
    
    puts "All backups"
    database_admin_client.list_backups(parent: instance_path).each do |backup|
      puts backup.name
    end
    
    puts "All backups with backup name containing \"#{backup_id}\":"
    database_admin_client.list_backups(parent: instance_path, filter: "name:#{backup_id}").each do |backup|
      puts backup.name
    end
    
    puts "All backups for databases with a name containing \"#{database_id}\":"
    database_admin_client.list_backups(parent: instance_path, filter: "database:#{database_id}").each do |backup|
      puts backup.name
    end
    
    puts "All backups that expire before a timestamp:"
    expire_time = Time.now + (30 * 24 * 3600) # 30 days from now
    database_admin_client.list_backups(parent: instance_path, filter: "expire_time < \"#{expire_time.iso8601}\"").each do |backup|
      puts backup.name
    end
    
    puts "All backups with a size greater than 500 bytes:"
    database_admin_client.list_backups(parent: instance_path, filter: "size_bytes >= 500").each do |backup|
      puts backup.name
    end
    
    puts "All backups that were created after a timestamp that are also ready:"
    create_time = Time.now - (24 * 3600) # From 1 day ago
    database_admin_client.list_backups(parent: instance_path, filter: "create_time >= \"#{create_time.iso8601}\" AND state:READY").each do |backup|
      puts backup.name
    end
    
    puts "All backups with pagination:"
    list = database_admin_client.list_backups parent: instance_path, page_size: 5
    list.each do |backup|
      puts backup.name
    end

## Update the backup expiration period

### Console

  1. Go to the Spanner Instances page in the Google Cloud console.

[Go to the Spanner Instances page](https://console.cloud.google.com/spanner/instances)

  2. Click the instance containing the database to open its **Overview** page.

  3. Click the database to open its **Overview** page.

  4. In the navigation pane, click **Backup/Restore**.

  5. Click the **Actions** button for your selected backup, then select **Update metadata**.

  6. Select the new expiration date.

  7. Click **Update**.




###  gcloud 

To update a backup's expiration period date, use [`gcloud spanner backups update-metadata`](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/backups/update-metadata):

Before using any of the command data below, make the following replacements: 

  * PROJECT_ID: the project ID.
  * BACKUP_ID: the Spanner backup ID.
  * INSTANCE_ID: the Spanner instance ID.
  * EXPIRATION_DATE: the expiration date time stamp.
  * DATABASE_ID: the Spanner database ID.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backups update-metadata BACKUP_ID \
    --instance=INSTANCE_ID \
    --expiration-date=EXPIRATION_DATE

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backups update-metadata BACKUP_ID `
    --instance=INSTANCE_ID `
    --expiration-date=EXPIRATION_DATE

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backups update-metadata BACKUP_ID ^
    --instance=INSTANCE_ID ^
    --expiration-date=EXPIRATION_DATE

You should receive a response similar to the following:
    
    
    createTime: '2020-02-04T02:05:43.920377Z'
    database: projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID
    expireTime: '2020-05-05T00:00:00Z'
    name: projects/PROJECT_ID/instances/INSTANCE_ID/backups/BACKUP_ID
    sizeBytes: '1000000000'
    state: READY
    

### Client libraries

The following code sample retrieves the expiry time of a backup and extends it.

### C++
    
    
    void UpdateBackup(google::cloud::spanner_admin::DatabaseAdminClient client,
                      std::string const& project_id, std::string const& instance_id,
                      std::string const& backup_id,
                      absl::Duration expiry_extension) {
      google::cloud::spanner::Backup backup_name(
          google::cloud::spanner::Instance(project_id, instance_id), backup_id);
      auto backup = client.GetBackup(backup_name.FullName());
      if (!backup) throw std::move(backup).status();
      auto expire_time =
          google::cloud::spanner::MakeTimestamp(backup->expire_time())
              .value()
              .get<absl::Time>()
              .value();
      expire_time += expiry_extension;
      auto max_expire_time =
          google::cloud::spanner::MakeTimestamp(backup->max_expire_time())
              .value()
              .get<absl::Time>()
              .value();
      if (expire_time > max_expire_time) expire_time = max_expire_time;
      google::spanner::admin::database::v1::UpdateBackupRequest request;
      request.mutable_backup()->set_name(backup_name.FullName());
      *request.mutable_backup()->mutable_expire_time() =
          google::cloud::spanner::MakeTimestamp(expire_time)
              .value()
              .get<google::protobuf::Timestamp>()
              .value();
      request.mutable_update_mask()->add_paths("expire_time");
      backup = client.UpdateBackup(request);
      if (!backup) throw std::move(backup).status();
      std::cout
          << "Backup " << backup->name() << " updated to expire at "
          << google::cloud::spanner::MakeTimestamp(backup->expire_time()).value()
          << ".\n";
    }

### C#
    
    
    using [Google.Cloud.Spanner.Admin.Database.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    
    public class UpdateBackupSample
    {
        public Backup UpdateBackup(string projectId, string instanceId, string backupId)
        {
            // Create the DatabaseAdminClient instance.
            [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html) databaseAdminClient = [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_Create)();
    
            // Retrieve existing backup.
            [BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupName.html) backupName = [BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupName.html).[FromProjectInstanceBackup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupName.html#Google_Cloud_Spanner_Admin_Database_V1_BackupName_FromProjectInstanceBackup_System_String_System_String_System_String_)(projectId, instanceId, backupId);
            [Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html) backup = databaseAdminClient.[GetBackup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_GetBackup_Google_Cloud_Spanner_Admin_Database_V1_BackupName_Google_Api_Gax_Grpc_CallSettings_)(backupName);
    
            // Add 1 hour to the existing ExpireTime.
            backup.[ExpireTime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html#Google_Cloud_Spanner_Admin_Database_V1_Backup_ExpireTime) = backup.[ExpireTime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html#Google_Cloud_Spanner_Admin_Database_V1_Backup_ExpireTime).[ToDateTime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html#Google_Protobuf_WellKnownTypes_Timestamp_ToDateTime)().AddHours(1).[ToTimestamp](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.TimeExtensions.html#Google_Protobuf_WellKnownTypes_TimeExtensions_ToTimestamp_System_DateTime_)();
    
            [UpdateBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.UpdateBackupRequest.html) backupUpdateRequest = new [UpdateBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.UpdateBackupRequest.html)
            {
                UpdateMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)
                {
                    Paths = { "expire_time" }
                },
                Backup = backup
            };
    
            // Make the UpdateBackup requests.
            var updatedBackup = databaseAdminClient.[UpdateBackup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_UpdateBackup_Google_Cloud_Spanner_Admin_Database_V1_Backup_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)(backupUpdateRequest);
    
            Console.WriteLine($"Updated Backup ExpireTime: {updatedBackup.ExpireTime}");
    
            return updatedBackup;
        }
    }

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"regexp"
    	"time"
    
    	database "cloud.google.com/go/spanner/admin/database/apiv1"
    	adminpb "cloud.google.com/go/spanner/admin/database/apiv1/databasepb"
    	"google.golang.org/genproto/protobuf/field_mask"
    	"google.golang.org/protobuf/types/known/timestamppb"
    )
    
    // updateBackup updates the expiration time of a pending or completed backup.
    func updateBackup(w io.Writer, db string, backupID string) error {
    	// db := "projects/my-project/instances/my-instance/databases/my-database"
    	// backupID := "my-backup"
    
    	// Add timeout to context.
    	ctx, cancel := context.WithTimeout(context.Background(), time.Hour)
    	defer cancel()
    
    	adminClient, err := database.NewDatabaseAdminClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer adminClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/database/apiv1.html#cloud_google_com_go_spanner_admin_database_apiv1_DatabaseAdminClient_Close)()
    
    	matches := regexp.MustCompile("^(.*)/databases/(.*)$").FindStringSubmatch(db)
    	if matches == nil || len(matches) != 3 {
    		return fmt.Errorf("invalid database id %s", db)
    	}
    	backupName := matches[1] + "/backups/" + backupID
    
    	// Get the backup instance.
    	backup, err := adminClient.GetBackup(ctx, &adminpb.GetBackupRequest{Name: backupName})
    	if err != nil {
    		return err
    	}
    
    	// Expire time must be within 366 days of the create time of the backup.
    	maxExpireTime := time.Unix(backup.MaxExpireTime.Seconds, int64(backup.MaxExpireTime.Nanos))
    	expireTime := time.Unix(backup.ExpireTime.Seconds, int64(backup.ExpireTime.Nanos)).AddDate(0, 0, 30)
    
    	// Ensure that new expire time is less than the max expire time.
    	if expireTime.After(maxExpireTime) {
    		expireTime = maxExpireTime
    	}
    	expireTimepb := timestamppb.New(expireTime)
    
    	// Make the update backup request.
    	_, err = adminClient.UpdateBackup(ctx, &adminpb.UpdateBackupRequest{
    		Backup: &adminpb.Backup{
    			Name:       backupName,
    			ExpireTime: expireTimepb,
    		},
    		UpdateMask: &field_mask.FieldMask{Paths: []string{"expire_time"}},
    	})
    	if err != nil {
    		return err
    	}
    
    	fmt.Fprintf(w, "Updated backup %s with expire time %s\n", backupName, expireTime)
    
    	return nil
    }
    

### Java
    
    
    static void updateBackup(DatabaseAdminClient dbAdminClient, String projectId,
        String instanceId, String backupId) {
      BackupName backupName = BackupName.of(projectId, instanceId, backupId);
    
      // Get current backup metadata.
      Backup backup = dbAdminClient.getBackup(backupName);
      // Add 30 days to the expire time.
      // Expire time must be within 366 days of the create time of the backup.
      Timestamp currentExpireTime = backup.getExpireTime();
      com.google.cloud.Timestamp newExpireTime =
          com.google.cloud.Timestamp.ofTimeMicroseconds(
              TimeUnit.SECONDS.toMicros(currentExpireTime.getSeconds())
                  + TimeUnit.NANOSECONDS.toMicros(currentExpireTime.getNanos())
                  + TimeUnit.DAYS.toMicros(30L));
    
      // New Expire Time must be less than Max Expire Time
      newExpireTime =
          newExpireTime.compareTo(com.google.cloud.Timestamp.fromProto(backup.getMaxExpireTime()))
              < 0 ? newExpireTime : com.google.cloud.Timestamp.fromProto(backup.getMaxExpireTime());
    
      System.out.println(String.format(
          "Updating expire time of backup [%s] to %s...",
          backupId.toString(),
          java.time.OffsetDateTime.ofInstant(
              Instant.ofEpochSecond(newExpireTime.getSeconds(),
                  newExpireTime.getNanos()), ZoneId.systemDefault())));
    
      // Update expire time.
      backup = backup.toBuilder().setExpireTime(newExpireTime.toProto()).build();
      dbAdminClient.updateBackup(backup,
          FieldMask.newBuilder().addAllPaths(Lists.newArrayList("expire_time")).build());
      System.out.println("Updated backup [" + backupId + "]");
    }

**Note:** The old client library interface code samples for Java are archived in [GitHub](https://github.com/googleapis/google-cloud-java/tree/main/java-spanner/samples/snippets/src/main/java/com/example/spanner/admin/archived). 

### Node.js
    
    
    // Imports the Google Cloud client library and precise date library
    const {Spanner, protos} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    const {PreciseDate} = require('[@google-cloud/precise-date](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/overview.html)');
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const projectId = 'my-project-id';
    // const instanceId = 'my-instance';
    // const backupId = 'my-backup';
    
    // Creates a client
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({
      projectId: projectId,
    });
    
    // Gets a reference to a Cloud Spanner Database Admin Client object
    const databaseAdminClient = spanner.[getDatabaseAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)();
    
    // Read backup metadata and update expiry time
    try {
      const [metadata] = await databaseAdminClient.getBackup({
        name: databaseAdminClient.backupPath(projectId, instanceId, backupId),
      });
    
      const currentExpireTime = metadata.expireTime;
      const maxExpireTime = metadata.maxExpireTime;
      const wantExpireTime = new [PreciseDate](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/precise-date/precisedate.html)(currentExpireTime);
      wantExpireTime.setDate(wantExpireTime.getDate() + 1);
    
      // New expire time should be less than the max expire time
      const min = (currentExpireTime, maxExpireTime) =>
        currentExpireTime < maxExpireTime ? currentExpireTime : maxExpireTime;
      const newExpireTime = new [PreciseDate](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/precise-date/precisedate.html)(min(wantExpireTime, maxExpireTime));
      console.log(
        `Backup ${backupId} current expire time: ${[Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html).[timestamp](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)(
          currentExpireTime,
        ).[toISOString](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/precise-date/precisedate.html)()}`,
      );
      console.log(
        `Updating expire time to ${[Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html).[timestamp](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)(
          newExpireTime,
        ).[toISOString](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/precise-date/precisedate.html)()}`,
      );
    
      await databaseAdminClient.updateBackup({
        backup: {
          name: databaseAdminClient.backupPath(projectId, instanceId, backupId),
          expireTime: [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html).[timestamp](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)(newExpireTime).[toStruct](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/precise-date/precisedate.html)(),
        },
        updateMask: (protos.google.protobuf.[FieldMask](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.protobuf.fieldmask.html) = {
          paths: ['expire_time'],
        }),
      });
      console.log('Expire time updated.');
    } catch (err) {
      console.error('ERROR:', err);
    }

**Note:** The old client library interface code samples for Node.js are archived in [GitHub](https://github.com/googleapis/nodejs-spanner/tree/main/samples/archived). 

### PHP
    
    
    use Google\Cloud\Spanner\Admin\Database\V1\Backup;
    use Google\Cloud\Spanner\Admin\Database\V1\UpdateBackupRequest;
    use Google\Cloud\Spanner\Admin\Database\V1\Client\DatabaseAdminClient;
    use Google\Protobuf\Timestamp;
    
    /**
     * Update the backup expire time.
     * Example:
     * ```
     * update_backup($projectId, $instanceId, $backupId);
     * ```
     * @param string $projectId The Google Cloud project ID.
     * @param string $instanceId The Spanner instance ID.
     * @param string $backupId The Spanner backup ID.
     */
    function update_backup(string $projectId, string $instanceId, string $backupId): void
    {
        $databaseAdminClient = new DatabaseAdminClient();
        $backupName = DatabaseAdminClient::backupName($projectId, $instanceId, $backupId);
        $newExpireTime = new Timestamp();
        $newExpireTime->setSeconds((new \DateTime('+30 days'))->getTimestamp());
        $request = new UpdateBackupRequest([
            'backup' => new Backup([
                'name' => $backupName,
                'expire_time' => $newExpireTime
            ]),
            'update_mask' => new \Google\Protobuf\FieldMask(['paths' => ['expire_time']])
        ]);
    
        $info = $databaseAdminClient->updateBackup($request);
        printf('Backup %s new expire time: %d' . PHP_EOL, basename($info->getName()), $info->getExpireTime()->getSeconds());
    }

**Note:** The old client library interface code samples for PHP are archived in [GitHub](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/main/spanner/src/admin/archived). 

### Python
    
    
    def update_backup(instance_id, backup_id):
        from google.cloud.spanner_admin_database_v1.types import backup as backup_pb
    
        spanner_client = spanner.Client()
        database_admin_api = spanner_client.database_admin_api
    
        backup = database_admin_api.get_backup(
            backup_pb.GetBackupRequest(
                name=database_admin_api.backup_path(
                    spanner_client.project, instance_id, backup_id
                ),
            )
        )
    
        # Expire time must be within 366 days of the create time of the backup.
        old_expire_time = backup.expire_time
        # New expire time should be less than the max expire time
        new_expire_time = min(backup.max_expire_time, old_expire_time + timedelta(days=30))
        database_admin_api.update_backup(
            backup_pb.UpdateBackupRequest(
                backup=backup_pb.Backup(name=backup.name, expire_time=new_expire_time),
                update_mask={"paths": ["expire_time"]},
            )
        )
        print(
            "Backup {} expire time was updated from {} to {}.".format(
                backup.name, old_expire_time, new_expire_time
            )
        )
    
    

**Note:** The old client library interface code samples for Python are archived in [GitHub](https://github.com/googleapis/python-spanner/tree/main/samples/samples/archived). 

### Ruby
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "Your Spanner instance ID"
    # backup_id = "Your Spanner backup ID"
    
    require "google/cloud/spanner"
    require "google/cloud/spanner/admin/database"
    
    database_admin_client = Google::Cloud::Spanner::Admin::Database.database_admin
    instance_path = database_admin_client.instance_path project: project_id, instance: instance_id
    backup_path = database_admin_client.backup_path project: project_id,
                                                    instance: instance_id,
                                                    backup: backup_id
    backup = database_admin_client.get_backup name: backup_path
    backup.expire_time = Time.now + (60 * 24 * 3600) # Extending the expiry time by 60 days from now.
    database_admin_client.update_backup backup: backup,
                                        update_mask: { paths: ["expire_time"] }
    
    puts "Expiration time updated: #{backup.expire_time}"

## Delete a backup

When you delete a backup, Spanner releases the storage and all other resources associated with that backup.

If you delete a backup that's still being created, Spanner also cancels the long-running backup operation.

Deleting an incremental backup might not free up storage if a younger incremental backup depends on it. For more information, see [Backups overview](https://docs.cloud.google.com/spanner/docs/backup#incremental-backups).

### Console

  1. Go to the Spanner Instances page in the Google Cloud console.

[Go to the Spanner Instances page](https://console.cloud.google.com/spanner/instances)

  2. Click the instance containing the database to open its **Overview** page.

  3. Click the database to open its **Overview** page.

  4. In the navigation pane, click **Backup/Restore**.

  5. Click the **Actions** button for your selected backup, then select **Delete**.

  6. Type the backup ID.

  7. Click **Delete**.




###  gcloud 

To delete a backup, use [`gcloud spanner backups delete`](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/backups/delete).

Before using any of the command data below, make the following replacements: 

  * INSTANCE_ID: the Spanner instance ID.
  * BACKUP_NAME: the Spanner backup name.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backups delete BACKUP_NAME --instance=INSTANCE_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backups delete BACKUP_NAME --instance=INSTANCE_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backups delete BACKUP_NAME --instance=INSTANCE_ID

You should receive a response similar to the following:
    
    
    You are about to delete backup BACKUP_NAME
    
    Do you want to continue (Y/n)?  Y
    
    Deleted backup BACKUP_NAME.
    

### Client libraries

The following code sample deletes a backup and verifies that it was deleted.

### C++
    
    
    void DeleteBackup(google::cloud::spanner_admin::DatabaseAdminClient client,
                      std::string const& project_id, std::string const& instance_id,
                      std::string const& backup_id) {
      google::cloud::spanner::Backup backup(
          google::cloud::spanner::Instance(project_id, instance_id), backup_id);
      auto status = client.DeleteBackup(backup.FullName());
      if (!status.ok()) throw std::move(status);
      std::cout << "Backup " << backup.FullName() << " was deleted.\n";
    }

### C#
    
    
    using [Google.Cloud.Spanner.Admin.Database.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.html);
    using System;
    
    public class DeleteBackupSample
    {
        public void DeleteBackup(string projectId, string instanceId, string backupId)
        {
            // Create the DatabaseAdminClient instance.
            [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html) databaseAdminClient = [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_Create)();
    
            // Make the DeleteBackup request.
            [BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupName.html) backupName = [BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupName.html).[FromProjectInstanceBackup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupName.html#Google_Cloud_Spanner_Admin_Database_V1_BackupName_FromProjectInstanceBackup_System_String_System_String_System_String_)(projectId, instanceId, backupId);
            databaseAdminClient.[DeleteBackup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_DeleteBackup_Google_Cloud_Spanner_Admin_Database_V1_BackupName_Google_Api_Gax_Grpc_CallSettings_)(backupName);
    
            Console.WriteLine("Backup deleted successfully.");
        }
    }

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"regexp"
    
    	database "cloud.google.com/go/spanner/admin/database/apiv1"
    	adminpb "cloud.google.com/go/spanner/admin/database/apiv1/databasepb"
    )
    
    func deleteBackup(ctx context.Context, w io.Writer, db, backupID string) error {
    	adminClient, err := database.NewDatabaseAdminClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer adminClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/database/apiv1.html#cloud_google_com_go_spanner_admin_database_apiv1_DatabaseAdminClient_Close)()
    
    	matches := regexp.MustCompile("^(.*)/databases/(.*)$").FindStringSubmatch(db)
    	if matches == nil || len(matches) != 3 {
    		return fmt.Errorf("Invalid database id %s", db)
    	}
    	backupName := matches[1] + "/backups/" + backupID
    	// Delete the backup.
    	err = adminClient.DeleteBackup(ctx, &adminpb.DeleteBackupRequest{Name: backupName})
    	if err != nil {
    		return err
    	}
    	fmt.Fprintf(w, "Deleted backup %s\n", backupID)
    	return nil
    }
    

### Java
    
    
    static void deleteBackup(DatabaseAdminClient dbAdminClient,
        String project, String instance, String backupId) {
      BackupName backupName = BackupName.of(project, instance, backupId);
    
      // Delete the backup.
      System.out.println("Deleting backup [" + backupId + "]...");
      dbAdminClient.deleteBackup(backupName);
      // Verify that the backup is deleted.
      try {
        dbAdminClient.getBackup(backupName);
      } catch (NotFoundException e) {
        if (e.getStatusCode().getCode() == Code.NOT_FOUND) {
          System.out.println("Deleted backup [" + backupId + "]");
        } else {
          System.out.println("Delete backup [" + backupId + "] failed");
          throw new RuntimeException("Delete backup [" + backupId + "] failed", e);
        }
      }
    }

**Note:** The old client library interface code samples for Java are archived in [GitHub](https://github.com/googleapis/google-cloud-java/tree/main/java-spanner/samples/snippets/src/main/java/com/example/spanner/admin/archived). 

### Node.js
    
    
    // Imports the Google Cloud client library
    const {Spanner} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const projectId = 'my-project-id';
    // const instanceId = 'my-instance';
    // const databaseId = 'my-database';
    // const backupId = 'my-backup';
    
    // Creates a client
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({
      projectId: projectId,
    });
    
    // Gets a reference to a Cloud Spanner Database Admin Client object
    const databaseAdminClient = spanner.[getDatabaseAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)();
    
    // Delete the backup
    console.log(`Deleting backup ${backupId}.`);
    await databaseAdminClient.deleteBackup({
      name: databaseAdminClient.backupPath(projectId, instanceId, backupId),
    });
    console.log('Backup deleted.');
    
    // Verify backup no longer exists
    try {
      await databaseAdminClient.getBackup({
        name: databaseAdminClient.backupPath(projectId, instanceId, backupId),
      });
      console.error('Error: backup still exists.');
    } catch (err) {
      console.log('Backup deleted.');
    }

**Note:** The old client library interface code samples for Node.js are archived in [GitHub](https://github.com/googleapis/nodejs-spanner/tree/main/samples/archived). 

### PHP
    
    
    use Google\Cloud\Spanner\Admin\Database\V1\Client\DatabaseAdminClient;
    use Google\Cloud\Spanner\Admin\Database\V1\DeleteBackupRequest;
    
    /**
     * Delete a backup.
     * Example:
     * ```
     * delete_backup($projectId, $instanceId, $backupId);
     * ```
     * @param string $projectId The Google Cloud project ID.
     * @param string $instanceId The Spanner instance ID.
     * @param string $backupId The Spanner backup ID.
     */
    function delete_backup(string $projectId, string $instanceId, string $backupId): void
    {
        $databaseAdminClient = new DatabaseAdminClient();
    
        $backupName = DatabaseAdminClient::backupName($projectId, $instanceId, $backupId);
    
        $request = new DeleteBackupRequest();
        $request->setName($backupName);
        $databaseAdminClient->deleteBackup($request);
    
        print("Backup $backupName deleted" . PHP_EOL);
    }

**Note:** The old client library interface code samples for PHP are archived in [GitHub](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/main/spanner/src/admin/archived). 

### Python
    
    
    def delete_backup(instance_id, backup_id):
        from google.cloud.spanner_admin_database_v1.types import backup as backup_pb
    
        spanner_client = spanner.Client()
        database_admin_api = spanner_client.database_admin_api
        backup = database_admin_api.get_backup(
            backup_pb.GetBackupRequest(
                name=database_admin_api.backup_path(
                    spanner_client.project, instance_id, backup_id
                ),
            )
        )
    
        # Wait for databases that reference this backup to finish optimizing.
        while backup.referencing_databases:
            time.sleep(30)
            backup = database_admin_api.get_backup(
                backup_pb.GetBackupRequest(
                    name=database_admin_api.backup_path(
                        spanner_client.project, instance_id, backup_id
                    ),
                )
            )
    
        # Delete the backup.
        database_admin_api.delete_backup(backup_pb.DeleteBackupRequest(name=backup.name))
    
        # Verify that the backup is deleted.
        try:
            backup = database_admin_api.get_backup(
                backup_pb.GetBackupRequest(name=backup.name)
            )
        except NotFound:
            print("Backup {} has been deleted.".format(backup.name))
            return
    
    

**Note:** The old client library interface code samples for Python are archived in [GitHub](https://github.com/googleapis/python-spanner/tree/main/samples/samples/archived). 

### Ruby
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "Your Spanner instance ID"
    # backup_id = "Your Spanner backup ID"
    
    require "google/cloud/spanner"
    require "google/cloud/spanner/admin/database"
    
    database_admin_client = Google::Cloud::Spanner::Admin::Database.database_admin
    instance_path = database_admin_client.instance_path project: project_id, instance: instance_id
    backup_path = database_admin_client.backup_path project: project_id,
                                                    instance: instance_id,
                                                    backup: backup_id
    
    database_admin_client.delete_backup name: backup_path
    puts "Backup #{backup_id} deleted"

## What's next

  * To learn more about backups, see [Backups overview](https://docs.cloud.google.com/spanner/docs/backup).

  * To create backups, see [Create backups](https://docs.cloud.google.com/spanner/docs/backup/create-backups).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
