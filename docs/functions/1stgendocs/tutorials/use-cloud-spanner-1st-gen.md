---
url: https://docs.cloud.google.com/functions/1stgendocs/tutorials/use-cloud-spanner-1st-gen/
title: Using Spanner with Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:33.604607+00:00
---

# Using Spanner with Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/tutorials/use-cloud-spanner-1st-gen/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback 

#  Using Spanner with Cloud Run functions (1st gen) Stay organized with collections  Save and categorize content based on your preferences. 

## Objectives

Write, deploy, and trigger an [HTTP Cloud Run function](https://docs.cloud.google.com/functions/1stgendocs/writing/write-http-functions) that accesses Spanner.

## Costs

This document uses Spanner and Cloud Run functions, which are billable components of Google Cloud.

  * For information on the cost of using Spanner, see [Spanner pricing](https://cloud.google.com/spanner/pricing).

  * For information on the cost of using Cloud Run functions, including free invocations, see [Cloud Run functions pricing](https://cloud.google.com/functions/pricing).




## Before you begin

  1. This document assumes you have a Spanner instance named `test-instance` and a database named `example-db` that uses the music application [schema](https://docs.cloud.google.com/spanner/docs/schema-and-data-model#creating-interleaved-tables). For instructions on creating an instance and database with the music application schema, see [Quickstart using the console](https://docs.cloud.google.com/spanner/docs/create-query-database-console) or the tutorials for Getting Started in [Go](https://docs.cloud.google.com/spanner/docs/getting-started/go), [Java](https://docs.cloud.google.com/spanner/docs/getting-started/java), [Node.js](https://docs.cloud.google.com/spanner/docs/getting-started/nodejs), or [Python](https://docs.cloud.google.com/spanner/docs/getting-started/python).

**Note:** After this step, you should have two tables, [`Singers`](https://docs.cloud.google.com/spanner/docs/schema-and-data-model#creating_a_table) and [`Albums`](https://docs.cloud.google.com/spanner/docs/schema-and-data-model#creating_multiple_tables), in your database with the sample data specified in the music application schema.
  2. Enable the Cloud Run functions and Cloud Build APIs.

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudfunctions.googleapis.com,cloudbuild.googleapis.com)

  3. [Install and initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs).

If you already have the gcloud CLI installed, update it by running the following command:
         
         gcloud components update
         

  4. Prepare your development environment:

###  Node.js 

[ Go to the Node.js setup guide ](https://docs.cloud.google.com/nodejs/docs/setup)

###  Python 

[ Go to the Python setup guide ](https://docs.cloud.google.com/python/docs/setup)

###  Go 

[ Go to the Go setup guide ](https://docs.cloud.google.com/go/docs/setup)

###  Java 

[ Go to the Java setup guide ](https://docs.cloud.google.com/java/docs/setup)




## Prepare the application

  1. Clone the sample app repository to your local machine:

###  Node.js 
         
         git clone https://github.com/GoogleCloudPlatform/nodejs-docs-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/archive/main.zip) as a zip file and extract it. 

###  Python 
         
         git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/python-docs-samples/archive/main.zip) as a zip file and extract it. 

###  Go 
         
         git clone https://github.com/GoogleCloudPlatform/golang-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/golang-samples/archive/main.zip) as a zip file and extract it. 

###  Java 
         
         git clone https://github.com/GoogleCloudPlatform/java-docs-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/java-docs-samples/archive/main.zip) as a zip file and extract it. 

  2. Change to the directory that contains the Cloud Run functions sample code for accessing Spanner:

###  Node.js 
         
         cd nodejs-docs-samples/functions/spanner/

###  Python 
         
         cd python-docs-samples/functions/spanner/

###  Go 
         
         cd golang-samples/functions/spanner/

###  Java 
         
         cd java-docs-samples/functions/spanner/

  3. Take a look at the sample code:

###  Node.js 
         
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

###  Python 
         
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
         
         

###  Go 
         
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
         

###  Java 
         
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
                   [SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html).[getDefaultProjectId](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.connection.ConnectionOptions.html#com_google_cloud_spanner_connection_ConnectionOptions_getDefaultProjectId_com_google_auth_Credentials_)(),
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

The function sends a SQL query to fetch all `Albums` data from your database. The function executes when you make an HTTP request to the function's endpoint.




## Deploy the function

To deploy the function with an HTTP trigger, run the following command in the `spanner` directory:

###  Node.js 
    
    
    gcloud functions deploy get \
    --runtime nodejs22 --trigger-http

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Node.js version](https://docs.cloud.google.com/static/functions/docs/runtime-support#node.js) to run your function. 

###  Python 
    
    
    gcloud functions deploy spanner_read_data \
    --runtime python312 --trigger-http

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Python version](https://docs.cloud.google.com/functions/docs/runtime-support#python) to run your function. 

###  Go 
    
    
    gcloud functions deploy HelloSpanner \
    --runtime go121 --trigger-http

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Go version](https://docs.cloud.google.com/functions/docs/runtime-support#go) to run your function. 

###  Java 
    
    
    gcloud functions deploy java-spanner-function \
    --entry-point functions.HelloSpanner \
    --runtime java17 \
    --memory 512MB --trigger-http

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Java version](https://docs.cloud.google.com/functions/docs/runtime-support#java) to run your function. 

Function deployment might take up to two minutes.

Note the `url` value returned when your function finishes deploying. You will use it when you trigger the function.

You can view your deployed functions on the [Cloud Run functions](https://console.cloud.google.com/project/_/functions) page in the Google Cloud console. You can also create and edit functions on that page, and get details and diagnostics for your functions.

## Trigger the function

Make an HTTP request to your function:

###  Node.js 
    
    
    curl "https://REGION-PROJECT_ID.cloudfunctions.net/get" 

###  Python 
    
    
    curl "https://REGION-PROJECT_ID.cloudfunctions.net/spanner_read_data" 

###  Go 
    
    
    curl "https://REGION-PROJECT_ID.cloudfunctions.net/HelloSpanner" 

###  Java 
    
    
    curl "https://REGION-PROJECT_ID.cloudfunctions.net/java-spanner-function" 

where `REGION` and `PROJECT_ID` match the values that are visible in your terminal when your function finishes deploying. You should see output that shows the results of the SQL query, assuming you worked through a Getting Started [tutorial](https://docs.cloud.google.com/spanner/docs/tutorials) and populated the database:
    
    
    SingerId: 2, AlbumId: 2, AlbumTitle: Forever Hold Your Peace
    SingerId: 1, AlbumId: 2, AlbumTitle: Go, Go, Go
    SingerId: 2, AlbumId: 1, AlbumTitle: Green
    SingerId: 2, AlbumId: 3, AlbumTitle: Terrified
    SingerId: 1, AlbumId: 1, AlbumTitle: Total Junk
    

You can also visit the function's URL in your browser to see the result of your SQL query.

## Cleanup

To avoid incurring additional charges to your Google Cloud account for the Spanner and Cloud Run functions resources used in this document, do the following:

  1. Delete the instance:
         
         gcloud spanner instances delete test-instance
         

  2. Delete the function that you deployed: 

###  Node.js 
         
         gcloud functions delete get 

###  Python 
         
         gcloud functions delete spanner_read_data 

###  Go 
         
         gcloud functions delete HelloSpanner 

###  Java 
         
         gcloud functions delete java-spanner-function 




## What's next

  * [Learn more about writing Cloud Run functions](https://docs.cloud.google.com/functions/1stgendocs/writing).
  * [Learn more about deploying Cloud Run functions](https://docs.cloud.google.com/functions/1stgendocs/deploy).
  * [Learn more about calling Cloud Run functions](https://docs.cloud.google.com/functions/1stgendocs/calling).
  * [Learn more about monitoring Cloud Run functions](https://docs.cloud.google.com/functions/1stgendocs/monitoring).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
