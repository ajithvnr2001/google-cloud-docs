---
url: https://docs.cloud.google.com/spanner/docs/samples/spanner-query-with-parameter/
title: Query data with parameter \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:21.514518+00:00
---

# Query data with parameter  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/samples/spanner-query-with-parameter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Samples ](https://docs.cloud.google.com/spanner/docs/samples)



#  Query data with parameter Stay organized with collections  Save and categorize content based on your preferences. 

Query data by using a parameter.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Getting started with Spanner and PGAdapter](https://docs.cloud.google.com/spanner/docs/getting-started/pgadapter)
  * [Getting started with Spanner in ADO.NET](https://docs.cloud.google.com/spanner/docs/getting-started/ado_net)
  * [Getting started with Spanner in C#](https://docs.cloud.google.com/spanner/docs/getting-started/csharp)
  * [Getting started with Spanner in C++](https://docs.cloud.google.com/spanner/docs/getting-started/cpp)
  * [Getting started with Spanner in Go](https://docs.cloud.google.com/spanner/docs/getting-started/go)
  * [Getting started with Spanner in Go database/sql](https://docs.cloud.google.com/spanner/docs/getting-started/database_sql)
  * [Getting started with Spanner in Java](https://docs.cloud.google.com/spanner/docs/getting-started/java)
  * [Getting started with Spanner in JDBC](https://docs.cloud.google.com/spanner/docs/getting-started/jdbc)
  * [Getting started with Spanner in Node.js](https://docs.cloud.google.com/spanner/docs/getting-started/nodejs)
  * [Getting started with Spanner in PHP](https://docs.cloud.google.com/spanner/docs/getting-started/php)
  * [Getting started with Spanner in Python](https://docs.cloud.google.com/spanner/docs/getting-started/python)
  * [Getting started with Spanner in Ruby](https://docs.cloud.google.com/spanner/docs/getting-started/ruby)



## Code sample

### C++

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    void QueryWithParameter(google::cloud::spanner::Client client) {
      namespace spanner = ::google::cloud::spanner;
    
      spanner::SqlStatement select(
          "SELECT SingerId, FirstName, LastName FROM Singers"
          " WHERE LastName = @last_name",
          {{"last_name", spanner::Value("Garcia")}});
      using RowType = std::tuple<std::int64_t, std::string, std::string>;
      auto rows = client.ExecuteQuery(std::move(select));
      for (auto& row : spanner::StreamOf<RowType>(rows)) {
        if (!row) throw std::move(row).status();
        std::cout << "SingerId: " << std::get<0>(*row) << "\t";
        std::cout << "FirstName: " << std::get<1>(*row) << "\t";
        std::cout << "LastName: " << std::get<2>(*row) << "\n";
      }
    
      std::cout << "Query completed for [spanner_query_with_parameter]\n";
    }

### C#

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Spanner.Data](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.html);
    using System.Collections.Generic;
    using System.Threading.Tasks;
    
    public class QueryWithParameterAsyncSample
    {
        public class Singer
        {
            public int SingerId { get; set; }
            public string FirstName { get; set; }
            public string LastName { get; set; }
        }
    
        public async Task<List<Singer>> QueryWithParameterAsync(string projectId, string instanceId, string databaseId)
        {
            string connectionString = $"Data Source=projects/{projectId}/instances/{instanceId}/databases/{databaseId}";
    
            using var connection = new [SpannerConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html)(connectionString);
            using var cmd = connection.[CreateSelectCommand](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_CreateSelectCommand_System_String_Google_Cloud_Spanner_Data_SpannerParameterCollection_)(
                $"SELECT SingerId, FirstName, LastName FROM Singers WHERE LastName = @lastName",
                new [SpannerParameterCollection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerParameterCollection.html) { { "lastName", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[String](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_String), "Garcia" } });
    
            var singers = new List<Singer>();
            using var reader = await cmd.[ExecuteReaderAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerCommand.html#Google_Cloud_Spanner_Data_SpannerCommand_ExecuteReaderAsync)();
            while (await reader.[ReadAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDataReader.html#Google_Cloud_Spanner_Data_SpannerDataReader_ReadAsync_System_Threading_CancellationToken_)())
            {
                singers.Add(new Singer
                {
                    SingerId = reader.GetFieldValue<int>("SingerId"),
                    FirstName = reader.GetFieldValue<string>("FirstName"),
                    LastName = reader.GetFieldValue<string>("LastName")
                });
            }
            return singers;
        }
    }

### Go

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"database/sql"
    	"fmt"
    	"io"
    
    	_ "github.com/googleapis/go-sql-spanner"
    )
    
    func QueryDataWithParameter(ctx context.Context, w io.Writer, databaseName string) error {
    	db, err := sql.Open("spanner", databaseName)
    	if err != nil {
    		return err
    	}
    	defer db.Close()
    
    	rows, err := db.QueryContext(ctx,
    		`SELECT SingerId, FirstName, LastName
    		FROM Singers
    		WHERE LastName = ?`, "Garcia")
    	defer rows.Close()
    	if err != nil {
    		return err
    	}
    	for rows.Next() {
    		var singerId int64
    		var firstName, lastName string
    		err = rows.Scan(&singerId, &firstName, &lastName)
    		if err != nil {
    			return err
    		}
    		fmt.Fprintf(w, "%v %v %v\n", singerId, firstName, lastName)
    	}
    	if rows.Err() != nil {
    		return rows.Err()
    	}
    	return rows.Close()
    }
    

### Java

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import java.sql.Connection;
    import java.sql.DriverManager;
    import java.sql.PreparedStatement;
    import java.sql.ResultSet;
    import java.sql.SQLException;
    
    class QueryDataWithParameter {
      static void queryDataWithParameter(String host, int port, String database) throws SQLException {
        String connectionUrl = String.format("jdbc:postgresql://%s:%d/%s", host, port, database);
        try (Connection connection = DriverManager.getConnection(connectionUrl)) {
          try (PreparedStatement statement =
              connection.prepareStatement(
                  "SELECT singer_id, first_name, last_name "
                      + "FROM singers "
                      + "WHERE last_name = ?")) {
            statement.setString(1, "Garcia");
            try (ResultSet resultSet = statement.executeQuery()) {
              while (resultSet.next()) {
                System.out.printf(
                    "%d %s %s\n",
                    resultSet.getLong("singer_id"),
                    resultSet.getString("first_name"),
                    resultSet.getString("last_name"));
              }
            }
          }
        }
      }
    }
    

### Node.js

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const {Spanner} = require('@google-cloud/spanner');
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const projectId = 'my-project-id';
    // const instanceId = 'my-instance';
    // const databaseId = 'my-database';
    
    // Creates a client
    const spanner = new Spanner({
      projectId: projectId,
    });
    
    // Gets a reference to a Cloud Spanner instance and database
    const instance = spanner.instance(instanceId);
    const database = instance.database(databaseId);
    
    const query = {
      sql: `SELECT SingerId, FirstName, LastName
            FROM Singers WHERE LastName = @lastName`,
      params: {
        lastName: 'Garcia',
      },
    };
    
    // Queries rows from the Albums table
    try {
      const [rows] = await database.run(query);
    
      rows.forEach(row => {
        const json = row.toJSON();
        console.log(
          `SingerId: ${json.SingerId}, FirstName: ${json.FirstName}, LastName: ${json.LastName}`
        );
      });
    } catch (err) {
      console.error('ERROR:', err);
    } finally {
      // Close the database when finished.
      await database.close();
    }

### Node.js

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import { Client } from 'pg';
    
    async function queryWithParameter(host: string, port: number, database: string): Promise<void> {
      // Connect to Spanner through PGAdapter.
      const connection = new Client({
        host: host,
        port: port,
        database: database,
      });
      await connection.connect();
    
      const result = await connection.query(
          "SELECT singer_id, first_name, last_name " +
          "FROM singers " +
          "WHERE last_name = $1", ["Garcia"]);
      for (const row of result.rows) {
        console.log(`${row["singer_id"]} ${row["first_name"]} ${row["last_name"]}`);
      }
    
      // Close the connection.
      await connection.end();
    }

### PHP

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    function query_data_with_parameter(string $host, string $port, string $database): void
    {
        $dsn = sprintf("pgsql:host=%s;port=%s;dbname=%s", $host, $port, $database);
        $connection = new PDO($dsn);
    
        $statement = $connection->prepare("SELECT singer_id, first_name, last_name "
                            ."FROM singers "
                            ."WHERE last_name = ?"
        );
        $statement->execute(["Garcia"]);
        $rows = $statement->fetchAll();
        foreach ($rows as $singer)
        {
            printf("%s\t%s\t%s\n", $singer["singer_id"], $singer["first_name"], $singer["last_name"]);
        }
    
        $rows = null;
        $statement = null;
        $connection = null;
    }

### Python

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import string
    import psycopg
    
    
    def query_data_with_parameter(host: string, port: int, database: string):
        with psycopg.connect("host={host} port={port} dbname={database} "
                             "sslmode=disable".format(host=host,
                                                      port=port,
                                                      database=database)) as conn:
            conn.autocommit = True
            with conn.cursor() as cur:
                cur.execute("SELECT singer_id, first_name, last_name "
                            "FROM singers "
                            "WHERE last_name = %s", ("Garcia",))
                for singer in cur:
                    print(singer)

### Ruby

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "Your Spanner instance ID"
    # database_id = "Your Spanner database ID"
    
    require "google/cloud/spanner"
    
    spanner = Google::Cloud::[Spanner](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-instance-v1/latest/Google-Cloud-Spanner.html).new project: project_id
    client  = spanner.[client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Project.html) instance_id, database_id
    
    sql_query = "SELECT SingerId, FirstName, LastName
                 FROM Singers
                 WHERE LastName = @lastName"
    
    params      = { lastName: "Garcia" }
    param_types = { lastName: :STRING }
    
    client.execute(sql_query, params: params, types: param_types).rows.[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-BatchWriteResults.html) do |row|
      puts "#{row[:SingerId]} #{row[:FirstName]} #{row[:LastName]}"
    end

### Rust
    
    
    use google_cloud_spanner::client::DatabaseClient;
    use google_cloud_spanner::statement::Statement;
    
    pub async fn sample(client: &DatabaseClient) -> anyhow::Result<()> {
        let statement = Statement::builder(
            "SELECT SingerId, FirstName, LastName \
             FROM Singers \
             WHERE LastName = @lastName",
        )
        .add_param("lastName", "Garcia")
        .build();
    
        let transaction = client.single_use().build();
        let mut result_set = transaction.execute_query(statement).await?;
    
        while let Some(row) = result_set.next().await.transpose()? {
            let singer_id: i64 = row.get("SingerId")?;
            let first_name: String = row.get("FirstName")?;
            let last_name: String = row.get("LastName")?;
            println!("{singer_id} {first_name} {last_name}");
        }
        Ok(())
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudspanner). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
