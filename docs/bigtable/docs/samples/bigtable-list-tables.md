---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-list-tables/
title: List tables \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:23:56.918677+00:00
---

# List tables  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-list-tables/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  List tables Stay organized with collections  Save and categorize content based on your preferences. 

List all tables in a Cloud Bigtable instance.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and manage tables](https://docs.cloud.google.com/bigtable/docs/managing-tables)



## Code sample

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    namespace cbta = ::google::cloud::bigtable_admin;
    using ::google::cloud::StreamRange;
    [](cbta::BigtableTableAdminClient admin, std::string const& project_id,
       std::string const& instance_id) {
      std::string instance_name = cbt::InstanceName(project_id, instance_id);
    
      google::bigtable::admin::v2::ListTablesRequest r;
      r.set_parent(instance_name);
      r.set_view(google::bigtable::admin::v2::Table::NAME_ONLY);
    
      StreamRange<google::bigtable::admin::v2::Table> tables =
          admin.ListTables(std::move(r));
      for (auto& table : tables) {
        if (!table) throw std::move(table).status();
        std::cout << table->name() << "\n";
      }
    }

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Lists tables in intance.
    // Initialize request argument(s).
    ListTablesRequest request = new ListTablesRequest
    {
        ParentAsInstanceName = s_instanceName
    };
    try
    {
        // Make the request.
        PagedEnumerable<ListTablesResponse, Table> response = bigtableTableAdminClient.ListTables(request);
    
    }
    catch (Exception ex)
    {
        Console.WriteLine($"Error listing tables {ex.Message}");
    }

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Lists tables in the current instance.
    try {
      String parent = "projects/" + projectId + "/instances/" + instanceId;
      ListTablesRequest request = ListTablesRequest.newBuilder().setParent(parent).build();
      for (Table table : adminClient.listTables(request).iterateAll()) {
        System.out.println(table.getName());
      }
    } catch (NotFoundException e) {
      System.err.println("Failed to list tables from a non-existent instance: " + e.getMessage());
    }

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\ListTablesRequest;
    
    /**
     * List tables in an instance
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     */
    function list_tables(
        string $projectId,
        string $instanceId
    ): void {
        $instanceAdminClient = new BigtableInstanceAdminClient();
        $tableAdminClient = new BigtableTableAdminClient();
    
        $instanceName = $instanceAdminClient->instanceName($projectId, $instanceId);
    
        printf('Listing Tables:' . PHP_EOL);
        $listTablesRequest = (new ListTablesRequest())
            ->setParent($instanceName);
        $tables = $tableAdminClient->listTables($listTablesRequest)->iterateAllElements();
        $tables = iterator_to_array($tables);
        if (empty($tables)) {
            print('No table exists.' . PHP_EOL);
            return;
        }
        foreach ($tables as $table) {
            print($table->getName() . PHP_EOL);
        }
    }

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    tables = instance.list_tables()
    print("Listing tables in current project...")
    if tables != []:
        for tbl in tables:
            print(tbl.table_id)
    else:
        print("No table exists in current project...")
    

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # instance_id = "my-instance"
    bigtable.tables(instance_id).all.each do |t|
      puts "Table: #{t.name}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
