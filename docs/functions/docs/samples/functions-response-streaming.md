---
url: https://docs.cloud.google.com/functions/docs/samples/functions-response-streaming/
title: Stream BigQuery query results \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:18.126327+00:00
---

# Stream BigQuery query results  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-response-streaming/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Stream BigQuery query results Stay organized with collections  Save and categorize content based on your preferences. 

This sample demonstrates how to stream the results of a BigQuery query using a Cloud Function.

## Code sample

### C#

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.BigQuery.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.html);
    using Google.Cloud.Functions.Framework;
    using Microsoft.AspNetCore.Http;
    using System;
    using System.Threading.Tasks;
    
    namespace StreamBigQuery;
    
    public class Function : IHttpFunction
    {
        public async Task HandleAsync(HttpContext context)
        {
            context.Response.ContentType = "text/plain";
            string projectId = Environment.GetEnvironmentVariable("GOOGLE_PROJECT_ID");
            [BigQueryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html) client = [BigQueryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html#Google_Cloud_BigQuery_V2_BigQueryClient_Create_System_String_Google_Apis_Auth_OAuth2_GoogleCredential_)(projectId).WithDefaultLocation([Locations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.Locations.html).[UnitedStates](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.Locations.html#Google_Cloud_BigQuery_V2_Locations_UnitedStates));
    
            // Example to retrieve a large payload from BigQuery public dataset.
            string query = "SELECT title FROM `bigquery-public-data.breathe.bioasq` LIMIT 1000";
            [BigQueryParameter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryParameter.html)[] parameters = null;
            [BigQueryResults](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryResults.html) results = await client.[ExecuteQueryAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html#Google_Cloud_BigQuery_V2_BigQueryClient_ExecuteQueryAsync_System_String_System_Collections_Generic_IEnumerable_Google_Cloud_BigQuery_V2_BigQueryParameter__Google_Cloud_BigQuery_V2_QueryOptions_Google_Cloud_BigQuery_V2_GetQueryResultsOptions_System_Threading_CancellationToken_)(query, parameters, cancellationToken: context.RequestAborted);
    
            // Stream out the payload response by iterating rows.
            foreach ([BigQueryRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryRow.html) row in results)
            {
                await context.Response.WriteAsync($"{row["title"]}\n", context.RequestAborted);
                // Artificially add a 50ms delay per line, just to make the streaming nature clearer
                // when viewing the results in a browser.
                await Task.Delay(50);
            }
        }
    }

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Package responsestreaming contains a function that streams out a large payload in chunks.
    package responsestreaming
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"log"
    	"net/http"
    	"os"
    
    	"cloud.google.com/go/bigquery"
    	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
    	"google.golang.org/api/iterator"
    )
    
    func init() {
    	functions.HTTP("streamBigQuery", streamBigQuery)
    }
    
    // streamBigQuery retrieves a large payload from BigQuery public dataset and streams its rows.
    func streamBigQuery(w http.ResponseWriter, r *http.Request) {
    	projectID := os.Getenv("GOOGLE_CLOUD_PROJECT")
    	if projectID == "" {
    		fmt.Println("GOOGLE_CLOUD_PROJECT environment variable must be set.")
    		os.Exit(1)
    	}
    	ctx := context.Background()
    	// Must include project ID in client.
    	client, err := bigquery.NewClient(ctx, projectID)
    	if err != nil {
    		log.Fatalf("bigquery.NewClient: %v", err)
    	}
    	defer client.Close()
    
    	// Run the query and ensure the job finishes without error.
    	rows, err := query(ctx, client)
    	if err != nil {
    		log.Fatal(err)
    	}
    
    	// Stream out the payload by iterating rows and flushing out the writer.
    	streamResults(w, rows)
    }
    
    // query returns a row iterator suitable for reading query results.
    func query(ctx context.Context, client *bigquery.Client) (*bigquery.[RowIterator](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_RowIterator), error) {
    	q := client.Query(
    		"SELECT abstract FROM `bigquery-public-data.breathe.bioasq` LIMIT 1000")
    	q.[Location](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_Job_Location) = "US"
    	return q.Read(ctx)
    }
    
    // streamResults streams results from a query of BigQuery's public dataset.
    func streamResults(w io.Writer, it *bigquery.[RowIterator](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_RowIterator)) {
    	for {
    		var row []bigquery.[Value](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_Value)
    		err := it.Next(&row)
    		if err == iterator.Done {
    			break
    		}
    		fmt.Fprintln(w, row[0])
    		if f, ok := w.(http.Flusher); ok {
    			f.Flush()
    			fmt.Fprintln(w, "Successfully flushed row")
    		}
    	}
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.bigquery.[BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html);
    import com.google.cloud.bigquery.[BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html);
    import com.google.cloud.bigquery.[BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html);
    import com.google.cloud.bigquery.[QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html);
    import com.google.cloud.bigquery.[TableResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult.html);
    import com.google.cloud.functions.HttpFunction;
    import com.google.cloud.functions.HttpRequest;
    import com.google.cloud.functions.HttpResponse;
    import java.io.BufferedWriter;
    import java.io.IOException;
    
    public class StreamBigQuery implements HttpFunction {
      @Override
      public void service(HttpRequest request, HttpResponse response) {
        String query = "SELECT abstract FROM `bigquery-public-data.breathe.bioasq` LIMIT 1000";
        streamQueryResult(query, response);
      }
    
      public static void streamQueryResult(String query, HttpResponse response) {
        try {
          BufferedWriter writer = response.getWriter();
          // Initialize client that will be used to send requests.
          // This client only needs to be created once,
          // and can be reused for multiple requests.
          [BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) bigquery = [BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html).getDefaultInstance().getService();
          [TableResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult.html) results = bigquery.[query](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_query_com_google_cloud_bigquery_QueryJobConfiguration_com_google_cloud_bigquery_BigQuery_JobOption____)([QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html).of(query));
    
          results.[iterateAll](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult.html#com_google_cloud_bigquery_TableResult_iterateAll__)().forEach(
              row -> row.forEach(val -> {
                try {
                  writer.write(val.getValue().toString() + "\n");
                  writer.flush();
                  System.out.println("Successfully flushed row");
                } catch (IOException e) {
                  System.out.println("Could not get rows: " + e.toString());
                }
              }));
        } catch ([BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html) | InterruptedException | IOException e) {
          System.out.println("Query not performed: " + e.toString());
        }
      }
    }

### PHP

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Psr\Http\Message\ServerRequestInterface;
    use Google\Cloud\BigQuery\BigQueryClient;
    
    function streamBigQuery(ServerRequestInterface $request)
    {
        // Provide the Cloud Project ID by setting env var.
        $projectId = getenv('GOOGLE_PROJECT_ID');
        // Example large payload from BigQuery's public dataset.
        $bigQuery = new BigQueryClient(['projectId' => $projectId]);
        $queryJobConfig = $bigQuery->query(
            'SELECT abstract FROM `bigquery-public-data.breathe.bioasq` LIMIT 1000'
        );
        $queryResults = $bigQuery->runQuery($queryJobConfig);
    
        // Stream out large payload by iterating rows and flushing output.
        foreach ($queryResults as $row) {
            foreach ($row as $column => $value) {
                printf('%s' . PHP_EOL, json_encode($value));
                flush();
            }
        }
        printf('Successfully streamed rows');
    }

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from flask import Response, stream_with_context
    
    import functions_framework
    from google.cloud import [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest)
    
    # Construct a BigQuery client object.
    client = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)()
    
    
    @functions_framework.http
    def stream_big_query_output(request):
        """HTTP Cloud Function.
        Args:
            request (flask.Request): The request object.
            <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
        Returns:
            The response text, or any set of values that can be turned into a
            Response object using `make_response`
            <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
        """
        # Example large query from public dataset
        query = """
        SELECT abstract
        FROM `bigquery-public-data.breathe.bioasq`
        LIMIT 1000
        """
        query_job = client.[query](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)(query)  # Make an API request.
    
        def generate():
            for row in query_job:
                yield row[0]
    
        return Response(stream_with_context(generate()))
    
    

### Ruby

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "functions_framework"
    require "google/cloud/bigquery"
    
    FunctionsFramework.http "stream_big_query" do |_request|
      # Provide the Project ID by setting the env variable or specifying directly.
      # project_id = "Your Google Cloud project ID"
      project_id = ENV["CLOUD_PROJECT_ID"]
      bigquery = Google::Cloud::[Bigquery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery.html) project: project_id
      # Example to retrieve a large payload from public BigQuery dataset.
      sql = "SELECT abstract FROM `bigquery-public-data.breathe.bioasq` LIMIT 1000"
    
      results = bigquery.query sql do |config|
        config.location = "US"
      end
    
      # Stream out the large payload by iterating rows.
      body = Enumerator.[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery.html) do |y|
        results.each do |row|
          y << "#{row}\n"
        end
      end
      [200, {}, body]
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
