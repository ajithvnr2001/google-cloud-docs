---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-list-column-families/
title: List column families \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:23:56.241975+00:00
---

# List column families  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-list-column-families/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  List column families Stay organized with collections  Save and categorize content based on your preferences. 

List column families.

## Code sample

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    namespace cbta = ::google::cloud::bigtable_admin;
    using ::google::cloud::StatusOr;
    [](cbta::BigtableTableAdminClient admin, std::string const& project_id,
       std::string const& instance_id, std::string const& table_id) {
      std::string table_name = cbt::TableName(project_id, instance_id, table_id);
    
      google::bigtable::admin::v2::GetTableRequest r;
      r.set_name(table_name);
      r.set_view(google::bigtable::admin::v2::Table::FULL);
    
      StatusOr<google::bigtable::admin::v2::Table> schema =
          admin.GetTable(std::move(r));
    
      if (!schema) throw std::move(schema).status();
      for (auto const& kv : schema->column_families()) {
        std::string const& column_family_name = kv.first;
        google::bigtable::admin::v2::ColumnFamily const& family = kv.second;
        std::cout << "Column family name: " << column_family_name << "\n"
                  << "Column family metadata: " << family.DebugString() << "\n";
      }
    }

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Lists all families in the table with GC rules.
    try {
      String tableName =
          "projects/" + projectId + "/instances/" + instanceId + "/tables/" + tableId;
      Table table = adminClient.getTable(tableName);
      for (Map.Entry<String, ColumnFamily> entry : table.getColumnFamiliesMap().entrySet()) {
        System.out.printf(
            "Column family: %s%nGC Rule: %s%n", entry.getKey(), entry.getValue().getGcRule());
      }
    } catch (NotFoundException e) {
      System.err.println(
          "Failed to list column families from a non-existent table: " + e.getMessage());
    }

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\GetTableRequest;
    
    /**
     * List column families of a table
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table for which the families need to be displayed
     */
    function list_column_families(
        string $projectId,
        string $instanceId,
        string $tableId
    ): void {
        $tableAdminClient = new BigtableTableAdminClient();
    
        $tableName = $tableAdminClient->tableName($projectId, $instanceId, $tableId);
        $getTableRequest = (new GetTableRequest())
            ->setName($tableName);
    
        $table = $tableAdminClient->getTable($getTableRequest);
        $columnFamilies = $table->getColumnFamilies()->getIterator();
    
        foreach ($columnFamilies as $k => $columnFamily) {
            printf('Column Family: %s' . PHP_EOL, $k);
            print('GC Rule:' . PHP_EOL);
            printf('%s' . PHP_EOL, $columnFamily->serializeToJsonString());
        }
    }

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    print("Printing Column Family and GC Rule for all column families...")
    column_families = table.list_column_families()
    for column_family_name, gc_rule in sorted(column_families.items()):
        print("Column Family:", column_family_name)
        print("GC Rule:")
        print(gc_rule.to_pb())
        # Sample output:
        #         Column Family: cf4
        #         GC Rule:
        #         gc_rule {
        #           intersection {
        #             rules {
        #               max_age {
        #                 seconds: 432000
        #               }
        #             }
        #             rules {
        #               max_num_versions: 2
        #             }
        #           }
        #         }
    

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    table = bigtable.table(
      instance_id,
      table_id,
      view:           :FULL,
      perform_lookup: true
    )
    table.column_families.each do |name, family|
      puts "Column family name: #{name}"
      puts "GC Rule:"
      p family.gc_rule
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
