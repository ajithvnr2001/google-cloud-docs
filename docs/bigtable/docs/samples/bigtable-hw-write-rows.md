---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-hw-write-rows/
title: Insert using mutate \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:48.712396+00:00
---

# Insert using mutate  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-hw-write-rows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Insert using mutate Stay organized with collections  Save and categorize content based on your preferences. 

Insert rows using mutate.

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
    
    
    std::vector<std::string> greetings{"Hello World!", "Hello Cloud Bigtable!",
                                       "Hello C++!"};
    int i = 0;
    for (auto const& greeting : greetings) {
      // Each row has a unique row key.
      //
      // Note: This example uses sequential numeric IDs for simplicity, but
      // this can result in poor performance in a production application.
      // Since rows are stored in sorted order by key, sequential keys can
      // result in poor distribution of operations across nodes.
      //
      // For more information about how to design a Bigtable schema for the
      // best performance, see the documentation:
      //
      //     https://cloud.google.com/bigtable/docs/schema-design
      std::string row_key = "key-" + std::to_string(i);
      google::cloud::Status status = table.Apply(cbt::SingleRowMutation(
          std::move(row_key), cbt::SetCell("family", "c0", greeting)));
    
      if (!status.ok()) throw std::runtime_error(status.message());
      ++i;
    }

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Initialize Google.Cloud.Bigtable.V2.TableName object.
    Google.Cloud.Bigtable.Common.V2.TableName tableName = new Google.Cloud.Bigtable.Common.V2.TableName(projectId, instanceId, tableId);
    
    // Write some rows
    /* Each row has a unique row key.
    
           Note: This example uses sequential numeric IDs for simplicity, but
           this can result in poor performance in a production application.
           Since rows are stored in sorted order by key, sequential keys can
           result in poor distribution of operations across nodes.
    
           For more information about how to design a Bigtable schema for the
           best performance, see the documentation:
    
           https://cloud.google.com/bigtable/docs/schema-design */
    
    Console.WriteLine($"Write some greetings to the table {tableId}");
    
    // Insert 1 row using MutateRow()
    s_greetingIndex = 0;
    try
    {
        bigtableClient.MutateRow(tableName, rowKeyPrefix + s_greetingIndex, MutationBuilder());
        Console.WriteLine($"\tGreeting:   -- {s_greetings[s_greetingIndex],-18}-- written successfully");
    }
    catch (Exception ex)
    {
        Console.WriteLine($"\tFailed to write greeting: --{s_greetings[s_greetingIndex]}");
        Console.WriteLine(ex.Message);
        throw;
    }
    
    // Insert multiple rows using MutateRows()
    // Build a MutateRowsRequest (contains table name and a collection of entries).
    MutateRowsRequest request = new MutateRowsRequest
    {
        TableNameAsTableName = tableName
    };
    
    s_mapToOriginalGreetingIndex = new List<int>();
    while (++s_greetingIndex < s_greetings.Length)
    {
        s_mapToOriginalGreetingIndex.Add(s_greetingIndex);
        // Build an entry for every greeting (consists of rowkey and a collection of mutations).
        string rowKey = rowKeyPrefix + s_greetingIndex;
        request.Entries.Add(Mutations.CreateEntry(rowKey, MutationBuilder()));
    }
    
    // Make the request to write multiple rows.
    MutateRowsResponse response = bigtableClient.MutateRows(request);
    
    // Check the status code of each entry to ensure that it was written successfully.
    foreach (MutateRowsResponse.Types.Entry entry in response.Entries)
    {
        s_greetingIndex = s_mapToOriginalGreetingIndex[(int)entry.Index];
        if (entry.Status.Code == 0)
        {
            Console.WriteLine($"\tGreeting:   -- {s_greetings[s_greetingIndex],-18}-- written successfully");
        }
        else
        {
            Console.WriteLine($"\tFailed to write greeting: --{s_greetings[s_greetingIndex]}");
            Console.WriteLine(entry.Status.Message);
        }
    }
    
    Mutation MutationBuilder() =>
        Mutations.SetCell(columnFamily, columnName, s_greetings[s_greetingIndex], new BigtableVersion(DateTime.UtcNow));

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    tbl := client.Open(tableName)
    muts := make([]*bigtable.Mutation, len(greetings))
    rowKeys := make([]string, len(greetings))
    
    log.Printf("Writing greeting rows to table")
    for i, greeting := range greetings {
    	muts[i] = bigtable.NewMutation()
    	muts[i].Set(columnFamilyName, columnName, bigtable.Now(), []byte(greeting))
    
    	// Each row has a unique row key.
    	//
    	// Note: This example uses sequential numeric IDs for simplicity, but
    	// this can result in poor performance in a production application.
    	// Since rows are stored in sorted order by key, sequential keys can
    	// result in poor distribution of operations across nodes.
    	//
    	// For more information about how to design a Bigtable schema for the
    	// best performance, see the documentation:
    	//
    	//     https://cloud.google.com/bigtable/docs/schema-design
    	rowKeys[i] = fmt.Sprintf("%s%d", columnName, i)
    }
    
    rowErrs, err := tbl.ApplyBulk(ctx, rowKeys, muts)
    if err != nil {
    	log.Fatalf("Could not apply bulk row mutation: %v", err)
    }
    if rowErrs != nil {
    	for _, rowErr := range rowErrs {
    		log.Printf("Error writing row: %v", rowErr)
    	}
    	log.Fatalf("Could not write some rows")
    }

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    try {
      System.out.println("\nWriting some greetings to the table");
      String[] names = {"World", "Bigtable", "Java"};
      for (int i = 0; i < names.length; i++) {
        String greeting = "Hello " + names[i] + "!";
        RowMutation rowMutation =
            RowMutation.create(TableId.of(tableId), ROW_KEY_PREFIX + i)
                .setCell(COLUMN_FAMILY, COLUMN_QUALIFIER_NAME, names[i])
                .setCell(COLUMN_FAMILY, COLUMN_QUALIFIER_GREETING, greeting);
        dataClient.mutateRow(rowMutation);
        System.out.println(greeting);
      }
    } catch (NotFoundException e) {
      System.err.println("Failed to write to non-existent table: " + e.getMessage());
    }

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    print("Writing some greetings to the table.")
    greetings = [b"Hello World!", b"Hello Cloud Bigtable!", b"Hello Python!"]
    rows = []
    column = b"greeting"
    for i, value in enumerate(greetings):
        # Note: This example uses sequential numeric IDs for simplicity,
        # but this can result in poor performance in a production
        # application.  Since rows are stored in sorted order by key,
        # sequential keys can result in poor distribution of operations
        # across nodes.
        #
        # We recommend that you use bytestrings directly for row keys
        # where possible, rather than encoding strings.
        #
        # For more information about how to design a Bigtable schema for
        # the best performance, see the documentation:
        #
        #     https://cloud.google.com/bigtable/docs/schema-design
        row_key = f"greeting{i}".encode()
        row = table.direct_row(row_key)
        row.set_cell(
            column_family_id,
            column,
            value,
            timestamp=datetime.now(timezone.utc),
        )
        rows.append(row)
    table.mutate_rows(rows)

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    puts "Write some greetings to the table #{table_id}"
    greetings = ["Hello World!", "Hello Bigtable!", "Hello Ruby!"]
    
    # Get a table data object for the new table we created.
    table = bigtable.table instance_id, table_id
    
    # Insert rows one by one
    # Note: To perform multiple mutation on multiple rows use `mutate_rows`.
    greetings.each_with_index do |value, i|
      puts " Writing,  Row key: greeting#{i}, Value: #{value}"
    
      entry = table.new_mutation_entry "greeting#{i}"
      entry.set_cell(
        column_family,
        column_qualifier,
        value,
        timestamp: (Time.now.to_f * 1_000_000).round(-3)
      )
    
      table.mutate_row entry
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
