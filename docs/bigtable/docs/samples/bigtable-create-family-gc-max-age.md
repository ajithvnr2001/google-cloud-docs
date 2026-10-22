---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-create-family-gc-max-age/
title: Maximum age \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:13.294228+00:00
---

# Maximum age  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-create-family-gc-max-age/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Maximum age Stay organized with collections  Save and categorize content based on your preferences. 

Create a column family with an age-based garbage-collection policy.

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
      auto constexpr kSecondsPerDay =
          std::chrono::seconds(std::chrono::hours(24)).count();
    
      ModifyColumnFamiliesRequest::Modification mod;
      mod.set_id(family_name);
      mod.mutable_create()->mutable_gc_rule()->mutable_max_age()->set_seconds(
          5 * kSecondsPerDay);
    
      StatusOr<google::bigtable::admin::v2::Table> schema =
          admin.ModifyColumnFamilies(table_name, {std::move(mod)});
    
      if (!schema) throw std::move(schema).status();
      std::cout << "Schema modified to: " << schema->DebugString() << "\n";
    }

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Create a column family with GC policy : maximum age
    // where age = current time minus cell timestamp
    // Initialize request argument(s).
    // Define the GC rule to retain data with max age of 5 days
    GcRule MaxAgeRule = new GcRule { MaxAge = Duration.FromTimeSpan(TimeSpan.FromDays(5.0)) };
    
    // Column family to create
    ColumnFamily columnFamily = new ColumnFamily { GcRule = MaxAgeRule };
    
    TableName tableName = new TableName(projectId, instanceId, tableId);
    
    // Modification to create column family
    ModifyColumnFamiliesRequest.Types.Modification modification = new ModifyColumnFamiliesRequest.Types.Modification
    {
        Create = columnFamily,
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
        Console.WriteLine("Created column family");
        // Print table information.
        GetTable(tableId);
    }
    catch (Exception ex)
    {
        Console.WriteLine($"Error creating column family {ex.Message}");
    }

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/bigtable"
    )
    
    func createFamilyGCMaxAge(w io.Writer, projectID, instanceID string, tableName string) error {
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
    	if err := adminClient.[CreateColumnFamily](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_AdminClient_CreateColumnFamily)(ctx, tableName, columnFamilyName); err != nil {
    		return fmt.Errorf("CreateColumnFamily(%s): %w", columnFamilyName, err)
    	}
    
    	// Set a garbage collection policy of 5 days.
    	maxAge := time.Hour * 24 * 5
    	policy := bigtable.[MaxAgePolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_GCPolicy_MaxAgePolicy)(maxAge)
    	if err := adminClient.[SetGCPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_AdminClient_SetGCPolicy)(ctx, tableName, columnFamilyName, policy); err != nil {
    		return fmt.Errorf("SetGCPolicy(%s): %w", policy, err)
    	}
    
    	fmt.Fprintf(w, "created column family %s with policy: %v\n", columnFamilyName, policy)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Creates a column family with GC policy : maximum age
    // where age = current time minus cell timestamp
    
    // Defines the GC rule to retain data with max age of 5 days.
    GcRule maxAgeRule = GcRuleBuilder.maxAge(Duration.ofDays(5));
    
    // Creates column family with given GC rule.
    try {
      String tableName =
          "projects/" + projectId + "/instances/" + instanceId + "/tables/" + tableId;
      ModifyColumnFamiliesRequest request =
          ModifyColumnFamiliesRequest.newBuilder()
              .setName(tableName)
              .addModifications(
                  ModifyColumnFamiliesRequest.Modification.newBuilder()
                      .setId(COLUMN_FAMILY_1)
                      .setCreate(ColumnFamily.newBuilder().setGcRule(maxAgeRule)))
              .build();
      adminClient.modifyColumnFamilies(request);
      System.out.println("Created column family: " + COLUMN_FAMILY_1);
    } catch (AlreadyExistsException e) {
      System.err.println(
          "Failed to create column family with rule, already exists: " + e.getMessage());
    }

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\ColumnFamily;
    use Google\Cloud\Bigtable\Admin\V2\GcRule;
    use Google\Cloud\Bigtable\Admin\V2\ModifyColumnFamiliesRequest;
    use Google\Cloud\Bigtable\Admin\V2\ModifyColumnFamiliesRequest\Modification;
    use Google\Protobuf\Duration;
    
    /**
     * Create a new column family with a max age GC rule
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance where the table resides
     * @param string $tableId The ID of the table in which the rule needs to be created
     */
    function create_family_gc_max_age(
        string $projectId,
        string $instanceId,
        string $tableId
    ): void {
        $tableAdminClient = new BigtableTableAdminClient();
    
        $tableName = $tableAdminClient->tableName($projectId, $instanceId, $tableId);
    
        print('Creating column family cf1 with MaxAge GC Rule...' . PHP_EOL);
        // Create a column family with GC policy : maximum age
        // where age = current time minus cell timestamp
    
        $columnFamily1 = new ColumnFamily();
        $duration = new Duration();
        $duration->setSeconds(3600 * 24 * 5);
        $MaxAgeRule = (new GcRule())->setMaxAge($duration);
        $columnFamily1->setGcRule($MaxAgeRule);
    
        $columnModification = new Modification();
        $columnModification->setId('cf1');
        $columnModification->setCreate($columnFamily1);
        $modifyColumnFamiliesRequest = (new ModifyColumnFamiliesRequest())
            ->setName($tableName)
            ->setModifications([$columnModification]);
        $tableAdminClient->modifyColumnFamilies($modifyColumnFamiliesRequest);
        print('Created column family cf1 with MaxAge GC Rule.' . PHP_EOL);
    }

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    print("Creating column family cf1 with with MaxAge GC Rule...")
    # Create a column family with GC policy : maximum age
    # where age = current time minus cell timestamp
    
    # Define the GC rule to retain data with max age of 5 days
    max_age_rule = column_family.MaxAgeGCRule(datetime.timedelta(days=5))
    
    column_family1 = table.column_family("cf1", max_age_rule)
    column_family1.create()
    print("Created column family cf1 with MaxAge GC Rule.")
    

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Create a column family with GC policy : maximum age
    # where age = current time minus cell timestamp
    # NOTE: Age value must be atleast 1 millisecond
    max_age_rule = Google::Cloud::Bigtable::GcRule.max_age 60 * 60 * 24 * 5
    column_families = table.column_families do |cfs|
      cfs.add "cf1", gc_rule: max_age_rule
    end
    family = column_families["cf1"]

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
