---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-hw-create-table/
title: Create a table \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:53.374995+00:00
---

# Create a table  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-hw-create-table/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Create a table Stay organized with collections  Save and categorize content based on your preferences. 

Create a table with a "Hello World" application.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [C# hello world](https://docs.cloud.google.com/bigtable/docs/samples-c-sharp-hello)
  * [C++ hello world](https://docs.cloud.google.com/bigtable/docs/samples-cpp-hello)
  * [Go hello world](https://docs.cloud.google.com/bigtable/docs/samples-go-hello)
  * [Java hello world](https://docs.cloud.google.com/bigtable/docs/samples-java-hello-world)
  * [Node.js hello world](https://docs.cloud.google.com/bigtable/docs/samples-nodejs-hello)
  * [PHP hello world](https://docs.cloud.google.com/bigtable/docs/samples-php-hello)
  * [Python hello world](https://docs.cloud.google.com/bigtable/docs/samples-python-hello)
  * [Ruby hello world](https://docs.cloud.google.com/bigtable/docs/samples-ruby-hello)



## Code sample

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Define the desired schema for the Table.
    google::bigtable::admin::v2::Table t;
    auto& families = *t.mutable_column_families();
    families["family"].mutable_gc_rule()->set_max_num_versions(1);
    
    // Create a table.
    std::string instance_name = cbt::InstanceName(project_id, instance_id);
    StatusOr<google::bigtable::admin::v2::Table> schema =
        table_admin.CreateTable(instance_name, table_id, std::move(t));

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Create a table with a single column family.
    Console.WriteLine($"Create new table: {tableId} with column family: {columnFamily}, instance: {instanceId}");
    
    // Check whether a table with given TableName already exists.
    if (!TableExist(bigtableTableAdminClient))
    {
        bigtableTableAdminClient.CreateTable(
            new InstanceName(projectId, instanceId),
            tableId,
            new Table
            {
                Granularity = Table.Types.TimestampGranularity.Millis,
                ColumnFamilies =
                {
                    {
                        columnFamily, new ColumnFamily
                        {
                            GcRule = new GcRule
                            {
                                MaxNumVersions = 1
                            }
                        }
                    }
                }
            });
        // Confirm that table was created successfully.
        Console.WriteLine(TableExist(bigtableTableAdminClient)
            ? $"Table {tableId} created successfully\n"
            : $"There was a problem creating a table {tableId}");
    }
    else
    {
        Console.WriteLine($"Table: {tableId} already exists");
    }

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    tables, err := adminClient.Tables(ctx)
    if err != nil {
    	log.Fatalf("Could not fetch table list: %v", err)
    }
    
    if !sliceContains(tables, tableName) {
    	log.Printf("Creating table %s", tableName)
    	if err := adminClient.CreateTable(ctx, tableName); err != nil {
    		log.Fatalf("Could not create table %s: %v", tableName, err)
    	}
    }
    
    tblInfo, err := adminClient.TableInfo(ctx, tableName)
    if err != nil {
    	log.Fatalf("Could not read info for table %s: %v", tableName, err)
    }
    
    if !sliceContains(tblInfo.Families, columnFamilyName) {
    	if err := adminClient.CreateColumnFamily(ctx, tableName, columnFamilyName); err != nil {
    		log.Fatalf("Could not create column family %s: %v", columnFamilyName, err)
    	}
    }

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Checks if table exists, creates table if does not exist.
    boolean exists = false;
    try {
      adminClient.getTable(
          GetTableRequest.newBuilder()
              .setName("projects/" + projectId + "/instances/" + instanceId + "/tables/" + tableId)
              .setView(Table.View.NAME_ONLY)
              .build());
      exists = true;
    } catch (NotFoundException e) {
      // ignore
    }
    if (!exists) {
      System.out.println("Creating table: " + tableId);
      String parent = "projects/" + projectId + "/instances/" + instanceId;
      CreateTableRequest request =
          CreateTableRequest.newBuilder()
              .setParent(parent)
              .setTableId(tableId)
              .setTable(
                  Table.newBuilder()
                      .putColumnFamilies(COLUMN_FAMILY, ColumnFamily.getDefaultInstance())
                      .build())
              .build();
      adminClient.createTable(request);
      System.out.printf("Table %s created successfully%n", tableId);
    }

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $instanceName = $instanceAdminClient->instanceName($projectId, $instanceId);
    $tableName = $tableAdminClient->tableName($projectId, $instanceId, $tableId);
    
    // Check whether table exists in an instance.
    // Create table if it does not exists.
    $table = new Table();
    printf('Creating a Table: %s' . PHP_EOL, $tableId);
    
    try {
        $getTableRequest = (new GetTableRequest())
            ->setName($tableName)
            ->setView(View::NAME_ONLY);
        $tableAdminClient->getTable($getTableRequest);
        printf('Table %s already exists' . PHP_EOL, $tableId);
    } catch (ApiException $e) {
        if ($e->getStatus() === 'NOT_FOUND') {
            printf('Creating the %s table' . PHP_EOL, $tableId);
            $createTableRequest = (new CreateTableRequest())
                ->setParent($instanceName)
                ->setTableId($tableId)
                ->setTable($table);
    
            $tableAdminClient->createtable($createTableRequest);
            $columnFamily = new ColumnFamily();
            $columnModification = new Modification();
            $columnModification->setId('cf1');
            $columnModification->setCreate($columnFamily);
            $modifyColumnFamiliesRequest = (new ModifyColumnFamiliesRequest())
                ->setName($tableName)
                ->setModifications([$columnModification]);
            $tableAdminClient->modifyColumnFamilies($modifyColumnFamiliesRequest);
            printf('Created table %s' . PHP_EOL, $tableId);
        } else {
            throw $e;
        }
    }

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    print("Creating the {} table.".format(table_id))
    table = instance.table(table_id)
    
    print("Creating column family cf1 with Max Version GC rule...")
    # Create a column family with GC policy : most recent N versions
    # Define the GC policy to retain only the most recent 2 versions
    max_versions_rule = bigtable.column_family.MaxVersionsGCRule(2)
    column_family_id = b"cf1"
    column_families = {column_family_id: max_versions_rule}
    if not table.exists():
        table.create(column_families=column_families)
    else:
        print("Table {} already exists.".format(table_id))

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This is the full resource name for the table. Use this name to make admin
    # calls for the table, such as reading or deleting the resource.
    table_name = table_client.table_path project: bigtable.project_id,
                                         instance: instance_id,
                                         table: table_id
    begin
      # Attempt to get the table to see if it already exists
      table_client.get_table name: table_name
      puts "#{table_id} is already exists."
      exit 0
    rescue Google::Cloud::NotFoundError
      # The table doesn't exist, so let's create it.
      # The following is the resource name for the table's instance.
      instance_name = table_client.instance_path project: bigtable.project_id,
                                                 instance: instance_id
      # This is the configuration of the table's column families.
      table_config = {
        column_families: {
          column_family => {
            gc_rule: Google::Cloud::Bigtable::Admin::V2::GcRule.max_num_versions(1)
          }
        }
      }
      # Now call the API to create the table.
      table_client.create_table parent: instance_name,
                                table_id: table_id,
                                table: table_config
      puts "Table #{table_id} created."
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
