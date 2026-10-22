---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-writes-conditional/
title: Conditionally write a value \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:02.518145+00:00
---

# Conditionally write a value  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-writes-conditional/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Conditionally write a value Stay organized with collections  Save and categorize content based on your preferences. 

Send a conditional write request. This type of write makes a CheckAndMutateRow API request.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Write examples](https://docs.cloud.google.com/bigtable/docs/writing-data)



## Code sample

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    [](cbt::Table table) {
      auto timestamp = std::chrono::duration_cast<std::chrono::milliseconds>(
          std::chrono::system_clock::now().time_since_epoch());
    
      std::string row_key = "phone#4c410523#20190501";
      cbt::SingleRowMutation mutation(row_key);
      std::string column_family = "stats_summary";
      cbt::Filter predicate = cbt::Filter::Chain(
          cbt::Filter::ColumnName(column_family, "os_build"),
          cbt::Filter::Latest(1), cbt::Filter::ValueRegex("PQ2A\\..*"));
    
      google::cloud::StatusOr<cbt::MutationBranch> branch =
          table.CheckAndMutateRow(
              row_key, std::move(predicate),
              {cbt::SetCell(column_family, "os_name", timestamp, "android")}, {});
    
      if (!branch) throw std::move(branch).status();
      if (*branch == cbt::MutationBranch::kPredicateMatched) {
        std::cout << "Successfully updated row\n";
      } else {
        std::cout << "The predicate was not matched\n";
      }
    }

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using [Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.html);
    using [Google.Cloud.Bigtable.Common.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.html);
    
    namespace Writes
    {
        public class WriteConditionalSample
        {
            /// <summary>
            /// Check if a row has a certain value then mutate the row if it does.
            ///</summary>
            /// <param name="projectId">Your Google Cloud Project ID.</param>
            /// <param name="instanceId">Your Google Cloud Bigtable Instance ID.</param>
            /// <param name="tableId">Your Google Cloud Bigtable table ID.</param>
            public string WriteConditional(
                string projectId = "YOUR-PROJECT-ID",
                string instanceId = "YOUR-INSTANCE-ID",
                string tableId = "YOUR-TABLE-ID")
            {
                [BigtableClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient.html) bigtableClient = [BigtableClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient.html#Google_Cloud_Bigtable_V2_BigtableClient_Create)();
    
                [TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html) tableName = new [TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)(projectId, instanceId, tableId);
                [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html) rowkey = new [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)("phone#4c410523#20190501");
                [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion.html) timestamp = new [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion.html)(DateTime.UtcNow);
                string COLUMN_FAMILY = "stats_summary";
    
                [CheckAndMutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowResponse.html) checkAndMutateRowResponse = bigtableClient.[CheckAndMutateRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient.html#Google_Cloud_Bigtable_V2_BigtableClient_CheckAndMutateRow_Google_Cloud_Bigtable_Common_V2_TableName_Google_Cloud_Bigtable_Common_V2_BigtableByteString_Google_Cloud_Bigtable_V2_RowFilter_Google_Cloud_Bigtable_V2_Mutation___)(
                    tableName,
                    rowkey,
                    [RowFilters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilters.html).[Chain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilters.html#Google_Cloud_Bigtable_V2_RowFilters_Chain_Google_Cloud_Bigtable_V2_RowFilter___)(
                        [RowFilters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilters.html).[FamilyNameExact](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilters.html#Google_Cloud_Bigtable_V2_RowFilters_FamilyNameExact_System_String_)(COLUMN_FAMILY),
                        [RowFilters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilters.html).[ColumnQualifierExact](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilters.html#Google_Cloud_Bigtable_V2_RowFilters_ColumnQualifierExact_Google_Cloud_Bigtable_Common_V2_BigtableByteString_)("os_build"),
                        [RowFilters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilters.html).[ValueRegex](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilters.html#Google_Cloud_Bigtable_V2_RowFilters_ValueRegex_System_String_)("PQ2A\\..*")),
                    [Mutations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutations.html).[SetCell](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutations.html#Google_Cloud_Bigtable_V2_Mutations_SetCell_System_String_Google_Cloud_Bigtable_Common_V2_BigtableByteString_Google_Cloud_Bigtable_Common_V2_BigtableByteString_System_Nullable_Google_Cloud_Bigtable_V2_BigtableVersion__)(COLUMN_FAMILY, "os_name", "android", timestamp));
    
                return $"Successfully updated row's os_name: {checkAndMutateRowResponse.[PredicateMatched](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowResponse.html#Google_Cloud_Bigtable_V2_CheckAndMutateRowResponse_PredicateMatched)}";
            }
        }
    }

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/bigtable"
    )
    
    func writeConditionally(w io.Writer, projectID, instanceID string, tableName string) error {
    	// projectID := "my-project-id"
    	// instanceID := "my-instance-id"
    	// tableName := "mobile-time-series"
    
    	ctx := context.Background()
    	client, err := bigtable.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Client_NewClient)(ctx, projectID, instanceID)
    	if err != nil {
    		return fmt.Errorf("bigtable.NewAdminClient: %w", err)
    	}
    	defer client.Close()
    	tbl := client.[Open](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Client_Open)(tableName)
    	columnFamilyName := "stats_summary"
    	timestamp := bigtable.[Now](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Timestamp_Now)()
    
    	mut := bigtable.[NewMutation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Mutation_NewMutation)()
    	mut.[Set](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Mutation_Set)(columnFamilyName, "os_name", timestamp, []byte("android"))
    
    	filter := bigtable.[ChainFilters](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Filter_ChainFilters)(
    		bigtable.[FamilyFilter](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Filter_FamilyFilter)(columnFamilyName),
    		bigtable.[ColumnFilter](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Filter_ColumnFilter)("os_build"),
    		bigtable.[ValueFilter](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Filter_ValueFilter)("PQ2A\\..*"))
    	conditionalMutation := bigtable.[NewCondMutation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Mutation_NewCondMutation)(filter, mut, nil)
    
    	rowKey := "phone#4c410523#20190501"
    	if err := tbl.Apply(ctx, rowKey, conditionalMutation); err != nil {
    		return fmt.Errorf("Apply: %w", err)
    	}
    
    	fmt.Fprintln(w, "Successfully updated row's os_name")
    	return nil
    }
    

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import static com.google.cloud.bigtable.data.v2.models.[Filters](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Filters.html).FILTERS;
    
    import com.google.cloud.bigtable.data.v2.[BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html);
    import com.google.cloud.bigtable.data.v2.models.[ConditionalRowMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.ConditionalRowMutation.html);
    import com.google.cloud.bigtable.data.v2.models.[Filters](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Filters.html).Filter;
    import com.google.cloud.bigtable.data.v2.models.[Mutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Mutation.html);
    import com.google.cloud.bigtable.data.v2.models.[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TableId.html);
    
    public class WriteConditionally {
      private static final String COLUMN_FAMILY_NAME = "stats_summary";
    
      public static void writeConditionally(String projectId, String instanceId, String tableId) {
        // String projectId = "my-project-id";
        // String instanceId = "my-instance-id";
        // String tableId = "mobile-time-series";
    
        try ([BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html) dataClient = [BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html).create(projectId, instanceId)) {
          long timestamp = System.currentTimeMillis() * 1000;
    
          String rowkey = "phone#4c410523#20190501";
    
          [Mutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Mutation.html) mutation =
              [Mutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Mutation.html).create().setCell(COLUMN_FAMILY_NAME, "os_name", timestamp, "android");
    
          Filter filter =
              FILTERS
                  .chain()
                  .filter(FILTERS.family().exactMatch(COLUMN_FAMILY_NAME))
                  .filter(FILTERS.qualifier().exactMatch("os_build"))
                  .filter(FILTERS.value().regex("PQ2A\\..*"));
    
          [ConditionalRowMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.ConditionalRowMutation.html) conditionalRowMutation =
              [ConditionalRowMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.ConditionalRowMutation.html).create([TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TableId.html).of(tableId), rowkey)
                  .condition(filter)
                  .then(mutation);
    
          boolean success = dataClient.[checkAndMutateRow](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_checkAndMutateRow_com_google_cloud_bigtable_data_v2_models_ConditionalRowMutation_)(conditionalRowMutation);
    
          System.out.printf("Successfully updated row's os_name: %b", success);
    
        } catch (Exception e) {
          System.out.println("Error during WriteConditionally: \n" + e.toString());
          e.printStackTrace();
        }
      }
    }
    

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    use Google\Cloud\Bigtable\Filter;
    use Google\Cloud\Bigtable\Mutations;
    
    /**
     * Write data conditionally in a table
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table where the data needs to be written
     */
    function write_conditionally(
        string $projectId,
        string $instanceId,
        string $tableId = 'mobile-time-series'
    ): void {
        // Connect to an existing table with an existing instance.
        $dataClient = new BigtableClient([
            'projectId' => $projectId,
        ]);
        $table = $dataClient->table($instanceId, $tableId);
    
        $timestampMicros = time() * 1000 * 1000;
        $columnFamilyId = 'stats_summary';
    
        $mutations = (new Mutations())->upsert($columnFamilyId, 'os_name', 'android', $timestampMicros);
        $predicateFilter = Filter::chain()
        ->addFilter(Filter::family()->exactMatch($columnFamilyId))
        ->addFilter(Filter::qualifier()->exactMatch('os_build'))
        ->addFilter(Filter::value()->regex('PQ2A.*'));
        $options = ['predicateFilter' => $predicateFilter, 'trueMutations' => $mutations];
    
        $table->checkAndMutateRow('phone#4c410523#20190501', $options);
    
        printf('Successfully updated row\'s os_name' . PHP_EOL);
    }

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from datetime import datetime, timezone
    
    from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
    from google.cloud.bigtable import row_filters
    
    
    def write_conditional(project_id, instance_id, table_id):
        client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
    
        timestamp = datetime.now(timezone.utc)
        column_family_id = "stats_summary"
    
        row_key = "phone#4c410523#20190501"
    
        row_filter = row_filters.RowFilterChain(
            filters=[
                row_filters.FamilyNameRegexFilter(column_family_id),
                row_filters.ColumnQualifierRegexFilter("os_build"),
                row_filters.ValueRegexFilter("PQ2A\\..*"),
            ]
        )
        row = table.[conditional_row](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.table.Table.html#google_cloud_bigtable_table_Table_conditional_row)(row_key, filter_=row_filter)
        row.set_cell(column_family_id, "os_name", "android", timestamp)
        row.commit()
    
        print("Successfully updated row's os_name.")
    
    

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # instance_id = "my-instance"
    # table_id    = "my-table"
    table = bigtable.table instance_id, table_id
    column_family = "stats_summary"
    timestamp = (Time.now.to_f * 1_000_000).round(-3)
    
    rowkey = "phone#4c410523#20190501"
    predicate_filter = Google::Cloud::Bigtable::RowFilter.chain
                                                         .family(column_family)
                                                         .qualifier("os_build")
                                                         .value("PQ2A\\..*")
    
    on_match_mutations = Google::Cloud::Bigtable::MutationEntry.new
    on_match_mutations.set_cell(
      column_family,
      "os_name",
      "android",
      timestamp: timestamp
    )
    
    response = table.check_and_mutate_row(
      rowkey,
      predicate_filter,
      on_match: on_match_mutations
    )
    
    puts "Successfully updated row's os_name: #{response}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
