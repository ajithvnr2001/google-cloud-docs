---
url: https://docs.cloud.google.com/spanner/docs/samples/spanner-list-database-operations/
title: List database operations \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:11.247580+00:00
---

# List database operations  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/samples/spanner-list-database-operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Samples ](https://docs.cloud.google.com/spanner/docs/samples)



#  List database operations Stay organized with collections  Save and categorize content based on your preferences. 

List all operations running on the database and list the percentage complete for each operation.

## Code sample

### C++

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    void ListDatabaseOperations(
        google::cloud::spanner_admin::DatabaseAdminClient client,
        std::string const& project_id, std::string const& instance_id) {
      google::cloud::spanner::Instance in(project_id, instance_id);
      google::spanner::admin::database::v1::ListDatabaseOperationsRequest request;
      request.set_parent(in.FullName());
      request.set_filter(
          "(metadata.@type:type.googleapis.com/"
          "google.spanner.admin.database.v1.OptimizeRestoredDatabaseMetadata)");
      for (auto& operation : client.ListDatabaseOperations(request)) {
        if (!operation) throw std::move(operation).status();
        google::spanner::admin::database::v1::OptimizeRestoredDatabaseMetadata
            metadata;
        (void)operation->metadata().UnpackTo(&metadata);
        std::cout << "Database " << metadata.name() << " restored from backup is "
                  << metadata.progress().progress_percent() << "% optimized.\n";
      }
    }

