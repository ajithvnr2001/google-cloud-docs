---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-update-gc-rule/
title: Update a garbage-collection rule \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:04.898636+00:00
---

# Update a garbage-collection rule  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-update-gc-rule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Update a garbage-collection rule Stay organized with collections  Save and categorize content based on your preferences. 

Update a column-family garbage-collection rule.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Configure garbage collection](https://docs.cloud.google.com/bigtable/docs/configuring-garbage-collection)



## Code sample

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    namespace cbta = ::google::cloud::bigtable_admin;
    using ::google::bigtable::admin::v2::ModifyColumnFamiliesRequest;
    using ::google::cloud::StatusOr;
    [](cbta::BigtableTableAdminClient admin, std::string const& project_id,
       std::string const& instance_id, std::string const& table_id,
       std::string const& family_name) {
      std::string table_name = cbt::TableName(project_id, instance_id, table_id);
    
      ModifyColumnFamiliesRequest::Modification mod;
      mod.set_id(family_name);
      mod.mutable_update()->mutable_gc_rule()->set_max_num_versions(1);
    
      StatusOr<google::bigtable::admin::v2::Table> schema =
          admin.ModifyColumnFamilies(table_name, {std::move(mod)});
    
      if (!schema) throw std::move(schema).status();
      std::cout << "Schema modified to: " << schema->DebugString() << "\n";
    }

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Update the column family metadata to update the GC rule.
    // Initialize request argument(s).
    // Updated column family GC rule.
    GcRule maxVersionsRule = new GcRule { MaxNumVersions = 1 };
    
    // Column family to create
    ColumnFamily columnFamily = new ColumnFamily { GcRule = maxVersionsRule };
    
    TableName tableName = new TableName(projectId, instanceId, tableId);
    
    // Modification to update column family
    ModifyColumnFamiliesRequest.Types.Modification modification = new ModifyColumnFamiliesRequest.Types.Modification
    {
        Update = columnFamily,
        Id = "cf1"
    };
    
    ModifyColumnFamiliesRequest request = new ModifyColumnFamiliesRequest
    {
        TableName = tableName,
        Modifications = { modification }
    };
    try
    {
        // Make the request
        Table response = bigtableTableAdminClient.ModifyColumnFamilies(request);
        Console.WriteLine("Updated column family");
    }
    catch (Exception ex)
    {
        Console.WriteLine($"Error updating column family {ex.Message}");
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
    
    func updateGCRule(w io.Writer, projectID, instanceID string, tableName string) error {
    	// projectID := "my-project-id"
    	// instanceID := "my-instance-id"
    	// tableName := "my-table-name"
    
    	ctx := context.Background()
    
    	adminClient, err := bigtable.[NewAdminClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_AdminClient_NewAdminClient)(ctx, projectID, instanceID)
    	if err != nil {
    		return fmt.Errorf("bigtable.NewAdminClient: %w", err)
    	}
    	defer adminClient.Close()
    
    	columnFamilyName := "cf1"
    	// Update the column family cf1 to update the GC rule.
    	policy := bigtable.[MaxVersionsPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_GCPolicy_MaxVersionsPolicy)(1)
    	if err := adminClient.[SetGCPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_AdminClient_SetGCPolicy)(ctx, tableName, columnFamilyName, policy); err != nil {
    		return fmt.Errorf("SetGCPolicy(%s): %w", policy, err)
    	}
    
    	fmt.Fprintf(w, "Updated column family %s GC rule with policy: %v\n", columnFamilyName, policy)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Updates the column family metadata to update the GC rule.
    // Updates a column family GC rule.
    GcRule versionRule = GcRuleBuilder.maxVersions(1);
    try {
      String tableName =
          "projects/" + projectId + "/instances/" + instanceId + "/tables/" + tableId;
      ModifyColumnFamiliesRequest request =
          ModifyColumnFamiliesRequest.newBuilder()
              .setName(tableName)
              .addModifications(
                  ModifyColumnFamiliesRequest.Modification.newBuilder()
                      .setId(COLUMN_FAMILY_1)
                      .setUpdate(ColumnFamily.newBuilder().setGcRule(versionRule)))
              .build();
      adminClient.modifyColumnFamilies(request);
      System.out.printf("Column family %s GC rule updated%n", COLUMN_FAMILY_1);
    } catch (NotFoundException e) {
      System.err.println("Failed to modify a non-existent column family: " + e.getMessage());
    }

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\ColumnFamily;
    use Google\Cloud\Bigtable\Admin\V2\GcRule;
    use Google\Cloud\Bigtable\Admin\V2\ModifyColumnFamiliesRequest;
    use Google\Cloud\Bigtable\Admin\V2\ModifyColumnFamiliesRequest\Modification;
    
    /**
     * Update the GC Rule for an existing column family in the table
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table where the rule needs to be updated
     * @param string $familyId The ID of the column family
     */
    function update_gc_rule(
        string $projectId,
        string $instanceId,
        string $tableId,
        string $familyId = 'cf3'
    ): void {
        $tableAdminClient = new BigtableTableAdminClient();
        $tableName = $tableAdminClient->tableName($projectId, $instanceId, $tableId);
        $columnFamily1 = new ColumnFamily();
    
        printf('Updating column family %s GC rule...' . PHP_EOL, $familyId);
        $columnFamily1->setGcRule((new GcRule())->setMaxNumVersions(1));
        // Update the column family with ID $familyId to update the GC rule
        $columnModification = new Modification();
        $columnModification->setId($familyId);
        $columnModification->setUpdate($columnFamily1);
    
        try {
            $modifyColumnFamiliesRequest = (new ModifyColumnFamiliesRequest())
                ->setName($tableName)
                ->setModifications([$columnModification]);
            $tableAdminClient->modifyColumnFamilies($modifyColumnFamiliesRequest);
        } catch (ApiException $e) {
            if ($e->getStatus() === 'NOT_FOUND') {
                printf('Column family %s does not exist.' . PHP_EOL, $familyId);
                return;
            }
            throw $e;
        }
    
        printf('Print column family %s GC rule after update...' . PHP_EOL, $familyId);
        printf('Column Family: ' . $familyId . PHP_EOL);
        printf('%s' . PHP_EOL, $columnFamily1->serializeToJsonString());
    }

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    print("Updating column family cf1 GC rule...")
    # Update the column family cf1 to update the GC rule
    column_family1 = table.column_family("cf1", column_family.MaxVersionsGCRule(1))
    column_family1.update()
    print("Updated column family cf1 GC rule\n")
    

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    gc_rule = Google::Cloud::Bigtable::GcRule.max_versions 1
    column_families = table.column_families do |cfs|
      cfs.update "cf1", gc_rule: gc_rule
    end
    p column_families["cf1"]

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
