---
url: https://docs.cloud.google.com/spanner/docs/samples/spanner-query-data-with-index/
title: Query data with index \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:21.822772+00:00
---

# Query data with index  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/samples/spanner-query-data-with-index/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Samples ](https://docs.cloud.google.com/spanner/docs/samples)



#  Query data with index Stay organized with collections  Save and categorize content based on your preferences. 

Query data by using an index.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Secondary indexes](https://docs.cloud.google.com/spanner/docs/secondary-indexes)



## Code sample

### C++

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    void QueryUsingIndex(google::cloud::spanner::Client client) {
      namespace spanner = ::google::cloud::spanner;
    
      spanner::SqlStatement select(
          "SELECT AlbumId, AlbumTitle, MarketingBudget"
          " FROM Albums@{FORCE_INDEX=AlbumsByAlbumTitle}"
          " WHERE AlbumTitle >= @start_title AND AlbumTitle < @end_title",
          {{"start_title", spanner::Value("Aardvark")},
           {"end_title", spanner::Value("Goo")}});
      using RowType =
          std::tuple<std::int64_t, std::string, std::optional<std::int64_t>>;
      auto rows = client.ExecuteQuery(std::move(select));
      for (auto& row : spanner::StreamOf<RowType>(rows)) {
        if (!row) throw std::move(row).status();
        std::cout << "AlbumId: " << std::get<0>(*row) << "\t";
        std::cout << "AlbumTitle: " << std::get<1>(*row) << "\t";
        auto marketing_budget = std::get<2>(*row);
        if (marketing_budget) {
          std::cout << "MarketingBudget: " << *marketing_budget << "\n";
        } else {
          std::cout << "MarketingBudget: NULL\n";
        }
      }
      std::cout << "Read completed for [spanner_query_data_with_index]\n";
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
    	"strconv"
    
    	"cloud.google.com/go/spanner"
    	"google.golang.org/api/iterator"
    )
    
    func queryUsingIndex(w io.Writer, db string) error {
    	ctx := context.Background()
    	client, err := spanner.NewClient(ctx, db)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	stmt := spanner.[Statement](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Statement){
    		SQL: `SELECT AlbumId, AlbumTitle, MarketingBudget
    			FROM Albums@{FORCE_INDEX=AlbumsByAlbumTitle}
    			WHERE AlbumTitle >= @start_title AND AlbumTitle < @end_title`,
    		Params: map[string]interface{}{
    			"start_title": "Aardvark",
    			"end_title":   "Goo",
    		},
    	}
    	iter := client.[Single](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Client_Single)().Query(ctx, stmt)
    	defer iter.Stop()
    	for {
    		row, err := iter.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return err
    		}
    		var albumID int64
    		var marketingBudget spanner.[NullInt64](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_NullInt64)
    		var albumTitle string
    		if err := row.[ColumnByName](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Row_ColumnByName)("AlbumId", &albumID); err != nil {
    			return err
    		}
    		if err := row.[ColumnByName](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Row_ColumnByName)("AlbumTitle", &albumTitle); err != nil {
    			return err
    		}
    		if err := row.[ColumnByName](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Row_ColumnByName)("MarketingBudget", &marketingBudget); err != nil {
    			return err
    		}
    		budget := "NULL"
    		if marketingBudget.Valid {
    			budget = strconv.FormatInt(marketingBudget.[Int64](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/spansql.html#cloud_google_com_go_spanner_spansql_Bool_Int64_Float64_Numeric_String_Bytes_Date_Timestamp_JSON_Proto_Enum_Tokenlist_UUID), 10)
    		}
    		fmt.Fprintf(w, "%d %s %s\n", albumID, albumTitle, budget)
    	}
    	return nil
    }
    

### Java

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static void queryUsingIndex(DatabaseClient dbClient) {
      Statement statement =
          Statement
              // We use FORCE_INDEX hint to specify which index to use. For more details see
              // https://cloud.google.com/spanner/docs/query-syntax#from-clause
              .newBuilder(
                  "SELECT AlbumId, AlbumTitle, MarketingBudget "
                      + "FROM Albums@{FORCE_INDEX=AlbumsByAlbumTitle} "
                      + "WHERE AlbumTitle >= @StartTitle AND AlbumTitle < @EndTitle")
              // We use @BoundParameters to help speed up frequently executed queries.
              //  For more details see https://cloud.google.com/spanner/docs/sql-best-practices
              .bind("StartTitle")
              .to("Aardvark")
              .bind("EndTitle")
              .to("Goo")
              .build();
      try (ResultSet resultSet = dbClient.singleUse().executeQuery(statement)) {
        while (resultSet.next()) {
          System.out.printf(
              "%d %s %s\n",
              resultSet.getLong("AlbumId"),
              resultSet.getString("AlbumTitle"),
              resultSet.isNull("MarketingBudget") ? "NULL" : resultSet.getLong("MarketingBudget"));
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
    // const startTitle = 'Ardvark';
    // const endTitle = 'Goo';
    
    // Imports the Google Cloud Spanner client library
    const {Spanner} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    
    // Instantiates a client
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({
      projectId: projectId,
    });
    
    async function queryDataWithIndex() {
      // Gets a reference to a Cloud Spanner instance and database
      const instance = spanner.instance(instanceId);
      const database = instance.database(databaseId);
    
      const query = {
        sql: `SELECT AlbumId, AlbumTitle, MarketingBudget
                    FROM Albums@{FORCE_INDEX=AlbumsByAlbumTitle}
                    WHERE AlbumTitle >= @startTitle AND AlbumTitle <= @endTitle`,
        params: {
          startTitle: startTitle,
          endTitle: endTitle,
        },
      };
    
      // Queries rows from the Albums table
      try {
        const [rows] = await database.run(query);
    
        rows.forEach(row => {
          const json = row.toJSON();
          const marketingBudget = json.MarketingBudget
            ? json.MarketingBudget
            : null; // This value is nullable
          console.log(
            `AlbumId: ${json.AlbumId}, AlbumTitle: ${json.AlbumTitle}, MarketingBudget: ${marketingBudget}`
          );
        });
      } catch (err) {
        console.error('Failed to query data with index:', err.message || err);
      } finally {
        // Close the database when finished.
        await database.close();
      }
    }
    queryDataWithIndex();

### PHP

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Spanner\SpannerClient;
    
    /**
     * Queries sample data from the database using SQL and an index.
     *
     * The index must exist before running this sample. You can add the index
     * by running the `add_index` sample or by running this DDL statement against
     * your database:
     *
     *     CREATE INDEX AlbumsByAlbumTitle ON Albums(AlbumTitle)
     *
     * Example:
     * ```
     * query_data_with_index($instanceId, $databaseId);
     * ```
     *
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     * @param string $startTitle The start of the title index.
     * @param string $endTitle   The end of the title index.
     */
    function query_data_with_index(
        string $instanceId,
        string $databaseId,
        string $startTitle = 'Aardvark',
        string $endTitle = 'Goo'
    ): void {
        $spanner = new SpannerClient();
        $instance = $spanner->instance($instanceId);
        $database = $instance->database($databaseId);
    
        $parameters = [
            'startTitle' => $startTitle,
            'endTitle' => $endTitle
        ];
    
        $results = $database->execute(
            'SELECT AlbumId, AlbumTitle, MarketingBudget ' .
            'FROM Albums@{FORCE_INDEX=AlbumsByAlbumTitle} ' .
            'WHERE AlbumTitle >= @startTitle AND AlbumTitle < @endTitle',
            ['parameters' => $parameters]
        );
    
        foreach ($results as $row) {
            printf('AlbumId: %s, AlbumTitle: %s, MarketingBudget: %d' . PHP_EOL,
                $row['AlbumId'], $row['AlbumTitle'], $row['MarketingBudget']);
        }
    }

### Python

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def query_data_with_index(
        instance_id, database_id, start_title="Aardvark", end_title="Goo"
    ):
        """Queries sample data from the database using SQL and an index.
    
        The index must exist before running this sample. You can add the index
        by running the `add_index` sample or by running this DDL statement against
        your database:
    
            CREATE INDEX AlbumsByAlbumTitle ON Albums(AlbumTitle)
    
        This sample also uses the `MarketingBudget` column. You can add the column
        by running the `add_column` sample or by running this DDL statement against
        your database:
    
            ALTER TABLE Albums ADD COLUMN MarketingBudget INT64
    
        """
        spanner_client = spanner.Client()
        instance = spanner_client.instance(instance_id)
        database = instance.database(database_id)
    
        params = {"start_title": start_title, "end_title": end_title}
        param_types = {
            "start_title": spanner.param_types.STRING,
            "end_title": spanner.param_types.STRING,
        }
    
        with database.snapshot() as snapshot:
            results = snapshot.execute_sql(
                "SELECT AlbumId, AlbumTitle, MarketingBudget "
                "FROM Albums@{FORCE_INDEX=AlbumsByAlbumTitle} "
                "WHERE AlbumTitle >= @start_title AND AlbumTitle < @end_title",
                params=params,
                param_types=param_types,
            )
    
            for row in results:
                print("AlbumId: {}, AlbumTitle: {}, MarketingBudget: {}".format(*row))
    
    

### Ruby

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "Your Spanner instance ID"
    # database_id = "Your Spanner database ID"
    # start_title = "An album title to start with such as 'Ardvark'"
    # end_title   = "An album title to end with such as 'Goo'"
    
    require "google/cloud/spanner"
    
    spanner = Google::Cloud::[Spanner](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-instance-v1/latest/Google-Cloud-Spanner.html).new project: project_id
    client  = spanner.[client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Project.html) instance_id, database_id
    
    sql_query = "SELECT AlbumId, AlbumTitle, MarketingBudget
                 FROM Albums@{FORCE_INDEX=AlbumsByAlbumTitle}
                 WHERE AlbumTitle >= @start_title AND AlbumTitle < @end_title"
    
    params      = { start_title: start_title, end_title: end_title }
    param_types = { start_title: :STRING,     end_title: :STRING }
    
    client.execute(sql_query, params: params, types: param_types).rows.[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-BatchWriteResults.html) do |row|
      puts "#{row[:AlbumId]} #{row[:AlbumTitle]} #{row[:MarketingBudget]}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudspanner). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
