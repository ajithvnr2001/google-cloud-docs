---
url: https://docs.cloud.google.com/spanner/docs/samples/spanner-restore-backup/
title: Restore database from backup \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:08.354409+00:00
---

# Restore database from backup  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/samples/spanner-restore-backup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Samples ](https://docs.cloud.google.com/spanner/docs/samples)



#  Restore database from backup Stay organized with collections  Save and categorize content based on your preferences. 

Restore a database from a backup. 

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Recover data using point-in-time recovery (PITR)](https://docs.cloud.google.com/spanner/docs/use-pitr)
  * [Restore from a backup](https://docs.cloud.google.com/spanner/docs/backup/restore-backups)



## Code sample

### C++

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    void RestoreDatabase(google::cloud::spanner_admin::DatabaseAdminClient client,
                         std::string const& project_id,
                         std::string const& instance_id,
                         std::string const& database_id,
                         std::string const& backup_id) {
      google::cloud::spanner::Database database(project_id, instance_id,
                                                database_id);
      google::cloud::spanner::Backup backup(database.instance(), backup_id);
      auto restored_db =
          client
              .RestoreDatabase(database.instance().FullName(),
                               database.database_id(), backup.FullName())
              .get();
      if (!restored_db) throw std::move(restored_db).status();
      std::cout << "Database";
      if (restored_db->restore_info().source_type() ==
          google::spanner::admin::database::v1::BACKUP) {
        auto const& backup_info = restored_db->restore_info().backup_info();
        std::cout << " " << backup_info.source_database() << " as of "
                  << google::cloud::spanner::MakeTimestamp(
                         backup_info.version_time())
                         .value();
      }
      std::cout << " restored to " << restored_db->name();
      std::cout << " from backup " << backup.FullName();
      std::cout << ".\n";
    }

### C#

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Spanner.Admin.Database.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.html);
    using [Google.Cloud.Spanner.Common.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using System;
    
    public class RestoreDatabaseSample
    {
        public RestoreInfo RestoreDatabase(string projectId, string instanceId, string databaseId, string backupId)
        {
            // Create the DatabaseAdminClient instance.
            [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html) databaseAdminClient = [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_Create)();
    
            [InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html) parentAsInstanceName = [InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html).[FromProjectInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html#Google_Cloud_Spanner_Common_V1_InstanceName_FromProjectInstance_System_String_System_String_)(projectId, instanceId);
            [BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupName.html) backupAsBackupName = [BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupName.html).[FromProjectInstanceBackup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupName.html#Google_Cloud_Spanner_Admin_Database_V1_BackupName_FromProjectInstanceBackup_System_String_System_String_System_String_)(projectId, instanceId, backupId);
    
            // Make the RestoreDatabase request.
            Operation<Database, RestoreDatabaseMetadata> response = databaseAdminClient.[RestoreDatabase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_RestoreDatabase_Google_Cloud_Spanner_Admin_Database_V1_RestoreDatabaseRequest_Google_Api_Gax_Grpc_CallSettings_)(parentAsInstanceName, databaseId, backupAsBackupName);
    
            Console.WriteLine("Waiting for the operation to finish");
    
            // Poll until the returned long-running operation is complete.
            var completedResponse = response.PollUntilCompleted();
    
            if (completedResponse.IsFaulted)
            {
                Console.WriteLine($"Database Restore Failed: {completedResponse.Exception}");
                throw completedResponse.Exception;
            }
    
            [RestoreInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.RestoreInfo.html) restoreInfo = completedResponse.Result.[RestoreInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.RestoreInfo.html);
            Console.WriteLine(
                $"Database {restoreInfo.[BackupInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.RestoreInfo.html#Google_Cloud_Spanner_Admin_Database_V1_RestoreInfo_BackupInfo).[SourceDatabase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupInfo.html#Google_Cloud_Spanner_Admin_Database_V1_BackupInfo_SourceDatabase)} was restored " +
                $"to {databaseId} from backup {restoreInfo.[BackupInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.RestoreInfo.html#Google_Cloud_Spanner_Admin_Database_V1_RestoreInfo_BackupInfo).[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html)} " +
                $"with version time {restoreInfo.[BackupInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.RestoreInfo.html#Google_Cloud_Spanner_Admin_Database_V1_RestoreInfo_BackupInfo).VersionTime}");
    
            return restoreInfo;
        }
    }

### Go

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"regexp"
    
    	database "cloud.google.com/go/spanner/admin/database/apiv1"
    	adminpb "cloud.google.com/go/spanner/admin/database/apiv1/databasepb"
    )
    
    func restoreBackup(ctx context.Context, w io.Writer, db, backupID string) error {
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
    	databaseID := matches[2]
    	backupName := instanceName + "/backups/" + backupID
    
    	// Start restoring backup to a new database.
    	restoreOp, err := adminClient.RestoreDatabase(ctx, &adminpb.RestoreDatabaseRequest{
    		Parent:     instanceName,
    		DatabaseId: databaseID,
    		Source: &adminpb.RestoreDatabaseRequest_Backup{
    			Backup: backupName,
    		},
    	})
    	if err != nil {
    		return err
    	}
    	// Wait for restore operation to complete.
    	dbObj, err := restoreOp.Wait(ctx)
    	if err != nil {
    		return err
    	}
    	// Newly created database has restore information.
    	backupInfo := dbObj.RestoreInfo.GetBackupInfo()
    	if backupInfo != nil {
    		fmt.Fprintf(w, "Source database %s restored from backup %s\n", backupInfo.SourceDatabase, backupInfo.Backup)
    	}
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static void restoreBackup(
        DatabaseAdminClient dbAdminClient,
        String projectId,
        String instanceId,
        String backupId,
        String restoreToDatabaseId) {
      BackupName backupName = BackupName.of(projectId, instanceId, backupId);
      Backup backup = dbAdminClient.getBackup(backupName);
      // Initiate the request which returns an OperationFuture.
      System.out.println(String.format(
          "Restoring backup [%s] to database [%s]...", backup.getName(), restoreToDatabaseId));
      try {
        RestoreDatabaseRequest request =
            RestoreDatabaseRequest.newBuilder()
                .setParent(InstanceName.of(projectId, instanceId).toString())
                .setDatabaseId(restoreToDatabaseId)
                .setBackup(backupName.toString()).build();
        OperationFuture<com.google.spanner.admin.database.v1.Database, RestoreDatabaseMetadata> op =
            dbAdminClient.restoreDatabaseAsync(request);
        // Wait until the database has been restored.
        com.google.spanner.admin.database.v1.Database db = op.get();
        // Get the restore info.
        RestoreInfo restoreInfo = db.getRestoreInfo();
        BackupInfo backupInfo = restoreInfo.getBackupInfo();
    
        System.out.println(
            "Restored database ["
                + db.getName()
                + "] from ["
                + restoreInfo.getBackupInfo().getBackup()
                + "] with version time [" + backupInfo.getVersionTime() + "]");
      } catch (ExecutionException e) {
        throw SpannerExceptionFactory.newSpannerException(e.getCause());
      } catch (InterruptedException e) {
        throw SpannerExceptionFactory.propagateInterrupt(e);
      }
    }

### PHP

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Spanner\Admin\Database\V1\Client\DatabaseAdminClient;
    use Google\Cloud\Spanner\Admin\Database\V1\RestoreDatabaseRequest;
    
    /**
     * Restore a database from a backup.
     * Example:
     * ```
     * restore_backup($projectId, $instanceId, $databaseId, $backupId);
     * ```
     * @param string $projectId The Google Cloud project ID.
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     * @param string $backupId The Spanner backup ID.
     */
    function restore_backup(
        string $projectId,
        string $instanceId,
        string $databaseId,
        string $backupId
    ): void {
        $databaseAdminClient = new DatabaseAdminClient();
    
        $backupName = DatabaseAdminClient::backupName($projectId, $instanceId, $backupId);
        $instanceName = DatabaseAdminClient::instanceName($projectId, $instanceId);
    
        $request = new RestoreDatabaseRequest([
            'parent' => $instanceName,
            'database_id' => $databaseId,
            'backup' => $backupName
        ]);
    
        $operationResponse = $databaseAdminClient->restoreDatabase($request);
        $operationResponse->pollUntilComplete();
    
        $database = $operationResponse->operationSucceeded() ? $operationResponse->getResult() : null;
        $restoreInfo = $database->getRestoreInfo();
        $backupInfo = $restoreInfo->getBackupInfo();
        $sourceDatabase = $backupInfo->getSourceDatabase();
        $sourceBackup = $backupInfo->getBackup();
        $versionTime = $backupInfo->getVersionTime()->getSeconds();
        printf(
            'Database %s restored from backup %s with version time %s' . PHP_EOL,
            $sourceDatabase, $sourceBackup, $versionTime
        );
    }

### Python

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def restore_database(instance_id, new_database_id, backup_id):
        """Restores a database from a backup."""
        spanner_client = spanner.Client()
        instance = spanner_client.instance(instance_id)
        # Create a backup on database_id.
    
        # Start restoring an existing backup to a new database.
        backup = instance.backup(backup_id)
        new_database = instance.database(new_database_id)
        operation = new_database.restore(backup)
    
        # Wait for restore operation to complete.
        operation.result(1600)
    
        # Newly created database has restore information.
        new_database.reload()
        restore_info = new_database.restore_info
        print(
            "Database {} restored to {} from backup {} with version time {}.".format(
                restore_info.backup_info.source_database,
                new_database_id,
                restore_info.backup_info.backup,
                restore_info.backup_info.version_time,
            )
        )
    
    

### Ruby

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "Your Spanner instance ID"
    # database_id = "Your Spanner database ID of where to restore"
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
    
    job = database_admin_client.restore_database parent: instance_path,
                                                 database_id: database_id,
                                                 backup: backup_path
    
    puts "Waiting for restore backup operation to complete"
    
    job.wait_until_done!
    
    database = database_admin_client.get_database name: db_path
    restore_info = database.restore_info
    puts "Database #{restore_info.backup_info.source_database} was restored to #{database_id} from backup #{restore_info.backup_info.backup} with version time #{restore_info.backup_info.version_time}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudspanner). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
