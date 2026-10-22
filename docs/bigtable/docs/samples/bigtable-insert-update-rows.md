---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-insert-update-rows/
title: Update or insert rows \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:30.066751+00:00
---

# Update or insert rows  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-insert-update-rows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Update or insert rows Stay organized with collections  Save and categorize content based on your preferences. 

Update or insert rows in a table.

## Code sample

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    struct InsertOrUpdate {
      std::string column_family;
      std::string column;
      std::string value;
    };
    namespace cbt = ::google::cloud::bigtable;
    [](cbt::Table table, std::string const& key,
       std::vector<InsertOrUpdate> const& inserts) {
      cbt::SingleRowMutation mutation(key);
      for (auto const& mut : inserts) {
        mutation.emplace_back(
            cbt::SetCell(mut.column_family, mut.column, mut.value));
      }
      google::cloud::Status status = table.Apply(std::move(mutation));
      if (!status.ok()) throw std::runtime_error(status.message());
      std::cout << "Row successfully updated\n";
    }

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\ColumnFamily;
    use Google\Cloud\Bigtable\Admin\V2\CreateTableRequest;
    use Google\Cloud\Bigtable\Admin\V2\ModifyColumnFamiliesRequest;
    use Google\Cloud\Bigtable\Admin\V2\ModifyColumnFamiliesRequest\Modification;
    use Google\Cloud\Bigtable\Admin\V2\Table as TableClass;
    use Google\Cloud\Bigtable\BigtableClient;
    
    /**
     * Perform insert/update operations on a Bigtable
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table on which we intend to insert/update rows
     */
    function insert_update_rows(
        string $projectId,
        string $instanceId = 'quickstart-instance-php',
        string $tableId = 'bigtable-php-table'
    ): void {
        $dataClient = new BigtableClient([
            'projectId' => $projectId,
        ]);
    
        $instanceAdminClient = new BigtableInstanceAdminClient();
        $tableAdminClient = new BigtableTableAdminClient();
    
        $instanceName = $instanceAdminClient->instanceName($projectId, $instanceId);
        $tableName = $tableAdminClient->tableName($projectId, $instanceId, $tableId);
    
        $table = new TableClass();
    
        printf('Creating table %s' . PHP_EOL, $tableId);
    
        try {
            $createTableRequest = (new CreateTableRequest())
                ->setParent($instanceName)
                ->setTableId($tableId)
                ->setTable($table);
            $tableAdminClient->createtable($createTableRequest);
        } catch (ApiException $e) {
            if ($e->getStatus() === 'ALREADY_EXISTS') {
                printf('Table %s already exists.' . PHP_EOL, $tableId);
                return;
            }
            throw $e;
        }
    
        printf('Table %s created' . PHP_EOL, $tableId);
    
        $table = $dataClient->table($instanceId, $tableId);
        $columnFamilyId = 'cf1';
    
        printf('Creating column family %s' . PHP_EOL, $columnFamilyId);
    
        $columnFamily4 = new ColumnFamily();
        $columnModification = new Modification();
        $columnModification->setId($columnFamilyId);
        $columnModification->setCreate($columnFamily4);
        $modifyColumnFamiliesRequest = (new ModifyColumnFamiliesRequest())
            ->setName($tableName)
            ->setModifications([$columnModification]);
        $tableAdminClient->modifyColumnFamilies($modifyColumnFamiliesRequest);
    
        printf('Inserting data in the table' . PHP_EOL);
    
        $insertRows = [
            'rk5' => [
                'cf1' => [
                    'cq5' => [
                        'value' => 'Value5',
                        'timeStamp' => time_in_microseconds()
                    ]
                ]
            ]
        ];
        $table->upsert($insertRows);
    
        printf('Data inserted successfully!' . PHP_EOL);
    }
    
    function time_in_microseconds(): float
    {
        $mt = microtime(true);
        $mt = sprintf('%.03f', $mt);
        return (float) $mt * 1000000;
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
