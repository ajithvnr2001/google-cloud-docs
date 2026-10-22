---
url: https://docs.cloud.google.com/bigtable/docs/configuring-garbage-collection/
title: Configure garbage collection \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:18.213513+00:00
---

# Configure garbage collection  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/configuring-garbage-collection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure garbage collection

Bigtable garbage collection policies let you control storage costs and remove obsolete cell data automatically. You can view, define, and update these policies using the Google Cloud console, the `cbt` CLI , or Cloud Bigtable client libraries. Before you begin, review the [Garbage collection overview](https://docs.cloud.google.com/bigtable/docs/garbage-collection).

## View current garbage collection policies

You can use either the Google Cloud console or the `cbt` CLI to view a column family's garbage collection policies.

###  Console 

To view the current garbage collection policy for a column family:

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance whose tables you want to view.

  3. Click **Tables** in the left pane.

The Tables page displays a list of tables in the instance.

  4. Click edit **Edit** in the table's row.

  5. Click keyboard_arrow_down **Open** next to the column family that you want to view.

  6. When you are finished viewing the garbage collection policy, click **Cancel** to exit.




###  cbt 

You can look up the current garbage collection policies for a given table by running the following command, substituting a valid table ID for `TABLE_ID`:
    
    
    cbt ls TABLE_ID
    

## Set garbage collection policies

You can set garbage collection policies using the Google Cloud console, the [ `cbt` CLI ](https://docs.cloud.google.com/bigtable/docs/cbt-overview), or the Cloud Bigtable [client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries).

### Garbage collection based on age

The following section shows how to set the [maximum age](https://docs.cloud.google.com/bigtable/docs/garbage-collection#age-based) for data in a column family.

###  Console 

To set an expiration time for cells in a column family:

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance whose tables you want to view.

  3. Click **Tables** in the left pane.

The Tables page displays a list of tables in the instance.

  4. Click edit Edit.

  5. Click keyboard_arrow_down **Open** next to the column family that you want to edit.

  6. Select **Age based policy**.

  7. Enter the age by entering a number in the **Max age** field and using the **Unit** drop-down to select the unit of time.

For example, to retain a column family's data for 30 minutes, enter **30** and choose **minutes**.

  8. Click **Save**.




### cbt

This example creates a column family named `cf1`, then sets the maximum age for data in the column family to five days. This tells Bigtable to remove all data with timestamps older than five days in all columns in this column family.
    
    
    cbt createfamily your-table cf1
    cbt setgcpolicy your-table cf1 maxage=5d
    

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    print("Creating column family cf1 with with MaxAge GC Rule...")
    # Create a column family with GC policy : maximum age
    # where age = current time minus cell timestamp
    
    # Define the GC rule to retain data with max age of 5 days
    max_age_rule = column_family.MaxAgeGCRule(datetime.timedelta(days=5))
    
    column_family1 = table.column_family("cf1", max_age_rule)
    column_family1.create()
    print("Created column family cf1 with MaxAge GC Rule.")
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    // Create a column family with GC policy : maximum age
    // where age = current time minus cell timestamp
    
    // Define the GC rule to retain data with max age of 5 days
    const maxAgeRule = GcRuleBuilder.rule({
      maxAge: {
        // Value must be atleast 1 millisecond
        seconds: 60 * 60 * 24 * 5,
        nanos: 0,
      },
    });
    let [family] = await adminClient.modifyColumnFamilies({
      name: table.name,
      modifications: [
        {
          id: 'cf1',
          create: {
            gcRule: maxAgeRule,
          },
        },
      ],
    });
    console.log(`Created column family ${family.name}`);

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    # Create a column family with GC policy : maximum age
    # where age = current time minus cell timestamp
    # NOTE: Age value must be atleast 1 millisecond
    max_age_rule = Google::Cloud::Bigtable::GcRule.max_age 60 * 60 * 24 * 5
    column_families = table.column_families do |cfs|
      cfs.add "cf1", gc_rule: max_age_rule
    end
    family = column_families["cf1"]

### Garbage collection based on the number of versions

The following section shows how to create a column family with a garbage collection policy that states the [number of versions](https://docs.cloud.google.com/bigtable/docs/garbage-collection#version-based) of the data, or number of cells, to keep.

###  Console 

To set the number of cells, or versions, to retain in a column family:

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance whose tables you want to view.

  3. Click **Tables** in the left pane.

The Tables page displays a list of tables in the instance.

  4. Click edit **Edit** in the table's row.

  5. Click keyboard_arrow_down **Open** next to the column family that you want to edit.

  6. Select **Version based policy**.

  7. Enter the number of cells to retain in every column in the column family.

  8. Click **Save**.




### cbt

This example creates a column family named `cf2`, then sets the number of versions to keep in the column family to two. This tells Bigtable to remove all but the two most recent cells in all columns in this column family.
    
    
    cbt createfamily your-table cf2
    cbt setgcpolicy your-table cf2 maxversions=2
    

This example sets a policy to remove all cells except the newest one.
    
    
    cbt setgcpolicy your-table cf2 maxversions=1
    

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/bigtable"
    )
    
    func createFamilyGCMaxVersions(w io.Writer, projectID, instanceID string, tableName string) error {
    	// projectID := "my-project-id"
    	// instanceID := "my-instance-id"
    	// tableName := "my-table-name"
    
    	ctx := context.Background()
    
    	adminClient, err := bigtable.[NewAdminClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_AdminClient_NewAdminClient)(ctx, projectID, instanceID)
    	if err != nil {
    		return fmt.Errorf("bigtable.NewAdminClient: %w", err)
    	}
    	defer adminClient.Close()
    
    	columnFamilyName := "cf2"
    	if err := adminClient.[CreateColumnFamily](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_AdminClient_CreateColumnFamily)(ctx, tableName, columnFamilyName); err != nil {
    		return fmt.Errorf("CreateColumnFamily(%s): %w", columnFamilyName, err)
    	}
    
    	// Set a garbage collection policy of 2 versions.
    	policy := bigtable.[MaxVersionsPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_GCPolicy_MaxVersionsPolicy)(2)
    	if err := adminClient.[SetGCPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_AdminClient_SetGCPolicy)(ctx, tableName, columnFamilyName, policy); err != nil {
    		return fmt.Errorf("SetGCPolicy(%s): %w", policy, err)
    	}
    
    	fmt.Fprintf(w, "created column family %s with policy: %v\n", columnFamilyName, policy)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    // Creates a column family with GC policy : most recent N versions
    // where 1 = most recent version
    
    // Defines the GC policy to retain only the most recent 2 versions.
    GcRule versionRule = GcRuleBuilder.maxVersions(2);
    
    // Creates column family with given GC rule.
    try {
      String tableName =
          "projects/" + projectId + "/instances/" + instanceId + "/tables/" + tableId;
      ModifyColumnFamiliesRequest request =
          ModifyColumnFamiliesRequest.newBuilder()
              .setName(tableName)
              .addModifications(
                  ModifyColumnFamiliesRequest.Modification.newBuilder()
                      .setId(COLUMN_FAMILY_2)
                      .setCreate(ColumnFamily.newBuilder().setGcRule(versionRule)))
              .build();
      adminClient.modifyColumnFamilies(request);
      System.out.println("Created column family: " + COLUMN_FAMILY_2);
    } catch (AlreadyExistsException e) {
      System.err.println(
          "Failed to create column family with rule, already exists: " + e.getMessage());
    }

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    print("Creating column family cf2 with max versions GC rule...")
    # Create a column family with GC policy : most recent N versions
    # where 1 = most recent version
    
    # Define the GC policy to retain only the most recent 2 versions
    max_versions_rule = column_family.MaxVersionsGCRule(2)
    
    column_family2 = table.column_family("cf2", max_versions_rule)
    column_family2.create()
    print("Created column family cf2 with Max Versions GC Rule.")
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    // Create a column family with GC policy : most recent N versions
    // where 1 = most recent version
    // Initialize request argument(s).
    // Define the GC policy to retain only the most recent 2 versions
    GcRule maxVersionsRule = new GcRule { MaxNumVersions = 2 };
    
    // Column family to create
    ColumnFamily columnFamily = new ColumnFamily { GcRule = maxVersionsRule };
    
    TableName tableName = new TableName(projectId, instanceId, tableId);
    
    // Modification to create column family
    ModifyColumnFamiliesRequest.Types.Modification modification = new ModifyColumnFamiliesRequest.Types.Modification
    {
        Create = columnFamily,
        Id = "cf2"
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

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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
      mod.mutable_create()->mutable_gc_rule()->set_max_num_versions(2);
    
      StatusOr<google::bigtable::admin::v2::Table> schema =
          admin.ModifyColumnFamilies(table_name, {std::move(mod)});
    
      if (!schema) throw std::move(schema).status();
      std::cout << "Schema modified to: " << schema->DebugString() << "\n";
    }

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    // Create a column family with GC policy : most recent N versions
    // where 1 = most recent version
    
    // Define the GC policy to retain only the most recent 2 versions
    const maxVersionsRule = GcRuleBuilder.rule({
      maxVersions: 2,
    });
    
    // Create a column family with given GC rule
    [family] = await adminClient.modifyColumnFamilies({
      name: table.name,
      modifications: [
        {
          id: 'cf2',
          create: {
            gcRule: maxVersionsRule,
          },
        },
      ],
    });
    console.log(`Created column family ${family.name}`);

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\ColumnFamily;
    use Google\Cloud\Bigtable\Admin\V2\GcRule;
    use Google\Cloud\Bigtable\Admin\V2\ModifyColumnFamiliesRequest;
    use Google\Cloud\Bigtable\Admin\V2\ModifyColumnFamiliesRequest\Modification;
    
    /**
     * Create a new column family with a max versions GC rule
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance where the table resides
     * @param string $tableId The ID of the table in which the rule needs to be created
     */
    function create_family_gc_max_versions(
        string $projectId,
        string $instanceId,
        string $tableId
    ): void {
        $tableAdminClient = new BigtableTableAdminClient();
    
        $tableName = $tableAdminClient->tableName($projectId, $instanceId, $tableId);
    
        print('Creating column family cf2 with max versions GC rule...' . PHP_EOL);
        $columnFamily2 = new ColumnFamily();
        $maxVersionRule = (new GcRule())->setMaxNumVersions(2);
        $columnFamily2->setGCRule($maxVersionRule);
    
        $columnModification = new Modification();
        $columnModification->setId('cf2');
        $columnModification->setCreate($columnFamily2);
        $modifyColumnFamiliesRequest = (new ModifyColumnFamiliesRequest())
            ->setName($tableName)
            ->setModifications([$columnModification]);
        $tableAdminClient->modifyColumnFamilies($modifyColumnFamiliesRequest);
    
        print('Created column family cf2 with Max Versions GC Rule.' . PHP_EOL);
    }

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    # Create a column family with GC policy : most recent N versions
    # where 1 = most recent version
    max_versions_rule = Google::Cloud::Bigtable::GcRule.max_versions 2
    column_families = table.column_families do |cfs|
      cfs.add "cf2", gc_rule: max_versions_rule
    end
    family = column_families["cf2"]

### Garbage collection based on multiple criteria

The following section demonstrate how to create a column family with an [intersection](https://docs.cloud.google.com/bigtable/docs/garbage-collection#intersection) garbage collection policy.

###  Console 

To set an intersection garbage collection policy for cells in a column family:

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance whose tables you want to view.

  3. Click **Tables** in the left pane.

The Tables page displays a list of tables in the instance.

  4. Click edit **Edit** in the table's row.

  5. Click keyboard_arrow_down **Open** next to the column family that you want to edit.

  6. Select **Custom policy**.

  7. Enter a garbage collection rule in the text area, setting values for `maxage`, `maxversions`, or both. Acceptable age units are **ms** , **s** , **m** , **h** , and **d** , which stand for milliseconds, seconds, minutes, hours, and days.

For example, to remove cells that are older than five days _and_ older than the two most recent cells, enter the following. Cells must meet _both_ criteria to be removed.
         
         maxage=5d and maxversions=2
         

  8. Click **Save**.




### cbt

This example creates a column family named `cf4`, then sets a garbage collection policy that removes cells that are older than five days _and_ older than the two most recent cells for all columns in the column family. Cells must meet _both_ criteria to be removed.
    
    
    cbt createfamily your-table cf4
    cbt setgcpolicy your-table cf4 maxage=5d and maxversions=2
    

This example sets a policy that removes all cells more than 14 days old except the newest one.
    
    
    cbt setgcpolicy your-table cf4 maxage=14d and maxversions=1
    

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    // Create a column family with GC policy to drop data that matches all conditions
    
    // GC rule: Drop cells older than 5 days AND older than the most recent 2 versions
    const intersectionRule = GcRuleBuilder.intersection(
      GcRuleBuilder.rule({
        maxVersions: 2,
      }),
      GcRuleBuilder.rule({
        maxAge: {
          seconds: 60 * 60 * 24 * 5,
          nanos: 0,
        },
      }),
    );
    [family] = await adminClient.modifyColumnFamilies({
      name: table.name,
      modifications: [
        {
          id: 'cf4',
          create: {
            gcRule: intersectionRule,
          },
        },
      ],
    });
    console.log(`Created column family ${family.name}`);

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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
    

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    # Create a column family with GC policy to drop data that matches at least
    # one condition
    max_age_rule = Google::Cloud::Bigtable::GcRule.max_age 60 * 60 * 24 * 5
    max_versions_rule = Google::Cloud::Bigtable::GcRule.max_versions 2
    intersection_gc_rule = Google::Cloud::Bigtable::GcRule.intersection max_age_rule, max_versions_rule
    column_families = table.column_families do |cfs|
      cfs.add "cf4", gc_rule: intersection_gc_rule
    end
    family = column_families["cf4"]

The following section shows how to create a column family that has a [union](https://docs.cloud.google.com/bigtable/docs/garbage-collection#union) garbage collection policy.

###  Console 

To set a union garbage collection policy for cells in a column family:

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance whose tables you want to view.

  3. Click **Tables** in the left pane.

The Tables page displays a list of tables in the instance.

  4. Click edit **Edit** in the table's row.

  5. Click keyboard_arrow_down **Open** next to the column family that you want to edit.

  6. Select **Custom policy**.

  7. Enter a garbage collection rule in the text area, setting values for `maxage`, `maxversions`, or both. Acceptable age units are **ms** , **s** , **m** , **h** , and **d** , which stand for milliseconds, seconds, minutes, hours, and days.

For example, to remove cells that are more than five days old _or_ are older than the two most recent cells, enter the following. Cells must meet _either_ criteria to be removed.
         
         maxage=5d or maxversions=2
         

  8. Click **Save**.




### cbt

This example creates a column family named `cf3`, then sets a garbage collection policy that removes cells that are more than five days old _or_ are older than the two most recent cells. Cells must meet _either_ conditions to be removed.
    
    
    cbt createfamily your-table cf3
    cbt setgcpolicy your-table cf3 maxage=5d or maxversions=2
    

This example sets a policy that removes all cell values except the newest one, but removes even the newest cell if it is more than one second old.
    
    
    cbt setgcpolicy your-table cf3 maxversions=1 or maxage=1s
    

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/bigtable"
    )
    
    func createFamilyGCUnion(w io.Writer, projectID, instanceID string, tableName string) error {
    	// projectID := "my-project-id"
    	// instanceID := "my-instance-id"
    	// tableName := "my-table-name"
    
    	ctx := context.Background()
    
    	adminClient, err := bigtable.[NewAdminClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_AdminClient_NewAdminClient)(ctx, projectID, instanceID)
    	if err != nil {
    		return fmt.Errorf("bigtable.NewAdminClient: %w", err)
    	}
    	defer adminClient.Close()
    
    	columnFamilyName := "cf3"
    	if err := adminClient.[CreateColumnFamily](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_AdminClient_CreateColumnFamily)(ctx, tableName, columnFamilyName); err != nil {
    		return fmt.Errorf("CreateColumnFamily(%s): %w", columnFamilyName, err)
    	}
    
    	// Define a GC rule to drop cells older than 5 days or not the most recent version
    	maxAge := time.Hour * 24 * 5
    	maxAgePolicy := bigtable.[MaxAgePolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_GCPolicy_MaxAgePolicy)(maxAge)
    	policy := bigtable.[UnionPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_GCPolicy_UnionPolicy)(bigtable.[MaxVersionsPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_GCPolicy_MaxVersionsPolicy)(2), maxAgePolicy)
    	if err := adminClient.[SetGCPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_AdminClient_SetGCPolicy)(ctx, tableName, columnFamilyName, policy); err != nil {
    		return fmt.Errorf("SetGCPolicy(%s): %w", policy, err)
    	}
    
    	fmt.Fprintf(w, "created column family %s with policy: %v\n", columnFamilyName, policy)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    // Creates a column family with GC policy to drop data that matches at least one condition.
    
    // Defines a list of GC rules to drop cells older than 5 days OR not the most recent
    // version.
    GcRule unionRule =
        GcRuleBuilder.union()
            .add(GcRuleBuilder.maxAge(Duration.ofDays(5)))
            .add(GcRuleBuilder.maxVersions(1))
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
                      .setId(COLUMN_FAMILY_3)
                      .setCreate(ColumnFamily.newBuilder().setGcRule(unionRule)))
              .build();
      adminClient.modifyColumnFamilies(request);
      System.out.println("Created column family: " + COLUMN_FAMILY_3);
    } catch (AlreadyExistsException e) {
      System.err.println(
          "Failed to create column family with rule, already exists: " + e.getMessage());
    }

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    print("Creating column family cf3 with union GC rule...")
    # Create a column family with GC policy to drop data that matches
    # at least one condition.
    # Define a GC rule to drop cells older than 5 days or not the
    # most recent version
    union_rule = column_family.GCRuleUnion(
        [
            column_family.MaxAgeGCRule(datetime.timedelta(days=5)),
            column_family.MaxVersionsGCRule(2),
        ]
    )
    
    column_family3 = table.column_family("cf3", union_rule)
    column_family3.create()
    print("Created column family cf3 with Union GC rule")
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    // Create a column family with GC policy to drop data that matches at least one condition.
    // Initialize request argument(s).
    // Define a GC rule to drop cells older than 5 days or not the most recent version.
    GcRule.Types.Union unionRule = new GcRule.Types.Union
    {
        Rules =
        {
            new GcRule { MaxNumVersions = 1 },
            new GcRule { MaxAge = Duration.FromTimeSpan(TimeSpan.FromDays(5)) }
        }
    };
    GcRule gcRule = new GcRule { Union = unionRule };
    
    // Column family to create
    ColumnFamily columnFamily = new ColumnFamily { GcRule = gcRule };
    
    TableName tableName = new TableName(projectId, instanceId, tableId);
    
    // Modification to create column family
    ModifyColumnFamiliesRequest.Types.Modification modification = new ModifyColumnFamiliesRequest.Types.Modification
    {
        Create = columnFamily,
        Id = "cf3"
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

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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
      auto& gc_union = *mod.mutable_create()->mutable_gc_rule()->mutable_union_();
      gc_union.add_rules()->set_max_num_versions(1);
      gc_union.add_rules()->mutable_max_age()->set_seconds(5 * kSecondsPerDay);
    
      StatusOr<google::bigtable::admin::v2::Table> schema =
          admin.ModifyColumnFamilies(table_name, {std::move(mod)});
    
      if (!schema) throw std::move(schema).status();
      std::cout << "Schema modified to: " << schema->DebugString() << "\n";
    }

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    // Create a column family with GC policy to drop data that matches at least one condition.
    
    // Define a GC rule to drop cells older than 5 days or not the most recent version
    const unionRule = GcRuleBuilder.union(
      GcRuleBuilder.rule({
        maxVersions: 1,
      }),
      GcRuleBuilder.rule({
        maxAge: {
          seconds: 60 * 60 * 24 * 5,
          nanos: 0,
        },
      }),
    );
    
    [family] = await adminClient.modifyColumnFamilies({
      name: table.name,
      modifications: [
        {
          id: 'cf3',
          create: {
            gcRule: unionRule,
          },
        },
      ],
    });
    console.log(`Created column family ${family.name}`);

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\ColumnFamily;
    use Google\Cloud\Bigtable\Admin\V2\GcRule;
    use Google\Cloud\Bigtable\Admin\V2\GcRule\Union as GcRuleUnion;
    use Google\Cloud\Bigtable\Admin\V2\ModifyColumnFamiliesRequest;
    use Google\Cloud\Bigtable\Admin\V2\ModifyColumnFamiliesRequest\Modification;
    use Google\Protobuf\Duration;
    
    /**
     * Create a new column family with a union GC rule
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance where the table resides
     * @param string $tableId The ID of the table in which the rule needs to be created
     */
    function create_family_gc_union(
        string $projectId,
        string $instanceId,
        string $tableId
    ): void {
        $tableAdminClient = new BigtableTableAdminClient();
    
        $tableName = $tableAdminClient->tableName($projectId, $instanceId, $tableId);
    
        print('Creating column family cf3 with union GC rule...' . PHP_EOL);
        // Create a column family with GC policy to drop data that matches
        // at least one condition.
        // Define a GC rule to drop cells older than 5 days or not the
        // most recent version
    
        $columnFamily3 = new ColumnFamily();
    
        $ruleUnion = new GcRuleUnion();
        $ruleUnionArray = [
            (new GcRule())->setMaxNumVersions(2),
            (new GcRule())->setMaxAge((new Duration())->setSeconds(3600 * 24 * 5))
        ];
        $ruleUnion->setRules($ruleUnionArray);
        $union = new GcRule();
        $union->setUnion($ruleUnion);
    
        $columnFamily3->setGCRule($union);
    
        $columnModification = new Modification();
        $columnModification->setId('cf3');
        $columnModification->setCreate($columnFamily3);
        $modifyColumnFamiliesRequest = (new ModifyColumnFamiliesRequest())
            ->setName($tableName)
            ->setModifications([$columnModification]);
        $tableAdminClient->modifyColumnFamilies($modifyColumnFamiliesRequest);
    
        print('Created column family cf3 with Union GC rule.' . PHP_EOL);
    }

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    # Create a column family with GC policy to drop data that matches at least
    # one condition
    max_age_rule = Google::Cloud::Bigtable::GcRule.max_age 60 * 60 * 24 * 5
    max_versions_rule = Google::Cloud::Bigtable::GcRule.max_versions 2
    union_gc_rule = Google::Cloud::Bigtable::GcRule.union max_age_rule, max_versions_rule
    column_families = table.column_families do |cfs|
      cfs.add "cf3", gc_rule: union_gc_rule
    end
    family = column_families["cf3"]

The following section shows how to create a column family that has a **nested** garbage collection policy. A nested garbage collection policy has a combination of union and intersection rules.

###  Console 

To set a nested garbage collection policy for cells in a column family:

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance whose tables you want to view.

  3. Click **Tables** in the left pane.

The Tables page displays a list of tables in the instance.

  4. Click edit **Edit** in the table's row.

  5. Click keyboard_arrow_down **Open** next to the column family that you want to edit.

  6. Select **Custom policy**.

  7. Enter a garbage collection rule in the text area, setting values for `maxage`, `maxversions`, or both. Acceptable age units are **ms** , **s** , **m** , **h** , and **d** , which stand for milliseconds, seconds, minutes, hours, and days.

For example, to keep the two newest cells even if they are more than one minute old, or keep the ten newest cells as long as they are less than one minute old, enter the following:
         
         (maxage=1m and maxversions=2) or maxversions=10
         

  8. Click **Save**.




### cbt

This example creates a column family named `cf5`, then sets a garbage collection policy that removes cells in the column family that meet _either_ of the following conditions:

  * Older than the ten most recent cells
  * More than one minute old _and_ older than the two most recent cells



In other words, this policy keeps the two newest cells even if they are more than one minute old, or keeps the ten newest cells as long as they are less than one minute old.
    
    
    cbt createfamily your-table cf5
    cbt setgcpolicy your-table cf5 "(maxage=1m and maxversions=2) or
    maxversions=10"
    

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    // Create a nested GC rule:
    // Drop cells that are either older than the 10 recent versions
    // OR
    // Drop cells that are older than a month AND older than the 2 recent versions
    const nestedRule = GcRuleBuilder.union(
      GcRuleBuilder.rule({
        maxVersions: 10,
      }),
      GcRuleBuilder.intersection(
        GcRuleBuilder.rule({
          maxVersions: 2,
        }),
        GcRuleBuilder.rule({
          maxAge: {
            // one month
            seconds: 60 * 60 * 24 * 30,
            nanos: 0,
          },
        }),
      ),
    );
    
    [family] = await adminClient.modifyColumnFamilies({
      name: table.name,
      modifications: [
        {
          id: 'cf5',
          create: {
            gcRule: nestedRule,
          },
        },
      ],
    });
    console.log(`Created column family ${family.name}`);

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    # Create a nested GC rule:
    # Drop cells that are either older than the 10 recent versions
    # OR
    # Drop cells that are older than a month AND older than the 2 recent versions
    max_versions_rule1 = Google::Cloud::Bigtable::GcRule.max_versions 10
    max_age_rule = Google::Cloud::Bigtable::GcRule.max_age 60 * 60 * 24 * 5
    max_versions_rule2 = Google::Cloud::Bigtable::GcRule.max_versions 2
    intersection_gc_rule = Google::Cloud::Bigtable::GcRule.intersection max_age_rule, max_versions_rule2
    nested_gc_rule = Google::Cloud::Bigtable::GcRule.union max_versions_rule1, intersection_gc_rule

## Update a garbage collection policy

The following section demonstrates how to modify an existing garbage collection policy.

To increase the retention period for a column family in a table that uses replication, you must acknowledge a warning about the potential for your clusters to become out of sync. The new value must be no more than 90 days more than the current value. For details, see [Changing age-based policies](https://docs.cloud.google.com/bigtable/docs/garbage-collection#change-age-based).

###  Console 

To update the garbage collection policy for a column family, follow these steps.

**Note:** You can't use the console to increase the value of `max age` in a replicated table. Use the `cbt` CLI instead.

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance whose tables you want to view.

  3. Click **Tables** in the left pane.

The Tables page displays a list of tables in the instance.

  4. Click edit **Edit** in the table's row.

  5. Click keyboard_arrow_down **Open** next to the column family that you want to edit.

  6. Set the policy.

  7. Click **Save**.




### cbt
    
    
    cbt setgcpolicy your-table cf1 maxage=1d
    

If you increase the value of `maxage` in a replicated table, you must use the optional `force` flag. The new value must be no more than 90 days more than the current value.

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    print("Updating column family cf1 GC rule...")
    # Update the column family cf1 to update the GC rule
    column_family1 = table.column_family("cf1", column_family.MaxVersionsGCRule(1))
    column_family1.update()
    print("Updated column family cf1 GC rule\n")
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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
    

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    // Update the column family metadata to update the GC rule
    
    // Update a column family GC rule
    const updatedMetadata = GcRuleBuilder.rule({
      maxNumVersions: 1,
    });
    
    const [apiResponse] = await adminClient.modifyColumnFamilies({
      name: table.name,
      modifications: [
        {
          id: 'cf1',
          update: {
            gcRule: updatedMetadata,
          },
        },
      ],
    });
    console.log(`Updated GC rule: ${JSON.stringify(apiResponse)}`);

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    gc_rule = Google::Cloud::Bigtable::GcRule.max_versions 1
    column_families = table.column_families do |cfs|
      cfs.update "cf1", gc_rule: gc_rule
    end
    p column_families["cf1"]

## What's next

  * [Look at additional code samples](https://docs.cloud.google.com/bigtable/docs/samples).
  * [Explore strategies to simulate cell-level TTL](https://docs.cloud.google.com/bigtable/docs/gc-cell-level).
  * [Read about how timestamps that are sequential numbers affect garbage collection](https://docs.cloud.google.com/bigtable/docs/gc-sequence-numbers).
  * [Learn how to keep only the most recent value of a column](https://docs.cloud.google.com/bigtable/docs/gc-latest-value).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
