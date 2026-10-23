---
url: https://docs.cloud.google.com/spanner/docs/samples/spanner-update-backup/
title: Update backup \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:42.221971+00:00
---

# Update backup  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/samples/spanner-update-backup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Samples ](https://docs.cloud.google.com/spanner/docs/samples)



#  Update backup Stay organized with collections  Save and categorize content based on your preferences. 

Update a backup by retrieving the expiry time of a backup and extending it.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage backups](https://docs.cloud.google.com/spanner/docs/backup/manage-backups)



## Code sample

### C++

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### PHP

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Python

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def update_backup(instance_id, backup_id):
        spanner_client = spanner.Client()
        instance = spanner_client.instance(instance_id)
        backup = instance.backup(backup_id)
        backup.reload()
    
        # Expire time must be within 366 days of the create time of the backup.
        old_expire_time = backup.expire_time
        # New expire time should be less than the max expire time
        new_expire_time = min(backup.max_expire_time, old_expire_time + timedelta(days=30))
        backup.update_expire_time(new_expire_time)
        print(
            "Backup {} expire time was updated from {} to {}.".format(
                backup.name, old_expire_time, new_expire_time
            )
        )
    
    

### Ruby

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudspanner). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
