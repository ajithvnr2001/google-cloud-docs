---
url: https://docs.cloud.google.com/spanner/docs/samples/spanner-query-graph-data-with-parameter/
title: Query data in a graph with a parameter \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:26.452014+00:00
---

# Query data in a graph with a parameter  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/samples/spanner-query-graph-data-with-parameter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Samples ](https://docs.cloud.google.com/spanner/docs/samples)



#  Query data in a graph with a parameter Stay organized with collections  Save and categorize content based on your preferences. 

Query data in a Spanner Graph using a parameter.

## Code sample

### C++

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    void QueryDataWithParameter(google::cloud::spanner::Client client) {
      namespace spanner = ::google::cloud::spanner;
    
      spanner::SqlStatement select(R"""(
          Graph FinGraph
          MATCH (a:Person)-[o:Owns]->()-[t:Transfers]->()<-[p:Owns]-(b:Person)
          WHERE t.amount >= @min
          RETURN a.name AS sender,
                 b.name AS receiver,
                 t.amount,
                 t.create_time AS transfer_at)""",
                                   {{"min", spanner::Value(500)}});
      using RowType =
          std::tuple<std::string, std::string, double, spanner::Timestamp>;
      auto rows = client.ExecuteQuery(std::move(select));
      for (auto& row : spanner::StreamOf<RowType>(rows)) {
        if (!row) throw std::move(row).status();
        std::cout << "sender: " << std::get<0>(*row) << "\t";
        std::cout << "receiver: " << std::get<1>(*row) << "\t";
        std::cout << "amount: " << std::get<2>(*row) << "\t";
        std::cout << "transfer_at: " << std::get<3>(*row) << "\n";
      }
    
      std::cout
          << "Query completed for [spanner_query_graph_data_with_parameter]\n";
    }

### Go

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/spanner"
    	"google.golang.org/api/iterator"
    )
    
    func queryGraphDataWithParameter(w io.Writer, db string) error {
    	ctx := context.Background()
    	client, err := spanner.NewClient(ctx, db)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	// Execute a Spanner query statement comprising a graph query. Graph queries
    	// are characterized by 'MATCH' statements describing node and edge
    	// patterns.
    	//
    	// This statement finds entities ('Account's) owned by all 'Person's 'b' to
    	// which transfers greater than a specified 'min' have been made by entities
    	// ('Account's) owned by any 'Person' 'a' in the graph called 'FinGraph'.
    	// It then returns the names of all such 'Person's 'a' and 'b', and the
    	// amount and time of the transfer.
    	// The parameter 'min' is distinguished by a leading '@', and the value
    	// of the parameter is specified using a map.
    	stmt := spanner.[Statement](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Statement){
    		SQL: `Graph FinGraph 
    			  MATCH (a:Person)-[o:Owns]->()-[t:Transfers]->()<-[p:Owns]-(b:Person)
    			  WHERE t.amount >= @min
    			  RETURN a.name AS sender, b.name AS receiver, t.amount, t.create_time AS transfer_at`,
    		Params: map[string]interface{}{
    			"min": 500,
    		},
    	}
    	iter := client.[Single](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Client_Single)().Query(ctx, stmt)
    	defer iter.Stop()
    
    	// The results are returned in tabular form. Iterate over the
    	// result rows and print them.
    	for {
    		row, err := iter.Next()
    		if err == iterator.Done {
    			return nil
    		}
    		if err != nil {
    			return err
    		}
    		var sender, receiver string
    		var amount float64
    		var transfer_at time.Time
    		if err := row.[Columns](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Row_Columns)(&sender, &receiver, &amount, &transfer_at); err != nil {
    			return err
    		}
    		fmt.Fprintf(w, "%s %s %f %s\n", sender, receiver, amount, transfer_at.Format(time.RFC3339))
    	}
    }
    

### Java

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static void queryWithParameter(DatabaseClient dbClient) {
      Statement statement =
          Statement.newBuilder(
                  "Graph FinGraph MATCH"
                      + " (a:Person)-[o:Owns]->()-[t:Transfers]->()<-[p:Owns]-(b:Person) WHERE"
                      + " t.amount >= @min RETURN a.name AS sender, b.name AS receiver, t.amount,"
                      + " t.create_time AS transfer_at")
              .bind("min")
              .to(500)
              .build();
      try (ResultSet resultSet = dbClient.singleUse().executeQuery(statement)) {
        while (resultSet.next()) {
          System.out.printf(
              "%s %s %f %s\n",
              resultSet.getString("sender"),
              resultSet.getString("receiver"),
              resultSet.getDouble("amount"),
              resultSet.getTimestamp("transfer_at"));
        }
      }
    }
    

### Python

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def query_data_with_parameter(instance_id, database_id):
        """Queries sample data from the database using SQL with a parameter."""
    
        spanner_client = spanner.Client()
        instance = spanner_client.instance(instance_id)
        database = instance.database(database_id)
    
        with database.snapshot() as snapshot:
            results = snapshot.execute_sql(
                """Graph FinGraph
                MATCH (a:Person)-[o:Owns]->()-[t:Transfers]->()<-[p:Owns]-(b:Person)
                WHERE t.amount >= @min
                RETURN a.name AS sender, b.name AS receiver, t.amount, t.create_time AS transfer_at""",
                params={"min": 500},
                param_types={"min": spanner.param_types.INT64},
            )
    
            for row in results:
                print("sender: {}, receiver: {}, amount: {}, transfer_at: {}".format(*row))
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudspanner). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
