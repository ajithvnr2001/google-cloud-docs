---
url: https://docs.cloud.google.com/spanner/docs/batch-write/
title: Modify data using batch write \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:40.123216+00:00
---

# Modify data using batch write  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/batch-write/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Modify data using batch write Stay organized with collections  Save and categorize content based on your preferences. 

This page describes Spanner batch write requests and how you can use them to modify your Spanner data.

You can use Spanner batch write to insert, update, or delete multiple rows in your Spanner tables. Spanner batch write supports low latency writes without a read operation, and returns responses as mutations are applied in batches. To use batch write, you group related mutations together, and all mutations in a group are committed atomically. The mutations across groups are applied in an unspecified order and are independent of one another (non-atomic). Spanner doesn't need to wait for all mutations to be applied before sending a response, which means that batch write allows for partial failure. You can also execute multiple batch writes at a time. For more information, see How to use batch write.

## Use cases

Spanner batch write is especially useful if you want to commit a large number of writes without a read operation, but don't require an atomic transaction for all your mutations.

If you want to batch your DML requests, use [batch DML](https://docs.cloud.google.com/spanner/docs/dml-tasks#use-batch) to modify your Spanner data. For more information on the differences between DML and mutations, see [Comparing DML and mutations](https://docs.cloud.google.com/spanner/docs/dml-versus-mutations).

For single mutation requests, we recommend using a [locking read-write transaction](https://docs.cloud.google.com/spanner/docs/transactions#read-write_transactions).

## Limitations

Spanner batch write has the following limitations:

  * **Spanner batch write is not available using the Google Cloud console or Google Cloud CLI.** It is only available using REST and RPC APIs and the Spanner client libraries.

  * **[Replay protection](https://docs.cloud.google.com/spanner/docs/sessions#handle_errors_for_write_transactions_that_are_not_idempotent) is not supported using batch write.** It's possible for mutations to be applied more than once, and a mutation that is applied more than once might result in a failure. For example, if an insert mutation is replayed, it might produce an already exists error, or if you use generated or commit timestamp-based keys in the mutation, it might result in additional rows being added to the table. We recommend structuring your writes to be idempotent to avoid this issue.

  * **You can't rollback a completed batch write request.** You can cancel an in-progress batch write request. If you cancel an in-progress batch write, mutations in uncompleted groups are rolled back. Mutations in completed groups are committed to the database.

  * **The maximum size for a batch write request is the same as the limit for a commit request.** For more information, see [Limits for creating, reading, updating, and deleting data](https://docs.cloud.google.com/spanner/quotas#limits-for).




## How to use batch write

To use batch write, you must have the `spanner.databases.write` permission on the database that you want to modify. You can batch write mutations non-atomically in a single call using a [REST](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/batchWrite) or [RPC API](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.v1#google.spanner.v1.Spanner.BatchWrite) request call.

You should group the following mutation types together when using batch write:

  * Inserting rows with the same primary key prefix in both the parent and child tables.
  * Inserting rows into tables with a foreign key relationship between the tables.
  * Other types of related mutations depending on your database schema and application logic.



You can also batch write using the Spanner client libraries. The following code example updates the `Singers` table with new rows.

###  Client libraries 

###  C++ 
    
    
    namespace spanner = ::google::cloud::spanner;
    // Use upserts as mutation groups are not replay protected.
    auto commit_results = client.CommitAtLeastOnce({
        // group #0
        spanner::Mutations{
            spanner::InsertOrUpdateMutationBuilder(
                "Singers", {"SingerId", "FirstName", "LastName"})
                .EmplaceRow(16, "Scarlet", "Terry")
                .Build(),
        },
        // group #1
        spanner::Mutations{
            spanner::InsertOrUpdateMutationBuilder(
                "Singers", {"SingerId", "FirstName", "LastName"})
                .EmplaceRow(17, "Marc", "")
                .EmplaceRow(18, "Catalina", "Smith")
                .Build(),
            spanner::InsertOrUpdateMutationBuilder(
                "Albums", {"SingerId", "AlbumId", "AlbumTitle"})
                .EmplaceRow(17, 1, "Total Junk")
                .EmplaceRow(18, 2, "Go, Go, Go")
                .Build(),
        },
    });
    for (auto& commit_result : commit_results) {
      if (!commit_result) throw std::move(commit_result).status();
      std::cout << "Mutation group indexes [";
      for (auto index : commit_result->indexes) std::cout << " " << index;
      std::cout << " ]: ";
      if (commit_result->commit_timestamp) {
        auto const& ts = *commit_result->commit_timestamp;
        std::cout << "Committed at " << ts.get<absl::Time>().value();
      } else {
        std::cout << commit_result->commit_timestamp.status();
      }
      std::cout << "\n";
    }

### C#
    
    
    // Copyright 2026 Google LLC
    //
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    //     http://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    
    
    using [Google.Cloud.Spanner.Data](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.html);
    using [Google.Rpc](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.html);
    using [Google.Cloud.Spanner.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    using System.Collections.Generic;
    using System.Threading.Tasks;
    
    public class BatchWriteAtLeastOnceAsyncSample
    {
        public async Task BatchWriteAtLeastOnceAsync(string projectId, string instanceId, string databaseId)
        {
            string connectionString = $"Data Source=projects/{projectId}/instances/{instanceId}/databases/{databaseId}";
    
            using var connection = new [SpannerConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html)(connectionString);
            await connection.[OpenAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_OpenAsync_Google_Cloud_Spanner_Data_SpannerTransactionCreationOptions_Google_Cloud_Spanner_Data_SpannerTransactionOptions_System_Threading_CancellationToken_)();
    
            // 1. Create a SpannerBatchWriteCommand.
            var cmd = connection.CreateBatchWriteCommand();
    
            // 2. Create and add mutation groups.
            // Mutation group 1: Insert or update a singer (16).
            var cmdSinger1 = connection.[CreateInsertOrUpdateCommand](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_CreateInsertOrUpdateCommand_System_String_Google_Cloud_Spanner_Data_SpannerParameterCollection_)("Singers", new [SpannerParameterCollection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerParameterCollection.html)
            {
                { "SingerId", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[Int64](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_Int64), 16 },
                { "FirstName", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[String](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_String), "Scarlet" },
                { "LastName", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[String](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_String), "Terry" }
            });
            cmd.Add(cmdSinger1);
    
            // Mutation group 2: Insert or update multiple singers and albums together.
            var cmdSinger2 = connection.[CreateInsertOrUpdateCommand](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_CreateInsertOrUpdateCommand_System_String_Google_Cloud_Spanner_Data_SpannerParameterCollection_)("Singers", new [SpannerParameterCollection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerParameterCollection.html)
            {
                { "SingerId", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[Int64](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_Int64), 17 },
                { "FirstName", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[String](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_String), "Marc" },
                { "LastName", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[String](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_String), "Smith" }
            });
    
            var cmdSinger3 = connection.[CreateInsertOrUpdateCommand](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_CreateInsertOrUpdateCommand_System_String_Google_Cloud_Spanner_Data_SpannerParameterCollection_)("Singers", new [SpannerParameterCollection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerParameterCollection.html)
            {
                { "SingerId", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[Int64](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_Int64), 18 },
                { "FirstName", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[String](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_String), "Catalina" },
                { "LastName", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[String](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_String), "Smith" }
            });
    
            var cmdAlbum1 = connection.[CreateInsertOrUpdateCommand](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_CreateInsertOrUpdateCommand_System_String_Google_Cloud_Spanner_Data_SpannerParameterCollection_)("Albums", new [SpannerParameterCollection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerParameterCollection.html)
            {
                { "SingerId", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[Int64](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_Int64), 17 },
                { "AlbumId", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[Int64](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_Int64), 1 },
                { "AlbumTitle", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[String](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_String), "Total Junk" }
            });
    
            var cmdAlbum2 = connection.[CreateInsertOrUpdateCommand](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_CreateInsertOrUpdateCommand_System_String_Google_Cloud_Spanner_Data_SpannerParameterCollection_)("Albums", new [SpannerParameterCollection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerParameterCollection.html)
            {
                { "SingerId", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[Int64](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_Int64), 18 },
                { "AlbumId", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[Int64](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_Int64), 2 },
                { "AlbumTitle", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[String](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_String), "Go, Go, Go" }
            });
    
            // Add multiple commands to the same group.
            cmd.Add(cmdSinger2, cmdSinger3, cmdAlbum1, cmdAlbum2);
    
            // 3. Execute the batch write request.
            try
            {
                // ExecuteNonQueryAsync returns an IAsyncEnumerable of BatchWriteResponse.
                await foreach (var response in cmd.ExecuteNonQueryAsync())
                {
                    if (response.[Status](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Status.html)?.Code == (int)[Code](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Code.html).[Ok](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Code.html#Google_Rpc_Code_Ok))
                    {
                        Console.WriteLine($"Mutation group indexes {string.Join(", ", response.[Indexes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.BatchWriteResponse.html#Google_Cloud_Spanner_V1_BatchWriteResponse_Indexes))} have been applied with commit timestamp {response.CommitTimestamp}");
                    }
                    else
                    {
                        Console.WriteLine($"Mutation group indexes {string.Join(", ", response.[Indexes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.BatchWriteResponse.html#Google_Cloud_Spanner_V1_BatchWriteResponse_Indexes))} could not be applied with error code {response.[Status](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Status.html)?.Code}");
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error executing batch write: {ex.Message}");
                throw;
            }
        }
    }
    

###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/spanner"
    	sppb "cloud.google.com/go/spanner/apiv1/spannerpb"
    	"google.golang.org/grpc/status"
    )
    
    // batchWrite demonstrates writing mutations to a Spanner database through
    // BatchWrite API - https://pkg.go.dev/cloud.google.com/go/spanner#Client.BatchWrite
    func batchWrite(w io.Writer, db string) error {
    	// db := "projects/my-project/instances/my-instance/databases/my-database"
    	ctx := context.Background()
    	client, err := spanner.NewClient(ctx, db)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	// Database is assumed to exist - https://cloud.google.com/spanner/docs/getting-started/go#create_a_database
    	singerColumns := []string{"SingerId", "FirstName", "LastName"}
    	albumColumns := []string{"SingerId", "AlbumId", "AlbumTitle"}
    	mutationGroups := make([]*spanner.[MutationGroup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_MutationGroup), 2)
    
    	mutationGroup1 := []*spanner.Mutation{
    		spanner.[InsertOrUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Mutation_InsertOrUpdate)("Singers", singerColumns, []interface{}{16, "Scarlet", "Terry"}),
    	}
    	mutationGroups[0] = &spanner.[MutationGroup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_MutationGroup){Mutations: mutationGroup1}
    
    	mutationGroup2 := []*spanner.Mutation{
    		spanner.[InsertOrUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Mutation_InsertOrUpdate)("Singers", singerColumns, []interface{}{17, "Marc", ""}),
    		spanner.[InsertOrUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Mutation_InsertOrUpdate)("Singers", singerColumns, []interface{}{18, "Catalina", "Smith"}),
    		spanner.[InsertOrUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Mutation_InsertOrUpdate)("Albums", albumColumns, []interface{}{17, 1, "Total Junk"}),
    		spanner.[InsertOrUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Mutation_InsertOrUpdate)("Albums", albumColumns, []interface{}{18, 2, "Go, Go, Go"}),
    	}
    	mutationGroups[1] = &spanner.[MutationGroup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_MutationGroup){Mutations: mutationGroup2}
    	iter := client.BatchWrite(ctx, mutationGroups)
    	// See https://pkg.go.dev/cloud.google.com/go/spanner#BatchWriteResponseIterator.Do
    	doFunc := func(response *sppb.BatchWriteResponse) error {
    		if err = status.ErrorProto(response.GetStatus()); err == nil {
    			fmt.Fprintf(w, "Mutation group indexes %v have been applied with commit timestamp %v",
    				response.GetIndexes(), response.GetCommitTimestamp())
    		} else {
    			fmt.Fprintf(w, "Mutation group indexes %v could not be applied with error %v",
    				response.GetIndexes(), err)
    		}
    		// Return an actual error as needed.
    		return nil
    	}
    	return iter.Do(doFunc)
    }
    

###  Java 
    
    
    import com.google.api.gax.rpc.[ServerStream](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStream.html);
    import com.google.cloud.spanner.[DatabaseClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseClient.html);
    import com.google.cloud.spanner.[DatabaseId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseId.html);
    import com.google.cloud.spanner.[Mutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.Mutation.html);
    import com.google.cloud.spanner.[MutationGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.MutationGroup.html);
    import com.google.cloud.spanner.[Options](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Options.html);
    import com.google.cloud.spanner.[Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html);
    import com.google.cloud.spanner.[SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html);
    import com.google.common.collect.ImmutableList;
    import com.google.rpc.[Code](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.Code.html);
    import com.google.spanner.v1.[BatchWriteResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.BatchWriteResponse.html);
    
    public class BatchWriteAtLeastOnceSample {
    
      /***
       * Assume DDL for the underlying database:
       * <pre>{@code
       *   CREATE TABLE Singers (
       *     SingerId   INT64 NOT NULL,
       *     FirstName  STRING(1024),
       *     LastName   STRING(1024),
       *   ) PRIMARY KEY (SingerId)
       *
       *   CREATE TABLE Albums (
       *     SingerId     INT64 NOT NULL,
       *     AlbumId      INT64 NOT NULL,
       *     AlbumTitle   STRING(1024),
       *   ) PRIMARY KEY (SingerId, AlbumId),
       *   INTERLEAVE IN PARENT Singers ON DELETE CASCADE
       * }</pre>
       */
    
      private static final [MutationGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.MutationGroup.html) MUTATION_GROUP1 =
          [MutationGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.MutationGroup.html).of(
              [Mutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.Mutation.html).[newInsertOrUpdateBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Mutation.html#com_google_cloud_spanner_Mutation_newInsertOrUpdateBuilder_java_lang_String_)("Singers")
                  .set("SingerId")
                  .[to](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.ValueBinder.html#com_google_cloud_spanner_ValueBinder_to_boolean_)(16)
                  .set("FirstName")
                  .[to](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.ValueBinder.html#com_google_cloud_spanner_ValueBinder_to_boolean_)("Scarlet")
                  .set("LastName")
                  .[to](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.ValueBinder.html#com_google_cloud_spanner_ValueBinder_to_boolean_)("Terry")
                  .build());
      private static final [MutationGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.MutationGroup.html) MUTATION_GROUP2 =
          [MutationGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.MutationGroup.html).of(
              [Mutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.Mutation.html).[newInsertOrUpdateBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Mutation.html#com_google_cloud_spanner_Mutation_newInsertOrUpdateBuilder_java_lang_String_)("Singers")
                  .set("SingerId")
                  .[to](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.ValueBinder.html#com_google_cloud_spanner_ValueBinder_to_boolean_)(17)
                  .set("FirstName")
                  .[to](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.ValueBinder.html#com_google_cloud_spanner_ValueBinder_to_boolean_)("Marc")
                  .build(),
              [Mutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.Mutation.html).[newInsertOrUpdateBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Mutation.html#com_google_cloud_spanner_Mutation_newInsertOrUpdateBuilder_java_lang_String_)("Singers")
                  .set("SingerId")
                  .[to](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.ValueBinder.html#com_google_cloud_spanner_ValueBinder_to_boolean_)(18)
                  .set("FirstName")
                  .[to](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.ValueBinder.html#com_google_cloud_spanner_ValueBinder_to_boolean_)("Catalina")
                  .set("LastName")
                  .[to](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.ValueBinder.html#com_google_cloud_spanner_ValueBinder_to_boolean_)("Smith")
                  .build(),
              [Mutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.Mutation.html).[newInsertOrUpdateBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Mutation.html#com_google_cloud_spanner_Mutation_newInsertOrUpdateBuilder_java_lang_String_)("Albums")
                  .set("SingerId")
                  .[to](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.ValueBinder.html#com_google_cloud_spanner_ValueBinder_to_boolean_)(17)
                  .set("AlbumId")
                  .[to](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.ValueBinder.html#com_google_cloud_spanner_ValueBinder_to_boolean_)(1)
                  .set("AlbumTitle")
                  .[to](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.ValueBinder.html#com_google_cloud_spanner_ValueBinder_to_boolean_)("Total Junk")
                  .build(),
              [Mutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.Mutation.html).[newInsertOrUpdateBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Mutation.html#com_google_cloud_spanner_Mutation_newInsertOrUpdateBuilder_java_lang_String_)("Albums")
                  .set("SingerId")
                  .[to](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.ValueBinder.html#com_google_cloud_spanner_ValueBinder_to_boolean_)(18)
                  .set("AlbumId")
                  .[to](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.ValueBinder.html#com_google_cloud_spanner_ValueBinder_to_boolean_)(2)
                  .set("AlbumTitle")
                  .[to](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.ValueBinder.html#com_google_cloud_spanner_ValueBinder_to_boolean_)("Go, Go, Go")
                  .build());
    
      static void batchWriteAtLeastOnce() {
        // TODO(developer): Replace these variables before running the sample.
        final String projectId = "my-project";
        final String instanceId = "my-instance";
        final String databaseId = "my-database";
        batchWriteAtLeastOnce(projectId, instanceId, databaseId);
      }
    
      static void batchWriteAtLeastOnce(String projectId, String instanceId, String databaseId) {
        try ([Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html) spanner =
            [SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html).newBuilder().setProjectId(projectId).build().getService()) {
          [DatabaseId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseId.html) dbId = [DatabaseId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseId.html).of(projectId, instanceId, databaseId);
          final [DatabaseClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseClient.html) dbClient = spanner.getDatabaseClient(dbId);
    
          // Creates and issues a BatchWrite RPC request that will apply the mutation groups
          // non-atomically and respond back with a stream of BatchWriteResponse.
          ServerStream<BatchWriteResponse> responses =
              dbClient.[batchWriteAtLeastOnce](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseClient.html#com_google_cloud_spanner_DatabaseClient_batchWriteAtLeastOnce_java_lang_Iterable_com_google_cloud_spanner_MutationGroup__com_google_cloud_spanner_Options_TransactionOption____)(
                  ImmutableList.of(MUTATION_GROUP1, MUTATION_GROUP2),
                  Options.tag("batch-write-tag"));
    
          // Iterates through the results in the stream response and prints the MutationGroup indexes,
          // commit timestamp and status.
          for ([BatchWriteResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.BatchWriteResponse.html) response : responses) {
            if (response.getStatus().getCode() == [Code](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.Code.html).OK_VALUE) {
              System.out.printf(
                  "Mutation group indexes %s have been applied with commit timestamp %s",
                  response.getIndexesList(), response.getCommitTimestamp());
            } else {
              System.out.printf(
                  "Mutation group indexes %s could not be applied with error code %s and "
                      + "error message %s", response.getIndexesList(),
                  [Code](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.Code.html).forNumber(response.getStatus().getCode()), response.getStatus().getMessage());
            }
          }
        }
      }
    }
    

###  Node 
    
    
    // Imports the Google Cloud client library
    const {Spanner, MutationGroup} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const instanceId = 'my-instance';
    // const databaseId = 'my-database';
    // const projectId = 'my-project-id';
    
    // Creates a client
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({
      projectId: projectId,
    });
    
    // Gets a reference to a Cloud Spanner instance and database
    const instance = spanner.instance(instanceId);
    const database = instance.database(databaseId);
    
    // Create Mutation Groups
    /**
     * Related mutations should be placed in a group, such as insert mutations for both a parent and a child row.
     * A group must contain related mutations.
     * Please see {@link https://cloud.google.com/spanner/docs/reference/rpc/google.spanner.v1#google.spanner.v1.BatchWriteRequest.MutationGroup}
     * for more details and examples.
     */
    const mutationGroup1 = new [MutationGroup](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/mutationgroup.html)();
    mutationGroup1.insert('Singers', {
      SingerId: 1,
      FirstName: 'Scarlet',
      LastName: 'Terry',
    });
    
    const mutationGroup2 = new [MutationGroup](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/mutationgroup.html)();
    mutationGroup2.insert('Singers', {
      SingerId: 2,
      FirstName: 'Marc',
    });
    mutationGroup2.insert('Singers', {
      SingerId: 3,
      FirstName: 'Catalina',
      LastName: 'Smith',
    });
    mutationGroup2.insert('Albums', {
      AlbumId: 1,
      SingerId: 2,
      AlbumTitle: 'Total Junk',
    });
    mutationGroup2.insert('Albums', {
      AlbumId: 2,
      SingerId: 3,
      AlbumTitle: 'Go, Go, Go',
    });
    
    const options = {
      transactionTag: 'batch-write-tag',
    };
    
    try {
      database
        .[batchWriteAtLeastOnce](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/database.html)([mutationGroup1, mutationGroup2], options)
        .on('error', console.error)
        .on('data', response => {
          // Check the response code of each response to determine whether the mutation group(s) were applied successfully.
          if (response.status.code === 0) {
            console.log(
              `Mutation group indexes ${
                response.indexes
              }, have been applied with commit timestamp ${Spanner.timestamp(
                response.commitTimestamp,
              ).toJSON()}`,
            );
          }
          // Mutation groups that fail to commit trigger a response with a non-zero status code.
          else {
            console.log(
              `Mutation group indexes ${response.indexes}, could not be applied with error code ${response.status.code}, and error message ${response.status.message}`,
            );
          }
        })
        .on('end', () => {
          console.log('Request completed successfully');
        });
    } catch (err) {
      console.log(err);
    }

### PHP
    
    
    <?php
    /**
     * Copyright 2026 Google Inc.
     *
     * Licensed under the Apache License, Version 2.0 (the "License");
     * you may not use this file except in compliance with the License.
     * You may obtain a copy of the License at
     *
     *     http://www.apache.org/licenses/LICENSE-2.0
     *
     * Unless required by applicable law or agreed to in writing, software
     * distributed under the License is distributed on an "AS IS" BASIS,
     * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     * See the License for the specific language governing permissions and
     * limitations under the License.
     */
    
    /**
     * For instructions on how to run the full sample:
     *
     * @see https://github.com/GoogleCloudPlatform/php-docs-samples/tree/main/spanner/README.md
     */
    
    namespace Google\Cloud\Samples\Spanner;
    
    use Google\Cloud\Spanner\SpannerClient;
    
    /**
     * Inserts sample data into the given database via BatchWrite API.
     * The database and table must already exist and can be created using `create_database`.
     *
     * Example:
     * ```
     * batch_write($projectId, $instanceId, $databaseId);
     * ```
     *
     * @param string $projectId The Google Cloud project ID.
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     */
    function batch_write(string $projectId, string $instanceId, string $databaseId): void
    {
        $spanner = new SpannerClient(['projectId' => $projectId]);
        $database = $spanner->instance($instanceId)->database($databaseId);
    
        // Create Mutation Groups
        // All mutations within a single group are applied atomically.
        // Mutations across groups are applied non-atomically.
    
        // Group 1: Single mutation
        $mutationGroup1 = $database->mutationGroup();
        $mutationGroup1->insertOrUpdate('Singers', [
            'SingerId' => 16,
            'FirstName' => 'Scarlet',
            'LastName' => 'Terry'
        ]);
    
        // Group 2: Multiple mutations
        $mutationGroup2 = $database->mutationGroup();
        $mutationGroup2->insertOrUpdateBatch('Singers', [
            ['SingerId' => 17, 'FirstName' => 'Marc'],
            ['SingerId' => 18, 'FirstName' => 'Catalina', 'LastName' => 'Smith']
        ]);
        $mutationGroup2->insertOrUpdateBatch('Albums', [
            ['SingerId' => 17, 'AlbumId' => 1, 'AlbumTitle' => 'Total Junk'],
            ['SingerId' => 18, 'AlbumId' => 2, 'AlbumTitle' => 'Go, Go, Go']
        ]);
    
        // Call batchWrite on the high-level Database client.
        // Equivalent to batchWriteAtLeastOnce in other languages.
        $responses = $database->batchWrite([$mutationGroup1, $mutationGroup2], [
            'requestOptions' => ['transactionTag' => 'batch-write-tag']
        ]);
    
        // Check the response code of each response to determine whether the mutation group(s) were applied successfully.
        // $responses is a Generator yielding V1\BatchWriteResponse items.
        // Check the response code of each response to determine whether the mutation group(s) were applied successfully.
        // $responses is a Generator yielding response arrays.
        foreach ($responses as $response) {
            $status = $response['status'];
            $indexes = implode(', ', $response['indexes']);
            if ($status['code'] === 0) {
                $timestamp = $response['commitTimestamp'] ?? 'Unknown';
                printf('Mutation group indexes [%s] have been applied with commit timestamp %s' . PHP_EOL,
                    $indexes,
                    $timestamp
                );
            } else {
                printf('Mutation group indexes [%s] could not be applied with error code %s and error message %s' . PHP_EOL,
                    $indexes,
                    $status['code'],
                    $status['message']
                );
            }
        }
    }
    
    // The following 2 lines are only needed to run the samples
    require_once __DIR__ . '/../../testing/sample_helpers.php';
    \Google\Cloud\Samples\execute_sample(__FILE__, __NAMESPACE__, $argv);
    

###  Python 
    
    
    def batch_write(instance_id, database_id):
        """Inserts sample data into the given database via BatchWrite API.
    
        The database and table must already exist and can be created using
        `create_database`.
        """
        from google.rpc.code_pb2 import OK
    
        spanner_client = spanner.Client()
        instance = spanner_client.instance(instance_id)
        database = instance.database(database_id)
    
        with database.mutation_groups() as groups:
            group1 = groups.group()
            group1.insert_or_update(
                table="Singers",
                columns=("SingerId", "FirstName", "LastName"),
                values=[
                    (16, "Scarlet", "Terry"),
                ],
            )
    
            group2 = groups.group()
            group2.insert_or_update(
                table="Singers",
                columns=("SingerId", "FirstName", "LastName"),
                values=[
                    (17, "Marc", ""),
                    (18, "Catalina", "Smith"),
                ],
            )
            group2.insert_or_update(
                table="Albums",
                columns=("SingerId", "AlbumId", "AlbumTitle"),
                values=[
                    (17, 1, "Total Junk"),
                    (18, 2, "Go, Go, Go"),
                ],
            )
    
            for response in groups.batch_write():
                if response.status.code == OK:
                    print(
                        "Mutation group indexes {} have been applied with commit timestamp {}".format(
                            response.indexes, response.commit_timestamp
                        )
                    )
                else:
                    print(
                        "Mutation group indexes {} could not be applied with error {}".format(
                            response.indexes, response.status
                        )
                    )
    
    

### Ruby
    
    
    require "google/cloud/spanner"
    
    ##
    # This is a snippet for showcasing how to apply a batch of mutations groups.
    # All mutations in a group are applied atomically.
    #
    # @param project_id  [String] The ID of the Google Cloud project.
    # @param instance_id [String] The ID of the spanner instance.
    # @param database_id [String] The ID of the database.
    #
    def spanner_batch_write project_id:, instance_id:, database_id:
      spanner = Google::Cloud::[Spanner](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-instance-v1/latest/Google-Cloud-Spanner.html).new project: project_id
      client  = spanner.[client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Project.html) instance_id, database_id
    
      results = client.batch_write do |b|
        # First mutation group
        b.[mutation_group](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-BatchWrite.html) do |mg|
          mg.upsert "Singers", [{ SingerId: 16, FirstName: "Scarlet", LastName: "Terry" }]
        end
    
        # Second mutation group
        b.[mutation_group](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-BatchWrite.html) do |mg|
          mg.upsert "Singers", [
            { SingerId: 17, FirstName: "Marc" },
            { SingerId: 18, FirstName: "Catalina", LastName: "Smith" }
          ]
          mg.upsert "Albums", [
            { SingerId: 17, AlbumId: 1, AlbumTitle: "Total Junk" },
            { SingerId: 18, AlbumId: 2, AlbumTitle: "Go, Go, Go" }
          ]
        end
      end
    
      results.[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-BatchWriteResults.html) do |response|
        if response.ok?
          puts "Mutation group indexes applied: #{response.indexes}"
        else
          puts "Mutation group failed to apply: #{response.indexes}"
          puts "Error: #{response.status.[message](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Status.html)}"
        end
      end
    end

## What's next

  * Learn more about [Spanner transactions](https://docs.cloud.google.com/spanner/docs/transactions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
