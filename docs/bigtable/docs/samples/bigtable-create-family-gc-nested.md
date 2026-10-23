---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-create-family-gc-nested/
title: Nested garbage-collection policy \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:05.933921+00:00
---

# Nested garbage-collection policy  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-create-family-gc-nested/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Nested garbage-collection policy Stay organized with collections  Save and categorize content based on your preferences. 

Create a column family with a nested garbage-collection policy, if supported. 

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
      auto& gc = *mod.mutable_create()->mutable_gc_rule();
      auto& gc_1 = *gc.mutable_union_()->add_rules();
      auto& gc_2 = *gc.mutable_union_()->add_rules();
      auto& gc_2_1 = *gc_2.mutable_intersection()->add_rules();
      auto& gc_2_2 = *gc_2.mutable_intersection()->add_rules();
    
      gc_1.set_max_num_versions(10);
      gc_2_1.set_max_num_versions(1);
      gc_2_2.mutable_max_age()->set_seconds(5 * kSecondsPerDay);
    
      StatusOr<google::bigtable::admin::v2::Table> schema =
          admin.ModifyColumnFamilies(table_name, {std::move(mod)});
    
      if (!schema) throw std::move(schema).status();
      std::cout << "Schema modified to: " << schema->DebugString() << "\n";
    }

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Create a nested GC rule:
    // Drop cells that are either older than the 10 recent versions
    // OR
    // Drop cells that are older than 5 days AND older than the 2 recent versions.
    // Initialize request argument(s).
    GcRule.Types.Intersection intersectionRule = new GcRule.Types.Intersection
    {
        Rules =
        {
            new GcRule { MaxNumVersions = 2 },
            new GcRule { MaxAge = Duration.FromTimeSpan(TimeSpan.FromDays(5)) }
        }
    };
    
    GcRule.Types.Union nestedRule = new GcRule.Types.Union
    {
        Rules =
        {
            new GcRule { MaxNumVersions = 10 },
            new GcRule { Intersection = intersectionRule }
        }
    };
    
    GcRule gcRule = new GcRule { Union = nestedRule };
    
    // Column family to create
    ColumnFamily columnFamily = new ColumnFamily { GcRule = gcRule };
    
    TableName tableName = new TableName(projectId, instanceId, tableId);
    
    // Modification to create column family
    ModifyColumnFamiliesRequest.Types.Modification modification = new ModifyColumnFamiliesRequest.Types.Modification
    {
        Create = columnFamily,
        Id = "cf5"
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
    
    func createFamilyGCNested(w io.Writer, projectID, instanceID string, tableName string) error {
    	// projectID := "my-project-id"
    	// instanceID := "my-instance-id"
    	// tableName := "my-table-name"
    
    	ctx := context.Background()
    
    	adminClient, err := bigtable.[NewAdminClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_AdminClient_NewAdminClient)(ctx, projectID, instanceID)
    	if err != nil {
    		return fmt.Errorf("bigtable.NewAdminClient: %w", err)
    	}
    	defer adminClient.Close()
    
    	columnFamilyName := "cf5"
    	if err := adminClient.[CreateColumnFamily](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_AdminClient_CreateColumnFamily)(ctx, tableName, columnFamilyName); err != nil {
    		return fmt.Errorf("CreateColumnFamily(%s): %w", columnFamilyName, err)
    	}
    
    	// Create a nested GC rule:
    	// Drop cells that are either older than the 10 recent versions
    	// OR
    	// Drop cells that are older than a month AND older than the 2 recent versions
    	maxAge := time.Hour * 24 * 5
    	maxAgePolicy := bigtable.[MaxAgePolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_GCPolicy_MaxAgePolicy)(maxAge)
    	policy := bigtable.[UnionPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_GCPolicy_UnionPolicy)(
    		bigtable.[MaxVersionsPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_GCPolicy_MaxVersionsPolicy)(10),
    		bigtable.[IntersectionPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_GCPolicy_IntersectionPolicy)(
    			bigtable.[MaxVersionsPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_GCPolicy_MaxVersionsPolicy)(2),
    			maxAgePolicy))
    	if err := adminClient.[SetGCPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_AdminClient_SetGCPolicy)(ctx, tableName, columnFamilyName, policy); err != nil {
    		return fmt.Errorf("SetGCPolicy(%s): %w", policy, err)
    	}
    
    	fmt.Fprintf(w, "created column family %s with policy: %v\n", columnFamilyName, policy)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Creates a nested GC rule:
    // Drop cells that are either older than the 10 recent versions
    // OR
    // Drop cells that are older than a month AND older than the 2 recent versions
    GcRule intersectionRule =
        GcRuleBuilder.intersection()
            .add(GcRuleBuilder.maxAge(Duration.ofDays(30)))
            .add(GcRuleBuilder.maxVersions(2))
            .build();
    GcRule unionRule =
        GcRuleBuilder.union().add(intersectionRule).add(GcRuleBuilder.maxVersions(10)).build();
    
    // Creates column family with given GC rule.
    try {
      String tableName =
          "projects/" + projectId + "/instances/" + instanceId + "/tables/" + tableId;
      ModifyColumnFamiliesRequest request =
          ModifyColumnFamiliesRequest.newBuilder()
              .setName(tableName)
              .addModifications(
                  ModifyColumnFamiliesRequest.Modification.newBuilder()
                      .setId(COLUMN_FAMILY_5)
                      .setCreate(ColumnFamily.newBuilder().setGcRule(unionRule)))
              .build();
      adminClient.modifyColumnFamilies(request);
      System.out.println("Created column family: " + COLUMN_FAMILY_5);
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
    use Google\Cloud\Bigtable\Admin\V2\GcRule\Intersection as GcRuleIntersection;
    use Google\Cloud\Bigtable\Admin\V2\GcRule\Union as GcRuleUnion;
    use Google\Cloud\Bigtable\Admin\V2\ModifyColumnFamiliesRequest;
    use Google\Cloud\Bigtable\Admin\V2\ModifyColumnFamiliesRequest\Modification;
    use Google\Protobuf\Duration;
    
    /**
     * Create a new column family with a nested GC rule
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance where the table resides
     * @param string $tableId The ID of the table in which the rule needs to be created
     */
    function create_family_gc_nested(
        string $projectId,
        string $instanceId,
        string $tableId
    ): void {
        $tableAdminClient = new BigtableTableAdminClient();
    
        $tableName = $tableAdminClient->tableName($projectId, $instanceId, $tableId);
    
        print('Creating column family cf5 with a Nested GC rule...' . PHP_EOL);
        // Create a column family with nested GC policies.
        // Create a nested GC rule:
        // Drop cells that are either older than the 10 recent versions
        // OR
        // Drop cells that are older than a month AND older than the
        // 2 recent versions
        $columnFamily5 = new ColumnFamily();
        $rule1 = (new GcRule())->setMaxNumVersions(10);
    
        $rule2Intersection = new GcRuleIntersection();
        $rule2Duration1 = new Duration();
        $rule2Duration1->setSeconds(3600 * 24 * 30);
        $rule2Array = [
            (new GcRule())->setMaxAge($rule2Duration1),
            (new GcRule())->setMaxNumVersions(2)
        ];
        $rule2Intersection->setRules($rule2Array);
        $rule2 = new GcRule();
        $rule2->setIntersection($rule2Intersection);
    
        $nestedRule = new GcRuleUnion();
        $nestedRule->setRules([
            $rule1,
            $rule2
        ]);
        $nestedRule = (new GcRule())->setUnion($nestedRule);
    
        $columnFamily5->setGCRule($nestedRule);
    
        $columnModification = new Modification();
        $columnModification->setId('cf5');
        $columnModification->setCreate($columnFamily5);
        $modifyColumnFamiliesRequest = (new ModifyColumnFamiliesRequest())
            ->setName($tableName)
            ->setModifications([$columnModification]);
        $tableAdminClient->modifyColumnFamilies($modifyColumnFamiliesRequest);
    
        print('Created column family cf5 with a Nested GC rule.' . PHP_EOL);
    }

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    print("Creating column family cf5 with a Nested GC rule...")
    # Create a column family with nested GC policies.
    # Create a nested GC rule:
    # Drop cells that are either older than the 10 recent versions
    # OR
    # Drop cells that are older than a month AND older than the
    # 2 recent versions
    rule1 = column_family.MaxVersionsGCRule(10)
    rule2 = column_family.GCRuleIntersection(
        [
            column_family.MaxAgeGCRule(datetime.timedelta(days=30)),
            column_family.MaxVersionsGCRule(2),
        ]
    )
    
    nested_rule = column_family.GCRuleUnion([rule1, rule2])
    
    column_family5 = table.column_family("cf5", nested_rule)
    column_family5.create()
    print("Created column family cf5 with a Nested GC rule.")
    

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Create a nested GC rule:
    # Drop cells that are either older than the 10 recent versions
    # OR
    # Drop cells that are older than a month AND older than the 2 recent versions
    max_versions_rule1 = Google::Cloud::Bigtable::GcRule.max_versions 10
    max_age_rule = Google::Cloud::Bigtable::GcRule.max_age 60 * 60 * 24 * 5
    max_versions_rule2 = Google::Cloud::Bigtable::GcRule.max_versions 2
    intersection_gc_rule = Google::Cloud::Bigtable::GcRule.intersection max_age_rule, max_versions_rule2
    nested_gc_rule = Google::Cloud::Bigtable::GcRule.union max_versions_rule1, intersection_gc_rule

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
