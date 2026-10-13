---
url: https://docs.cloud.google.com/spanner/docs/backup/create-backups/
title: Create backups \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:32:41.527300+00:00
---

# Create backups  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/backup/create-backups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Create backups Stay organized with collections  Save and categorize content based on your preferences. 

This page offers information about how you can create backups of Spanner databases.

For more information about backups, see [Backups overview](https://docs.cloud.google.com/spanner/docs/backup). You can back up databases using the following ways:

  * Using the Google Cloud console.
  * Using the Google Cloud CLI.
  * Using the client libraries.
  * Using the [REST](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups) or [RPC](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.Backup) APIs.



## Before you begin

  * To get the permissions that you need to create backups, ask your administrator to grant you the following IAM roles on the instance: 

    * Create, view, update, and delete backups: [Cloud Spanner Backup Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupAdmin) (`roles/spanner.backupAdmin`) 
    * Create and view backups: [Cloud Spanner Backup Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupWriter) (`roles/spanner.backupWriter`) 

**Note:** [IAM basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) might also contain permissions to create backups. You shouldn't grant basic roles in a production environment, but you can grant them in a development or test environment. 
  * The gcloud CLI examples on this page make the following assumptions:

    * You have already set up [gcloud CLI](https://docs.cloud.google.com/sdk/docs) for use with Spanner. If you are new to using gcloud CLI with Spanner, see [Create and query a database using the gcloud CLI](https://docs.cloud.google.com/spanner/docs/getting-started/gcloud).
    * You have configured gcloud CLI with your project. For example:
          
          gcloud config set core/project PROJECT_ID




## Create a backup

When you create a backup, Spanner creates a [backup resource](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups) and a long-running [backup operation](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups.operations) to track the progress of the backup. The newly created backup resides in the same instance, region, and project as its source database.

You must specify the following information when creating a backup:

  * A source database ID.
  * A name for the backup resource.
  * An expiration date (up to 1 year from backup creation time).



Optionally, you can specify a [`versionTime`](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups) for the source database, which lets you back up your database to an earlier point in time. The `versionTime` field is typically used either to synchronize the backups of multiple databases or to recover data using [point-in-time recovery (PITR)](https://docs.cloud.google.com/spanner/docs/pitr). If `versionTime` is not specified, then it is set to the `createTime` of the backup.

You can also create backups on a specified frequency by using a backup schedule. For more information, see [Create and manage backup schedules](https://docs.cloud.google.com/spanner/docs/backup/create-manage-backup-schedules).

### Console

  1. In the Google Cloud console, go to the Spanner **Instances** page.

[Go to Instances](https://console.cloud.google.com/spanner/instances)

  2. Click the instance that contains the database that you want to back up.

  3. Click the database.

  4. In the navigation pane, click **Backup/Restore**.

  5. In the **Backups** tab, click **Create backup**.

  6. Fill out the form, and click **Create**.




To check the progress of a backup operation, see [Check the operation progress](https://docs.cloud.google.com/spanner/docs/backup/manage-backups#check-operation-progress).

###  gcloud 

Before using any of the command data below, make the following replacements: 

  * INSTANCE_ID: the Spanner instance ID.
  * DATABASE_ID: the Spanner database ID.
  * BACKUP_NAME: the Spanner backup name.
  * RETENTION_PERIOD: the retention period of the backup created. For example, if you want the retention duration to be one day, you can use `86400s`. 
  * ENCRYPTION_TYPE: the encryption type of backup created. Valid values are `USE_CONFIG_DEFAULT_OR_BACKUP_ENCRYPTION`, `GOOGLE_DEFAULT_ENCRYPTION` , or `CUSTOMER_MANAGED_ENCRYPTION`. If you use `CUSTOMER_MANAGED_ENCRYPTION`, you must specify a `kmsKeyName`. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backups create BACKUP_NAME \
    --instance=INSTANCE_ID \
    --database=DATABASE_ID \
    --retention-period=RETENTION_PERIOD \
    --encryption-type=ENCRYPTION_TYPE \
    --async

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backups create BACKUP_NAME `
    --instance=INSTANCE_ID `
    --database=DATABASE_ID `
    --retention-period=RETENTION_PERIOD `
    --encryption-type=ENCRYPTION_TYPE `
    --async

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner backups create BACKUP_NAME ^
    --instance=INSTANCE_ID ^
    --database=DATABASE_ID ^
    --retention-period=RETENTION_PERIOD ^
    --encryption-type=ENCRYPTION_TYPE ^
    --async

You should receive a response similar to the following:
    
    
    Create request issued for: BACKUP_NAME
    Check operation [projects/PROJECT_ID/instances/INSTANCE_ID/backups/BACKUP_NAME/operations/_auto_op_234567] for status.
    

Here are some usage notes:

  * To set the backup's expiration date, specify either the `--retention-period` or `--expiration-date` flag. For information on date syntax, see [`gcloud topic datetimes`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes).
  * The name of the backup must be unique in the instance.
  * The command returns immediately because of the `--async` flag. Without the flag, the command will wait for the backup operation to complete.
  * Specify the `--help` flag to get help for any command.



To check the progress of a backup operation, see [Check the operation progress](https://docs.cloud.google.com/spanner/docs/backup/manage-backups#check-operation-progress).

### Client libraries

The following code sample creates a backup at a specific [`version_time`](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups#Backup.FIELDS.version_time) and then waits for it to complete. Once complete, it verifies that the backup is ready and retrieves some information about it, such as its name, size, and create time.

### C++
    
    
    void CreateBackup(google::cloud::spanner_admin::DatabaseAdminClient client,
                      std::string const& project_id, std::string const& instance_id,
                      std::string const& database_id, std::string const& backup_id,
                      google::cloud::spanner::Timestamp expire_time,
                      google::cloud::spanner::Timestamp version_time) {
      google::cloud::spanner::Database database(project_id, instance_id,
                                                database_id);
      google::spanner::admin::database::v1::CreateBackupRequest request;
      request.set_parent(database.instance().FullName());
      request.set_backup_id(backup_id);
      request.mutable_backup()->set_database(database.FullName());
      *request.mutable_backup()->mutable_expire_time() =
          expire_time.get<google::protobuf::Timestamp>().value();
      *request.mutable_backup()->mutable_version_time() =
          version_time.get<google::protobuf::Timestamp>().value();
      auto backup = client.CreateBackup(request).get();
      if (!backup) throw std::move(backup).status();
      std::cout
          << "Backup " << backup->name() << " of " << backup->database()
          << " of size " << backup->size_bytes() << " bytes as of "
          << google::cloud::spanner::MakeTimestamp(backup->version_time()).value()
          << " was created at "
          << google::cloud::spanner::MakeTimestamp(backup->create_time()).value()
          << ".\n";
    }

### C#
    
    
    using [Google.Cloud.Spanner.Admin.Database.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.html);
    using [Google.Cloud.Spanner.Common.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    
    public class CreateBackupSample
    {
        public Backup CreateBackup(string projectId, string instanceId, string databaseId, string backupId, DateTime versionTime)
        {
            // Create the DatabaseAdminClient instance.
            [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html) databaseAdminClient = [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_Create)();
    
            // Initialize request parameters.
            [Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html) backup = new [Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html)
            {
                DatabaseAsDatabaseName = [DatabaseName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.DatabaseName.html).[FromProjectInstanceDatabase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.DatabaseName.html#Google_Cloud_Spanner_Common_V1_DatabaseName_FromProjectInstanceDatabase_System_String_System_String_System_String_)(projectId, instanceId, databaseId),
                ExpireTime = DateTime.UtcNow.AddDays(14).[ToTimestamp](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.TimeExtensions.html#Google_Protobuf_WellKnownTypes_TimeExtensions_ToTimestamp_System_DateTime_)(),
                VersionTime = versionTime.[ToTimestamp](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.TimeExtensions.html#Google_Protobuf_WellKnownTypes_TimeExtensions_ToTimestamp_System_DateTime_)(),
            };
            [InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html) instanceName = [InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html).[FromProjectInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html#Google_Cloud_Spanner_Common_V1_InstanceName_FromProjectInstance_System_String_System_String_)(projectId, instanceId);
    
            // Make the CreateBackup request.
            Operation<Backup, CreateBackupMetadata> response = databaseAdminClient.[CreateBackup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_CreateBackup_Google_Cloud_Spanner_Admin_Database_V1_CreateBackupRequest_Google_Api_Gax_Grpc_CallSettings_)(instanceName, backup, backupId);
    
            Console.WriteLine("Waiting for the operation to finish.");
    
            // Poll until the returned long-running operation is complete.
            Operation<Backup, CreateBackupMetadata> completedResponse = response.PollUntilCompleted();
    
            if (completedResponse.IsFaulted)
            {
                Console.WriteLine($"Error while creating backup: {completedResponse.Exception}");
                throw completedResponse.Exception;
            }
    
            Console.WriteLine($"Backup created successfully.");
    
            // GetBackup to get more information about the created backup.
            [BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupName.html) backupName = [BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupName.html).[FromProjectInstanceBackup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupName.html#Google_Cloud_Spanner_Admin_Database_V1_BackupName_FromProjectInstanceBackup_System_String_System_String_System_String_)(projectId, instanceId, backupId);
            backup = databaseAdminClient.[GetBackup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_GetBackup_Google_Cloud_Spanner_Admin_Database_V1_BackupName_Google_Api_Gax_Grpc_CallSettings_)(backupName);
            Console.WriteLine($"Backup {backup.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html#Google_Cloud_Spanner_Admin_Database_V1_Backup_Name)} of size {backup.[SizeBytes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html#Google_Cloud_Spanner_Admin_Database_V1_Backup_SizeBytes)} bytes " +
                          $"was created at {backup.[CreateTime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html#Google_Cloud_Spanner_Admin_Database_V1_Backup_CreateTime)} from {backup.[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html#Google_Cloud_Spanner_Admin_Database_V1_Backup_Database)} " +
                          $"and is in state {backup.[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html#Google_Cloud_Spanner_Admin_Database_V1_Backup_State)} " +
                          $"and has version time {backup.[VersionTime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html#Google_Cloud_Spanner_Admin_Database_V1_Backup_VersionTime)}");
            return backup;
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
    	pbt "github.com/golang/protobuf/ptypes/timestamp"
    )
    
    func createBackup(ctx context.Context, w io.Writer, db, backupID string, versionTime time.Time) error {
    	// versionTime := time.Now().AddDate(0, 0, -1) // one day ago
    	matches := regexp.MustCompile("^(.+)/databases/(.+)$").FindStringSubmatch(db)
    	if matches == nil || len(matches) != 3 {
    		return fmt.Errorf("createBackup: invalid database id %q", db)
    	}
    
    	adminClient, err := database.NewDatabaseAdminClient(ctx)
    	if err != nil {
    		return fmt.Errorf("createBackup.NewDatabaseAdminClient: %w", err)
    	}
    	defer adminClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/database/apiv1.html#cloud_google_com_go_spanner_admin_database_apiv1_DatabaseAdminClient_Close)()
    
    	expireTime := time.Now().AddDate(0, 0, 14)
    	// Create a backup.
    	req := adminpb.CreateBackupRequest{
    		Parent:   matches[1],
    		BackupId: backupID,
    		Backup: &adminpb.Backup{
    			Database:    db,
    			ExpireTime:  &pbt.Timestamp{Seconds: expireTime.Unix(), Nanos: int32(expireTime.Nanosecond())},
    			VersionTime: &pbt.Timestamp{Seconds: versionTime.Unix(), Nanos: int32(versionTime.Nanosecond())},
    		},
    	}
    	op, err := adminClient.CreateBackup(ctx, &req)
    	if err != nil {
    		return fmt.Errorf("createBackup.CreateBackup: %w", err)
    	}
    	// Wait for backup operation to complete.
    	backup, err := op.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("createBackup.Wait: %w", err)
    	}
    
    	// Get the name, create time, version time and backup size.
    	backupCreateTime := time.Unix(backup.CreateTime.Seconds, int64(backup.CreateTime.Nanos))
    	backupVersionTime := time.Unix(backup.VersionTime.Seconds, int64(backup.VersionTime.Nanos))
    	fmt.Fprintf(w,
    		"Backup %s of size %d bytes was created at %s with version time %s\n",
    		backup.Name,
    		backup.SizeBytes,
    		backupCreateTime.Format(time.RFC3339),
    		backupVersionTime.Format(time.RFC3339))
    	return nil
    }
    

### Java
    
    
    static void createBackup(DatabaseAdminClient dbAdminClient, String projectId, String instanceId,
        String databaseId, String backupId, Timestamp versionTime) {
      // Set expire time to 14 days from now.
      Timestamp expireTime =
          Timestamp.newBuilder().setSeconds(TimeUnit.MILLISECONDS.toSeconds((
              System.currentTimeMillis() + TimeUnit.DAYS.toMillis(14)))).build();
      BackupName backupName = BackupName.of(projectId, instanceId, backupId);
      Backup backup = Backup.newBuilder()
          .setName(backupName.toString())
          .setDatabase(DatabaseName.of(projectId, instanceId, databaseId).toString())
          .setExpireTime(expireTime).setVersionTime(versionTime).build();
    
      // Initiate the request which returns an OperationFuture.
      System.out.println("Creating backup [" + backupId + "]...");
      try {
        // Wait for the backup operation to complete.
        backup = dbAdminClient.createBackupAsync(
            InstanceName.of(projectId, instanceId), backup, backupId).get();
        System.out.println("Created backup [" + backup.getName() + "]");
      } catch (ExecutionException e) {
        throw SpannerExceptionFactory.asSpannerException(e);
      } catch (InterruptedException e) {
        throw SpannerExceptionFactory.propagateInterrupt(e);
      }
    
      // Reload the metadata of the backup from the server.
      backup = dbAdminClient.getBackup(backup.getName());
      System.out.println(
          String.format(
              "Backup %s of size %d bytes was created at %s for version of database at %s",
              backup.getName(),
              backup.getSizeBytes(),
              java.time.OffsetDateTime.ofInstant(
                  Instant.ofEpochSecond(backup.getCreateTime().getSeconds(),
                      backup.getCreateTime().getNanos()), ZoneId.systemDefault()),
              java.time.OffsetDateTime.ofInstant(
                  Instant.ofEpochSecond(backup.getVersionTime().getSeconds(),
                      backup.getVersionTime().getNanos()), ZoneId.systemDefault()))
      );
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
    // const databaseId = 'my-database';
    // const backupId = 'my-backup';
    // const versionTime = Date.now() - 1000 * 60 * 60 * 24; // One day ago
    
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
    
      // Expire backup 14 days in the future
      const expireTime = Date.now() + 1000 * 60 * 60 * 24 * 14;
    
      // Create a backup of the state of the database at the current time.
      const [operation] = await databaseAdminClient.createBackup({
        parent: databaseAdminClient.instancePath(projectId, instanceId),
        backupId: backupId,
        backup: (protos.google.spanner.admin.database.v1.[Backup](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.database.v1.backup-class.html) = {
          database: databaseAdminClient.databasePath(
            projectId,
            instanceId,
            databaseId,
          ),
          expireTime: [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html).[timestamp](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)(expireTime).[toStruct](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/precise-date/precisedate.html)(),
          versionTime: [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html).[timestamp](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)(versionTime).[toStruct](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/precise-date/precisedate.html)(),
          name: databaseAdminClient.backupPath(projectId, instanceId, backupId),
        }),
      });
    
      console.log(
        `Waiting for backup ${databaseAdminClient.backupPath(
          projectId,
          instanceId,
          backupId,
        )} to complete...`,
      );
      await operation.promise();
    
      // Verify backup is ready
      const [backupInfo] = await databaseAdminClient.getBackup({
        name: databaseAdminClient.backupPath(projectId, instanceId, backupId),
      });
      if (backupInfo.state === 'READY') {
        console.log(
          `Backup ${backupInfo.name} of size ` +
            `${backupInfo.sizeBytes} bytes was created at ` +
            `${new [PreciseDate](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/precise-date/precisedate.html)(backupInfo.createTime).[toISOString](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/precise-date/precisedate.html)()} ` +
            'for version of database at ' +
            `${new [PreciseDate](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/precise-date/precisedate.html)(backupInfo.versionTime).[toISOString](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/precise-date/precisedate.html)()}`,
        );
      } else {
        console.error('ERROR: Backup is not ready.');
      }
    } catch (err) {
      console.error('ERROR:', err);
    } finally {
      // Close the spanner client when finished.
      // The databaseAdminClient does not require explicit closure. The closure of the Spanner client will automatically close the databaseAdminClient.
      spanner.close();
    }

**Note:** The old client library interface code samples for Node.js are archived in [GitHub](https://github.com/googleapis/nodejs-spanner/tree/main/samples/archived). 

### PHP
    
    
    use Google\Cloud\Spanner\Admin\Database\V1\Backup;
    use Google\Cloud\Spanner\Admin\Database\V1\GetBackupRequest;
    use Google\Cloud\Spanner\Admin\Database\V1\Client\DatabaseAdminClient;
    use Google\Cloud\Spanner\Admin\Database\V1\CreateBackupRequest;
    use Google\Protobuf\Timestamp;
    
    /**
     * Create a backup.
     * Example:
     * ```
     * create_backup($projectId, $instanceId, $databaseId, $backupId, $versionTime);
     * ```
     *
     * @param string $projectId The Google Cloud project ID.
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     * @param string $backupId The Spanner backup ID.
     * @param string $versionTime The version of the database to backup. Read more
     * at https://cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups#Backup.FIELDS.version_time
     */
    function create_backup(
        string $projectId,
        string $instanceId,
        string $databaseId,
        string $backupId,
        string $versionTime = '-1hour'
    ): void {
        $databaseAdminClient = new DatabaseAdminClient();
        $databaseFullName = DatabaseAdminClient::databaseName($projectId, $instanceId, $databaseId);
        $instanceFullName = DatabaseAdminClient::instanceName($projectId, $instanceId);
        $timestamp = new Timestamp();
        $timestamp->setSeconds((new \DateTime($versionTime))->getTimestamp());
        $expireTime = new Timestamp();
        $expireTime->setSeconds((new \DateTime('+14 days'))->getTimestamp());
        $request = new CreateBackupRequest([
            'parent' => $instanceFullName,
            'backup_id' => $backupId,
            'backup' => new Backup([
                'database' => $databaseFullName,
                'expire_time' => $expireTime,
                'version_time' => $timestamp
            ])
        ]);
    
        $operation = $databaseAdminClient->createBackup($request);
    
        print('Waiting for operation to complete...' . PHP_EOL);
        $operation->pollUntilComplete();
    
        $request = new GetBackupRequest();
        $request->setName($databaseAdminClient->backupName($projectId, $instanceId, $backupId));
        $info = $databaseAdminClient->getBackup($request);
        printf(
            'Backup %s of size %d bytes was created at %d for version of database at %d' . PHP_EOL,
            basename($info->getName()),
            $info->getSizeBytes(),
            $info->getCreateTime()->getSeconds(),
            $info->getVersionTime()->getSeconds());
    }

**Note:** The old client library interface code samples for PHP are archived in [GitHub](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/main/spanner/src/admin/archived). 

### Python
    
    
    def create_backup(instance_id, database_id, backup_id, version_time):
        """Creates a backup for a database."""
    
        from google.cloud.spanner_admin_database_v1.types import backup as backup_pb
    
        spanner_client = spanner.Client()
        database_admin_api = spanner_client.database_admin_api
    
        # Create a backup
        expire_time = datetime.utcnow() + timedelta(days=14)
    
        request = backup_pb.CreateBackupRequest(
            parent=database_admin_api.instance_path(spanner_client.project, instance_id),
            backup_id=backup_id,
            backup=backup_pb.Backup(
                database=database_admin_api.database_path(
                    spanner_client.project, instance_id, database_id
                ),
                expire_time=expire_time,
                version_time=version_time,
            ),
        )
    
        operation = database_admin_api.create_backup(request)
    
        # Wait for backup operation to complete.
        backup = operation.result(2100)
    
        # Verify that the backup is ready.
        assert backup.state == backup_pb.Backup.State.READY
    
        print(
            "Backup {} of size {} bytes was created at {} for version of database at {}".format(
                backup.name, backup.size_bytes, backup.create_time, backup.version_time
            )
        )
    
    

**Note:** The old client library interface code samples for Python are archived in [GitHub](https://github.com/googleapis/python-spanner/tree/main/samples/samples/archived). 

### Ruby
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "Your Spanner instance ID"
    # database_id = "Your Spanner database ID"
    # backup_id = "Your Spanner backup ID"
    # version_time = Time.now - 60 * 60 * 24 # 1 day ago
    
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
                                                  expire_time: expire_time,
                                                  version_time: version_time
                                              }
    
    puts "Backup operation in progress"
    
    job.wait_until_done!
    
    backup = database_admin_client.get_backup name: backup_path
    puts "Backup #{backup_id} of size #{backup.size_bytes} bytes was created at #{backup.create_time} for version of database at #{backup.version_time}"

## What's next

  * To learn more about backups, see [Backups overview](https://docs.cloud.google.com/spanner/docs/backup).

  * To manage backups, see [Manage backups](https://docs.cloud.google.com/spanner/docs/backup/manage-backups).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
