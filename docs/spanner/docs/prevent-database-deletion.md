---
url: https://docs.cloud.google.com/spanner/docs/prevent-database-deletion/
title: Prevent accidental database deletion \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:56.194119+00:00
---

# Prevent accidental database deletion  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/prevent-database-deletion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Prevent accidental database deletion Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to protect Spanner databases from accidental deletion.

Spanner database deletion protection prevents the accidental deletion of existing databases by users or service accounts that have the necessary IAM permissions to delete the database. By enabling database deletion protection, you can safeguard databases that are important to your application and services. Use database deletion protection along with [point-in-time recovery](https://docs.cloud.google.com/spanner/docs/pitr) and [backup features](https://docs.cloud.google.com/spanner/docs/backup) to provide a comprehensive set of data protection capabilities for your Spanner databases.

By default, the deletion protection setting is disabled when you create your new database. You can enable the deletion protection setting after the database creation succeeds. Additionally, you can enable this setting on an existing database. If you want to protect multiple databases, enable the setting on each database individually. Enabling or disabling deletion protection doesn't have any performance impact on the database. If you need to delete a database that has database protection enabled, you need to disable the protection before you can delete the database.

## Limitations

You can't enable database deletion protection in the following scenarios:

  * If the database is being deleted.
  * If the database is being restored from a backup. (After the restore operation completes, you can enable database protection).



In addition, backups of a database and databases restored from a backup don't inherit the database deletion protection setting of their source database. After you restore a database from a backup, you must enable its database deletion protection separately.

If you delete your project, Spanner database deletion protection doesn't prevent the deletion of your database or instance. For more information about what happens when you delete your project, see [Shutting down (deleting) projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects).

## Access control with IAM

To enable the deletion protection setting of your database, you must have certain [IAM permissions](https://docs.cloud.google.com/spanner/docs/iam).

You need to have the `spanner.databases.update` permission to enable or disable database deletion protection. If you only need to view the status of your database configuration, you need to have the `spanner.databases.list` or `spanner.databases.get` permission. For information on how to grant Spanner IAM permissions, see [Apply IAM permissions](https://docs.cloud.google.com/spanner/docs/grant-permissions).

If you have the predefined [Spanner Database Admin `roles/spanner.databaseAdmin`](https://docs.cloud.google.com/spanner/docs/iam#spanner.databaseAdmin) role for your database, you can update and enable database deletion protection.

You can enable the database deletion protection setting on an existing database to prevent the accidental deletion of the database.

## Enable database deletion protection

You can enable database deletion protection using the gcloud CLI, the client libraries, and the [REST](https://cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/patch) or [RPC](https://cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.UpdateDatabase) APIs. You can't enable database deletion protection using the Google Cloud console.

###  gcloud 

To enable the deletion protection setting of a database, run the following command:
    
    
      gcloud spanner databases update
      DATABASE_ID --instance=INSTANCE_ID
      --enable-drop-protection [--async]
    

The following options are required:

`DATABASE_ID`
    ID of the database.
`INSTANCE_ID`
    ID of the instance for the database.

The following options are optional:

`--async`
    Return immediately, without waiting for the operation in progress to complete.

### Client libraries

### C++
    
    
    void UpdateDatabase(google::cloud::spanner_admin::DatabaseAdminClient client,
                        std::string const& project_id,
                        std::string const& instance_id,
                        std::string const& database_id, bool drop_protection) {
      google::cloud::spanner::Database db(project_id, instance_id, database_id);
      google::spanner::admin::database::v1::Database database;
      database.set_name(db.FullName());
      database.set_enable_drop_protection(drop_protection);
      google::protobuf::FieldMask update_mask;
      update_mask.add_paths("enable_drop_protection");
      auto updated = client.UpdateDatabase(database, update_mask).get();
      if (!updated) throw std::move(updated).status();
      std::cout << "Database " << updated->name() << " successfully updated.\n";
    }

### C#
    
    
    using [Google.Cloud.Spanner.Admin.Database.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.html);
    using [Google.Cloud.Spanner.Common.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    using System.Threading.Tasks;
    
    public class UpdateDatabaseAsyncSample
    {
        public async Task<Database> UpdateDatabaseAsync(string projectId, string instanceId, string databaseId)
        {
            var databaseAdminClient = await [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_CreateAsync_System_Threading_CancellationToken_)();
            var databaseName = [DatabaseName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.DatabaseName.html).[Format](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.DatabaseName.html#Google_Cloud_Spanner_Common_V1_DatabaseName_Format_System_String_System_String_System_String_)(projectId, instanceId, databaseId);
            Database databaseToUpdate = await databaseAdminClient.GetDatabaseAsync(databaseName);
    
            databaseToUpdate.[EnableDropProtection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Database.html#Google_Cloud_Spanner_Admin_Database_V1_Database_EnableDropProtection) = true;
            var updateDatabaseRequest = new [UpdateDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.UpdateDatabaseRequest.html)()
            {
                Database = databaseToUpdate,
                UpdateMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html) { Paths = { "enable_drop_protection" } }
            };
    
            var operation = await databaseAdminClient.UpdateDatabaseAsync(updateDatabaseRequest);
    
            // Wait until the operation has finished.
            Console.WriteLine("Waiting for the operation to finish.");
            var completedResponse = await operation.PollUntilCompletedAsync();
    
            if (completedResponse.IsFaulted)
            {
                Console.WriteLine($"Error while updating database {databaseId}: {completedResponse.Exception}");
                throw completedResponse.Exception;
            }
    
            Console.WriteLine($"Updated database {databaseId}.");
    
            // Return the updated database.
            return completedResponse.Result;
        }
    }

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	database "cloud.google.com/go/spanner/admin/database/apiv1"
    	adminpb "cloud.google.com/go/spanner/admin/database/apiv1/databasepb"
    	"google.golang.org/genproto/protobuf/field_mask"
    )
    
    func updateDatabase(ctx context.Context, w io.Writer, db string) error {
    	// db = `projects/<project>/instances/<instance-id>/database/<database-id>`
    	// Instantiate database admin client.
    	adminClient, err := database.NewDatabaseAdminClient(ctx)
    	if err != nil {
    		return fmt.Errorf("updateDatabase.NewDatabaseAdminClient: %w", err)
    	}
    	defer adminClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/database/apiv1.html#cloud_google_com_go_spanner_admin_database_apiv1_DatabaseAdminClient_Close)()
    
    	// Instantiate the request for performing update database operation.
    	op, err := adminClient.UpdateDatabase(ctx, &adminpb.UpdateDatabaseRequest{
    		Database: &adminpb.Database{
    			Name:                 db,
    			EnableDropProtection: true,
    		},
    		UpdateMask: &field_mask.FieldMask{
    			Paths: []string{"enable_drop_protection"},
    		},
    	})
    	if err != nil {
    		return fmt.Errorf("updateDatabase.UpdateDatabase: %w", err)
    	}
    
    	// Wait for update database operation to complete.
    	fmt.Fprintf(w, "Waiting for update database operation to complete [%s]\n", db)
    	if _, err := op.Wait(ctx); err != nil {
    		return fmt.Errorf("updateDatabase.Wait: %w", err)
    	}
    	fmt.Fprintf(w, "Updated database [%s]\n", db)
    	return nil
    }
    

### Java
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.spanner.[Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html);
    import com.google.cloud.spanner.[SpannerExceptionFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html);
    import com.google.cloud.spanner.[SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html);
    import com.google.cloud.spanner.admin.database.v1.[DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html);
    import com.google.common.collect.Lists;
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import com.google.spanner.admin.database.v1.[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Database.html);
    import com.google.spanner.admin.database.v1.[DatabaseName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.DatabaseName.html);
    import com.google.spanner.admin.database.v1.[UpdateDatabaseMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.UpdateDatabaseMetadata.html);
    import com.google.spanner.admin.database.v1.[UpdateDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.UpdateDatabaseRequest.html);
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class UpdateDatabaseSample {
    
      static void updateDatabase() {
        // TODO(developer): Replace these variables before running the sample.
        final String projectId = "my-project";
        final String instanceId = "my-instance";
        final String databaseId = "my-database";
    
        updateDatabase(projectId, instanceId, databaseId);
      }
    
      static void updateDatabase(
          String projectId, String instanceId, String databaseId) {
        try ([Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html) spanner =
            [SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html).newBuilder().setProjectId(projectId).build().getService();
            [DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html) databaseAdminClient = spanner.[createDatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html#com_google_cloud_spanner_Spanner_createDatabaseAdminClient__)()) {
          final [Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Database.html) database =
              [Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Database.html).newBuilder()
                  .setName([DatabaseName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.DatabaseName.html).of(projectId, instanceId, databaseId).toString())
                  .[setEnableDropProtection](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Database.Builder.html#com_google_spanner_admin_database_v1_Database_Builder_setEnableDropProtection_boolean_)(true).build();
          final [UpdateDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.UpdateDatabaseRequest.html) updateDatabaseRequest =
              [UpdateDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.UpdateDatabaseRequest.html).newBuilder()
                  .setDatabase(database)
                  .setUpdateMask(
                      [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addAllPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addAllPaths_java_lang_Iterable_java_lang_String__)(
                          Lists.newArrayList("enable_drop_protection")).build())
                  .build();
          OperationFuture<Database, UpdateDatabaseMetadata> operation =
              databaseAdminClient.updateDatabaseAsync(updateDatabaseRequest);
          System.out.printf("Waiting for update operation for %s to complete...\n", databaseId);
          [Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Database.html) updatedDb = operation.get(5, TimeUnit.MINUTES);
          System.out.printf("Updated database %s.\n", updatedDb.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Database.html#com_google_spanner_admin_database_v1_Database_getName__)());
        } catch (ExecutionException | TimeoutException e) {
          // If the operation failed during execution, expose the cause.
          throw [SpannerExceptionFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html).[asSpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html#com_google_cloud_spanner_SpannerExceptionFactory_asSpannerException_java_lang_Throwable_)(e.getCause());
        } catch (InterruptedException e) {
          // Throw when a thread is waiting, sleeping, or otherwise occupied,
          // and the thread is interrupted, either before or during the activity.
          throw [SpannerExceptionFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html).[propagateInterrupt](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html#com_google_cloud_spanner_SpannerExceptionFactory_propagateInterrupt_java_lang_InterruptedException_)(e);
        }
      }
    }

**Note:** The old client library interface code samples for Java are archived in [GitHub](https://github.com/googleapis/google-cloud-java/tree/main/java-spanner/samples/snippets/src/main/java/com/example/spanner/admin/archived). 

### Node.js
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const instanceId = 'my-instance';
    // const databaseId = 'my-database';
    // const projectId = 'my-project-id';
    
    // Imports the Google Cloud client library
    const {Spanner, protos} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    
    // creates a client
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({
      projectId: projectId,
    });
    
    const databaseAdminClient = spanner.[getDatabaseAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)();
    
    async function updateDatabase() {
      // Update the database metadata fields
      try {
        console.log(
          `Updating database ${databaseAdminClient.databasePath(
            projectId,
            instanceId,
            databaseId,
          )}.`,
        );
        const [operation] = await databaseAdminClient.updateDatabase({
          database: {
            name: databaseAdminClient.databasePath(
              projectId,
              instanceId,
              databaseId,
            ),
            enableDropProtection: true,
          },
          // updateMask contains the fields to be updated in database
          updateMask: (protos.google.protobuf.[FieldMask](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.protobuf.fieldmask.html) = {
            paths: ['enable_drop_protection'],
          }),
        });
        console.log(
          `Waiting for update operation for ${databaseId} to complete...`,
        );
        await operation.promise();
        console.log(`Updated database ${databaseId}.`);
      } catch (err) {
        console.log('ERROR:', err);
      }
    }
    updateDatabase();

**Note:** The old client library interface code samples for Node.js are archived in [GitHub](https://github.com/googleapis/nodejs-spanner/tree/main/samples/archived). 

### PHP
    
    
    use Google\Cloud\Spanner\Admin\Database\V1\Client\DatabaseAdminClient;
    use Google\Cloud\Spanner\Admin\Database\V1\Database;
    use Google\Cloud\Spanner\Admin\Database\V1\GetDatabaseRequest;
    use Google\Cloud\Spanner\Admin\Database\V1\UpdateDatabaseRequest;
    use Google\Protobuf\FieldMask;
    
    /**
     * Updates the drop protection setting for a database.
     * Example:
     * ```
     * update_database($projectId, $instanceId, $databaseId);
     * ```
     *
     * @param string $projectId The Google Cloud project ID.
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     */
    function update_database(string $projectId, string $instanceId, string $databaseId): void
    {
        $newUpdateMaskField = new FieldMask([
            'paths' => ['enable_drop_protection']
        ]);
        $databaseAdminClient = new DatabaseAdminClient();
        $databaseFullName = DatabaseAdminClient::databaseName($projectId, $instanceId, $databaseId);
        $database = (new Database())
            ->setEnableDropProtection(true)
            ->setName($databaseFullName);
    
        printf('Updating database %s', $databaseId);
        $operation = $databaseAdminClient->updateDatabase((new UpdateDatabaseRequest())
            ->setDatabase($database)
            ->setUpdateMask($newUpdateMaskField));
    
        $operation->pollUntilComplete();
    
        $database = $databaseAdminClient->getDatabase(
            new GetDatabaseRequest(['name' => $databaseFullName])
        );
        printf(
            'Updated the drop protection for %s to %s' . PHP_EOL,
            $database->getName(),
            $database->getEnableDropProtection()
        );
    }

**Note:** The old client library interface code samples for PHP are archived in [GitHub](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/main/spanner/src/admin/archived). 

### Python
    
    
    def update_database(instance_id, database_id):
        """Updates the drop protection setting for a database."""
        from google.cloud.spanner_admin_database_v1.types import spanner_database_admin
    
        spanner_client = spanner.Client()
        database_admin_api = spanner_client.database_admin_api
    
        request = spanner_database_admin.UpdateDatabaseRequest(
            database=spanner_database_admin.Database(
                name=database_admin_api.database_path(
                    spanner_client.project, instance_id, database_id
                ),
                enable_drop_protection=True,
            ),
            update_mask={"paths": ["enable_drop_protection"]},
        )
        operation = database_admin_api.update_database(request=request)
        print(
            "Waiting for update operation for {}/databases/{} to complete...".format(
                database_admin_api.instance_path(spanner_client.project, instance_id),
                database_id,
            )
        )
        operation.result(OPERATION_TIMEOUT_SECONDS)
    
        print(
            "Updated database {}/databases/{}.".format(
                database_admin_api.instance_path(spanner_client.project, instance_id),
                database_id,
            )
        )
    
    

**Note:** The old client library interface code samples for Python are archived in [GitHub](https://github.com/googleapis/python-spanner/tree/main/samples/samples/archived). 

### Ruby
    
    
    require "google/cloud/spanner/admin/database"
    
    ##
    # This is a snippet for showcasing how to update database.
    #
    # @param project_id  [String] The ID of the Google Cloud project.
    # @param instance_id [String] The ID of the spanner instance.
    # @param database_id [String] The ID of the database.
    #
    def spanner_update_database project_id:, instance_id:, database_id:
      client = Google::Cloud::Spanner::Admin::Database.database_admin project_id: project_id
      db_path = client.database_path project: project_id, instance: instance_id, database: database_id
      database = client.get_database name: db_path
    
      puts "Updating database #{database.name}"
      database.enable_drop_protection = true
      job = client.update_database database: database, update_mask: { paths: ["enable_drop_protection"] }
      puts "Waiting for update operation for #{database.name} to complete..."
      job.wait_until_done!
      puts "Updated database #{database.name}"
    end
    

## Check if a database has deletion protection enabled

You can determine if your database has its deletion protection enabled by viewing the database configuration.

###  gcloud 

To check if a database has deletion protection enabled, you can run the `gcloud spanner databases describe` command to get detailed information about a database, or you can run the `gcloud spanner databases list` to get detailed information about databases within an instance.
    
    
      gcloud spanner databases describe
      projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID
    

The following options are required:

`PROJECT_ID`
    ID of the project for the database.
`INSTANCE_ID`
    ID of the instance for the database.
`DATABASE_ID`
    ID of the database.

If deletion protection is enabled, you'll see an `enableDropProtection: true` parameter in the output.

## Disable database deletion protection

You can disable database deletion protection if a database no longer needs this protection or if you need to delete a database that has this setting enabled.

If you want to delete an instance that has one or more databases with deletion protection enabled, you must first disable the deletion protection on all databases in that instance before you can delete the instance.

###  gcloud 

To disable the deletion protection setting of a database, run the following command:
    
    
      gcloud spanner databases update
      DATABASE_ID --instance=INSTANCE_ID
      --no-enable-drop-protection [--async]
    

The following options are required:

`DATABASE_ID`
    ID of the database.
`INSTANCE_ID`
    ID of the instance for the database.

The following options are optional:

`--async`
    Return immediately, without waiting for the operation in progress to complete.

## What's next

  * Learn how to [Create and manage databases](https://docs.cloud.google.com/spanner/docs/create-manage-databases).
  * Learn more about how to [backup and restore a database](https://docs.cloud.google.com/spanner/docs/backup).
  * Learn how to [make schema updates](https://docs.cloud.google.com/spanner/docs/schema-updates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
