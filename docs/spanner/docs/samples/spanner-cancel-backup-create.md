---
url: https://docs.cloud.google.com/spanner/docs/samples/spanner-cancel-backup-create/
title: Cancel backup create operation \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:41.532710+00:00
---

# Cancel backup create operation  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/samples/spanner-cancel-backup-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Samples ](https://docs.cloud.google.com/spanner/docs/samples)



#  Cancel backup create operation Stay organized with collections  Save and categorize content based on your preferences. 

Cancel a create backup database operation.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage backups](https://docs.cloud.google.com/spanner/docs/backup/manage-backups)



## Code sample

### C++

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### PHP

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Python

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def cancel_backup(instance_id, database_id, backup_id):
        spanner_client = spanner.Client()
        instance = spanner_client.instance(instance_id)
        database = instance.database(database_id)
    
        expire_time = datetime.utcnow() + timedelta(days=30)
    
        # Create a backup.
        backup = instance.backup(backup_id, database=database, expire_time=expire_time)
        operation = backup.create()
    
        # Cancel backup creation.
        operation.cancel()
    
        # Cancel operations are best effort so either it will complete or
        # be cancelled.
        while not operation.done():
            time.sleep(300)  # 5 mins
    
        # Deal with resource if the operation succeeded.
        if backup.exists():
            print("Backup was created before the cancel completed.")
            backup.delete()
            print("Backup deleted.")
        else:
            print("Backup creation was successfully cancelled.")
    
    

### Ruby

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudspanner). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
