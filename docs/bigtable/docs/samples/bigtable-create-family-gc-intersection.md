---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-create-family-gc-intersection/
title: Intersection garbage-collection policy \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:19.137962+00:00
---

# Intersection garbage-collection policy  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-create-family-gc-intersection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Intersection garbage-collection policy Stay organized with collections  Save and categorize content based on your preferences. 

Create a column family with an intersection garbage-collection policy (age and versions).

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
      auto& gc_int =
          *mod.mutable_create()->mutable_gc_rule()->mutable_intersection();
      gc_int.add_rules()->set_max_num_versions(1);
      gc_int.add_rules()->mutable_max_age()->set_seconds(5 * kSecondsPerDay);
    
      StatusOr<google::bigtable::admin::v2::Table> schema =
          admin.ModifyColumnFamilies(table_name, {std::move(mod)});
    
      if (!schema) throw std::move(schema).status();
      std::cout << "Schema modified to: " << schema->DebugString() << "\n";
    }

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Create a column family with GC policy to drop data that matches all conditions.
    // Initialize request argument(s).
    // GC rule: Drop cells older than 5 days AND older than the most recent 2 versions.
    GcRule.Types.Intersection intersectionRule = new GcRule.Types.Intersection
    {
        Rules =
        {
            new GcRule { MaxNumVersions = 2 },
            new GcRule { MaxAge = Duration.FromTimeSpan(TimeSpan.FromDays(5)) }
        }
    };
    GcRule gcRule = new GcRule { Intersection = intersectionRule };
    
    // Column family to create
    ColumnFamily columnFamily = new ColumnFamily { GcRule = gcRule };
    
    TableName tableName = new TableName(projectId, instanceId, tableId);
    
    // Modification to create column family
    ModifyColumnFamiliesRequest.Types.Modification modification = new ModifyColumnFamiliesRequest.Types.Modification
    {
        Create = columnFamily,
        Id = "cf4"
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
    
    func createFamilyGCIntersect(w io.Writer, projectID, instanceID string, tableName string) error {
    	// projectID := "my-project-id"
    	// instanceID := "my-instance-id"
    	// tableName := "my-table-name"
    
    	ctx := context.Background()
    
    	adminClient, err := bigtable.[NewAdminClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_AdminClient_NewAdminClient)(ctx, projectID, instanceID)
    	if err != nil {
    		return fmt.Errorf("bigtable.NewAdminClient: %w", err)
    	}
    	defer adminClient.Close()
    
    	columnFamilyName := "cf4"
    	if err := adminClient.[CreateColumnFamily](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_AdminClient_CreateColumnFamily)(ctx, tableName, columnFamilyName); err != nil {
    		return fmt.Errorf("CreateColumnFamily(%s): %w", columnFamilyName, err)
    	}
    
    	// GC rule: Drop cells older than 5 days AND older than the most recent 2 versions
    	maxAge := time.Hour * 24 * 5
    	maxAgePolicy := bigtable.[MaxAgePolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_GCPolicy_MaxAgePolicy)(maxAge)
    	policy := bigtable.[IntersectionPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_GCPolicy_IntersectionPolicy)(bigtable.[MaxVersionsPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_GCPolicy_MaxVersionsPolicy)(2), maxAgePolicy)
    	if err := adminClient.[SetGCPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_AdminClient_SetGCPolicy)(ctx, tableName, columnFamilyName, policy); err != nil {
    		return fmt.Errorf("SetGCPolicy(%s): %w", policy, err)
    	}
    
    	fmt.Fprintf(w, "created column family %s with policy: %v\n", columnFamilyName, policy)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Creates a column family with GC policy to drop data that matches all conditions.
    
    // Defines a GC rule to drop cells older than 5 days AND older than the most recent 2 versions.
    GcRule intersectionRule =
        GcRuleBuilder.intersection()
            .add(GcRuleBuilder.maxAge(Duration.ofDays(5)))
            .add(GcRuleBuilder.maxVersions(2))
            .build();
    
    // Creates column family with given GC rule.
    try {
      String tableName =
          "projects/" + projectId + "/instances/" + instanceId + "/tables/" + tableId;
      ModifyColumnFamiliesRequest request =
          ModifyColumnFamiliesRequest.newBuilder()
              .setName(tableName)
              .addModifications(
                  ModifyColumnFamiliesRequest.Modification.newBuilder()
                      .setId(COLUMN_FAMILY_4)
                      .setCreate(ColumnFamily.newBuilder().setGcRule(intersectionRule)))
              .build();
      adminClient.modifyColumnFamilies(request);
      System.out.println("Created column family: " + COLUMN_FAMILY_4);
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
    use Google\Cloud\Bigtable\Admin\V2\ModifyColumnFamiliesRequest;
    use Google\Cloud\Bigtable\Admin\V2\ModifyColumnFamiliesRequest\Modification;
    use Google\Protobuf\Duration;
    
    /**
     * Create a new column family with an intersection GC rule
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance where the table resides
     * @param string $tableId The ID of the table in which the rule needs to be created
     */
    function create_family_gc_intersection(
        string $projectId,
        string $instanceId,
        string $tableId
    ): void {
        $tableAdminClient = new BigtableTableAdminClient();
    
        $tableName = $tableAdminClient->tableName($projectId, $instanceId, $tableId);
    
        print('Creating column family cf4 with Intersection GC rule...' . PHP_EOL);
        $columnFamily4 = new ColumnFamily();
    
        $intersectionRule = new GcRuleIntersection();
        $intersectionArray = [
            (new GcRule())->setMaxAge((new Duration())->setSeconds(3600 * 24 * 5)),
            (new GcRule())->setMaxNumVersions(2)
        ];
        $intersectionRule->setRules($intersectionArray);
    
        $intersection = new GcRule();
        $intersection->setIntersection($intersectionRule);
    
        $columnFamily4->setGCRule($intersection);
    
        $columnModification = new Modification();
        $columnModification->setId('cf4');
        $columnModification->setCreate($columnFamily4);
        $modifyColumnFamiliesRequest = (new ModifyColumnFamiliesRequest())
            ->setName($tableName)
            ->setModifications([$columnModification]);
        $tableAdminClient->modifyColumnFamilies($modifyColumnFamiliesRequest);
    
        print('Created column family cf4 with Union GC rule' . PHP_EOL);
    }
    

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    print("Creating column family cf4 with Intersection GC rule...")
    # Create a column family with GC policy to drop data that matches
    # all conditions
    # GC rule: Drop cells older than 5 days AND older than the most
    # recent 2 versions
    intersection_rule = column_family.GCRuleIntersection(
        [
            column_family.MaxAgeGCRule(datetime.timedelta(days=5)),
            column_family.MaxVersionsGCRule(2),
        ]
    )
    
    column_family4 = table.column_family("cf4", intersection_rule)
    column_family4.create()
    print("Created column family cf4 with Intersection GC rule.")
    

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Create a column family with GC policy to drop data that matches at least
    # one condition
    max_age_rule = Google::Cloud::Bigtable::GcRule.max_age 60 * 60 * 24 * 5
    max_versions_rule = Google::Cloud::Bigtable::GcRule.max_versions 2
    intersection_gc_rule = Google::Cloud::Bigtable::GcRule.intersection max_age_rule, max_versions_rule
    column_families = table.column_families do |cfs|
      cfs.add "cf4", gc_rule: intersection_gc_rule
    end
    family = column_families["cf4"]

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
