---
url: https://docs.cloud.google.com/spanner/docs/backup/create-manage-backup-schedules/
title: Create and manage backup schedules \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:41.110298+00:00
---

# Create and manage backup schedules  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/backup/create-manage-backup-schedules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Create and manage backup schedules Stay organized with collections  Save and categorize content based on your preferences. 

This page describes Spanner backup schedule operations and explains how to set up a backup schedule for your database.

## Before you begin

  * To get the permissions that you need to create and manage backup schedules, ask your administrator to grant you the following IAM roles on the instance: 

    * Create, view, update, and delete backup schedules: [Cloud Spanner Backup Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupAdmin) (`roles/spanner.backupAdmin`) 
    * Create and view backup schedules: [Cloud Spanner Backup Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupWriter) (`roles/spanner.backupWriter`) 

**Note:** [IAM basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) might also contain permissions to create and manage backup schedules. You shouldn't grant basic roles in a production environment, but you can grant them in a development or test environment. 



## Create a backup schedule

### Console

  1. In the Google Cloud console, go to the Spanner **Instances** page.



[Go to the Spanner Instances page](https://console.cloud.google.com/spanner/instances)

  1. Click the instance containing the database.

  2. Click the database.

  3. In the navigation menu, click the **Backup/Restore**.

  4. Click **Create backup schedule**.

  5. Fill out the form, then click **Create**.




###  gcloud 

Before using any of the command data below, make the following replacements: 

  * SCHEDULE_ID: the backup schedule ID. 
  * PROJECT_ID: the project ID.
  * INSTANCE_ID: the ID of the instance where you want to create the backup schedule. 
  * DATABASE_ID: the ID of the database where you want to create the backup schedule. 
  * RETENTION_DURATION: the retention duration of the backups created by the schedule. For example, if you want the retention duration to be one day, you can use `86400s`. 
  * CRONTAB_EXPRESSION: the crontab expression for the backup schedule frequency. For example, if you want the backup schedule frequency to be every 12 hours, you can use `0 12 * * *`. 
  * BACKUP_TYPE: whether it's a full backup schedule or an incremental backup schedule. Possible values are `full-backup` or `incremental-backup`. 
  * ENCRYPTION_TYPE: the encryption type of backups created by the backup schedule. Valid values are `USE_DATABASE_ENCRYPTION`, `GOOGLE_DEFAULT_ENCRYPTION` , or `CUSTOMER_MANAGED_ENCRYPTION`. If you use `CUSTOMER_MANAGED_ENCRYPTION`, you must specify a `kmsKeyName` or `kmsKeyNames`. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backup-schedules create SCHEDULE_ID \
      --project=PROJECT_ID \
      --instance=INSTANCE_ID \
      --database=DATABASE_ID \
      --retention-duration=RETENTION_DURATION \
      --cron="CRONTAB_EXPRESSION" \
      --backup-type=BACKUP_TYPE \
      --encryption-type=ENCRYPTION_TYPE

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backup-schedules create SCHEDULE_ID `
      --project=PROJECT_ID `
      --instance=INSTANCE_ID `
      --database=DATABASE_ID `
      --retention-duration=RETENTION_DURATION `
      --cron="CRONTAB_EXPRESSION" `
      --backup-type=BACKUP_TYPE `
      --encryption-type=ENCRYPTION_TYPE

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backup-schedules create SCHEDULE_ID ^
      --project=PROJECT_ID ^
      --instance=INSTANCE_ID ^
      --database=DATABASE_ID ^
      --retention-duration=RETENTION_DURATION ^
      --cron="CRONTAB_EXPRESSION" ^
      --backup-type=BACKUP_TYPE ^
      --encryption-type=ENCRYPTION_TYPE

### REST v1

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID.
  * INSTANCE_ID: the ID of the instance where you want to create the backup schedule. 
  * DATABASE_ID: the ID of the database where you want to create the backup schedule. 
  * SCHEDULE_ID: the backup schedule ID.
  * BACKUP_TYPE: whether it's a full backup schedule or an incremental backup schedule. Possible values are `fullBackupSpec` or `incrementalBackupSpec`. 
  * ENCRYPTION_TYPE: the encryption type of backups created by the backup schedule. Possible values are `USE_DATABASE_ENCRYPTION`, `GOOGLE_DEFAULT_ENCRYPTION`, or `CUSTOMER_MANAGED_ENCRYPTION`. If you use `CUSTOMER_MANAGED_ENCRYPTION`, you must specify a `kmsKeyName` or `kmsKeyNames`. 
  * RETENTION_DURATION: the retention duration of the backups created by the schedule. 



HTTP method and URL: 
    
    
    POST https://spanner.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID/backupSchedules?backup_schedule_id=SCHEDULE_ID

Request JSON body: 
    
    
    {
      "retentionDuration": "RETENTION_DURATION",
      "spec": {
        "cronSpec": {
          "text": "0 2 * * *"
        }
      },
      "encryptionConfig": {
        "encryptionType": "ENCRYPTION_TYPE"
      },
      "BACKUP_TYPE": {}
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://spanner.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID/backupSchedules?backup_schedule_id=SCHEDULE_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://spanner.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID/backupSchedules?backup_schedule_id=SCHEDULE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID/backupSchedules/SCHEDULE_ID",
      "retentionDuration": "86400s",
      "encryptionConfig": {
        "encryptionType": "USE_DATABASE_ENCRYPTION"
      },
      "spec": {
        "cronSpec": {
          "text": "0 2 * * *",
          "timeZone": "UTC",
          "creationWindow": "14400s"
        }
      },
      "BACKUP_TYPE": {},
      "updateTime": "2024-05-22T11:13:51.835590Z"
    }
    

### Client libraries

### C#

To create a full backup schedule, see the following sample code: 
    
    
    using [Google.Cloud.Spanner.Admin.Database.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.html);
    using [Google.Cloud.Spanner.Common.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    
    public class CreateFullBackupScheduleSample
    {
        public BackupSchedule CreateFullBackupSchedule(string projectId, string instanceId, string databaseId, string scheduleId)
        {
            [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html) client = [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_Create)();
    
            [BackupSchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupSchedule.html) response = client.[CreateBackupSchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_CreateBackupSchedule_Google_Cloud_Spanner_Admin_Database_V1_CreateBackupScheduleRequest_Google_Api_Gax_Grpc_CallSettings_)(
                new [CreateBackupScheduleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupScheduleRequest.html)
                {
                    ParentAsDatabaseName = [DatabaseName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.DatabaseName.html).[FromProjectInstanceDatabase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.DatabaseName.html#Google_Cloud_Spanner_Common_V1_DatabaseName_FromProjectInstanceDatabase_System_String_System_String_System_String_)(projectId, instanceId, databaseId),
                    BackupScheduleId = scheduleId,
                    BackupSchedule = new [BackupSchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupSchedule.html)
                    {
                        Spec = new [BackupScheduleSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupScheduleSpec.html)
                        {
                            CronSpec = new [CrontabSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CrontabSpec.html)
                            {
                                Text = "30 12 * * *",
                            }
                        },
                        RetentionDuration = new [Duration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)
                        {
                            Seconds = 86400,
                        },
                        EncryptionConfig = new [CreateBackupEncryptionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupEncryptionConfig.html)
                        {
                            EncryptionType = [CreateBackupEncryptionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupEncryptionConfig.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupEncryptionConfig.Types.html).[EncryptionType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupEncryptionConfig.Types.EncryptionType.html).[UseDatabaseEncryption](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupEncryptionConfig.Types.EncryptionType.html#Google_Cloud_Spanner_Admin_Database_V1_CreateBackupEncryptionConfig_Types_EncryptionType_UseDatabaseEncryption),
                        },
                        FullBackupSpec = new [FullBackupSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.FullBackupSpec.html) { },
                    }
                });
    
            Console.WriteLine($"Created full backup schedule: {response}");
            return response;
        }
    }

To create an incremental backup schedule, see the following sample code: 
    
    
    using [Google.Cloud.Spanner.Admin.Database.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.html);
    using [Google.Cloud.Spanner.Common.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    
    public class CreateIncrementalBackupScheduleSample
    {
        public BackupSchedule CreateIncrementalBackupSchedule(string projectId, string instanceId, string databaseId, string scheduleId)
        {
            [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html) client = [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_Create)();
    
            [BackupSchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupSchedule.html) response = client.[CreateBackupSchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_CreateBackupSchedule_Google_Cloud_Spanner_Admin_Database_V1_CreateBackupScheduleRequest_Google_Api_Gax_Grpc_CallSettings_)(
                new [CreateBackupScheduleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupScheduleRequest.html)
                {
                    ParentAsDatabaseName = [DatabaseName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.DatabaseName.html).[FromProjectInstanceDatabase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.DatabaseName.html#Google_Cloud_Spanner_Common_V1_DatabaseName_FromProjectInstanceDatabase_System_String_System_String_System_String_)(projectId, instanceId, databaseId),
                    BackupScheduleId = scheduleId,
                    BackupSchedule = new [BackupSchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupSchedule.html)
                    {
                        Spec = new [BackupScheduleSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupScheduleSpec.html)
                        {
                            CronSpec = new [CrontabSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CrontabSpec.html)
                            {
                                Text = "30 12 * * *",
                            }
                        },
                        RetentionDuration = new [Duration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)
                        {
                            Seconds = 86400,
                        },
                        EncryptionConfig = new [CreateBackupEncryptionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupEncryptionConfig.html)
                        {
                            EncryptionType = [CreateBackupEncryptionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupEncryptionConfig.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupEncryptionConfig.Types.html).[EncryptionType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupEncryptionConfig.Types.EncryptionType.html).[GoogleDefaultEncryption](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupEncryptionConfig.Types.EncryptionType.html#Google_Cloud_Spanner_Admin_Database_V1_CreateBackupEncryptionConfig_Types_EncryptionType_GoogleDefaultEncryption),
                        },
                        IncrementalBackupSpec = new [IncrementalBackupSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.IncrementalBackupSpec.html) { },
                    }
                });
    
            Console.WriteLine($"Created incremental backup schedule: {response}");
            return response;
        }
    }

### C++

To create a full backup schedule, see the following sample code: 
    
    
    void CreateFullBackupSchedule(
        google::cloud::spanner_admin::DatabaseAdminClient client,
        std::string const& project_id, std::string const& instance_id,
        std::string const& database_id, std::string const& backup_schedule_id) {
      google::spanner::admin::database::v1::BackupSchedule backup_schedule;
      *backup_schedule.mutable_full_backup_spec() = {};
      backup_schedule.mutable_spec()->mutable_cron_spec()->set_text("30 12 * * *");
      backup_schedule.mutable_retention_duration()->set_seconds(3600 * 24);
    
      google::spanner::admin::database::v1::CreateBackupEncryptionConfig
          encryption_config;
      encryption_config.set_encryption_type(
          google::spanner::admin::database::v1::CreateBackupEncryptionConfig::
              USE_DATABASE_ENCRYPTION);
      *backup_schedule.mutable_encryption_config() = std::move(encryption_config);
    
      google::cloud::spanner::Database db(project_id, instance_id, database_id);
      google::spanner::admin::database::v1::CreateBackupScheduleRequest request;
      request.set_parent(db.FullName());
      request.set_backup_schedule_id(backup_schedule_id);
      *request.mutable_backup_schedule() = std::move(backup_schedule);
    
      auto created_backup_schedule = client.CreateBackupSchedule(request);
      if (!created_backup_schedule) {
        throw std::move(created_backup_schedule).status();
      }
      std::cout << "Backup schedule " << created_backup_schedule->name()
                << " created at "
                << *google::cloud::spanner::MakeTimestamp(
                       created_backup_schedule->update_time());
    }

To create an incremental backup schedule, see the following sample code: 
    
    
    void CreateIncrementalBackupSchedule(
        google::cloud::spanner_admin::DatabaseAdminClient client,
        std::string const& project_id, std::string const& instance_id,
        std::string const& database_id, std::string const& backup_schedule_id) {
      google::spanner::admin::database::v1::BackupSchedule backup_schedule;
      *backup_schedule.mutable_incremental_backup_spec() = {};
      backup_schedule.mutable_spec()->mutable_cron_spec()->set_text("30 12 * * *");
      backup_schedule.mutable_retention_duration()->set_seconds(3600 * 24);
    
      google::spanner::admin::database::v1::CreateBackupEncryptionConfig
          encryption_config;
      encryption_config.set_encryption_type(
          google::spanner::admin::database::v1::CreateBackupEncryptionConfig::
              GOOGLE_DEFAULT_ENCRYPTION);
      *backup_schedule.mutable_encryption_config() = std::move(encryption_config);
    
      google::cloud::spanner::Database db(project_id, instance_id, database_id);
      google::spanner::admin::database::v1::CreateBackupScheduleRequest request;
      request.set_parent(db.FullName());
      request.set_backup_schedule_id(backup_schedule_id);
      *request.mutable_backup_schedule() = std::move(backup_schedule);
    
      auto created_backup_schedule = client.CreateBackupSchedule(request);
      if (!created_backup_schedule) {
        throw std::move(created_backup_schedule).status();
      }
      std::cout << "Incremental backup schedule " << created_backup_schedule->name()
                << " created at "
                << *google::cloud::spanner::MakeTimestamp(
                       created_backup_schedule->update_time());
    }

### Go

To create a full backup schedule, see the following sample code: 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	database "cloud.google.com/go/spanner/admin/database/apiv1"
    	"cloud.google.com/go/spanner/admin/database/apiv1/databasepb"
    	"google.golang.org/protobuf/types/known/durationpb"
    )
    
    func createFullBackupSchedule(w io.Writer, dbName string, scheduleId string) error {
    	ctx := context.Background()
    
    	client, err := database.NewDatabaseAdminClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/database/apiv1.html#cloud_google_com_go_spanner_admin_database_apiv1_DatabaseAdminClient_Close)()
    
    	// Create a schedule to create full backups daily at 12:30 AM, using the
    	// database's encryption config, and retained for 24 hours.
    	req := databasepb.CreateBackupScheduleRequest{
    		Parent:           dbName,
    		BackupScheduleId: scheduleId,
    		BackupSchedule: &databasepb.BackupSchedule{
    			Spec: &databasepb.BackupScheduleSpec{
    				ScheduleSpec: &databasepb.BackupScheduleSpec_CronSpec{
    					CronSpec: &databasepb.CrontabSpec{
    						Text: "30 12 * * *",
    					},
    				},
    			},
    			RetentionDuration: durationpb.New(24 * time.Hour),
    			EncryptionConfig: &databasepb.CreateBackupEncryptionConfig{
    				EncryptionType: databasepb.[CreateBackupEncryptionConfig_USE_DATABASE_ENCRYPTION](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/database/apiv1/databasepb.html#cloud_google_com_go_spanner_admin_database_apiv1_databasepb_CreateBackupEncryptionConfig_ENCRYPTION_TYPE_UNSPECIFIED_CreateBackupEncryptionConfig_USE_DATABASE_ENCRYPTION_CreateBackupEncryptionConfig_GOOGLE_DEFAULT_ENCRYPTION_CreateBackupEncryptionConfig_CUSTOMER_MANAGED_ENCRYPTION),
    			},
    			BackupTypeSpec: &databasepb.BackupSchedule_FullBackupSpec{},
    		},
    	}
    
    	res, err := client.CreateBackupSchedule(ctx, &req)
    	if err != nil {
    		return err
    	}
    
    	fmt.Fprintf(w, "Created full backup schedule: %s", res)
    	return nil
    }
    

To create an incremental backup schedule, see the following sample code: 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	database "cloud.google.com/go/spanner/admin/database/apiv1"
    	"cloud.google.com/go/spanner/admin/database/apiv1/databasepb"
    	"google.golang.org/protobuf/types/known/durationpb"
    )
    
    func createIncrementalBackupSchedule(w io.Writer, dbName string, scheduleId string) error {
    	ctx := context.Background()
    
    	client, err := database.NewDatabaseAdminClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/database/apiv1.html#cloud_google_com_go_spanner_admin_database_apiv1_DatabaseAdminClient_Close)()
    
    	// Create a schedule to create incremental backups daily at 12:30 AM, using
    	// Google-managed encryption, and retained for 24 hours.
    	req := databasepb.CreateBackupScheduleRequest{
    		Parent:           dbName,
    		BackupScheduleId: scheduleId,
    		BackupSchedule: &databasepb.BackupSchedule{
    			Spec: &databasepb.BackupScheduleSpec{
    				ScheduleSpec: &databasepb.BackupScheduleSpec_CronSpec{
    					CronSpec: &databasepb.CrontabSpec{
    						Text: "30 12 * * *",
    					},
    				},
    			},
    			RetentionDuration: durationpb.New(24 * time.Hour),
    			EncryptionConfig: &databasepb.CreateBackupEncryptionConfig{
    				EncryptionType: databasepb.[CreateBackupEncryptionConfig_GOOGLE_DEFAULT_ENCRYPTION](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/database/apiv1/databasepb.html#cloud_google_com_go_spanner_admin_database_apiv1_databasepb_CreateBackupEncryptionConfig_ENCRYPTION_TYPE_UNSPECIFIED_CreateBackupEncryptionConfig_USE_DATABASE_ENCRYPTION_CreateBackupEncryptionConfig_GOOGLE_DEFAULT_ENCRYPTION_CreateBackupEncryptionConfig_CUSTOMER_MANAGED_ENCRYPTION),
    			},
    			BackupTypeSpec: &databasepb.BackupSchedule_IncrementalBackupSpec{},
    		},
    	}
    
    	res, err := client.CreateBackupSchedule(ctx, &req)
    	if err != nil {
    		return err
    	}
    
    	fmt.Fprintf(w, "Created incremental backup schedule: %s", res)
    	return nil
    }
    

### Java

To create a full backup schedule, see the following sample code: 
    
    
    import com.google.cloud.spanner.admin.database.v1.[DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import com.google.spanner.admin.database.v1.[BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupSchedule.html);
    import com.google.spanner.admin.database.v1.[BackupScheduleSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupScheduleSpec.html);
    import com.google.spanner.admin.database.v1.[CreateBackupEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateBackupEncryptionConfig.html);
    import com.google.spanner.admin.database.v1.[CreateBackupScheduleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateBackupScheduleRequest.html);
    import com.google.spanner.admin.database.v1.[CrontabSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CrontabSpec.html);
    import com.google.spanner.admin.database.v1.[DatabaseName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.DatabaseName.html);
    import com.google.spanner.admin.database.v1.[FullBackupSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.FullBackupSpec.html);
    import java.io.IOException;
    
    class CreateFullBackupScheduleSample {
    
      static void createFullBackupSchedule() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project";
        String instanceId = "my-instance";
        String databaseId = "my-database";
        String backupScheduleId = "my-backup-schedule";
        createFullBackupSchedule(projectId, instanceId, databaseId, backupScheduleId);
      }
    
      static void createFullBackupSchedule(
          String projectId, String instanceId, String databaseId, String backupScheduleId)
          throws IOException {
        final [CreateBackupEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateBackupEncryptionConfig.html) encryptionConfig =
            [CreateBackupEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateBackupEncryptionConfig.html).newBuilder()
                .setEncryptionType([CreateBackupEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateBackupEncryptionConfig.html).EncryptionType.USE_DATABASE_ENCRYPTION)
                .build();
        final [BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupSchedule.html) backupSchedule =
            [BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupSchedule.html).newBuilder()
                .[setFullBackupSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupSchedule.Builder.html#com_google_spanner_admin_database_v1_BackupSchedule_Builder_setFullBackupSpec_com_google_spanner_admin_database_v1_FullBackupSpec_)([FullBackupSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.FullBackupSpec.html).newBuilder().build())
                .[setRetentionDuration](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupSchedule.Builder.html#com_google_spanner_admin_database_v1_BackupSchedule_Builder_setRetentionDuration_com_google_protobuf_Duration_)([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(3600 * 24).build())
                .[setSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupSchedule.Builder.html#com_google_spanner_admin_database_v1_BackupSchedule_Builder_setSpec_com_google_spanner_admin_database_v1_BackupScheduleSpec_)(
                    [BackupScheduleSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupScheduleSpec.html).newBuilder()
                        .[setCronSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupScheduleSpec.Builder.html#com_google_spanner_admin_database_v1_BackupScheduleSpec_Builder_setCronSpec_com_google_spanner_admin_database_v1_CrontabSpec_)([CrontabSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CrontabSpec.html).newBuilder().[setText](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CrontabSpec.Builder.html#com_google_spanner_admin_database_v1_CrontabSpec_Builder_setText_java_lang_String_)("30 12 * * *").build())
                        .build())
                .setEncryptionConfig(encryptionConfig)
                .build();
    
        try ([DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html) databaseAdminClient = [DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html).create()) {
          [DatabaseName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.DatabaseName.html) databaseName = [DatabaseName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.DatabaseName.html).of(projectId, instanceId, databaseId);
          final [BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupSchedule.html) createdBackupSchedule =
              databaseAdminClient.createBackupSchedule(
                  [CreateBackupScheduleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateBackupScheduleRequest.html).newBuilder()
                      .setParent(databaseName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.DatabaseName.html#com_google_spanner_admin_database_v1_DatabaseName_toString__)())
                      .[setBackupScheduleId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateBackupScheduleRequest.Builder.html#com_google_spanner_admin_database_v1_CreateBackupScheduleRequest_Builder_setBackupScheduleId_java_lang_String_)(backupScheduleId)
                      .setBackupSchedule(backupSchedule)
                      .build());
          System.out.println(
              String.format(
                  "Created backup schedule: %s\n%s",
                  createdBackupSchedule.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupSchedule.html#com_google_spanner_admin_database_v1_BackupSchedule_getName__)(), createdBackupSchedule.toString()));
        }
      }
    }

To create an incremental backup schedule, see the following sample code: 
    
    
    import com.google.cloud.spanner.admin.database.v1.[DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import com.google.spanner.admin.database.v1.[BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupSchedule.html);
    import com.google.spanner.admin.database.v1.[BackupScheduleSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupScheduleSpec.html);
    import com.google.spanner.admin.database.v1.[CreateBackupEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateBackupEncryptionConfig.html);
    import com.google.spanner.admin.database.v1.[CreateBackupScheduleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateBackupScheduleRequest.html);
    import com.google.spanner.admin.database.v1.[CrontabSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CrontabSpec.html);
    import com.google.spanner.admin.database.v1.[DatabaseName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.DatabaseName.html);
    import com.google.spanner.admin.database.v1.[IncrementalBackupSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.IncrementalBackupSpec.html);
    import java.io.IOException;
    
    class CreateIncrementalBackupScheduleSample {
    
      static void createIncrementalBackupSchedule() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project";
        String instanceId = "my-instance";
        String databaseId = "my-database";
        String backupScheduleId = "my-backup-schedule";
        createIncrementalBackupSchedule(projectId, instanceId, databaseId, backupScheduleId);
      }
    
      static void createIncrementalBackupSchedule(
          String projectId, String instanceId, String databaseId, String backupScheduleId)
          throws IOException {
        final [CreateBackupEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateBackupEncryptionConfig.html) encryptionConfig =
            [CreateBackupEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateBackupEncryptionConfig.html).newBuilder()
                .setEncryptionType(
                    [CreateBackupEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateBackupEncryptionConfig.html).EncryptionType.GOOGLE_DEFAULT_ENCRYPTION)
                .build();
        final [BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupSchedule.html) backupSchedule =
            [BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupSchedule.html).newBuilder()
                .[setIncrementalBackupSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupSchedule.Builder.html#com_google_spanner_admin_database_v1_BackupSchedule_Builder_setIncrementalBackupSpec_com_google_spanner_admin_database_v1_IncrementalBackupSpec_)([IncrementalBackupSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.IncrementalBackupSpec.html).newBuilder().build())
                .[setRetentionDuration](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupSchedule.Builder.html#com_google_spanner_admin_database_v1_BackupSchedule_Builder_setRetentionDuration_com_google_protobuf_Duration_)([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(3600 * 24).build())
                .[setSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupSchedule.Builder.html#com_google_spanner_admin_database_v1_BackupSchedule_Builder_setSpec_com_google_spanner_admin_database_v1_BackupScheduleSpec_)(
                    [BackupScheduleSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupScheduleSpec.html).newBuilder()
                        .[setCronSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupScheduleSpec.Builder.html#com_google_spanner_admin_database_v1_BackupScheduleSpec_Builder_setCronSpec_com_google_spanner_admin_database_v1_CrontabSpec_)([CrontabSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CrontabSpec.html).newBuilder().[setText](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CrontabSpec.Builder.html#com_google_spanner_admin_database_v1_CrontabSpec_Builder_setText_java_lang_String_)("30 12 * * *").build())
                        .build())
                .setEncryptionConfig(encryptionConfig)
                .build();
    
        try ([DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html) databaseAdminClient = [DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html).create()) {
          [DatabaseName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.DatabaseName.html) databaseName = [DatabaseName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.DatabaseName.html).of(projectId, instanceId, databaseId);
          final [BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupSchedule.html) createdBackupSchedule =
              databaseAdminClient.createBackupSchedule(
                  [CreateBackupScheduleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateBackupScheduleRequest.html).newBuilder()
                      .setParent(databaseName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.DatabaseName.html#com_google_spanner_admin_database_v1_DatabaseName_toString__)())
                      .[setBackupScheduleId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateBackupScheduleRequest.Builder.html#com_google_spanner_admin_database_v1_CreateBackupScheduleRequest_Builder_setBackupScheduleId_java_lang_String_)(backupScheduleId)
                      .setBackupSchedule(backupSchedule)
                      .build());
          System.out.println(
              String.format(
                  "Created incremental backup schedule: %s\n%s",
                  createdBackupSchedule.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupSchedule.html#com_google_spanner_admin_database_v1_BackupSchedule_getName__)(), createdBackupSchedule.toString()));
        }
      }
    }

### Node.js

To create a full backup schedule, see the following sample code: 
    
    
    // Import the Google Cloud client library for Spanner.
    const {Spanner} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'my-project-id';
    // const instanceId = 'my-instance-id';
    // const databaseId = 'my-database-id';
    // const scheduleId = 'my-schedule-id';
    
    // Create a Spanner database admin client.
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({projectId});
    const client = spanner.[getDatabaseAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)();
    
    try {
      // Create a schedule to create full backups daily at 12:30 AM, using the
      // database's encryption config, and retained for 24 hours.
      const [response] = await [client](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/requestconfig.html).createBackupSchedule({
        parent: [client](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/requestconfig.html).databasePath(projectId, instanceId, databaseId),
        backupScheduleId: scheduleId,
        backupSchedule: {
          spec: {
            cronSpec: {
              text: '30 12 * * *',
            },
          },
          retentionDuration: {
            seconds: 86400,
          },
          encryptionConfig: {
            encryptionType: 'USE_DATABASE_ENCRYPTION',
          },
          fullBackupSpec: {},
        },
      });
      console.log('Created full backup schedule:', response);
    } catch (err) {
      console.error('ERROR:', err);
    }

To create an incremental backup schedule, see the following sample code: 
    
    
    // Import the Google Cloud client library for Spanner.
    const {Spanner} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'my-project-id';
    // const instanceId = 'my-instance-id';
    // const databaseId = 'my-database-id';
    // const scheduleId = 'my-schedule-id';
    
    // Create a Spanner database admin client.
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({projectId});
    const client = spanner.[getDatabaseAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)();
    
    try {
      // Create a schedule to create incremental backups daily at 12:30 AM,
      // using Google-managed encryption, and retained for 24 hours.
      const [response] = await [client](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/requestconfig.html).createBackupSchedule({
        parent: [client](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/requestconfig.html).databasePath(projectId, instanceId, databaseId),
        backupScheduleId: scheduleId,
        backupSchedule: {
          spec: {
            cronSpec: {
              text: '30 12 * * *',
            },
          },
          retentionDuration: {
            seconds: 86400,
          },
          encryptionConfig: {
            encryptionType: 'GOOGLE_DEFAULT_ENCRYPTION',
          },
          incrementalBackupSpec: {},
        },
      });
      console.log('Created incremental backup schedule:', response);
    } catch (err) {
      console.error('ERROR:', err);
    }

### PHP

To create a full backup schedule, see the following sample code: 
    
    
    use Google\Cloud\Spanner\Admin\Database\V1\Client\DatabaseAdminClient;
    use Google\Cloud\Spanner\Admin\Database\V1\CreateBackupScheduleRequest;
    use Google\Cloud\Spanner\Admin\Database\V1\CreateBackupEncryptionConfig;
    use Google\Cloud\Spanner\Admin\Database\V1\CreateBackupEncryptionConfig\EncryptionType;
    use Google\Cloud\Spanner\Admin\Database\V1\BackupSchedule;
    use Google\Cloud\Spanner\Admin\Database\V1\FullBackupSpec;
    use Google\Cloud\Spanner\Admin\Database\V1\BackupScheduleSpec;
    use Google\Cloud\Spanner\Admin\Database\V1\CrontabSpec;
    use Google\Protobuf\Duration;
    
    /**
     * Create a backup schedule.
     * Example:
     * ```
     * create_backup_schedule($projectId, $instanceId, $databaseId, $backupScheduleId);
     * ```
     *
     * @param string $projectId The Google Cloud project ID.
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     * @param string $backupScheduleId The ID of the backup schedule to be created.
     * at https://cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.backupSchedules#BackupSchedule.FIELDS
     */
    function create_backup_schedule(
        string $projectId,
        string $instanceId,
        string $databaseId,
        string $backupScheduleId,
    ): void {
        $databaseAdminClient = new DatabaseAdminClient();
        $databaseFullName = DatabaseAdminClient::databaseName($projectId, $instanceId, $databaseId);
        printf('%s', $databaseFullName);
    
        $encryptionConfig = (new CreateBackupEncryptionConfig())
            ->setEncryptionType(EncryptionType::USE_DATABASE_ENCRYPTION);
        $backupSchedule = new BackupSchedule([
            'full_backup_spec' => new FullBackupSpec(),
            'retention_duration' => (new Duration())
                ->setSeconds(24 * 60 * 60),
            'spec' => new BackupScheduleSpec([
                'cron_spec' => new CrontabSpec([
                    'text' => '30 12 * * *'
                ]),
            ]),
            'encryption_config' => $encryptionConfig,
        ]);
        $request = new CreateBackupScheduleRequest([
            'parent' => $databaseFullName,
            'backup_schedule_id' => $backupScheduleId,
            'backup_schedule' => $backupSchedule,
        ]);
    
        $created_backup_schedule = $databaseAdminClient->createBackupSchedule($request);
    
        printf('Created backup scehedule %s' . PHP_EOL, $created_backup_schedule->getName());
    }

### Python

To create a full backup schedule, see the following sample code: 
    
    
    def create_full_backup_schedule(
        instance_id: str,
        database_id: str,
        schedule_id: str,
    ) -> None:
        from datetime import timedelta
        from google.cloud import [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html)
        from google.cloud.spanner_admin_database_v1.types import (
            backup_schedule as backup_schedule_pb,
        )
        from google.cloud.spanner_admin_database_v1.types import (
            [CreateBackupEncryptionConfig](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CreateBackupEncryptionConfig.html),
            [FullBackupSpec](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.FullBackupSpec.html),
        )
    
        client = [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html).[Client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html)()
        database_admin_api = [client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.html).[database_admin_api](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html#google_cloud_spanner_v1_client_Client_database_admin_api)
    
        request = backup_schedule_pb.[CreateBackupScheduleRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CreateBackupScheduleRequest.html)(
            parent=[database_admin_api](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html#google_cloud_spanner_v1_client_Client_database_admin_api).database_path(
                [client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.html).project, instance_id, database_id
            ),
            backup_schedule_id=schedule_id,
            backup_schedule=backup_schedule_pb.[BackupSchedule](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.BackupSchedule.html)(
                spec=backup_schedule_pb.[BackupScheduleSpec](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.BackupScheduleSpec.html)(
                    cron_spec=backup_schedule_pb.[CrontabSpec](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CrontabSpec.html)(
                        text="30 12 * * *",
                    ),
                ),
                retention_duration=timedelta(hours=24),
                encryption_config=CreateBackupEncryptionConfig(
                    encryption_type=[CreateBackupEncryptionConfig](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CreateBackupEncryptionConfig.html).EncryptionType.USE_DATABASE_ENCRYPTION,
                ),
                full_backup_spec=FullBackupSpec(),
            ),
        )
    
        response = [database_admin_api](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html#google_cloud_spanner_v1_client_Client_database_admin_api).create_backup_schedule(request)
        print(f"Created full backup schedule: {response}")
    
    

To create an incremental backup schedule, see the following sample code: 
    
    
    def create_incremental_backup_schedule(
        instance_id: str,
        database_id: str,
        schedule_id: str,
    ) -> None:
        from datetime import timedelta
        from google.cloud import [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html)
        from google.cloud.spanner_admin_database_v1.types import (
            backup_schedule as backup_schedule_pb,
        )
        from google.cloud.spanner_admin_database_v1.types import (
            [CreateBackupEncryptionConfig](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CreateBackupEncryptionConfig.html),
            [IncrementalBackupSpec](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.IncrementalBackupSpec.html),
        )
    
        client = [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html).[Client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html)()
        database_admin_api = [client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.html).[database_admin_api](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html#google_cloud_spanner_v1_client_Client_database_admin_api)
    
        request = backup_schedule_pb.[CreateBackupScheduleRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CreateBackupScheduleRequest.html)(
            parent=[database_admin_api](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html#google_cloud_spanner_v1_client_Client_database_admin_api).database_path(
                [client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.html).project, instance_id, database_id
            ),
            backup_schedule_id=schedule_id,
            backup_schedule=backup_schedule_pb.[BackupSchedule](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.BackupSchedule.html)(
                spec=backup_schedule_pb.[BackupScheduleSpec](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.BackupScheduleSpec.html)(
                    cron_spec=backup_schedule_pb.[CrontabSpec](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CrontabSpec.html)(
                        text="30 12 * * *",
                    ),
                ),
                retention_duration=timedelta(hours=24),
                encryption_config=CreateBackupEncryptionConfig(
                    encryption_type=[CreateBackupEncryptionConfig](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CreateBackupEncryptionConfig.html).EncryptionType.GOOGLE_DEFAULT_ENCRYPTION,
                ),
                incremental_backup_spec=IncrementalBackupSpec(),
            ),
        )
    
        response = [database_admin_api](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html#google_cloud_spanner_v1_client_Client_database_admin_api).create_backup_schedule(request)
        print(f"Created incremental backup schedule: {response}")
    
    

## Get a backup schedule

### Console

  1. In the Google Cloud console, go to the Spanner **Instances** page.



[Go to the Spanner Instances page](https://console.cloud.google.com/spanner/instances)

  1. Click the instance containing the database.

  2. Click the database.

  3. In the navigation menu, click the **Backup/Restore**.

  4. Click the **Schedules** tab to view all the backup schedules and their information.




###  gcloud 

Before using any of the command data below, make the following replacements: 

  * PROJECT_ID: the project ID.
  * INSTANCE_ID: the instance ID.
  * DATABASE_ID: the database ID.
  * SCHEDULE_ID: the backup schedule ID.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backup-schedules describe SCHEDULE_ID \
      --project=PROJECT_ID \
      --instance=INSTANCE_ID \
      --database=DATABASE_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backup-schedules describe SCHEDULE_ID `
      --project=PROJECT_ID `
      --instance=INSTANCE_ID `
      --database=DATABASE_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backup-schedules describe SCHEDULE_ID ^
      --project=PROJECT_ID ^
      --instance=INSTANCE_ID ^
      --database=DATABASE_ID

You should receive a response similar to the following:
    
    
    {
      encryptionConfig:
        encryptionType: USE_DATABASE_ENCRYPTION
      incrementalBackupSpec: {}
      name: projects/my-project/instances/my-instance/databases/my-database/backupSchedules/my-schedule
      retentionDuration: 2592000s
      spec:
        cronSpec:
          creationWindow: 14400s
          text: 0 */4 * * *
          timeZone: UTC
      updateTime: '2024-09-13T10:24:18.754839Z'
    }
    

### REST v1

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID.
  * INSTANCE_ID: the instance ID.
  * DATABASE_ID: the database ID.
  * SCHEDULE_ID: the backup schedule ID.



HTTP method and URL: 
    
    
    GET https://spanner.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID/backupSchedules/SCHEDULE_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://spanner.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID/backupSchedules/SCHEDULE_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://spanner.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID/backupSchedules/SCHEDULE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID/backupSchedules/SCHEDULE_ID",
      "retentionDuration": "100000s",
      "encryptionConfig": {
        "encryptionType": "USE_DATABASE_ENCRYPTION"
      },
      "spec": {
        "cronSpec": {
          "text": "0 2 * * *",
          "timeZone": "UTC",
          "creationWindow": "14400s"
        }
      },
      "fullBackupSpec": {},
      "updateTime": "2024-05-22T11:13:51.835590Z"
    }
    