### C#

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Spanner.Admin.Database.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.html);
    using [Google.Cloud.Spanner.Common.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using System;
    using System.Collections.Generic;
    using System.Linq;
    
    public class ListDatabaseOperationsSample
    {
        public IEnumerable<Operation> ListDatabaseOperations(string projectId, string instanceId)
        {
            // Create the DatabaseAdminClient instance.
            [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html) databaseAdminClient = [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_Create)();
    
            var filter = "(metadata.@type:type.googleapis.com/google.spanner.admin.database.v1.OptimizeRestoredDatabaseMetadata)";
    
            [ListDatabaseOperationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.ListDatabaseOperationsRequest.html) request = new [ListDatabaseOperationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.ListDatabaseOperationsRequest.html)
            {
                ParentAsInstanceName = [InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html).[FromProjectInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html#Google_Cloud_Spanner_Common_V1_InstanceName_FromProjectInstance_System_String_System_String_)(projectId, instanceId),
                Filter = filter
            };
    
            // List the optimize restored databases operations on the instance.
            var operations = databaseAdminClient.[ListDatabaseOperations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_ListDatabaseOperations_Google_Cloud_Spanner_Admin_Database_V1_ListDatabaseOperationsRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // We print the first 5 elements for demonstration purposes.
            // You can print all operations in the sequence by removing the call to Take(5).
            // The sequence will lazily fetch elements in pages as needed.
            foreach (var operation in operations.Take(5))
            {
                [OptimizeRestoredDatabaseMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.OptimizeRestoredDatabaseMetadata.html) metadata =
                    operation.[Metadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html#Google_LongRunning_Operation_Metadata).Unpack<OptimizeRestoredDatabaseMetadata>();
                Console.WriteLine(
                    $"Database {metadata.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.OptimizeRestoredDatabaseMetadata.html#Google_Cloud_Spanner_Admin_Database_V1_OptimizeRestoredDatabaseMetadata_Name)} restored from backup is {metadata.[Progress](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.OptimizeRestoredDatabaseMetadata.html#Google_Cloud_Spanner_Admin_Database_V1_OptimizeRestoredDatabaseMetadata_Progress).[ProgressPercent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.OperationProgress.html#Google_Cloud_Spanner_Admin_Database_V1_OperationProgress_ProgressPercent)}% optimized.");
            }
    
            return operations;
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
    	"github.com/golang/protobuf/ptypes"
    	"google.golang.org/api/iterator"
    )
    
    func listDatabaseOperations(ctx context.Context, w io.Writer, db string) error {
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
    	// List the databases that are being optimized after a restore operation.
    	filter := "(metadata.@type:type.googleapis.com/google.spanner.admin.database.v1.OptimizeRestoredDatabaseMetadata)"
    	iter := adminClient.ListDatabaseOperations(ctx, &adminpb.ListDatabaseOperationsRequest{
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
    		metadata := &adminpb.OptimizeRestoredDatabaseMetadata{}
    		if err := ptypes.UnmarshalAny(resp.Metadata, metadata); err != nil {
    			return err
    		}
    		fmt.Fprintf(w, "Database %s restored from backup is %d%% optimized.\n",
    			metadata.Name,
    			metadata.Progress.ProgressPercent,
    		)
    	}
    	return nil
    }
    

### Java

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static void listDatabaseOperations(
        DatabaseAdminClient dbAdminClient, String projectId, String instanceId) {
      // Get optimize restored database operations.
      com.google.cloud.Timestamp last24Hours = com.google.cloud.Timestamp.ofTimeSecondsAndNanos(
          TimeUnit.SECONDS.convert(
              TimeUnit.HOURS.convert(com.google.cloud.Timestamp.now().getSeconds(), TimeUnit.SECONDS)
                  - 24,
              TimeUnit.HOURS), 0);
      String filter = String.format("(metadata.@type:type.googleapis.com/"
          + "google.spanner.admin.database.v1.OptimizeRestoredDatabaseMetadata) AND "
          + "(metadata.progress.start_time > \"%s\")", last24Hours);
      ListDatabaseOperationsRequest listDatabaseOperationsRequest =
          ListDatabaseOperationsRequest.newBuilder()
              .setParent(com.google.spanner.admin.instance.v1.InstanceName.of(
                  projectId, instanceId).toString()).setFilter(filter).build();
      ListDatabaseOperationsPagedResponse pagedResponse
          = dbAdminClient.listDatabaseOperations(listDatabaseOperationsRequest);
      for (Operation op : pagedResponse.iterateAll()) {
        try {
          OptimizeRestoredDatabaseMetadata metadata =
              op.getMetadata().unpack(OptimizeRestoredDatabaseMetadata.class);
          System.out.println(String.format(
              "Database %s restored from backup is %d%% optimized",
              metadata.getName(),
              metadata.getProgress().getProgressPercent()));
        } catch (InvalidProtocolBufferException e) {
          // The returned operation does not contain OptimizeRestoredDatabaseMetadata.
          System.err.println(e.getMessage());
        }
      }
    }

### PHP

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Spanner\SpannerClient;
    
    /**
     * List all optimize restored database operations in an instance.
     * Example:
     * ```
     * list_database_operations($instanceId);
     * ```
     *
     * @param string $instanceId The Spanner instance ID.
     */
    function list_database_operations(string $instanceId): void
    {
        $spanner = new SpannerClient();
        $instance = $spanner->instance($instanceId);
    
        // List the databases that are being optimized after a restore operation.
        $filter = '(metadata.@type:type.googleapis.com/' .
                  'google.spanner.admin.database.v1.OptimizeRestoredDatabaseMetadata)';
    
        $operations = $instance->databaseOperations(['filter' => $filter]);
    
        foreach ($operations as $operation) {
            if (!$operation->done()) {
                $meta = $operation->info()['metadata'];
                $dbName = basename($meta['name']);
                $progress = $meta['progress']['progressPercent'];
                printf('Database %s restored from backup is %d%% optimized.' . PHP_EOL, $dbName, $progress);
            }
        }
    }

### Python

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def list_database_operations(instance_id):
        spanner_client = spanner.Client()
        instance = spanner_client.instance(instance_id)
    
        # List the progress of restore.
        filter_ = (
            "(metadata.@type:type.googleapis.com/"
            "google.spanner.admin.database.v1.OptimizeRestoredDatabaseMetadata)"
        )
        operations = instance.list_database_operations(filter_=filter_)
        for op in operations:
            print(
                "Database {} restored from backup is {}% optimized.".format(
                    op.metadata.name, op.metadata.progress.progress_percent
                )
            )
    
    

### Ruby

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "Your Spanner instance ID"
    
    require "google/cloud/spanner"
    require "google/cloud/spanner/admin/database"
    
    database_admin_client = Google::Cloud::Spanner::Admin::Database.database_admin
    instance_path = database_admin_client.instance_path project: project_id, instance: instance_id
    jobs = database_admin_client.list_database_operations parent: instance_path,
                                                          filter: "metadata.@type:type.googleapis.com/google.spanner.admin.database.v1.OptimizeRestoredDatabaseMetadata"
    
    jobs.each do |job|
      if job.error?
        puts job.error
      elsif job.results
        progress_percent = job.metadata.progress.progress_percent
        puts "Database #{job.results.name} restored from backup is #{progress_percent}% optimized"
      end
    end
    
    puts "List database operations with optimized database filter found #{jobs.count} jobs."
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudspanner). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
