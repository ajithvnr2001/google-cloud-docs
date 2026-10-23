---
url: https://docs.cloud.google.com/spanner/docs/samples/spanner-functions-quickstart/
title: Functions \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:09:46.541986+00:00
---

# Functions  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/samples/spanner-functions-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Samples ](https://docs.cloud.google.com/spanner/docs/samples)



#  Functions Stay organized with collections  Save and categorize content based on your preferences. 

Connect by using functions.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a Cloud Run function that returns Spanner results](https://docs.cloud.google.com/run/docs/tutorials/function-sends-query-to-spanner-database)
  * [Using Spanner with Cloud Run functions (1st gen)](https://docs.cloud.google.com/functions/1stgendocs/tutorials/use-cloud-spanner-1st-gen)



## Code sample

### Go

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Package spanner contains an example of using Spanner from a Cloud Function.
    package spanner
    
    import (
    	"context"
    	"fmt"
    	"log"
    	"net/http"
    	"sync"
    
    	"cloud.google.com/go/spanner"
    	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
    	"google.golang.org/api/iterator"
    )
    
    // client is a global Spanner client, to avoid initializing a new client for
    // every request.
    var client *spanner.Client
    var clientOnce sync.Once
    
    // db is the name of the database to query.
    var db = "projects/my-project/instances/my-instance/databases/example-db"
    
    func init() {
    	functions.HTTP("HelloSpanner", HelloSpanner)
    }
    
    // HelloSpanner is an example of querying Spanner from a Cloud Function.
    func HelloSpanner(w http.ResponseWriter, r *http.Request) {
    	clientOnce.Do(func() {
    		// Declare a separate err variable to avoid shadowing client.
    		var err error
    		client, err = spanner.NewClient(context.Background(), db)
    		if err != nil {
    			http.Error(w, "Error initializing database", http.StatusInternalServerError)
    			log.Printf("spanner.NewClient: %v", err)
    			return
    		}
    	})
    
    	fmt.Fprintln(w, "Albums:")
    	stmt := spanner.[Statement](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Statement){SQL: `SELECT SingerId, AlbumId, AlbumTitle FROM Albums`}
    	iter := client.[Single](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Client_Single)().Query(r.Context(), stmt)
    	defer iter.Stop()
    	for {
    		row, err := iter.Next()
    		if err == iterator.Done {
    			return
    		}
    		if err != nil {
    			http.Error(w, "Error querying database", http.StatusInternalServerError)
    			log.Printf("iter.Next: %v", err)
    			return
    		}
    		var singerID, albumID int64
    		var albumTitle string
    		if err := row.[Columns](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Row_Columns)(&singerID, &albumID, &albumTitle); err != nil {
    			http.Error(w, "Error parsing database response", http.StatusInternalServerError)
    			log.Printf("row.Columns: %v", err)
    			return
    		}
    		fmt.Fprintf(w, "%d %d %s\n", singerID, albumID, albumTitle)
    	}
    }
    

### Java

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.client.http.[HttpStatusCodes](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpStatusCodes.html);
    import com.google.cloud.functions.HttpFunction;
    import com.google.cloud.functions.[HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest.html);
    import com.google.cloud.functions.[HttpResponse](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpResponse.html);
    import com.google.cloud.spanner.[DatabaseClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseClient.html);
    import com.google.cloud.spanner.[DatabaseId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseId.html);
    import com.google.cloud.spanner.[LazySpannerInitializer](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.LazySpannerInitializer.html);
    import com.google.cloud.spanner.[ResultSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.ResultSet.html);
    import com.google.cloud.spanner.[SpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerException.html);
    import com.google.cloud.spanner.[SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html);
    import com.google.cloud.spanner.[Statement](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Statement.html);
    import com.google.common.annotations.VisibleForTesting;
    import com.google.common.base.MoreObjects;
    import java.io.PrintWriter;
    import java.util.logging.Level;
    import java.util.logging.Logger;
    
    // HelloSpanner is an example of querying Spanner from a Cloud Function.
    public class HelloSpanner implements HttpFunction {
      private static final Logger logger = Logger.getLogger(HelloSpanner.class.getName());
    
      // TODO<developer>: Set these environment variables.
      private static final String SPANNER_INSTANCE_ID =
          MoreObjects.firstNonNull(System.getenv("SPANNER_INSTANCE"), "my-instance");
      private static final String SPANNER_DATABASE_ID =
          MoreObjects.firstNonNull(System.getenv("SPANNER_DATABASE"), "example-db");
    
      private static final [DatabaseId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseId.html) databaseId =
          [DatabaseId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseId.html).of(
              [SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html).[getDefaultProjectId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.connection.ConnectionOptions.html#com_google_cloud_spanner_connection_ConnectionOptions_getDefaultProjectId_com_google_auth_Credentials_)(),
              SPANNER_INSTANCE_ID,
              SPANNER_DATABASE_ID);
    
      // The LazySpannerInitializer instance is shared across all instances of the HelloSpanner class.
      // It will create a Spanner instance the first time one is requested, and continue to return that
      // instance for all subsequent requests.
      private static final [LazySpannerInitializer](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.LazySpannerInitializer.html) SPANNER_INITIALIZER = new [LazySpannerInitializer](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.LazySpannerInitializer.html)();
    
      @VisibleForTesting
      [DatabaseClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseClient.html) getClient() throws Throwable {
        return SPANNER_INITIALIZER.get().getDatabaseClient(databaseId);
      }
    
      @Override
      public void service([HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest.html) request, [HttpResponse](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpResponse.html) response) throws Exception {
        var writer = new PrintWriter(response.getWriter());
        try {
          [DatabaseClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseClient.html) client = getClient();
          try ([ResultSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.ResultSet.html) rs =
              client
                  .[singleUse](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseClient.html#com_google_cloud_spanner_DatabaseClient_singleUse__)()
                  .executeQuery([Statement](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Statement.html).of("SELECT SingerId, AlbumId, AlbumTitle FROM Albums"))) {
            writer.printf("Albums:%n");
            while (rs.next()) {
              writer.printf(
                  "%d %d %s%n",
                  rs.getLong("SingerId"), rs.getLong("AlbumId"), rs.getString("AlbumTitle"));
            }
          } catch ([SpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerException.html) e) {
            writer.printf("Error querying database: %s%n", e.getMessage());
            response.[setStatusCode](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpResponseException.Builder.html#com_google_api_client_http_HttpResponseException_Builder_setStatusCode_int_)([HttpStatusCodes](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpStatusCodes.html).STATUS_CODE_SERVER_ERROR, e.getMessage());
          }
        } catch (Throwable t) {
          logger.log(Level.SEVERE, "Spanner example failed", t);
          writer.printf("Error setting up Spanner: %s%n", t.getMessage());
          response.[setStatusCode](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpResponseException.Builder.html#com_google_api_client_http_HttpResponseException_Builder_setStatusCode_int_)([HttpStatusCodes](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpStatusCodes.html).STATUS_CODE_SERVER_ERROR, t.getMessage());
        }
      }
    }

### Node.js

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const {Spanner} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    
    // Imports the functions framework to register your HTTP function
    const functions = require('@google-cloud/functions-framework');
    
    // Instantiates a client
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)();
    
    // Your Cloud Spanner instance ID
    const instanceId = 'test-instance';
    
    // Your Cloud Spanner database ID
    const databaseId = 'example-db';
    
    /**
     * HTTP Cloud Function.
     *
     * @param {Object} req Cloud Function request context.
     * @param {Object} res Cloud Function response context.
     */
    functions.http('spannerQuickstart', async (req, res) => {
      // Gets a reference to a Cloud Spanner instance and database
      const instance = spanner.instance(instanceId);
      const database = instance.database(databaseId);
    
      // The query to execute
      const query = {
        sql: 'SELECT * FROM Albums',
      };
    
      // Execute the query
      try {
        const results = await database.run(query);
        const rows = results[0].map(row => row.toJSON());
        rows.forEach(row => {
          res.write(
            `SingerId: ${row.SingerId}, ` +
              `AlbumId: ${row.AlbumId}, ` +
              `AlbumTitle: ${row.AlbumTitle}\n`
          );
        });
        res.status(200).end();
      } catch (err) {
        res.status(500).send(`Error querying Spanner: ${err}`);
      }
    });

### Python

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import functions_framework
    from google.cloud import [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html)
    
    instance_id = "test-instance"
    database_id = "example-db"
    
    client = [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html).[Client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html)()
    instance = [client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html#google_cloud_spanner_v1_client_Client_instance)(instance_id)
    database = instance.database(database_id)
    
    
    @functions_framework.http
    def spanner_read_data(request):
        query = "SELECT * FROM Albums"
    
        outputs = []
        with database.snapshot() as snapshot:
            results = snapshot.execute_sql(query)
    
            for row in results:
                output = "SingerId: {}, AlbumId: {}, AlbumTitle: {}".format(*row)
                outputs.append(output)
    
        return "\n".join(outputs)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudspanner). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