### Client libraries

### C#
    
    
    using [Google.Cloud.Spanner.Admin.Database.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.html);
    using System;
    
    public class GetBackupScheduleSample
    {
        public BackupSchedule GetBackupSchedule(string projectId, string instanceId, string databaseId, string scheduleId)
        {
            [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html) client = [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_Create)();
    
            [BackupSchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupSchedule.html) response = client.[GetBackupSchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_GetBackupSchedule_Google_Cloud_Spanner_Admin_Database_V1_BackupScheduleName_Google_Api_Gax_Grpc_CallSettings_)([BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupScheduleName.html).[FromProjectInstanceDatabaseSchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupScheduleName.html#Google_Cloud_Spanner_Admin_Database_V1_BackupScheduleName_FromProjectInstanceDatabaseSchedule_System_String_System_String_System_String_System_String_)(projectId, instanceId, databaseId, scheduleId));
    
            Console.WriteLine($"Backup schedule: {response}");
            return response;
        }
    }

### C++
    
    
    void GetBackupSchedule(google::cloud::spanner_admin::DatabaseAdminClient client,
                           std::string const& project_id,
                           std::string const& instance_id,
                           std::string const& database_id,
                           std::string const& backup_schedule_id) {
      google::cloud::spanner::Database db(project_id, instance_id, database_id);
      std::string backup_schedule_name =
          db.FullName() + "/backupSchedules/" + backup_schedule_id;
    
      google::spanner::admin::database::v1::GetBackupScheduleRequest request;
      request.set_name(backup_schedule_name);
    
      auto backup_schedule = client.GetBackupSchedule(request);
      if (!backup_schedule) throw std::move(backup_schedule).status();
      std::cout << "Retrieved backup schedule:\n" << backup_schedule->DebugString();
    }

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	database "cloud.google.com/go/spanner/admin/database/apiv1"
    	"cloud.google.com/go/spanner/admin/database/apiv1/databasepb"
    )
    
    func getBackupSchedule(w io.Writer, dbName string, scheduleId string) error {
    	ctx := context.Background()
    
    	client, err := database.NewDatabaseAdminClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/database/apiv1.html#cloud_google_com_go_spanner_admin_database_apiv1_DatabaseAdminClient_Close)()
    
    	req := databasepb.GetBackupScheduleRequest{
    		Name: fmt.Sprintf("%s/backupSchedules/%s", dbName, scheduleId),
    	}
    
    	res, err := client.GetBackupSchedule(ctx, &req)
    	if err != nil {
    		return err
    	}
    
    	fmt.Fprintf(w, "Backup schedule: %s", res)
    	return nil
    }
    

### Java
    
    
    import com.google.cloud.spanner.admin.database.v1.[DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html);
    import com.google.spanner.admin.database.v1.[BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupSchedule.html);
    import com.google.spanner.admin.database.v1.[BackupScheduleName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupScheduleName.html);
    import com.google.spanner.admin.database.v1.[GetBackupScheduleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.GetBackupScheduleRequest.html);
    import java.io.IOException;
    
    class GetBackupScheduleSample {
    
      static void getBackupSchedule() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project";
        String instanceId = "my-instance";
        String databaseId = "my-database";
        String backupScheduleId = "my-backup-schedule";
        getBackupSchedule(projectId, instanceId, databaseId, backupScheduleId);
      }
    
      static void getBackupSchedule(
          String projectId, String instanceId, String databaseId, String backupScheduleId)
          throws IOException {
        try ([DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html) databaseAdminClient = [DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html).create()) {
          [BackupScheduleName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupScheduleName.html) backupScheduleName =
              [BackupScheduleName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupScheduleName.html).of(projectId, instanceId, databaseId, backupScheduleId);
          final [BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupSchedule.html) backupSchedule =
              databaseAdminClient.getBackupSchedule(
                  [GetBackupScheduleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.GetBackupScheduleRequest.html).newBuilder().setName(backupScheduleName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupScheduleName.html#com_google_spanner_admin_database_v1_BackupScheduleName_toString__)()).build());
          System.out.println(
              String.format(
                  "Backup schedule: %s\n%s", backupSchedule.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupSchedule.html#com_google_spanner_admin_database_v1_BackupSchedule_getName__)(), backupSchedule.toString()));
        }
      }
    }

### Node.js
    
    
    // Import the Google Cloud client library for Spanner.
    const {Spanner} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'my-project-id';
    // const instanceId = 'my-instance-id';
    // const databaseId = 'my-database-id';
    // const scheduleId = 'my-schedule-id';
    
    // Create a Spanner database admin client.
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({projectId});
    const client = spanner.[getDatabaseAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)();
    
    try {
      // Get the backup schedule.
      const [response] = await [client](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/requestconfig.html).getBackupSchedule({
        name: [client](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/requestconfig.html).backupSchedulePath(
          projectId,
          instanceId,
          databaseId,
          scheduleId,
        ),
      });
      console.log('Backup schedule:', response);
    } catch (err) {
      console.error('ERROR:', err);
    }

### PHP
    
    
    use Google\Cloud\Spanner\Admin\Database\V1\Client\DatabaseAdminClient;
    use Google\Cloud\Spanner\Admin\Database\V1\GetBackupScheduleRequest;
    
    /**
     * Get a backup schedule.
     * Example:
     * ```
     * get_backup_schedule($projectId, $instanceId, $databaseId, $backupScheduleId);
     * ```
     *
     * @param string $projectId The Google Cloud project ID.
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     * @param string $backupScheduleId The ID of the backup schedule to be created.
     * at https://cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.backupSchedules#BackupSchedule.FIELDS
     */
    function get_backup_schedule(
        string $projectId,
        string $instanceId,
        string $databaseId,
        string $backupScheduleId,
    ): void {
        $databaseAdminClient = new DatabaseAdminClient();
    
        $backupScheduleName = sprintf(
            'projects/%s/instances/%s/databases/%s/backupSchedules/%s',
            $projectId,
            $instanceId,
            $databaseId,
            $backupScheduleId
        );
        $request = new GetBackupScheduleRequest([
            'name' => $backupScheduleName,
        ]);
    
        $backup_schedule = $databaseAdminClient->getBackupSchedule($request);
    
        printf('Fetched backup scehedule %s' . PHP_EOL, $backup_schedule->getName());
    }

### Python
    
    
    def get_backup_schedule(
        instance_id: str,
        database_id: str,
        schedule_id: str,
    ) -> None:
        from google.cloud import [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html)
        from google.cloud.spanner_admin_database_v1.types import (
            backup_schedule as backup_schedule_pb,
        )
    
        client = [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html).[Client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html)()
        database_admin_api = [client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.html).[database_admin_api](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html#google_cloud_spanner_v1_client_Client_database_admin_api)
    
        request = backup_schedule_pb.[GetBackupScheduleRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.GetBackupScheduleRequest.html)(
            name=[database_admin_api](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html#google_cloud_spanner_v1_client_Client_database_admin_api).backup_schedule_path(
                [client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.html).project,
                instance_id,
                database_id,
                schedule_id,
            ),
        )
    
        response = [database_admin_api](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html#google_cloud_spanner_v1_client_Client_database_admin_api).get_backup_schedule(request)
        print(f"Backup schedule: {response}")
    
    

## List backup schedules

### Console

  1. In the Google Cloud console, go to the Spanner **Instances** page.



[Go to the Spanner Instances page](https://console.cloud.google.com/spanner/instances)

  1. Click the instance containing the database.

  2. Click the database.

  3. In the navigation menu, click the **Backup/Restore**.

  4. Click the **Schedules** tab to view all the backup schedules and their information.




###  gcloud 

Before using any of the command data below, make the following replacements: 

  * PROJECT_ID: the project ID.
  * INSTANCE_ID: the instance ID.
  * DATABASE_ID: the database ID.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backup-schedules list \
      --project=PROJECT_ID \
      --instance=INSTANCE_ID \
      --database=DATABASE_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backup-schedules list `
      --project=PROJECT_ID `
      --instance=INSTANCE_ID `
      --database=DATABASE_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backup-schedules list ^
      --project=PROJECT_ID ^
      --instance=INSTANCE_ID ^
      --database=DATABASE_ID

You should receive a response similar to the following:
    
    
    

Name | Backup type | Cron | Retention duration | Encryption type  
---|---|---|---|---  
my-full-schedule | FULL | 30 12 * * * | 2592000s | USE_DATABASE_ENCRYPTION  
my-incr-schedule | INCREMENTAL | 0 */4 * * * | 2592000s | USE_DATABASE_ENCRYPTION  
  
### REST v1

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID.
  * INSTANCE_ID: the instance ID.
  * DATABASE_ID: the database ID.



HTTP method and URL: 
    
    
    GET https://spanner.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID/backupSchedules

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://spanner.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID/backupSchedules"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://spanner.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID/backupSchedules" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "backupSchedules": [
        {
          "name": "projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID/backupSchedules/SCHEDULE_ID",
          "retentionDuration": "172800s",
          "encryptionConfig": {
            "encryptionType": "USE_DATABASE_ENCRYPTION"
          },
          "spec": {
            "cronSpec": {
              "text": "0 */12 * * *",
              "timeZone": "UTC",
              "creationWindow": "14400s"
            }
          },
          "fullBackupSpec": {},
          "updateTime": "2024-09-09T07:21:43.946180Z"
        },
        {
          "name": "projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID/backupSchedules/SCHEDULE_ID",
          "retentionDuration": "2592000s",
          "encryptionConfig": {
            "encryptionType": "CUSTOMER_MANAGED_ENCRYPTION",
            "kmsKeyName": "projects/PROJECT_ID/locations/us-central1/keyRings/cmek-demo/cryptoKeys/test-key"
          },
          "spec": {
            "cronSpec": {
              "text": "30 12 * * *",
              "timeZone": "UTC",
              "creationWindow": "14400s"
            }
          },
          "fullBackupSpec": {},
          "updateTime": "2024-09-17T18:27:53.868741Z"
        }
      ]
    }
    

### Client libraries

### C#
    
    
    using [Google.Cloud.Spanner.Admin.Database.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.html);
    using [Google.Cloud.Spanner.Common.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.html);
    using System;
    using System.Collections.Generic;
    
    public class ListBackupSchedulesSample
    {
        public IEnumerable<BackupSchedule> ListBackupSchedules(string projectId, string instanceId, string databaseId)
        {
            [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html) client = [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_Create)();
    
            var backupSchedules = client.[ListBackupSchedules](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_ListBackupSchedules_Google_Cloud_Spanner_Admin_Database_V1_ListBackupSchedulesRequest_Google_Api_Gax_Grpc_CallSettings_)(
                new [ListBackupSchedulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.ListBackupSchedulesRequest.html)
                {
                    ParentAsDatabaseName = [DatabaseName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.DatabaseName.html).[FromProjectInstanceDatabase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.DatabaseName.html#Google_Cloud_Spanner_Common_V1_DatabaseName_FromProjectInstanceDatabase_System_String_System_String_System_String_)(projectId, instanceId, databaseId),
                });
    
            foreach ([BackupSchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupSchedule.html) backupSchedule in backupSchedules)
            {
                Console.WriteLine($"Backup schedule: {backupSchedule}");
            }
            return backupSchedules;
        }
    }

### C++
    
    
    void ListBackupSchedules(
        google::cloud::spanner_admin::DatabaseAdminClient client,
        std::string const& project_id, std::string const& instance_id,
        std::string const& database_id) {
      google::cloud::spanner::Database db(project_id, instance_id, database_id);
      google::spanner::admin::database::v1::ListBackupSchedulesRequest request;
      request.set_parent(db.FullName());
    
      int count = 0;
      for (auto& backup_schedule : client.ListBackupSchedules(request)) {
        if (!backup_schedule) throw std::move(backup_schedule).status();
    
        std::cout << "Backup Schedule [" << ++count << "]:\n"
                  << backup_schedule->DebugString();
      }
      if (count == 0) {
        std::cout << "No backup schedules found for database " << db.FullName();
      }
    }

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	database "cloud.google.com/go/spanner/admin/database/apiv1"
    	"cloud.google.com/go/spanner/admin/database/apiv1/databasepb"
    	"google.golang.org/api/iterator"
    )
    
    func listBackupSchedules(w io.Writer, dbName string) error {
    	ctx := context.Background()
    
    	client, err := database.NewDatabaseAdminClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/database/apiv1.html#cloud_google_com_go_spanner_admin_database_apiv1_DatabaseAdminClient_Close)()
    
    	req := databasepb.ListBackupSchedulesRequest{
    		Parent: dbName,
    	}
    	iter := client.ListBackupSchedules(ctx, &req)
    
    	for {
    		backupSchedule, err := iter.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return err
    		}
    		fmt.Fprintf(w, "Backup schedule: %s\n", backupSchedule)
    	}
    
    	return nil
    }
    

### Java
    
    
    import com.google.cloud.spanner.admin.database.v1.[DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html);
    import com.google.spanner.admin.database.v1.[BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupSchedule.html);
    import com.google.spanner.admin.database.v1.[DatabaseName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.DatabaseName.html);
    import java.io.IOException;
    
    class ListBackupSchedulesSample {
    
      static void listBackupSchedules() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project";
        String instanceId = "my-instance";
        String databaseId = "my-database";
        listBackupSchedules(projectId, instanceId, databaseId);
      }
    
      static void listBackupSchedules(String projectId, String instanceId, String databaseId)
          throws IOException {
        try ([DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html) databaseAdminClient = [DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html).create()) {
          [DatabaseName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.DatabaseName.html) databaseName = [DatabaseName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.DatabaseName.html).of(projectId, instanceId, databaseId);
    
          System.out.println(
              String.format("Backup schedules for database '%s'", databaseName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.DatabaseName.html#com_google_spanner_admin_database_v1_DatabaseName_toString__)()));
          for ([BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupSchedule.html) backupSchedule :
              databaseAdminClient.listBackupSchedules(databaseName).iterateAll()) {
            System.out.println(
                String.format(
                    "Backup schedule: %s\n%s", backupSchedule.getName(), backupSchedule.toString()));
          }
        }
      }
    }

### Node.js
    
    
    // Import the Google Cloud client library for Spanner.
    const {Spanner} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'my-project-id';
    // const instanceId = 'my-instance-id';
    // const databaseId = 'my-database-id';
    
    // Create a Spanner database admin client.
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({projectId});
    const client = spanner.[getDatabaseAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)();
    
    try {
      // List backup schedules of a database.
      const [schedules] = await [client](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/requestconfig.html).listBackupSchedules({
        parent: [client](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/requestconfig.html).databasePath(projectId, instanceId, databaseId),
      });
      schedules.forEach(schedule => {
        console.log('Backup schedule:', schedule);
      });
    } catch (err) {
      console.error('ERROR:', err);
    }

### PHP
    
    
    use Google\Cloud\Spanner\Admin\Database\V1\Client\DatabaseAdminClient;
    use Google\Cloud\Spanner\Admin\Database\V1\ListBackupSchedulesRequest;
    
    /**
     * Get list of all backup schedules for a given database.
     * Example:
     * ```
     * list_backup_schedules($projectId, $instanceId, $databaseId, $backupScheduleId);
     * ```
     *
     * @param string $projectId The Google Cloud project ID.
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     * at https://cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.backupSchedules#BackupSchedule.FIELDS
     */
    function list_backup_schedules(
        string $projectId,
        string $instanceId,
        string $databaseId,
    ): void {
        $databaseAdminClient = new DatabaseAdminClient();
        $databaseFullName = DatabaseAdminClient::databaseName($projectId, $instanceId, $databaseId);
    
        $request = new ListBackupSchedulesRequest([
            'parent' => $databaseFullName,
        ]);
        $backup_schedules = $databaseAdminClient->listBackupSchedules($request);
    
        printf('Backup schedules for database %s' . PHP_EOL, $databaseFullName);
        foreach ($backup_schedules as $schedule) {
            printf('Backup schedule: %s' . PHP_EOL, $schedule->getName());
        }
    }

### Python
    
    
    def list_backup_schedules(instance_id: str, database_id: str) -> None:
        from google.cloud import [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html)
        from google.cloud.spanner_admin_database_v1.types import (
            backup_schedule as backup_schedule_pb,
        )
    
        client = [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html).[Client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html)()
        database_admin_api = [client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.html).[database_admin_api](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html#google_cloud_spanner_v1_client_Client_database_admin_api)
    
        request = backup_schedule_pb.[ListBackupSchedulesRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListBackupSchedulesRequest.html)(
            parent=[database_admin_api](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html#google_cloud_spanner_v1_client_Client_database_admin_api).database_path(
                [client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.html).project,
                instance_id,
                database_id,
            ),
        )
    
        for backup_schedule in [database_admin_api](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html#google_cloud_spanner_v1_client_Client_database_admin_api).list_backup_schedules(request):
            print(f"Backup schedule: {backup_schedule}")
    
    

## Update a backup schedule

### Console

  1. In the Google Cloud console, go to the Spanner **Instances** page.



[Go to the Spanner Instances page](https://console.cloud.google.com/spanner/instances)

  1. Click the instance containing the database.

  2. Click the database.

  3. In the navigation menu, click the **Backup/Restore**.

  4. Click the **Schedules** tab.

  5. Select **More actions** for your backup schedule and click **Update**.

  6. You can update the frequency and retention time of the backup schedule. If it's a full backup schedule, you can also update the encryption type.

  7. Click **Save**.




###  gcloud 

Before using any of the command data below, make the following replacements: 

  * SCHEDULE_ID: the backup schedule ID.
  * PROJECT_ID: the project ID.
  * INSTANCE_ID: the ID of the instance where you want to modify the backup schedule. 
  * DATABASE_ID: the ID of the database where you want to modify the backup schedule. 
  * RETENTION_DURATION: the retention duration of the backups created by the schedule. 
  * CRONTAB_EXPRESSION: the crontab expression for the backup schedule frequency. For example, if you want the backup schedule frequency to be every 12 hours, you can use `0 12 * * *`. 
  * ENCRYPTION_TYPE: the encryption type of backups created by the backup schedule. Valid values are `USE_DATABASE_ENCRYPTION`, `GOOGLE_DEFAULT_ENCRYPTION` , or `CUSTOMER_MANAGED_ENCRYPTION`. If you use `CUSTOMER_MANAGED_ENCRYPTION`, you must specify a `kmsKeyName` or `kmsKeyNames`. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backup-schedules update SCHEDULE_ID \
      --project=PROJECT_ID \
      --instance=INSTANCE_ID \
      --database=DATABASE_ID \
      --retention-duration=RETENTION_DURATION \
      --cron="CRONTAB_EXPRESSION" \
      --encryption-type=ENCRYPTION_TYPE

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backup-schedules update SCHEDULE_ID `
      --project=PROJECT_ID `
      --instance=INSTANCE_ID `
      --database=DATABASE_ID `
      --retention-duration=RETENTION_DURATION `
      --cron="CRONTAB_EXPRESSION" `
      --encryption-type=ENCRYPTION_TYPE

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backup-schedules update SCHEDULE_ID ^
      --project=PROJECT_ID ^
      --instance=INSTANCE_ID ^
      --database=DATABASE_ID ^
      --retention-duration=RETENTION_DURATION ^
      --cron="CRONTAB_EXPRESSION" ^
      --encryption-type=ENCRYPTION_TYPE

### REST v1

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID.
  * INSTANCE_ID: the ID of the instance where you want to modify the backup schedule. 
  * DATABASE_ID: the ID of the database where you want to modify the backup schedule. 
  * SCHEDULE_ID: the backup schedule ID.
  * RETENTION_DURATION: the retention duration of the backups created by the schedule. For example, if you want the retention duration to be one day, specify `86400s`. 
  * ENCRYPTION_TYPE: the encryption type of backups created by the backup schedule. Possible values are `USE_DATABASE_ENCRYPTION`, `GOOGLE_DEFAULT_ENCRYPTION` , or `CUSTOMER_MANAGED_ENCRYPTION`. If you use `CUSTOMER_MANAGED_ENCRYPTION`, you must specify a `kmsKeyName` or `kmsKeyNames`. 



HTTP method and URL: 
    
    
    PATCH https://spanner.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID/backupSchedules/SCHEDULE_ID?updateMask=retention_duration,encryption_config,spec.cron_spec.text

Request JSON body: 
    
    
    {
      "retentionDuration": "RETENTION_DURATION",
      "spec": {
        "cronSpec": {
          "text": "0 2 * * *"
        }
        "encryptionConfig": {
          "encryptionType": "ENCRYPTION_TYPE"
        },
      },
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://spanner.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID/backupSchedules/SCHEDULE_ID?updateMask=retention_duration,encryption_config,spec.cron_spec.text"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://spanner.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID/backupSchedules/SCHEDULE_ID?updateMask=retention_duration,encryption_config,spec.cron_spec.text" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
      {
        "name": "projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID/backupSchedules/SCHEDULE_ID",
        "retentionDuration": "86400s",
        "encryptionConfig": {
          "encryptionType": "USE_DATABASE_ENCRYPTION"
        },
        "spec": {
          "cronSpec": {
            "text": "0 2 * * *",
            "timeZone": "UTC",
            "creationWindow": "14400s"
          }
        },
        "fullBackupSpec": {},
        "updateTime": "2024-05-22T11:13:51.835590Z"
      }
    

### Client libraries

### C#
    
    
    using [Google.Cloud.Spanner.Admin.Database.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    
    public class UpdateBackupScheduleSample
    {
        public BackupSchedule UpdateBackupSchedule(string projectId, string instanceId, string databaseId, string scheduleId)
        {
            [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html) client = [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_Create)();
    
            [BackupSchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupSchedule.html) response = client.[UpdateBackupSchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_UpdateBackupSchedule_Google_Cloud_Spanner_Admin_Database_V1_BackupSchedule_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)(
                new [UpdateBackupScheduleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.UpdateBackupScheduleRequest.html)
                {
                    BackupSchedule = new [BackupSchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupSchedule.html)
                    {
                        BackupScheduleName = [BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupScheduleName.html).[FromProjectInstanceDatabaseSchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupScheduleName.html#Google_Cloud_Spanner_Admin_Database_V1_BackupScheduleName_FromProjectInstanceDatabaseSchedule_System_String_System_String_System_String_System_String_)(projectId, instanceId, databaseId, scheduleId),
                        Spec = new [BackupScheduleSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupScheduleSpec.html)
                        {
                            CronSpec = new [CrontabSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CrontabSpec.html)
                            {
                                Text = "45 15 * * *",
                            },
                        },
                        RetentionDuration = new [Duration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)
                        {
                            Seconds = 172800,
                        },
                        EncryptionConfig = new [CreateBackupEncryptionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupEncryptionConfig.html)
                        {
                            EncryptionType = [CreateBackupEncryptionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupEncryptionConfig.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupEncryptionConfig.Types.html).[EncryptionType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupEncryptionConfig.Types.EncryptionType.html).[UseDatabaseEncryption](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupEncryptionConfig.Types.EncryptionType.html#Google_Cloud_Spanner_Admin_Database_V1_CreateBackupEncryptionConfig_Types_EncryptionType_UseDatabaseEncryption),
                        },
                    },
                    UpdateMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)
                    {
                        Paths = { "spec.cron_spec.text", "retention_duration", "encryption_config" },
                    },
                });
    
            Console.WriteLine($"Updated backup schedule: {response}");
            return response;
        }
    }

### C++
    
    
    void UpdateBackupSchedule(
        google::cloud::spanner_admin::DatabaseAdminClient client,
        std::string const& project_id, std::string const& instance_id,
        std::string const& database_id, std::string const& backup_schedule_id) {
      google::cloud::spanner::Database db(project_id, instance_id, database_id);
      std::string backup_schedule_name =
          db.FullName() + "/backupSchedules/" + backup_schedule_id;
    
      google::spanner::admin::database::v1::BackupSchedule backup_schedule;
      backup_schedule.set_name(backup_schedule_name);
      backup_schedule.mutable_spec()->mutable_cron_spec()->set_text("45 15 * * *");
      backup_schedule.mutable_retention_duration()->set_seconds(3600 * 48);
    
      google::spanner::admin::database::v1::CreateBackupEncryptionConfig
          encryption_config;
      encryption_config.set_encryption_type(
          google::spanner::admin::database::v1::CreateBackupEncryptionConfig::
              USE_DATABASE_ENCRYPTION);
      *backup_schedule.mutable_encryption_config() = std::move(encryption_config);
    
      google::protobuf::FieldMask update_mask;
      update_mask.add_paths("spec.cron_spec.text");
      update_mask.add_paths("retention_duration");
      update_mask.add_paths("encryption_config");
    
      google::spanner::admin::database::v1::UpdateBackupScheduleRequest request;
      *request.mutable_backup_schedule() = std::move(backup_schedule);
      *request.mutable_update_mask() = std::move(update_mask);
    
      auto updated_backup_schedule = client.UpdateBackupSchedule(request);
      if (!updated_backup_schedule) {
        throw std::move(updated_backup_schedule).status();
      }
      std::cout << "Backup schedule " << updated_backup_schedule->name()
                << " updated at "
                << *google::cloud::spanner::MakeTimestamp(
                       updated_backup_schedule->update_time());
    }

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	database "cloud.google.com/go/spanner/admin/database/apiv1"
    	"cloud.google.com/go/spanner/admin/database/apiv1/databasepb"
    	"google.golang.org/protobuf/types/known/durationpb"
    	"google.golang.org/protobuf/types/known/fieldmaskpb"
    )
    
    func updateBackupSchedule(w io.Writer, dbName string, scheduleId string) error {
    	ctx := context.Background()
    
    	client, err := database.NewDatabaseAdminClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/database/apiv1.html#cloud_google_com_go_spanner_admin_database_apiv1_DatabaseAdminClient_Close)()
    
    	// Update a schedule to create backups daily at 3:45 PM, using the database's
    	// encryption config, and retained for 48 hours.
    	req := databasepb.UpdateBackupScheduleRequest{
    		BackupSchedule: &databasepb.BackupSchedule{
    			Name: fmt.Sprintf("%s/backupSchedules/%s", dbName, scheduleId),
    			Spec: &databasepb.BackupScheduleSpec{
    				ScheduleSpec: &databasepb.BackupScheduleSpec_CronSpec{
    					CronSpec: &databasepb.CrontabSpec{
    						Text: "45 15 * * *",
    					},
    				},
    			},
    			RetentionDuration: durationpb.New(48 * time.Hour),
    			EncryptionConfig: &databasepb.CreateBackupEncryptionConfig{
    				EncryptionType: databasepb.[CreateBackupEncryptionConfig_USE_DATABASE_ENCRYPTION](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/database/apiv1/databasepb.html#cloud_google_com_go_spanner_admin_database_apiv1_databasepb_CreateBackupEncryptionConfig_ENCRYPTION_TYPE_UNSPECIFIED_CreateBackupEncryptionConfig_USE_DATABASE_ENCRYPTION_CreateBackupEncryptionConfig_GOOGLE_DEFAULT_ENCRYPTION_CreateBackupEncryptionConfig_CUSTOMER_MANAGED_ENCRYPTION),
    			},
    		},
    		UpdateMask: &fieldmaskpb.FieldMask{
    			Paths: []string{
    				"spec.cron_spec.text",
    				"retention_duration",
    				"encryption_config",
    			},
    		},
    	}
    
    	res, err := client.UpdateBackupSchedule(ctx, &req)
    	if err != nil {
    		return err
    	}
    
    	fmt.Fprintf(w, "Updated backup schedule: %s", res)
    	return nil
    }
    

### Java
    
    
    import com.google.cloud.spanner.admin.database.v1.[DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import com.google.spanner.admin.database.v1.[BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupSchedule.html);
    import com.google.spanner.admin.database.v1.[BackupScheduleName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupScheduleName.html);
    import com.google.spanner.admin.database.v1.[BackupScheduleSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupScheduleSpec.html);
    import com.google.spanner.admin.database.v1.[CreateBackupEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateBackupEncryptionConfig.html);
    import com.google.spanner.admin.database.v1.[CrontabSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CrontabSpec.html);
    import com.google.spanner.admin.database.v1.[UpdateBackupScheduleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.UpdateBackupScheduleRequest.html);
    import java.io.IOException;
    
    class UpdateBackupScheduleSample {
    
      static void updateBackupSchedule() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project";
        String instanceId = "my-instance";
        String databaseId = "my-database";
        String backupScheduleId = "my-backup-schedule";
        updateBackupSchedule(projectId, instanceId, databaseId, backupScheduleId);
      }
    
      static void updateBackupSchedule(
          String projectId, String instanceId, String databaseId, String backupScheduleId)
          throws IOException {
        [BackupScheduleName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupScheduleName.html) backupScheduleName =
            [BackupScheduleName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupScheduleName.html).of(projectId, instanceId, databaseId, backupScheduleId);
        final [CreateBackupEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateBackupEncryptionConfig.html) encryptionConfig =
            [CreateBackupEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateBackupEncryptionConfig.html).newBuilder()
                .setEncryptionType([CreateBackupEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateBackupEncryptionConfig.html).EncryptionType.USE_DATABASE_ENCRYPTION)
                .build();
        final [BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupSchedule.html) backupSchedule =
            [BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupSchedule.html).newBuilder()
                .setName(backupScheduleName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupScheduleName.html#com_google_spanner_admin_database_v1_BackupScheduleName_toString__)())
                .[setRetentionDuration](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupSchedule.Builder.html#com_google_spanner_admin_database_v1_BackupSchedule_Builder_setRetentionDuration_com_google_protobuf_Duration_)([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(3600 * 48))
                .[setSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupSchedule.Builder.html#com_google_spanner_admin_database_v1_BackupSchedule_Builder_setSpec_com_google_spanner_admin_database_v1_BackupScheduleSpec_)(
                    [BackupScheduleSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupScheduleSpec.html).newBuilder()
                        .[setCronSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupScheduleSpec.Builder.html#com_google_spanner_admin_database_v1_BackupScheduleSpec_Builder_setCronSpec_com_google_spanner_admin_database_v1_CrontabSpec_)([CrontabSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CrontabSpec.html).newBuilder().[setText](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CrontabSpec.Builder.html#com_google_spanner_admin_database_v1_CrontabSpec_Builder_setText_java_lang_String_)("45 15 * * *").build())
                        .build())
                .setEncryptionConfig(encryptionConfig)
                .build();
    
        try ([DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html) databaseAdminClient = [DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html).create()) {
          final [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) fieldMask =
              [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder()
                  .[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("retention_duration")
                  .[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("spec.cron_spec.text")
                  .[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("encryption_config")
                  .build();
          final [BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupSchedule.html) updatedBackupSchedule =
              databaseAdminClient.updateBackupSchedule(
                  [UpdateBackupScheduleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.UpdateBackupScheduleRequest.html).newBuilder()
                      .setBackupSchedule(backupSchedule)
                      .setUpdateMask(fieldMask)
                      .build());
          System.out.println(
              String.format(
                  "Updated backup schedule: %s\n%s",
                  updatedBackupSchedule.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupSchedule.html#com_google_spanner_admin_database_v1_BackupSchedule_getName__)(), updatedBackupSchedule.toString()));
        }
      }
    }

### Node.js
    
    
    // Import the Google Cloud client library for Spanner.
    const {Spanner} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'my-project-id';
    // const instanceId = 'my-instance-id';
    // const databaseId = 'my-database-id';
    // const scheduleId = 'my-schedule-id';
    
    // Create a Spanner database admin client.
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({projectId});
    const client = spanner.[getDatabaseAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)();
    
    try {
      // Update the schedule to create backups daily at 3:45 PM, using the
      // database's encryption config, and retained for 48 hours.
      const [response] = await [client](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/requestconfig.html).updateBackupSchedule({
        backupSchedule: {
          name: [client](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/requestconfig.html).backupSchedulePath(
            projectId,
            instanceId,
            databaseId,
            scheduleId,
          ),
          spec: {
            cronSpec: {
              text: '45 15 * * *',
            },
          },
          retentionDuration: {
            seconds: 172800,
          },
          encryptionConfig: {
            encryptionType: 'USE_DATABASE_ENCRYPTION',
          },
        },
        updateMask: {
          paths: [
            'spec.cron_spec.text',
            'retention_duration',
            'encryption_config',
          ],
        },
      });
      console.log('Updated backup schedule:', response);
    } catch (err) {
      console.error('ERROR:', err);
    }

### PHP
    
    
    use Google\Cloud\Spanner\Admin\Database\V1\Client\DatabaseAdminClient;
    use Google\Cloud\Spanner\Admin\Database\V1\UpdateBackupScheduleRequest;
    use Google\Cloud\Spanner\Admin\Database\V1\CreateBackupEncryptionConfig;
    use Google\Cloud\Spanner\Admin\Database\V1\CreateBackupEncryptionConfig\EncryptionType;
    use Google\Cloud\Spanner\Admin\Database\V1\BackupSchedule;
    use Google\Cloud\Spanner\Admin\Database\V1\FullBackupSpec;
    use Google\Cloud\Spanner\Admin\Database\V1\BackupScheduleSpec;
    use Google\Cloud\Spanner\Admin\Database\V1\CrontabSpec;
    use Google\Protobuf\Duration;
    use Google\Protobuf\FieldMask;
    
    /**
     * Update an existing backup schedule.
     * Example:
     * ```
     * update_backup_schedule($projectId, $instanceId, $databaseId, $backupScheduleId);
     * ```
     *
     * @param string $projectId The Google Cloud project ID.
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     * @param string $backupScheduleId The ID of the backup schedule to be created.
     * at https://cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.backupSchedules#BackupSchedule.FIELDS
     */
    function update_backup_schedule(
        string $projectId,
        string $instanceId,
        string $databaseId,
        string $backupScheduleId,
    ): void {
        $databaseAdminClient = new DatabaseAdminClient();
    
        $encryptionConfig = new CreateBackupEncryptionConfig([
            'encryption_type' => EncryptionType::USE_DATABASE_ENCRYPTION,
        ]);
        $backupScheduleName = sprintf(
            'projects/%s/instances/%s/databases/%s/backupSchedules/%s',
            $projectId,
            $instanceId,
            $databaseId,
            $backupScheduleId
        );
        $backupSchedule = new BackupSchedule([
            'name' => $backupScheduleName,
            'full_backup_spec' => new FullBackupSpec(),
            'retention_duration' => (new Duration())
                ->setSeconds(48 * 60 * 60),
            'spec' => new BackupScheduleSpec([
                'cron_spec' => new CrontabSpec([
                    'text' => '45 15 * * *'
                ]),
            ]),
            'encryption_config' => $encryptionConfig,
        ]);
        $fieldMask = (new FieldMask())
            ->setPaths([
                'retention_duration',
                'spec.cron_spec.text',
                'encryption_config',
            ]);
    
        $request = new UpdateBackupScheduleRequest([
            'backup_schedule' => $backupSchedule,
            'update_mask' => $fieldMask,
        ]);
    
        $updated_backup_schedule = $databaseAdminClient->updateBackupSchedule($request);
    
        printf('Updated backup scehedule %s' . PHP_EOL, $updated_backup_schedule->getName());
    }

### Python
    
    
    def update_backup_schedule(
        instance_id: str,
        database_id: str,
        schedule_id: str,
    ) -> None:
        from datetime import timedelta
        from google.cloud import [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html)
        from google.cloud.spanner_admin_database_v1.types import (
            backup_schedule as backup_schedule_pb,
        )
        from google.cloud.spanner_admin_database_v1.types import (
            [CreateBackupEncryptionConfig](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CreateBackupEncryptionConfig.html),
        )
        from google.protobuf.field_mask_pb2 import FieldMask
    
        client = [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html).[Client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html)()
        database_admin_api = [client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.html).[database_admin_api](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html#google_cloud_spanner_v1_client_Client_database_admin_api)
    
        request = backup_schedule_pb.[UpdateBackupScheduleRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.UpdateBackupScheduleRequest.html)(
            backup_schedule=backup_schedule_pb.[BackupSchedule](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.BackupSchedule.html)(
                name=[database_admin_api](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html#google_cloud_spanner_v1_client_Client_database_admin_api).backup_schedule_path(
                    [client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.html).project,
                    instance_id,
                    database_id,
                    schedule_id,
                ),
                spec=backup_schedule_pb.[BackupScheduleSpec](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.BackupScheduleSpec.html)(
                    cron_spec=backup_schedule_pb.[CrontabSpec](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CrontabSpec.html)(
                        text="45 15 * * *",
                    ),
                ),
                retention_duration=timedelta(hours=48),
                encryption_config=CreateBackupEncryptionConfig(
                    encryption_type=[CreateBackupEncryptionConfig](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CreateBackupEncryptionConfig.html).EncryptionType.USE_DATABASE_ENCRYPTION,
                ),
            ),
            update_mask=FieldMask(
                paths=[
                    "spec.cron_spec.text",
                    "retention_duration",
                    "encryption_config",
                ],
            ),
        )
    
        response = [database_admin_api](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html#google_cloud_spanner_v1_client_Client_database_admin_api).update_backup_schedule(request)
        print(f"Updated backup schedule: {response}")
    
    

## Delete a backup schedule

### Console

  1. In the Google Cloud console, go to the Spanner **Instances** page.



[Go to the Spanner Instances page](https://console.cloud.google.com/spanner/instances)

  1. Click the instance containing the database.

  2. Click the database.

  3. In the navigation menu, click the **Backup/Restore**.

  4. Select **More actions** for your backup schedule and click **Delete**.

  5. Type the backup schedule name.

  6. Click **Confirm**.




###  gcloud 

Before using any of the command data below, make the following replacements: 

  * SCHEDULE_ID: the backup schedule ID.
  * PROJECT_ID: the project ID.
  * INSTANCE_ID: the ID of the instance where you want to delete the backup schedule. 
  * DATABASE_ID: the ID of the database where you want to delete the backup schedule. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backup-schedules delete SCHEDULE_ID \
      --project=PROJECT_ID \
      --instance=INSTANCE_ID \
      --database=DATABASE_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backup-schedules delete SCHEDULE_ID `
      --project=PROJECT_ID `
      --instance=INSTANCE_ID `
      --database=DATABASE_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backup-schedules delete SCHEDULE_ID ^
      --project=PROJECT_ID ^
      --instance=INSTANCE_ID ^
      --database=DATABASE_ID

### REST v1

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID.
  * INSTANCE_ID: the ID of the instance where you want to delete the backup schedule. 
  * DATABASE_ID: the ID of the database where you want to delete the backup schedule. 
  * SCHEDULE_ID: the backup schedule ID. 



HTTP method and URL: 
    
    
    DELETE https://spanner.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID/backupSchedules/SCHEDULE_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://spanner.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID/backupSchedules/SCHEDULE_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://spanner.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID/backupSchedules/SCHEDULE_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### Client libraries

### C#
    
    
    using [Google.Cloud.Spanner.Admin.Database.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.html);
    using System;
    
    public class DeleteBackupScheduleSample
    {
        public void DeleteBackupSchedule(string projectId, string instanceId, string databaseId, string scheduleId)
        {
            [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html) client = [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_Create)();
    
            client.[DeleteBackupSchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_DeleteBackupSchedule_Google_Cloud_Spanner_Admin_Database_V1_BackupScheduleName_Google_Api_Gax_Grpc_CallSettings_)([BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupScheduleName.html).[FromProjectInstanceDatabaseSchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupScheduleName.html#Google_Cloud_Spanner_Admin_Database_V1_BackupScheduleName_FromProjectInstanceDatabaseSchedule_System_String_System_String_System_String_System_String_)(projectId, instanceId, databaseId, scheduleId));
    
            Console.WriteLine("Deleted backup schedule");
        }
    }

### C++
    
    
    void DeleteBackupSchedule(
        google::cloud::spanner_admin::DatabaseAdminClient client,
        std::string const& project_id, std::string const& instance_id,
        std::string const& database_id, std::string const& backup_schedule_id) {
      google::cloud::spanner::Database db(project_id, instance_id, database_id);
      std::string backup_schedule_name =
          db.FullName() + "/backupSchedules/" + backup_schedule_id;
    
      google::spanner::admin::database::v1::DeleteBackupScheduleRequest request;
      request.set_name(backup_schedule_name);
    
      auto status = client.DeleteBackupSchedule(request);
      if (!status.ok()) throw std::move(status);
      std::cout << "Backup schedule " << backup_schedule_name << " deleted";
    }

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	database "cloud.google.com/go/spanner/admin/database/apiv1"
    	"cloud.google.com/go/spanner/admin/database/apiv1/databasepb"
    )
    
    func deleteBackupSchedule(w io.Writer, dbName string, scheduleId string) error {
    	ctx := context.Background()
    
    	client, err := database.NewDatabaseAdminClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/database/apiv1.html#cloud_google_com_go_spanner_admin_database_apiv1_DatabaseAdminClient_Close)()
    
    	req := databasepb.DeleteBackupScheduleRequest{
    		Name: fmt.Sprintf("%s/backupSchedules/%s", dbName, scheduleId),
    	}
    
    	err = client.DeleteBackupSchedule(ctx, &req)
    	if err != nil {
    		return err
    	}
    
    	fmt.Fprintf(w, "Deleted backup schedule")
    	return nil
    }
    

### Java
    
    
    import com.google.cloud.spanner.admin.database.v1.[DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html);
    import com.google.spanner.admin.database.v1.[BackupScheduleName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupScheduleName.html);
    import com.google.spanner.admin.database.v1.[DeleteBackupScheduleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.DeleteBackupScheduleRequest.html);
    import java.io.IOException;
    
    class DeleteBackupScheduleSample {
    
      static void deleteBackupSchedule() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project";
        String instanceId = "my-instance";
        String databaseId = "my-database";
        String backupScheduleId = "my-backup-schedule";
        deleteBackupSchedule(projectId, instanceId, databaseId, backupScheduleId);
      }
    
      static void deleteBackupSchedule(
          String projectId, String instanceId, String databaseId, String backupScheduleId)
          throws IOException {
        try ([DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html) databaseAdminClient = [DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html).create()) {
          [BackupScheduleName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupScheduleName.html) backupScheduleName =
              [BackupScheduleName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupScheduleName.html).of(projectId, instanceId, databaseId, backupScheduleId);
          databaseAdminClient.deleteBackupSchedule(
              [DeleteBackupScheduleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.DeleteBackupScheduleRequest.html).newBuilder().setName(backupScheduleName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupScheduleName.html#com_google_spanner_admin_database_v1_BackupScheduleName_toString__)()).build());
          System.out.println(
              String.format("Deleted backup schedule: %s", backupScheduleName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupScheduleName.html#com_google_spanner_admin_database_v1_BackupScheduleName_toString__)()));
        }
      }
    }

### Node.js
    
    
    // Import the Google Cloud client library for Spanner.
    const {Spanner} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'my-project-id';
    // const instanceId = 'my-instance-id';
    // const databaseId = 'my-database-id';
    // const scheduleId = 'my-schedule-id';
    
    // Create a Spanner database admin client.
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({projectId});
    const client = spanner.[getDatabaseAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)();
    
    try {
      // Delete the backup schedule.
      await [client](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/requestconfig.html).deleteBackupSchedule({
        name: [client](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/requestconfig.html).backupSchedulePath(
          projectId,
          instanceId,
          databaseId,
          scheduleId,
        ),
      });
      console.log('Deleted backup schedule');
    } catch (err) {
      console.error('ERROR:', err);
    }

### PHP
    
    
    use Google\Cloud\Spanner\Admin\Database\V1\Client\DatabaseAdminClient;
    use Google\Cloud\Spanner\Admin\Database\V1\DeleteBackupScheduleRequest;
    
    /**
     * Delete a backup schedule.
     * Example:
     * ```
     * delete_backup_schedule($projectId, $instanceId, $databaseId, $backupScheduleId);
     * ```
     *
     * @param string $projectId The Google Cloud project ID.
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     * @param string $backupScheduleId The ID of the backup schedule to be created.
     * at https://cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.backupSchedules#BackupSchedule.FIELDS
     */
    function delete_backup_schedule(
        string $projectId,
        string $instanceId,
        string $databaseId,
        string $backupScheduleId,
    ): void {
        $databaseAdminClient = new DatabaseAdminClient();
    
        $backupScheduleName = sprintf(
            'projects/%s/instances/%s/databases/%s/backupSchedules/%s',
            $projectId,
            $instanceId,
            $databaseId,
            $backupScheduleId
        );
        $request = new DeleteBackupScheduleRequest([
            'name' => strval($backupScheduleName),
        ]);
    
        $databaseAdminClient->deleteBackupSchedule($request);
        printf('Deleted backup scehedule %s' . PHP_EOL, $backupScheduleName);
    }

### Python
    
    
    def delete_backup_schedule(
        instance_id: str,
        database_id: str,
        schedule_id: str,
    ) -> None:
        from google.cloud import [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html)
        from google.cloud.spanner_admin_database_v1.types import (
            backup_schedule as backup_schedule_pb,
        )
    
        client = [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html).[Client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html)()
        database_admin_api = [client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.html).[database_admin_api](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html#google_cloud_spanner_v1_client_Client_database_admin_api)
    
        request = backup_schedule_pb.[DeleteBackupScheduleRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.DeleteBackupScheduleRequest.html)(
            name=[database_admin_api](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html#google_cloud_spanner_v1_client_Client_database_admin_api).backup_schedule_path(
                [client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.html).project,
                instance_id,
                database_id,
                schedule_id,
            ),
        )
    
        [database_admin_api](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html#google_cloud_spanner_v1_client_Client_database_admin_api).delete_backup_schedule(request)
        print("Deleted backup schedule")
    
    

## Set IAM access control policy

You can set an Identity and Access Management (IAM) access policy to specify who has access to the backup schedule.

###  gcloud 

Before using any of the command data below, make the following replacements: 

  * SCHEDULE_ID: the backup schedule ID.
  * PROJECT_ID: the project ID.
  * INSTANCE_ID: the instance ID.
  * DATABASE_ID: the database ID.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backup-schedules set-iam-policy SCHEDULE_ID \
      --project=PROJECT_ID \
      --instance=INSTANCE_ID \
      --database=DATABASE_ID \
      policy.json

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backup-schedules set-iam-policy SCHEDULE_ID `
      --project=PROJECT_ID `
      --instance=INSTANCE_ID `
      --database=DATABASE_ID `
      policy.json

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backup-schedules set-iam-policy SCHEDULE_ID ^
      --project=PROJECT_ID ^
      --instance=INSTANCE_ID ^
      --database=DATABASE_ID ^
      policy.json

You should receive a response similar to the following:
    
    
    Updated IAM policy for backupSchedule [SCHEDULE_ID].
    bindings:
    - members:
      - user:test@google.com
      role: roles/editor
    etag: BwYi82k-fho=
    version: 1
    

The following is an example `policy.json` file that you can use along with this Google Cloud CLI command: 
    
    
    {
    "version": 1,
    "etag": "BwYi8ypICC0=",
    "bindings": [
      {
        "role": "roles/editor",
        "members": [
          "user:test@gmail.com"
        ]
      }
    ]
    }
    

### REST v1

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID.
  * INSTANCE_ID: the instance ID.
  * DATABASE_ID: the database ID.
  * SCHEDULE_ID: the backup schedule ID.



HTTP method and URL: 
    
    
    POST https://spanner.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID/backupSchedules/SCHEDULE_ID:setIamPolicy?alt=json

Request JSON body: 
    
    
    {
      "policy": {
        "version": 1,
        "etag": "BwYi8ypICC0=",
        "bindings": [
          {
            "role": "roles/editor",
            "members": [
              "user:test@gmail.com"
            ]
          }
        ]
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://spanner.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID/backupSchedules/SCHEDULE_ID:setIamPolicy?alt=json"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://spanner.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID/backupSchedules/SCHEDULE_ID:setIamPolicy?alt=json" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      {
        "version": 1,
        "etag": "etag",
        "bindings": [
          {
            "role": "roles/non-primitive",
            "members": [
              "user:test@gmail.com"
            ]
          }
        ]
      }
    }
    

## Get IAM access control policy

###  gcloud 

Before using any of the command data below, make the following replacements: 

  * SCHEDULE_ID: the backup schedule ID.
  * PROJECT_ID: the project ID.
  * INSTANCE_ID: the instance ID.
  * DATABASE_ID: the database ID.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backup-schedules get-iam-policy SCHEDULE_ID \
      --project=PROJECT_ID \
      --instance=INSTANCE_ID \
      --database=DATABASE_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backup-schedules get-iam-policy SCHEDULE_ID `
      --project=PROJECT_ID `
      --instance=INSTANCE_ID `
      --database=DATABASE_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backup-schedules get-iam-policy SCHEDULE_ID ^
      --project=PROJECT_ID ^
      --instance=INSTANCE_ID ^
      --database=DATABASE_ID

You should receive a response similar to the following:
    
    
    bindings:
    - members:
      - user:test@gmail.com
      role: roles/editor
    etag: BwYi82k-fho=
    version: 1
    

### REST v1

Before using any of the request data, make the following replacements: 

  * INSTANCE_ID: the instance ID.
  * DATABASE_ID: the database ID.
  * SCHEDULE_ID: the backup schedule ID.
  * PROJECT_ID: the project ID.



HTTP method and URL: 
    
    
    POST https://spanner.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID/backupSchedules/SCHEDULE_ID:getIamPolicy?alt=json

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://spanner.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID/backupSchedules/SCHEDULE_ID:getIamPolicy?alt=json"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://spanner.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID/backupSchedules/SCHEDULE_ID:getIamPolicy?alt=json" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      {
        "version": 1,
        "etag": "BwYbyZ9pc4o=",
        "bindings": [
          {
            "role": "roles/editor",
            "members": [
              "user:test@gmail.com"
            ]
          }
        ]
      }
    }
    

## What's next

  * [Backups overview](https://docs.cloud.google.com/spanner/docs/backup)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
