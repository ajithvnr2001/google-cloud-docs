---
url: https://docs.cloud.google.com/spanner/docs/samples/spanner-query-data-with-array-of-struct/
title: Query data with array of STRUCT \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:37.718584+00:00
---

# Query data with array of STRUCT  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/samples/spanner-query-data-with-array-of-struct/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Samples ](https://docs.cloud.google.com/spanner/docs/samples)



#  Query data with array of STRUCT Stay organized with collections  Save and categorize content based on your preferences. 

Query data by using an array of STRUCT objects.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Working with STRUCT objects](https://docs.cloud.google.com/spanner/docs/structs)



## Code sample

### C++

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    void QueryDataWithArrayOfStruct(google::cloud::spanner::Client client) {
      namespace spanner = ::google::cloud::spanner;
      // Cloud Spanner STRUCT<> types with named fields are represented by
      // std::tuple<std::pair<std::string, T>...>, create an alias to make it easier
      // to follow this code.
      using SingerName = std::tuple<std::pair<std::string, std::string>,
                                    std::pair<std::string, std::string>>;
      auto make_name = [](std::string first_name, std::string last_name) {
        return std::make_tuple(std::make_pair("FirstName", std::move(first_name)),
                               std::make_pair("LastName", std::move(last_name)));
      };
      std::vector<SingerName> singer_info{
          make_name("Elena", "Campbell"),
          make_name("Gabriel", "Wright"),
          make_name("Benjamin", "Martinez"),
      };
    
      auto rows = client.ExecuteQuery(spanner::SqlStatement(
          "SELECT SingerId FROM Singers"
          " WHERE STRUCT<FirstName STRING, LastName STRING>(FirstName, LastName)"
          "    IN UNNEST(@names)",
          {{"names", spanner::Value(singer_info)}}));
    
      for (auto& row : spanner::StreamOf<std::tuple<std::int64_t>>(rows)) {
        if (!row) throw std::move(row).status();
        std::cout << "SingerId: " << std::get<0>(*row) << "\n";
      }
      std::cout << "Query completed for"
                << " [spanner_query_data_with_array_of_struct]\n";
    }

### C#

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Spanner.Data](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.html);
    using System.Collections.Generic;
    using System.Threading.Tasks;
    
    public class QueryDataWithArrayOfStructAsyncSample
    {
        public async Task<List<int>> QueryDataWithArrayOfStructAsync(string projectId, string instanceId, string databaseId)
        {
            var nameType = new [SpannerStruct](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerStruct.html)
            {
                { "FirstName", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[String](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_String), null},
                { "LastName", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[String](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_String), null}
            };
    
            var bandMembers = new List<SpannerStruct>
            {
                new [SpannerStruct](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerStruct.html) { { "FirstName", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[String](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_String), "Elena" }, { "LastName", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[String](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_String), "Campbell" } },
                new [SpannerStruct](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerStruct.html) { { "FirstName", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[String](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_String), "Gabriel" }, { "LastName", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[String](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_String), "Wright" } },
                new [SpannerStruct](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerStruct.html) { { "FirstName", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[String](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_String), "Benjamin" }, { "LastName", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[String](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_String), "Martinez" } },
            };
    
            var singerIds = new List<int>();
            string connectionString = $"Data Source=projects/{projectId}/instances/{instanceId}/databases/{databaseId}";
            using var connection = new [SpannerConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html)(connectionString);
            using var cmd = connection.[CreateSelectCommand](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_CreateSelectCommand_System_String_Google_Cloud_Spanner_Data_SpannerParameterCollection_)(
                "SELECT SingerId FROM Singers WHERE STRUCT<FirstName STRING, LastName STRING> "
                + "(FirstName, LastName) IN UNNEST(@names)");
            cmd.[Parameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerCommand.html#Google_Cloud_Spanner_Data_SpannerCommand_Parameters).Add("names", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[ArrayOf](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_ArrayOf_Google_Cloud_Spanner_Data_SpannerDbType_)(nameType.[GetSpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerStruct.html#Google_Cloud_Spanner_Data_SpannerStruct_GetSpannerDbType)()), bandMembers);
            using var reader = await cmd.[ExecuteReaderAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerCommand.html#Google_Cloud_Spanner_Data_SpannerCommand_ExecuteReaderAsync)();
            while (await reader.[ReadAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDataReader.html#Google_Cloud_Spanner_Data_SpannerDataReader_ReadAsync_System_Threading_CancellationToken_)())
            {
                singerIds.Add(reader.GetFieldValue<int>("SingerId"));
            }
            return singerIds;
        }
    }

### Go

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    stmt := spanner.Statement{
    	SQL: `SELECT SingerId FROM SINGERS
    		WHERE STRUCT<FirstName STRING, LastName STRING>(FirstName, LastName)
    		IN UNNEST(@names)`,
    	Params: map[string]interface{}{"names": bandMembers},
    }
    iter := client.Single().Query(ctx, stmt)
    defer iter.Stop()
    for {
    	row, err := iter.Next()
    	if err == iterator.Done {
    		return nil
    	}
    	if err != nil {
    		return err
    	}
    	var singerID int64
    	if err := row.Columns(&singerID); err != nil {
    		return err
    	}
    	fmt.Fprintf(w, "%d\n", singerID)
    }
    

### Java

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    Statement s =
        Statement.newBuilder(
                "SELECT SingerId FROM Singers WHERE "
                    + "STRUCT<FirstName STRING, LastName STRING>(FirstName, LastName) "
                    + "IN UNNEST(@names) "
                    + "ORDER BY SingerId DESC")
            .bind("names")
            .toStructArray(nameType, bandMembers)
            .build();
    try (ResultSet resultSet = dbClient.singleUse().executeQuery(s)) {
      while (resultSet.next()) {
        System.out.printf("%d\n", resultSet.getLong("SingerId"));
      }
    }

### Node.js

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const query = {
      sql:
        'SELECT SingerId FROM Singers ' +
        'WHERE STRUCT<FirstName STRING, LastName STRING>(FirstName, LastName) ' +
        'IN UNNEST(@names) ' +
        'ORDER BY SingerId',
      params: {
        names: bandMembers,
      },
      types: {
        names: bandMembersType,
      },
    };
    
    // Queries rows from the Singers table
    try {
      const [rows] = await database.run(query);
    
      rows.forEach(row => {
        const json = row.toJSON();
        console.log(`SingerId: ${json.SingerId}`);
      });
    } catch (err) {
      console.error('ERROR:', err);
    } finally {
      // Close the database when finished.
      await database.close();
    }

### PHP

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $results = $database->execute(
        'SELECT SingerId FROM Singers ' .
        'WHERE STRUCT<FirstName STRING, LastName STRING>(FirstName, LastName) ' .
        'IN UNNEST(@names)',
        [
            'parameters' => [
                'names' => $bandMembers
            ],
            'types' => [
                'names' => $nameType
            ]
        ]
    );
    foreach ($results as $row) {
        printf('SingerId: %s' . PHP_EOL,
            $row['SingerId']);
    }

### Python

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)
    
    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT SingerId FROM Singers WHERE "
            "STRUCT<FirstName STRING, LastName STRING>"
            "(FirstName, LastName) IN UNNEST(@names)",
            params={"names": band_members},
            param_types={"names": param_types.Array(name_type)},
        )
    
    for row in results:
        print("SingerId: {}".format(*row))

### Ruby

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    client.execute(
      "SELECT SingerId FROM Singers WHERE " +
      "STRUCT<FirstName STRING, LastName STRING>(FirstName, LastName) IN UNNEST(@names)",
      params: { names: band_members }
    ).rows.each do |row|
      puts row[:SingerId]
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudspanner). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
