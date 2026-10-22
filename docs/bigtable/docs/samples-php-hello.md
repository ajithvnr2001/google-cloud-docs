---
url: https://docs.cloud.google.com/bigtable/docs/samples-php-hello/
title: PHP hello world \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:04.297547+00:00
---

# PHP hello world  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples-php-hello/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# PHP hello world

This code sample is a "hello world" application that runs on PHP. The sample illustrates how to complete the following tasks:

  * Set up authentication
  * Connect to a Bigtable instance.
  * Create a new table.
  * Write data to the table.
  * Read the data back.
  * Delete the table.



## Set up authentication

To use the Python samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/bigtable/docs/authentication#local-development). 

## Running the sample

This code sample uses the [PHP client library for Cloud Bigtable](https://github.com/googleapis/google-cloud-php/tree/master/Bigtable) package of the [Google Cloud Client Library for PHP](https://github.com/googleapis/google-cloud-php) to communicate with Bigtable.

To run this sample program, follow the [instructions for the sample on GitHub](https://github.com/GoogleCloudPlatform/php-docs-samples/blob/master/bigtable/README.md).

## Using the Cloud Client Library with Bigtable

The sample application connects to Bigtable and demonstrates some basic operations.

### Requiring the client library

The sample uses ApiCore's [ApiException class](https://googleapis.github.io/gax-php/0.35.0/Google/ApiCore/ApiException.html) as well as a number of classes in the [PHP client for Bigtable](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/v0.116.0/bigtable/readme).
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\ColumnFamily;
    use Google\Cloud\Bigtable\Admin\V2\CreateTableRequest;
    use Google\Cloud\Bigtable\Admin\V2\DeleteTableRequest;
    use Google\Cloud\Bigtable\Admin\V2\GetTableRequest;
    use Google\Cloud\Bigtable\Admin\V2\ModifyColumnFamiliesRequest;
    use Google\Cloud\Bigtable\Admin\V2\ModifyColumnFamiliesRequest\Modification;
    use Google\Cloud\Bigtable\Admin\V2\Table;
    use Google\Cloud\Bigtable\Admin\V2\Table\View;
    use Google\Cloud\Bigtable\BigtableClient;
    use Google\Cloud\Bigtable\Mutations;
    use Google\Cloud\Bigtable\V2\RowFilter;
    

### Connecting to Bigtable

Establish the variables you will use in your application, using a valid Google Cloud project ID, Bigtable instance ID, and table ID. Then instantiate new [BigtableInstanceAdminClient](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/v0.119.0/bigtable/admin/v2/bigtableinstanceadminclient), [BigtableTableAdminClient](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/v0.119.0/bigtable/admin/v2/bigtabletableadminclient), and [BigtableClient](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/v0.119.0/bigtable/v2/bigtableclient) objects that you use to connect to Bigtable.
    
    
    /** Uncomment and populate these variables in your code */
    // $projectId = 'The Google project ID';
    // $instanceId = 'The Bigtable instance ID';
    // $tableId = 'The Bigtable table ID';
    
    $instanceAdminClient = new BigtableInstanceAdminClient();
    $tableAdminClient = new BigtableTableAdminClient();
    $dataClient = new BigtableClient([
        'projectId' => $projectId,
    ]);

### Creating a table

Check to see if your table already exists. If it doesn't, call the [`createtable()`](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/v0.119.0/bigtable/admin/v2/bigtabletableadminclient?method=createTable) method to create a [`Table`](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/v0.119.0/bigtable/admin/v2/table) object. The table has a single column family that retains one version of each column value.

**Note:** Columns that are related to one another are typically grouped into a column family. For more information about column families, see the [Bigtable storage model](https://docs.cloud.google.com/bigtable/docs/overview#storage-model).
    
    
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

### Writing rows to a table

Next, use a string array of greetings to create some new rows for the table. For each greeting, create a new [`Mutations`](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/v0.119.0/bigtable/mutations) object and add it to `entries` using [`upsert()`](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/v0.119.0/bigtable/mutations?method=upsert). Then write the entries to the table using the table's [`mutateRows()`](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/v0.119.0/bigtable/table?method=mutateRows) method.

**Note:** In this sample application, `upsert()` is only called once per mutation, but you can call it up to 10,000 times per single mutation.
    
    
    $table = $dataClient->table($instanceId, $tableId);
    
    printf('Writing some greetings to the table.' . PHP_EOL);
    $greetings = ['Hello World!', 'Hello Cloud Bigtable!', 'Hello PHP!'];
    $entries = [];
    $columnFamilyId = 'cf1';
    $column = 'greeting';
    foreach ($greetings as $i => $value) {
        $rowKey = sprintf('greeting%s', $i);
        $rowMutation = new Mutations();
        $rowMutation->upsert($columnFamilyId, $column, $value, time() * 1000 * 1000);
        $entries[$rowKey] = $rowMutation;
    }
    $table->mutateRows($entries);

### Using a filter to read a row

Before you read the data that you wrote, create a filter to limit the data that Bigtable returns. This filter tells Bigtable to return only the most recent version of each value, even if the table contains older versions that haven't been garbage-collected.

Create a row object, then call the [`readRow()`](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/v0.119.0/bigtable/table?method=readRow) method, passing in the filter, to get one version of each column in that row.
    
    
    printf('Getting a single greeting by row key.' . PHP_EOL);
    $key = 'greeting0';
    // Only retrieve the most recent version of the cell.
    $rowFilter = (new RowFilter())->setCellsPerColumnLimitFilter(1);
    
    $column = 'greeting';
    $columnFamilyId = 'cf1';
    
    $row = $table->readRow($key, [
        'filter' => $rowFilter
    ]);
    printf('%s' . PHP_EOL, $row[$columnFamilyId][$column][0]['value']);

### Scanning all table rows

Call the [`readRows()`](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/v0.119.0/bigtable/table?method=readRows) method, passing in the filter, to get all of the rows in the table. Because you passed in the filter, Bigtable returns only one version of each value.
    
    
    $columnFamilyId = 'cf1';
    $column = 'greeting';
    printf('Scanning for all greetings:' . PHP_EOL);
    $partialRows = $table->readRows([])->readAll();
    foreach ($partialRows as $row) {
        printf('%s' . PHP_EOL, $row[$columnFamilyId][$column][0]['value']);
    }

### Deleting a table

Delete the table with the admin client's [`deleteTable()`](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/v0.119.0/bigtable/admin/v2/bigtabletableadminclient?method=deleteTable) method.
    
    
    try {
        printf('Attempting to delete table %s.' . PHP_EOL, $tableId);
        $deleteTableRequest = (new DeleteTableRequest())
            ->setName($tableName);
        $tableAdminClient->deleteTable($deleteTableRequest);
        printf('Deleted %s table.' . PHP_EOL, $tableId);
    } catch (ApiException $e) {
        if ($e->getStatus() === 'NOT_FOUND') {
            printf('Table %s does not exists' . PHP_EOL, $tableId);
        } else {
            throw $e;
        }
    }

## Putting it all together

Here is the full code sample without comments.
    
    
    <?php
    
    
    
    require_once __DIR__ . '/../vendor/autoload.php';
    
    if (count($argv) != 4) {
        return printf('Usage: php %s PROJECT_ID INSTANCE_ID TABLE_ID' . PHP_EOL, __FILE__);
    }
    list($_, $projectId, $instanceId, $tableId) = $argv;
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\ColumnFamily;
    use Google\Cloud\Bigtable\Admin\V2\CreateTableRequest;
    use Google\Cloud\Bigtable\Admin\V2\DeleteTableRequest;
    use Google\Cloud\Bigtable\Admin\V2\GetTableRequest;
    use Google\Cloud\Bigtable\Admin\V2\ModifyColumnFamiliesRequest;
    use Google\Cloud\Bigtable\Admin\V2\ModifyColumnFamiliesRequest\Modification;
    use Google\Cloud\Bigtable\Admin\V2\Table;
    use Google\Cloud\Bigtable\Admin\V2\Table\View;
    use Google\Cloud\Bigtable\BigtableClient;
    use Google\Cloud\Bigtable\Mutations;
    use Google\Cloud\Bigtable\V2\RowFilter;
    
    
    
    $instanceAdminClient = new BigtableInstanceAdminClient();
    $tableAdminClient = new BigtableTableAdminClient();
    $dataClient = new BigtableClient([
        'projectId' => $projectId,
    ]);
    
    $instanceName = $instanceAdminClient->instanceName($projectId, $instanceId);
    $tableName = $tableAdminClient->tableName($projectId, $instanceId, $tableId);
    
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
    
    $table = $dataClient->table($instanceId, $tableId);
    
    printf('Writing some greetings to the table.' . PHP_EOL);
    $greetings = ['Hello World!', 'Hello Cloud Bigtable!', 'Hello PHP!'];
    $entries = [];
    $columnFamilyId = 'cf1';
    $column = 'greeting';
    foreach ($greetings as $i => $value) {
        $rowKey = sprintf('greeting%s', $i);
        $rowMutation = new Mutations();
        $rowMutation->upsert($columnFamilyId, $column, $value, time() * 1000 * 1000);
        $entries[$rowKey] = $rowMutation;
    }
    $table->mutateRows($entries);
    
    printf('Getting a single greeting by row key.' . PHP_EOL);
    $key = 'greeting0';
    $rowFilter = (new RowFilter())->setCellsPerColumnLimitFilter(1);
    
    $column = 'greeting';
    $columnFamilyId = 'cf1';
    
    $row = $table->readRow($key, [
        'filter' => $rowFilter
    ]);
    printf('%s' . PHP_EOL, $row[$columnFamilyId][$column][0]['value']);
    
    $columnFamilyId = 'cf1';
    $column = 'greeting';
    printf('Scanning for all greetings:' . PHP_EOL);
    $partialRows = $table->readRows([])->readAll();
    foreach ($partialRows as $row) {
        printf('%s' . PHP_EOL, $row[$columnFamilyId][$column][0]['value']);
    }
    
    try {
        printf('Attempting to delete table %s.' . PHP_EOL, $tableId);
        $deleteTableRequest = (new DeleteTableRequest())
            ->setName($tableName);
        $tableAdminClient->deleteTable($deleteTableRequest);
        printf('Deleted %s table.' . PHP_EOL, $tableId);
    } catch (ApiException $e) {
        if ($e->getStatus() === 'NOT_FOUND') {
            printf('Table %s does not exists' . PHP_EOL, $tableId);
        } else {
            throw $e;
        }
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
