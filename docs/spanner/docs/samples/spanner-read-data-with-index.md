---
url: https://docs.cloud.google.com/spanner/docs/samples/spanner-read-data-with-index/
title: Read data with index \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:44.791872+00:00
---

# Read data with index  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/samples/spanner-read-data-with-index/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Samples ](https://docs.cloud.google.com/spanner/docs/samples)



#  Read data with index Stay organized with collections  Save and categorize content based on your preferences. 

Read data by using an index.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Getting started with Spanner in C++](https://docs.cloud.google.com/spanner/docs/getting-started/cpp)
  * [Getting started with Spanner in Go](https://docs.cloud.google.com/spanner/docs/getting-started/go)
  * [Getting started with Spanner in Java](https://docs.cloud.google.com/spanner/docs/getting-started/java)
  * [Getting started with Spanner in Node.js](https://docs.cloud.google.com/spanner/docs/getting-started/nodejs)
  * [Getting started with Spanner in PHP](https://docs.cloud.google.com/spanner/docs/getting-started/php)
  * [Getting started with Spanner in Python](https://docs.cloud.google.com/spanner/docs/getting-started/python)
  * [Getting started with Spanner in Ruby](https://docs.cloud.google.com/spanner/docs/getting-started/ruby)
  * [Reads outside of transactions](https://docs.cloud.google.com/spanner/docs/reads)
  * [Secondary indexes](https://docs.cloud.google.com/spanner/docs/secondary-indexes)



## Code sample

### C++

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    void ReadDataWithIndex(google::cloud::spanner::Client client) {
      namespace spanner = ::google::cloud::spanner;
    
      auto rows =
          client.Read("Albums", google::cloud::spanner::KeySet::All(),
                      {"AlbumId", "AlbumTitle"},
                      google::cloud::Options{}.set<spanner::ReadIndexNameOption>(
                          "AlbumsByAlbumTitle"));
      using RowType = std::tuple<std::int64_t, std::string>;
      for (auto& row : spanner::StreamOf<RowType>(rows)) {
        if (!row) throw std::move(row).status();
        std::cout << "AlbumId: " << std::get<0>(*row) << "\t";
        std::cout << "AlbumTitle: " << std::get<1>(*row) << "\n";
      }
      std::cout << "Read completed for [spanner_read_data_with_index]\n";
    }

### C#

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Spanner.Data](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.html);
    using System.Collections.Generic;
    using System.Threading.Tasks;
    
    public class QueryDataWithIndexAsyncSample
    {
        public class Album
        {
            public int AlbumId { get; set; }
            public string AlbumTitle { get; set; }
            public long MarketingBudget { get; set; }
        }
    
        public async Task<List<Album>> QueryDataWithIndexAsync(string projectId, string instanceId, string databaseId,
            string startTitle, string endTitle)
        {
            string connectionString = $"Data Source=projects/{projectId}/instances/{instanceId}/databases/{databaseId}";
            using var connection = new [SpannerConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html)(connectionString);
            using var cmd = connection.[CreateSelectCommand](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_CreateSelectCommand_System_String_Google_Cloud_Spanner_Data_SpannerParameterCollection_)(
                "SELECT AlbumId, AlbumTitle, MarketingBudget FROM Albums@ "
                + "{FORCE_INDEX=AlbumsByAlbumTitle} "
                + $"WHERE AlbumTitle >= @startTitle "
                + $"AND AlbumTitle < @endTitle",
                new [SpannerParameterCollection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerParameterCollection.html)
                {
                    { "startTitle", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[String](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_String), startTitle },
                    { "endTitle", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[String](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_String), endTitle }
                });
    
            var albums = new List<Album>();
            using var reader = await cmd.[ExecuteReaderAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerCommand.html#Google_Cloud_Spanner_Data_SpannerCommand_ExecuteReaderAsync)();
            while (await reader.[ReadAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDataReader.html#Google_Cloud_Spanner_Data_SpannerDataReader_ReadAsync_System_Threading_CancellationToken_)())
            {
                albums.Add(new Album
                {
                    AlbumId = reader.GetFieldValue<int>("AlbumId"),
                    AlbumTitle = reader.GetFieldValue<string>("AlbumTitle"),
                    MarketingBudget = reader.[IsDBNull](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDataReader.html#Google_Cloud_Spanner_Data_SpannerDataReader_IsDBNull_System_Int32_)(reader.[GetOrdinal](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDataReader.html#Google_Cloud_Spanner_Data_SpannerDataReader_GetOrdinal_System_String_)("MarketingBudget")) ? 0 : reader.GetFieldValue<long>("MarketingBudget")
                });
            }
            return albums;
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
    
    func readUsingIndex(w io.Writer, db string) error {
    	ctx := context.Background()
    	client, err := spanner.NewClient(ctx, db)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	iter := client.[Single](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Client_Single)().ReadUsingIndex(ctx, "Albums", "AlbumsByAlbumTitle", spanner.[AllKeys](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_KeySet_AllKeys)(),
    		[]string{"AlbumId", "AlbumTitle"})
    	defer iter.Stop()
    	for {
    		row, err := iter.Next()
    		if err == iterator.Done {
    			return nil
    		}
    		if err != nil {
    			return err
    		}
    		var albumID int64
    		var albumTitle string
    		if err := row.[Columns](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Row_Columns)(&albumID, &albumTitle); err != nil {
    			return err
    		}
    		fmt.Fprintf(w, "%d %s\n", albumID, albumTitle)
    	}
    }
    

### Java

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static void readUsingIndex(DatabaseClient dbClient) {
      try (ResultSet resultSet =
          dbClient
              .singleUse()
              .readUsingIndex(
                  "Albums",
                  "AlbumsByAlbumTitle",
                  KeySet.all(),
                  Arrays.asList("AlbumId", "AlbumTitle"))) {
        while (resultSet.next()) {
          System.out.printf("%d %s\n", resultSet.getLong(0), resultSet.getString(1));
        }
      }
    }

### Node.js

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const instanceId = 'my-instance';
    // const databaseId = 'my-database';
    // const projectId = 'my-project-id';
    
    // Imports the Google Cloud Spanner client library
    const {Spanner} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    
    // Instantiates a client
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({
      projectId: projectId,
    });
    
    async function readDataWithIndex() {
      // Gets a reference to a Cloud Spanner instance and database
      const instance = spanner.instance(instanceId);
      const database = instance.database(databaseId);
    
      const albumsTable = database.table('Albums');
    
      const query = {
        columns: ['AlbumId', 'AlbumTitle'],
        keySet: {
          all: true,
        },
        index: 'AlbumsByAlbumTitle',
      };
    
      // Reads the Albums table using an index
      try {
        const [rows] = await albumsTable.read(query);
    
        rows.forEach(row => {
          const json = row.toJSON();
          console.log(`AlbumId: ${json.AlbumId}, AlbumTitle: ${json.AlbumTitle}`);
        });
      } catch (err) {
        console.error('ERROR:', err);
      } finally {
        // Close the database when finished.
        await database.close();
      }
    }
    readDataWithIndex();

### PHP

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Spanner\SpannerClient;
    
    /**
     * Reads sample data from the database using an index.
     *
     * The index must exist before running this sample. You can add the index
     * by running the `add_index` sample or by running this DDL statement against
     * your database:
     *
     *     CREATE INDEX AlbumsByAlbumTitle ON Albums(AlbumTitle)
     *
     * Example:
     * ```
     * read_data_with_index($instanceId, $databaseId);
     * ```
     *
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     */
    function read_data_with_index(string $instanceId, string $databaseId): void
    {
        $spanner = new SpannerClient();
        $instance = $spanner->instance($instanceId);
        $database = $instance->database($databaseId);
    
        $keySet = $spanner->keySet(['all' => true]);
        $results = $database->read(
            'Albums',
            $keySet,
            ['AlbumId', 'AlbumTitle'],
            ['index' => 'AlbumsByAlbumTitle']
        );
    
        foreach ($results->rows() as $row) {
            printf('AlbumId: %s, AlbumTitle: %s' . PHP_EOL,
                $row['AlbumId'], $row['AlbumTitle']);
        }
    }

### Python

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def read_data_with_index(instance_id, database_id):
        """Reads sample data from the database using an index.
    
        The index must exist before running this sample. You can add the index
        by running the `add_index` sample or by running this DDL statement against
        your database:
    
            CREATE INDEX AlbumsByAlbumTitle ON Albums(AlbumTitle)
    
        """
        spanner_client = spanner.Client()
        instance = spanner_client.instance(instance_id)
        database = instance.database(database_id)
    
        with database.snapshot() as snapshot:
            keyset = spanner.KeySet(all_=True)
            results = snapshot.read(
                table="Albums",
                columns=("AlbumId", "AlbumTitle"),
                keyset=keyset,
                index="AlbumsByAlbumTitle",
            )
    
            for row in results:
                print("AlbumId: {}, AlbumTitle: {}".format(*row))
    
    

### Ruby

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "Your Spanner instance ID"
    # database_id = "Your Spanner database ID"
    
    require "google/cloud/spanner"
    
    spanner = Google::Cloud::[Spanner](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-instance-v1/latest/Google-Cloud-Spanner.html).new project: project_id
    client  = spanner.[client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Project.html) instance_id, database_id
    
    result = client.read "Albums", [:AlbumId, :AlbumTitle],
                         index: "AlbumsByAlbumTitle"
    
    result.rows.[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-BatchWriteResults.html) do |row|
      puts "#{row[:AlbumId]} #{row[:AlbumTitle]}"
    end

### Rust
    
    
    use google_cloud_spanner::client::DatabaseClient;
    use google_cloud_spanner::key::KeySet;
    use google_cloud_spanner::read::ReadRequest;
    
    pub async fn sample(client: &DatabaseClient) -> anyhow::Result<()> {
        let read_request = ReadRequest::builder("Albums", ["AlbumId", "AlbumTitle"])
            .with_index("AlbumsByAlbumTitle", KeySet::all())
            .build();
    
        let transaction = client.single_use().build();
        let mut result_set = transaction.execute_read(read_request).await?;
    
        while let Some(row) = result_set.next().await.transpose()? {
            let album_id: i64 = row.get(0)?;
            let album_title: String = row.get(1)?;
            println!("{album_id} {album_title}");
        }
    
        Ok(())
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudspanner). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
