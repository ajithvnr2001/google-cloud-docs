---
url: https://docs.cloud.google.com/spanner/docs/samples/spanner-field-access-on-nested-struct-parameters/
title: Field access on nested STRUCT \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:35.487339+00:00
---

# Field access on nested STRUCT  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/samples/spanner-field-access-on-nested-struct-parameters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Samples ](https://docs.cloud.google.com/spanner/docs/samples)



#  Field access on nested STRUCT Stay organized with collections  Save and categorize content based on your preferences. 

Query data using field access on a nested STRUCT.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Working with STRUCT objects](https://docs.cloud.google.com/spanner/docs/structs)



## Code sample

### C++

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    void FieldAccessOnNestedStruct(google::cloud::spanner::Client client) {
      namespace spanner = ::google::cloud::spanner;
    
      // Cloud Spanner STRUCT<> with named fields is represented as
      // tuple<pair<string, T>...>. Create a type alias for this example:
      using SingerFullName = std::tuple<std::pair<std::string, std::string>,
                                        std::pair<std::string, std::string>>;
      auto make_name = [](std::string fname, std::string lname) {
        return SingerFullName({"FirstName", std::move(fname)},
                              {"LastName", std::move(lname)});
      };
      using SongInfo =
          std::tuple<std::pair<std::string, std::string>,
                     std::pair<std::string, std::vector<SingerFullName>>>;
      auto songinfo = SongInfo(
          {"SongName", "Imagination"},
          {"ArtistNames",
           {make_name("Elena", "Campbell"), make_name("Hannah", "Harris")}});
    
      auto rows = client.ExecuteQuery(spanner::SqlStatement(
          "SELECT SingerId, @songinfo.SongName FROM Singers"
          " WHERE STRUCT<FirstName STRING, LastName STRING>(FirstName, LastName)"
          "    IN UNNEST(@songinfo.ArtistNames)",
          {{"songinfo", spanner::Value(songinfo)}}));
    
      using RowType = std::tuple<std::int64_t, std::string>;
      for (auto& row : spanner::StreamOf<RowType>(rows)) {
        if (!row) throw std::move(row).status();
        std::cout << "SingerId: " << std::get<0>(*row)
                  << " SongName: " << std::get<1>(*row) << "\n";
      }
      std::cout << "Query completed for [spanner_field_access_on_nested_struct]\n";
    }

### C#

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Spanner.Data](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.html);
    using System;
    using System.Collections.Generic;
    using System.Threading.Tasks;
    
    public class QueryDataWithNestedStructFieldAsyncSample
    {
        public async Task<List<int>> QueryDataWithNestedStructFieldAsync(string projectId, string instanceId, string databaseId)
        {
            string connectionString = $"Data Source=projects/{projectId}/instances/{instanceId}/databases/{databaseId}";
    
            [SpannerStruct](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerStruct.html) name1 = new [SpannerStruct](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerStruct.html)
            {
                { "FirstName", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[String](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_String), "Elena" },
                { "LastName", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[String](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_String), "Campbell" }
            };
            [SpannerStruct](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerStruct.html) name2 = new [SpannerStruct](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerStruct.html)
            {
                { "FirstName", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[String](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_String), "Hannah" },
                { "LastName", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[String](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_String), "Harris" }
            };
            [SpannerStruct](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerStruct.html) songInfo = new [SpannerStruct](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerStruct.html)
            {
                { "song_name", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[String](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_String), "Imagination" },
                { "artistNames", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[ArrayOf](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_ArrayOf_Google_Cloud_Spanner_Data_SpannerDbType_)(name1.[GetSpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerStruct.html#Google_Cloud_Spanner_Data_SpannerStruct_GetSpannerDbType)()), new[] { name1, name2 } }
            };
    
            var singerIds = new List<int>();
            using var connection = new [SpannerConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html)(connectionString);
            using var cmd = connection.[CreateSelectCommand](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_CreateSelectCommand_System_String_Google_Cloud_Spanner_Data_SpannerParameterCollection_)(
                "SELECT SingerId, @song_info.song_name "
                + "FROM Singers WHERE STRUCT<FirstName STRING, LastName STRING>(FirstName, LastName) "
                + "IN UNNEST(@song_info.artistNames)");
    
            cmd.[Parameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerCommand.html#Google_Cloud_Spanner_Data_SpannerCommand_Parameters).Add("song_info", songInfo.[GetSpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerStruct.html#Google_Cloud_Spanner_Data_SpannerStruct_GetSpannerDbType)(), songInfo);
    
            using var reader = await cmd.[ExecuteReaderAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerCommand.html#Google_Cloud_Spanner_Data_SpannerCommand_ExecuteReaderAsync)();
            while (await reader.[ReadAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDataReader.html#Google_Cloud_Spanner_Data_SpannerDataReader_ReadAsync_System_Threading_CancellationToken_)())
            {
                var singerId = reader.GetFieldValue<int>("SingerId");
                singerIds.Add(singerId);
                Console.WriteLine($"SingerId: {singerId}");
                Console.WriteLine($"Song Name: {reader.GetFieldValue<string>(1)}");
            }
            return singerIds;
        }
    }

### Go

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/spanner"
    	"google.golang.org/api/iterator"
    )
    
    func queryWithNestedStructField(w io.Writer, db string) error {
    	ctx := context.Background()
    
    	client, err := spanner.NewClient(ctx, db)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	type nameType struct {
    		FirstName string
    		LastName  string
    	}
    	type songInfoStruct struct {
    		SongName    string
    		ArtistNames []nameType
    	}
    	var songInfo = songInfoStruct{
    		SongName: "Imagination",
    		ArtistNames: []nameType{
    			{FirstName: "Elena", LastName: "Campbell"},
    			{FirstName: "Hannah", LastName: "Harris"},
    		},
    	}
    	stmt := spanner.[Statement](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Statement){
    		SQL: `SELECT SingerId, @songinfo.SongName FROM Singers
    			WHERE STRUCT<FirstName STRING, LastName STRING>(FirstName, LastName)
    			IN UNNEST(@songinfo.ArtistNames)`,
    		Params: map[string]interface{}{"songinfo": songInfo},
    	}
    	iter := client.[Single](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Client_Single)().Query(ctx, stmt)
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
    		var songName string
    		if err := row.[Columns](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Row_Columns)(&singerID, &songName); err != nil {
    			return err
    		}
    		fmt.Fprintf(w, "%d %s\n", singerID, songName)
    	}
    }
    

### Java

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static void queryNestedStructField(DatabaseClient dbClient) {
      Type nameType =
          Type.struct(
              Arrays.asList(
                  StructField.of("FirstName", Type.string()),
                  StructField.of("LastName", Type.string())));
    
      Struct songInfo =
          Struct.newBuilder()
              .set("song_name")
              .to("Imagination")
              .set("artistNames")
              .toStructArray(
                  nameType,
                  Arrays.asList(
                      Struct.newBuilder()
                          .set("FirstName")
                          .to("Elena")
                          .set("LastName")
                          .to("Campbell")
                          .build(),
                      Struct.newBuilder()
                          .set("FirstName")
                          .to("Hannah")
                          .set("LastName")
                          .to("Harris")
                          .build()))
              .build();
      Statement s =
          Statement.newBuilder(
                  "SELECT SingerId, @song_info.song_name "
                      + "FROM Singers WHERE "
                      + "STRUCT<FirstName STRING, LastName STRING>(FirstName, LastName) "
                      + "IN UNNEST(@song_info.artistNames)")
              .bind("song_info")
              .to(songInfo)
              .build();
      try (ResultSet resultSet = dbClient.singleUse().executeQuery(s)) {
        while (resultSet.next()) {
          System.out.printf("%d %s\n", resultSet.getLong("SingerId"), resultSet.getString(1));
        }
      }
    }

### Node.js

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const {Spanner} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const projectId = 'my-project-id';
    // const instanceId = 'my-instance';
    // const databaseId = 'my-database';
    
    // Creates a client
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({
      projectId: projectId,
    });
    let database;
    try {
      // Gets a reference to a Cloud Spanner instance and database
      const instance = spanner.instance(instanceId);
      database = instance.database(databaseId);
    
      const nameType = {
        type: '[struct](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)',
        fields: [
          {
            name: 'FirstName',
            type: 'string',
          },
          {
            name: 'LastName',
            type: 'string',
          },
        ],
      };
    
      // Creates Song info STRUCT with a nested ArtistNames array
      const songInfoType = {
        type: '[struct](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)',
        fields: [
          {
            name: 'SongName',
            type: 'string',
          },
          {
            name: 'ArtistNames',
            type: 'array',
            child: nameType,
          },
        ],
      };
    
      const songInfoStruct = [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html).[struct](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({
        SongName: 'Imagination',
        ArtistNames: [
          [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html).[struct](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({FirstName: 'Elena', LastName: 'Campbell'}),
          [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html).[struct](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({FirstName: 'Hannah', LastName: 'Harris'}),
        ],
      });
    
      const query = {
        sql:
          'SELECT SingerId, @songInfo.SongName FROM Singers ' +
          'WHERE STRUCT<FirstName STRING, LastName STRING>(FirstName, LastName) ' +
          'IN UNNEST(@songInfo.ArtistNames)',
        params: {
          songInfo: songInfoStruct,
        },
        types: {
          songInfo: songInfoType,
        },
      };
    
      // Queries rows from the Singers table
      const [rows] = await database.run(query);
    
      rows.forEach(row => {
        const json = row.toJSON();
        console.log(`SingerId: ${json.SingerId}, SongName: ${json.SongName}`);
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
    
    
    use Google\Cloud\Spanner\SpannerClient;
    use Google\Cloud\Spanner\Database;
    use Google\Cloud\Spanner\StructType;
    use Google\Cloud\Spanner\StructValue;
    use Google\Cloud\Spanner\ArrayType;
    
    /**
     * Queries sample data from the database using a nested struct field value.
     * Example:
     * ```
     * query_data_with_nested_struct_field($instanceId, $databaseId);
     * ```
     *
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     */
    function query_data_with_nested_struct_field(string $instanceId, string $databaseId): void
    {
        $spanner = new SpannerClient();
        $instance = $spanner->instance($instanceId);
        $database = $instance->database($databaseId);
    
        $nameType = new ArrayType(
            (new StructType)
                ->add('FirstName', Database::TYPE_STRING)
                ->add('LastName', Database::TYPE_STRING)
        );
        $songInfoType = (new StructType)
            ->add('SongName', Database::TYPE_STRING)
            ->add('ArtistNames', $nameType);
        $nameStructValue1 = (new StructValue)
            ->add('FirstName', 'Elena')
            ->add('LastName', 'Campbell');
        $nameStructValue2 = (new StructValue)
            ->add('FirstName', 'Hannah')
            ->add('LastName', 'Harris');
        $songInfoValues = (new StructValue)
            ->add('SongName', 'Imagination')
            ->add('ArtistNames', [$nameStructValue1, $nameStructValue2]);
        $results = $database->execute(
            'SELECT SingerId, @song_info.SongName FROM Singers ' .
            'WHERE STRUCT<FirstName STRING, LastName STRING>(FirstName, LastName) ' .
            'IN UNNEST(@song_info.ArtistNames)',
            [
                'parameters' => [
                    'song_info' => $songInfoValues
                ],
                'types' => [
                    'song_info' => $songInfoType
                ]
            ]
        );
        foreach ($results as $row) {
            printf('SingerId: %s SongName: %s' . PHP_EOL,
                $row['SingerId'], $row['SongName']);
        }
    }

### Python

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def query_nested_struct_field(instance_id, database_id):
        """Query a table using nested field access on a STRUCT parameter."""
        spanner_client = spanner.Client()
        instance = spanner_client.instance(instance_id)
        database = instance.database(database_id)
    
        song_info_type = param_types.Struct(
            [
                param_types.StructField("SongName", param_types.STRING),
                param_types.StructField(
                    "ArtistNames",
                    param_types.Array(
                        param_types.Struct(
                            [
                                param_types.StructField("FirstName", param_types.STRING),
                                param_types.StructField("LastName", param_types.STRING),
                            ]
                        )
                    ),
                ),
            ]
        )
    
        song_info = ("Imagination", [("Elena", "Campbell"), ("Hannah", "Harris")])
    
        with database.snapshot() as snapshot:
            results = snapshot.execute_sql(
                "SELECT SingerId, @song_info.SongName "
                "FROM Singers WHERE "
                "STRUCT<FirstName STRING, LastName STRING>"
                "(FirstName, LastName) "
                "IN UNNEST(@song_info.ArtistNames)",
                params={"song_info": song_info},
                param_types={"song_info": song_info_type},
            )
    
        for row in results:
            print("SingerId: {} SongName: {}".format(*row))
    
    

### Ruby

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "Your Spanner instance ID"
    # database_id = "Your Spanner database ID"
    
    require "google/cloud/spanner"
    
    spanner = Google::Cloud::[Spanner](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-instance-v1/latest/Google-Cloud-Spanner.html).new project: project_id
    client  = spanner.[client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Project.html) instance_id, database_id
    
    name_type = client.fields FirstName: :STRING, LastName: :STRING
    
    song_info_struct = {
      SongName:    "Imagination",
      ArtistNames: [name_type.[struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Fields.html)(["Elena", "Campbell"]), name_type.[struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Fields.html)(["Hannah", "Harris"])]
    }
    
    client.execute(
      "SELECT SingerId, @song_info.SongName " \
      "FROM Singers WHERE STRUCT<FirstName STRING, LastName STRING>(FirstName, LastName) " \
      "IN UNNEST(@song_info.ArtistNames)",
      params: { song_info: song_info_struct }
    ).rows.[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-BatchWriteResults.html) do |row|
      puts row[:SingerId], row[:SongName]
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudspanner). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
