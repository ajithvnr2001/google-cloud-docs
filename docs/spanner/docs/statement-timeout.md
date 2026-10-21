---
url: https://docs.cloud.google.com/spanner/docs/statement-timeout/
title: Configure statement timeout \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:44.992643+00:00
---

# Configure statement timeout  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/statement-timeout/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Configure statement timeout Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set a timeout for a single statement execution using the Spanner client libraries. This can be used to override the default timeout configuration of the client library. The statement fails with a `DEADLINE_EXCEEDED` error if the statement cannot finish within the given timeout value.

**Note:** It is possible that the timeout occurs after the statement has finished executing on Spanner, but before the response reaches the client. In that case, it's possible that the statement was committed to Spanner successfully.

These samples show how to set a timeout for a single statement execution in the Cloud Spanner client library.

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/spanner"
    	"google.golang.org/grpc/codes"
    )
    
    func setStatementTimeout(w io.Writer, db string) error {
    	client, err := spanner.NewClient(context.Background(), db)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	_, err = client.ReadWriteTransaction(context.Background(),
    		func(ctx context.Context, txn *spanner.ReadWriteTransaction) error {
    			// Create a context with a 60-second timeout and apply this timeout to the insert statement.
    			ctxWithTimeout, cancel := context.WithTimeout(context.Background(), 60*time.Second)
    			defer cancel()
    			stmt := spanner.[Statement](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Statement){
    				SQL: `INSERT Singers (SingerId, FirstName, LastName)
    					VALUES (39, 'George', 'Washington')`,
    			}
    			rowCount, err := txn.Update(ctxWithTimeout, stmt)
    			// Get the error code from the error. This function returns codes.OK if err == nil.
    			code := spanner.[ErrCode](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_ErrCode)(err)
    			if code == codes.DeadlineExceeded {
    				fmt.Fprintf(w, "Insert statement timed out.\n")
    			} else if code == codes.OK {
    				fmt.Fprintf(w, "%d record(s) inserted.\n", rowCount)
    			} else {
    				fmt.Fprintf(w, "Insert statement failed with error %v\n", err)
    			}
    			return err
    		})
    	if err != nil {
    		return err
    	}
    	return nil
    }
    

### Java
    
    
    static void executeSqlWithTimeout() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project";
      String instanceId = "my-instance";
      String databaseId = "my-database";
    
      try (Spanner spanner =
          SpannerOptions.newBuilder().setProjectId(projectId).build().getService()) {
        DatabaseClient client =
            spanner.getDatabaseClient(DatabaseId.of(projectId, instanceId, databaseId));
        executeSqlWithTimeout(client);
      }
    }
    
    static void executeSqlWithTimeout(DatabaseClient client) {
      CallContextConfigurator configurator = new CallContextConfigurator() {
        public <ReqT, RespT> ApiCallContext configure(ApiCallContext context, ReqT request,
            MethodDescriptor<ReqT, RespT> method) {
          // DML uses the ExecuteSql RPC.
          if (method == SpannerGrpc.getExecuteSqlMethod()) {
            // NOTE: You can use a GrpcCallContext to set a custom timeout for a single RPC
            // invocation. This timeout can however ONLY BE SHORTER than the default timeout
            // for the RPC. If you set a timeout that is longer than the default timeout, then
            // the default timeout will be used.
            return GrpcCallContext.createDefault()
                .withCallOptions(CallOptions.DEFAULT.withDeadlineAfter(60L, TimeUnit.SECONDS));
          }
          // Return null to indicate that the default should be used for other methods.
          return null;
        }
      };
      // Create a context that uses the custom call configuration.
      Context context =
          Context.current().withValue(SpannerOptions.CALL_CONTEXT_CONFIGURATOR_KEY, configurator);
      // Run the transaction in the custom context.
      context.run(() ->
          client.readWriteTransaction().<long[]>run(transaction -> {
            String sql = "INSERT INTO Singers (SingerId, FirstName, LastName)\n"
                + "VALUES (20, 'George', 'Washington')";
            long rowCount = transaction.executeUpdate(Statement.of(sql));
            System.out.printf("%d record inserted.%n", rowCount);
            return null;
          })
      );
    }

### Node.js
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const projectId = 'my-project-id';
    // const instanceId = 'my-instance';
    // const databaseId = 'my-database';
    
    // Imports the Google Cloud client library
    const {Spanner} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    
    // Creates a client
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({
      projectId: projectId,
    });
    
    async function executeSqlWithTimeout() {
      // Gets a reference to a Cloud Spanner instance and database.
      const instance = spanner.instance(instanceId);
      const database = instance.database(databaseId);
    
      try {
        await database.[runTransactionAsync](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/database.html)(async tx => {
          // NOTE: You can use gaxOptions to set a custom timeout for a single RPC
          // invocation. This timeout can however ONLY BE SHORTER than the default timeout
          // for the RPC. If you set a timeout that is longer than the default timeout, then
          // the default timeout will be used.
          const query = {
            sql: "INSERT INTO Singers (SingerId, FirstName, LastName) VALUES (110, 'George', 'Washington')",
            gaxOptions: {
              timeout: 60000, // 60 seconds timeout
            },
          };
          const results = await tx.run(query);
          console.log(`${results[1].rowCountExact} record inserted.`);
          await tx.commit();
        });
      } catch (err) {
        console.error('ERROR:', err);
      } finally {
        await database.close();
      }
    }
    executeSqlWithTimeout();

### Python
    
    
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)
    
    def write(transaction):
        # Insert a record and configure the statement timeout to 60 seconds
        # This timeout can however ONLY BE SHORTER than the default timeout
        # for the RPC. If you set a timeout that is longer than the default timeout,
        # then the default timeout will be used.
        row_ct = transaction.execute_update(
            "INSERT INTO Singers (SingerId, FirstName, LastName) "
            " VALUES (110, 'George', 'Washington')",
            timeout=60,
        )
        print("{} record(s) inserted.".format(row_ct))
    
    database.run_in_transaction(write)
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
